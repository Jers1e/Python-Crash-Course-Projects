from pathlib import Path
import json

path = Path('Chapter_10_Files_and_Exceptions/text_files/numbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)