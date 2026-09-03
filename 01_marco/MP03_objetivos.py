import pdfplumber, re, pandas as pd

def objetivos(ruta, patrones):
    encontrados = []
    with pdfplumber.open(ruta) as pdf:
        for n, p in enumerate(pdf.pages, 1):
            t = p.extract_text() or ""
            for pat in patrones:
                for m in re.finditer(pat, t):
                    encontrados.append({"pagina": n, "codigo": m.group(1).strip(),
                                        "texto": m.group(2).strip()[:180]})
    return pd.DataFrame(encontrados).drop_duplicates(subset=["codigo"])

PAT_PEI = [r"(OEI\s*\.?\s*\d+)\s*[:.\-]?\s*(.{20,200})",
           r"(AEI\s*\.?\s*[\d.]+)\s*[:.\-]?\s*(.{20,200})"]
PAT_PGD = [r"(O\.?\s?G\.?D\.?\s*\d+|OGD\s*\d+|Objetivo\s+\d+)\s*[:.\-]?\s*(.{20,200})"]

obj_pei = objetivos("../evidencias/PEI.pdf", PAT_PEI)
obj_pgd = objetivos("../evidencias/PGD.pdf", PAT_PGD)
obj_pei.to_csv("MP03_objetivos_pei.csv", index=False)
obj_pgd.to_csv("MP03_objetivos_pgd.csv", index=False)
print(f"Objetivos identificados — PEI: {len(obj_pei)} | PGD: {len(obj_pgd)}")
print(obj_pei.to_string(index=False)); print(obj_pgd.to_string(index=False))
