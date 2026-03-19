import os

README_FILE = "README.md"

def get_solutions():
    solutions = []

    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith((
                # Core languages
                ".cpp",   # C++
                ".java",  # Java
                ".py3",   # Python3 (occasionally shows up)
                ".py",    # Python
                ".c",     # C
                ".cs",    # C#
                ".js",    # JavaScript
                ".ts",    # TypeScript
                ".rb",    # Ruby
                ".swift", # Swift
                ".go",    # Go
                ".kt",    # Kotlin
                ".rs",    # Rust
                ".scala", # Scala
                ".php",   # PHP
                ".dart",  # Dart

                # Functional / niche langs
                ".rkt",   # Racket
                ".ex",    # Elixir
                ".exs",   # Elixir script
                ".erl",   # Erlang

                # Shell / scripting
                ".sh",    # Bash

                # SQL / data
                ".sql",   # MySQL / PostgreSQL / Oracle
                ".psql",  # PostgreSQL alt
            )):
                path = os.path.join(root, file)

                # Skip hidden/system files
                if ".git" in path:
                    continue

                name = file.replace("_", " ").replace(".py", "").replace(".cpp", "").replace(".java", "").replace(".c", "")
                language = file.split(".")[-1]

                solutions.append((name.title(), language, path))

    return sorted(solutions)

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

    before = content.split(start)[0] + start + "\n"
    after = "\n" + end + content.split(end)[1]

    new_content = before + table + after

    with open(README_FILE, "w") as f:
        f.write(new_content)

if __name__ == "__main__":
    solutions = get_solutions()
    table = generate_table(solutions)
    update_readme(table)