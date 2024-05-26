class LogicGate:
    def __init__(self, n):
        self.name = n
        self.output = None

    def getLabel(self):
        return self.name

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate " + self.getLabel() + "-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate " + self.getLabel() + "-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 or b == 1:
            return 1
        else:
            return 0


class UnaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)
        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate " + self.getLabel() + "-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class NotGate(UnaryGate):
    def __init__(self, n):
        UnaryGate.__init__(self, n)

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1


class NandGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 0
        else:
            return 1


class NorGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 0 and b == 0:
            return 1
        else:
            return 0


class Connector:
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


class InputConnector:
    def __init__(self, val):
        self.value = val

    def getOutput(self):
        return self.value

    def getFrom(self):
        return self


def main():
    # Inputs for the gates
    a_val = int(input("Enter value for A (0 or 1): "))
    b_val = int(input("Enter value for B (0 or 1): "))
    c_val = int(input("Enter value for C (0 or 1): "))
    d_val = int(input("Enter value for D (0 or 1): "))

    # First part of the equality: NOT ((A AND B) OR (C AND D))
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)

    # Set the inputs for the first part
    g1.pinA = InputConnector(a_val)
    g1.pinB = InputConnector(b_val)
    g2.pinA = InputConnector(c_val)
    g2.pinB = InputConnector(d_val)

    output1 = g4.getOutput()
    print(f"Output of NOT ((A AND B) OR (C AND D)) is {output1}")

    # Second part of the equality: NOT (A AND B) AND NOT (C AND D)
    g5 = NandGate("G5")
    g6 = NandGate("G6")
    g7 = AndGate("G7")

    c4 = Connector(g5, g7)
    c5 = Connector(g6, g7)

    # Set the inputs for the second part
    g5.pinA = InputConnector(a_val)
    g5.pinB = InputConnector(b_val)
    g6.pinA = InputConnector(c_val)
    g6.pinB = InputConnector(d_val)

    output2 = g7.getOutput()
    print(f"Output of NOT (A AND B) AND NOT (C AND D) is {output2}")

main()
