import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class layer:

    def __init__(self, input, output ):
        self.w = np.random.randn(output, input) * 0.1
        self.b = np.zeros((output, 1))
        self.last_x = None

    def forward(self, x, ):

        self.last_x = x
        return np.dot(self.w, x) + self.b
    
    def backward(self, d_out, lr):
        dW = np.dot(d_out, self.last_x.T)
        dB = np.sum(d_out ,keepdims=True ,axis=1)
        d_x = np.dot(self.w.T , d_out)

        self.w -= dW * lr
        self.b -= dB * lr

        return d_x

    def  scale(a):

        a = a
        a_std = np.std(a, axis=0)
        a_mean = np.mean(a, axis=0)
        scaled_a = (a - a_mean) / a_std

        return scaled_a

df = pd.read_excel("real_estate1.xlsx")


x = df[['Masa7a' , 'Ghoraf' , 'Doraat_Miah' , '3omr_Albeet' , 'Al_Mantaqa']].values
y = df[['Target_Price' , 'Target_Installment' , 'Target_Deposit']].values


sx = layer.scale(x)
sy = layer.scale(y)

L1 = layer(5, 16)
L2 = layer(16, 8)
L3 = layer(8, 3)


out1 = L1.forward(sx.T)
out2 = L2.forward(out1)
out3 = L3.forward(out2)

d_out1 = L3.backward((out3 - sy.T), 0.001)
d_out2 = L2.backward(d_out1, 0.001)
_ = L1.backward(d_out2, 0.001) 


y_std = np.std(y, axis=0).reshape(3, 1)
y_mean = np.mean(y, axis=0).reshape(3, 1)


loss_history = []

L1.w = np.load("L1_AI3.W.npy")
L1.b = np.load("L1_AI3.B.npy")

L2.w = np.load("L2_AI3.W.npy")
L2.b = np.load("L2_AI3.B.npy")

L3.w = np.load("L3_AI3.W.npy")
L3.b = np.load("L3_AI3.B.npy")


for ai in range(500001):

    out1 = L1.forward(sx.T)
    out2 = L2.forward(out1)
    out3 = L3.forward(out2)

    d_out1 = L3.backward(((out3 - sy.T)), 0.00001)
    d_out2 = L2.backward(d_out1, 0.00001)
    _ = L1.backward(d_out2, 0.00001) 


    pred_scaled = out3
    pred_real = (out3 * y_std) + y_mean
    true_real = (sy.T * y_std) + y_mean


    mae_loss = np.mean(np.abs(sy.T - out3))

    acc = (1 - mae_loss) * 100


    if ai % 100000 == 0:
        print(f'{(ai - 1) + 1}-pred is {pred_real[:, 0]} the true is {true_real[:, 0]}')
        print()
        print(f'{(ai - 1)  + 1}-accurse is {acc}')
        print


    
    acc1 = np.mean(np.abs(sy.T - out3))
    if ai % 100 == 0:
        loss_history.append(acc)


np.save("L1_AI3.W.npy", L1.w)
np.save("L1_AI3.B.npy", L1.b)

np.save("L2_AI3.W.npy", L2.w)
np.save("L2_AI3.B.npy", L2.b)

np.save("L3_AI3.W.npy", L3.w)
np.save("L3_AI3.B.npy", L3.b)


np.save("x_mean.npy", np.mean(x, axis=0).reshape(5, 1))
np.save("x_std.npy", np.std(x, axis=0).reshape(5, 1))


np.save("y_mean.npy", np.mean(y, axis=0).reshape(3, 1))
np.save("y_std.npy", np.std(y, axis=0).reshape(3, 1))
plt.plot(loss_history, color='blue', linewidth=2)
plt.title("Model Training Progress (Loss Curve)")
plt.xlabel("Iterations (x10)")
plt.ylabel("Error Rate (MAE)")
plt.grid(True)
plt.ylim(0, 100)
plt.show() 



