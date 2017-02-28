import facebook
import urllib.request
import os
from tqdm import tqdm
import numpy as np
import scipy
from scipy import ndimage

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
			url = 'http://graph.facebook.com/' + id + '/picture?width=256&height=256'
			filename = id + '.jpg'
			urllib.request.urlretrieve(url, filename)

def process_images(filename='images'):
    image_files = os.listdir(filename)
    # dataset = np.ndarray(shape=(len(image_files), 128, 128, 3), dtype=np.float32)
    image_list = []
    num_images = 0
    for image in tqdm(image_files):
        if '.jpg' in image:
            image_file = os.path.join(filename+'/', image)
            image_data = ((ndimage.imread(fname=image_file)))
            image_data = scipy.misc.imresize(image_data, (128, 128))
    #         print(image_file, '', image_data.shape)
            if len(image_data.shape) is 2:
                print("Skipping", image)
            else:
                # dataset[num_images, :, :] = image_data
                image_list.append(image_data)
                num_images += 1
    return np.array(image_list)

# main
graph = facebook.GraphAPI(access_token=access_token)
ids = get_friend_ids(graph)
get_images(ids)
dataset = process_images()

