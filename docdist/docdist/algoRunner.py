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
    timeFunc(docdist1)
    timeFunc(docdist2)
    timeFunc(docdist3)
    timeFunc(docdist4)
    timeFunc(docdist5)
    timeFunc(docdist6)
    timeFunc(docdist7)
    timeFunc(docdist8)
    pass