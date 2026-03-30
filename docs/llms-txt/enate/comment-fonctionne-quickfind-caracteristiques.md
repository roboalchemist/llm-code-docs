# Source: https://docs.enate.net/enate-help/francais/quickfind/comment-fonctionne-quickfind-caracteristiques.md

# Recherche rapide : caractéristiques

Quelques explications supplémentaires sur le fonctionnement de Quickfind : Trois types de recherches différentes sont effectuées en parallèle lorsque vous saisissez des données de recherche dans Quickfind :

**1) Recherche spécifique par rapport au numéro de référence**. Cette méthode est basée sur la reconnaissance d'un format connu du numéro de référence du système pour les activités, puis sur le renvoi des résultats relatifs aux Tickets, aux Cas et aux Actions qui ont cette référence. Vous pouvez simplement taper la référence, par exemple « 40308-T » et le système la reconnaîtra comme telle. Vous n'avez pas besoin de saisir un code court principal.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FEtP46ggrgWas3dS2KCf4%2Fimage.png?alt=media\&token=96dad84f-34c6-4195-a34e-d0f1fd6b9389)

**2) Recherches dans les champs de données personnalisés**. Comme décrit ci-dessus. Le système pourra effectuer ce type de recherche lorsque vous saisirez un code court connu, par exemple « FN : ». La recherche portera sur un champ qui contient la valeur spécifique que vous entrez. Voir la note complémentaire ci- dessous sur les caractères génériques.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FZedxaQHQVpmOM8iS8iiz%2Fimage.png?alt=media\&token=f0318217-de56-4517-9369-9d0371f10775)

**3) La recherche en texte libre des Activités, des communications et des personnes** par rapport à tout ce que vous saisissez qui n’est pas conforme aux deux premiers types de données reconnues. Le système effectue une recherche en texte libre des mots individuels par rapport à divers attributs système des Activités, des communications et des personnes, par exemple le titre de l’Activité, le sujet et le corps d’un e-mail.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FXXPCr4vhbjy3mV10InCs%2Fimage.png?alt=media\&token=1378591b-59b9-4ed2-89e0-82db677a23dc)

**4) La recherche de fichiers « commence par »**. Le système utilise la logique « commence par » pour la recherche de fichiers en ajoutant un caractère générique à la FIN des textes de recherche. Cela signifie que si vous souhaitez trouver un fichier appelé « Traitement des factures.docx », rechercher « factures » ne vous permettra pas de trouver le fichier, mais rechercher de « Traitement » fonctionnera.

## Caractères génériques pour une recherche ouverte <a href="#a-caracteres-generiques-pour-une-recherche-ouverte" id="a-caracteres-generiques-pour-une-recherche-ouverte"></a>

Lors d'une recherche, le système ajoute un caractère générique à la FIN des textes de recherche mais pas au début.

Pour les recherches de données personnalisées en particulier, un exemple typique serait : rechercher « p:John Smi », ce qui permettrait de trouver des éléments contenant « John Smith » dans un champ de « personnes », tandis que rechercher « p :Smith » ne permettrait PAS de les trouver.

Pour résumer, avec les recherches de champs de données personnalisés, nous recherchons la valeur précise du champ ou les premières lettres de la valeur. Les recherches de texte libre ne fonctionnent *pas tout à fait* de la même façon puisqu'une recherche de texte libre tentera de trouver une correspondance avec chaque mot individuel dans un texte pour obtenir une correspondance plutôt que dans son ensemble.

Des caractères génériques sont également ajoutés à la fin des recherches de numéros de référence.

### **Utiliser des caractères génériques durant la saisie** <a href="#utiliser-des-caracteres-generiques-pendant-la-saisie" id="utiliser-des-caracteres-generiques-pendant-la-saisie"></a>

Lorsque vous entrez des mots-clés dans la Recherce rapide, le système effectue une recherche par caractère générique par rapport au tout dernier mot entré. Par exemple, si vous tapez dans le cadre d'une recherche de texte libre : « John return prio », le système utilisera un caractère générique pour le dernier mot et vous donnera également des résultats contenant « priority ».

Une fois que vous avez appuyé sur la barre espace, le système conclura que vous avez fini de saisir ce mot et effectuera une recherche sans caractère générique.

## Autres termes de recherche ignorés <a href="#b-autres-termes-de-recherche-ignores" id="b-autres-termes-de-recherche-ignores"></a>

Afin de préserver les performances du système, les éléments suivants sont exclus lors des recherches :

* Mots d’un à deux caractères.
* Mots de la liste d'arrêt du système. Il s'agit de mots courants tels que « et », « le », « moi », etc. qui produiraient trop de résultats. Cliquez [ici](https://docs.enate.net/enate-help/francais/annexe/termes-de-recherche-ignores-plus-dinformations#liste-de-mots-vides) pour consulter la liste complète des mots vides qui ne sont pas pris en compte lors des recherches (avec la Recherche rapide ou avec d'autres recherches).
* Les caractères spécifiques qui doivent être ignorés, par exemple « \* », « ? », « @ », etc.\
  Vous trouverez [ici ](https://docs.enate.net/enate-help/francais/annexe/termes-de-recherche-ignores-plus-dinformations#caracteres-ignores-dans-la-recherche-rapide)une liste complète des caractères ignorés. Cela signifie, par exemple, que si vous recherchez client.com, seuls les mots client et com seront recherchés. Il est recommandé de placer ces combinaisons de mots entre guillemets. « client.com » produira probablement les résultats que vous recherchez.

## **Autres éléments importants concernant** Quickfind

* Quickfind est une recherche basée sur le texte. La saisie de dates dans les chaînes de texte peut donner des résultats incohérents. Utilisez des « guillemets » lorsque cela est nécessaire pour que la recherche porte sur des chaînes de caractères entières.&#x20;
* Utilisez les curseurs de date pour rechercher des résultats dans des plages de dates spécifiques.
* Si vous recherchez plusieurs mots, la recherche utilisera la logique « ET » plutôt que « OU », c'est-à-dire que vous obtiendrez les articles contenant Pomme ET Banane ET Poire.

## **Caractéristiques des recherches sur les activités et les e-mails**

Il est important de noter que Quickfind effectue trois recherches indépendantes **:**&#x20;

* une pour les activités (Cas, Actions, Tickets)
* une pour les e-mails qui peuvent s'y rapporter
* une pour les personnes.

Ainsi, si vous effectuez une recherche sur une combinaison de trois mots, par exemple pomme, banane et poire, Quickfind affichera les résultats de toutes les activités où ces trois mots apparaissent et, séparément, tous les e-mails où ces trois mots apparaissent. Les situations dans lesquelles deux des mots apparaissent dans l’activité, et le troisième seulement dans un e-mail associé, ne seront pas trouvées par les deux recherches.

Les attributs spécifiques sur lesquels portent les recherches sur les activités sont les suivants :&#x20;

* Référence de l’activité
* Titre
* Nom du client
* Nom du fournisseur
* Nom du contrat
* Nom du service
* Nom de la ligne de service
* Nom du type de processus

Les attributs spécifiques sur lesquels portent les recherches sur communications sont les suivants :

* Titre de l’e-mail
* Corps de l’e-mail
* Adresses e-mails (De, À, Cc, Cci)
* Corps de la note interne (pour les notes ajoutées dans Enate/Libre service)
