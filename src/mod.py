class Mod:
    def __init__(self, name, gameVersion):
        self.name = name
        self.gameVersion = gameVersion

    def FileName(self):
        return self.name.lower().replace(" ", "_")

    def ModFile(self, path = False):
        return f"""
            name="{self.name}"
            tags={{
                "Graphics"
            }}
            supported_version="1.*"
            {f'path="mod/{self.FileName()}"' if path else ""}
        """