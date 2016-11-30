import os;
import sys;
import re;

logfile = "E:/Ubuntu/SocketWithoutUrc_Client.txt"
genttl = "E:/Log/IPIS100164900.ttl"

with open(logfile, 'r') as src:
    with open(genttl, 'w') as dest:
        line = src.readline().strip()
        while line:
            line = line.strip()
            if line.startswith("at") or line.startswith("AT"):
                gen_string = "send '" + line + "'"
                print(gen_string, file = dest)
                print("wait 'OK' ", file = dest)
        
            line = src.readline();
