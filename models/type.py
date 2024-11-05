import pytesseract

def form(datos_ocr, item): 
    for i, palabra in enumerate(datos_ocr['text']): 
        if palabra == "Applicant": 
            x,y,w,h = datos_ocr['left'][i], datos_ocr['top'][i], datos_ocr['width'][i], datos_ocr['height'][i]

            region_x = x + 340
            region_y = max(0, y -300) 
            region_w = 110
            region_h = 50

            region = item.crop((region_x, region_y, region_x + region_w, region_y + region_h))

            text = pytesseract.image_to_string(region)
            print(f"Tipo de documento: {text}")

            if "I-797C" in text: 
                return True  
            else: 
                return False
        
datos = [] 

def case_I_797C(datos_ocr, item): 

     print("Extrayendo informacion...")
     for i, palabra in enumerate(datos_ocr['text']): 
        if palabra == "Applicant": 
            x,y,w,h = datos_ocr['left'][i], datos_ocr['top'][i], datos_ocr['width'][i], datos_ocr['height'][i]

            #Obtener nombre 
            region_x = x 
            region_y = y + 15
            region_w = 400
            region_h = 30

            region = item.crop((region_x, region_y, region_x + region_w, region_y + region_h))

            new_text = pytesseract.image_to_string(region)
            format_text = new_text.replace("\n", "")
            datos.append(format_text)

            #Obtener Alien Number 

            region_x = x + 70 #<----->
            region_y = y - 5
            region_w = 180
            region_h = 30

            region = item.crop((region_x, region_y, region_x + region_w, region_y + region_h))

            text = pytesseract.image_to_string(region)
            format_text = text.replace("\n", "") 

            datos.append(format_text) 

            print(datos) 
            return datos
 
        
def bc_name (datos_ocr, item): 
    for i, palabra in enumerate(datos_ocr['text']): 
            if palabra == "Sexo:" or palabra == 'Sexo': 

                x,y,w,h = datos_ocr['left'][i], datos_ocr['top'][i], datos_ocr['width'][i], datos_ocr['height'][i]

                region_x = x - 42
                region_y = max(0, y - 195)
                region_w = 1700
                region_h = 50

                region = item.crop((region_x, region_y, region_x + region_w, region_y + region_h))

                text = pytesseract.image_to_string(region) 
                format_text = text.replace("\n", "")

                print(f"Nombre encontrado: {format_text}") 
                datos.append(format_text)

                return datos 