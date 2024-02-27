def original(value):
    print(f"original: {value}")

def logging(value):
    print("before call")
    original(value)
    print("after call")

def logFile(value, file):
    print("before call")
    with open(file, "a") as f:
        f.write(f"{value}\n")
    # original(value, file)
    print("after call")
    # close file
    f.close()


original = logFile
original("example", "logFile.txt")
