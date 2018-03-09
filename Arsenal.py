import csv                                      #imports csv functions
import operator                                 #sorts csv by column

csvfile = open('201718.csv', 'r')
csv1 = csv.reader(csvfile, delimiter=',')


class SortSystem:
    def __init__(self, entercsv):
        self.csv1 = entercsv
        self.firstline = True


    def __repr__(self):
        return 'This is a data analysis system'


    def organise(self):
        sort = sorted(self.csv1, key=operator.itemgetter(0))
        for eachline in sort:
            print(eachline)

        return '\nOrganised by team in alphabetical order'


    def scores(self):
        for eachline in self.csv1:
            if self.firstline:
                self.firstline = False
                continue
            print(eachline)
        return '\nFull scoresheet'


    def lower(self):
        for eachline in self.csv1:
            if self.firstline:
                self.firstline = False
                continue
            if int(eachline[3]) == -1 and eachline[6] == 'W':
                print(eachline[0])


    def higher(self):
        for eachline in self.csv1:
            if self.firstline:
                self.firstline = False
                continue
            if int(eachline[3]) == 1 and eachline[6] == 'L':
                print(eachline[0])


    def competition(self, compet):
        for eachline in self.csv1:
            if (eachline[2]) == compet:
                print('Arsenal', eachline[4], eachline[5], eachline[0])
        return '\n{!r} Scores'.format(compet)



p1 = SortSystem(csv1).competition('Premier Leagued')
print(p1)