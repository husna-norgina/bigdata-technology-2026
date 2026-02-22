from pymongo import MongoClient

uri = "mongodb+srv://husna-norgina:Husna99@cluster0.yo3vctf.mongodb.net/?appName=Cluster0"

try:
    client = MongoClient(uri)
    print("Koneksi berhasil!")
    print(client.list_database_names())
except Exception as e:
    print("Koneksi gagal:", e)