import time, os
amt_time = 0
amt_s, amt_m, amt_h = [0] * 3
os.system('clear')
print "-" * 50
print ">> Press Any Key to Start the Stopwatch"
print "-" * 50
raw_input("")
try:
	while True:
		time.sleep(1)
		os.system('clear')
		print "-" * 50
		print ">> Press ^C to Discontinue the Stopwatch"
		print "-" * 50
		amt_time += 1
		amt_s += 1
		if amt_s == 60:
			amt_m += 1
			amt_s = 0
		if amt_m == 60:
			amt_h += 1
			amt_m = 0
			amt_s = 0
		frm = "%(amt_h)02d : %(amt_m)02d : %(amt_s)02d" % vars()
		print frm

except KeyboardInterrupt:
	None
finally:
	os.system('clear')
	print "Timer Stopped At:\n%s" % frm
