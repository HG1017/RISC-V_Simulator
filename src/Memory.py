class memory: 
    TerminationCode = 0xFFFFFFFF
    instruction_memory = {}
    data_memory ={}
    RegisterFile = [0]*32
    RegisterFile[2] = 0x7FFFFFFC #x2 -> Stack Pointer

    def read_word(self,address):
        return self.instruction_memory.get(address)

    def write_word_instrMem(self,address, data):
        self.instruction_memory[address] = data
    
    def write_word_dataMem(self,address, data):
        self.data_memory[address] = data
    
    def load_program_memory(self,file_name):
        fp = open(file_name,"r")
        if(fp == None):
            print("Error opening input MC file\n")
            exit(1)
        TextSegment = True
        for line in fp.readlines():
            address, instruction = map(lambda x:int(x, 16), line.split()) #both stored as integers
            if(instruction == self.TerminationCode):
                self.write_word_instrMem(address, instruction)
                TextSegment = False #Termination Reached. Now switch to data memory.
                continue
            if TextSegment:
                self.write_word_instrMem(address, instruction)
            else:
                self.write_word_dataMem(address, instruction)
        fp.close()
