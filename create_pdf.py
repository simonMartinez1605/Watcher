import ocrmypdf

def new_pdf (input_pdf,output_pdf): 
    ocrmypdf.ocr(
        input_pdf, 
        output_pdf, 
        skip_text=True
    )