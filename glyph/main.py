#glyph
import testglyph as g #test mode: testglyph

g.bessie()
def main():
    #g.checkforimagline()
    g.getimportedfile()
    spacingsettings = ('n', 1)#g.getspacingopt()
    characterspacing = spacingsettings[0]
    linespacing = spacingsettings[1]
    g.typewriter()
    count = g.createmessageimage(
        g.translatemessage(characterspacing),
        linespacing
    )
    g.cleanup( count )
main()

