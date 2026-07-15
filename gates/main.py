from gates import *
from visualize import *

def main():
    # create gates object
    print("Select the gate to be visualized: ")
    print("1. Hadamard Gate\n2. Pauli X gate\n3. Pauli Y gate\n4. Pauli Z gate\n5. S gate\n6. T gate")
    choice = int(input())
    if choice == 1:
        state = g.hadamard()
        plot(state)
    elif choice == 2:
        state = g.x()
        plot(state)
    elif choice == 3:
        state = g.y()
        plot(state)
    elif choice  == 4:
        state = g.z()
        plot(state)
    elif choice == 5:
        state = g.s()
        plot(state)
    elif choice == 6:
        state = g.t()
        plot(state)
    else:
        print("Incorrect choice")
    plt.show()
if __name__ == "__main__":
    main()
