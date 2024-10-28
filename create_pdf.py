from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


def new_pdf(texto, output_pdf):
    c = canvas.Canvas(output_pdf, pagesize=letter)
    width, height = letter

    lines = texto.split('\n')
    y_position = height - 40  # posición inicial desde el margen superior

    max_width = 500  # límite de ancho para cada línea
    font_size = 12
    line_spacing = 20  # espacio entre líneas

    for line in lines:
        while line:
            # Encuentra el punto de corte más cercano que no exceda el ancho
            line_width = c.stringWidth(line, 'Helvetica', font_size)
            if line_width > max_width:
                # Corta la línea en la cantidad de caracteres que caben
                cut_index = 1
                while c.stringWidth(line[:cut_index], 'Helvetica', font_size) < max_width:
                    cut_index += 1
                cut_index -= 1  # ajusta para evitar sobrepasar el límite

                # Dibuja la parte de la línea que cabe
                c.drawString(40, y_position, line[:cut_index])
                line = line[cut_index:]  # resto de la línea a procesar
            else:
                # Dibuja la línea completa si cabe dentro del ancho permitido
                c.drawString(40, y_position, line)
                line = ""  # vacía la línea para salir del bucle

            # Ajusta la posición vertical
            y_position -= line_spacing

            # Salta a la nueva página si el espacio vertical es insuficiente
            if y_position < 40:
                c.showPage()
                y_position = height - 40

    c.save()
