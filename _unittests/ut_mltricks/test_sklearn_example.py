"""
@brief      test log(time=2s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG


try:
    import src
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    import src

from src.papierstat.mltricks.sklearn_example_classifier import SkCustomKnn


class TestSkCustomKnn (unittest.TestCase):

    def test_cs2(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        from sklearn import datasets
        try:
            from sklearn.model_selection import train_test_split, cross_val_score
        except ImportError as e:
            try:
                from sklearn.cross_validation import train_test_split, cross_val_score
            except ImportError as ee:
                import sklearn
                raise ImportError("Issue with sklearn %s\n%s" %
                                  (sklearn.__version__, ee)) from e
        from sklearn.neighbors import KNeighborsClassifier

        iris = datasets.load_iris()
        X = iris.data
        y = iris.target

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.33, random_state=42)

        K = 3

        # scikit
        knn1 = KNeighborsClassifier(n_neighbors=K, algorithm="brute")
        knn1.fit(X_train, y_train)
        pred = knn1.predict(X_test)
        fLOG("sklearn pred", pred[:10])
        fLOG("sklearn expe", y_test[:10])
        sc1 = knn1.score(X_train, y_train)
        fLOG("score sk", sc1)

        # custom knn
        knn2 = SkCustomKnn(k=K)
        knn2.fit(X_train, y_train)
        pred = knn2.predict(X_test)
        fLOG("custom pred", pred[:10])
        fLOG("custom expe", y_test[:10])
        sc2 = knn2.score(X_train, y_train)
        fLOG("score custom", sc2)

        self.assertGreater(sc1, 0.95)
        self.assertGreater(sc2, 0.95)

        # cross_validation
        cores1 = cross_val_score(knn1, X, y, cv=5)
        cores2 = cross_val_score(knn2, X, y, cv=5)
        fLOG(cores1)
        fLOG(cores2)
        self.assertEqual(len(cores1), 5)
        self.assertEqual(len(cores2), 5)


if __name__ == "__main__":
    unittest.main()
