# -*- coding: utf-8 -*-
"""
@brief      test log(time=2s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import ExtTestCase, get_temp_folder
from papierstat.datasets import load_enedis_dataset


class TestEnedis(ExtTestCase):

    def test_enedis(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, 'temp_enedis')
        df = load_enedis_dataset(fLOG=fLOG, dest=temp)
        self.assertEqual(df.shape, (9719, 26))


if __name__ == "__main__":
    unittest.main()
