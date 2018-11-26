import random

def getrandom(num, maxnum):
    arr = []
    for _ in range([maxnum]):
        arr.append(random.uniform(0.0, maxnum))
    return arr

class Neruon():
    def __init__(self, bias, weights):
        self.weights = weights
        self.bias = bias
    
    def runcalc(self, invals):
        curval = invals + self.bias
        outvals = [weight * curval for weight in self.weights]
        return outvals

    def update(self, bias, weights):
        self.weights = weights
        self.bias = bias

class Layer():
    def __init__(self, layerneurons, outputneurons):
        self.layerneurons = layerneurons
        self.outputneurons = outputneurons
        neurons = []
        for _ in range(layerneurons):
            neurons.append(Neruon(random.uniform(-5, 5), getrandom(outputneurons, 1.0)))
        self.neurons = neurons

    def layercalc(self, inputvals):
        outvals = []
        if len(inputvals) != self.layerneurons:
            raise Exception('inputs of len', len(inputvals, 'Is not equal to layer nerons', self.layerneurons))
        for _ in range(self.outputneurons):
            outvals.append(0)
        for i in range(self.layerneurons):
            tempweights = self.neurons[i].runcalc(inputvals[i])
            for i in range(self.outputneurons):
                outvals[i] += tempweights[i]
        return outvals

"""
example layout

layout = {
    inputs : 30,
    hiddenlayers : 3
    hiddenLayerNeurons : [15,10,5]
    outputs : 3
}
"""

class Network():
    def __init__(self, layout):
        layers = []

        layers.append(Layer(layout['inputs'], layout['hiddenLayerNeurons'][0])) #create input layer

        for i in range(layout['hiddenlayers'] - 1):
            layers.append(Layer(layout['hiddenLayerNeurons'][i], layout['hiddenLayerNeurons'][i + 1])) #create hidden layers

        layers.append(Layer(layout['hiddenLayerNeurons'][-1], layout['outputs'])) #create final hidden and output

        self.layers = layers
        print('netcreated')

    def runnet(self, inputdata):
        curdata = inputdata
        for layer in self.layers:
            curdata = layer.layercalc(curdata)
        return curdata
            







        
        
    
