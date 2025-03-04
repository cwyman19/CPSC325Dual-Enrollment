from sentence_transformers import SentenceTransformer
import openpyxl

# Load the workbook
workbook = openpyxl.load_workbook('2024-25CTEArticulations 3.xlsx')

# Get the sheet by name or index
sheet = workbook['Sheet1']  # Replace 'Sheet1' with your sheet name
# sheet = workbook.active # To get the active sheet

input_course_name = input("Enter HS Course Name: ")
input_course_description = input("Enter a brief course description: ")

data_list = []
for row in sheet.iter_rows(values_only=True):
    data_list.append(list(row))

# 1. Load a pretrained Sentence Transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")
filename = "output.txt"
f = open(filename, "a")

similar_instances = []
similar_instance_course_names = []
num_similar = 0
test = 0
count = [0,0,0,0,0]
averageValue = [0, 0, 0, 0, 0]
for row in data_list[2:50]:
    sentences = [
    row[0],
    row[1],
    row[2],
    row[3],
    row[4],
    input_course_name,
    input_course_description
    ]

    
    embeddings = model.encode(sentences)
    print(embeddings.shape)
    # [3, 384]

    # 3. Calculate the embedding similarities
    similarities = model.similarity(embeddings, embeddings)
    print(similarities)
    for x in range (0, 5): 
        new_item = similarities[x]
        for y in range (0, 5):
            if (y != x):
               count[y] = count[y] + 1
               test = test + new_item[y].item()
               averageValue[y] = averageValue[y] + new_item[y].item() 
            
    if ((similarities[0][5] >= 0.6) or (similarities[6][4] >= 0.6)):
        if sentences[2] not in similar_instance_course_names:
            print("SIMILAR!! ---------")
            similar_instances.append(similarities)
            similar_instance_course_names.append(sentences[2])
            num_similar += 1
        else:
            print("Duplicate course (Skipped)")
    
    print("t", test)
    # f.write(similarities)
    # tensor([[1.0000, 0.6660, 0.1046],
    #         [0.6660, 1.0000, 0.1411],
    #         [0.1046, 0.1411, 1.0000]])
f.close()
test 
# The sentences to encode
sentences = [
    "Computer Application Essentials (Empoweing Your Future)",
    "Empowering Your Future CTB104 [Computer App Essntials]",
    "Computer Application Essentials INFO 101",
    "Empowering Your Future CTB104 (Computer Application Essentials) introduces students to fundamental computer skills necessary for academic and professional success. The course covers essential software applications, including word processing, spreadsheets, and presentations, while emphasizing digital literacy, problem-solving, and productivity tools. Students will develop practical skills to efficiently use technology in everyday tasks and enhance their ability to communicate and collaborate in a digital world.",
    "Computer Application Essentials INFO 101 provides students with foundational knowledge and skills in using essential computer software applications. The course covers key areas such as word processing, spreadsheets, and presentation software, along with an introduction to digital literacy, file management, and internet research. Students will develop practical, hands-on experience to enhance productivity and efficiency in academic, professional, and personal tasks.",
    "Empowering Your Future CTB104 [Computer App Essntials]",
    "Empowering Your Future CTB104 (Computer Application Essentials) introduces students to fundamental computer skills necessary for academic and professional success. The course covers essential software applications, including word processing, spreadsheets, and presentations, while emphasizing digital literacy, problem-solving, and productivity tools. Students will develop practical skills to efficiently use technology in everyday tasks and enhance their ability to communicate and collaborate in a digital world."
]

print(averageValue)
print("Articulation", "High School Classes", "College Courses", "High School Course Description", "College Course Description", "New HS Course", "New HS Course Description")
averageTest = ["Articulation", "High School Classes", "College Courses", "High School Course Description", "College Course Description"]
for x in range(len(averageValue)):
    print("x: ", x)
    print(averageTest[x])
    print(averageValue[x])
    print(count[x])
    #print("average test [0][x]", averageTest[0][x])
    averageTest[x] = averageValue[x]/count[x]
# 2. Calculate embeddings by calling model.encode()
embeddings = model.encode(sentences)
print("embeddings: ", embeddings.shape)
# [5, 384]




# 3. Calculate the embedding similarities
similarities = model.similarity(embeddings, embeddings)
print("Articulation", "High School Classes", "College Courses", "High School Course Description", "College Course Description")
print("similarities: ", similarities)
print("--------------------------------------------------------------------------------")
print("Similar College Courses: ")
for i in similar_instance_course_names:
    print(i)
    print()
print()
print("Amount of similar instances: ", num_similar)
print("Similar Instances: ")
print(similar_instances)


#"Articulation", "High School Classes", "College Courses", "High School Course Description", "College Course Description"
# tensor ([[1.0000, 0.5124, 0.7984, 0.6900, 0.6815],
#        [0.5124, 1.0000, 0.4456, 0.6866, 0.3996],
#        [0.7984, 0.4456, 1.0000, 0.6800, 0.8325],
#        [0.6900, 0.6866, 0.6800, 1.0000, 0.7487],
#        [0.6815, 0.3996, 0.8325, 0.7487, 1.0000]])

# Notable outcomes: 
    # College Course Description to College Course Name - 0.8325 Similarity
    # College Course Description to High School Course Description - 0.7487 Similarity
    # High School Course Descrption to College Course Name - only 0.3996 similarity
    