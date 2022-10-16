import binascii

"""
LINK_FLAGS = {}

FILE_ATTRIBUTE_FLAGS = {}

SHOW_COMMAND_VALUES = {}

HOTKEY_FLAGS = {}
"""

SHELL_LINK_HEADER = {"HEADER_SIZE":[0x0, 0x4],
                     "LINK_CLSID":[0x0,0x10],
                     "LINK_FLAGS":[0x0,0x4],
                     "FILE_ATTRIBUTES":[0x0,0x4],
                     "CREATION_TIME":[0x0,0x8],
                     "ACCESS_TIME":[0x0,0x8],
                     "WRITE_TIME":[0x0,0x8],
                     "FILE_SIZE":[0x0,0x4],
                     "ICON_INDEX":[0x0,0x4],
                     "SHOW_COMMAND":[0x0,0x4],
                     "HOT_KEY":[0x0,0x2],
                     "RESERVED_1":[0x0,0x2],    
                     "RESERVED_2":[0x0,0x4],
                     "RESERVED_3":[0x0,0x4]}

def read_bytes(file_path):
    with open(file_path, "rb") as file:
        return file.read()

def parse_bytes(file_bytes):
    cursor = 0
    for i in SHELL_LINK_HEADER:
        SHELL_LINK_HEADER[i][0]=file_bytes[cursor:cursor+SHELL_LINK_HEADER[i][-1]] 
        cursor += SHELL_LINK_HEADER[i][-1]

    return SHELL_LINK_HEADER

def pretty_print(dispersed_data):
    for data in dispersed_data:
        print(data+"["+str(dispersed_data[data][-1])+"]",":",binascii.hexlify(dispersed_data[data][0], " ").decode('ascii').upper())

pretty_print(parse_bytes(read_bytes(input("File Path> "))))
