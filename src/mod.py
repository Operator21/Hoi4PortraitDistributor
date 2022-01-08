import inspect

class Mod:
    def __init__(self, name, gameVersion):
        self.name = name
        self.gameVersion = gameVersion

    #def __init__(self):
     #   self.name = input("Enter your mod name: ")
      #  self.gameVersion = input("Enter targeted version: ")

    def FileName(self):
        return self.name.lower().replace(" ", "_")

    def ModFile(self, path = False):
        mod = (
            'name="' + self.name + '"'
            'tags={'
                '"Graphics"'
            '}'
            'supported_version="1.*"'
            )
        if path:
            mod += 'path="mod/' + self.FileName() + '"'
        return mod