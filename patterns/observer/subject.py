"Author: Jashan"
class Subject:
    def __init__(self):
        self._observers = []


    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:s
            observer.update(self, message)
