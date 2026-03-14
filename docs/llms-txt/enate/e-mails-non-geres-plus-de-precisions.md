# Source: https://docs.enate.net/enate-help/francais/courriels/gestion-des-e-mails-non-geres/e-mails-non-geres-plus-de-precisions.md

# E-mails non gérés : plus de précisions

### Quand les e-mails apparaissent-ils dans la vue *E-mails non gérés* ?

Les e-mails apparaissent dans la vue *E-mails non traités* de votre boîte de réception sur Work Manager s’ils remplissent l’une des conditions suivantes :

1. Aucune des adresses e-mail *À* et/ou en *Cc* ne dispose d’un itinéraire d’e-mail compatible.
2. L’e-mail ne contient que des adresses en *Cci*, pas d’adresses *À* ou en *Cc*.

Consultez le tableau ci-dessous pour obtenir des informations plus détaillées sur la manière dont les e-mails reçus par Enate sont traités en fonction des combinaisons d’adresses e-mail pertinentes pour Enate qui figurent dans les champs *À*, *Cc* ou *Cci*.

| **Scénario**                                                                                                               | **Nombre d’activités créées**        | **Seront-ils affichés dans la vue&#x20;*****E-mails non traités***                                                                                                                                     |
| -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| E-mail à une seule adresse e-mail en *À* ou en *Cc*                                                                        | 1                                    | <mark style="color:red;">Non</mark>                                                                                                                                                                    |
| E-mail à deux adresses e-mail en *À* ou en *Cc*                                                                            | 2 ou plus                            | <mark style="color:red;">Non</mark>                                                                                                                                                                    |
| E-mail à une adresse e-mail en *À*, une autre en *Cc*, et une en *Cci*                                                     | 1 pour chaque adresse *À* ou en *Cc* | <mark style="color:red;">Non</mark>                                                                                                                                                                    |
| \*E-mail à une adresse e-mail en *À*, une autre en *Cci*                                                                   | 1 pour le champ *À*                  | <mark style="color:red;">Non</mark>                                                                                                                                                                    |
| E-mail uniquement à une ou plusieurs adresses en *Cci*. Champs *À* ou *Cc* vides                                           | 0                                    | <mark style="color:green;">Oui, pour la boîte de messagerie des adresses e-mail en</mark> <mark style="color:green;"></mark>*<mark style="color:green;">Cci</mark>*<mark style="color:green;">.</mark> |
| E-mail à une seule adresse e-mail qui n’est pas correctement configurée dans Enate                                         | 0                                    | <mark style="color:green;">Oui, pour l’adresse e-mail non configurée</mark>                                                                                                                            |
| E-mail à une adresse e-mail qui n’est pas correctement configurée dans Enate et à une adresse e-mail configurée dans Enate | 1 pour l’adresse e-mail configurée   | <mark style="color:red;">Non</mark>                                                                                                                                                                    |
