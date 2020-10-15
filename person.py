class Person:
  def __init__(self, cod, name, address, phone):
    self.__codigo = cod
    self.name = name
    self._address = address
    self._phone = phone
    
  def PrintName(self):
    print(self.name)

  def _PrintAddress(self):
    print(self._address)

  def _PrintPhone(self):
    print(self._phone)

class PF(Person):
  def __init__(self, cod, name, address, phone, cpf, age, weight, height):
    Person.__init__(self, cod, name, address, phone)
    self.__cpf = cpf
    self.age = age
    self.weight = float(weight)
    self.height = float(height)
    self.imc = 0
    
  def PrintCPF(self):
    print(self.__cpf)

  def PrintAge(self):
    print(self.age)

  def PrintWeight(self):
    print(self.weight)

  def PrintHeight(self):
    print(self.height)
    
  def CalcuteIMC(self):
    self.imc = self.weight/(self.height*self.height)
    return self.imc
  
  def PrintIMC(self):
    print ("O IMC de %s é %f" % (self.name,self.CalcuteIMC()))
      
class PJ(Person):
  def __init__(self, cod, name, address, phone, cnpj, StateRegister, NumberEmployees):
    Person.__init__(self, cod, name, address, phone)
    self.__cnpj = cnpj
    self.__StateRegister = StateRegister
    self.NumberEmployees = NumberEmployees
    
  def PrintCNPJ(self):
    print(self.__cnpj)

  def PrintStateRegister(self):
    print(self.__StateRegister)
    
  def __EmitInvoice(self):
    print(self.__StateRegister)
    
  def getInvoice(self):
    return (self.__EmitInvoice())
