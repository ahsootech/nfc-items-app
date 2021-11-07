from pymongo import MongoClient


class dbconfig:

    dbport = 27017
    mydb = None

    def __init__(self):
        # Step 1: Connect to MongoDB - Note: Change connection string as needed
        # mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
        client = MongoClient(port=self.dbport)
        self.mydb = db = client.nfctesting

    def getdb(self):
        if self.mydb is None:
            self.mydb = db = self.client.nfctesting
        return self.mydb