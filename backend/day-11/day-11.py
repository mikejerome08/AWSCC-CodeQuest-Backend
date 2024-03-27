try:
    with open("names.txt", "r") as f:
        names = f.readlines()
    names = [name.strip() for name in names]
    names.sort()

    with open("names.txt", "w") as f:
        for name in names:
            f.write(name + "\n")

    print("Names have been sorted alphabetically and written back to the file.")

except:
    print("File not found")