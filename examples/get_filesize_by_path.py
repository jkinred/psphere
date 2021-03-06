from __future__ import absolute_import, division, print_function

from psphere.client import Client
from psphere.managedobjects import HostSystem

if __name__ == '__main__':
    client = Client('localhost:8989', 'user', 'pass')
    hosts = HostSystem.all(client)
    host = hosts[0]

    db = host.datastoreBrowser
    mor = db.SearchDatastore_Task(datastorePath="[datastore1] vCenter/",
    searchSpec={"matchPattern":"vCenter.vmx",
                    "details":{"fileType":True,
                                    "fileSize":True,
                                    "modification":True,
                                    "fileOwner":True},
                    "searchCaseInsensitive":False,
                    "sortFoldersFirst":False,
                    "query":None
            })

    while True:
        info = mor.info
        if info.state in ["success"]:
            break
        mor.update(properties=["info"])

    result = info.result
    files = result.file

    for file in files:
        print("FileName:%s, FileSize:%s" %(file.path, file.fileSize))
