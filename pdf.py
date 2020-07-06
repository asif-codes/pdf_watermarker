import PyPDF2
import sys

# get the arguments from the command line

watermark_pdf = sys.argv[1]
template_pdf = sys.argv[2]
output_pdf = sys.argv[3]

# create a function for watermarking the pdf


def watermark(watermark_pdf, template_pdf, output_pdf):
    watermark_file = PyPDF2.PdfFileReader(open(watermark_pdf, 'rb'))
    template_file = PyPDF2.PdfFileReader(open(template_pdf, 'rb'))
    output = PyPDF2.PdfFileWriter()
    for page_num in range(template_file.getNumPages()):
        page = template_file.getPage(page_num)
        page.mergePage(watermark_file.getPage(0))
        output.addPage(page)
    with open(output_pdf, 'wb') as file:
        output.write(file)


watermark(watermark_pdf, template_pdf, output_pdf)
