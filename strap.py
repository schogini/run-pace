#!/usr/local/bin/python

import sys
program_name = sys.argv[0]
arguments = sys.argv[1:]
count = len(arguments)
# print count;exit(0)
# s=14;w=3.0;r=20.0;rp=7.5;wp=10;t=328
# splits=s;walk=w;run=r;run_pace=rp;walk_pace=wp;total=t
splits=float(sys.argv[1]);
walk=float(sys.argv[2]);
run=float(sys.argv[3]);
run_pace=float(sys.argv[4]);
walk_pace=float(sys.argv[5]);
total=float(sys.argv[6])
lap=0
dist=0
time=0
distance=42.2

def pc (p):
	d=int(p)
	# print int(d);exit();
	s=int((p-d)*60)
	return str(d)+"'"+str(s)+'"'

# print str(splits)+" "+str(run)+" "+str(run_pace)+" "+str(walk)+" "+str(walk_pace)
# exit();

dd = (float(run)/float(run_pace)) + (float(walk)/float(walk_pace))

tt = run + walk
avg_pace=tt/dd

print "Run:\t" + str(int(run))+ "m\t"+ pc(run_pace)+ "/"+str(round(60/run_pace,1)) + "kph"
print "Walk:\t" + str(int(walk)) + "m\t" + pc(walk_pace)+"/"+str(round(60/walk_pace,1)) +"kph"
print "AvPace:\t" +pc(round(avg_pace,2)) + " Splits: " + str(splits)

while True:
  lap+=1
  dist+=(walk/walk_pace)+(run/run_pace)
  time+=walk+run 
  print "\t" + str(lap) + "\t" + str(int(round(dist,0))) + "k\t" + str(int(round(time,0)))
  if lap==(splits-1):
  	break
 
bal=distance-dist
lap+=1
dist=distance
time+=bal*avg_pace
print "\t" + str(lap) + "\t" + str(int(round(dist,0))) + "k\t" + str(int(round(time,0)))
