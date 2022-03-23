import json

# Since we're dealing with a tree structure, it's natural to use nested dictionaries.
# We create a subclass of dict
class TreeNode(dict):
    def __init__(self, name):
        self.__dict__ = self
        self.name = name
        self.parent = None
        self.children = []

    def add_child(self, child):
        child.parent = self.name
        self.children.append(child)

def build_product_tree():
    root = TreeNode("Animal")

    mammel = TreeNode("Mammals")
    mammel.add_child(TreeNode("Dog"))
    mammel.add_child(TreeNode("Cat"))
    mammel.add_child(TreeNode("Human"))

    reptile = TreeNode("Reptiles")
    reptile.add_child(TreeNode("Turtle"))
    reptile.add_child(TreeNode("Snake"))
    reptile.add_child(TreeNode("Crocodile"))

    insects = TreeNode("Insects")
    insects.add_child(TreeNode("Bee"))
    insects.add_child(TreeNode("Fly"))

    root.add_child(mammel)
    root.add_child(reptile)
    root.add_child(insects)
  
    return root


treeData = build_product_tree()

tree = json.dumps([treeData])

