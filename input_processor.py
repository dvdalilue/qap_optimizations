# File handler module

def readIntArray(file, n):
    aux_list = []

    for line in xrange(0,n):
        aux_list.append(map(int, file.readline().split()))

    return aux_list

def readDistances(file, n):
    return readIntArray(file, n)

def readFlows(file, n):
    return readIntArray(file, n)

def processInput(file):
    n = int(file.readline()) # Read first line (number of nodes)

    file.readline() # Skip the empty new line

    distances = readDistances(file, n)

    file.readline() # Skip the empty new line

    flows = readFlows(file, n)

    return (n, distances, flows)