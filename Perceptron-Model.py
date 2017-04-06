class Perceptron:
    def __init__(self,sample):
        self.sample = sample

    def setWeight(self,weight):
        self.weight = weight

    def getBetaY(self,result,answer):
        if result > 0:
            Y = 1
        else:
            Y = -1

        if answer == Y:
            return 1*Y
        else :
            return -1*Y

    def networkTrain(self):
        for i in sample:
            result = i[0]*weight[0]+i[1]*weight[1]
            betaY = self.getBetaY(result,i[2])
            self.weight[0] = self.weight[0]+i[0]*betaY
            self.weight[1] = self.weight[1]+i[1]*betaY
            print(weight)

if __name__ == "__main__":
    sample = [[0.3,0.7,1],[-0.6,0.3,-1],[0.7,0.3,1],[-0.2,-0.8,-1]]
    weight = [-0.6,0.8]
    per = Perceptron(sample)
    per.setWeight(weight)
    per.networkTrain()
