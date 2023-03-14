from SignedExtension import signedExtension,signed32
from include import *

def decode():
  res = (bin(int(pkt.inst_hex, 16))[2:]).zfill(32) #binary representation of the instruction
  opcode = res[25:32]
  pkt.rd = int(res[20:25],2)
  funct3 = int(res[17:20],2)
  rs1 = int(res[12:17],2)
  rs2 = int(res[7:12],2)
  funct7 = int(res[0:7],2)
  pkt.op1 = mem.RegisterFile[rs1]
  pkt.op2 = mem.RegisterFile[rs2]
  
  pkt.ImmI = signed32(signedExtension(int(res[0:12],2)))
  pkt.ImmS = signed32(signedExtension(int(res[0:7]+res[20:25],2)))
  pkt.ImmB = signed32(signedExtension(int(res[0]+res[24]+res[1:7]+res[20:24]+str(0),2)))
  pkt.ImmJ = signed32(signedExtension(int(res[0]+res[12:20]+res[11]+res[1:11],2),True))
  pkt.ImmU = signed32(int(res[0:20],2)<<12) 
  
  if opcode=="0110011":
    pkt.inst_format = "R"
    control.controlRtype() #Sets the required control signals for this particular format
    if(funct3==0):
      if(funct7==0):
        pkt.inst="add"
      else:
        pkt.inst="sub"
    elif(funct3==1):
      pkt.inst="sll"
    elif(funct3==2):
      pkt.inst="slt"
    elif(funct3==4):
      pkt.inst="xor"
    elif(funct3==5):
      pkt.inst="srl"
    elif(funct3==6):
      pkt.inst="or"
    elif(funct3==7):
      pkt.inst="and"
    
    print("DECODE:","Instruction format:",pkt.inst_format,", Operation:",pkt.inst,", First Operand x"+str(rs1),", Second Operand x"+str(rs2),", Destination Register x"+str(pkt.rd))
    print("DECODE:","Read Registers:","x"+str(rs1)+"="+str(pkt.op1),", x"+str(rs2)+"="+str(pkt.op2))

  elif opcode=="0010011":
    pkt.inst_format = "I"
    control.controlItype() #Control
    if(funct3==0):
      pkt.inst="addi"
    elif(funct3==6):
      pkt.inst="ori"
    elif(funct3==7):
      pkt.inst="andi"

    print("DECODE:","Instruction format:",pkt.inst_format,", Operation:",pkt.inst,", First Operand x"+str(rs1),", Immediate value ",pkt.ImmI,", Destination Register x"+str(pkt.rd))
    print("DECODE:","Read Registers:","x"+str(rs1)+"="+str(pkt.op1))
    
  elif opcode=="0000011":
    pkt.inst_format = "I"
    control.controlLoad() #Control
    if(funct3==0):
      pkt.inst="lb"
    elif(funct3==1):
      pkt.inst="lh"
    elif(funct3==2):
      pkt.inst="lw"
    elif(funct3==4):
      pkt.inst="lbu"
    elif(funct3==5):
      pkt.inst="lhu"

    print("DECODE:","Instruction format:",pkt.inst_format,", Operation:",pkt.inst,", First Operand x"+str(rs1),", Immediate value ",pkt.ImmI,", Destination Register x"+str(pkt.rd))
    print("DECODE:","Read Registers:","x"+str(rs1)+"="+str(pkt.op1))

    
  elif opcode=="0100011":
    pkt.inst_format = "S"
    control.controlStore() #control
    if(funct3==0):
      pkt.inst="sb"
    elif(funct3==1):
      pkt.inst="sh"
    elif(funct3==2):
      pkt.inst="sw"
  
    print("DECODE:","Instruction format:",pkt.inst_format,", Operation:",pkt.inst,", First Operand x"+str(rs1),", Second Operand x"+str(rs2),", Immediate value ",pkt.ImmS)
    print("DECODE:","Read Registers:","x"+str(rs1)+"="+str(pkt.op1),", x"+str(rs2)+"="+str(pkt.op2))

  elif opcode=="1100011":
    pkt.inst_format = "B"
    control.controlBtype() #control
    if(funct3==0):
      pkt.inst="beq"
    elif(funct3==1):
      pkt.inst="bne"
    elif(funct3==4):
      pkt.inst="blt"
    elif(funct3==5):
      pkt.inst="bge"
    
    print("DECODE:","Instruction format:",pkt.inst_format,", Operation:",pkt.inst,", First Operand x"+str(rs1),", Second Operand x"+str(rs2),", Immediate value ",pkt.ImmB)
    print("DECODE:","Read Registers:","x"+str(rs1)+"="+str(pkt.op1),", x"+str(rs2)+"="+str(pkt.op2))

  
  elif opcode=="1101111":
    pkt.inst_format = "J"
    control.controlJal() #Control
    pkt.inst="jal"

    print("DECODE:","Instruction format:",pkt.inst_format,", Operation:",pkt.inst,", Immediate value ",pkt.ImmJ,", Destination Register x"+str(pkt.rd))


  elif opcode=="1100111":
    pkt.inst_format = "I"
    control.controlJalr()
    pkt.inst="jalr"

    print("DECODE:","Instruction format:",pkt.inst_format,", Operation:",pkt.inst,", First Operand x"+str(rs1),", Immediate value ",pkt.ImmI,", Destination Register x"+str(pkt.rd))
    print("DECODE:","Read Registers:","x"+str(rs1)+"="+str(pkt.op1))


  elif opcode=="0110111":
    control.controlLui() #Control
    pkt.inst_format = "U"
    pkt.inst="lui"

    print("DECODE:","Instruction format:",pkt.inst_format,", Operation:",pkt.inst,", Immediate value ",pkt.ImmU,", Destination Register x"+str(pkt.rd))
 
  
  elif opcode=="0010111":
    control.controlAuipc() #Control
    pkt.inst_format = "U"
    pkt.inst="auipc"

    print("DECODE:","Instruction format:",pkt.inst_format,", Operation:",pkt.inst,", Immediate value ",pkt.ImmU,", Destination Register x"+str(pkt.rd))
    
  #print("DECODE:","Instruction format:",pkt.inst_format,", Operation:",pkt.inst,", First Operand x"+str(rs1),", Second Operand x"+str(rs2),", Destination Register x"+str(pkt.rd))
  #print("DECODE:","Read Registers:","x"+str(rs1)+"="+str(pkt.op1),", x"+str(rs2)+"="+str(pkt.op2))
  #print("RFWrite",control.RFWrite)