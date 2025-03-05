from sentence_transformers import SentenceTransformer
import openpyxl

# Load the workbook
workbook = openpyxl.load_workbook('2024-25CTEArticulations 3.xlsx')

# Get the sheet by name or index
sheet = workbook['Sheet1']  # Replace 'Sheet1' with your sheet name
# sheet = workbook.active # To get the active sheet



data_list = []
for row in sheet.iter_rows(values_only=True):
    data_list.append(list(row))

# 1. Load a pretrained Sentence Transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")
filename = "output.txt"
f = open(filename, "a")
input_course_name = input("Enter HS Course Name: ")
input_course_description = input("Enter a brief course description: ")

instances_list = [] # [course name similarity, course description similarity, course name, course desc]
course_name_similarities = []
course_desc_similarities = []
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
    
    if sentences[2] not in similar_instance_course_names:
        instances_list.append([similarities[0][5], similarities[6][4], sentences[2], sentences[4]])
        course_name_similarities.append(similarities[0][5])
        course_desc_similarities.append(similarities[6][4])
        similar_instance_course_names.append(sentences[2])
    

            
    #if ((similarities[0][5] >= 0.6) or (similarities[6][4] >= 0.6)):
    #    if sentences[2] not in similar_instance_course_names:
    #        print("SIMILAR!! ---------")
    #        similar_instances.append(similarities)
    #        similar_instance_course_names.append(sentences[2])
    #        num_similar += 1
    #    else:
    #        print("Duplicate course (Skipped)")
    
    print("t", test)
    # f.write(similarities)
    # tensor([[1.0000, 0.6660, 0.1046],
    #         [0.6660, 1.0000, 0.1411],
    #         [0.1046, 0.1411, 1.0000]])

most_similar_courses = []
print("Instances list: ")
print(instances_list)
for i in range(0, 3):
    most_similar_name = max(course_name_similarities)
    most_similar_desc = max(course_desc_similarities)
    print("most similar name: ", most_similar_name)
    print("most similar desc: ", most_similar_desc)
    instance_index = 0
    if most_similar_name > most_similar_desc:
        for j in range(len(instances_list)):
            print("j: ", j)
            #print("name instance: ", instances_list[j][0], "  ideal name instance: ", most_similar_name)
            if (instances_list[j][0] == most_similar_name):
                most_similar_courses.append(instances_list[j])
                instance_index = j
                print("POP")
                if (instances_list[j][1] == most_similar_desc):
                    course_desc_similarities.remove(most_similar_desc)
        instances_list.pop(instance_index)
        course_name_similarities.remove(most_similar_name)

    else:
        for j in range(len(instances_list)):
            print("j: ", j)
            #print("course desc instance: ", instances_list[j][0], "  ideal course desc instance: ", most_similar_desc)
            if (instances_list[j][1] == most_similar_desc):
                most_similar_courses.append(instances_list[j])
                instance_index = j
                print("POP")
                if (instances_list[j][0] == most_similar_name):
                    course_name_similarities.remove(most_similar_name)
        instances_list.pop(instance_index)
        course_desc_similarities.remove(most_similar_desc)



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
count = 1
for i in most_similar_courses:
    print(f"{count}. ", i[2])
    print()
    count += 1
print()
user_input = input("Would you like to see course descriptions for these courses? Y/N ")
print()
count = 1
if (user_input == 'y') or (user_input == 'Y'):
    for i in most_similar_courses:
        print(f"{count}. ", i[2], ": ", i[3])
        print()
        count += 1
print()

#print("Similar Instances: ")
#print(similar_instances)


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
    