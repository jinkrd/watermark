import PyPDF2

template=PyPDF2.PdfFileReader(open('super.pdf','rb'))
wmark=PyPDF2.PdfFileReader(open('wtr.pdf','rb'))
output=PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
	page=template.getPage(i)
	page.mergePage(wmark.getPage(0))
	output.addPage(page)
	

with open('wmarked_op.pdf','wb')as file:
	output.write(file)