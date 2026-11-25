"""make.fun entry: One Line, One Laugh.
Writes the entry text to /output/entry.txt for the make.fun grader.
No network, no secrets, no files outside this repository.
"""
from pathlib import Path
ENTRY = 'My Roomba filed for divorce. It said I never let it finish a room, and the dust bunnies got custody.'
def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")
if __name__ == "__main__":
    main()
