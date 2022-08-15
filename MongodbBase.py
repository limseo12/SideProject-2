from pymongo import MongoClient
import certifi
import toptrack
from toptrack import toptrack_results

client = MongoClient('localhost', port = 27017)

HOST = 'cluster0.iqmnw.mongodb.net'
USER = 'Lim'
PASSWORD = '04130413'
DATABASE_NAME = 'spotifydata'
COLLECTION_NAME = 'spotifydata'
MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"

##toptrack.py의 main
toptrack.main()
##list형태를 dictionary로 변경
dictionary = {string : i for i,string in enumerate(toptrack_results)}

##dictionary 확인
##print(dictionary)

##mongoDB저장
tlsCAFile=certifi.where()
client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())
# client = MongoClient(MONGO_URI)
database = client[DATABASE_NAME]
collection = database[COLLECTION_NAME]
collection.insert_one(dictionary)
