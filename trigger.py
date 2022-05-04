import subprocess
import os

def trigger_bomb():
    # subprocess.run(["ls"])
    # print(os.getcwd())
    # os.chdir("~/Documents")
    # cd_to_mounted_device = subprocess.run(["cd", "/home/bryanlin99/Documents"])
    # print(os.getcwd())
    subprocess.run(["ls"])
    # remove_picture = subprocess.run(["rm", "/pic.jpg"], stdout=subprocess.DEVNULL)
    # sync()
    # unload_file_bomb = subprocess.run(["7z", "-e", "zbsm.zip"], stdout=subprocess.DEVNULL)
    # sync()

def sync():
    sync = subprocess.run(["sync"])

if __name__ == '__main__':
    trigger_bomb()