import random
import utils
import time
import translate
import listen

def printStartText():
    print "Welcome to Transcribe Mode. In this mode, you will translate"
    print "period-delimited and line-delimited sentences from Morse Code, given as beeps."
    # print "As usual, type \"/exit\" to exit, and \"/help\" for a list of commands,"
    print "Standard commands are enabled for Transcribe Mode. Type \"/exit\" to exit."
    print "Note that stats are NOT currently being tracked for Transcribe Mode."
    print "Consequently, /stats will give you the stats for Listen Mode."
    print "Transcribe mode is still rather rudimentary, but it works for now."
    return



def transcribe(curstats, data):
    printStartText()
    exit = "Exiting Transcribe Mode."
    f, pcval = translate.getInputFile(curstats, data, exit)
    if pcval == -1:
        return f
    sentences, pcval = translate.processFile(f, curstats, data, exit)
    if pcval == -1:
        return sentences
    tunit, pcval = listen.inputTUnit(curstats, data)
    if pcval == -1:
        return tunit
    cin, pcval = translate.runMode(listen.playCode, sentences, curstats, data, exit, tunit)
    if pcval == -1:
        return cin
    print "That was the last sentence in the given input file."
    print exit

    return
