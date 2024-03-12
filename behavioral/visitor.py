from abc import ABC, abstractmethod

class FileSystemElement(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class File(FileSystemElement):
    def __init__(self, name):
        self.name = name

    def accept(self, visitor):
        visitor.visit_file(self)

class Directory(FileSystemElement):
    def __init__(self, name):
        self.name = name
        self.elements = []

    def accept(self, visitor):
        visitor.visit_directory(self)

    def add_element(self, element):
        self.elements.append(element)

class Visitor(ABC):
    @abstractmethod
    def visit_file(self, file):
        pass

    @abstractmethod
    def visit_directory(self, directory):
        pass

class SaveVisitor(Visitor):
    def visit_file(self, file):
        print(f"Saving file: {file.name}")

    def visit_directory(self, directory):
        print(f"Saving directory: {directory.name}")
        for element in directory.elements:
            element.accept(self)

root_directory = Directory("root")
file_a = File("fileA.txt")
directory_b = Directory("dirB")
file_b1 = File("fileB1.txt")

root_directory.add_element(file_a)
root_directory.add_element(directory_b)
directory_b.add_element(file_b1)

save_visitor = SaveVisitor()
root_directory.accept(save_visitor)
