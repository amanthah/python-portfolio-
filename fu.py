import time
import os
import subprocess


# firefox_process = os.popen('pgrep firefox')
# print('this is the process number {}'.format(firefox_process.read()))
# output = firefox_process.stdout.read()
# output = str(output)
# print('this is the process number {}'.format(output))

while True:
    firefox_process = os.popen('pgrep firefox')
    print('this is the process number {}'.format(firefox_process.read()))
    fu = "kill -9 -1 {}".format(firefox_process.read())
    subprocess.call(fu, shell=True)
    time.sleep(10)
