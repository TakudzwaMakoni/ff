#glyph
import glyph as g #test mode: testglyph

g.bessie()
def main():
    #g.checkforimagline()
    importmode = g.getimportedfile()
    spacingsettings = ('y', 1)#g.getspacingopt()
    characterspacing = spacingsettings[0]
    linespacing = spacingsettings[1]
    if importmode != True:
        g.typewriter(g.getimportedfile)
    count = g.createmessageimage(
        g.translatemessage(characterspacing),
        linespacing
    )
    g.cleanup( count )
main()

