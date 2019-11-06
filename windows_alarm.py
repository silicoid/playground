import os
import time
import threading


class Alarm (threading.Thread):
    def __init__(self, timeout):
        threading.Thread.__init__(self)
        self.timeout = timeout
        self.setDaemon(True)

    def run(self):
        time.sleep(self.timeout)
        print("Break")
        os._exit(1)


alarm = Alarm(4)
alarm.start()
time.sleep(2)
del alarm
print('yup')

alarm = Alarm(4)
alarm.start()
time.sleep(8)
del alarm
print('nope')  # we don't make it this far
