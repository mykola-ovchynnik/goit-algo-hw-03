import os
import shutil
import unittest
from file_organizer import parse_arguments, copy_files_recursive


class TestFileOrganizer(unittest.TestCase):
    def setUp(self):
        self.test_source_dir = "test_source"
        self.test_dest_dir = "test_dest"
        os.makedirs(self.test_source_dir, exist_ok=True)
        os.makedirs(self.test_dest_dir, exist_ok=True)

        with open(os.path.join(self.test_source_dir, "test1.txt"), "w") as f:
            f.write("This is a test file.")
        with open(os.path.join(self.test_source_dir, "test2.jpg"), "w") as f:
            f.write("This is another test file.")
        os.makedirs(os.path.join(self.test_source_dir, "subdir"), exist_ok=True)
        with open(os.path.join(self.test_source_dir, "subdir", "test3.png"), "w") as f:
            f.write("This is a test file in a subdirectory.")

    def tearDown(self):
        shutil.rmtree(self.test_source_dir)
        shutil.rmtree(self.test_dest_dir)

    def test_copy_files_recursive(self):
        copy_files_recursive(self.test_source_dir, self.test_dest_dir)
        self.assertTrue(
            os.path.exists(os.path.join(self.test_dest_dir, "txt", "test1.txt"))
        )
        self.assertTrue(
            os.path.exists(os.path.join(self.test_dest_dir, "jpg", "test2.jpg"))
        )
        self.assertTrue(
            os.path.exists(os.path.join(self.test_dest_dir, "png", "test3.png"))
        )


if __name__ == "__main__":
    unittest.main()
