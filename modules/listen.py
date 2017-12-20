import random
import utils
import time
import quiz
import threading

def printStartText():
    print "Welcome to Listen Mode!"
    print "Listen Mode is like Quiz Mode except you will only translate"
    print "from Morse to English, and you will hear beeps instead of"
    print "seeing a visual representation of the Morse Code."
    print "As in Quiz Mode, type \"//\" if you don't know the answer."
    print "Type \"/replay\" to replay the sound."
    print "As a reminder, type \"/exit\" to exit."
    print "Right now, Quiz Mode and Listen Mode stats are not distinct."

def run_async(f):
    def g(*args, **kwargs):
        threading.Thread(target=f, args=args, kwargs=kwargs).start()
    return g


@run_async
def playCode(code, tunit):
    freq = 800 # Frequency in Hertz
    prior = 0 # Track prior character to robustly pause between beeps
    for char in code:
        if char == '.':
            if prior == 0:
                time.sleep(tunit / 1000.) # 1 unit between beeps
            if prior == -1:
                time.sleep(tunit / 1000. * 3) # 3 units between chars
            utils.beep(freq, tunit)
            prior = 0
        elif char == '-' or char == '=':
            if prior == 0:
                time.sleep(tunit / 1000.)
            if prior == -1:
                time.sleep(tunit / 1000. * 3) # 3 units between chars
            utils.beep(freq, 3 * tunit)
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

def inputTUnit(curstats, data):
    print "Specify a unit time in milliseconds. This will be the length"
    print "of a dot. The recommended time is 120. Note that the sound"
    print "may not play correctly if the unit time is too short."
    tunit = -1
    while tunit <= 0:
        tunit, pcval = utils.getInput(curstats, data, "Specify a unit time in ms.")
        if pcval == -1:
            return tunit, pcval
        try:
            tunit = int(tunit)
            if tunit <= 0:
                print "Specify a positive integer time."
            tunit = tunit + 0 # Verify that it's not a string somehow
        except:
            print "Specify a positive integer time."
            tunit = -1
    return tunit, 0


def listen(curstats, data):
    printStartText()
    tunit, pcval = inputTUnit(curstats, data)
    if pcval == -1:
        return tunit


    # Trackers so more recent keys aren't as likely to be generated.
    turns = 0
    lastused = {}
    for key in curstats.wins:
        lastused[key] = 0
    adcmd = []
    adcmd.append("/replay")
    adcmd.append("/repeat")

    while True:
        turns = turns + 1
        # starttime = time.clock()
        key = utils.getKey(data["codes"], lastused, turns, curstats.wins, curstats.losses, data["debug"]) 
        lastused[key] = turns
        lastused[data["demorse"][key]] = turns
        print "Type the character for the following: "
        playCode(key, tunit)
        cin, pcval = utils.getInput(curstats, data, "Type /replay to replay the code.", adcmd)
        while cin == "/replay" or cin == "/repeat": 
            playCode(key, tunit)
            cin, pcval = utils.getInput(curstats, data, "Type /replay to replay the code.", adcmd)
        
        if cin == "//" or cin == "??" or cin == "idk":
            print "Okay, the correct answer is: ", data["demorse"][key]
            print "Try it!"
            # curstats.losses[key] = curstats.losses[key] + 1
            # curstats.tl = curstats.tl + 1
            cin, pcval = utils.getInput(curstats, data, "Type /replay to replay the code.", adcmd)
        if pcval == -1:
            print "Exiting Listen Mode."
            return cin
        while cin == "/replay" or cin == "/repeat":
            playCode(key, tunit)
            cin, pcval = utils.getInput(curstats, data, "Type /replay to replay the code.", adcmd)
        quiz.processAnswer(cin.upper(), 0, 0, key, data["demorse"][key], curstats)

