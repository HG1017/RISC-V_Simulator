#Extends sign of 12 bit or 20 bit immediate. #jal type instruction has 20 bit immediate
def signedExtension(imm,jal = False):
  if(jal): 
    if(imm&0x80000):
      imm = imm|0xFFF00000 #last 20 bits preserved. Rest made 1
    return imm
  elif(imm&0x800):
    #if 12th bit is set (1).
    imm = imm|0xFFFFF000 #last 12 bits preserved. Rest made 1
  return imm

#Returns signed 32 bit representation of the immeddiate
def signed32(imm):
  if(imm>>31==1):
    imm=imm-4294967296
  else:
    imm=imm
  return imm