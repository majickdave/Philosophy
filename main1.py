from bs4 import BeautifulSoup
import urllib2
from unidecode import unidecode
import uuid

BASE = "https://en.wikipedia.org"
starter = "/wiki/Mahatma_Gandhi"
# CRAWLER
paths = []
def crawler(URL):

	solved = False
	hops = 0


	page = urllib2.urlopen(URL).read()
	html = BeautifulSoup(page, "html.parser")
	
	ID = uuid.uuid4()
	path = URL.rpartition("""/""")[2]
	paths.append((path, ID))
	
	if unidecode(html.find(id="firstHeading").get_text()) == "Philosophy":
		import pdb; pdb.set_trace()
		return (paths, hops)

	links = html.p.find_all("a")
	#import pdb; pdb.set_trace()
	URLs = [unidecode(x.get('href')) for x in links]
	
	for url in URLs:
		#import pdb; pdb.set_trace()
		if url != '/wiki/'+ path and url[:5] == '/wiki':
			#import pdb; pdb.set_trace()
			
			print url
			hops += 1
			return crawler(BASE+url)
		

	

	
		
		



print crawler(BASE+starter)