# Projet : Création d’un Jumeau Numérique de Batterie pour la Supervision

## Aperçu
Dans ce projet, vous allez développer un **jumeau numérique d'un système de batterie** en utilisant Python et l’apprentissage automatique. Ce jumeau va simuler les performances et la dégradation d’une batterie au fil du temps en prédisant la **durée de vie restante (RUL - Remaining Useful Life)**. Vous travaillerez avec des données réelles, comme le nombre de cycles de charge, la température et la tension, pour entraîner votre modèle. Vous créerez aussi une **interface homme-machine (IHM)** avec **Streamlit** pour superviser le jumeau numérique et afficher les résultats en temps réel.

Pour pimenter le projet, voici quelques **bonus** que vous pouvez explorer :
1. **Utilisation d’un modèle de description standardisé** comme **AAS (Asset Administration Shell)**.
2. **Création d’une API REST** pour faciliter l’aide à la décision avec votre modèle d’apprentissage automatique.
3. **Proposition d’une IHM animée** en fonction des paramètres simulés et des résultats prédits.

Les données que vous utiliserez proviennent de la **NASA Ames Prognostics Center of Excellence (PCoE)**. Vous pouvez les trouver dans ce [fichier discharge.zip](./Design%20a%20ML%20model%20of%20a%20Battery/discharge.zip), ou depuis cette source [Li-ion Battery Aging Datasets](https://data.nasa.gov/dataset/Li-ion-Battery-Aging-Datasets/uj5r-zjdb/about_data).

## Objectifs
- **Développer un jumeau numérique** d'une batterie capable de prédire sa capacité ou durée de vie restante.
- **Implémenter une API REST** pour exposer votre modèle d'IA prédictif.
- Créer une **IHM interactive et animée** pour simuler ou superviser les performances de la batterie en temps réel.
- **Utiliser un modèle de description standardisé** (ex. : AAS) pour modéliser les données et les interactions avec le jumeau numérique.
- Apprendre à utiliser **Streamlit** pour créer un tableau de bord interactif et visualiser les données.

## Concepts Clés

1. **Dégradation des Batteries** : Au fil du temps et des cycles de charge-décharge, les batteries perdent leur capacité, réduisant ainsi leur **durée de vie utile restante (RUL)**. Vous modéliserez ce processus grâce à un modèle d'apprentissage automatique basé sur des données réelles de la NASA.

2. **Apprentissage Automatique** : En utilisant `scikit-learn` ou `TensorFlow`, vous créerez un modèle pour estimer la RUL en fonction de divers paramètres de la batterie (cycles de charge, température, tension).

3. **Modèle de Description Standardisé (AAS)** : L'**Asset Administration Shell (AAS)** est une norme qui vous aidera à structurer les informations d'un actif physique et à faciliter l'interaction entre les systèmes numériques.

4. **API REST pour l'IA** : Vous créerez une **API REST** pour permettre des appels externes à votre modèle d’IA, facilitant son intégration dans d'autres systèmes.

5. **Streamlit et Animation IHM** : Votre interface sera créée avec **Streamlit** et comprendra des **animations dynamiques** pour visualiser l'état de la batterie et la prédiction de la RUL.

## Déroulement du Projet

### 1. **Création du Modèle d'IA de Batterie**
Commencez par créer un modèle d’apprentissage automatique capable de prédire la RUL de la batterie. En utilisant les données de la NASA, vous :
- **Prétraiterez les données** : Nettoyez, structurez et divisez les données en ensembles d’entraînement et de test.
- **Entraînerez le modèle** : Utilisez Python et `scikit-learn` pour prédire combien de cycles il reste avant que la batterie ne se dégrade.
- **Évaluerez le modèle** : Mesurez la précision avec des métriques comme le Mean Squared Error (MSE).

#### Jeu de Données :
- Données provenant de la [NASA Ames Prognostics Center of Excellence](https://data.nasa.gov/dataset/Li-ion-Battery-Aging-Datasets/uj5r-zjdb/about_data).
- **Caractéristiques** : Tension, température, cycles de charge.
- **Cible** : Nombre de cycle ou Capacité de batterie

### 2. **Implémentation du Modèle de Jumeau Numérique avec AAS**
Vous modéliserez le jumeau numérique en suivant le **modèle standardisé** AAS :
- **Télécharger l'AAS** vous permettant de créer un modèle AAS et l'exposer via une API. [AASX Package Explorer](https://github.com/eclipse-aaspe/package-explorer/releases/download/v2024-06-10.alpha/aasx-package-explorer-blazorexplorer.2024-06-10.alpha.zip)
- **Structurer les données** de la batterie selon les sous-modèles définis par l'AAS.
- **Gérer les interactions** via une API REST.

### 3. **Exposition de l'API REST pour l'IA**
Créez une **API REST** avec un framework comme **Flask** ou **FastAPI** pour permettre aux utilisateurs d'interroger le modèle :
- **Envoyer des paramètres de batterie** et recevoir la prédiction de la RUL.
- **Faciliter l'intégration** dans d'autres systèmes pour l'automatisation de la décision.

### 4. **Création du Tableau de Bord avec Streamlit et Animations**
Une fois votre modèle et l'API en place, développez un tableau de bord interactif avec **Streamlit** :
- **Visualisez les paramètres actuels** de la batterie.
- **Affichez les prédictions** concernant la durée de vie restante.
- **Simulez l'état de la batterie** : en remplaçant les parametres actuels par des valeurs nouvelle à saisir (vous pouvez utiliser les sliders de streamlit) 
- **Bonus** : Animez l'IHM - Indiquez les changements de performance de la batterie avec des animations.

#### Éléments du Tableau de Bord :
1. **État de la Batterie** : Visualisation des métriques clés en temps réel.
2. **Prédiction de la Durée de Vie** : Indication de la RUL prédite.
3. **Contrôles Interactifs** : Ajustez les paramètres simulés.
4. **Graphiques Animés** : Montrez en temps réel l’évolution des paramètres et des prédictions.

### 5. **Tests et Scénarios de Simulation**
Testez votre système dans divers scénarios simulés, par exemple :
- **Simulation de l’augmentation des cycles de charge**.
- **Impact de la température sur la dégradation**.
- **Détection des alertes critiques** lorsque la RUL atteint un seuil.

## Outils et Technologies
- **Python** : Pour le traitement des données et l’apprentissage automatique.
- **scikit-learn** ou **TensorFlow** : Pour entraîner le modèle prédictif. [Scikit - Getting started](https://scikit-learn.org/stable/getting_started.html)
- **Flask** ou **FastAPI** : Pour l'API REST. [Flask - Quick start](https://flask.palletsprojects.com/en/3.0.x/quickstart/)
- **Streamlit** : Pour l'interface interactive et les animations. Voir la [documentation ici](https://docs.streamlit.io/)
- **AAS (Asset Administration Shell)** : Pour modéliser le jumeau numérique. [AASX Package Explorer](https://github.com/eclipse-aaspe/package-explorer/releases/download/v2024-06-10.alpha/aasx-package-explorer-blazorexplorer.2024-06-10.alpha.zip)
- **Jeu de Données de la NASA** : Pour entraîner et tester le modèle. [NASA Ames Prognostics Center of Excellence](https://data.nasa.gov/dataset/Li-ion-Battery-Aging-Datasets/uj5r-zjdb/about_data)

## Organisation du travail dans un groupe
- **Etudiant A** : Entraînement du modèle d’apprentissage automatique; Implémentation de l’API REST.
- **Etudiant B** : Modélisation du jumeau numérique avec AAS; Exposition du modèle par API REST.
- **Etudiant C** : Création du tableau de bord interactif avec animations en utilisant streamlit et les API des étudiants A et B.
