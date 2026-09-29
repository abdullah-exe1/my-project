import numpy as np


class neuron:

    def __init__(self, inputs):
        self.w = np.random.randn(inputs)
        self.b = 0


    def forward(self, x  ):
        return(np.dot(self.w, x) + self.b)

    def train(self, x, lr, target):
        pred = self.forward(x)
        error = pred - target

        self.w = self.w - (lr * error) * x
        self.b = self.b - (lr * error)

class layers:

    def __init__(self, input , neurons):
        self.neurons = []

        for i in range(neurons):
            self.neurons.append(neuron(input))

    def forward(self, x):
        results = []

        for neuron in self.neurons:
            results.append(neuron.forward(x))

        return np.array(results)

    def train (self, x ,lr , target):
        for i in range(len(self.neurons)):
            self.neurons[i].train(x, lr, target[i])



x = np.array([-0.41, 0.22, -0.3, 0.4, 0.12])
y = 717



layer1 = layers(5, 20)
layer2 = layers(20, 5)
layer3 = layers(5, 1)


for ai in range(1000000):


    z = layer1.forward(x)
    o = layer2.forward(z)
    j = layer3.forward(o)


    loss = x - j


    mae_loss = np.mean(np.abs(loss))
    layer3.neurons[0].train(o , 0.000001, y)


    #layer1.train(x, 0.01, y)
    #layer2.train(o, 0.01, y)
    #layer3.train(j, 0.01, y)


    if ai % 100000 == 0:
        print(f'{(ai - 1) + 1}-pred is {j}')
        print()
        print(f'{(ai - 1) + 1}-loss is {mae_loss:,.2f} ')
        print()