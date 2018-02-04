
=======================
Devinettes et probl�mes
=======================

Cette page regroupe quelques questions et probl�mes
dont les solutions figurent dans les pages de ce site
int�ressante du point de vue d'un data scientiste.

.. contents::
    :depth: 1
    :local:

Math�matiques
=============

.. contents::
    :local:

Corr�lations non lin�aires
++++++++++++++++++++++++++

Le `coefficient de Pearson <https://en.wikipedia.org/wiki/Pearson_correlation_coefficient>`_
est sans aucun doute le coefficient de corr�lation le plus
connu. Le `coefficient de Spearman <https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient>`_
mesure la corr�lation entre deux variables � partir de leur rang.
Et si on essayait de d�finir un coefficient de corr�lation
non lin�aire ? A base d'arbre de d�cision ? Pas forc�menet sym�trique ?

D�corr�lation de variables
++++++++++++++++++++++++++

On suppose que les variables :math:`(X_1, ..., X_n)` sont
corr�l�es avec une matrice variance coveriance �gale � :math:`\Sigma`.
Comment construire des variables d�corr�l�es � partir de
:math:`(X_1, ..., X_n)` ?

p-value et intervalle de confiance
++++++++++++++++++++++++++++++++++

L'�cole anglaise a tendance � pr�f�rer les
`p-values <https://en.wikipedia.org/wiki/P-value>`_,
l'�cole fran�aise pr�f�re les
`intervalles de confiance <https://fr.wikipedia.org/wiki/Intervalle_de_confiance>`_.
Ces deux notions sont �quivalentes mais connaissez-vous le lien
qui les unit ?

M�thodologie
============

.. contents::
    :local:

Normalisation
+++++++++++++

Le code suivant pr�sente une erreur de m�thodologie
qui a souvent peu d'incidence mais qui n'en reste pas moins
probl�matique.

::

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    from sklearn.preprocessing import normalize
    X_train_norm = normalize(X_train)
    X_test_norm = normalize(X_test)

Quelle est elle ?
