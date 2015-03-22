from flask import Response
from wikiserver import wikiserver as server
import wikiserver.wikidata as datahelper
import json

# default route
@server.route('/')
def fulldata():
	results = datahelper.get_wiki_data()
	data = {}
	if len(results)>0:
		data = {'status':'success','results':results}
	else:
		data = {'status':'failed'}
	js = json.dumps(data)
	resp = Response(js, status=200, mimetype='application/json')
	return resp
