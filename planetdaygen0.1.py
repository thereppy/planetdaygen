import math
pi=3.1415926535898

planetname=input("What is the name of the planet? ")

yearlength=input("How many days are in "+planetname+"'s year? ")
yearlength=float(yearlength)

axialtilt=input("What is "+planetname+"'s axial tilt? ")
axialtilt=float(axialtilt)

latitude=input("What is the latitude in question? ")
latitude=float(latitude)

days=input("How many days has it been since the Vernal Equinox? ")
days=float(days)

delta=6.28319*(days/yearlength)
delta=math.sin(delta)
delta=axialtilt*(delta)
delta=math.tan(delta)
beta=latitude*pi/180
beta=math.tan(beta)
tau=-beta*delta*pi/180
tau=math.acos(tau)
tau=tau*180/pi
seconds=(tau*480)
minutes,seconds=divmod(seconds,60)
hours,minutes=divmod(minutes,60)
seconds=str(int(seconds))
minutes=str(int(minutes))
hours=str(int(hours))

print()
print(planetname+ " Units: " + hours + " Hours, " + minutes + " Minutes, and " + seconds + " seconds.")
