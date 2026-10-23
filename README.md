# [🌳 Symmetric Tree — A Tale of Two Mirrors 🪞](https://leetcode.com/problems/symmetric-tree/?envType=study-plan-v2&envId=top-interview-150)

### 📖 The Story: The Magical Mirror

Imagine standing in front of a magical mirror where everything on your left is perfectly reflected on your right. Your left hand mirrors your right, and every movement has an opposite counterpart! ✨

Now, imagine a binary tree that follows the same rule. For the tree to be symmetric, its left and right subtrees must be mirror images of each other—not just have the same values, but also arrange their children in opposite positions. If even one node is missing or misplaced, the reflection breaks! 🪞

### 🎯 Problem Statement

Given the `root` of a binary tree, determine whether the tree is symmetric around its center.

Return `True` if the left and right subtrees are mirror images of each other; otherwise, return `False`.

To verify symmetry, compare the **left child of the left subtree with the right child of the right subtree, and the right child of the left subtree with the left child of the right subtree**. Their values and structures must match perfectly. 🔄

#### 🧪 Example

- **The Perfect Reflection ✅**
    
    ![](https://assets.leetcode.com/uploads/2021/02/19/symtree1.jpg)
    - **Input:** `root = [1,2,2,3,4,4,3]`
    - **Output:** True`
    - **Explanation:** The root node `1` has two children with value `2`. Looking deeper, the outer nodes (`3` and `3`) match, and the inner nodes (`4` and `4`) match. Both subtrees have mirrored structures and identical corresponding values, so the tree is symmetric! 🎉

- **The Broken Reflection ❌**

    ![](https://assets.leetcode.com/uploads/2021/02/19/symtree2.jpg)
    - **Input:** `root = [1,2,2,null,3,null,3]`
    - **Output:** `False`
    - **Explanation:** Although both children of the root have value `2`, their structures do not mirror each other. The left subtree has a right child with value `3`, while the right subtree also has a right child with value `3`. These nodes occupy the same relative position instead of opposite positions, breaking the symmetry. 💔

#### 📌 Constraints
- 🌲 The number of nodes in the tree is between `1` and `1000`, inclusive.
- 🔢 Each node's value satisfies `-100 <= Node.val <= 100`.
These constraints mean the tree can contain up to 1,000 nodes, and node values can be negative, zero, or positive.

#### 💡 Key Takeaway
A symmetric tree is like a perfect reflection! 🪞 Always compare **opposite sides**: left with right, and right with left. Matching values alone aren't enough—the structure and positions of the nodes must also be mirrored. 🌳✅

---

### 🌳 Symmetric Tree — All Approaches Explained 🪞

A binary tree is symmetric if its left and right subtrees are mirror images of each other. That means corresponding nodes must have equal values, and their children must appear in opposite positions. 🔄

We can solve this problem using three approaches: Recursive DFS, Iterative DFS, and Iterative BFS.

1. **🌿 Recursive DFS — Let Recursion Do the Work**

    - **💡 Intuition :** Imagine two people standing on opposite sides of a mirror. Each person checks whether their counterpart has the same value and whether their children mirror each other. They keep repeating this process down the tree until every pair matches.

    - **⚙️ Steps :**
        1. If the root is None, return `True`.
        2. If both compared nodes are None, return `True`.
        3. If only one node is None or their values differ, return `False`.
        4. Compare the outer children and inner children recursively.
        5. Return `True` only if both comparisons succeed.
    
    - **📝 Pseudocode :**
        ```
        function isSymmetric(root):
            if root is None:
                return True

            return isMirror(root.left, root.right)

        function isMirror(left, right):
            if left is None and right is None:
                return True

            if left is None or right is None:
                return False

            if left.val != right.val:
                return False

            return isMirror(left.left, right.right)
            AND isMirror(left.right, right.left)
        ```
    
    - **⏱️ Complexity :**
        - **Time:** `O(n)` — Each node is visited at most once.
        - **Auxiliary space:** `O(h)` — Recursion stack, where `h` is tree height; worst case `O(n)` .

2. **📚 Iterative DFS — Mirror Checking with a Stack**

    - **💡 Intuition :** What if we do not want recursion to manage the journey? We can maintain our own stack of node pairs that must mirror each other. Like a to-do list, we process a pair, verify it, and add its child pairs for later checking. Since a stack follows LIFO (Last In, First Out), the most recently added pair is processed first.

    - **⚙️ Steps :**
        1. If the root is None, return `True`.
        2. Push (`root.left, root.right`) onto a stack.
        3. Pop a pair and check whether both nodes are missing.
        4. Return `False` if only one is missing or their values differ.
        5. Push the outer pair (`left.left, right.right`).
        6. Push the inner pair (`left.right, right.left`).
        7. If the stack becomes empty without a mismatch, return `True`.

    - **📝 Pseudocode :**
        ```
        function isSymmetric(root):
            if root is None:
                return True

            stack = [(root.left, root.right)]

            while stack is not empty:
                left, right = stack.pop()

                if left is None and right is None:
                    continue

                if left is None or right is None:
                    return False

                if left.val != right.val:
                    return False

                push (left.left, right.right) onto stack
                push (left.right, right.left) onto stack

            return True
        ```
    
    - **⏱️ Complexity :**
        - **Time:** `O(n)` — Each node is checked at most once.
        - **Auxiliary space:** `O(n)` worst case for the stack.

3. **🚦 Iterative BFS — Compare Mirrors Level by Level**

    - **💡 Intuition :** Instead of diving deep into one branch, imagine inspecting the tree one level at a time. A queue stores pairs of nodes that should mirror each other. Using **FIFO** (First In, First Out), we process earlier pairs first, gradually moving down the tree.

    - **⚙️ Steps :**
        1. If the root is `None`, return `True`.
        2. Initialize a queue with (`root.left, root.right`).
        3. Remove the next pair from the front of the queue.
        4. Skip the pair if both nodes are missing.
        5. Return `False` if only one is missing or their values differ.
        6. Enqueue the outer and inner mirrored child pairs.
        7. If every pair matches, return `True`.

    - **📝 Pseudocode :**
        ```
        function isSymmetric(root):
            if root is None:
                return True

            queue = [(root.left, root.right)]

            while queue is not empty:
                left, right = remove_front(queue)

                if left is None and right is None:
                    continue

                if left is None or right is None:
                    return False

                if left.val != right.val:
                    return False

                add (left.left, right.right) to queue
                add (left.right, right.left) to queue

            return True
        ```
    
    - **⏱️ Complexity**
        - **Time:** `O(n)` — Each node is checked at most once.
        - **Auxiliary space:** `O(n)` worst case for the queue.

#### 🏆 Quick Comparison

| Feature | 🌿 Recursive DFS | 📚 Iterative DFS | 🚦 Iterative BFS |
|---|---|---|---|
| **Data structure** | Call stack | Explicit stack | Queue |
| **Traversal style** | Depth-first | Depth-first | Level-order |
| **Time complexity** | `O(n)` | `O(n)` | `O(n)` |
| **Auxiliary space** | `O(h)` | `O(n)` | `O(n)` |
| **Recursion used** | ✅ Yes | ❌ No | ❌ No |
| **Main advantage** | ✨ Clean and concise | 🛡️ Avoids recursion-depth limits | 🔄 Processes pairs level by level |

💡 Here, `n` is the number of nodes and `h` is the height of the tree.

#### 🎯 Final Takeaway

All three approaches use the same fundamental rule: **compare the outer children with each other and the inner children with each other. 🪞**
- **🌿 Recursive DFS:** Best when you want concise, natural code.
- **📚 Iterative DFS:** Useful when you prefer an explicit stack and want to avoid recursion-depth limits.
- **🚦 Iterative BFS:** Ideal when you want to process mirrored node pairs level by level.

**Remember:** Matching values alone is not enough. A symmetric tree must have both matching values and **mirrored structure**. 🌳✅

---
