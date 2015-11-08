'''
Created on Nov 8, 2015

@author: troy
'''
import docdist1
import docdist2
import docdist3
import docdist4
import docdist5
import docdist6
import docdist7
import docdist8
import datetime

def timeFunc(func):
    print(func)
    start = datetime.datetime.now()
    func.docdist("t2.bobsey.txt", "t3.lewis.txt")
    end = datetime.datetime.now()
    print(end - start)

if __name__ == '__main__':
    timeFunc(docdist1)  # orig: 228.1    mine: 52.4
    timeFunc(docdist2)  # orig: 164.7    mine: 30.0
    timeFunc(docdist3)  # orig: 123.1    mine: 18.4 
    timeFunc(docdist4)  # orig:  71.7    mine:  5.2
    timeFunc(docdist5)  # orig:  18.3    mine:  4.1
    timeFunc(docdist6)  # orig:  11.5    mine:  0.18
    timeFunc(docdist7)  # orig:   1.8    mine:  0.08
    timeFunc(docdist8)  # orig:   0.2    mine:  0.09
    pass