
class BinaryTree:

    def __init__(self):

        self.root = None

    ### ================================================================ ###
    ### INSERT                                                           ###
    ### ================================================================ ###

    def insert(self, value):
        node = Node(value)
        if (not self.root):
            self.root = node
            return
        self.insert_node(self.root, node)

    def insert_node(self, node, inserted_node):
        # Right child
        if (inserted_node.value >= node.value):
            if (not node.r_child):
                node.r_child = inserted_node
            else:
                self.insert_node(node.r_child, inserted_node)
        # Left child
        else:
            if (not node.l_child):
                node.l_child = inserted_node
            else:
                self.insert_node(node.l_child, inserted_node)


    ### ================================================================ ###
    ### SEARCH                                                           ###
    ### ================================================================ ###

    def search(self, value):
        if (not self.root):
            return False
        return self.search_node(self.root, value)

    def search_node(self, node, value):
        if (not node):
            return False
        if (node.value == value):
            return True
        elif (value >= node.value):
            return self.search_node(node.r_child, value)
        else:
            return self.search_node(node.l_child, value)

    

    ### ================================================================ ###
    ### SIZE                                                             ###
    ### ================================================================ ###


    ### ================================================================ ###
    ### PRINT                                                            ###
    ### ================================================================ ###

    def show(self):
        tree = []
        level = 0
        tree.append([])
        self.show_node(level, self.root, tree)
        print(tree)
        
    def show_node(self, level, node, tree):
        tree[level].append(node.value)
        level += 1
        if (len(tree) <= level):
            tree.append([])
        if (node.l_child):
            self.show_node(level, node.l_child, tree)
        if (node.r_child):
            self.show_node(level, node.r_child, tree)

class Node:

    def __init__(self, value):

        self.value = value

        self.l_child = None
        self.r_child = None

        # print(f'creating node with value {self.value}')

    def show(self):
        print(f' {self.value}        ')
        print(f'{self.l_child.value}      {self.r_child.value}')



if __name__ == '__main__':
    tree = BinaryTree()


    tree.insert(6)
    tree.insert(3)
    tree.insert(4)
    tree.insert(8)
    tree.insert(7)
    tree.insert(2)
    tree.insert(4)
    tree.insert(4)

    tree.show()

    print(f'looking for 3 : {tree.search(3)}')
    print(f'looking for 5 : {tree.search(5)}')
    print(f'looking for 8 : {tree.search(8)}')
