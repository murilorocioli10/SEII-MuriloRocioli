import numpy as np
import matplotlib.pyplot as plt
#import pendulo

def f(t, x, u):
    # State vector
    # x = [x2 x1]^T

    x1 = x[0]
    x2 = x[1]

    # Variáveis do aeropêndulo
    l1 = .75
    l2 = 1.2
    J = 1e-2
    p = .85*9.81
    ua = .1
    x_dot = np.array( [ x2, \
        (-p*l1/J)*np.sin(x1) + (-ua/J)*x2 + (l2/J)*u ], dtype='float64')
    return x_dot

# Runge Kutta de 4a ordem - Metodo iterativo para melhorar precisão da resposta 
def rk4(tk, h, xk, uk):
    k1 = f(tk, xk, uk)
    k2 = f(tk + h/2.0, xk + h*k1/2.0, uk)
    k3 = f(tk + h/2.0, xk + h*k2/2.0, uk)
    k4 = f(tk + h, xk + h*k3, uk)
    xkp1 = xk + (h/6.0)*(k1 + 2*k2 + 2*k3 + k4)

    return xkp1


def saida(ang): #Definindo função de saída no pendulo 
    print('FunçãoSaida')
    print(ang)
    if ang is None:
        ang = 30 
    # PARÂMETROS DE SIMULAÇÃO
    h = 1e-4 # Sample time
    t = np.arange(0,5,h) # vetor tempo
    tam = len(t) # comprimento de t
    # Vetor de estados
    x = np.zeros([2, tam], dtype='float64')
    
    Kp = 30 # ganho proporcional 
    Kd = 2e+4 # ganho derivativo
    Ki = 40 # ganho integral
    phi_ref = (ang*np.pi)/180 # ângulo de referência 
    
    l1 =.75
    l2 = 1.2
    J = 1e-2
    p = .85*9.81
    u_eq = np.sin(phi_ref)*p*l1/l2 # ângulo de equilibrio
    # Vetor de entrada
    u = np.zeros([tam],dtype='float64') # u de equilibrio
    e = np.zeros([tam], dtype='float64') # erro de rastreamoento
    e1 = 0

    # Execução da simulação
    for k in range(tam-1):
    # u(k) será calculado aqui na simulação
    # Atualização do estado

        
        #CONTROLADOR PID Discreto
        e[k] = phi_ref - x[0][k]  # erro da referência
        
        u[k] = Kp*e[k] + Ki*(e[k] + e1) + Kd*(e[k] - e1) + u_eq # ação de controle -> equação de diferenças

        e1 = e[k]
        x[:,k+1] = rk4(t[k], h, x[:,k], u[k]) # saída da planta


    return t, x

# Comportamento da planta
if __name__ == '__main__':
    t, x = saida()
    plt.subplot(2, 1, 1)
    plt.plot(t,x[0,:]*180/np.pi)
    plt.ylabel('$x_1$ - i ')
    plt.subplot(2, 1, 2)
    plt.plot(t,x[1,:]*180/np.pi)
    plt.ylabel('$x_2$ - q')
    plt.xlabel('t [s]')
    plt.show()





