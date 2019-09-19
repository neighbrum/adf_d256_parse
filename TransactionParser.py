
import ADF
import TSYS
from io import StringIO

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
        thr = TSYS.TransmissionHeaderRecord(self.f)
        print(thr.data)

def main():
    #ADFSTM = ADFStateMachine("data/test_4.ADF")
    #ADFSTM.run()
    TSYSSTM = TSYSStateMachine('data/test_0.TSYS')
    TSYSSTM.run()


if __name__ == "__main__":
    main()