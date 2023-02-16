#!/usr/bin/python3
"""read from standard input and print some stats"""


import re
import sys

def validate_input(line):
    """validate the line"""
    regx_addr = '^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+'
    regx_date = '\[[0-9]{4}-[0-9]{2}-[0-9]{2}\s[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]+\]'
    regx_get = '\"GET\s\/projects\/260\sHTTP\/1.1\"'
    regx_status = '\s[0-9]{3}\s'
    regx_size = '[0-9]+$'
    x = regx_addr + '\s-\s' + regx_date + '\s' + regx_get + regx_status + regx_size
    x = re.compile(x)
    x = x.match(line)
    if x is None:
        return False
    return True

def get_file_size(line):
    regx_size = '[0-9]+$'
    x = re.search(regx_size, line)
    return(int(x.group()))



def get_status(line):
    regx_status = '\s[0-9]{3}\s'
    x = re.search(regx_status, line)
    x = re.search('[0-9]{3}', x.group())
    return(x.group())

def print_info(size, stat):
    print('File size: {}'.format(size))
    status = [200, 301, 400, 401, 403, 404, 405, 500]
    for i in status:
        if stat[str(i)] > 0:
            print('{}: {}'.format(str(i), stat[str(i)]))


if __name__ == "__main__":
    line_number = 0
    stat = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
    totalsize = 0
    try:
        for line in sys.stdin:
            valid = validate_input(line.rstrip())
            if not valid:
                continue
            line_number += 1
            totalsize += get_file_size(line)
            status = get_status(line)
            if status in stat.keys():
                stat[status] += 1
            if line_number == 10:
                print_info(totalsize, stat)
                line_number = 0
    except KeyboardInterrupt:
        print_info(totalsize, stat)
