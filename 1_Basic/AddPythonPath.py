import sys
#MyPythonFolder = "D:\MyPythonFolder*"
#MyPythonFolder = "Python27amd64"

MyPythonFolder = "C:\dev\NBTATOOLS\Build\Python\Lib\site-packages\PyQt5\plugins"




if MyPythonFolder in sys.path:
	print MyPythonFolder + " already in sys.path"
else:
	print  "add " + MyPythonFolder + " into sys.path"
	sys.path.insert(0,MyPythonFolder)
	print sys.path





