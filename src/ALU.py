class ALU:
    #has two input pins -> op1 and second input based on OP2Select
    #one output pin -> ALUResult
    inp1=0
    inp2=0

    def addition(self):
        return  self.inp1+self.inp2
    def subtraction(self):
        return self.inp1-self.inp2
    def leftshift(self):
        return self.inp1<<self.inp2
    def xor(self):
        return self.inp1^self.inp2
    def srl(self):
        return self.inp1 >> self.inp2
    def sra(self):
        # Check if the value is negative
        if self.inp1 < 0:
        # In Python, the >> operator preserves the sign bit
        # So, we need to manually clear the sign bit by
        # performing a bitwise AND with a mask
            mask = (1 << self.inp1.bit_length()) - 1
            self.inp1 &= mask
        return self.inp1 >> self.inp2