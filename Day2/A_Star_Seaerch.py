from copy import deepcopy

graph = {'A': ['B','C','D'],
         'B': ['E','F'],
         'C': ['G'],
         'D': ['G'],
         'E':[],
         'F':['G'],
         'G':[]}
g = {'A': {'A':0},
     'B': {'A':10},
     'C': {'A':10},
     'D': {'A':10},
     'E': {'B':20},
     'F': {'B':20},
     'G': {'F':30, 'C':30,'D':28}}

h = {'A': 15,
     'B': 5,
     'C': 19,
     'D': 18,
     'E': 30,
     'F': 2,
     'G': 0}

f = {}


def print_list(X, open_list, closed, f):
    f_list = []
    print("------------")
    print("X = ", X)
    print('open :', open_list)
    if len(open_list) != 0:
        for state in open_list:
            f_list.append(f[state])
    print('f_value :', f_list)
    print('closed :', closed)


def A_Star_Search(graph,start,goal):
    open_list = []
    closed_list = []
    open_list.extend(start)
    f[start] = h[start]
    print_list(None,open_list,closed_list,f)
    while(open_list):
        X = open_list.pop(0)
        if X == goal:
            print_list(X,open_list,closed_list,f)
            return "***Success***"
        else:
            children = graph[X]
            closed_list.extend(X)
            for child in children:
                f[child] = g[child][X] + h[child]

            sorted_children = sorted(children, key = f.get)
            for child in sorted_children:
                if child in open_list:
                    print("update child from open list: ",child)
                    f[child] = g[child][X] + h[child]

                if child in closed_list:
                    print("update child from closed list",child)
                    f[child] = g[child][X] + h[child]

                else:
                    if child not in open_list:
                        open_list.extend(child)
            open_list = sorted(open_list,key=f.get)
        print_list(X, open_list, closed_list, f)


start_state = input("Start State: ")
goal_state = input("Goal State: ")
print(A_Star_Search(deepcopy(graph),start_state,goal_state))