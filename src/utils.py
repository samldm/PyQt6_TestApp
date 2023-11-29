
class StringList(list):
    def __str__(self):
        return ", ".join(self)