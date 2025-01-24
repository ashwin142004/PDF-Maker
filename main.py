from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4')

pdf.add_page()

pdf.set_font(family = "Times", style = "B", size = 16)
pdf.cell(w = 0, h = 12, txt = "Hello World", border = 1, ln = 1, align = 'C')
pdf.cell(w = 0, h = 12, txt = "Hello There", border = 1, ln = 1, align = 'C')


pdf.output('output.pdf')
