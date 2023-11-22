import cairo
import blue
#import colour
import arc
import bezier
import test

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

test.draw_curve(ctx)
#colour.draw_curve(ctx)
#arc.draw_arc(ctx)
#bezier.draw_curve(ctx)

surface.write_to_png("trialcard.png")