from pathlib import Path

# Uses Path  to find pi_digits  file, then reads and strips the contents and prints output
path = Path('Chapter_10_Files_and_Exceptions/text_files/learning_python.txt')
contents = path.read_text().rstrip()
print(contents)

#Uses splitlines to turn file into set of lines and individual loop (and print) each line
for line in contents.splitlines():
    print(line)

replace = contents.replace('Python', 'Rust')
print(replace)