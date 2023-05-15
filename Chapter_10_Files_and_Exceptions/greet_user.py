from pathlib import Path
import json

path = Path("Chapter_10_Files_and_Exceptions/text_files/username.json")
contents = path.read_text()
username = json.loads(contents)

print(f"Welcome back, {username}!")