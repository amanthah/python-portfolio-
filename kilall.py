import subprocess

# things = "kill -9 {}".format(i)
while True:
    for i in range(500,1212443):
        print("Killing {}".format(i))
        subprocess.call("kill -9 {}".format(i), shell=True)
