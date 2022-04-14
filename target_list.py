import subprocess
import hashlib

def target_list():
    tools_hash_set = set()
    tools_hash_set.add("6fedcdd12c7f5c6c0c028a5973a4b8e6") # /usr/bin/fred
    tools_hash_set.add("d1a4329dcbf2371ee6054b7d8f71e16d") # /usr/bin/autopsy
    tools_hash_set.add("7dde32182bd5496e6ef48419b2287af5") # /opt/lsoft/DiskEditor/DiskEditor
    with open("forensic_tools.txt", "r") as forensic_tools_file:
        command_list = forensic_tools_file.readlines()
        for command in command_list:
            command_name = command.strip()

            whereis_cmd = ["whereis", "-b", command_name]
            whereis_output = subprocess.Popen(whereis_cmd, stdout=subprocess.PIPE).communicate()[0]
            whereis_output_string = str(whereis_output, 'utf-8')
            process_whereis = whereis_output_string.split(':')
            process_binary_path = process_whereis[1].split()
            if len(process_binary_path) != 0:
                for binary in process_binary_path:
                    open_binary_file = open(binary, "rb")
                    binary_hash = hashlib.md5(open_binary_file.read()).hexdigest()
                    tools_hash_set.add(binary_hash)
                    open_binary_file.close()

    return tools_hash_set

if __name__ == '__main__':
    print(target_list())
