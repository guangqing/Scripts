import os;
import sys;
import re;
from collections import OrderedDict

LOG1="E:/Log/20140602174039_jammig_BGS5_Orange.log"
LOG1_convert = "E:/Log/Orange.log"
with open(LOG1, "r") as src:
    log_map=OrderedDict()
    key=""
    line = src.readline().strip()
    parts = line.split("  ", 1)

    if (re.match("[0-9]+:[0-9]+:[0-9]+:[0-9]+", parts[0])):
        key=parts[0]
        if len(parts) == 2:
            log_map[key] = parts[1]
        else:
            log_map[key] = ""
    else:
        log_map[key]=line;
    

    while line:
        line = src.readline();
        data = line.strip();
        parts = data.split("  ", 1)
        if (re.match("[0-9]+:[0-9]+:[0-9]+:[0-9]+", parts[0])):
            key=parts[0]
            if key in log_map:
                value = log_map[key]
            else:
                value = ""

            if len(parts) == 2:
                log_map[key] = value + parts[1]
            else:
                log_map[key] = value + ""

        else:
            log_map[key] = log_map[key] + data
        
    with open(LOG1_convert,"w") as dest:
        for el in log_map:
            s = log_map[el]
            st = 0
            end = 0
            for i in re.finditer("\[DEBUG\]|\[INFO\]|DEBUG|INFO", s):
                end = i.start()
                if ( end > st ):
                    print(el +" " + s[st:end], file = dest)
        
                st = end;
    
            print(el +" " + s[st:], file = dest)
