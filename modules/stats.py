# For usage inputting data.
def extract(arr, index):
    if len(arr) <= index:
        return 0
    return arr[index].strip()
class Stats():
    def __init__(self, data):
        print "Welcome to Morsetrainer!"
        print "Enter your username. If you don't have one,"
        print "just pick a new one and enter it."
        self.username = ""
        while self.username == "":
            self.username = raw_input().strip()
        self.wins = {}
        self.losses = {}
        self.tbonsu = {}
        self.lwins = {}
        self.llosses = {}
        self.ltbonsu = {}
        self.tw = 0
        self.tl = 0
        self.ttb = 0
        self.ltw = 0
        self.ltl = 0
        self.lttb =0
        try:
            statsfile = open(self.username+".stats", "r")
            for line in statsfile:
                splitline = line.split(" ")
                key = splitline[0]
                self.wins[key] = int(extract(splitline, 1))
                self.losses[key] = int(extract(splitline, 2))
                self.tbonsu[key] = float(extract(splitline, 3))
                self.lwins[key] = int(extract(splitline, 4))
                self.llosses[key] = int(extract(splitline, 5))
                self.ltbonsu[key] = int(extract(splitline, 6))

                self.tw = self.tw + self.wins[key]
                self.tl = self.tl + self.losses[key]
                self.ttb = self.ttb + self.tbonsu[key]
                self.ltw = self.ltw + self.lwins[key]
                self.ltl = self.ltl + self.llosses[key]
                self.lttb = self.lttb + self.ltbonsu[key]
            statsfile.close()
            print "Welcome back, "+self.username+"."
            self.stats()
        except:
            print "Welcome, "+self.username+". I see you are a new user."
            print "Just follow the instructions and everything should be ok."
            for key in data["letters"]:
                self.wins[key] = 0
                self.losses[key] = 0
                self.tbonsu[key] = 0.
                self.lwins[key] = 0
                self.llosses[key] = 0
                self.ltbonsu[key] = 0.
            for key in data["codes"]:
                self.wins[key] = 0
                self.losses[key] = 0
                self.tbonsu[key] = 0.
                self.lwins[key] = 0
                self.llosses[key] = 0
                self.ltbonsu[key] = 0.
    

    def stats(self, data = None):
        print "Your current unweighted overall stats are "
        print str(self.tw)+" successes out of "+str(self.tw+self.tl)+" attempts"
        if self.tw + self.tl > 0:
            print "which is " + str(100. * self.tw / (self.tw + self.tl)) + "%."
        print "Including time bonuses, your overall stats are "
        print str(self.tw + self.ttb)+" points out of "+str(self.tw + self.tl)+"."
        if self.tw + self.tl > 0:
            print "which is " + str(100. * (self.tw + self.ttb) / (self.tw + self.tl)) + "%."
        if self.tw > 0:
            print "Your average time bonus per correct answer is " + str(self.ttb / self.tw) + "."
        if not data == None:
            print "Here are stats for each letter and code (key success fail):"
            for key in data["letters"]:
                print key + " " + str(self.wins[key]) + " " + str(self.losses[key]) + " " + str(self.tbonsu[key])
            for key in data["codes"]:
                print key + " " + str(self.wins[key]) + " " + str(self.losses[key]) + " " + str(self.tbonsu[key])
               
        return

    def saveStats(self):
        print "Stats are now being saved to file."
        statsfile = open(self.username+".stats", "w")
        for item in self.wins:
            statsfile.write(item + " " + str(self.wins[item]) + " " + str(self.losses[item])+" " + str(self.tbonsu[item]) + "\n")
        statsfile.close()
        return

