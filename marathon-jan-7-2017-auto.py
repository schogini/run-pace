#!/usr/local/bin/python

# 326.0 Run/Walk: 30.0m/5.0m Pace: 7.5/9.5 Speed: 8.0/6.3 Dist: 4.0/0.5 Splits: 9
# Lap: 1 Dist: 2.9 Time: 24.0
# Lap: 2 Dist: 5.8 Time: 48.0
# Lap: 3 Dist: 8.8 Time: 72.0
# Lap: 4 Dist: 11.7 Time: 96.0
# Lap: 5 Dist: 14.6 Time: 120.0
# Lap: 6 Dist: 17.5 Time: 144.0
# Lap: 7 Dist: 20.4 Time: 168.0
# Lap: 8 Dist: 23.4 Time: 192.0
# Lap: 9 Dist: 26.3 Time: 216.0
# Lap: 10 Dist: 29.2 Time: 240.0
# Lap: 11 Dist: 32.1 Time: 264.0
# Lap: 12 Dist: 35.1 Time: 288.0
# Lap: 13 Dist: 38.0 Time: 312.0
# Lap: 14 Dist: 40.9 Time: 336.0

walk_pace=9.5
max_time=330.0

# 8254
# r=[20.0]
# w=[4.0]
# rp= [7.5]
r=[15.0]
w=[2.0,3.0,4.0]
rp= [7.4, 7.5, 7.75, 8.0]

output = []

def pc (p):
	d=int(p)
	# print int(d);exit();
	s=int((p-d)*60)
	return str(d)+"'"+str(s)+'"'

# ===============
distance=42.2
inc=0.1
for run in r:
	for walk in w:
		for run_pace in rp:
			time = 0.0
			dist = 0.0
			no=False
			dd = (run/run_pace) + (walk/walk_pace)
			tt = run + walk
			avg_pace=tt/dd
			rspeed=60/run_pace
			wspeed=60/walk_pace
			while True:
				dist += inc
				time += avg_pace * 0.1
				# time += (inc*(run/(run+walk)))*run_pace
				# time += (inc*(walk/(run+walk)))*walk_pace


				# print "avg_pace="+str(avg_pace)+" rpace="+str(run_pace)+" wpace="+str(walk_pace)+ "run/walk: " +str(run)+"/"+str(walk)+" dist/time: " +str(dist)+"/"+str(time)
				# exit();

				# splits += 1
				# print "Dist: " + str(dist) + " Time: " + str(round(time,2))
				if dist>=distance:
					if time>max_time:	
						no=True		
					break
				if time>max_time:	
					no=True
					break
			time=round(time,0)
			splits=int(round(distance/dd,0))
			rd=run/run_pace
			wd=walk/walk_pace
			# a = str(time) + " Run/Walk: " + str(run) + "m/" + str(walk) +"m Pace: "+str(run_pace)+"/"+str(walk_pace) + " Speed: "+str(round(rspeed,1))+"/"+str(round(wspeed,1)) + " Dist: "+str(round(rd,1))+"/"+str(round(wd,1)) +" Splits: " + str(splits)+ " Avg.Pace: " + str(round(avg_pace,2))
			a = str(int(time)) + "m R/W: " + str(int(run)) + "m/" + str(int(walk)) +"m P: "+pc(run_pace)+"/"+pc(walk_pace) + " K/h: "+str(round(rspeed,1))+"/"+str(round(wspeed,1)) + " K: "+str(round(rd,1))+"/"+str(round(wd,1)) +" L: " + str(splits)+ " AvP: " + str(round(avg_pace,2))
			# b = "s=" + str(splits) + ";w=" + str(walk) +";r="+str(run)+";rp="+str(run_pace)+";wp="+str(walk_pace)+";t="+str(time)
			b = " " + str(splits) + " " + str(walk) +" "+str(run)+" "+str(run_pace)+" "+str(walk_pace)+" "+str(time)
			a+=" # ./strap.py" +b
			# a = str(time) + " Run/Walk: Time: " + str(run) + "m/" + str(walk) +"m Pace: "+str(run_pace)+"/"+str(walk_pace) + " Time: " + str(time) + "m Splits: " + str(splits)#+ " Dist: " + str(round(dist,2))
			if not no :
				# print a
				output.append(a)
output.sort()
for a in output:
	print a


exit()
