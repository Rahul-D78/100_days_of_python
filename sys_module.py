import sys


def printData():
	print(sys.argv)


def printsum():
	print(int(sys.argv[1])+ int(sys.argv[2])) 

printData()

#printsum()	

print(sys.version)
print(sys.path)
print(sys.maxsize)
print(type(sys.stdin))
print(sys.stdout)