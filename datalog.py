import xlsxwriter

# Workbook() takes one, non-optional, argument
# which is the filename that we want to create.
workbook = xlsxwriter.Workbook('hello.xlsx')

# The workbook object is then used to add new
# worksheet via the add_worksheet() method.
worksheet = workbook.add_worksheet()

# Use the worksheet object to write
# data via the write() method.

worksheet.write('A1', 'Name')
worksheet.write('B1', 'Phone No')
worksheet.write('C1', 'Place')
worksheet.write('D1', 'Body Temp')

a = input('enter the name')
b = input('enter the phone no')
c = input('Place of origin')
d = float(input('Body Temp'))
worksheet.write('A2', a)
worksheet.write('B2', b)
worksheet.write('C2', c)
worksheet.write('D2', d)

# Finally, close the Excel file
# via the close() method.
workbook.close()
