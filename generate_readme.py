import os

README_FILE = "README.md"

# Directories to ignore
SKIP_DIRS = {".git", ".github", "glsync", "__pycache__"}

# Extension → Language mapping
EXT_TO_LANG = {
    ".cpp": "C++",
    ".java": "Java",
    ".py": "Python",
    ".py3": "Python3",
    ".c": "C",
    ".cs": "C#",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".rb": "Ruby",
    ".swift": "Swift",
    ".go": "Go",
    ".kt": "Kotlin",
    ".rs": "Rust",
    ".scala": "Scala",
    ".php": "PHP",
    ".dart": "Dart",
    ".rkt": "Racket",
    ".ex": "Elixir",
    ".exs": "Elixir",
    ".erl": "Erlang",
    ".sh": "Bash",
    ".sql": "SQL",
}

def get_solutions():
    solutions = []

    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]

        if root == ".":
            continue

        for file in files:
            ext = os.path.splitext(file)[1]

            if ext in EXT_TO_LANG:
                path = os.path.join(root, file)
                clean_path = path.replace("./", "")

                folder = os.path.basename(root)

                # Extract problem number + name
                parts = folder.split(" ", 1)
                if len(parts) == 2 and parts[0].isdigit():
                    number = parts[0]
                    name = parts[1]
                else:
                    number = ""
                    name = folder

                language = EXT_TO_LANG.get(ext, "Unknown")

                # Store folder path instead of file path
                folder_path = root.replace("./", "")

                solutions.append((int(number) if number else float("inf"), number, name, language, folder_path))

    return sorted(solutions, key=lambda x: x[0])


if __name__ == "__main__":
    solutions = get_solutions()
    table = generate_table(solutions)
    update_readme(table)