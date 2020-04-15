from TransactionParser import ADF
from TransactionParser import TSYS
from io import StringIO
import os
class ADFStateMachine:
 
    def __init__(self,fn):
        self.f = StringIO(open(fn,"r").read().replace("\n",""))
        self.records = []

    def run(self):
        record = self.f.read(4)
        while(len(record) == 4):
            self.f.seek(self.f.tell()-4)
            self.records.append(ADF.Records.LUT[record][-1](self.f))
            record = self.f.read(4)
        self.f.close()

class TSYSStateMachine:
    def __init__(self,fn):
        self.f = StringIO(open(fn,"r").read().replace("\n",""))
        self.records = []

    def run(self):
        transmissionHeader = TSYS.TransmissionHeader(self.f)

        batchHeader = TSYS.BatchHeader(self.f)

        merchantHeader = TSYS.MerchantHeader(self.f)

        financialRecord = TSYS.FinancialRecord(self.f)

        #if there is a extension record, handle it here... then loop until no more batch headers?

        batchTrailer = TSYS.BatchTrailer(self.f)

        transmissionTrailer = TSYS.TransmissionTrailer(self.f)

def main():
    #ADFSTM = ADFStateMachine("data/test_4.ADF")
    #ADFSTM.run()
    print(os.getcwd())
    TSYSSTM = TSYSStateMachine('data/test_1.TSYS')
    TSYSSTM.run()


if __name__ == "__main__":
    main()