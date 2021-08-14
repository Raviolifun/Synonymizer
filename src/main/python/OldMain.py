# Internal imports

# External imports

# Self imports
from src.main.python import Sub_Functions as Sub_Fun

Sub_Fun.download()

value = "Nothing is original"
for i in range(20):
    value = Sub_Fun.synoantonym_string(value, "a an the i it as its no in", True)
    print(str(i) + ": " + value)


# randomly select words from books

# Sub_Fun.synoantonym_file("BeeMovie.txt", "a an the i it as its no in", True)
