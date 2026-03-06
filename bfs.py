from collections import deque

# -----------------------------
# Define Tree Node
# -----------------------------
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# -----------------------------
# BFS - Level Order Traversal
# -----------------------------
def bfs_tree(root):
    if root is None:
        return
    
    queue = deque()
    queue.append(root)

    print("BFS Traversal:", end=" ")
    
    while queue:
        current = queue.popleft()
        print(current.value, end=" ")

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    print()


# -----------------------------
# BFS - Print Level by Level
# -----------------------------
def bfs_levels(root):
    if root is None:
        return
    
    queue = deque([root])
    
    print("\nLevel Order Traversal:")
    
    while queue:
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()
            print(node.value, end=" ")

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        print()  # New line after each level


# -----------------------------
# Create Example Tree
# -----------------------------
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)


# -----------------------------
# Run BFS
# -----------------------------
bfs_tree(root)
bfs_levels(root)