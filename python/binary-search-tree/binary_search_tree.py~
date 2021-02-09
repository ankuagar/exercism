class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        fmt = 'TreeNode(data={}, left={}, right={})'
        return fmt.format(self.data, self.left, self.right)


class BinarySearchTree:
    def __init__(self, tree_data):
        if len(tree_data) > 0:
            self.root = TreeNode(tree_data[0])
            for data in tree_data[1:]:
                self.root = BinarySearchTree._insert(self.root, data)
        else:
            self.root = None
    @staticmethod
    def _insert(node, data):
        if node is None:
            return TreeNode(data)
        elif int(data) <= int(node.data):
            node.left = BinarySearchTree._insert(node.left, data)
        elif int(data) > int(node.data):
            node.right = BinarySearchTree._insert(node.right, data)            
        return node 
        
    def data(self):
        return self.root

    def sorted_data(self):
        '''
        In order traversal
        '''
        def sort(node, coll):
            if node is None:
                return
            sort(node.left, coll)
            coll.append(node.data)
            sort(node.right, coll)
                           
            return coll

        if self.root is None:
            return []
        else:            
            return sort(self.root, [])
