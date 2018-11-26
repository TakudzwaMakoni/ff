import PIL.Image as I

unit_length = 4
canvas_size = 1000
canvas = I.new('RGB', (canvas_size, canvas_size), 'white')
new_im = I.new('RGB', (unit_length, unit_length), '#052208')

offset = 0
for i in range(10):
    canvas.paste(new_im, ( offset , offset))
    canvas.paste(new_im, ( unit_length + offset , offset))
    canvas.paste(new_im, ( offset , unit_length + offset))
    offset += unit_length

canvas.save('test.png')
