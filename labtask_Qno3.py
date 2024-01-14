class TreeNode:
    def __init__(self, name, is_directory=False):
        self.name = name
        self.is_directory = is_directory
        self.children = {}

class FileSystem:
    def __init__(self):
        self.root = TreeNode("/")

    def create(self, path, is_directory=False):
        current_node = self.root
        components = path.strip("/").split("/")
        
        for component in components:
            if component not in current_node.children:
                current_node.children[component] = TreeNode(component, is_directory)
            current_node = current_node.children[component]

    def delete(self, path):
        current_node = self.root
        components = path.strip("/").split("/")
        
        for component in components:
            if component not in current_node.children:
                raise FileNotFoundError(f"File or directory '{path}' not found.")
            current_node = current_node.children[component]

        if current_node.children:
            raise ValueError(f"Cannot delete non-empty directory '{path}'.")
        del current_node.parent.children[current_node.name]

    def retrieve(self, path):
        current_node = self.root
        components = path.strip("/").split("/")
        
        for component in components:
            if component not in current_node.children:
                raise FileNotFoundError(f"File or directory '{path}' not found.")
            current_node = current_node.children[component]

        return current_node

# Example Usage:
file_system = FileSystem()

# Creating directories and files
file_system.create("/documents", is_directory=True)
file_system.create("/documents/text_files", is_directory=True)
file_system.create("/documents/pictures", is_directory=True)
file_system.create("/documents/text_files/report.txt")
file_system.create("/documents/text_files/note.txt")
file_system.create("/documents/pictures/vacation.jpg")

# Retrieving a file
file_node = file_system.retrieve("/documents/text_files/report.txt")
print(f"File found: {file_node.name}")

# Deleting a file
file_system.delete("/documents/text_files/note.txt")

# Deleting a directory
file_system.delete("/documents/pictures")

# Trying to retrieve a non-existent file
try:
    file_system.retrieve("/nonexistent/file.txt")
except FileNotFoundError as e:
    print(e)
