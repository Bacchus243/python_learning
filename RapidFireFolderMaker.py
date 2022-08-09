# The url below contains instructions for building this python script.

# https://www.geeksforgeeks.org/make-multiple-directories-based-on-a-list-using-python/





import os

root_path = '/Users/trenton/Library/CloudStorage/OneDrive-ArizonaStateUniversity/Python Testing'

list = ['Module 01 - Intro & Java Programming',
        'Module 02 - Data Types and Variables',
        'Module 03 - Decisions',
        'Module 04 - Loops',
        'Module 05 - Methods Part 1 User Defined Methods',
        'Module 06 - Methods Part 2 Scope and Mechanics',
        'Module 07 - Arrays Part 1',
        'Module 08 - Arrays Part 2 Multidimensional Arrays and Arraylists',
        'Module 09 - Objects and Classes Part 1',
        'Module 10 - Objects and Classes Part 2',
        'Module 11 - Objects and Classes Part 3',
        'Module 12 - Objects and Classes Part 4',
        'Module 13 - Exceptions and File Input and Output',
        'Module 14 - Review and Advanced Topics']

for items in list:
    path = os.path.join(root_path, items)
    os.mkdir(path)
