from include import *

def write_back():
  #print("RFWrite",control.RFWrite)
  if control.RFWrite == 1:

    if control.ResultSelect ==0:
      mem.RegisterFile[pkt.rd] = pkt.ALUResult

    elif control.ResultSelect ==1:
      mem.RegisterFile[pkt.rd] = pkt.LoadData

    elif control.ResultSelect ==2:
      mem.RegisterFile[pkt.rd] = pkt.ImmU

    elif control.ResultSelect ==3:
      mem.RegisterFile[pkt.rd] = pkt.PC+4

    print("WRITEBACK: Value in register x"+str(pkt.rd),"is",mem.RegisterFile[pkt.rd])

  else:
    print("WRITEBACK: No Writeback operation")
    pass #Writeback is Diabled
  
  
