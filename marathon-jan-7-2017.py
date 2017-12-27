#!/usr/local/bin/python

walk_speed=6.5; sp1=7.0; sp2=7.5; sp3=7.0   # Time: 348.0 minutes
walk_speed=6.5; sp1=7.5; sp2=8.5; sp3=8.0   # Time: 314.0 minutes
walk_speed=6.0; sp1=7.5; sp2=8.5; sp3=8.0   # Time: 317.0 minutes
walk_speed=6.0; sp1=7.5; sp2=8.5; sp3=7.0   # Time: 319.0 minutes
walk_speed=6.0; sp1=7.5; sp2=8.5; sp3=6.0   # Time: 322.0 minutes

walk_speed=6.0; sp1=7.5; sp2=8.0; sp3=6.0   # Time: 335.0 minutes

walk_speed=6.0; sp1=7.5; sp2=7.5; sp3=6.0   # Time: 350.0 minutes

walk_speed=6.0; sp1=7.0; sp2=7.5; sp3=6.0   # Time: 353.0 minutes

# ===============
distance=42.2
# time=340
splits=8
walk_for=5  #minutes

# Walk
walk_pace=60/walk_speed
walk_time=walk_for*splits
walk_distance=round(walk_time/walk_pace,1)

# Run
# remaining_time=time-walk_time
remaining_distance=distance-walk_distance

d1=5 #kn
d3=2.2 
d2=remaining_distance-d1-d3


# Pace
p1=round(60/sp1,1)
p2=round(60/sp2,1)
p3=round(60/sp3,1)

# print "Target Timing: " + str(time) + " minutes " + str(time / 60) + ":" +str(time % 60)
print "Splits: " + str(splits) + " breaks"
print "== Walk Profile =="
print "  Walk for: " + str(walk_for) + " minutes"
print "  Walk speed: " + str(walk_speed) + " kmh <======= "
print "  Walk time = " + str(walk_time) + " minutes"
print "  Walk distance = " + str(walk_distance) + " kms\n"

t1=d1*p1
t2=d2*p2
t3=d3*p3
t=round(t1+t2+t3+walk_time,0)
print "== Run Profile =="
# print "  Run time = " + str(remaining_time) + " minutes"
print "  Run distance = " + str(remaining_distance) + " kms\n"

print "  First  :  " + str(d1) + " km:   " + str(sp1) + " kmh Pace: " + str(p1) + " min/km for " + str(t1) + "  minutes"
print "  Middle : " + str(d2) + " km: " + str(sp2) + " kmh Pace: " + str(p2) + " min/km for " + str(t2) + " minutes"
print "  Last   :  " + str(d3) + " km: " + str(sp3) + " kmh Pace: " + str(p3) + " min/km for " + str(t3) + "  minutes"

print "\nTotal Time: " + str(t) + " minutes " + str(int(t / 60)) + ":" + str(int(t % 60))

print "== \n"

print "Walk: " + str(walk_speed) + "kmh " + str(d1) + "km " + str(p1) + "/" + str(sp1) + "kmh " + str(d2) + "km " + str(p2) + "/" + str(sp2) + "kmh " + str(d3) + "km " + str(p3) + "/" + str(sp3) + "kmh Time: " + str(t) + " minutes"






