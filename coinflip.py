import random, os, time, datetime

starttime = time.time()
heads = 0
tails = 0
flipped = 0
i = 0

print("The following flips a coin for the amount of times you enter and shows the results.")
repeat = float(input("Number of times for the coin to be flipped: "))
logfilename = input("Log file filename: ")

while i < repeat:
	flip = random.randrange(2)
	flipped = flipped+1
	i=i+1
	if flip == 0:
		heads = heads+1
	else:
		tails = tails+1
	print(flip, end=" ")
tailspercent = (100/repeat)*tails
headspercent = (100/repeat)*heads
if tails > heads:
	difference = tails - heads
elif heads > tails:
	difference = heads - tails
else:
	difference = 0

elapsedtime = str(datetime.timedelta(seconds=round(time.time()-starttime,2)))
elapsedtime = elapsedtime[:-4]

print()
print("Flipped", repeat, "times.")
print("Total execution time:", elapsedtime)
print("Tails was flipped", tails, "times, or", tailspercent, "% of the time.")
print("Tails was flipped", heads, "times, or", headspercent, "% of the time.")
print("The difference between the two was", difference, ".")

logfile = open(os.getcwd()+'/'+logfilename, 'w')
logfile.write("Flipped a coin " + str(repeat) + " times.\n")
logfile.write("Total execution time: " + str(elapsedtime) + "\n")
logfile.write("Tails " + str(tails) + " times, or " + str(tailspercent) + "% of the time.\n")
logfile.write("Heads " + str(heads) + " times, or " + str(headspercent) + "% of the time.\n")
logfile.write("The difference between the two was " + str(difference) + ".\n")
logfile.close()
