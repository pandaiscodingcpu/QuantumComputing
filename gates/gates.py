# this file will contain the gates logic and using qskit
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


class Gates:
    def __init__(self,gate): # the object gets the type of gate user wants
        self.gate = gate

    # initialize a circuit and get the state vector
    # build a basic hadamard gate
    def hadamard(self):
        # 1 qubit circuit and apply the hadamard gate
        qc = QuantumCircuit(1)
        qc.h(0)
        state = Statevector.from_instruction(qc)
        print(state)
        return state

g = Gates("gates")












