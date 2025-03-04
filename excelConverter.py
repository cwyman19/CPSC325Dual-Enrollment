import openpyxl

# Load the workbook
workbook = openpyxl.load_workbook('2024-25CTEArticulations 3.xlsx')

# Get the sheet by name or index
sheet = workbook['Sheet1']  # Replace 'Sheet1' with your sheet name
# sheet = workbook.active # To get the active sheet

data_list = []
for row in sheet.iter_rows(values_only=True):
    data_list.append(list(row))
# print(data_list[2][0])
# # Now data_list contains all rows as lists
# print(data_list)

# print(data_list[2])