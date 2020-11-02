import re


class Winners:
    def __init__(self):
        self.winners = {}
        self.answer = None

    def winners_update(self, answer, filename):
        ''' get current info from score.txt and update dic'''
        self.answer = answer
        # open file
        f = open(filename, "r")
        # extract info and add to dic
        for line in f:
            text = line.split()
            self.winners[text[0]] = int(text[1])
        # update score in the dic
        if self.answer in self.winners:
            self.winners[self.answer] += 1
        else:
            self.winners[self.answer] = 1

    def winners_rewrite(self, filename):
        ''' get a list of sorted dic and rewrite the file'''
        # sorted list
        sorted_dic = self.sorted_count()
        # rewrite file
        with open(filename, "w") as f:
            for item in sorted_dic:
                f.write(str(item[0]) + "\t" + str(item[1]) + "\n")

    def sorted_count(self):
        ''' sorted the dic and return the sorted list'''
        return sorted(
            self.winners.items(),
            key=lambda x: x[1],
            reverse=True
        )
