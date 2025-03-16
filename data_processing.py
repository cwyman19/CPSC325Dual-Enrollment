'''
Data Processing for dual enrollment data
uses MyPyTable objects
'''
import pandas as pd
import numpy as np

#my_raw_dataset = MyPyTable().load_from_file("input_data/Dual-Enrollment-Data.csv")

# my_raw_dataset.pretty_print()
# print("column names: ", my_dataset.column_names)
header = ["College", "College District", "Articulation", "College Program", "Career Cluster", "College Course", "College Course Name", 
          "College Credits", "College Course CIP Code", "College Course Description", "High School", "HS Course Name", "HS Course CIP Code", 
          "HS Course Credits", "Academic Years", "HS Course Description", "Type of Credit", "Status of Articulation"]
#my_cleaned_dataset = MyPyTable(column_names=header)


'''
count = 0
for row in my_raw_dataset.data:
    new_row = [f"\"{row}\","]
    my_cleaned_dataset.data.append(new_row)
    count += 1

my_cleaned_dataset.pretty_print()
my_cleaned_dataset.save_to_file("input_data/Dual-Enrollment-Data-Cleaned.csv")
'''


file_path = 'input_data/Dual-Enrollment-Data.csv'

# Read the CSV file into a DataFrame
# df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
# print(df.head())
#series = pd.Series
#pops_dict = {"WA": washington, "ID": idaho, "OR": oregon}   # washington, idaho, and oregon are lists
#df2 = pd.DataFrame(pops_dict)
#print(df2)
header = ["College", "College District", "Articulation", "College Program", "Career Cluster", "College Course", "College Course Name", 
          "College Credits", "College Course CIP Code", "College Course Description", "High School", "HS Course Name", "HS Course CIP Code", 
          "HS Course Credits", "HS Course Description", "Academic Years", "Type of Credit", "Status of Articulation"]
# Existing DataFrame
'''
df = pd.DataFrame({
    'College': [np.nan],
    'College District': [np.nan],
    'Articulation': ["Computer Application Essentials (Empowering Your Future)"],
    'College Program': [np.nan],
    'Career Cluster': [np.nan],
    'College Course': ["Computer Application Essentials INFO 101"],
    'College Course Name': [np.nan],
    'College Credits': [np.nan],
    'College Course CIP Code': [np.nan],
    'College Course Description': ["Provides students with foundational knowledge and skills in using essential computer software applications. The course covers key areas such as word processing, spreadsheets, and presentation software, along with an introduction to digital literacy, file management, and internet research. Students will develop practical, hands-on experience to enhance productivity and efficiency in academic, professional, and personal tasks."],
    'High School': [np.nan],
    'HS Course Name': ["Empowering Your Future CTB104 [Computer App Essentials]"],
    'HS Course CIP Code': [np.nan],
    'HS Course Credits': [np.nan],
    'HS Course Description': ["Introduces students to fundamental computer skills necessary for academic and professional success. The course covers essential software applications, including word processing, spreadsheets, and presentations, while emphasizing digital literacy, problem-solving, and productivity tools. Students will develop practical skills to efficiently use technology in everyday tasks and enhance their ability to communicate and collaborate in a digital world."],
    'Academic Years': [np.nan],
    'Type of Credit': [np.nan],
    'Status of Articulation': [np.nan]
})

# New row to add (as DataFrame)
#new_row = pd.DataFrame({'A': [4], 'B': [7]})

# Concatenate the new row to the original DataFrame
#df = pd.concat([df, new_row], ignore_index=True)

# Print the updated DataFrame
print(df)
df.to_csv("output_data.csv")
'''

input_filename = input("What is the filename of the input data? (must be a csv format) ")

input_df = pd.read_csv(f"input_data/{input_filename}")
old_df = pd.read_csv("output_data/output_course_data.csv")

for i in range(len(input_df)):
    new_row = input_df.iloc[i]
    new_row = new_row.to_numpy()
    #print("new row: ", new_row)
    old_df.loc[-1] = new_row
    old_df.index = old_df.index + 1
    

print("new dataframe: ")
print(old_df)
old_df.to_csv("output_data/output_course_data.csv", index=False)
#print(input_df)
#print(new_df)
new_row_indeces = {"College": 0, "College District": 1, "Articulation": 2, "College Program": 3, "Career Cluster": 4, "College Course": 5, "College Course Name": 6, 
          "College Credits": 7, "College Course CIP Code": 8, "College Course Description": 9, "High School": 10, "HS Course Name": 11, "HS Course CIP Code": 12, 
          "HS Course Credits": 13, "HS Course Description": 14, "Academic Years": 15, "Type of Credit": 16, "Status of Articulation": 17}

#new_df.loc[-1] = ["Everett", np.nan, "Computer Science", np.nan, np.nan, "SOFT 101", "Introduction to Information Technology [Computer Science]", 
#          np.nan, np.nan, "Introduces students to the fundamentals of information technology, including computer hardware, software, networks, and basic problem-solving techniques in IT.", np.nan, "AP Computer Science Principles A [Computer Science]", np.nan, 
#          np.nan, "Focuses on the foundational principles of computer science, including algorithms, programming, and problem-solving with a focus on digital technology's impact on society.", np.nan, np.nan, np.nan]
#new_df.index = new_df.index + 1
#new_df.sort_index()
#print(" --------------------------- ")
#print("new dataframe + new row: ")
#print(new_df)

#new_df.to_csv("output_data2.csv", index=False)
# TODO: concatenate college course name and college course number together if both fields are filled (for algorithm).

