def decodeString(string, demorse):
    words = string.split("_")
    out = ""
    for word in words:
        letters = word.strip().split(" ")
        for letter in letters:
            unequalsed = ""
            letter = letter.strip()
            for char in letter:
                if char == '=':
                    unequalsed = unequalsed + '-'
                else:
                    unequalsed = unequalsed + char
            try:
                out = out + demorse[unequalsed.strip()]
            except:
                out = out + unequalsed
        out = out + " "
    return out

if __name__ == "__main__":
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
    print "This is an interface for decoding morse."
    print "Components of a single character should not be separated."
    print "Distinct letters in a word should be space-separated."
    print "Distinct words in a sentence should be underscore-separated."
    print "Equals signs may be substituted for hyphens."
    print "Press ctrl+C to exit."
    while True:
        cin = raw_input("Input code to be decoded.\n")
        print decodeString(cin, demorse)
