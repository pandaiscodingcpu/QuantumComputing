# this file will contain the gates logic and using qskit
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


class Gates:
    def __init__(self,gate): # the object gets the type of gate user wants
        self.gate = gate
        self.qc = QuantumCircuit(1) # initialized the circuit
        #self.state = Statevector.from_instruction(self.qc)
    # initialize a circuit and get the state vector
    def hadamard(self):
        # Apply H gate to the running circuit
        self.qc.h(0)
        # Compute the updated statevector immediately after
        state = Statevector.from_instruction(self.qc)
        return state
    def x(self):
        # Apply X gate to the SAME running circuit
        self.qc.x(0)
        state = Statevector.from_instruction(self.qc)
        return state
    def y(self):
        # Apply X gate to the SAME running circuit
        self.qc.y(0)
        state = Statevector.from_instruction(self.qc)
        return state
    def z(self):
        # Apply X gate to the SAME running circuit
        self.qc.z(0)
        state = Statevector.from_instruction(self.qc)
        return state
    def s(self):
        # Apply X gate to the SAME running circuit
        self.qc.s(0)
        state = Statevector.from_instruction(self.qc)
        return state
    def t(self):
        # Apply X gate to the SAME running circuit
        self.qc.t(0)
        state = Statevector.from_instruction(self.qc)
        return state
g = Gates("gates")










