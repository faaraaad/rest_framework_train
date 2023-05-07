import pymongo
def get_cursor(host, port):
    return pymongo.MongoClient('127.0.0.1', 27018)