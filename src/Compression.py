import time
import os

def compress():
    time_start = time.time()
    print("Generating library", round(time.time()-time_start, 1))

    library = {}

    with open("FileToCompress.txt", 'r') as filetocompress:
        with open("CompressedFile.txt", 'w') as compressedfile:
            linenr = 0
            for line in filetocompress.readlines():
                linenr += 1
                wordnr = 0
                for word in line.split(" "):
                    wordnr += 1
                    if word not in library.keys():
                        library[word] = (linenr, wordnr)

    print(len(library))
    print("Generated Library\n"+
          "Generating compressed file", round(time.time()-time_start, 1))

    if os.path.exists("CompressedFile.txt"):
        os.remove("CompressedFile.txt")

    with open("FileToCompress.txt", 'r') as filetocompress:
        with open("CompressedFile.txt", 'w') as compressedfile:
            for line in filetocompress.readlines():
                temp = []
                for word in line.split(" "):
                    if word in library.keys():
                        rewrittentuple = rewrite_tuple(library[word])
                        if len(rewrittentuple) < len(word):
                            temp.append(rewrittentuple)
                        else:
                            temp.append(word)
                    else:
                        temp.append(word)
                temp = " ".join(temp)
                compressedfile.write(temp)
    print("Generated compressed file", round(time.time() - time_start, 1))
    return


def rewrite_tuple(torewrite):
    return "$"+str(torewrite[0])+"^"+str(torewrite[1])+"$"



