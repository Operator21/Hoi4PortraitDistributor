import unittest, os, sys
# Add the "src" directory to the Python path
sys.path.append(os.path.abspath("src"))

from filehelper import CopyFile
import PIL.Image as Image


class TestFileHelper(unittest.TestCase):

    def setUp(self):
        basepath = f"{os.getcwd()}"
        self.source = f"{basepath}/test_source.png"
        self.destination = f"{basepath}/test_dest.dds"
        # creating a sample image file to be used as source
        image = Image.new('RGB', (100, 100), color=(255, 0, 0))
        image.save(self.source)

        # Check if the file is created and exists in the specified path
        if not os.path.isfile(self.source):
            raise FileNotFoundError(f"{self.source} file not created.")
        print(f"{self.source} file created successfully.")

    def tearDown(self):
        # removing the source and destination files after test
        os.remove(self.source)
        if os.path.exists(self.destination):
            os.remove(self.destination)

    def test_CopyFile(self):
        CopyFile(self.source, self.destination)
        # check if file exists at destination
        self.assertTrue(os.path.exists(self.destination))

if __name__ == '__main__':
    unittest.main()
