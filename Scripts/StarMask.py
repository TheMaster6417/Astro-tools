import sys
from sys import platform
if platform == "linux" or platform == "linux2":
    print("Linux not supported")
elif platform == "darwin":
    print("OS Type: Mac-os")
    path_to = '../PreReq/Starnet++/OSX/StarNet_MacOS-2'
elif platform == "win32":
    print("OS Type: windows")
    path_to = '../PreReq/Starnet++/Windows/StarNet_Win'

image = sys.argv[1]
output = sys.argv[2]