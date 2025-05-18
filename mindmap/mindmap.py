"""
MindMap module for managing hierarchical nodes including add, delete,
search, display, and persistence operations.
"""

import json
from .node import Node


class MindMap:
    def __init__(self, root_name: str):
        """Initialize the mind map with a root node."""
        self.root = Node(root_name)

    def add_node(self, parent_name: str, child_name: str) -> bool:
        """
        Add a child node under a specified parent node.

        Args:
            parent_name: Name of the parent node.
            child_name: Name of the new child node.

        Returns:
            True if the child was added successfully;
            False if parent not found.
        """
        path = self.root.find_node(parent_name)
        if not path:
            print(f"Parent '{parent_name}' not found.")
            return False

        parent = self._get_node_by_path(path)
        parent.add_child(Node(child_name))
        return True

    def delete_node(self, name: str) -> bool:
        """
        Delete a node by name, disallowing deletion of the root.

        Args:
            name: Name of the node to delete.

        Returns:
            True if deletion succeeded; False if node not found or root.
        """
        path = self.root.find_node(name)
        if not path or len(path) < 2:
            print(f"Node '{name}' not found or is the root.")
            return False

        parent = self._get_node_by_path(path[:-1])
        parent.remove_child(name)
        return True

    def _get_node_by_path(self, path: list[str]) -> Node:
        """
        Traverse the mind map according to a path and return the target node.

        Args:
            path: List of node names from root to the target node.

        Returns:
            The Node object at the end of the path.
        """
        node = self.root
        for name in path[1:]:
            node = next(child for child in node.children if child.name == name)
        return node

    def display(self, node: Node | None = None, indent: int = 0) -> None:
        """
        Recursively print the tree structure.

        Args:
            node: Node to start display from (default is root).
            indent: Indentation level (used internally).
        """
        if node is None:
            node = self.root

        print(" " * indent + "- " + node.name)
        for child in node.children:
            self.display(child, indent + 2)

    def save_to_file(self, filename: str) -> None:
        """
        Serialize and save the mind map to a JSON file.

        Args:
            filename: Path to the output file.
        """
        def to_dict(node: Node) -> dict:
            return {
                "name": node.name,
                "children": [to_dict(c) for c in node.children]
            }

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(to_dict(self.root), f, indent=2)

    def load_from_file(self, filename: str) -> None:
        """
        Load and deserialize the mind map from a JSON file.

        Args:
            filename: Path to the input file.
        """
        def from_dict(data: dict) -> Node:
            node = Node(data["name"])
            for child in data.get("children", []):
                node.add_child(from_dict(child))
            return node

        with open(filename, encoding='utf-8') as f:
            self.root = from_dict(json.load(f))

    def search(self, name: str) -> list[str] | None:
        """
        Search for a node by name.

        Args:
            name: Node name to find.

        Returns:
            Path from root to the node if found; otherwise None.
        """
        return self.root.find_node(name)
