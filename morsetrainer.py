from modules.quiz import quiz
from modules.stats import Stats
from modules.translate import translate
import modules.utils as utils


# Read in characters and codes from file
data={}
data["debug"] = False
f = open("morsetrainer.in", "r")
data["letters"] = []
data["codes"] = []
data["morse"] = {}
data["demorse"] = {}
for line in f:
    splitline = line.split(" ")
    data["morse"][splitline[0]] = splitline[1].strip()
    data["demorse"][splitline[1].strip()] = splitline[0]
    data["letters"].append(splitline[0])
    data["codes"].append(splitline[1].strip())

# Initialize stats tracker, which also has user input username
curstats = Stats(data)

print "Type \"quiz\" to play Quiz Mode or \"translate\""
print "to play translate mode. Alternatively, type any command."
print "Type \"/help\" for a list of commands."
cin, pcval = utils.getInput(curstats, data, "Enter another command or select a mode.")
cin = cin.lower()
lastcmd = cin
try:
    while pcval >= 0:
        if pcval == -1: # That would be the exit command.
            break
        elif cin == "quiz":
            # Run quiz mode, and track the return value
            # so we can see if we're exiting the program itself.
            lastcmd = quiz(data, curstats)
            if lastcmd == "/exit!" or lastcmd == "/rq": # Kind of hacky but w/e
                break
            print "Type \"/exit\" to exit Morsetrainer, or "
            print "enter a command or select a mode."
        elif cin == "translate":
            lastcmd = translate(data, curstats)
            if lastcmd == "/exit!" or lastcmd == "/rq":
                break
            print "Type \"/exit\" to exit Morsetrainer, or "
            print "enter a command or select a mode."
        else:
            print "That's not a valid input."

        cin, pcval = utils.getInput(curstats, data, "Enter another command or select a mode.")
        cin = cin.lower()
        lastcmd = cin

except: # Make sure we save in case anything breaks
    print "==ERR DETECTED=="
    print "Wow, you broke something. Although it's actually probably my fault."
    print "Try running morsetrainer again, and type /update after entering"
    print "your username. If that doesn't work, you should poke me,"
    print "let me know what happened. Saving and exiting."
    curstats.saveStats()
    raise
if not lastcmd == "/rq":
    # Save and quit.
    print "Thank you for using morsetrainer."
    curstats.stats()
    curstats.saveStats()
    print "Stats have been output to file. Exiting."
else:
    print "Ragequitting."
