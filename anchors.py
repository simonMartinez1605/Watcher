import pytesseract
from pdf2image import convert_from_path
from PIL import Image
from models.type import bc_name, form, case_I_797C

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def anchors(pdf): 

    pages = convert_from_path(pdf)

    print("Revisando el documento...")

    for item in pages: 
        datos_ocr = pytesseract.image_to_data(item, output_type=pytesseract.Output.DICT)

        case_type = form(datos_ocr, item) 

        if case_type == True:
            return case_I_797C(datos_ocr, item)
        else: 
            return bc_name(datos_ocr, item)     