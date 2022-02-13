# GITHUB: https://github.com/NotCosmo/Python-Logic-Gates

class LogicGate():

    def __init__(self):
        self.OUTPUT = 0

    def AND_FUNC(self, INPUT_A, INPUT_B):

        if (INPUT_A == 0) and (INPUT_B == 0):
            self.OUTPUT = 0
            return self.OUTPUT

        if (INPUT_A == 0) and (INPUT_B == 1):
            self.OUTPUT = 0
            return self.OUTPUT

        if (INPUT_A == 1) and (INPUT_B == 0):
            self.OUTPUT = 0
            return self.OUTPUT

        if (INPUT_A == 1) and (INPUT_B == 1):
            self.OUTPUT = 1
            return self.OUTPUT

    def AND_SOLVE(self, INPUT_A, INPUT_B):

        if (INPUT_A == 0) and (INPUT_B == 0):
            self.OUTPUT = 0
            return print(
                "A  |  B  | OUT\n"
                f"{INPUT_A}  |  {INPUT_B}  | {self.OUTPUT}"
            )

        if (INPUT_A == 0) and (INPUT_B == 1):
            self.OUTPUT = 0
            return print(
                "A  |  B  | OUT\n"
                f"{INPUT_A}  |  {INPUT_B}  | {self.OUTPUT}"
            )

        if (INPUT_A == 1) and (INPUT_B == 0):
            self.OUTPUT = 0
            return print(
                "A  |  B  | OUT\n"
                f"{INPUT_A}  |  {INPUT_B}  | {self.OUTPUT}"
            )

        if (INPUT_A == 1) and (INPUT_B == 1):
            self.OUTPUT = 1
            return print(
                "A  |  B  | OUT\n"
                f"{INPUT_A}  |  {INPUT_B}  | {self.OUTPUT}"
            )

    def AND_TABLE(self):

        print(">> Displaying AND truth table..")
        return print(
            "A  |  B  |  OUT\n"
            f"0  |  0  |  {self.AND_FUNC(0, 0)}\n"
            f"0  |  1  |  {self.AND_FUNC(0, 1)}\n"
            f"1  |  0  |  {self.AND_FUNC(1, 0)}\n"
            f"1  |  1  |  {self.AND_FUNC(1, 1)}\n"
        )

    def OR_FUNC(self, INPUT_A, INPUT_B):

        if (INPUT_A == 1) or (INPUT_B == 1):
            self.OUTPUT = 1
            return self.OUTPUT

        else:
            self.OUTPUT = 0
            return self.OUTPUT

    def OR_SOLVE(self, INPUT_A, INPUT_B):

        if (INPUT_A == 1) or (INPUT_B == 1):
            self.OUTPUT = 1
        else:
            self.OUTPUT = 0

        return print(
            "A  |  B  | OUT\n"
            f"{INPUT_A}  |  {INPUT_B}  | {self.OUTPUT}"
        )

    def OR_TABLE(self):

        print(">> Displaying OR truth table..")
        return print(
            "A  |  B  |  OUT\n"
            f"0  |  0  |  {self.OR_FUNC(0, 0)}\n"
            f"0  |  1  |  {self.OR_FUNC(0, 1)}\n"
            f"1  |  0  |  {self.OR_FUNC(1, 0)}\n"
            f"1  |  1  |  {self.OR_FUNC(1, 1)}\n"
        )

    def NAND_FUNC(self, INPUT_A, INPUT_B):

        if (INPUT_A == 1) and (INPUT_B != 1):
            self.OUTPUT = 1
            return self.OUTPUT

        if (INPUT_A != 1) and (INPUT_B == 1):
            self.OUTPUT = 1
            return self.OUTPUT

        if (INPUT_A != 1) and (INPUT_B != 1):
            self.OUTPUT = 1
            return self.OUTPUT

        if (INPUT_A == 1) and (INPUT_B == 1):
            self.OUTPUT = 0
            return self.OUTPUT

    def NAND_SOLVE(self, INPUT_A, INPUT_B):

        if (INPUT_A == 1) and (INPUT_B != 1):
            self.OUTPUT = 1
            return print(
                "A  |  B  | OUT\n"
                f"{INPUT_A}  |  {INPUT_B}  | {self.OUTPUT}"
            )

        if (INPUT_A != 1) and (INPUT_B == 1):
            self.OUTPUT = 1
            return print(
                "A  |  B  | OUT\n"
                f"{INPUT_A}  |  {INPUT_B}  | {self.OUTPUT}"
            )

        if (INPUT_A != 1) and (INPUT_B != 1):
            self.OUTPUT = 1
            return print(
                "A  |  B  | OUT\n"
                f"{INPUT_A}  |  {INPUT_B}  | {self.OUTPUT}"
            )

        if (INPUT_A == 1) and (INPUT_B == 1):
            self.OUTPUT = 0
            return print(
                "A  |  B  | OUT\n"
                f"{INPUT_A}  |  {INPUT_B}  | {self.OUTPUT}"
            )

    def NAND_TABLE(self):

        print(">> Displaying NAND truth table..")
        return print(
            "A  |  B  |  OUT\n"
            f"0  |  0  |  {self.NAND_FUNC(0, 0)}\n"
            f"0  |  1  |  {self.NAND_FUNC(0, 1)}\n"
            f"1  |  0  |  {self.NAND_FUNC(1, 0)}\n"
            f"1  |  1  |  {self.NAND_FUNC(1, 1)}\n"
        )

    def XOR_FUNC(self, INPUT_A, INPUT_B):

        # XOR Gate is only true if either A or B value are true.
        if (INPUT_A == 1) or (INPUT_B == 1):
            self.OUTPUT = 1

        if (INPUT_A == 0) and (INPUT_B == 0):
            self.OUTPUT = 0

        if (INPUT_A == 1) and (INPUT_B == 1):
            self.OUTPUT = 0

        return self.OUTPUT

    def XOR_SOLVE(self, INPUT_A, INPUT_B):

        # XOR Gate is only true if either A or B value are true.
        if (INPUT_A == 1) or (INPUT_B == 1):
            self.OUTPUT = 1

        if (INPUT_A == 0) and (INPUT_B == 0):
            self.OUTPUT = 0

        if (INPUT_A == 1) and (INPUT_B == 1):
            self.OUTPUT = 0

        return print(
            "A  |  B  | OUT\n"
            f"{INPUT_A}  |  {INPUT_B}  | {self.OUTPUT}"
        )

    def XOR_TABLE(self):

        print(">> Displaying XOR truth table..")
        return print(
            "A  |  B  |  OUT\n"
            f"0  |  0  |  {self.XOR_FUNC(0, 0)}\n"
            f"0  |  1  |  {self.XOR_FUNC(0, 1)}\n"
            f"1  |  0  |  {self.XOR_FUNC(1, 0)}\n"
            f"1  |  1  |  {self.XOR_FUNC(1, 1)}\n"
        )

continue_ = True
while continue_ == True:

    user_input = str(input(">>> "))

    # AND Displays
    if (".and " in user_input) or (".AND " in user_input):
        temp = user_input.split(" ")

        # Check if input is a table
        if temp[1] == "table":
            LogicGate().AND_TABLE()

        else:
            # Remove the comma from "x,"
            INPUT_A = int(temp[1].replace(",",""))
            INPUT_B = int(temp[2])

            # Check if inputs are 1s and 0s
            if INPUT_A not in [1, 0] or INPUT_B not in [1, 0]:
                print("[!] Error Occured. Only accepted values are [1, 0]")
            else:
                LogicGate().AND_SOLVE(INPUT_A, INPUT_B)

    if (".or " in user_input) or (".OR " in user_input):
        temp = user_input.split(" ")

        if temp[1] == "table":
            LogicGate().OR_TABLE()

        else:

            # Remove the comma from "x,"
            INPUT_A = int(temp[1].replace(",", ""))
            INPUT_B = int(temp[2])

            # Check if inputs are 1s and 0s
            if INPUT_A not in [1, 0] or INPUT_B not in [1, 0]:
                print("[!] Error Occured. Only accepted values are [1, 0]")
            else:
                LogicGate().OR_SOLVE(INPUT_A, INPUT_B)

    if (".xor " in user_input) or (".XOR " in user_input):
        temp = user_input.split(" ")

        if temp[1] == "table":
            LogicGate().XOR_TABLE()

        else:

            # Remove the comma from "x,"
            INPUT_A = int(temp[1].replace(",", ""))
            INPUT_B = int(temp[2])

            # Check if inputs are 1s and 0s
            if INPUT_A not in [1, 0] or INPUT_B not in [1, 0]:
                print("[!] Error Occured. Only accepted values are [1, 0]")
            else:
                LogicGate().XOR_SOLVE(INPUT_A, INPUT_B)

    # Killswitch
    if user_input in ['.terminate', '.end', '.kill']:
        continue_ = False
        print("Program Terminated.")
