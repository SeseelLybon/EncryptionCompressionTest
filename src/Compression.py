import time
import os

def compress():

    buffersize = 1000
    position = 0
    bufferposition = 0
    buffer = None

    time_start = time.time()
    print("Generating library", round(time.time()-time_start, 1))

    library = {}

    if os.path.exists("CompressedFile.txt"):
        os.remove("CompressedFile.txt")

    with open("FileToCompress.txt", 'r') as filetocompress:
        with open("CompressedFile.txt", 'w') as compressedfile:
            buffer = filetocompress.read(500)
            buffer2 = list()

            indextoskipto = 0

            part = 0
            while buffer != "":
                part += 1
                print(part)

                index_w_bsize = 1
                while index_w_bsize < buffersize:
                    try:
                        similiar = list()

                        for index2 in range(0, index_w_bsize):
                            if index_w_bsize >= len(buffer):
                                break

                            if buffer[index_w_bsize] == buffer[index2]:
                                buffer2.append("$")
                                index_w_bsize += 1

                            else:
                                buffer2.append(buffer[index_w_bsize])
                                '''
                                if index_w_bsize < buffersize:
                                    index_w_bsize += 1
                            elif len(similiar):
                                
                                if len(similiar) > 2:
                                    buffer2.append("$55^55$")
                                similiar = []
                            '''
                    finally:
                        index_w_bsize += 1

                compressedfile.write("".join(buffer2))

                buffer2 = list()
                buffer = filetocompress.read(500)


    # os.rename("CompressedFile.txt.tmp", "CompressedFile.txt")


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



