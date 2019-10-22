# # Python3 program to demonstrate 
# # working of Alpha-Beta Pruning 

# # Initial values of Aplha and Beta 
# MAX, MIN = 1000, -1000

# # Returns optimal value for current player 
# #(Initially called for root and maximizer) 
# def minimax(depth, nodeIndex, maximizingPlayer, 
#             values, alpha, beta): 

#     # Terminating condition. i.e 
#     # leaf node is reached 
#     if depth == 3: 
#         return values[nodeIndex] 

#     if maximizingPlayer: 
    
#         best = MIN

#         # Recur for left and right children 
#         for i in range(0, 2): 
            
#             val = minimax(depth + 1, nodeIndex * 2 + i, 
#                         False, values, alpha, beta) 
#             best = max(best, val) 
#             alpha = max(alpha, best) 

#             # Alpha Beta Pruning 
#             if beta <= alpha: 
#                 break
        
#         return best 
    
#     else: 
#         best = MAX

#         # Recur for left and 
#         # right children 
#         for i in range(0, 2): 
        
#             val = minimax(depth + 1, nodeIndex * 2 + i, 
#                             True, values, alpha, beta) 
#             best = min(best, val) 
#             beta = min(beta, best) 

#             # Alpha Beta Pruning 
#             if beta <= alpha: 
#                 break
        
#         return best 
    
# # Driver Code 
# if __name__ == "__main__": 

#     values = [3, 5, 6, 9, 1, 2, 0, -1] 
#     print("The optimal value is :", minimax(0, 0, True, values, MIN, MAX)) 
tree = []
root = 0
pruned = 0

def children(branch, depth, alpha, beta):
    global tree
    global root
    global pruned
    i = 0
    for child in branch:
        if type(child) is list:
            (nalpha, nbeta) = children(child, depth + 1, alpha, beta)
            if depth % 2 == 1:
                beta = nalpha if nalpha < beta else beta
            else:
                alpha = nbeta if nbeta > alpha else alpha
            branch[i] = alpha if depth % 2 == 0 else beta
            i += 1
        else:
            if depth % 2 == 0 and alpha < child:
                alpha = child
            if depth % 2 == 1 and beta > child:
                beta = child
            if alpha >= beta:
                pruned += 1
                break
    if depth == root:
        tree = alpha if root == 0 else beta
    return (alpha, beta)

def alphabeta(in_tree=tree, start=root, lower=-15, upper=15):
    global tree
    global root
    global pruned

    m = int(input("Enter no. of rows"))
    n = int(input("Enter no. of cols"))

    for i in range(0,m):
        tree.append([])
        for j in range(0,n):
            tree[i].append(int(input("Enter value : ")))

    
    (alpha, beta) = children(tree, start, lower, upper)
    
    if __name__ == "__main__":
        print ("(alpha, beta): ", alpha, beta)
        print ("Result: ", tree)
        print ("Times pruned: ", pruned)
    
    return (alpha, beta, tree, pruned)

if __name__ == "__main__":
    alphabeta()