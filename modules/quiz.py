import random
import utils
import time
# import winsound

def processAnswer(cin, partime, starttime, key, answer, curstats):
    if cin == answer:
        print "Correct!"
        if not partime == 0:
            endtime = time.clock()
            taken = endtime - starttime
            print "The time taken was " + str(taken) + " seconds."
            bonsu = 20 * (partime / (taken + partime * partime) - partime / (partime + partime * partime ) ) 
            print "Your time bonus is: " + str(bonsu)
            if curstats is not None:
                curstats.tbonsu[key] = curstats.tbonsu[key] + bonsu
                curstats.ttb = curstats.ttb + bonsu
        if curstats is not None:
            curstats.wins[key] = curstats.wins[key] + 1
            curstats.tw = curstats.tw + 1
    else:
        print "Incorrect, the correct answer is: ", answer
        if curstats is not None:
            curstats.losses[key] = curstats.losses[key] + 1
            curstats.tl = curstats.tl + 1
            # if curstats.buzzer:
            #     winsound.Beep(400, 600)

    print ""
    return

def printStartText():
    print "Welcome to Quiz mode!"
    print "Weighted randomization has been implemented"
    print "So letters you do worse in, or which haven't come up recently"
    print "are more likely."
    print "Type in the prompted answer, or \"//\" if you don't know.\n"
    print "Answering correctly counts as a success. Answering wrongly"
    print "counts as a failed attempt. Skipping a question will count"
    print "as a failed attempt as well, but you'll be immediately"
    print "prompted with the same thing so presumably you'll get it"
    print "the second time."
    print "As a reminder, type \"/exit\" to exit. If you want to check"
    print "your stats, you can type \"/stats\". The stats output is"
    print "a bit rudimentary right now, however."
    print ""
    return
    
def getPartime(curstats, data):
    print "A quiz timer has been implemented."
    print "Enter a floating-point number to select a par time in seconds."
    print "If you don't want to play with a timer, choose 0."
    partime = -1
    while partime < 0:
        try:
            cin, pcval = utils.getInput(curstats, data, "Enter another command, or choose a par time.")
            if pcval == -1:
                print "Exiting Quiz mode."
                return partime, cin
            partime = float(cin)
            if partime < 0:
                print "You need to choose a nonnegative par time."
        except:
            print "That's not a valid input."

    if partime == 0:
        print "Timed mode is OFF."
    else:
        print "Timed mode is ON, with par time set to "+ str(partime) + "."
        print "The time bonus you will receive for each correct answer is"
        print "20 * par/(time + par^2) - 20 * par/(par + par^2)"
        print "Note that entering commands will NOT reset or invalidate"
        print "the timer, except for exiting."
        print "Press <ENTER> or enter any non-command to begin."
        cin, pcval = utils.getInput(curstats, data, "Press <ENTER> or enter any non-command to begin.")
        if pcval == -1:
            print "Exiting Quiz mode."
            return partime, cin
    return partime, None



def quiz(curstats, data):
    printStartText()
    partime, cin = getPartime(curstats, data)
    if cin is not None:
        return cin

    # Trackers so more recent keys aren't as likely to be generated.
    turns = 0
    lastused = {}
    for key in curstats.wins:
        lastused[key] = 0

    while True:
        turns = turns + 1
        starttime = time.clock()
        if random.randint(0, 1) == 0:
            letter = utils.getKey(data["letters"], lastused, turns, curstats.wins, curstats.losses, data["debug"]) 
            lastused[letter] = turns
            lastused[data["morse"][letter]] = turns
            print "Type the code for: "+letter
            cin, pcval = utils.getInput(curstats, data, "Type the code for: "+letter)
            if cin == "//" or cin == "??" or cin == "idk":
                print "Okay, the correct answer is: ", data["morse"][letter]
                print "Try it!"
                curstats.losses[letter] = curstats.losses[letter] + 1
                curstats.tl = curstats.tl + 1
                cin, pcval = utils.getInput(curstats, data, "Type the code for: "+letter)
            if pcval == -1:
                print "Exiting Quiz mode."
                return cin
            processAnswer(cin.upper(), partime, starttime, letter, data["morse"][letter], curstats)
        else:
            code = utils.getKey(data["codes"], lastused, turns, curstats.wins, curstats.losses, data["debug"]) 
            lastused[code] = turns
            lastused[data["demorse"][code]] = turns
            print "Type the character for: "+code
            cin, pcval = utils.getInput(curstats, data, "Type the character for: "+code)
            if cin == "//" or cin == "??" or cin == "idk":
                print "Okay, the correct answer is: ", data["demorse"][code]
                print "Try it!"
                curstats.tl = curstats.tl + 1
                curstats.losses[code] = curstats.losses[code] + 1
                cin, pcval = utils.getInput(curstats, data, "Type the character for: "+code)
            if pcval == -1:
                print "Exiting Quiz mode."
                return cin
            processAnswer(cin.upper(), partime, starttime, code, data["demorse"][code], curstats)
