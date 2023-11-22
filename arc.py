import cairo


def draw(n: int):
    """This function takes a variable n of type int and recursively draws a complex
    shape out of it. This shape is created using cubic bezier curves
    """
    context.move_to(100, 30)
    context.line_to(100, 100)
    end = 100
    for x in range(n):
        m = 100 * x
        context.curve_to(m + 250, 50, m + 50, 50, m + 200, 100)
        end = m + 200
    context.line_to(end, 30)
        
    context.close_path()
    context.set_source_rgb(1, 0, 0)
    context.set_line_width(10)
    context.stroke()

# Create a PyCairo surface and context
width, height = 500, 500
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
context = cairo.Context(surface)


draw(4)
surface.write_to_png("replicated_curves.png")
surface.finish()
