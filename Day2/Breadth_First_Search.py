from copy import deepcopy

graph = {'A': ['B','C','D'],
         'B': ['E','F'],
         'C': ['G'],
         'D': ['G'],
         'E':[],
         'F':['G'],
         'G':[]}

def print_list(X,open_list,closed):
    print("----------")
    print("X =", X)
    print('open :',open_list)
    print('closed :',closed)

def BFS(graph,start,goal):
    open_list = []
    closed_list = []
    open_list.extend(start)
    print_list(None,open_list,closed_list)
    while(open_list):
        X = open_list.pop(0)
        if X == goal:
            print_list(X, open_list, closed_list)
            return "***Success***"
        else:
            children = graph[X]
            closed_list.extend(X)

            for i in open_list:
                if i in children:
                    children.remove(i)
            for j in open_list:
                if j in children:
                    children.remove(j)
            open_list.extend(children)
        print_list(X, open_list, closed_list)
start_state = input("Start State: ")
goal_state = input("Goal State: ")
print(BFS(deepcopy(graph),start_state,goal_state))


