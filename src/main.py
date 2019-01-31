
import os


print("Start compressing")

temp = ""

library = {}

with open("FileToCompress.txt", 'r') as filetocompress:
    filedata = filetocompress.read()
    linenr = 0
    wordnr = 0
    for line in filedata:
        linenr += 1
        wordnr = 0
        for word in line:
            wordnr += 1
            if word not in library.keys():
                library[word] = (linenr, wordnr)

print(list(library.keys())[:100])
print(list(library.values())[:100])

print("Done compressing")