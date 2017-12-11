#! python3
# lucky.py - Opens several Google search results.

import requests, sys, webbrowser


# Retrieve top search result links.

# Open a browser tab from each link.
'''
Open all links on a page in separate browser tabs.

Open the browser to the URL for your local weather.

Open several social network sites that you regularly check.
'''
linkElems = ['http://www.cnblogs.com/jinxulin/p/3526542.html',
             'https://classroom.udacity.com/nanodegrees/nd009/parts/9777e610-ebeb-4c49-b502-88c692489ae3'
             ,'https://github.com/diyjac/smartcab/blob/master/smartcab.ipynb']
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open(linkElems[i])