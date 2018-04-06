import random
import math

class Neuron:
    def __init__(self, weights):
        self.inside = 1
        self.outside = 1
        self.weights = []
        for elem in range(weights):
            self.weights.append((random.randrange(1, 999, 1))/float(1000))

class Network:
    def __init__(self, inputs, classes):
        self.bias = []
        self.inputs = []
        self.hiddens = []
        self.outputs = []
        self.target = []
        self.classes = classes
        print(classes)
        hidden = inputs * len(classes)
        self.bias.append(Neuron(hidden))
        self.bias.append(Neuron(len(classes)))
        self.learningRate = 0.1
        for elem in range(inputs):
            self.inputs.append(Neuron(hidden))
        for elem in range(hidden):
            self.hiddens.append(Neuron(len(classes)))
        for elem in classes:
            self.outputs.append(Neuron(0))

    def addClass(self, classes):
        taille = len(self.outputs)
        for elem in classes:
            self.classes.append(elem)
            self.outputs.append(Neuron(0))
            self.bias[1].weights.append((random.randrange(1, 999, 1))/float(1000))
            for hid in self.hiddens:
                hid.weights.append((random.randrange(1, 999, 1))/float(1000))
        for out in self.outputs:
            for inp in self.inputs:
                for inp2 in self.inputs:
                    inp2.weights.append((random.randrange(1, 999, 1))/float(1000))
                self.hiddens.append(Neuron(taille + len(classes)))
            self.bias[0].weights.append((random.randrange(1, 999, 1))/float(1000))

    def addInput(self, number):
        taille = len(self.inputs) * len(self.outputs)
        for elem in range(number):
            for outp in self.outputs:
                self.hiddens.append(Neuron(len(self.outputs)))
            self.inputs.append(Neuron(len(self.inputs[0].weights)))
        for elem in range(len(self.inputs) * len(self.outputs) - taille):
            for inp in self.inputs:
                inp.weights.append((random.randrange(1, 999, 1))/float(1000))
                self.bias[0].weights.append((random.randrange(1, 999, 1))/float(1000))


    def setClasses(self, data):
        self.classes = data

    def train(self, data):
        for elem in range(0, 150):
            item = random.randrange(0, len(data), 1)
            expected = [0] * len(self.classes)
            expected[data[item][1]] = 1
            print(expected)
            self.setInputsAndOutputs(data[item][0], expected)
            self.hiddenCalc()
            self.outputCalc()
            self.backPropagate()

    def setInputsAndOutputs(self, inputs, outputs):
        for idx, elem in enumerate(inputs):
            self.inputs[idx].inside = elem
            self.inputs[idx].outside = elem
        self.target = outputs

    def hiddenCalc(self):
        for idxi, i in enumerate(self.hiddens):
            inData = 0
            for idxj, j in enumerate(self.inputs):
                inData += self.inputs[idxj].weights[idxi] * self.inputs[idxj].outside
            inData += self.bias[0].inside * self.bias[0].weights[idxi]
            self.hiddens[idxi].inside = inData
            if inData < 0:
                self.hiddens[idxi].outside = 0
            else:
                self.hiddens[idxi].outside = inData

    def outputCalc(self):
        sumExp = 0
        maximum = 0
        for idxi, i in enumerate(self.outputs):
            inData = 0
            for idxj, j in enumerate(self.hiddens):
                inData += self.hiddens[idxj].weights[idxi] * self.hiddens[idxj].outside
            if inData > maximum:
                maximum = inData
        for idxi, i in enumerate(self.outputs):
            inData = 0
            for idxj, j in enumerate(self.hiddens):
                inData += self.hiddens[idxj].weights[idxi] * self.hiddens[idxj].outside
            inData += self.bias[1].inside * self.bias[1].weights[idxi]
            self.outputs[idxi].inside = inData - maximum
            sumExp += math.exp(inData - maximum)
        for idxi, i in enumerate(self.outputs):
            self.outputs[idxi].outside = math.exp(self.outputs[idxi].inside) / sumExp

    def backPropagate(self):
        self.hiddenToInput()
        self.outputToHidden()

    def hiddenToInput(self):
        for idxi, i in enumerate(self.inputs):
            for idxj, j in enumerate(self.hiddens):
                final = 0
                for idxk, k in enumerate(self.outputs):
                    if self.hiddens[idxj].inside < 0:
                        final += (self.outputs[idxk].outside - self.target[idxk]) * (self.hiddens[idxj].weights[idxk]) * (0)
                    else:
                        final += (self.outputs[idxk].outside - self.target[idxk]) * (self.hiddens[idxj].weights[idxk]) * (1)
                self.inputs[idxi].weights[idxj] = self.inputs[idxi].weights[idxj] - (self.learningRate * final)
        for idxj, j in enumerate(self.hiddens):
            final = 0
            for idxk, k in enumerate(self.outputs):
                if self.hiddens[idxj].inside < 0:
                    final += (self.outputs[idxk].outside - self.target[idxk]) * (self.hiddens[idxj].weights[idxk]) * (0)
                else:
                    final += (self.outputs[idxk].outside - self.target[idxk]) * (self.hiddens[idxj].weights[idxk]) * (1)
            self.bias[0].weights[idxj] = self.inputs[idxi].weights[idxj] - (self.learningRate * final)

    def outputToHidden(self):
        final = 0
        final2 = 0
        for idxi, i in enumerate(self.hiddens):
            for idxj, j in enumerate(self.outputs):
                final = (self.outputs[idxj].outside - self.target[idxj]) * self.hiddens[idxi].outside
                self.hiddens[idxi].weights[idxj] = self.hiddens[idxi].weights[idxj] - (self.learningRate * final)
        for idxj, j in enumerate(self.outputs):
            final2 = self.outputs[idxj].outside - self.target[idxj]
            self.bias[1].weights[idxj] = self.bias[1].weights[idxj] - (self.learningRate * final2)

    def log(self):
        #print("Inputs:")
        #for elem in self.inputs:
        #    print(elem.weights)
        #print("Hidden:")
        #for elem in self.hiddens:
        #    print(elem.weights)
        for elem in self.outputs:
            print(elem.outside)
        print("   ")
        print("     -----")
        print("   ")

    def test(self, data):
        for idx, elem in enumerate(data):
            self.inputs[idx].inside = elem
            self.inputs[idx].outside = elem
        self.hiddenCalc()
        self.outputCalc()
        self.log()
        self.getClass()

    def getClass(self):
        supIdx = 0
        supVal = 0.0
        for idx, elem in enumerate(self.outputs):
            if elem.outside > supVal:
                supIdx = idx
                supVal = elem.outside
        self.resultatActuel = self.classes[supIdx]
        print(self.resultatActuel)

network = Network(3, ["chien", "chat", "humain"])
exemple1 = [[4, 1, 0], 0]
#4 pattes, fourrure et pas felin pour chien
exemple2 = [[4, 1, 5], 1]
#4 pattes, fourrur, et felin pour chat
exemple3 = [[2, 0, 0], 2]
#2 jambes, pas de fourrure, pas un felin pour l'humain
total = [exemple1, exemple2, exemple3]
network.train(total)
network.test([4, 1, 5])
network.test([4, 1, 0])
network.test([2, 0, 0])