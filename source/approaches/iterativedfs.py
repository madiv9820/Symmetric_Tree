"""🌳 Check binary tree symmetry using iterative Depth-First Search (DFS)."""
from typing import Optional, List, Tuple
from treenode import TreeNode

class IterativeDFS:
    """🪞 Determine whether a binary tree is symmetric using a stack."""

    @staticmethod
    def isSymmetric(root: Optional[TreeNode]) -> bool:
        """🔍 Compare mirrored node pairs iteratively.

        Args:
            root: The root node of the binary tree.

        Returns:
            True if the tree is symmetric; otherwise, False.
        """

        # 🌱 An empty tree is symmetric by definition.
        if root:
            # 📚 Store pairs of nodes that must mirror each other.
            #    Start by comparing the root's left and right subtrees.
            nodeStack: List[Tuple[Optional[TreeNode], Optional[TreeNode]]] = [
                (root.left, root.right)
            ]

            # 🔄 Process node pairs until the stack is empty or a mismatch appears.
            while nodeStack:
                # 📤 Retrieve the most recently added pair (LIFO order).
                leftSubtree, rightSubtree = nodeStack.pop()

                # ✅ Two missing nodes match; no further checks are needed.
                if not leftSubtree and not rightSubtree:
                    continue

                # ❌ Only one missing node means the structures are asymmetric.
                if not leftSubtree or not rightSubtree:
                    return False

                # ⚖️ Corresponding mirror nodes must have equal values.
                if leftSubtree.val != rightSubtree.val:
                    return False

                # 🪞 Compare opposite child positions to preserve mirror symmetry.
                nodeStack.append((leftSubtree.left, rightSubtree.right))
                nodeStack.append((leftSubtree.right, rightSubtree.left))

        # 🎉 All node pairs matched, so the tree is symmetric.
        return True
