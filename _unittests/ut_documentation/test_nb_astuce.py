# -*- coding: utf-8 -*-
"""
@brief      test log(time=5s)
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import add_missing_development_version
from pyquickhelper.ipythonhelper import test_notebook_execution_coverage
import papierstat


class TestNotebookAstuce(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["jyquickhelper"], __file__, hide=True)

    def test_notebook_astuces(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.assertTrue(papierstat is not None)
        folder = os.path.join(os.path.dirname(__file__),
                              "..", "..", "_doc", "notebooks", "astuces")
        test_notebook_execution_coverage(
            __file__, "", folder, 'papierstat', copy_files=[], fLOG=fLOG)


if __name__ == "__main__":
    unittest.main()
