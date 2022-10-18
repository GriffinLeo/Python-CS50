ex=input("File name: ")
new_ex = ex.lower().strip()
if ".gif" in new_ex:
    print("image/gif")
elif ".jpg" in new_ex:
    print("image/jpeg")
elif ".jpeg" in new_ex:
    print("image/jpeg")
elif ".png" in new_ex:
    print("image/png")
elif ".pdf" in new_ex:
    print("application/pdf")
elif ".txt" in new_ex:
    print("text/plain")
elif ".zip" in new_ex:
    print("application/zip")
else:
    print("application/octet-stream")