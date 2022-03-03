import unittest, sys

sys.path.append("..")
from tests.root_path import testSuiteTestCase


def suite():
    suite_set = unittest.TestSuite()
    suite_set.addTest(testSuiteTestCase("testRootpath"))
    suite_set.addTests(
        [testSuiteTestCase("testRootpath"), testSuiteTestCase("testRootpath2")]
    )
    return suite_set


if __name__ == "__main__":
    tests = suite()
    runner = unittest.TextTestRunner()
    runner.run(tests)
