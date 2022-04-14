import subprocess
import hashlib

def target_list():
    tools_hash = {}
    tools_hash["/usr/bin/fred"] = "6fedcdd12c7f5c6c0c028a5973a4b8e6"
    tools_hash["/usr/bin/autopsy"] = "d1a4329dcbf2371ee6054b7d8f71e16d"
    tools_hash["/opt/lsoft/DiskEditor/DiskEditor"] = "7dde32182bd5496e6ef48419b2287af5"
    forensic_tools_file = open("forensic_tools.txt")
    command_list = forensic_tools_file.readlines()
    for command in command_list:
        command_name = command.strip()
        try:
            which_cmd = ["which", command_name]
            which_output = subprocess.Popen(which_cmd, stdout=subprocess.PIPE).communicate()[0]
            which_output_string = str(which_output, 'utf-8')
            which_output_string = which_output_string.strip()
            process_binaries = which_output_string.split("\n")
            open_binary_file = open(process_binaries[0], "rb")
            binary_hash = hashlib.md5(open_binary_file.read())
            tools_hash[process_binaries[0]] = binary_hash.hexdigest()
            open_binary_file.close()

            # process_whereis = whereis_output_string.split(':')
            # process_binary_path = process_whereis[1].split()
            # if len(process_binary_path) != 0:
            #     for binary in process_binary_path:
            #         open_binary_file = open(binary, "rb")
            #         binary_hash = hashlib.md5(open_binary_file.read())
            #         tools_hash[binary] = binary_hash.hexdigest()
            #         open_binary_file.close()
        except:
            pass
    forensic_tools_file.close()
    return tools_hash

#print(target_list())