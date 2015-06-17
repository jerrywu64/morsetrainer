import random
import utils
import time
import winsound
import quiz

def printStartText():
    print "Welcome to Listen Mode!"
    print "Listen Mode is like Quiz Mode except you will only translate"
    print "from Morse to English, and you will hear beeps instead of"
    print "seeing a visual representation of the Morse Code."
    print "As in Quiz Mode, type \"//\" if you don't know the answer."
    print "Type \"/replay\" to replay the sound."
    print "As a reminder, type \"/exit\" to exit."
    print "Stats are not currently being tracked for Listen Mode, so"
    print "/stats will give stats for Quiz Mode."

def playCode(code, tunit):
    freq = 800 # Frequency in Hertz
    prior = 0 # Track prior character to robustly pause between beeps
    for char in code:
        if char == '.':
            if prior == 0:
                time.sleep(tunit / 1000.) # 1 unit between beeps
            if prior == -1:
                time.sleep(tunit / 1000. * 3) # 3 units between chars
            winsound.Beep(freq, tunit)
            prior = 0
        elif char == '-' or char == '=':
            if prior == 0:
                time.sleep(tunit / 1000.)
            if prior == -1:
                time.sleep(tunit / 1000. * 3) # 3 units between chars
            winsound.Beep(freq, 3 * tunit)
            prior = 0
        elif char == " ":
            if not prior == 1:
                prior = -1
        elif char == "_":
            time.sleep(tunit / 1000. * 7)
            prior = 1
        else:
            print "Error: detected unplayable character, skipping"
            continue
    return   

def listen(curstats, data):
    printStartText()
    print "Specify a unit time in milliseconds. This will be the length"
    print "of a dot. The recommended time is 120. Note that the sound"
    print "may not play correctly if the unit time is too short."
    tunit = -1
    while tunit <= 0:
        tunit, pcval = utils.getInput(curstats, data, "Specify a unit time in ms.")
        if pcval == -1:
            return tunit
        try:
            tunit = int(tunit)
            if tunit <= 0:
                print "Specify a positive integer time."
        except:
            print "Specify a positive integer time."


    # Trackers so more recent keys aren't as likely to be generated.
    turns = 0
    lastused = {}
    for key in curstats.wins:
        lastused[key] = 0

    while True:
        turns = turns + 1
        # starttime = time.clock()
        key = utils.getKey(data["codes"], lastused, turns, curstats, data["debug"]) 
        lastused[key] = turns
        lastused[data["demorse"][key]] = turns
        print "Type the character for the following: "
        playCode(key, tunit)
        cin, pcval = utils.getInput(curstats, data, "Type /replay to replay the code.")
        while cin == "/replay" or cin == "/repeat": 
            playCode(key, tunit)
            cin, pcval = utils.getInput(curstats, data, "Type /replay to replay the code.")
        
        if cin == "//" or cin == "??" or cin == "idk":
            print "Okay, the correct answer is: ", data["demorse"][key]
            print "Try it!"
            # curstats.losses[key] = curstats.losses[key] + 1
            # curstats.tl = curstats.tl + 1
            cin, pcval = utils.getInput(curstats, data, "Type /replay to replay the code.")
        if pcval == -1:
            print "Exiting Listen Mode."
            return cin
        while cin == "/replay" or cin == "/repeat":
            playCode(key, tunit)
            cin, pcval = utils.getInput(curstats, data, "Type /replay to replay the code.")
        quiz.processAnswer(cin.upper(), 0, 0, key, data["demorse"][key], None)

