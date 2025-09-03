import os
import markdown

def validate_paths(root_dir):
    """Check if all referenced paths in the project exist."""
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename == '.DS_Store':
                continue  # Skip macOS system files

            filepath = os.path.join(dirpath, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if filename.endswith('.md'):
                        # Check for links in Markdown files
                        md = markdown.Markdown()
                        for line in content.splitlines():
                            if '(' in line and ')' in line:
                                link = line.split('(')[-1].split(')')[0]
                                if not os.path.exists(link):
                                    print(f"Broken link in {filepath}: {link}")
            except (UnicodeDecodeError, IOError) as e:
                print(f"Error reading {filepath}: {e}")

if __name__ == "__main__":
    project_root = os.path.dirname(os.path.abspath(__file__))
    validate_paths(project_root)
