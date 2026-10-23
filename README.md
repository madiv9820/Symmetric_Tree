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
