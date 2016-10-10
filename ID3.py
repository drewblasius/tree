
class ID3Tree(object):
    def __init__(self):
        pass

    def setRoot(self,root):
        self.__root = root

    def getRoot(self):
        return self.__root

    def findByAttribute(examples,attribute,value):
        # examples is a 2 x N numpy array which looks like
        # [[ex1,val1],
        #  [ex2,val2],
        #  [exN,valN]],
        # where exJ are themselves 1-d arrays of length k.
        # returns a subarray with examples[attribute] = value
        



    def split(node,examples):
        bestAttribute = self.getBestAttribute(examples)
        node.setAttrbute(bestAttribute)
        if self.getAttributeValues() is None:
            raise ValueError("Attribute Values must be set prior to training!")
        else:
            for value in self.getAttributeValues()[bestAttribute]:
                child = node.addChild()
                #Get the training examples which have this value
                node.addData(correctExamples) # needs to be finished
                if not isPure(child.getData()):
                    self.split(child,correctExamples)

