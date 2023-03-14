class Control:
    #Only one instance of this class required. That's why no seperate constructor.
    isBranch = 0 #0 to select PC+4, 1 to select Branch Target and 2 to select ALUResult.
    RFWrite = 0 #1 to write into register file
    OP2Select = 2 #0 to select ImmS, 1 to select ImmI, 2 to select op2
    ALUOp = "" #
    MemOP = 0 #0 to disable write to data memory, 1 to write to data memory
    ResultSelect = 0 #0 to select ALUResult, 1 to select LoadData, 2 to select ImmU, 3 to select PC+4
    BranchTargetSet = 0 #0 to select ImmJ, 1 to select ImmB

    def controlRtype(self):
        self.OP2Select = 2 #Select op2. 
        self.RFWrite = 1 #Enable Write.
        self.ResultSelect = 0
        self.isBranch = 0
        self.MemOP = 0
        #BranchTargetSet -> Don't Care Condition
    
    def controlItype(self):
        self.OP2Select = 1 #Select ImmI. 
        self.RFWrite = 1 #Enable Write.
        self.ResultSelect = 0
        self.isBranch = 0
        self.MemOP = 0
        #BranchTargetSet -> Don't Care Condition
    
    def controlLoad(self):
        self.OP2Select = 1 #Select ImmI. 
        self.RFWrite = 1 #Enable Write.
        self.ResultSelect = 1 #Select LoadData.
        self.isBranch = 0
        self.MemOP = 0
        #BranchTargetSet -> Don't Care Condition
    
    def controlStore(self):
        self.OP2Select = 0 #Select ImmS. 
        self.RFWrite = 0 #Disable Write.
        self.isBranch = 0
        self.MemOP = 1 #Enable Write to data memory.
        #ResultSelect,BranchTargetSet -> Don't Care Condition
    
    def controlBtype(self):
        self.OP2Select = 2 #Select op2. 
        self.RFWrite = 0 #No Write
        self.isBranch = 0 #will be changed after execute stage where ALUResult will determine whether branch will be taken.
        self.MemOP = 0
        self.BranchTargetSet = 1 #Select ImmB
        #ResultSelect -> Don't Care Condition
    
    def controlJal(self):
        self.RFWrite = 1 #Enable Write
        self.isBranch = 1 #Select Unconditional Branch Target
        self.MemOP = 0
        self.BranchTargetSet = 0 #Select ImmJ
        self.ResultSelect = 3 #Select PC+4
        #OP2Select -> Don't Care Condition
    
    def controlJalr(self):
        self.OP2Select = 1
        self.RFWrite = 1 #Enable Write
        self.isBranch = 2 #Select ALUResult
        self.MemOP = 0
        self.ResultSelect = 3 #Select PC+4
        #BranchTargetSet -> Don't Care Condition

    def controlLui(self):
        self.RFWrite = 1 #Enable Write
        self.isBranch = 0 #Select PC+4
        self.MemOP = 0
        self.ResultSelect = 2 #Select ImmU
        #OP2Select,BranchTargetSet -> Don't Care Condition
    
    def controlAuipc(self):
        #self.OP2Select = 1
        self.RFWrite = 1 #Enable Write
        self.isBranch = 0 #Select PC+4
        self.MemOP = 0
        self.ResultSelect = 0 #Select ALUResult
        #OP2Select,BranchTargetSet -> Don't Care Condition
    
    
    