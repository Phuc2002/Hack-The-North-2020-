import Algorithmia
from Algorithmia.acl import ReadAcl

client = Algorithmia.client('<API-KEY>')

# Get directory's contents as JSON
exampleJson = client.file("data://.algo/media/VideoAlgorithms/perm").getJson()
file_list = exampleJson['files']


# POST LOCAL VIDEO MP4 FILE TO THE STORAGE
def post(filename,local):
    client.file("data://Chillies/tmp/"+filename).putFile(local)


# DOWNLOAD
# RETURN THE PATH OF THE DOWNLOADED VIDEO MP4 FILES
def download():
    paths = list()
    for file in file_list:
        f = client.file("data://.algo/media/VideoAlgorithms/perm/" + file['filename']).getFile()
        #print(f.name)
        path = f.name
        paths.append(path)
        print(file['filename'])

    print("------DOWNLOADED------")
    return paths

# DELETE
def delete():
    for file in file_list:
        exampleFile = client.file("data://.algo/media/VideoAlgorithms/perm/" + file['filename'])
        print(file)
        exampleFile.delete()

    print("------DELETED-----")
