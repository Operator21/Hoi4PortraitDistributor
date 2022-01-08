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

    def ModFile(self):
        return inspect.cleandoc(f"""version="1"
                tags={{
                    "Graphics"
                }}
                name="{self.name}"
                supported_version="{self.gameVersion}"
                path="mod/{self.FileName()}""")
        