"""make.fun entry: One Line, One Laugh.

Writes the entry text to /output/entry.txt for the make.fun grader.
No network, no secrets, no files outside this repository.
"""
from pathlib import Path
ENTRY = 'My Roomba filed for divorce. It said I never let it finish a room, and the dust bunnies got custody.'
OUTPUT = Path("/output/entry.txt")
def write_entry() -> Path:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(ENTRY, encoding="utf-8")
    return OUTPUT
def main() -> None:
    write_entry()
if __name__ == "__main__":
    main()
