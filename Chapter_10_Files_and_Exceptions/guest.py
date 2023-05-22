from pathlib import Path
import os

try:
    os.remove('Chapter_10_Files_and_Exceptions/text_files/guest_list.txt')
except FileNotFoundError:
    pass

path = Path('Chapter_10_Files_and_Exceptions/text_files/guest_list.txt')

guest_amt = ['first', 'second', 'third', 'fourth', 'fifth']
guest_list = []

for g_word in guest_amt:
    guest_name = input(f"Who is the {g_word} guest? ")
    guest_list.append(guest_name)


make_guest_list = Path('Chapter_10_Files_and_Exceptions/text_files/guest_list.txt').open('a')
for guest in guest_list:
    make_guest_list.write(f"{guest}\n")
make_guest_list.close()
print(guest_list)



