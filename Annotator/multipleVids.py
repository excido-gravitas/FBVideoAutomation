import requests
# First set up server api variables
server = 'http://localhost:8080'
api = '/api/v1'
tasks = '/tasks'
users = '/users'
auth = ('tejas', 'teja322985')

# get all files mounted on share
req = server + api + '/server/share?directory=/'
response = requests.get(req, auth=auth)
# print(response.json())
print('shared file get result: {}'.format(response))
shared_fnames = [ res['name'] for res in response.json() if res['name'] != '.DS_Store']
print(shared_fnames)


for fname in shared_fnames:
    create_task_data = {
        "name": fname,
        "assignee": 2,
        "overlap": 0,
        "segment_size": 500,
        "z_order": False,
        "image_quality": 95,
        "labels": [{"name": "plate"}]
    }

    # create tasks
    req = server + api + tasks
    response = requests.post(req, json=create_task_data, auth=auth)
    print('task create response: {}'.format(response))

    print(response.json())
 
    # send data to task
    task_id = response.json()['id']
    data = {'server_files[0]': fname}
    req = server + api +tasks + f'/{task_id}/data'
    print("task data request: {}".format(req))
    response = requests.post(req, data=data, auth=auth)
    print("task data response: {}".format(response))