# How to use 'filecmd'
This document is 'filecmd' guide.   
   
## Show list of filestore
```bash
$ ./filecmd.py list
filestore url: http://filestore.testdom
filestore id: root
filestore password: xxxxxxx
{'list_files': ['test.txt', 'test2.txt', 'test3.txt', 'test4.txt', 'jira.txt', 'Dockerfile']}
```

## Upload file
```bash
$ ./filecmd.py upload test2
filestore url: http://filestore.testdom
filestore id: root
filestore password: xxxxxxx
{"filenames":["test2"]}
```

## Upload files
```bash
$ ./filecmd.py upload test1 test9
filestore url: http://filestore.testdom
filestore id: root
filestore password: xxxxxxx
{"filenames":["test1"]}{"filenames":["test9"]}

$ ./filecmd.py list
filestore url: http://filestore.testdom
filestore id: root
filestore password: xxxxxxx
{'list_files': ['test1', 'test9']}
```

## Download file
```bash
$ ./filecmd.py list
filestore url: http://filestore.testdom
filestore id: root
filestore password: xxxxxxx
{'list_files': ['test1', 'test9', 'test2', 'down.txt']}

$ ./filecmd.py download down.txt
filestore url: http://filestore.testdom
filestore id: root
filestore password: xxxxxxx
download done

$ ls -la down.txt
-rw-r--r-- 1 root root 9 Dec 13 16:53 down.txt
```
