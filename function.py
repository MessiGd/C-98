def countingwordsfromfile():
    a = input("Enter the file name:")
    numberofwords = 0
    file = open(a,'r')
    for line in file:
        words = line.split()
        numberofwords = numberofwords + len(words)
    print("Number of words:", numberofwords) 

countingwordsfromfile()   