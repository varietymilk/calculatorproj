import npyscreen

class CalculatorApp(npyscreen.NPSAppManaged):
    def onStart(self):
        self.num1 = None
        self.num2 = None
        self.addForm('MAIN', CalculatorForm)
    pass

class CalculatorForm(npyscreen.ActionForm):
    def afterEditing(self):
        self.parentApp.num1 = self.num1.value
        self.parentApp.num2 = self.num2.value
        self.parentApp.setNextForm(None)
    
    def create(self):
        self.add(npyscreen.FixedText)
        self.num1 = self.add(npyscreen.TitleText, name="number 1")
        self.num2 = self.add(npyscreen.TitleText, name="number 2")

    def on_cancel(self):
        self.parentApp.switchFormPrevious()

if __name__ == '__main__':
    calculator = CalculatorApp()
    calculator.run()
    print(calculator.num1)

def calculate(int1, int2):
    number1 = int(int1)
    number2 = int(int2)
    print('what operation\n1)addition\n2)subtraction\n3)division\n4)multiplication')    
    
    while True:
        operation = int(input("Select number 1-4: "))
        if operation == 1:
            print(number1+number2)
            break
        if operation == 2:
            print(number1-number2)
            break
        if operation == 3:
            print(number1/number2)
            break
        if operation == 4:
            print(number1*number2)
            break
        else:
            print("???")








## num1 = int(input('number 1:'))
## num2 = int(input('number 2:'))
# calculate(num1,num2)

