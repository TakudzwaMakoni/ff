import PIL.Image as I

filename = input('filename: ') + '.txt'

with open(filename) as f:
    lines = f.readlines()
    count = 0
    for i in lines:
        numbers = i.split()[1]
        count += int(numbers)

unit_length = 2
canvas_size = 1000
canvas = I.new('RGB', (canvas_size, canvas_size), 'white')
pallet = {'HG':'#285800','K':'#101010','R':'#C80000','W':'#E0E0E0','Y':'#E8C000', 'LN':'#C0C0C0','TK':'#8C7038','RB':'#0C585C','DR':'#880000','GO':'#FFD700','MB':'#3474FC','RC':'#5C5C5C','BB':'#14283C','EG':'#004028'}
offset = 0

with open(filename) as f:
    halfsett = f.readlines()
    sett = halfsett + halfsett[::-1]
    for i in sett:
        pixel_data = [j for j in i.split()]
        pixel_colour, pixel_size = pallet[pixel_data[0]], int(pixel_data[1])
        pixel = I.new('RGB', (unit_length * pixel_size, unit_length * pixel_size), pixel_colour)
        m_pixel = I.new('RGB', ( unit_length, unit_length ), pixel_colour)
        
        offset2 = offset
        for j in range(pixel_size):
            x_offset_diverge = offset
            y_offset_diverge = offset
            for i in range(700):
                canvas.paste( m_pixel, (x_offset_diverge + j, offset2 ) )
                canvas.paste( m_pixel, (offset2,y_offset_diverge + j) )
                y_offset_diverge += unit_length #2*(( (-1)**j) +1 ) * unit_length  #  was 2*
                x_offset_diverge += unit_length  # was 2 *
            offset2 += unit_length
        
        offset2 = offset
        for j in range(pixel_size):
            x_offset_diverge = offset
            y_offset_diverge = offset
            for i in range(700):
                canvas.paste( m_pixel, (x_offset_diverge + j, offset2 ) )
                canvas.paste( m_pixel, (offset2,y_offset_diverge + j) )
                y_offset_diverge +=  -2 * unit_length #2*(( (-1)**j) +1 ) * unit_length  #  was 2*
                x_offset_diverge += -2 * unit_length  # was 2 *
            offset2 += unit_length
    
        canvas.paste(pixel, ( offset , offset))
        canvas.paste(pixel, ( unit_length + offset , offset)) #horizontal paste
        canvas.paste(pixel, ( offset , unit_length + offset)) #vertical paste
        
        offset += unit_length * pixel_size
canvas.save('test.png')
