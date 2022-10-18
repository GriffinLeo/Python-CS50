'''In deep.py, implement a program that prompts the user for the answer to the Great Question of Life,
the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.'''

d=input("What is the Answer to the Great Question of Life, the Universe, and Everything  ?")
if d.strip() == "42":
    print("Yes")
elif d.lower().strip() == "forty-two":
    print("Yes")
elif d.lower().strip() == "forty two":
    print("Yes")
else:
    print("No")
