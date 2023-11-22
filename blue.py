import cairo
import math

def draw_line(contxt):

    contxt.move_to(100, 300)
    contxt.line_to(200, 200)
    #for circle
    contxt.move_to(300, 150)
    contxt.line_to(300, 250)

    contxt.move_to(250, 200)
    contxt.line_to(350, 200)
    
    

    contxt.move_to(500, 300)
    contxt.line_to(300, 500)
    #for right angled tri
    contxt.move_to(250, 50)
    contxt.line_to(250, 100)
    contxt.line_to(400, 100)
    contxt.close_path()
    #for right angled tri2
    contxt.move_to(250, 100)
    contxt.line_to(400, 100)
    contxt.line_to(400, 150)
    contxt.close_path()

    contxt.set_source_rgb(0, 0, 1)
    contxt.set_line_width(10)
    contxt.stroke()