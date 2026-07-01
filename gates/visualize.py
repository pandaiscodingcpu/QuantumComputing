# this file will contain the visualization on bloch sphere
import numpy as np
from qutip import Bloch,Qobj
import matplotlib.pyplot as plt
def plot(statevector):
    # convert the qiskit's statevector into QuTip quantum object -> ket
    ket = Qobj(statevector)

    # initialize the bloch sphere
    b = Bloch()
    b.add_states(ket)
    #render the sphere
    b.show()
    plt.show()

