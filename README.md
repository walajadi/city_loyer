
Pour lancer le projet:
1. docker build -t myimage  . (rajouter --platform linux/amd64  pour la puce M1)
2. docker run -d --name mycontainer -p 80:80 myimage 

Pour le dataset de prix moyen, lien de telechargement:
 - https://www.data.gouv.fr/fr/datasets/carte-des-loyers-indicateurs-de-loyers-dannonce-par-
commune-en-2018/
 - Ficher a placer dans le folder app/data.

Exemple d'appel:
 - curl  http://localhost/api/v1/villes/?dept=93&surface=40&loyer_max=700  

