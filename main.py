import shelve
import pyperclip
import sys
# see here
# main.pyw - saves and copies content of clipboard
# basically a clipboard thingy
# how to use?
# three args or 2 args on the command line.
# usage: py.exe mcb.pyw save <keyword> => clipboard saved
#       py.exe mcb.pyw <kw> => copied
#       py.exe mcb.pyw list => all the KWs are copied

shelfFile = shelve.open('mcb')


# saving new file into the clipboard

if(len(sys.argv) == 3) and sys.argv[1].lower() == 'save':
    if sys.argv[2].lower() == 'all':
        print('this word has a special meaning so you can\' really just use this.')
        sys.exit()
    else:
        key = sys.argv[2].lower()
        shelfFile[key] = pyperclip.paste()

        # for saved file
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        copyList = list(shelfFile.keys())
        print(copyList)
    else:
        key = sys.argv[1].lower()
        if key in shelfFile:
            pyperclip.copy((shelfFile[key]))
        else:
            print('sorry no idea what you searching for')

# deleting files in the clipboard:
elif (len(sys.argv) == 3) and sys.argv[1].lower() == 'delete':
    if sys.argv[2].lower() == 'all':
        for key in list(shelfFile.keys()):
            del shelfFile[key]
    else:
        key = sys.argv[2].lower()
        if key in list(shelfFile.keys()):
            del shelfFile[key]
        else:
            print('no content found saved on that name')
shelfFile.close()
