# For usage inputting data.
def extract(arr, index):
    if len(arr) <= index:
        return 0
    return arr[index].strip()
class StatsModule():
    def __init__(self, data, contents, name, username):
        self.username = username
        self.name = name
        self.wins = {}
        self.losses = {}
        self.tbonsu = {}
        self.tw = 0
        self.tl = 0
        self.ttb = 0
        self.buzzer = False
        for line in contents:
            key = line[0]
            self.wins[key] = int(line[1])
            self.losses[key] = int(line[2])
            self.tbonsu[key] = float(line[3])
            self.tw = self.tw + self.wins[key]
            self.tl = self.tl + self.losses[key]
            self.ttb = self.ttb + self.tbonsu[key]
    def stats(self, data = None):
        print "Stats for "+self.name + " Mode:"
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
            print "Here are stats for each key (key success fail):"
            try:
                for key in data["letters"]:
                    print key + " " + str(self.wins[key]) + " " + str(self.losses[key]) + " " + str(self.tbonsu[key])
            except:
                pass
            try:
                for key in data["codes"]:
                    print key + " " + str(self.wins[key]) + " " + str(self.losses[key]) + " " + str(self.tbonsu[key])
            except:
                pass

               
        return


class Stats():
    def __init__(self, data):
        print "Welcome to Morsetrainer!"
        print "Enter your username. If you don't have one,"
        print "just pick a new one and enter it."
        self.username = ""
        while self.username == "":
            self.username = raw_input().strip()
        quizlines = []
        listenlines = []
        self.keys = []
        newuser = False
        try:
            statsfile = open(self.username+".stats", "r")
            for line in statsfile:
                splitline = line.split(" ")
                key = splitline[0]
                self.keys.append(key)
                quizline = []
                listenline = []
                quizline.append(key)
                listenline.append(key)

                for i in xrange(1, 4):
                    quizline.append(extract(splitline, i))
                for i in xrange(4, 7):
                    listenline.append(extract(splitline, i))
                quizlines.append(quizline)
                listenlines.append(listenline)

            statsfile.close()
            print "Welcome back, "+self.username+"."
        except:
            newuser = True
            print "Welcome, "+self.username+". I see you are a new user."
            print "Just follow the instructions and everything should be ok."
            for key in data["letters"]:
                quizline = []
                listenline = []
                quizline.append(key)
                listenline.append(key)
                for i in xrange(0, 3):
                    quizline.append(0)
                    listenline.append(0)
                quizlines.append(quizline)
                listenlines.append(listenline)

            for key in data["codes"]:
                quizline = []
                listenline = []
                quizline.append(key)
                listenline.append(key)
                for i in xrange(0, 3):
                    quizline.append(0)
                    listenline.append(0)
                quizlines.append(quizline)
                listenlines.append(listenline)
        self.quiz = StatsModule(data, quizlines, "Quiz", self.username)
        self.listen = StatsModule(data, listenlines, "Listen", self.username)
        if not newuser:
            self.stats()
    

    def stats(self, data = None):
        print "The stats output is not currently operational, sorry."
        return
#        print "Your current unweighted overall stats are "
#        print str(self.tw)+" successes out of "+str(self.tw+self.tl)+" attempts"
#        if self.tw + self.tl > 0:
#            print "which is " + str(100. * self.tw / (self.tw + self.tl)) + "%."
#        print "Including time bonuses, your overall stats are "
#        print str(self.tw + self.ttb)+" points out of "+str(self.tw + self.tl)+"."
#        if self.tw + self.tl > 0:
#            print "which is " + str(100. * (self.tw + self.ttb) / (self.tw + self.tl)) + "%."
#        if self.tw > 0:
#            print "Your average time bonus per correct answer is " + str(self.ttb / self.tw) + "."
#        if not data == None:
#            print "Here are stats for each letter and code (key success fail):"
#            for key in data["letters"]:
#                print key + " " + str(self.wins[key]) + " " + str(self.losses[key]) + " " + str(self.tbonsu[key])
#            for key in data["codes"]:
#                print key + " " + str(self.wins[key]) + " " + str(self.losses[key]) + " " + str(self.tbonsu[key])
#               
#        return

    def saveStats(self):
        print "Stats are now being saved to file."
        statsfile = open(self.username+".stats", "w")
        for item in self.keys:
            # print "Writing key: "+item
            line = item + " "
            line = line + str(self.quiz.wins[item]) + " "
            line = line + str(self.quiz.losses[item]) + " "
            line = line + str(self.quiz.tbonsu[item]) + " "
            line = line + str(self.listen.wins[item]) + " "
            line = line + str(self.listen.losses[item]) + " "
            line = line + str(self.listen.tbonsu[item]) + " "
            statsfile.write(line + "\n")
        statsfile.close()
        return

