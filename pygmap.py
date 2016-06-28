#/!usr/bin/python

import webbrowser, sys

if len(sys.argv) >1:
    #get address from command line
    address = ''.join(sys.argv[1:])

webbrowser.open('https://www.google.com/maps/place/'+ address)
