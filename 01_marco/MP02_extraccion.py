import pdfplumber, re, pandas as pd

def estructura(ruta, patron_titulo=r"^\s*(\d+(?:\.\d+)*)\s+([A-ZÁÉÍÓÚÑ][^\n]{4,90})$"):
    """Extrae el índice real del documento a partir de sus encabezados numerados."""
    filas = []
    with pdfplumber.open(ruta) as pdf:
        for n, pagina in enumerate(pdf.pages, 1):
            texto = pagina.extract_text() or ""
            for linea in texto.split("\n"):
                m = re.match(patron_titulo, linea.strip())
                if m:
                    filas.append({"pagina": n, "numeral": m.group(1),
                                  "titulo": m.group(2).strip(),
                                  "nivel": m.group(1).count(".") + 1})
    return pd.DataFrame(filas).drop_duplicates(subset=["numeral","titulo"])

pei = estructura("../evidencias/PEI.pdf")
pgd = estructura("../evidencias/PGD.pdf")
pei.to_csv("MP02_estructura_pei.csv", index=False)
pgd.to_csv("MP02_estructura_pgd.csv", index=False)
print("=== ESTRUCTURA DEL PEI ===\n", pei[pei.nivel <= 2].to_string(index=False))
print("\n=== ESTRUCTURA DEL PGD ===\n", pgd[pgd.nivel <= 2].to_string(index=False))
