def main():
    string = input("camelCase: ")
    print("snake_case: ",end="")
    snake_case(string)

def snake_case(string):
    for character in string:
        if character.isupper():
            print("_" + character.lower(), end="")
        else:
            print(character, end="")
    print()


main()


