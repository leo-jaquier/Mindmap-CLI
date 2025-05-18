"""
Command-line interface for MindMap operations.
Supports create, add, delete, show, save, load, and search commands.
"""

import argparse
import os
from mindmap.mindmap import MindMap

DATA_DIR = "data"
DEFAULT_FILENAME = "mindmap.json"
DEFAULT_FILE = os.path.join(DATA_DIR, DEFAULT_FILENAME)


def load_mindmap(filename: str) -> MindMap:
    """Load mind map from file if it exists; otherwise create new."""
    mindmap = MindMap("Root")
    if os.path.exists(filename):
        mindmap.load_from_file(filename)
    return mindmap


def ensure_data_dir() -> None:
    """Create the data directory if it doesn't exist."""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)


def main() -> None:
    """Parse arguments and execute requested MindMap command."""
    parser = argparse.ArgumentParser(description="MindMap CLI")
    parser.add_argument(
        "command",
        choices=["create", "add", "delete", "show", "save", "load", "search"],
        help="Command to execute"
    )
    parser.add_argument("--name", help="Node name")
    parser.add_argument("--parent", help="Parent node name")
    parser.add_argument("--file", help="Filename in data/ directory")

    args = parser.parse_args()

    ensure_data_dir()
    filename = args.file or DEFAULT_FILENAME
    full_path = os.path.join(DATA_DIR, filename)

    if args.command != "create":
        mindmap = load_mindmap(full_path)
    else:
        mindmap = MindMap("Root")

    if args.command == "create":
        print(f"Created new mind map with root '{mindmap.root.name}'.")
        mindmap.save_to_file(full_path)

    elif args.command == "add" and args.name and args.parent:
        if mindmap.add_node(args.parent, args.name):
            print(f"Added '{args.name}' under '{args.parent}'.")
            mindmap.save_to_file(full_path)

    elif args.command == "delete" and args.name:
        if mindmap.delete_node(args.name):
            print(f"Deleted '{args.name}'.")
            mindmap.save_to_file(full_path)

    elif args.command == "show":
        mindmap.display()

    elif args.command == "save":
        mindmap.save_to_file(full_path)
        print(f"Saved mind map to '{full_path}'.")

    elif args.command == "load":
        mindmap.load_from_file(full_path)
        print(f"Loaded mind map from '{full_path}'.")

    elif args.command == "search" and args.name:
        path = mindmap.search(args.name)
        if path:
            print(" > ".join(path))
        else:
            print(f"Node '{args.name}' not found.")


if __name__ == "__main__":
    main()
