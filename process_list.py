import subprocess
import hashlib
import threading
from target_list import target_list

# Parsing ps ouput to retrieve the commands
# cmd = ["ps", "-aux"]
# output = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]
# output_string = str(output, 'utf-8')
# output_string = output_string.strip()
# processesEntries = output_string.split("\n")[1:]

def stringToPath(s: str):
    return s.split()[10]

def parsePsList():
    cmd = ["ps", "-aux"]
    output = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]
    output_string = str(output, 'utf-8')
    output_string = output_string.strip()
    processesEntries = output_string.split("\n")[1:]
    process_list = []
    for idx, ele in enumerate(processesEntries):
        path = stringToPath(ele)
        process_list.append(path)
    return process_list

command_list = parsePsList()
# for idx, ele in enumerate(processesEntries):
#     path = stringToPath(ele)
#     command_list.append(path)
# print(command_list)


# Creating a binary database where the keys are the path of the binary and the
# md5 hash is the value
binary_database = {}
# for path in command_list:
#     try:
#         whereis_cmd = ["whereis", "-b", path]
#         whereis_output = subprocess.Popen(whereis_cmd, stdout=subprocess.PIPE).communicate()[0]
#         whereis_output_string = str(whereis_output, 'utf-8')
#         process_whereis = whereis_output_string.split(':')
#         process_binary_path = process_whereis[1].split()
#         if len(process_binary_path) != 0:
#             for binary in process_binary_path:
#                 open_binary_file = open(binary, "rb")
#                 binary_hash = hashlib.md5(open_binary_file.read())
#                 binary_database[binary] = binary_hash.hexdigest()
#                 open_binary_file.close()
#     except:
#         pass 

# Learning to use threading to make processing the process list database faster
#thread_lock = threading.Lock()

class processListThread (threading.Thread):
    def __init__(self, command_name):
        threading.Thread.__init__(self)
        self.command_name = command_name

    def run(self):
        # thread_lock.acquire()
        whereisSearch(self.command_name)
        # thread_lock.release()

def whereisSearch(path: str):
    try:
        whereis_cmd = ["whereis", "-b", path]
        whereis_output = subprocess.Popen(whereis_cmd, stdout=subprocess.PIPE).communicate()[0]
        whereis_output_string = str(whereis_output, 'utf-8')
        process_whereis = whereis_output_string.split(':')
        process_binary_path = process_whereis[1].split()
        if len(process_binary_path) != 0:
            for binary in process_binary_path:
                open_binary_file = open(binary, "rb")
                binary_hash = hashlib.md5(open_binary_file.read())
                binary_database[binary] = binary_hash.hexdigest()
                open_binary_file.close()
    except:
        pass

thread_list = []
for path in command_list:
    thread_list.append(processListThread(path))

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print(binary_database)

class heartbeat1(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        thread_lock.acquire()
        process_list = parsePsList()
        checkBinaryDatabase(process_list)
        thread_lock.release()


def checkBinaryDatabase(process_list: list):
    tools_db = target_list()
    for process in process_list:
        if process not in binary_database:
            if process in tools_db:
                pass
                # trigger

# print(checkBinaryDatabase(parsePsList()))
