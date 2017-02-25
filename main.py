import facebook
import urllib.request
import os
from tqdm import tqdm
from pprint import pprint

''' 
- todo -
1) get friends id (x)
2) get friends pic (x)
3) preprocess pictures ( )
4) get friends likes ( )
5) preprocess entire data ( )
6) train CNN model ( )
7) make simple web app ( )
'''


access_token = open('access_token.txt', 'r').read()


def get_friend_ids(graph, profile='me'):
	friends = graph.get_connections(id=profile, connection_name='friends')
	friends = friends['data']
	ids = [friend['id'] for friend in friends]
	return ids

def get_images(ids):
	if not os.path.isdir('images/'): 
		os.makedirs('images/')
		os.chdir('images/')
		for id in tqdm(ids):
			url = 'http://graph.facebook.com/' + id + '/picture?width=128&height=128'
			filename = id + '.jpg'
			urllib.request.urlretrieve(url, filename)

def prepare_dataset():
	pass

# main
graph = facebook.GraphAPI(access_token=access_token)
ids = get_friend_ids(graph)
print(len(ids))
get_images(ids)
