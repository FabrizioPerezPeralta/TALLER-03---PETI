import pdfplumber
import sys

def read_first_page(file_path):
    print(f"--- Leyendo {file_path} ---")
    try:
        with pdfplumber.open(file_path) as pdf:
            print(f"Total de páginas: {len(pdf.pages)}")
            first_page = pdf.pages[0]
            print(first_page.extract_text()[:500])
    except Exception as e:
        print(f"Error leyendo el PDF: {e}")
    print("\n")

read_first_page("000301-2024.pdf")
read_first_page("000395-2025.pdf")
