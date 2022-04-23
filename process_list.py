import subprocess
import hashlib
import threading
import os
from target_list import target_list

target_list_result = target_list()
bomb_triggered = False

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
        global bomb_triggered
        subprocess.call('~/Documents/forensics-final-project-disk-bomb/detonate.sh', shell=True, stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL)
        # print("FIle BOMB detonating!")
        bomb_triggered = True

    def whereisSearch(self, path: str):
        try:
            whereis_cmd = ["whereis", "-b", path]
            whereis_output = subprocess.Popen(whereis_cmd, stdout=subprocess.PIPE).communicate()[0]
            whereis_output_string = str(whereis_output, 'utf-8')
            process_binary_path = whereis_output_string.strip().split()[1:]

            for binary in process_binary_path:
                if os.path.isfile(binary):
                    md5sum_cmd = ['md5sum', binary]
                    md5sum_output = subprocess.Popen(md5sum_cmd, stdout=subprocess.PIPE).communicate()[0]
                    md5sum_output_string = str(md5sum_output, 'utf-8').strip().split()[0]
                    if md5sum_output_string in target_list_result:
                        self.trigger()

        except:
            pass

    def run(self):
        self.whereisSearch(self.command_name)

while not bomb_triggered:
    command_list = parsePsList()
    thread_list = []
    for path in command_list:
        thread_list.append(processListThread(path))

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()
