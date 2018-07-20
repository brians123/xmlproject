dict={}

def main():
    poem = open("poem.txt", "r")
    for row in poem:
        myList = row.split() 
        for word in myList:
            #print (word)
            if word.endswith(('.', '!', ',', ';', '\'s', '\'')):
                word = word[:-1]
            word = word.lower()
            if word in dict:
                counter = dict[word]
                counter = counter + 1
                dict[word] = counter
            else:
                dict[word] = 1
    """for key in dict:
        print key, dict[key]"""
    #sort the keys in descending order from highest to lowest
    sortedKeys = sorted(dict, key=dict.get, reverse = True)
    for key in sortedKeys:
        print key, dict[key]
if __name__=="__main__":
    main()