import pytesseract
from pdf2image import convert_from_path
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def anchors(pdf): 

    # Especifica la ruta completa a tesseract.exe

    pages = convert_from_path(pdf)

    for item in pages: 
        datos_ocr = pytesseract.image_to_data(item, output_type=pytesseract.Output.DICT)
        print("Revisando el documento...")

        for i, palabra in enumerate(datos_ocr['text']): 
            if palabra == "Sexo:" or palabra == 'Sexo': 

                x,y,w,h = datos_ocr['left'][i], datos_ocr['top'][i], datos_ocr['width'][i], datos_ocr['height'][i]

                region_x = x - 42
                region_y = max(0, y - 195)
                region_w = 1700 
                region_h = 50

                region = item.crop((region_x, region_y, region_x + region_w, region_y + region_h))

                final_txt = pytesseract.image_to_string(region) 

                print(f"Nombre encontrado: {final_txt}") 
                return final_txt 