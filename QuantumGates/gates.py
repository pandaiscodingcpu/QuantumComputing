import numpy as np
import math

# Define gates
h_gate = (1/math.sqrt(2)) * np.array([[1, 1], [1, -1]])
cnot_gate = np.array([[1, 0, 0, 0],
                      [0, 1, 0, 0],
                      [0, 0, 0, 1],
                      [0, 0, 1, 0]])

# Define base states as column vectors (kets)
ket0 = np.array([[1], [0]])
ket1 = np.array([[0], [1]])

# Create the combined state |01> using the Kronecker product
state_01 = np.kron(ket0, ket1)

# Apply CNOT: State_final = CNOT * state_01
# Since CNOT is 4x4 and state_01 is 4x1, the result is 4x1
output_state = np.dot(cnot_gate, state_01)

print("Combined State |01>:\n", state_01)
print("\nState after CNOT:\n", output_state)

# demonstrating bell state
identity = np.eye(2)

h_on_q0 = np.kron(h_gate, identity) # this applies hadamard on q0 and does nothing to q1

state_00 = np.kron(ket0, ket0)

step1 = np.dot(h_on_q0, state_00)

bell_state = np.dot(cnot_gate, step1)

print("Final Bell State Vector:\n", bell_state)