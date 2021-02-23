from abc import ABC, abstractmethod

class AbstracTemplate(ABC):

    def template(self) -> None:T
    # The template method defines the skeleton of an algorithm.
        self.evaluate()
        self.base_operation2()
        self.required_operations1()
        self.required_operations2()

    # These operations already have implementations.
    def evaluate(x, y_hat):
    ''' Calcula a acurácia da ConvNet (variável cnn)
      para o par de entradas e saídas desejadas
      x, y_hat. Aqui assume-se que y_hat está
      originalmente no formato one-hot. Tanto
      x quanto y_hat devem ser lotes, não amostras
      individuais.
    '''
        y = cnn(x).argmax(dim=1)
        y_hat = y_hat.argmax(dim=1)
        return 100*float((y == y_hat).sum()) / len(y)

    def base_operation2(self) -> None:
        print("AbstractClass says: But I let subclasses override some operations")

    # These operations have to be implemented in subclasses.
    @abstractmethod
    def required_operations1(self) -> None:
        pass

    @abstractmethod
    def required_operations2(self) -> None:
        pass

class ConcreteClass1(AbstractClass):

    def required_operations1(self) -> None:
        print("ConcreteClass1 says: Implemented Operation1")

    def required_operations2(self) -> None:
        print("ConcreteClass1 says: Implemented Operation2")

def client_code(abstract_class: AbstractClass) -> None:

    abstract_class.template_method()

if __name__ == "__main__":
    
    print("Same client code can work with different subclasses:")
    
    client_code(ConcreteClass1())