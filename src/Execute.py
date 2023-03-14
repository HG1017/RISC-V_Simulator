from include import *

def execute():
    alu.inp1 = pkt.op1
    if(control.OP2Select == 0): alu.inp2 = pkt.ImmS
    elif (control.OP2Select == 1): alu.inp2 = pkt.ImmI
    else: alu.inp2 = pkt.op2

    if(pkt.inst == "add" or pkt.inst=="addi" or pkt.inst in ["lb","lh","lw"] or pkt.inst_format=="S" or pkt.inst == "jalr" ):
        control.ALUOp = "addition"
        pkt.ALUResult = alu.addition()
        print("EXECUTE: ADD", alu.inp1, "and", alu.inp2)

    elif(pkt.inst == "sub" or pkt.inst == "slt" or pkt.inst_format == "B"):
        control.ALUOp = "subtraction"
        result = alu.subtraction()

        if(pkt.inst=="sub"):
            pkt.ALUResult = result
        elif (pkt.inst == "slt"):
            pkt.ALUResult = 1 if result<0 else 0
        else: #Branch Instructions
            if(pkt.inst=="beq"):
                pkt.ALUResult = 1 if result==0 else 0 #1-> Branch will be taken
            elif(pkt.inst=="bne"):
                pkt.ALUResult = 1 if result!=0 else 0
            elif(pkt.inst=="bge"):
                pkt.ALUResult = 1 if result>=0 else 0
            elif(pkt.inst=="blt"):
                pkt.ALUResult = 1 if result<0 else 0
            control.isBranch = 1 if pkt.ALUResult==1 else 0      
        print("EXECUTE: SUBTRACT", alu.inp2, "from", alu.inp1)

    elif(pkt.inst == "sll"):
        control.ALUOp = "left shift"
        pkt.ALUResult = alu.leftshift()
        print("EXECUTE: LEFT SHIFT", alu.inp1, "by", alu.inp2, "bits")

    elif(pkt.inst == "xor"):
        control.ALUOp = "xor"
        pkt.ALUResult = alu.xor()
        print("EXECUTE: XOR operation on", alu.inp1, "and", alu.inp2)

    elif(pkt.inst == "srl" or pkt.inst == "sra"):
        if(pkt.inst=="srl"): pkt.ALUResult = alu.srl(); print("EXECUTE: LOGICAL RIGHT SHIFT", alu.inp1, "by", alu.inp2, "bits")
        else: pkt.ALUResult = alu.sra(); print("EXECUTE: ARITHMETIC RIGHT SHIFT", alu.inp1, "by", alu.inp2, "bits")

    elif(pkt.inst == "or" or pkt.inst=="ori"):
        pkt.ALUResult = alu.inp1 | alu.inp2
        print("EXECUTE: OR operation on", alu.inp1, "and", alu.inp2)

    elif(pkt.inst == "and" or pkt.inst=="andi"):
        pkt.ALUResult = alu.inp1 & alu.inp2
        print("EXECUTE: AND operation on", alu.inp1, "and", alu.inp2)

    elif(pkt.inst == "jal"):
        print("EXECUTE: jal operation") 
        pass #No ALU Operation
  
    elif(pkt.inst == "lui"):
        print("EXECUTE: lui operation")
        pass
  
    elif(pkt.inst == "auipc"):
        pkt.ALUResult = pkt.PC + pkt.ImmU
        print("EXECUTE: auipc operation")
  
    else:
        print("Invalid instruction type\n")
  
    #PC Update and Branch Target Calculations
    if(control.BranchTargetSet==0): pkt.BranchTarget = pkt.PC+pkt.ImmJ
    else: pkt.BranchTarget = pkt.PC+pkt.ImmB
      
    if (control.isBranch ==0): pkt.PC = pkt.PC + 4
    elif(control.isBranch ==1): pkt.PC = pkt.BranchTarget
    else: pkt.PC = pkt.ALUResult
