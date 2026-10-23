"""🌳 Check binary tree symmetry using iterative Breadth-First Search (BFS)."""
from collections import deque
from typing import Deque, Optional, Tuple
from treenode import TreeNode

class IterativeBFS:
    """🪞 Check whether a binary tree is symmetric using a queue."""

    @staticmethod
    def isSymmetric(root: Optional[TreeNode]) -> bool:
        """🔍 Compare mirrored node pairs level by level.

        Args:
            root: The root node of the binary tree.

        Returns:
            True if the tree is symmetric; otherwise, False.
        """

        # 🌱 An empty tree is symmetric by definition.
        if root:
            # 📥 Initialize a queue with the root's left and right children.
            #    Each pair contains nodes that should mirror each other.
            treeQ: Deque[Tuple[Optional[TreeNode], Optional[TreeNode]]] = deque(
                [(root.left, root.right)]
            )

            # 🔄 Process mirrored node pairs in FIFO order (level by level).
            while treeQ:
                # 📤 Retrieve the next pair from the front of the queue.
                leftSubtree, rightSubtree = treeQ.popleft()

                # ✅ Two missing nodes match, so skip this pair.
                if not leftSubtree and not rightSubtree:
                    continue

                # ❌ Only one missing node means the structures are asymmetric.
                if not leftSubtree or not rightSubtree:
                    return False

                # ⚖️ Corresponding mirror nodes must have equal values.
                if leftSubtree.val != rightSubtree.val:
                    return False

                # 🪞 Enqueue opposite child positions for mirror comparison.
                treeQ.append((leftSubtree.left, rightSubtree.right))
                treeQ.append((leftSubtree.right, rightSubtree.left))

        # 🎉 Every mirrored pair matches, so the tree is symmetric.
        return True
