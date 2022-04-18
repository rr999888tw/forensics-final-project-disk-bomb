import subprocess

def trigger_bomb():
    cd_to_mounted_device = subprocess.run(["cd", "/mnt/shady_stuff/Downloads"], stdout=subprocess.DEVNULL)
    remove_picture = subprocess.run(["rm", "pic.jpg"], stdout=subprocess.DEVNULL)
    sync()
    unload_file_bomb = subprocess.run(["7z", "-e", "zbsm.zip"], stdout=subprocess.DEVNULL)
    sync()

def sync():
    sync = subprocess.run(["sync"])