## Docstring stuff



class ID3Tree(object):
    def __init__(self,trainingData=None,attributeValues=None):
        self.setTrainingData(trainingData)
        self.setAttributeValues(attributeValues)

    # Setter and getter methods -- 
    def setRoot(self,root):
        # sets root of tree
        self.__root = root

    def getRoot(self):
        # gets root of tree
        return self.__root

    def setTrainingData(self,trainingData):
        # trainingData should be a (k + 1) x N - dimensional numpy array
        # which looks like
        # [[ex1 val1],
        #  [ex2 val2],
        #  ..........
        #  [exN valN]]
        # where each example has k attributes
        self.__trainingData = trainingData

    def getTrainingData(self):
        # gets training data (see setTrainingData for formatting)
        return self.__trainingData

    def setAttributeValues(self,attributeValues):
        # sets attribute values
        self.__attributeValues = attributeValues

    def getAttributeValues(self):
        # gets attribute values
        return self.__attributeValues
    # end of setter/getter methods --

    #TBD
    def getBestAttribute(self,examples):
        # given a set of examples, gets the best attribute (see find for 
        # examples formatting). Does so by computing the infomation gain of 
        # each attribute. 
        pass

    def split(node,examples):
        bestAttribute = self.getBestAttribute(examples)
        node.setAttribute(bestAttribute)
        if self.getAttributeValues() is None:
            raise ValueError("Attribute Values must be set prior to training!")
        else:
            for value in self.getAttributeValues()[bestAttribute]:
                # add a new node
                child = Node()
                node.addChild(child) 
                # add examples   
                nextExamples = examples[ np.where(examples[:,bestAttribute] == value) ]
                if not child.isPure():
                    self.split(child,nextExamples)

    def ID3(self):
        if self.getTrainingData() is None:
            raise ValueError("Tree needs training data!")
        elif self.getAttributeValues() is None:
            raise ValueError("Tree needs attribute values!")
        elif self.getRoot() is not None:
            raise ValueError("Root of tree is already set!")
        else:
            root = Node()
            self.setRoot(root)
            self.split(root,self.getTrainingData())

    #TBD
    def classify(self,instance): 
        if self.getRoot() is None:
            raise ValueError("Tree has not been initialized.")
        else:
            currentNode = self.getRoot()


class Node(object):
    def __init__(self):
        pass

    def setData(self,data):
        self.__data = data

    def getData(self):
        return self.__data

    def setChildren(self,children):
        self.__children = children

    def getChildren(self):
        return self.__children

    def setAttribute(self,attribute):
        self.__attribute = attribute

    def getAttribute(self):
        return self.__attribute

    # not sure if the set/get parent methods are necessary
    def setParent(self,parent):
        self.__parent = parent

    def getParent(self):
        return self.__parent

    def addChild(self,child):
        self.getChildren().append(child)
    
    #TBD
    def isPure(self):
        pass


