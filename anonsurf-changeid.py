import time
import subprocess

while True:
    script = "/home/mesa/codium/anonsurf-loop/changeid.sh"
    subprocess.call(script)
    time.sleep(10*60)
    