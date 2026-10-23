"""🌳 Check binary tree symmetry using recursive Depth-First Search (DFS)."""
from typing import Optional
from treenode import TreeNode

class RecursiveDFS:
    """🪞 Compare two subtrees to determine whether they are mirror images."""

    @staticmethod
    def helper(
        leftSubTree: Optional[TreeNode],
        rightSubTree: Optional[TreeNode],
    ) -> bool:
        """🔍 Recursively compare two subtrees in mirrored positions."""

        # ✅ Both nodes are absent, so this pair is symmetric.
        if not leftSubTree and not rightSubTree:
            return True

        # ❌ Only one node is absent, so their structures do not mirror.
        if not leftSubTree or not rightSubTree:
            return False

        # ⚖️ Corresponding mirror nodes must have equal values.
        if leftSubTree.val != rightSubTree.val:
            return False

        # 🔄 Compare outer children (left-left vs. right-right)
        #    and inner children (left-right vs. right-left).
        #    Both pairs must be symmetric for the subtrees to match.
        return (
            RecursiveDFS.helper(leftSubTree.left, rightSubTree.right)
            and
            RecursiveDFS.helper(leftSubTree.right, rightSubTree.left)
        )

    @staticmethod
    def isSymmetric(root: Optional[TreeNode]) -> bool:
        """🚀 Return True if the binary tree is symmetric around its center."""

        # 🌱 An empty tree is symmetric by definition.
        if not root: return True

        # 🪞 The root itself needs no comparison; check its two subtrees.
        return RecursiveDFS.helper(root.left, root.right)
