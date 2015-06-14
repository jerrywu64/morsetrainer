class Stats():
    def __init__(self, data):
        print "Welcome to Morsetrainer!"
        print "Enter your username. If you don't have one,"
        print "just pick a new one and enter it."
        self.username = raw_input()
        self.wins = {}
        self.losses = {}
        self.tbonsu = {}
        self.tw = 0
        self.tl = 0
        self.ttb = 0
        try:
            statsfile = open(self.username+".stats", "r")
            for line in statsfile:
                splitline = line.split(" ")
                self.wins[splitline[0]] = int(splitline[1].strip())
                self.losses[splitline[0]] = int(splitline[2].strip())
                if len(splitline) == 3: # For old stats files.
                    self.tbonsu[splitline[0]] = 0
                else:
                    self.tbonsu[splitline[0]] = float(splitline[3].strip())
                self.tw = self.tw + self.wins[splitline[0]]
                self.tl = self.tl + self.losses[splitline[0]]
                self.ttb = self.ttb + self.tbonsu[splitline[0]]
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
            for key in data["codes"]:
                self.wins[key] = 0
                self.losses[key] = 0
                self.tbonsu[key] = 0.


    def stats(self, data = None):
        print "Your current unweighted overall stats are "
        print str(self.tw)+" successes out of "+str(self.tw+self.tl)+" attempts"
        print "which is " + str(100. * self.tw / (self.tw + self.tl)) + "%."
        print "Including time bonuses, your overall stats are "
        print str(self.tw + self.ttb)+" points out of "+str(self.tw + self.tl)+"."
        print "which is " + str(100. * (self.tw + self.ttb) / (self.tw + self.tl)) + "%."
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

