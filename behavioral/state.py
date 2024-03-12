from abc import ABC, abstractmethod

class DocumentState(ABC):
    @abstractmethod
    def publish(self):
        pass

class Draft(DocumentState):
    def publish(self):
        print("Draft published. Moving to moderation.")
        return Moderation()

class Moderation(DocumentState):
    def publish(self):
        print("Moderation approved. Document is now published.")
        return Published()

class Published(DocumentState):
    def publish(self):
        print("Document is already published.")

class Document:
    def __init__(self):
        self.state = Draft()

    def publish(self):
        self.state = self.state.publish()

document = Document()

document.publish()
document.publish() 
document.publish()  
