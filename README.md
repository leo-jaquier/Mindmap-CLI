# Mindmap-CLI

**Mindmap-CLI** is a command-line tool designed to create and manage mind maps directly from your terminal. This project was developed as a technical test and serves as a foundational implementation for CLI-based mind mapping.

## Features

- Create hierarchical mind maps using a simple command-line interface
- Add, edit, delete, and search nodes
- Store and retrieve mind maps using JSON files
- Lightweight and Python-based

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/leo-jaquier/Mindmap-CLI.git
   cd Mindmap-CLI
   ```
2. **Ensure you have Python installed (version 3.6 or higher).**
3. **(Optional) Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
## Usage
  Run the CLI tool with:
  ```bash
  python cli.py
  ```
  Or run specific commands as described below.
## Example Test
Here’s an example of creating and interacting with a mind map:
```bash
python cli.py create
python cli.py add --parent Root --name "Idea 1"
python cli.py add --parent "Idea 1" --name "Subidea A"
python cli.py show
```
**Expected Output:**
```bash
Created new mind map with root 'Root'.
Added 'Idea 1' under 'Root'.
Added 'Subidea A' under 'Idea 1'.
- Root
  - Idea 1
    - Subidea A
```
**Save and Load Mind Map**
```bash
python cli.py save --file mindmap.json
python cli.py load --file mindmap.json
```
**Expected Behavior:**

A file named mindmap.json is created inside the data folder.

The mind map is correctly loaded from this file.

**Search a Node**
```bash
python cli.py search --name "Subidea A"
```
**Expected Output:**
```bash
Root > Idea 1 > Subidea A
```
## Project Structure

  <code>cli.py</code>  – Main CLI entry point

  <code>mindmap/</code>  – Module containing logic for mind map manipulation

  <code> data/</code>  – Folder where mind maps are stored as JSON files
