#! python3
# lucky.py - Opens several Google search results.

import requests, sys, webbrowser, bs4

print('Googling...') # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))

try:
	res.raise_for_status()
except Exception as exc:
	print ('there is error: %s'%exc)

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text,"lxml")


# Open a browser tab for each result.
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))


'''
Open all the product pages after searching a shopping site such as Amazon
Open all the links to reviews for a single product
Open the result links to photos after performing a search on a photo site such as Flickr or Imgur
 '''