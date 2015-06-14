def __init__():
    pass

def encodeString(string, morse):
    words = string.split()
    out = ""
    for index in xrange(len(words)):
        word = words[index]
        for char in word:
            try:
                # print "/"+char+"/"
                out = out + morse[char]
            except:
                out = out + char
            out = out + " "
        if index < len(words) - 1:
            out = out + "_ "
    return out
if __name__ == '__main__':
    f = open("morsetrainer.in", "r")
    letters = []
    codes = []
    morse = {}
    demorse = {}
    for line in f:
        splitline = line.split(" ")
        morse[splitline[0]] = splitline[1].strip()
        demorse[splitline[1].strip()] = splitline[0]
        letters.append(splitline[0])
        codes.append(splitline[1].strip())
    # for key in morse:
        # print "/" + key + "/" + morse[key]
    print "This is an interface for encoding morse."
    print "Type an equals sign before the sentence to be encoded"
    print "to replace hyphens with equals signs."
    print "Press ctrl+C to exit."
    while True:
        cin = raw_input("Input sentence to be encoded.\n")
        cout = encodeString(cin.upper(), morse)
        if cout[0] == '=':
            subout = ""
            for i in xrange(2, len(cout)):
                if cout[i] == '-':
                    subout = subout + '='
                else:
                    subout = subout + cout[i]
            print subout
        else:
            print cout

