from pymongo import MongoClient

my_client = MongoClient("mongodb://localhost:27017/")

##몽고db와 연결이 잘 되었나 확인하는 데이터베이스 test 코드. 
print(my_client.list_database_names())


mydb = my_client['test']
mycol = mydb['customers']

my_dict = [{"name":"PUTTY", "address":"SSH World, Network"},
           {"name":"donghyunjang", "address":"Seoul, Korea"},
           {"name":"Avengers", "address":"Avengers Team Building, USA"}]

x = mycol.insert_many(my_dict)
print(x.inserted_ids)

##지우기
