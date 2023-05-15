from pathlib import Path

# Uses Path  to find pi_digits  file, then reads and strips the contents and prints output
path = Path('pi_digits.txt')
contents = path.read_text().rstrip()
print(contents)

#Uses splitlines to turn file into set of lines and individual loop (and print) each line
lines = contents.splitlines()
for line in lines:
    print(line)

#Starts with an empty string, fills it with the lines from above and prints the length and len count
pi_string = ''
for line in lines:
    pi_string += line.lstrip()
print(f"{pi_string[:52]}...")
print(len(pi_string))

