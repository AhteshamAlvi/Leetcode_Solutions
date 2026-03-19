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
        # Remove unwanted directories
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]

        # Skip root-level files
        if root == ".":
            continue

        for file in files:
            ext = os.path.splitext(file)[1]

            if ext in EXT_TO_LANG:
                path = os.path.join(root, file)

                # Clean path for README
                clean_path = path.replace("./", "")

                # Folder name = problem name
                problem_name = os.path.basename(root)

                language = EXT_TO_LANG.get(ext, "Unknown")

                solutions.append((problem_name, language, clean_path))

    # Sort by problem number if present
    def extract_number(name):
        try:
            return int(name.split()[0])
        except:
            return float("inf")

    return sorted(solutions, key=lambda x: extract_number(x[0]))

def generate_table(solutions):
    table = "| Problem Name | Language | File |\n"
    table += "|-------------|----------|------|\n"

    for name, lang, path in solutions:
        table += f"| {name} | {lang} | [{path}]({path}) |\n"

    return table

def update_readme(table):
    with open(README_FILE, "r") as f:
        content = f.read()

    start = "<!-- START_TABLE -->"
    end = "<!-- END_TABLE -->"

    if start not in content or end not in content:
        print("ERROR: README missing table markers")
        return

    before = content.split(start)[0] + start + "\n"
    after = "\n" + end + content.split(end)[1]

    new_content = before + table + after

    with open(README_FILE, "w") as f:
        f.write(new_content)

if __name__ == "__main__":
    solutions = get_solutions()
    table = generate_table(solutions)
    update_readme(table)