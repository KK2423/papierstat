# -*- coding: utf-8 -*-
"""
@brief      test log(time=2s)
"""
import unittest
from pyquickhelper.pycode import ExtTestCase
from papierstat.datasets import duration_selling
from papierstat.datasets.documentation import list_notebooks_rst_links


class TestDuration(ExtTestCase):

    def test_duration(self):

        df = duration_selling()
        self.assertEqual(list(sorted(df.columns)), [
                         'commande', 'reception', 'true_duration'])
        df["wk"] = df.commande.dt.weekday
        df["hour"] = df.commande.dt.hour
        gr = df.groupby('wk').count()
        hr = df.groupby('hour').count()
        self.assertNotIn(6, gr.index)
        self.assertNotIn(8, hr.index)
        self.assertNotIn(0, hr.index)
        self.assertNotIn(20, hr.index)
        self.assertNotIn(23, hr.index)
        self.assertGreater(df.shape[0], 1000)

        df["wk2"] = df.reception.dt.weekday
        df["hour2"] = df.reception.dt.hour
        gr2 = df.groupby('wk2').count()
        hr2 = df.groupby('hour2').count()
        self.assertNotIn(6, gr2.index)
        self.assertNotIn(8, hr2.index)
        self.assertNotIn(0, hr2.index)
        self.assertNotIn(20, hr2.index)
        self.assertNotIn(19, hr2.index)
        self.assertNotIn(23, hr2.index)

    def test_notebooks_duration(self):
        links = list_notebooks_rst_links('lectures', 'artificiel_duration')
        self.assertNotEmpty(links)


if __name__ == "__main__":
    unittest.main()
