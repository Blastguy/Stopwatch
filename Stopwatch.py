import time

print('Press ENTER to start. Use Ctrl-C to quit at any time')
input()
print('Stopwatch started! Press ENTER to lap')

start = time.time()
lastTime = start
lap = 1

print('Lap\tTotal Time      Lap Time')

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 4)
        totalTime = round(time.time() - start, 4)
        lastTime = time.time()
        print('Lap %s:  %s\t\t%s' % (str(lap), totalTime, lapTime))
        lap += 1
except KeyboardInterrupt:
    print('\nDone! Press Enter to exit')
    input()