import random

# Generates a random element from arr.
def getKey(arr, lastused, turns, wins, losses, debug = False): 
    best = -99999999
    worst = 99999999
    lru = turns
    for key in arr:
        diff = wins[key] - losses[key]
        if diff > best:
            best = diff
        if diff < worst:
            worst = diff
        if lastused[key] < lru:
            lru = lastused[key]
    if debug:
        print best
        print worst
        print lru
    key = arr[random.randint(0, len(arr)-1)]
    while (best > worst and random.randint(1, (best - worst)) > (losses[key] - wins[key] + best)) or random.randint(1, turns - lru) > turns - lastused[key]:
        key = arr[random.randint(0, len(arr) - 1)]
    if debug:
        # print "Generated key: "+key
        print "Stats: " + str(wins[key]) + " " + str(losses[key])
        if best == worst:
            print "Best == worst right now."
        else:
            print "Relative probability 1: "+ str(losses[key] - wins[key] + best) + " / " + str(best - worst)
        print "Relative probability 2: " + str(turns - lastused[key])+ " / " + str(turns - lru)
    return key

def processCommand(cmd, curstats, data, addedcmd = []):
    if cmd == "/stats":
        curstats.stats()
        return 1
    if cmd == "/dstats":
        curstats.stats(data)
        return 1
    if cmd == "/debug":
        data["debug"] = not data["debug"]
        print "debug mode set to " + str(data["debug"])
        return 1
    if cmd == "/exit" or cmd == ":wq" or cmd == "/exit!": # because apparently I accidentally use vim commands sometimes
        return -1
    if cmd == "/buzzer":
        print "Wow, an easter egg!"
        curstats.buzzer = not curstats.buzzer
        return 1

    if cmd == "/help":
        print "Available commands:"
        print "/stats: Brief summary of current stats."
        print "/dstats: Detailed summary of current stats."
        print "/debug: Toggle debug mode."
        print "/help: You'll have to figure this one out yourself."
        print "/update: Fixes any compatibility issues due to code changes."
        print "/exit: Exits the current mode, or exits the program."
        print "/exit!: Exits the program."
        print "/rq: Exits the program without saving stats."
        return 1
    if cmd == "/update":
        for key in data["letters"]:
            if key not in curstats.wins:
                curstats.wins[key] = 0
            if key not in curstats.losses:
                curstats.losses[key] = 0
            if key not in curstats.tbonsu:
                curstats.tbonsu[key] = 0
        for key in data["codes"]:
            if key not in curstats.wins:
                curstats.wins[key] = 0
            if key not in curstats.losses:
                curstats.losses[key] = 0
            if key not in curstats.tbonsu:
                curstats.tbonsu[key] = 0
        print "Update successful."
        return 1
    if cmd == "/reset":
        print "Are you sure you want to reset your stats? (y to confirm)"
        cin = raw_input()
        if not cin == "y":
            print "Aborted reset attempt."
            return 1
        for key in curstats.wins:
            curstats.wins[key] = 0
            curstats.losses[key] = 0
            curstats.tbonsu[key] = 0
            curstats.tw = 0
            curstats.tl = 0
            curstats.ttb = 0
        print "Stats reset for user " + curstats.username
        return 1
    if cmd == "/rq":
        print "Are you sure you want to quit without saving? (y to confirm)"
        cin = raw_input()
        if not cin == "y":
            print "Aborted ragequit attempt."
            return 1
        return -1
    if len(cmd) > 2 and cmd[0] == "/" and cmd not in addedcmd:
        print "That's not a valid command."
        return 1
    return 0

def getInput(curstats, data, text = "", addedcmd = []):
    cin = raw_input()
    pcval = processCommand(cin.lower(), curstats, data, addedcmd)
    while pcval > 0:
        cin = raw_input(text + "\n")
        pcval = processCommand(cin.lower(), curstats, data, addedcmd)
    return cin, pcval

