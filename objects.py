import cairo


#Setting up the interface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

ctx.move_to(100, 100)
ctx.line_to(200, 100)
ctx.line_to(150, 200)
ctx.line_to(50, 150)
ctx.close_path()
ctx.set_source_rgb(1, 0, 1)
ctx.fill()





