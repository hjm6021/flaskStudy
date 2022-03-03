import os, unittest, tempfile, sys

sys.path.append("../")
import flaskr


class FlaskrTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.db_fd, flaskr.app.config["DATABASE"] = tempfile.mkdtemp()
        flaskr.app.config["TESTING"] = True
        self.app = flaskr.app.test_client()
        flaskr.init_db()

    def tearDown(self) -> None:
        os.close(self.db_fd)
        os.unlink(flaskr.app.config["DATABASE"])


if __name__ == "__main__":
    unittest.main()
