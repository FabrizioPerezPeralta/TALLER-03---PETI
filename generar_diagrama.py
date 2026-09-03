from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs('graficos', exist_ok=True)

width, height = 800, 700
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)

try:
    font = ImageFont.truetype("arial.ttf", 16)
    font_bold = ImageFont.truetype("arialbd.ttf", 16)
except:
    font = ImageFont.load_default()
    font_bold = font

def draw_box(draw, text, x, y, w, h, fill='white', outline='black', width_line=2, is_bold=False):
    draw.rectangle([x, y, x+w, y+h], fill=fill, outline=outline, width=width_line)
    f = font_bold if is_bold else font
    # Calculate text position
    lines = text.split('\n')
    total_h = sum(draw.textbbox((0, 0), line, font=f)[3] - draw.textbbox((0, 0), line, font=f)[1] for line in lines) + 5 * (len(lines)-1)
    
    current_y = y + (h - total_h) / 2
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=f)
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]
        draw.text((x + (w - text_w)/2, current_y), line, fill='black', font=f)
        current_y += text_h + 5

def draw_arrow(draw, x, y1, y2):
    draw.line([x, y1, x, y2], fill='black', width=2)
    draw.polygon([x, y2, x-6, y2-12, x+6, y2-12], fill='black')

texts = [
    "Política Nacional de Transformación Digital al 2030\n(D.S. 085-2023-PCM)",
    "PESEM del Sector Economía y Finanzas (MEF)",
    "Plan Estratégico Institucional (PEI)\n(Vigente hasta 2030)",
    "Plan Operativo Institucional (POI)\n(Año 2024)"
]

peti_text = "PETI / Plan de Gobierno Digital 2025 - 2027\n\nSe articula al OEI.01: Mejorar el cumplimiento tributario y aduanero"

center_x = width // 2
box_w, box_h = 500, 70
start_y = 50
gap = 40

for i, t in enumerate(texts):
    y = start_y + i * (box_h + gap)
    draw_box(draw, t, center_x - box_w//2, y, box_w, box_h, fill='#E8F1FB', outline='#16285C')
    draw_arrow(draw, center_x, y + box_h, y + box_h + gap)

y_peti = start_y + len(texts) * (box_h + gap)
draw_box(draw, peti_text, center_x - box_w//2 - 20, y_peti, box_w + 40, box_h + 30, fill='#FFF2CC', outline='#D6B656', width_line=3, is_bold=True)

image.save('graficos/mapa_instrumentos.png')
print("Imagen generada exitosamente.")
