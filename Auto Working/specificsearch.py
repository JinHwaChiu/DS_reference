#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

import webbrowser, sys
#pyperclip

address = ' '.join(sys.argv[1:])
'''
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()
'''
webbrowser.open('https://www.youtube.com/results?search_query='+ address)


#https://www.youtube.com/results?search_query=