import sys
from Fetch import fetch
from Decode import decode
from Execute import execute
from MemoryAcess import memory_access
from WriteBack import write_back
from include import *

if __name__ == '__main__':
    # file_name = r"test/BubbleSort.mc"
    # mem.load_program_memory(file_name)
    file_path = sys.argv[1]
    mem.load_program_memory(file_path)
    print("Initial Memory State: ")
    print("Address: Data")
    for i in mem.data_memory:
        print("{}:  {}".format(hex(i), mem.data_memory[i]))
    print("\n")

    Clock = 1
    while True:
        print("Clock Cycle No.", Clock)
        fetch()
        decode()
        execute()
        memory_access()
        write_back()
        print()
        Clock += 1
