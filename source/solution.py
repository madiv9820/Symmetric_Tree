"""🌳 Determine whether a binary tree is symmetric."""
from typing import Optional
from treenode import TreeNode
from .approaches import RecursiveDFS

class Solution:
    """🧩 Provide a solution for checking tree symmetry."""

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """🪞 Check whether the binary tree mirrors itself.

        Args:
            root: The root node of the binary tree.

        Returns:
            True if the tree is symmetric; otherwise, False.
        """
        recursiveDFS: RecursiveDFS = RecursiveDFS()
        return recursiveDFS.isSymmetric(root)
