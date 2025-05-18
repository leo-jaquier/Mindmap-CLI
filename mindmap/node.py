"""
Node module defining the basic building block of the MindMap.
Each node contains a name and a list of child nodes.
"""


class Node:
    def __init__(self, name: str):
        """Initialize a node with a name and an empty list of children."""
        self.name = name
        self.children = []

    def add_child(self, node: "Node") -> None:
        """Attach a child node to this node."""
        self.children.append(node)

    def remove_child(self, name: str) -> None:
        """Remove a child node by its name."""
        self.children = [c for c in self.children if c.name != name]

    def find_node(
            self,
            name: str,
            path: list[str] | None = None
    ) -> list[str] | None:
        """
        Recursively search for a node by name.

        Args:
            name: Name of the node to find.
            path: Current traversal path (used internally).

        Returns:
            List of node names representing the path to the node if found;
            otherwise None.
        """
        if path is None:
            path = [self.name]

        if self.name == name:
            return path

        for child in self.children:
            result = child.find_node(name, path + [child.name])
            if result:
                return result

        return None
