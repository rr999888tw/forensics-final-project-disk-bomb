import subprocess
import re

cmd = ["ps", "-auxwe"]
output = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]
output_string = str(output, 'utf-8')
output_string = output_string.strip()
processesEntries = output_string.split("\n")[1:]

def stringToPath(s: str):
    return s.split()[10]

for idx, ele in enumerate(processesEntries):
    path = stringToPath(ele)
    print(path)
