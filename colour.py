import cairo
import math
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

ctx.arc(150, 75, 25, math.pi/2, math.pi)
ctx.arc(100, 75, 25, 0*math.pi,math.pi/2 )
ctx.arc(100, 125, 25, 3*math.pi/2,0*math.pi )
ctx.arc(150, 125, 25, math.pi, 3*math.pi/2)
ctx.close_path()


    
ctx.set_source_rgb(1, 0, 0)
ctx.set_line_width(4)
ctx.stroke()
ctx.fill()

surface.write_to_png("trial.png")
