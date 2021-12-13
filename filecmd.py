#!/usr/bin/python3

import sys, os
import getpass
import requests

headers = {
    'accept': 'application/json',
}

var_arg = sys.argv[1]

if len(sys.argv) < 2:
    print("Insufficient arguments")
    sys.exit()

filestore_url = input("filestore url: ")
if "http://" in filestore_url:
    filestore_url = filestore_url.strip()
    pass
else:
    filestore_url = "http://" + filestore_url.strip()

filestore_id = input("filestore id: ")
filestore_pw = getpass.getpass("filestore password: ")

if var_arg == "list":
    response = requests.get(filestore_url + "/files/", headers=headers, auth=(filestore_id, filestore_pw))
    print(response.json())
elif var_arg == "upload":
    if len(sys.argv) < 3:
        print("plz input the filename")
        sys.exit()
    else:
        for i in range(2, len(sys.argv)):
          contents = sys.argv[i]
          cmd = f"curl -s -u {filestore_id}:{filestore_pw} -X \'POST\' \'{filestore_url}/uploadfiles/\' -H \'accept: application/json\' -H \'Content-Type: multipart/form-data\' -F \'files=@{contents}\'"
          os.system(cmd)
elif var_arg == "download":
    cmd = f"curl -s -u {filestore_id}:{filestore_pw} -X \'GET\' \'{filestore_url}/download/?filename={sys.argv[2]}\' -H \'accept: application/json\' -o {sys.argv[2]}"
    os.system(cmd)
    print("download done")
else:
    print("plz input arguments. (list/upload/download)")
