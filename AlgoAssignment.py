class Graph:

	# init function to declare class variables
	def __init__(self, V):
		self.V = V
		self.adj = [[] for i in range(V)]

	def DFSUtil(self, temp, v, visited):

		# Mark the current vertex as visited
		visited[v] = True

		# Store the vertex to list
		temp.append(v)

		# Repeat for all vertices adjacent
		# to this vertex v
		for i in self.adj[v]:
			if visited[i] == False:

				# Update the list
				temp = self.DFSUtil(temp, i, visited)
		return temp

	# method to add an undirected edge
	def addEdge(self, v, w):
		self.adj[v].append(w)
		self.adj[w].append(v)

	# Method to retrieve connected components in an undirected graph
	def connectedComponents(self):
		visited = []
		cc = []
		for i in range(self.V):
			visited.append(False)
		for v in range(self.V):
			if visited[v] == False:
				temp = []
				cc.append(self.DFSUtil(temp, v, visited))
		return cc
    
def summationFormula(k):
    if k==1:
        return 0
    else:
        return k*(k-1)/2

# Driver Code
if __name__ == "__main__":

    with open("input05 copy.txt") as f:
        lines = f.readlines()
        lines = (line for line in lines if line)

    list = []

    for line in lines:

        if not line.strip():
            continue
        else:
            info = line.split()
            list.append(info)
    
    n = (int(list[0][0])) #nr of artists
    p = (int(list[0][1])) #nr of information lines

    g=Graph(n)

    for i in range(1,p+1):
        g.addEdge(int(list[i][0]),int(list[i][1]))
    cc = g.connectedComponents()

    arraySingerPerState = []
    notAllowedDuets = 0
    
    #insert in an array the number of singers per state
    for x in cc:
        #print(len(x))
        arraySingerPerState.append(len(x))
    
    #calculate the number of not allowed duets between singers of same nationality
    for y in arraySingerPerState:
        summationFormula(y)
        notAllowedDuets = notAllowedDuets + summationFormula(y)

    #print (len(cc)) #this will tell the number of nationalities
    #print(notAllowedDuets)
    #total nr of allowed duets is equal to the number of all duets between all singers - not allowed duets
    AllowedDuets = summationFormula(n)-notAllowedDuets
    print(int(AllowedDuets))

# Assignment 1
# Algorithms & Complexity
# Worked by Ervin Balla & Erald Caka

# The implementation of the Graph class, DFS function and connected 
# component function were retrieved by us from a code created by Abhishek Valsan
# which can be found at the GeeksforGeeks website at the following link
# https://www.geeksforgeeks.org/connected-components-in-an-undirected-graph/
