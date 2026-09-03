import pdfplumber

with pdfplumber.open('evidencias/PGD.pdf') as pdf:
    text = ""
    for i in range(62, 72):
        if i < len(pdf.pages):
            page_text = pdf.pages[i].extract_text()
            if page_text:
                text += f"\n--- PAGINA {i+1} ---\n" + page_text
                
with open('extracted_text_utf8.txt', 'w', encoding='utf-8') as f:
    f.write(text)
