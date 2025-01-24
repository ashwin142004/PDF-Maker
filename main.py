from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv('topics.csv')

def footer():
        pdf.set_y(-10)
        pdf.set_font('Times', 'I', 8)
        pdf.cell(0, 10, f'{row["Topic"]}', 0, 0, 'R')

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family = "Times", style = "B", size = 24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w = 0, h = 12, txt = row['Topic'], border = 0, ln = 1, align = 'L')
    pdf.line(x1 = 10, y1 = 20, x2 = 200, y2 = 20)

    pdf.set_draw_color(80, 80, 80)

    for lines in range(30, 285, 10):
        pdf.line(x1 = 10, y1 = lines, x2 = 200, y2 = lines)

    # lines = 30
    # while lines < 285:
    #     pdf.line(x1 = 10, y1 = lines, x2 = 200, y2 = lines)
    #     lines += 10

    footer()
    
    for pg_no in range(row['Pages'] - 1):
        pdf.add_page()
        pdf.set_draw_color(80, 80, 80)
        
        for lines in range(10, 285, 10):
            pdf.line(x1 = 10, y1 = lines, x2 = 200, y2 = lines)

        # lines = 10
        # while lines < 285:
        #     pdf.line(x1 = 10, y1 = lines, x2 = 200, y2 = lines)
        #     lines += 10
        footer()

pdf.output('output.pdf')
