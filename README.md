<p align="center"><h1>pythonAI</h1></p>

Voici mon prototype de générateur de réseaux neuronaux (et à terme d'Intelligence Artificielle) en python basé sur mon précédent projet en Javascript.

## Contenu:
* Serveur (Server.py)
* Reseau neuronal (Prototype.py)
* Client (./client)

### A faire (au 06/04/2018):
- [ ] Finir le client pour gérer et permettre le test des réseaux neuronaux
- [ ] Gérer la relation des mots clés et neurones d'entrées directement sur le serveur
- [ ] Finir la gestion des requetes CRUD sur le serveur
- [ ] Connecter le serveur et le client
- [ ] Ameliorer le système en permettant de connecter plusieurs réseaux entre eux

#### Technologies utilisées:
1. Python 2.7
2. Flask pour python
3. Ionic et Cordova pour le client

# Comment utiliser ?
A partir du fichier Prototype.py uniquement pour le moment, il est possible de créer, entrainer et tester un réseau neuronal à partir d'entrées et de sorties décidées par l'utilisateur.

1. Créer un reseau (exemple):

```python
network = Network(3, ["chien", "chat", "humain"])
#Ici on a créé un reseau avec 3 entrées possibles et trois sorties possibles ayant pour nom attribué respectivement "chien", "chat" et "humain"
#Chaque entrée represente une donnée numérique, un entier, qui correspond à une représentation numérique d'un attribut de ces résultats
#Par exemple l'entrée 1 representerait le nombre de pattes/jambes
#L'entrée 2 si oui (1) ou non (0) le resultat a une fourrure
#L'entrée 3 le nombre de souris mangées par cet animal
#Ce sont des representation imaginaire, purement théoriques afin de servir l'exemple
```

2. Nourrir le reseau (exemple):

Il faudra d'abord créer des données sous la forme:
```python
exemple1 = [[valeurEntree1, valeurEntree2, valeurEntree3], indexDeLaSortieAttendue]
# Ici il y a un echantillon test avec les valeurs pour chaque entrée et la sortie attendue
exemple2 = [[valeurEntree1, valeurEntree2, valeurEntree3], indexDeLaSortieAttendue]
exemple3 = [[valeurEntree1, valeurEntree2, valeurEntree3], indexDeLaSortieAttendue]
# Dans l'exemple on crée trois echantillons hypotethiques
totalDesEchantillons = [exemple1, exemple2, exemple3]
# Et on range chaque echantillon dans un array qui servira à nourrir le reseau neuronal
```
En se basant sur notre exemple de réseau présenté plus haut cela pourrait donner ceci:
```python
exemple1 = [[4, 1, 0], 0]
#4 pattes, fourrure et pas de souris pour chien
exemple2 = [[4, 1, 5], 1]
#4 pattes, fourrure, et 5 souris mangées pour chat
exemple3 = [[2, 0, 0], 2]
#2 jambes, pas de fourrure, pas de souris pour l'humain
total = [exemple1, exemple2, exemple3]
```

Le reseau n'a plus qu'à etre nourri via une de ses methodes
```python
network.train(total)
```

3. Tester le reseau:

Une fois que le reseau est entrainé il ne reste plus qu'à le tester pour vérifier s'il a bien été entrainé.
Pour cela il suffira de lui fournir des valeurs d'entrée correspondantes comme arguments à sa methode de test.
Dans cet exemple donc:
```python
network.test([4, 1, 5])
network.test([4, 1, 0])
network.test([2, 0, 0])
```
Et la console devrait afficher à la fois les resultats numeriques mais ausssi la forme textuelle de ce resultat (ici "chat", "chien" et "humain")
