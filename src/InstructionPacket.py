class Packet:
    #containing the various global variables that are required by the processor stages.
    ImmI=0;ImmS=0;ImmB=0;ImmJ=0;ImmU = 0
    op1=0;op2=0;rd=0
    LoadData=0
    ALUResult = 0
    inst_format="";inst = ""
    inst_hex = ""
    PC = 0x0
    BranchTarget=0