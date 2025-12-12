class Calculator:
    def __init__(self):
        self.a = int(input("Enter the value a: "))
        self.b = int(input("Enter the value b: "))

    def calculate(self, operation):
        if operation == "add":
            return self.a + self.b
        elif operation == "sub":
            return self.a - self.b
        elif operation == "mul":
            return self.a * self.b
        elif operation == "div":
            return self.a / self.b
        else:
            return "Invalid operation"
calc = Calculator()
        
        
op = input("Enter operation (add/sub/mul/div): ")
print("Result:", calc.calculate(op))
