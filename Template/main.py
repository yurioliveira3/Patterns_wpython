from abc import ABC, abstractmethod

class AbstractClass(ABC):

    def template_method(self) -> None:
    # The template method defines the skeleton of an algorithm.
        self.base_operation1()
        self.base_operation2()
        self.required_operations1()
        self.required_operations2()

    # These operations already have implementations.
    def base_operation1(self) -> None:
        print("AbstractClass says: I am doing the bulk of the work")

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
    
    client_code(ConcreteClass1())