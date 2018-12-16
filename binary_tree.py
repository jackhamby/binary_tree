
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
    ### MAX / MIN VALUES                                                 ###
    ### ================================================================ ###

    def max_value(self):
        if (not self.root):
            return False
        max_value = self.root.value
        r_child = self.root.r_child
        while(r_child):
            max_value = r_child.value
            r_child = r_child.r_child
        return max_value

    def min_value(self):
        if (not self.root):
            return False
        min_value = self.root.value
        l_child = self.root.l_child
        while(l_child):
            min_value = l_child.value
            l_child = l_child.l_child
        return min_value


    ### ================================================================ ###
    ### MAX / MIN DEPTH                                                  ###
    ### ================================================================ ###


    def max_depth(self):
        pass

    def min_depth(self):
        pass


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

    def size(self):
        self.size = 0
        if (not self.root):
            return self.size
        self.count_node(self.root)
        return self.size
    
    def count_node(self, node):
        self.size += 1
        if (node.l_child):
            self.count_node(node.l_child)
        if (node.r_child):
            self.count_node(node.r_child)
        

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
    tree.insert(12)
    tree.insert(1)

    tree.show()

    print(f'looking for 3 : {tree.search(3)}')
    print(f'looking for 5 : {tree.search(5)}')
    print(f'looking for 8 : {tree.search(8)}')

    print(f'tree size is: {tree.size()} nodes')
    print(f'tree max value is: {tree.max_value()}')
    print(f'tree min value is: {tree.min_value()}')
