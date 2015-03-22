import wikipedia as wiki
from random import randint
text = "india,indian"
results = wiki.search(text,25,False)
pge = ""
title = ""
url = ""
content = ""
if len(results) > 0:
	topics = results
	#suggestions = results[1]
	index = topics[randint(0, len(topics)-1)]
	pge = wiki.page(index)
	title = pge.title
	url = pge.url
	content = pge.content
print len(topics)," results found!"
#print results
print topics
print url
print title
print content
