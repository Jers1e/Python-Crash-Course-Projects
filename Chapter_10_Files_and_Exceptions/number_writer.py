from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]

path = Path('Chapter_10_Files_and_Exceptions/text_files/numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)