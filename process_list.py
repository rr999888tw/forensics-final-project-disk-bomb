import subprocess
import re

cmd = ["ps", "ax"]
output = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]
output_string = str(output)
processes = output_string.split("\n")
processes = output_string.split("\\")

command_names = []
for i in range(1, len(processes) - 1): 
    command = processes[i].split()
    command_names.append(command[5])
    print(command_names)
