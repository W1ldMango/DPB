

list = ["Alex;15","Max;12","Martin;16"]
path = '/Users/wildmango/PycharmProjects/DPB/test1.csv'

def save_persons(path, array=None):
    with open(path,'w') as file:
        for i in range(len(array)):
            file.write(str(array[i]) + '\n')

save_persons(path,list)
def load_persons(path):
    with open(path,'r+') as file:
        data = file.read().splitlines()
        for i in range(len(data)):
            name = data[i].split(";")[0]
            age = data[i].split(";")[1]
            print("name:",name,"age:",age)
load_persons(path)

import collections
path_text = '/Users/wildmango/PycharmProjects/DPB/book.txt'
def text_analysis(path):
    with open(path,'r+') as file:
        fileR = file.read().lower()
        letter = collections.Counter(fileR.lower())
        letter_sorted = sorted(letter.items(),key=lambda k:k[-1])
        #print(letter_sorted)

        words = collections.Counter(fileR.split(" "))
        #print(words)
        return words, letter_sorted

#text_analysis(path_text)

words, letters = text_analysis(path_text)

#n - count of words
#m - len of word
#print("new")
def get_words(n,m,struct):
    for i in struct.items():
        if n == 0:
            break
        if "\n" in i[0]:
            str = i[0].split("\n")
            #print(str)
            for j in range(len(str)):
                size = len(str[j])
                if size > m:
                    print(str[j])
                    n -= 1
        elif len(i[0]) > m:
            print(i[0])
            n -= 1

#get_words(20,8,words)

cypher_path_in = "/Users/wildmango/PycharmProjects/DPB/cypher_in"
cypher_path_out = "/Users/wildmango/PycharmProjects/DPB/cypher_out.txt"
decypher_path_out = "/Users/wildmango/PycharmProjects/DPB/decypher_out.txt"

def cypher(path_in,path_out):
    with open(path_in, "r+") as IN:
        file = IN.read()
        new_file = " ".join(reversed(file)).lower().replace("a", "???")
    with open(path_out,"w") as OUT:
        OUT.write(new_file)

cypher(cypher_path_in,cypher_path_out)

def decypher(path_in,path_out):
    with open(path_in,"r+") as IN:
        file = IN.read()
        new_file = "".join(reversed(file)).replace("???", "a").replace(" ", "")
    with open(path_out,"w") as OUT:
        OUT.write(new_file)

decypher(cypher_path_out,decypher_path_out)