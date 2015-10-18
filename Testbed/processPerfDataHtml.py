#!/usr/bin/python

import sys
import os
import numpy
import time

usage = "Usage: %s filename\n" % sys.argv[0]

def printTrailer():
  print "</table></div>"
  print "</body>"
  print "</html>"

def printHeader():
  print "<!DOCTYPE html>"
  print "<html>"
  print "<head>"
  print "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\" />"
  print "<title>NDN Testbed Diagnostics (runs every 10 minutes at n*10 + 2)</title>"
  print "<link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\" />"
  print "<script type='text/javascript' src='http://ajax.googleapis.com/ajax/libs/jquery/1.6.4/jquery.min.js'></script>"
  print "<script type=\"text/JavaScript\" src=\"mjs.js\"></script>"
  print "</head>"
  print "NDN Diagnostics : ",
  print (time.strftime("%D %T"))
  print "<table border =\"1\"; width=\"1100\";>"
  #print "<tr><td width = 80px>&nbsp;</td>"
  print "<td width = 100px; bgcolor =\"#7CFC00\">Node</td>"
  print "<td width = 200px; bgcolor =\"#7CFC00\">epochTime</td>"
  print "<td width = 40px; bgcolor =\"#7CFC00\">tz</td>"
  print "<td width = 40px; bgcolor =\"#7CFC00\">tz+-</td>"
  print "<td width = 40px; bgcolor =\"#7CFC00\">cpu%</td>"
  print "<td width = 40px; bgcolor =\"#7CFC00\">mem%</td>"
  print "<td width = 80px; bgcolor =\"#7CFC00\">nfdVSZ</td>"
  print "<td width = 80px; bgcolor =\"#7CFC00\">nfdRSS</td>"
  print "<td width = 80px; bgcolor =\"#7CFC00\">nfdTime</td>"
  print "<td width = 80px; bgcolor =\"#7CFC00\">upTime</td>"
  print "<td width = 60px; bgcolor =\"#7CFC00\">nameTree</td>"
  print "<td width = 60px; bgcolor =\"#7CFC00\">Fib</td>"
  print "<td width = 60px; bgcolor =\"#7CFC00\">Pit</td>"
  print "<td width = 60px; bgcolor =\"#7CFC00\">CS</td>"
  print "<td width = 100px; bgcolor =\"#7CFC00\">Measurement</td>"
  print "</tr>"

def main(arv=None):
    filename = sys.argv[1]
    f = open(filename, 'r')

    line1 = f.readline()
    #print line1
    #print "Node          epochTime      cpu% mem% nfdVSZ nfdRSS nfdTIME upTime nameTree Fib Pit CS Measurement"
    printHeader()
    while (line1 != ''):
        words = line1.split()
        #print len(words)
        if len(words) > 0:
          if words[0] == "Node" :
            # we found a node block
            subwords = words[1].split(':')
            nodeName = subwords[0]
            #print nodeName, " ",
            print "<tr>"
            print "<td>", nodeName, "</td>"
            line1 = f.readline()
            #print line1
            done = False
            epochTime = "0.0"
            tz = "x"
            tzoffset = "x"
            cpuPercent = "0"
            memPercent = "0"
            nfdVSZ = "0"
            nfdRSS = "0"
            nfdTIME = "0"
            nfdUptime = "0"
            nfdNameTree = "0"
            nfdFib = "0"
            nfdPit = "0"
            nfdCs = "0"
            nfdMsrmnt = "0"
            while (line1 != '') and not done:
              words = line1.split()
              wordsEqual = line1.split('=')
              if len(words) > 0:
                if (words[0] == "onTimeout:"):
                  done = True
                  #print "nfd VSZ = ", nfdVSZ, " nfd RSS = ", nfdRSS, " nfd TIME = ", nfdTIME
                  #print epochTime, nfdVSZ, nfdRSS, nfdTIME
                else:
                  if (words[0] == "TIME"):
                      if len(words) > 1:
                        epochTime = words[1]
                  if (words[0] == "TZ"):
                      if len(words) > 1:
                        tz = words[1]
                  if (words[0] == "TZOFFSET"):
                      if len(words) > 1:
                        tzoffset = words[1]
                  if (words[0] == "COMMAND"):
                    line1 = f.readline()
                    if (line1 != ''):
                      words = line1.split()
                      if len(words) > 6:
                        #COMMAND           PID %CPU %MEM   RSS    VSZ     TIME
                        cpuPercent = words[2]
                        memPercent = words[3]
                        nfdRSS = words[4]
                        nfdVSZ = words[5]
                        nfdTIME = words[6]
                        #print "nfd VSZ = ", nfdVSZ, " nfd RSS = ", nfdRSS, " nfd TIME = ", nfdTIME
                        #print epochTime, nfdVSZ, nfdRSS, nfdTIME
                  if (words[0] == "F"):
                    line1 = f.readline()
                    #print line1
                    if (line1 != ''):
                      words = line1.split()
                      if len(words) > 12:
                        nfdVSZ = words[6]
                        nfdRSS = words[7]
                        nfdTIME = words[11]
                        #print "nfd VSZ = ", nfdVSZ, " nfd RSS = ", nfdRSS, " nfd TIME = ", nfdTIME
                        #print epochTime, nfdVSZ, nfdRSS, nfdTIME
                if not done and len(wordsEqual) > 1:
                  #print line1
                  #print wordsEqual[0]
                  #print wordsEqual[1]
                  subwords1 = wordsEqual[0].split()
                  subwords2 = wordsEqual[1].split()
                  #print subwords[0]
                  if (subwords1[0] == "uptime"):
                    nfdUptime = subwords2[0]
                    #print "nfdUptime = ", nfdUptime
                  if (subwords1[0] == "nNameTreeEntries"):
                    nfdNameTree = subwords2[0]
                  if (subwords1[0] == "nFibEntries"):
                    nfdFib = subwords2[0]
                  if (subwords1[0] == "nPitEntries"):
                    nfdPit = subwords2[0]
                  if (subwords1[0] == "nMeasurementsEntries"):
                    nfdMsrmnt = subwords2[0]
                  if (subwords1[0] == "nCsEntries"):
                    nfdCs = subwords2[0]
                    done = True
              if done == True:
                  #print epochTime, cpuPercent, memPercent, nfdVSZ, nfdRSS, nfdTIME, nfdUptime, nfdNameTree, nfdFib, nfdPit, nfdCs, nfdMsrmnt
                  print "<td>", epochTime, "</td>"
                  print "<td>", tz, "</td>"
                  print "<td>", tzoffset, "</td>"
                  print "<td>", cpuPercent, "</td>"
                  print "<td>", memPercent, "</td>"
                  print "<td>", nfdVSZ, "</td>"
                  print "<td>", nfdRSS, "</td>"
                  print "<td>", nfdTIME, "</td>"
                  print "<td>", nfdUptime, "</td>"
                  print "<td>", nfdNameTree, "</td>"
                  print "<td>", nfdFib, "</td>"
                  print "<td>", nfdPit, "</td>"
                  print "<td>", nfdCs, "</td>"
                  print "<td>", nfdMsrmnt, "</td>"
                  print "</tr>"
                  
              line1 = f.readline()
                
        line1 = f.readline()
    printTrailer()


if __name__ == '__main__':
    status = main()
    sys.exit(status)

