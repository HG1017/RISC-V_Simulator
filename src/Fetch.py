from include import *

TerminationCode = 0xFFFFFFFF

def fetch():
    inst_encoding = mem.instruction_memory.get(pkt.PC)
    # print (mem.instruction_memory)
    if(inst_encoding == TerminationCode):
      print("All instructions executed successfully")
      print(mem.data_memory)
      with open("register_values.mc", "w+") as f:
        for i in range(0, len(mem.RegisterFile)):
          f.write("X{}:  {}\n".format(i, mem.RegisterFile[i]))
      with open("data_mem.mc", "w+") as p: 
        for i in mem.data_memory:
          p.write("{}:  {}\n".format(hex(i), mem.data_memory[i]))
      exit()
    pkt.inst_hex = hex(inst_encoding) #hexadecimal string representation
    print("FETCH : Fetch Instruction", pkt.inst_hex, "from address", hex(pkt.PC))