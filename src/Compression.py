import time
import os

def compress():

    buffersize = 100
    position = 0
    buffer = None

    time_start = time.time()
    print("Generating library", round(time.time()-time_start, 1))

    library = {}

    if os.path.exists("CompressedFile.txt"):
        os.remove("CompressedFile.txt")

    with open("FileToCompress.txt", 'rb') as filetocompress:
        with open("CompressedFile.txt", 'wb') as compressedfile:
            buffer = filetocompress.read(buffersize)
            for i in buffer:
                print(i)


    print(len(library))
    print("Generated compressed file", round(time.time() - time_start, 1))
    return
'''
    linenr = 0
    for line in filetocompress.readlines():
        linenr += 1
        wordnr = 0
        temp = []
        for word in line.split(" "):
            wordnr += 1
            if word not in library.keys():
                library[word] = (linenr, wordnr)

            rewrittentuple = rewrite_tuple(library[word])
        
            if word in library.keys():
                if len(rewrittentuple) < len(word):
                    temp.append(rewrittentuple)
                else:
                    temp.append(word)
            else:
                temp.append(word)
        temp = " ".join(temp)
        compressedfile.write(temp)
'''


def rewrite_tuple(torewrite):
    return "$"+str(torewrite[0])+"^"+str(torewrite[1])+"$"



