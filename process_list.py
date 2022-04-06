import subprocess
import hashlib

# Parsing ps ouput to retrieve the commands
cmd = ["ps", "-aux"]
output = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]
output_string = str(output, 'utf-8')
output_string = output_string.strip()
processesEntries = output_string.split("\n")[1:]

def stringToPath(s: str):
    return s.split()[10]

command_list = []
for idx, ele in enumerate(processesEntries):
    path = stringToPath(ele)
    command_list.append(path)
    # print(command_list)


# Creating a binary database where the keys are the path of the binary and the
# md5 hash is the value
binary_database = {}
for path in command_list:
    try:
        whereis_cmd = ["whereis", "-b", path]
        whereis_output = subprocess.Popen(whereis_cmd, stdout=subprocess.PIPE).communicate()[0]
        whereis_output_string = str(whereis_output, 'utf-8')
        process_whereis = whereis_output_string.split(':')
        process_binary_path = process_whereis[1].split()
        if len(process_binary_path) != 0:
            for binary in process_binary_path:
                binary_hash = hashlib.md5(binary.encode())
                binary_database[binary] = binary_hash.hexdigest()
    except:
        pass 

print(binary_database)
