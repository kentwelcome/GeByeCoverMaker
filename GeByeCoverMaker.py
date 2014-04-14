#!/usr/bin/python 
# -*- coding: utf-8 -*-
import os
import sys
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

CoverWide = 851
CoverTall = 315

geByeTemplate = u"自己的{thing}自己{action}"

def showUsage(argv):
    print "usage: python {py} Action Thing".format(py=argv[0])
    pass

def main(argv):
    if len(argv) != 3:
        showUsage(argv)
        return
    else:
        geByeAction = argv[1].decode('utf-8')
        geByeThing = argv[2].decode('utf-8')

    # Init GeBye Image
    img = Image.new("RGB", (CoverWide, CoverTall), "black")
    font = ImageFont.truetype(os.path.join("font","GeByeFont.otf"), 52)
    draw = ImageDraw.Draw(img)
    
    # Generate GeBye String
    geByeText = geByeTemplate.format(thing=geByeThing,
                                     action=geByeAction)
    print u"Create GeByeCover: {GeByeText}".format(GeByeText=geByeText).encode('utf-8')

    # Start to draw GeByeCover
    geByeSize = font.getsize(geByeText)
    geByeLocation = ((CoverWide-geByeSize[0])/2, (CoverTall-geByeSize[1])/2)
    draw.text(geByeLocation,geByeText,(255,255,255),font=font)
    
    # Save image file
    img.save("GeByeCover.png", "PNG")
    pass

if __name__ == '__main__':
    main(sys.argv)
    os.system("open GeByeCover.png")
