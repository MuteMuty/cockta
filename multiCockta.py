import sys
import subprocess

procs = []
x = int(input('Vnesi število procesov, ki se izvajajo naenkrat:'))
for i in range(x):
    proc = subprocess.Popen([sys.executable, 'cockta.py'])
    procs.append(proc)

for proc in procs:
    proc.wait()
