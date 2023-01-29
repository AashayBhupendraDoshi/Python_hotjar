import requests
import numpy as np
from sklearn.utils import shuffle
from template_data import sparce_template, dense_template


URL = 'http://127.0.0.1:8000/'


def post_data(x):
    rx = requests.post(URL + 'post', json={'x': x[0], 'y': x[1]})
    return rx.json()


def get_all_data():
    rx = requests.get(URL + 'all_data')
    # print(x, x.text, type(x.text))
    # print(x.json())
    x = []
    y = []
    id = []
    for i in rx.json():
        x.append(i['x'])
        y.append(i['y'])
        id.append(i['cluster_id'])
    return np.array([x,y,id]).T



def classify_data(x):

    rx = requests.post(URL + 'classify', json={'x': x[0], 'y': x[1]})
    return rx.json()




x, y = dense_template()
x, y = shuffle(x.T, y)
print(x.shape, y.shape)
for i in x[:1160]:
    post_data(i)

# payload = [0.6, 0.4]
# print(post_data(payload))
# print(classify_data(payload))
# print(get_all_data().shape)
