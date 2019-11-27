class Crate:
    def __init__(self, inputWidth, inputLength, inputHeight):
        self.width = inputWidth
        self.length = inputLength
        self.height = inputHeight

    def increaseLength(self, additionLength):
        self.length = self.length + additionLength;

    def __repr__( self ):
        return "width: " + str(self.width) \
               + ", length: " + str(self.length) \
               + ", height: " + str(self.height)

    def calVolumn(self):
        return self.width * self.height * self.length