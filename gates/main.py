from gates import *
from visualize import *

def main():
    # create gates object
    print("Generating statevector for the hadamard gate.....")
    state = g.hadamard()
    # pass the state to render on bloch
    print("Rendering the Bloch sphere.......")
    plot(state)

if __name__ == "__main__":
    main()
