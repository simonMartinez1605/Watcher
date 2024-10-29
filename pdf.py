import  pytesseract
from pdf2image import convert_from_path


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def pdf_reader(pdf_path):
    pages = convert_from_path(pdf_path, dpi=300)

    for i, page in enumerate(pages): 
        texto = pytesseract.image_to_string(page, lang='spa')
        texto_total = ""
        texto_total += f"\n\n--- Página {i+1} ---\n\n" + texto

    
    return texto_total 
    
#Toca instalar Poppler y colocarlo dentro de las variables de entorno para que se pueda leer como 