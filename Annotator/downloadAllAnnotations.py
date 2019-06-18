import requests
import pickle
from tqdm import tqdm
from config import config
# First set up server api variables


server = 'http://localhost:8080'
api = '/api/v1'
tasks = '/tasks'
users = '/users'
auth = (config["user"], config["password"])

fileObject = open("nameToIDMap",'rb')
nameToIDMap = pickle.load(fileObject)

for taskName in tqdm(nameToIDMap.keys()):
	taskId = nameToIDMap[taskName]

	response = requests.get("http://localhost:8080/api/v1/tasks/{0}/annotations/{0}_{1}?format=api".format(taskId, taskName), auth = auth)
	response = requests.get("http://localhost:8080/api/v1/tasks/{0}/annotations/{0}_{1}".format(taskId, taskName), auth = auth)
	response = requests.get("http://localhost:8080/api/v1/tasks/{0}/annotations/{0}_{1}?action=download".format(taskId, taskName), auth = auth)
	# print(response.text)

	file = open("./annotations" + "/{0}.xml".format(taskName.split(".")[0]), "w")
	file.write(response.text)
	file.close()

fileObject.close()






