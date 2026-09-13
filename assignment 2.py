with open("file.txt","r")as f:
    data=f.read()
    print("word",":",len(data.split()))
    print("line",":",len(data.splitlines()))
    print("character",":",len(data))
    