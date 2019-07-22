import xlsxwriter
#创建文件     Workbook 大写！！
workbook=xlsxwriter.Workbook("demo.xlsx")
#添加工作表
worksheet = workbook.add_worksheet()

worksheet.write("A1","我要自学网")
worksheet.write("A2","Python教程")

#关闭文件 必须关闭，否则没有表格
workbook.close()