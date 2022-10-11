
# ******************************
# Make your Code
# ******************************

# print the words that has 'a', 'r', 'e' in sequence

words = input('Enter the list: ').split()
words_print = []
are = ['a', 'r', 'e']
idxlst = []
for i in range(len(words)):
    idxlst.append(words[i].find("a"))
    idxlst.append(words[i].find("r"))
    for j in range(1, len(words)):
        idxlst.append(words[-j].find("e"))
if idxlst == sorted(idxlst):
    
        words_print.append(words[i])
print(words_print)
