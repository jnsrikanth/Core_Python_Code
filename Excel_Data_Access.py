#Accessing Data in Python from an Excel File
import openpyxl
excel_document = openpyxl.load_workbook('sample.xlsx')

# This command below will give you the names of the Sheets available in the Excel
# file
excel_document.get_sheet_names()

#The command below will allow us to access a sheet from a Workbook with multiple
#sheets via name 
#We can further access data by indexing into the sheet by the standard cell naming
#notation used in Excel as shown below.

sheet = excel_document.get_sheet_by_name('Sheet1')
print sheet['A2'].value

#If we want to access multiple cells from an Excel Sheet, we can do so as below
# by specifying a Cell Range "'A1':'B3'" and printing using a for loop

multiple_cells = sheet['A1':'B3']
for row in multiple_cells:
    for cell in row:
        print cell.value

#In order to access all rows inside and Excel Sheet, please use the below method.
all_rows = sheet.rows
print all_rows[:]

#Accessing all columns would be as follows...
all_columns = sheet.columns
print all_columns[:]

