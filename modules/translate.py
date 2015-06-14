import random
from encode import encodeString
from decode import decodeString

def translate(data, curstats):
    print "Welcome to Translate Mode. In this mode, you will translate"
    print "period-delimited and line-delimited sentences both to and from Morse Code."
    # print "As usual, type \"/exit\" to exit, and \"/help\" for a list of commands,"
    print "Commands are not enabled for Translate mode. Type \"/exit\" to exit."
    print "Note that stats are NOT currently being tracked for Translate Mode."
    print "Translate mode is still rather rudimentary, but it works for now."
    f = None
    while f is None:
        filename = raw_input("Specify an input file for sample translation text.\n")
        try:
            # while processCommand(filename) > 0:
            #    filename = raw_input("Specify an input file for sample translation text.\n")
            f = open(filename, "r")
        except:
            print "Error, invalid input file given."
    sentences = []
    for line in f:
        splitline = line.split(".")
        for sentence in splitline:
            sentence = sentence.strip().upper()
            modified = ""
            for char in sentence:
                if char in data["letters"] or char == ' ':
                    modified= modified + char 
            if not sentence == "":
                sentences.append(modified)
    print "Fileread successful. Sentences will be given to you in random order."
    random.shuffle(sentences)
    # print sentences
    for sentence in sentences:
        if random.randint(0, 1) == 0:
            print "Translate the following sentence into Morse Code:"
            encoded = encodeString(sentence, data["morse"])
            print decodeString(encoded, data["demorse"]) # sigh stupid edge cases
            cin = raw_input()
            if cin == "/exit" or cin == "/exit!":
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
            cin = raw_input()
            if cin == "/exit" or cin == "/exit!":
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

