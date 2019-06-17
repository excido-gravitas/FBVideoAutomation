import requests
import pickle
from tqdm import tqdm
# First set up server api variables
server = 'http://localhost:8080'
api = '/api/v1'
tasks = '/tasks'
users = '/users'
auth = ('tejas', 'teja322985')

# # get all files mounted on share
# req = server + api + '/server/share?directory=/'
# response = requests.get(req, auth=auth)
# # print(response.json())
# print('shared file get result: {}'.format(response))
# shared_fnames = [ res['name'] for res in response.json() if res['name'] != '.DS_Store']
# print(shared_fnames)


# for fname in shared_fnames:
#     create_task_data = {
#         "name": fname,
#         "assignee": 2,
#         "overlap": 0,
#         "z_order": False,
#         "image_quality": 95,
#         "labels": [{"name": "mainPlate"}, {"name": "otherPlate"}],
#     }

#     # create tasks
#     req = server + api + tasks
#     response = requests.post(req, json=create_task_data, auth=auth)
#     print('task create response: {}'.format(response))

#     print(response.json())
 
#     # send data to task
#     task_id = response.json()['id']
#     data = {'server_files[0]': fname}
#     req = server + api +tasks + f'/{task_id}/data'
#     print("task data request: {}".format(req))
#     response = requests.post(req, data=data, auth=auth)
#     print("task data response: {}".format(response))


# response = requests.get("http://localhost:8080/api/v1/tasks/31/data", auth = auth)
# /api/v1/tasks/37/annotations/37_1.mov?format=api
# response = requests.delete("http://localhost:8080/api/v1/tasks/39", auth = auth)
# print(response)

fileObject = open("nameToIDMap",'rb')
nameToIDMap = pickle.load(fileObject)

for taskName in tqdm(nameToIDMap.keys()):
	taskId = nameToIDMap[taskName]

	response = requests.get("http://localhost:8080/api/v1/tasks/{0}/annotations/{0}_{1}?format=api".format(taskId, taskName), auth = auth)
	response = requests.get("http://localhost:8080/api/v1/tasks/{0}/annotations/{0}_{1}".format(taskId, taskName), auth = auth)
	response = requests.get("http://localhost:8080/api/v1/tasks/{0}/annotations/{0}_{1}?action=download".format(taskId, taskName), auth = auth)
	# print(response.url)

	file = open("./annotations" + "/{0}.xml".format(taskName.split(".")[0]), "w")
	file.write(response.text)
	file.close()

fileObject.close()






