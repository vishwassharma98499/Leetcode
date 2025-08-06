from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Depth-First Search (DFS) Traversals
# Inorder Traversal (Left -> Root -> Right)

def inorder_traversal(root):
    result = []
    def inorder(node):
        if node:
            print(node.val)
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
    inorder(root)
    return result

#Preorder Traversal (Root -> Left -> Right)

def preorder_traversal(root):
    result = []
    def preorder(node):
        if node:
            result.append(node.val)
            preorder(node.left)
            preorder(node.right)
    preorder(root)
    return result

# Postorder Traversal (Left -> Right -> Root)

def postorder_traversal(root):
    result = []
    def postorder(node):
        if node:
            postorder(node.left)
            postorder(node.right)
            result.append(node.val)
    postorder(root)
    return result


# Breadth-First Search (BFS) Traversal
# Level Order Traversal

def level_order_traversal(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result





# Create a binary tree
#       1
#      / \
#     2   3
#    / \
#   4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Test all traversal algorithms
print("Inorder Traversal:", inorder_traversal(root))
print("Preorder Traversal:", preorder_traversal(root))
print("Postorder Traversal:", postorder_traversal(root))
print("Level Order Traversal:", level_order_traversal(root))

def min_operations_to_sort(weights, dist):
    n = len(weights)
    target = sorted(range(n), key=lambda x: weights[x])  # Indices of weights in sorted order
    current_positions = list(range(n))
    operations = 0

    for i in range(n):
        if current_positions[i] != target[i]:
            moves_needed = abs(target[i] - current_positions[i])
            moves_possible = sum(dist[j] for j in range(current_positions[i], target[i], 1 if target[i] > current_positions[i] else -1))
            if moves_possible < moves_needed:
                return -1  # Impossible to sort
            operations += moves_needed

    return operations

# Example usage
weights = [3, 2, 1]
dist = [1, 4, 5]
print(min_operations_to_sort(weights, dist))  # Output: 7
