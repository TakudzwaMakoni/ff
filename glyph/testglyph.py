import os,re
import PIL.Image as I


imdb = ['glyphs/space.png', 'glyphs/la1.png', 'glyphs/lb.png', 'glyphs/lc.png', 'glyphs/ld.png', 'glyphs/le1.png',
        'glyphs/lf.png', 'glyphs/lg.png', 'glyphs/lh.png', 'glyphs/li1.png', 'glyphs/lj.png',
        'glyphs/lk.png','glyphs/ll.png','glyphs/lm.png', 'glyphs/ln.png', 'glyphs/lo1.png','glyphs/lp.png', 17, 18, 19, 20, 21,
        22, 23, 24, 25, 26, 'glyphs/ca1.png','glyphs/cb.png', 'glyphs/cc.png', 'glyphs/cd.png', 'glyphs/ce1.png',
        'glyphs/cf.png', 'glyphs/cg.png', 'glyphs/ch.png', 'glyphs/ci1.png', 'glyphs/cj.png', 'glyphs/ck.png',
        'glyphs/cl.png', 'glyphs/cm.png', 'glyphs/cn.png', 'glyphs/co1.png', 'glyphs/cp.png', 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
        'glyphs/la2.png', 'glyphs/le2.png', 'glyphs/li2.png', 56, 57, 58, 59, 60, 61,
        'glyphs/ca2.png', 'glyphs/ce2.png', 'glyphs/ci2.png', 65, 64, 67, 68, 69, 70, 'glyphs/stop.png',
        'glyphs/comma.png', 73, 74, 75, 76, 77, 78, 79]
imdb2 = ['newglyphs/1.png','newglyphs/2.png','newglyphs/3.png','newglyphs/4.png','newglyphs/5.png','newglyphs/6.png','newglyphs/7.png','newglyphs/8.png',
         'newglyphs/9.png','newglyphs/10.png','newglyphs/11.png','newglyphs/12.png','newglyphs/13.png','newglyphs/14.png','newglyphs/15.png','newglyphs/16.png',
         'newglyphs/17.png','newglyphs/18.png','newglyphs/19.png','newglyphs/20.png','newglyphs/21.png','newglyphs/22.png','newglyphs/23.png','newglyphs/24.png',
         'newglyphs/25.png','newglyphs/26.png','newglyphs/27.png','newglyphs/28.png','newglyphs/29.png','newglyphs/0.png']



def bessie():
    print('\n')
    print(" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * \n\n        glyph 1.0.0   freedomfighter (ff), Milli group (c).    \n                                 2017-2018                   \n                         Written in Python 3.6 by            \n                             Takudzwa Makoni                 \n\n     GitHub: https://github.com/Millisoft/freedomfighter     \n\n                              \n\n * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * \n" )
    print('\n')




#cleanup will automatically remove the generated imagelines
#once they have been used to make the final image.
#It will also ask the user if they want to keep the message imageline.txt
def cleanup(count):
    for i in range(count):
        os.remove('line'+str(i)+'.png')


#will ask the user if they want to add character spacing, and what to
#set the linespacing to
def getspacingopt():
    cont = 'y'
    while cont == 'y':
        spcopt = input('add character spacing? (y/n) ')
        linespacing = int(input('enter line spacing '))
        if spcopt == 'y':
            return spcopt, linespacing
        elif spcopt == 'n':
            return spcopt, linespacing
        elif spcopt == '.quit':
            print('exiting program')
            exit(1)
        else:
            print('invalid entry')
            cont = 'y'

#add characters between list or string
def intersperse(lst, item):
    result = [item] * (len(lst) * 2 - 1)
    result[0::2] = lst
    return result

#find and replace (for words). the same function can be modified for
#numbers abover 9
def frw(string):
    a = [('ch','x'),('th','q'),('sh','c')]
    for ch in a:
        if ch[0] in string:
            string = string.replace(ch[0],ch[1])
    return string
#will read the message in imageline.txt character by character and
#produce an ordered list of imagefiles containing symbols to  translate
#the message
def translate(message,database=imdb2):
    nmessage = frw(message)
    a = list(nmessage)
    b = ['--' if x==' ' else x for x in a]
    c = intersperse(b,' ')
    dict1 ={"--":"glyphs/space.png"," ":"glyphs/smallspace.png","1":database[0],"2":database[1],"3":database[2],"4":database[3],"5":database[4],"6":database[5],"7":database[6],"8":database[7],"9":database[8],"10":database[9],"11":database[10],"12":database[11],"13":database[12],"14":database[13],"15":database[14],"16":database[15],"17":database[16],"18":database[17],"19":database[18],"20":database[19],"21":database[20],"22":database[21],"23":database[22],"24":database[23],"25":database[24],"26":database[25],"27":database[26],"28":database[27],"29":database[28]}
    imagelist = ["glyphs/smallspace.png" if ch == "\n" else dict1[ch] for ch in c]
    return imagelist

#checks if there already is a message 'imageline.txt' and
#asks the user if they want to continue with that on or overwrite it
def checkforimagline():
    cont = 'y'
    while cont == 'y':
        if os.path.isfile('imageline.txt'):
            usercommand = input("message already exists in 'imageline.txt' file. enter 'ow' to overwrite, or 'ap' to append to. ")
            if usercommand == 'ap':
                cont = 'n'
            elif usercommand == 'ow':
                os.remove('imageline.txt')
                cont = 'n'
            else:
                print('invalid entry.')
                cont = 'y'
        else:
            cont = 'n'


def getimportedfile():
    filename = input('enter file name (.txt) ')
    f1 = open('imageline.txt', 'w')
    f2 = open(filename,'r')
    lines = f2.readlines()
    
    for i in lines:
        f1.write(i)
    f1.close()
    f2.close()
    print('the file "' + filename + '" was imported')





#allows the user to type line by line the message to be saved
#to imageline.txt
def typewriter():
    print("info: enter '|end' on a new line to end entry any time.")
    while True:
        with open('imageline.txt', 'a') as f1:
            message = input("insert message ")
            if message == '|end':
                f1.close()
                break
            elif message == '|import':
                f1.close()
                getimportedfile()
                break
            elif message == '|Hspace':
                Hspacing()
            elif message == '|Vspace':
                Vspacing()
            else:
                f1.write(message + '\n')
        f1.close()

#opens the imageline.txt file and reads it line by line.
#the translate function will then be performed onto each line
#it then pruduces a list containing lists of the imagefiles for each translated line, which is the
#returned translated message
def translatemessage(addspaces='n'):
    f2  = open('imageline.txt', 'r')
    file = f2.readlines()
    translatedmessage = []
    for line in file:
        translatedline = translate(line)
        if addspaces == 'y':
            intersperse(translatedline,'glyphs/smallspace.png')
        translatedmessage.append(translatedline)
    return translatedmessage

#the image is created using the translated message returned by the translatemessage
#function, done by attaching symbol images horizontally to create each line, then attaching the lines vertically
def createmessageimage(listoftranslatedlines, numspaces):
    count = 0
    imlist = []
    for line in listoftranslatedlines:
        images = list(map(I.open, line))
        imflip = []
        for i in images:
            new = i.transpose(I.FLIP_LEFT_RIGHT)
            imflip.append(new)
        widths, heights = zip(*(i.size for i in imflip))
        total_width = sum(widths)
        max_height = max(heights)
        new_im = I.new('RGB', (total_width, max_height), 'white')
        x_offset = 0
        for im in imflip:
            new_im.paste(im, ( x_offset ,0))
            x_offset += im.size[0]
        new_im.save('line'+ str(count) + '.png')
        imlist.append('line'+ str(count) + '.png')
        count += 1
    
    #### modifications for reversal
    
    
    newlinespace = 'glyphs/newlinespace.png'
    count = len(imlist)
    iterative = 1
    for i in range(count):
        for x in range(numspaces):
            imlist.insert(i + iterative, newlinespace)
        iterative += numspaces
    
    
    finalimages = list(map(I.open, imlist))

    imrevf = []
    for i in reversed(finalimages):
        imrevf.append(i)
        widths, heights = zip(*(i.size for i in imrevf))
        max_width = max(widths)
        total_height = sum(heights)
        new_im = I.new('RGB', (max_width, total_height), 'white')
        y_offset = 0
        for im in imrevf:
            new_im.paste(im, (0, y_offset))
            y_offset += im.size[1]
    msg = new_im.transpose(I.FLIP_LEFT_RIGHT)
    saveask = input('save file? (y/n) ')
    if saveask != 'n':
        saveasask = input('save image file as: ')
        msg.save(saveasask +'.png')
    return count


