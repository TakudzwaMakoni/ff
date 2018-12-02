import PIL.Image as I
import subprocess, os

def bessie(title, version, repo, company, year, language, author, git ):
    print('\n')
    print(" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * \n\n        {} {},   {}, {}.    \n                                 {}                   \n                         Written in {} by            \n                             {}                 \n\n           github: {}     \n\n                              \n\n * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * \n".format(title, version, repo, company, year, language, author, git) )
    print('\n')
    subprocess.Popen(['afplay','-v', '0.075','trinkets/login.wav']) #run process in terminal (for terminal application) - is powerful.



def tartan( filename, SorR, pallet, unit_length=1, canvas_size=1000 ):
    canvas = I.new('RGB', (canvas_size, canvas_size), 'white')
    offset = 0
    if os.path.isfile(filename) == False:
        filename = 'threadcounts/' + filename
    
    with open(filename) as f:
        lines = f.readlines()
        count = 0
        for i in lines:
            numbers = i.split()[1]
            count += int(numbers)
    scale = (1000//count) + 1
    #print(scale)

    with open(filename) as f:
        halfsett = f.readlines()
        if SorR == 's':
            sett = halfsett + halfsett[::-1]
            for i in range(scale//2):
                sett.extend(sett)
        elif SorR == 'r':
            for i in range(scale):
                halfsett.extend(halfsett)
            sett = halfsett
        else:
            exit(1)

        for i in sett:
            pixel_data = [j for j in i.split()]
            pixel_colour, pixel_size = pallet[pixel_data[0]], int(pixel_data[1])
            pixel = I.new('RGB', (unit_length * pixel_size, unit_length * pixel_size), pixel_colour)
            m_pixel = I.new('RGB', ( unit_length, unit_length ), pixel_colour)
        
            offset2 = offset
            for j in range(pixel_size):
                x_offset_diverge = offset
                y_offset_diverge = offset
                for i in range(1000):
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
    name = input('save as (png): ')
    canvas.save('patterns/' + name + '.png')
    pattern = I.open('patterns/' + name + '.png')
    pattern.show()


