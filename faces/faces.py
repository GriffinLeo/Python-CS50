def main():
    text = convert(input(""))
    print(text)


def convert(a):
    a = a.replace(":)","🙂")
    a = a.replace(":(","🙁")
    return a


main()