from PIL import Image, ImageDraw
import time

def mandelbrot(c,MAX_ITER):
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z**2 + c
        n += 1
    return n


def drawImg(iterator):

    MAX_ITER = iterator

    # Image size (pixels)
    WIDTH = 1920 * 40
    HEIGHT = 1080 * 40

    # Plot window
    RE_START = -2
    RE_END = 1
    IM_START = -1
    IM_END = 1

    im = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0))
    draw = ImageDraw.Draw(im)

    for x in range(0, WIDTH):
        for y in range(0, HEIGHT):
            # Convert pixel coordinate to complex number
            c = complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
                        IM_START + (y / HEIGHT) * (IM_END - IM_START))
            # Compute the number of iterations
            m = mandelbrot(c,MAX_ITER)
            # The colour depends on the number of iterations m = count
            colour = 255 - int(m * 255 / MAX_ITER)
            # Plot the point
            draw.point([x, y], (colour, colour, colour))   #   more iterations => darker colour

    # im.save(str(iterator)+' iterations'+'.png', 'PNG')
    im.save('a40 times large - 50 iter.png', 'PNG')


start = 100
current = start
maximum = 100

##while current <= maximum:
##    drawImg(current)
##    current += 10


start_time = time.time()

drawImg(50) # 50 iterations

end_time = time.time()

print(end_time - start_time)
