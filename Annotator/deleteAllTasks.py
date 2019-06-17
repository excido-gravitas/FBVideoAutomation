import requests
from tqdm import tqdm
import pickle
# First set up server api variables
server = 'http://localhost:8080'
api = '/api/v1'
tasks = '/tasks'
users = '/users'
auth = ('<YOUR USERNAME>', '<YOUR PASSWORD>')

fileObject = open("nameToIDMap",'rb')
nameToIDMap = pickle.load(fileObject)


for taskName in tqdm(nameToIDMap.keys()):
	requests.delete(server + api + tasks + "/" + str(nameToIDMap[taskName]), auth = auth)

fileObject = open("nameToIDMap",'wb') 
# this writes the object a to the
# file named 'testfile'
pickle.dump({},fileObject)   
# here we close the fileObject
fileObject.close()




