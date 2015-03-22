import wikipedia as wiki
from random import randint

def get_wiki_data():
	text = "india*"
	results = wiki.search(text,5,False)
	page = ""
	title = ""
	url = ""
	content = ""
	topics = []
	if len(results) > 0:
		for x in results:
			page = wiki.page(x)
			title = page.title
			url = page.url
			content = page.content
			topics.append({'url':url,'title':title,'content':content})
	return topics
