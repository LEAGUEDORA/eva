from typing import Text
from PIL import Image
from pixelmatch.contrib.PIL import pixelmatch
import os

class ImageDiffClass:

    def __init__(self, directory: Text, file1: Text, file2: Text) -> None:
        self.directory = directory
        self.file1 = file1
        self.file2 = file2

    def getDifferenceInImage(self):                
        imge1 = Image.open(os.path.join(self.directory, self.file1))
        imge2 = Image.open(os.path.join(self.directory, self.file2))
        img_diff = Image.new("RGB", imge1.size)
        mismatch = pixelmatch(imge1, imge2, img_diff, includeAA = True)
        saved_image = f"{self.file1}_{self.file2}"
        img_diff.save(os.path.join(self.directory, saved_image))
        return saved_image