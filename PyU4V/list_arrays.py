#!/usr/bin/python3

"""
Based on HelloUnisphere.py. Just a first try to communicate with Unisphere.
The message 'No array id specified. Please set array ID using the
"set_array_id(array_id)" function.' can be ignored
"""
import PyU4V
import argparse

cliargs = argparse.ArgumentParser(description="Get list of arrays")

cliargs.add_argument("-s", "--server", help="Unisphere server",
                     type=str, required="true")
cliargs.add_argument("-u", "--user", help="Unisphere user",
                     type=str, required="true")
cliargs.add_argument("-p", "--password", help="Unisphere password",
                     type=str, required="true")


args = cliargs.parse_args()

u4v_conn = PyU4V.U4VConn(username=args.user, password=args.password,
                         server_ip=args.server, port='8443',
                         verify=False)

version = u4v_conn.common.get_uni_version()
arrays = u4v_conn.common.get_array_list()

print("Unisphere version: ", version[0])

for array in arrays:
    array_info = u4v_conn.common.get_array(array)
    type = "None"

    if array_info['local']:
        type = "local"
    else:
        type = "remote"
    print(array, "is a", type, array_info['model'], "running",
          array_info['ucode'], "with encryption",
          array_info['data_encryption'])
