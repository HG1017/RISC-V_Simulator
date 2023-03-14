from include import *

def memory_access():
  if control.MemOP == 0: #Write Disabled
    if pkt.ALUResult in mem.data_memory:
      pkt.LoadData = mem.data_memory[pkt.ALUResult]
    else:
      pkt.LoadData = 0
    
    if(pkt.inst=="lb"):
      pkt.LoadData = pkt.LoadData&0xFF  # Considering only first(LSB) 8 bits of LoadData as rd = M[rs1+imm][0:7] #Byte=8bits
      print("MEMORY: ", pkt.LoadData , "Loaded from address " + hex(pkt.ALUResult))
    elif(pkt.inst=="lh"):
      pkt.LoadData = pkt.LoadData&0xFFFF # Considering only first(LSB) 16 bits of LoadData as rd = M[rs1+imm][0:15] #Half-word = 16bits/2bytes
      print("MEMORY: ", pkt.LoadData , "Loaded from address " + hex(pkt.ALUResult))
    elif(pkt.inst=="lw"):
      pkt.LoadData = pkt.LoadData&0xFFFFFFFF # Considering all 32 bits of LoadData as rd = M[rs1+imm][0:31] #Word = 32bits/4bytes
      print("MEMORY: ", pkt.LoadData , "Loaded from address " + hex(pkt.ALUResult))

  else:
    dataStore = 0
    if(pkt.inst=="sb"):
      dataStore = (pkt.op2&0x000000FF)
      #Storing first 8 (LSB) bits of rs2 in first 8 (LSB) bits of Data memory #Byte=8bits
      mem.data_memory[pkt.ALUResult]= (mem.data_memory[pkt.ALUResult]&0xFFFFFF00)|(pkt.op2&0x000000FF) 
      print("MEMORY: " + "Storing" , dataStore , "at address" , hex(pkt.ALUResult))
    elif(pkt.inst=="sh"):
      dataStore = (pkt.op2&0x0000FFFF)
      #Storing first 16 (LSB) bits of rs2 in first 16 (LSBs) bits of Data memory #Half-word = 16bits/2bytes
      mem.data_memory[pkt.ALUResult]=(mem.data_memory[pkt.ALUResult]&0xFFFF0000)|(pkt.op2&0x0000FFFF)
      print("MEMORY: " + "Storing" , dataStore , "at address" , hex(pkt.ALUResult))
    elif(pkt.inst=="sw"):
      dataStore = pkt.op2
      #Storing all bits of rs2 in all bits of Data memory #Word = 32bits/4bytes
      mem.data_memory[pkt.ALUResult]=dataStore
      print("MEMORY: " + "Storing" , dataStore , "at address" , hex(pkt.ALUResult))
    
    if pkt.ALUResult in mem.data_memory:
      pkt.LoadData = mem.data_memory[pkt.ALUResult]
    else:
      pkt.LoadData = 0
  
  #print("loaddata",pkt.LoadData)
  if(pkt.inst not in ["lb","lh","lw","sb","sh","sw"]):
    print("MEMORY: No Memory Operation")