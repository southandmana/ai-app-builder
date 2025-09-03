import os

def check_paths(root_dir):
    """Scan all files in the project and check if referenced paths exist."""
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            try:
                with open(filepath, 'r') as f:
                    content = f.read()
                    for line in content.splitlines():
                        if 'path/to/' in line:  # Adjust this to match your path patterns
                            referenced_path = line.split('path/to/')[1].strip()
                            if not os.path.exists(referenced_path):
                                print(f"Broken path in {filepath}: {referenced_path}")
            except Exception as e:
                print(f"Error reading {filepath}: {e}")

if __name__ == "__main__":
    project_root = os.path.dirname(os.path.abspath(__file__))
    check_paths(project_root)
