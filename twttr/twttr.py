s=input("Input: ")
c = "aeiouAEIOU"
for i in c:
    #if c in ["a","e","i","o","u"]:
    s=s.replace(i,"")

print("Output:",s)

