
.. blogpost::
    :title: Automatiser des exp�riences de machine learning
    :keywords: scikit-learn, automatisation
    :date: 2018-02-16
    :categories: scikit-learn

    Prenons un exemple car le titre est assez flou.
    On souhaite apprendre deux mod�les diff�rents
    sur deux parties disjointes d'un jeu de donn�es :
    la pr�diction de la qualit� d'un vin selon qu'il est
    blanc ou rouge. Selon que le vin est blanc ou rouge,
    on n'appliquera pas le m�me mod�le. L'ensemble
    tient en quelques lignes dans un notebook mais comme
    cette id�e revient souvent, on peut �tre tent� de l'impl�menter
    une bonne fois pour toutes sous la forme d'un mod�le
    qui s'int�gre facilement avec :epkg:`scikit-learn`.
    C'est ce que propose la classe
    :class:`SkBaseLearnerCategory <papierstat.mltricks.sklearn_base_learner_category.SkBaseLearnerCategory>`.
    Ce point est abord� de fa�on plus d�taill�e :
    :ref:`l-sklearn-programmation`.
