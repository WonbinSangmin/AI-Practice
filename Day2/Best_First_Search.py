from copy import deepcopy

graph = {'A': ['B','C','D'],
         'B': ['E','F'],
         'C': ['G'],
         'D': ['G'],
         'E':[],
         'F':['G'],
         'G':[]}

f = {'A': 4,
     'B': 1,
     'C': 2,
     'D': 3,
     'E': 4,
     'F': 3,
     'G': 0}

def print_list(X,open_list,closed,f):
    f_list=[]
    print("------------")
    print("X = ", X)
    print('open :', open_list)
    if len(open_list) != 0 :
        for state in open_list:
            f_list.append(f[state])
    print('f_value :', f_list)
    print('closed :', closed )

def BFS(graph,start,goal):
    open_list = []
    closed_list = []
    open_list.extend(start)
    print_list(None,open_list,closed_list,f)
    while(open_list):
        X = open_list.pop(0)
        if X == goal:
            print_list(X, open_list, closed_list,f)
            return "***Success***"
        else:
            children = graph[X]
            closed_list.extend(X)
            sorted_children = sorted(children, key=f.get)
            for child in sorted_children:
                if child in open_list:
                    print("update child from open list: ",child)

                if child in closed_list:
                    print("update child from closed list",child)
                else:
                    open_list.extend(child)

            open_list = sorted(open_list, key=f.get)

        print_list(X,open_list,closed_list,f)

start_state = input("Start State: ")
goal_state = input("Goal State: ")
print(BFS(deepcopy(graph),start_state,goal_state))