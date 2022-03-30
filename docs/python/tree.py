# tree = (racine, liste des sous trees)

#un tree vide
tree=[]

#un tree avec un seul noeud racine
tree=["R",[]]

#un tree avec 3 fils
#         R
#       / | \
#     A   B  C
tree=["R",[["A",[]],["B",[]],["C",[]]]]

# un tree de hauteur 2
#         R
#       / | \
#     A   B  C
#    / \
#   D   E
tree=["R",[["A",[["D",[]],["E",[]]]],["B",[]],["C",[]]]]

# soit 4 trees de hauteur 0 de racines B,C,D et E:
treeB=["B",[]]
treeC=["C",[]]
treeD=["D",[]]
treeE=["E",[]]
# un tree de hauteur 1 de racine A composés des deux sous-trees D et E
treeA=["A",[treeD,treeE]]

#l'tree précédent de racine R est ainsi donné par
tree=["R",[treeA,treeB,treeC]]

print(tree)


# get tree's root
def get_root(tree):
    return tree[0] 

print(get_root(tree))

# test if a tree is empty
def isEmpty(tree):
    return len(tree) == 0
print("is emapty", isEmpty(tree))

# get sub-tree

def get_subtrees(tree):
    if isEmpty(tree) : 
        return
    else:
        return tree[1]

print("get_subtree", get_subtrees(tree))


# Return child nodes of the root
def get_leaves(tree):
    L=[]
    for subtree in get_subtrees(tree):
        L.append(get_root(subtree))
    return L

print("get_leaves: ", get_leaves(tree))

# Write a function named isLeaf that takes in as input a tree and return True if the node has no childres, otherwise False. 
def isLeaf(tree):
    return len(tree[1])==0

print("isLeaf: ", isLeaf(tree))

# Write a function in python to get the size of a tree. The function, named size, takes in as inputs a tree and returns the tree's size. If the tree passed as a parameter have zero nodes, the function returns the number 0.
def size(tree):
    S=0
    if isEmpty(tree):
        return 0
    else:
        for subtree in tree[1]:
            S += size(subtree)
        return 1 + S

# EXEMPLE : 
# un tree de hauteur 2
#         R
#       / | \
#     A   B  C
#    / \
#   D   E
print("taille de l'tree :",size(tree))

##  Write a function in python to get the height of a tree. The function, named height, takes in as inputs a tree and returns the tree's height.
def height(tree):
    L=[]
    if not isEmpty(tree) and isLeaf(tree):
        return 0
    else:
        for subtree in tree[1]:
            L.append(height(subtree))
        return 1+max(L)
    
print("tree's height :", height(tree))


#### Write a function in python to get the leaves' number of a tree. The function, named get_leaves_number, takes in as inputs a tree and returns the leaves' number of a tree.

def get_leaves_number(tree, lf = []):
    S=0
    if isEmpty(tree):
        return 0
    else:
        if isLeaf(tree):
            lf.append(get_root(tree))
            return 1
        else:
            for subtree in tree[1]:
                S += get_leaves_number(subtree, lf)
            return S

print("get_leaves_number :", get_leaves_number(tree))

# Write a python function to create a tree that is represented in this figure.
