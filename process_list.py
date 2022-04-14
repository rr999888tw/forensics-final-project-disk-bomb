import subprocess
import hashlib
import threading
from target_list import target_list

target_list_result = target_list()

def stringToPath(s: str):
    return s.split()[10]

def parsePsList():
    cmd = ["ps", "-aux"]
    output = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]
    output_string = str(output, 'utf-8')
    output_string = output_string.strip()
    processes_entries = output_string.split("\n")[1:]
    process_list = []
    for _, ele in enumerate(processes_entries):
        process_list.append(stringToPath(ele))
    return process_list

class processListThread (threading.Thread):
    def __init__(self, command_name):
        threading.Thread.__init__(self)
        self.command_name = command_name

    def trigger(self):
        print("FIle BOMB detonating!")

    def whereisSearch(self, path: str):
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
                    if binary_hash in target_list_result:
                        self.trigger()
        except:
            pass

    def run(self):
        self.whereisSearch(self.command_name)


while (1):
    command_list = parsePsList()
    thread_list = []
    for path in command_list:
        thread_list.append(processListThread(path))

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()
