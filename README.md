# Tree Terminology and Types of Binary Trees

## Tree Terminology

- **Root**: The top node without a parent.
- **Edge**: A link between a parent and a child node.
- **Leaf**: A node which does not have children.
- **Sibling**: Children of the same parent.
- **Ancestor**: A parent, grandparent, great-grandparent, etc., of a node.
- **Depth of a Node**: The length of the path from the root to the node, measured in the number of edges.
- **Height of a Node**: The length of the path from the node to the deepest node connected to it. This length is measured by the number of edges.
- **Depth of the Tree**: The depth of the root node, which is always zero.
- **Height of the Tree**: The height of the root node.

## Types of Binary Trees

### Full Binary Tree
- Each node has either 0 or 2 children. No node has exactly 1 child.

### Perfect Binary Tree
- Every node other than leaf nodes has exactly two children.
- All leaf nodes are at the same level.
- The tree has exactly 2^(h+1) - 1 nodes, where `h` is the height of the tree.
- The number of leaf nodes is (n+1)/2 for a tree with `n` nodes.

### Complete Binary Tree
- Every level, except possibly the last, is completely filled.
- If the last level is not filled, nodes are as far left as possible.

### Balanced Binary Tree
- A tree where all leaf nodes are at the same distance from the root.

## Deepest Node in a Binary Tree
- The deepest node is the last node reached in a level order traversal.

## Tree Search Techniques

### Depth First Search (DFS)
1. **Preorder Traversal**: Visit the root node, then the left subtree, followed by the right subtree.
2. **Inorder Traversal**: Visit the left subtree, then the root node, and finally the right subtree.
3. **Postorder Traversal**: Visit the left subtree, the right subtree, and then the root node.

### Breadth First Search (BFS)
- **Level Order Traversal**: Visit each level from left to right.
