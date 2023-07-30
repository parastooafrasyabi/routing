# parastoo afrasyabi

city=['arad','zerind','timisoara','oradea','sibiu','fagaras','lugoj','mehadia','dobreta','craiova','rimnicu vilcea','pitesti','bucharest']
neighbour={"arad":[["zerind",75],["timisoara",118],["sibiu",140]] ,
           "zerind":[["oradea",71],["arad",75]] ,
		    "fagaras":[["bucharest",211],["sibiu",99]],
          "rimnicu vilcea":[["pitesti",97],["sibiu",80],["craiova",146]],
          "pitesti":[["bucharest",101],["craiova",138],["rimnicu vilcea",97]],
          "mehadia":[["dobreta",75],["lugoj",70]] ,
		    "lugoj":[["mehadia",70],["timisoara",111]] ,
           "dobreta":[["craiova",120],["mehadia",75]],
          "craiova":[["pitesti",138],["rimnicu vilcea",146],["dobreta",120]],
           "timisoara":[["lugoj",111],["arad",118]] ,
           "oradea":[["sibiu",151],["zerind",71]] ,
          "sibiu":[["fagaras",99],["rimnicu vilcea",80],["oradea",151],["arad",140]],        
          "bucharest":[["pitesti",101],["fagaras",211]]}
h={'arad':366,'zerind':374,'timisoara':329,'oradea':380,'sibiu':253,'fagaras':176,'lugoj':244,'mehadia':241,'dobreta':242,'craiova':160,'rimnicu vilcea':193,'pitesti':98,'bucharest':0}
visit=[]
start='arad'
frontier=[start]
parent={start:start}
goal='bucharest'
g={start:0}
cost={'arad':360}
while frontier:
    current=min(cost, key=lambda k: cost[k])
    del cost[current]
    frontier.remove(current)
    visit.append(current)
    for x in neighbour[current]:
        if x[0] not in visit:
            parent[x[0]]=current
            frontier.append(x[0])
            g[x[0]]=x[1]+g[parent[x[0]]]
            cost[x[0]]=h[x[0]]+g[x[0]]
            
    if current==goal:
        break
curr=goal
route=[goal]
while curr!=start:
    route.append(parent[curr])
    curr=route[-1]
print('this is route')   
print(route[::-1])