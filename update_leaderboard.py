import sys
from pathlib import Path

username = sys.argv[1]
score = float(sys.argv[2])

leaderboard = Path("leaderboard.md")

# Create leaderboard if missing
if not leaderboard.exists():
    leaderboard.write_text(
        "# Leaderboard\n\n"
        "| Rank | User | Macro F1 |\n"
        "|------|------|----------|\n"
    )

lines = leaderboard.read_text().splitlines()
header = lines[:4]
rows = lines[4:]

# Remove existing user
rows = [r for r in rows if not r.startswith(f"|") or f"| {username} |" not in r]

# Add new row
rows.append(f"| 0 | {username} | {score:.4f} |")

# Sort by score desc
rows.sort(key=lambda r: float(r.split("|")[3]), reverse=True)


# Re-rank
new_rows = []
for i, r in enumerate(rows, start=1):
    parts = r.split("|")
    # Index 0 is empty (before first |), Index 1 is Rank, Index 2 is User
    parts[1] = f" {i} " 
    new_rows.append("|".join(parts))

leaderboard.write_text("\n".join(header + new_rows))
