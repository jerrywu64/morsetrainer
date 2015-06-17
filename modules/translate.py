import random
from encode import encodeString
from decode import decodeString
import utils

def translate(curstats, data):
    print "Welcome to Translate Mode. In this mode, you will translate"
    print "period-delimited and line-delimited sentences both to and from Morse Code."
    # print "As usual, type \"/exit\" to exit, and \"/help\" for a list of commands,"
    print "Standard commands are enabled for Translate Mode. Type \"/exit\" to exit."
    print "Note that stats are NOT currently being tracked for Translate Mode."
    print "Consequently, /stats will give you the stats for Quiz Mode."
    print "Translate mode is still rather rudimentary, but it works for now."
    f = None
    while f is None:
        print "Specify an input file for sample translation text."
        filename, pcval = utils.getInput(curstats, data, "Specify an input file for sample translation text.")
        if pcval == -1:
            print "Exiting Translate Mode."
            return filename
        try:
            f = open(filename, "r")
        except:
            print "Error, invalid input file given."
    sentences = []
    for line in f:
        # Splitting by periods and lines, essentially. Rudimentary and doesn't work super well but whatever.
        splitline = line.split(".") 
        for sentence in splitline:
            sentence = sentence.strip().upper()
            modified = ""
            for char in sentence:
                if char in data["letters"] or char == ' ':
                    modified= modified + char 
            if not sentence == "":
                sentences.append(modified)
    print "Fileread successful. Do you want to randomize the order of the input sentences? (y/n)"
    while True:
        rand, pcval = utils.getInput(curstats, data, "Do you want to randomize the order of the input sentences? (y/n)")
        if pcval == -1:
            print "Exiting Translate Mode."
            return rand
        if rand.lower() == "y":
            random.shuffle(sentences)
            print "Sentence order randomized."
            break
        if rand.lower() == "n":
            print "Sentence order preserved."
            break
    # print sentences
    for sentence in sentences:
        if random.randint(0, 1) == 0:
            print "Translate the following sentence into Morse Code:"
            encoded = encodeString(sentence, data["morse"])
            print decodeString(encoded, data["demorse"]) # sigh stupid edge cases
            cin, pcval = utils.getInput(curstats, data, "Translate the following sentence into Morse Code:\n"+decodeString(encoded, data["demorse"]))
            if pcval == -1:
                 print "Exiting Translate Mode."
                 return cin
            decoded = decodeString(cin, data["demorse"])
            if cin.strip() == encoded.strip():
                print "Correct!"
            else:
                print "Incorrect. Your input decodes as:"
                print decoded
                print "and the correct translation is"
                print encoded
        else:
            print "Translate the following Morse Code into English:"
            encoded = encodeString(sentence, data["morse"])
            print encoded
            decoded = decodeString(encoded, data["demorse"]) # yay edge cases again
            cin, pcval = utils.getInput(curstats, data, "Translate the following Morse Code into English:\n"+encoded)
            if pcval == -1:
                print "Exiting Translate Mode."
                return cin
            if cin.upper().strip() == decoded.strip():
                print "Correct!"
            else:
                print "Incorrect. The correct translation is:"
                print decoded.strip()
                print "and your input encodes as"
                print encodeString(cin.upper().strip(), data["morse"])
    print "That was the last sentence in the given input file."
    print "Exiting Translate Mode."
    return

