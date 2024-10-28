import pytesseract
from PIL import Image 

# Especifica la ruta completa al ejecutable de Tesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Carga la imagen
img = Image.open("C:/Users/Isack Munoz/Pictures/nasa/NASA Tophat Girls Classic.pdf")

# Realiza OCR en la imagen y extrae el texto
texto = pytesseract.image_to_string(img) 

# Imprime el texto extraído
print(texto)