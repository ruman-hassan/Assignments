import cairo
import math
def draw_curve(contxt):
    contxt.arc(150, 75, 25, math.pi/2, math.pi)
    contxt.arc(100, 75, 25, 0*math.pi,math.pi/2 )
    contxt.arc(100, 125, 25, 3*math.pi/2,0*math.pi )
    contxt.arc(150, 125, 25, math.pi, 3*math.pi/2)

    #contxt.arc(300, 75, 25, math.pi/2, math.pi)
    #contxt.arc(250, 75, 25, 0*math.pi,math.pi/2 )
    #contxt.arc(250, 125, 25, 3*math.pi/2,0*math.pi )
    #contxt.arc(300, 125, 25, math.pi, 3*math.pi/2)

    contxt.arc(300, 300, 25, math.pi/2, math.pi)
    contxt.arc(250, 300, 25, 0*math.pi,math.pi/2 )
    contxt.arc(250, 350, 25, 3*math.pi/2,0*math.pi )
    contxt.arc(300, 350, 25, math.pi, 3*math.pi/2)

    #contxt.arc(150, 300, 25, math.pi/2, math.pi)
    #contxt.arc(100, 300, 25, 0*math.pi,math.pi/2 )
    #contxt.arc(100, 350, 25, 3*math.pi/2,0*math.pi )
    #contxt.arc(150, 350, 25, math.pi, 3*math.pi/2)

    contxt.set_source_rgb(1, 0, 0)
    contxt.set_line_width(4)
    contxt.stroke()