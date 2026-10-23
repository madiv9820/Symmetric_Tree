"""🌳 Define the TreeNode class for binary tree problems."""
from typing import Optional

class TreeNode:
    """🧩 Represent a single node in a binary tree."""

    def __init__(
        self,
        val: int = 0,
        left: Optional[TreeNode] = None,
        right: Optional[TreeNode] = None,
    ) -> None:
        """⚙️ Initialize a node with a value and optional child nodes.

        Args:
            val: The integer value stored in the node.
            left: The left child node, if present.
            right: The right child node, if present.
        """
        self.val: int = val  # 🔢 Store the node's value.
        self.left: Optional[TreeNode] = left  # ⬅️ Reference to the left child.
        self.right: Optional[TreeNode] = right  # ➡️ Reference to the right child.
