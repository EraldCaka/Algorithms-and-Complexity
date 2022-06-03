## Algorithms-and-Complexity Assignment 1

<strong>A solution to a problem that requires the usage of graphs ,nodes and dfs algorithm</strong>

Important Code Snippets
----
![Components](https://user-images.githubusercontent.com/96385473/171694898-37da4e67-fd30-4ad4-97c1-6c5516a2f3c0.png)

![graphTRUE](https://user-images.githubusercontent.com/96385473/171694466-f4f1ab51-7912-44f2-98f5-8e7566e14daf.png)

Pseudocode for the Algorithm
-

	<span style="color: green"> Open file (“filename”) as f

	lines = f.readlines()

	list=[]

        for line in lines

	list.append(line.split())
	
	end for

	n=list[0][0]

	p=list[0][1]

	g=Graph(n)

		for i in range(1,p+1):

        		g.addEdge(int(list[i][0]),int(list[i][1]))
	
			end for
			

	cc = g.connectedComponents()

	arraySingerPerState = []

	notAllowedDuets = 0

		for x in cc:

        		arraySingerPerState.append(len(x))
	
			end for
			

		for y in arraySingerPerState:

        		summationFormula(y)
		
        		notAllowedDuets = notAllowedDuets + summationFormula(y)
		
			end for
			

	AllowedDuets = summationFormula(n)-notAllowedDuets

	print(int(AllowedDuets)) </span>
	
	```json
  	 // code for coloring
	```



Examples
-
All inputs that were given to us from our professor via Email

Output3
---

![output3](https://user-images.githubusercontent.com/96385473/171833011-9ffb2ffb-39c4-4f94-9f62-acd48bb75036.png)


Output4
-
![output4](https://user-images.githubusercontent.com/96385473/171832342-1e1ce98d-fa20-4e55-bcb3-33e315bf41cf.png)


Output5
-
![output5](https://user-images.githubusercontent.com/96385473/171832140-27589112-ffc2-4c1e-83c6-404a2d3e684b.png)

--------
<strong>Contributors :[Erald Caka](https://github.com/HidekiNatsumi) and [Ervin Balla](https://github.com/ViniCS2001)</strong>
