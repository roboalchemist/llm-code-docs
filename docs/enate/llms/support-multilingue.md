# Source: https://docs.enate.net/enate-help/francais/support-multilingue.md

# Support multilingue

Enate prend en charge les langues suivantes :

1. l'anglais
2. l'espagnol
3. le portugais (brésilien)
4. le roumain
5. l’hongrois
6. le polonais
7. le russe
8. le français
9. l’allemand

L'environnement des opérations permettant aux utilisateurs finaux de fournir le service prendra pleinement en charge plusieurs langues et chaque utilisateur sera autorisé à choisir sa langue préférée ainsi que le modèle de date et d'heure à partir du profil de l'utilisateur.

Pour définir votre langue préférée, sélectionnez une langue dans la liste déroulante des Langues dans les Paramètres de l'utilisateur.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MZCCjQMZrIXW_c-JAut%2F-MZCWE2H20vuRKMcEY_D%2FChange-Language.gif?alt=media\&token=112e24b6-1177-4eba-8d46-043d1fae0317)

L'affichage des étiquettes se fera dans la langue préférée de l'utilisateur connecté - ceci est réalisé en ajoutant un "paquet de langues" dans **Enate**. Chaque paquet de langues disposera d’une cartographie pour une langue spécifique à l'utilisateur comme le portugais, par exemple, "**Queue**" sera **Fila"** et "**Action"** sera "**Açao"** en portugais.

Voici la liste des éléments UI qui seront disponibles dans la langue préférée de l'utilisateur connecté -

| Éléments                        | Détails                                                                                                                                                                                                                         |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Page d'accueil                  | <ol><li>Filtres RAG</li><li>Mon équipe</li><li>Ensemble de bots</li><li>File d’attente</li><li>Graphique</li><li>Paramètres des grilles et des colonnes</li></ol><p>Même comportement sur la page de la boîte de réception.</p> |
| Quickfind                       | Recherche de personnes, de communications et d'activités                                                                                                                                                                        |
| Page des files d’attente        |                                                                                                                                                                                                                                 |
| Liens de navigation             | Lien vers le Builder, la page de file d'attente ou les activités récemment consultées, etc.                                                                                                                                     |
| Page de profil de l'utilisateur | Ici, l'utilisateur peut également définir sa langue préférée ainsi que le modèle de date et d'heure.                                                                                                                            |
| Page de traitement des appels   | Cette page présente toutes les communications et les activités des utilisateurs individuels                                                                                                                                     |
| Activité UI                     | Étiquettes et boutons comme Sélecteur de catégorie, État, etc.                                                                                                                                                                  |

{% hint style="info" %}
Note - Les vrais noms tels que les noms de clients et les noms d'utilisateurs resteront dans la langue d'origine tels qu'ils ont été saisie par les configurateurs dans Builder.
{% endhint %}

## Données saisies par les utilisateurs finaux de Work Manager <a href="#donnees-saisies-par-les-utilisateurs-finaux-de-work-manager" id="donnees-saisies-par-les-utilisateurs-finaux-de-work-manager"></a>

Enate prendra pleinement en charge la langue préférée de l'utilisateur dans l'affichage de Work Manager et les éléments de l'interface utilisateur, y compris les étiquettes, les liens et les boutons. Toutefois, tout ce que l'utilisateur ajoute restera dans la même langue que celle dans laquelle il l'a saisie à l'origine et ne sera pas traduit automatiquement dans une autre langue lorsqu'il sera consulté par d'autres utilisateurs ayant une langue préférée différente.

Voici la liste complète des éléments qui seront pilotés par les entrées de l'utilisateur et qui NE SERONT **PAS** traduits automatiquement par le produit.

| Éléments               | Détails                                                                                                                                                                                                                                                                                                                          |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cas                    | <p></p><ol><li>Notes</li><li>Courriels</li><li>Cas - brève description/titre</li><li>Annuler l'action Instruction d'une nouvelle action lancée par l'utilisateur final</li></ol>                                                                                                                                                 |
| Action                 | <p></p><ol><li>Notes</li><li>Courriels</li><li>Commentaires de la liste de contrôle</li><li>État de l'action - Texte du motif "Impossible à finir".</li><li>Annuler l'action Instruction d'une nouvelle action lancée par l'utilisateur final</li><li>Note d’examen par l’Associé de l'action saisie par l'évaluateur.</li></ol> |
| Ticket                 | <p></p><ol><li>Titre et description des nouveaux tickets pour enfants</li><li>Nom de la nouvelle action lancée par l'utilisateur</li><li>Nom du nouveau Cas lancé par l'utilisateur</li></ol>                                                                                                                                    |
| Contact                | Informations sur le contact comme l'adresse.                                                                                                                                                                                                                                                                                     |
| Fichiers               | Nom du fichier et note sur le fichier                                                                                                                                                                                                                                                                                            |
| Défaut                 | Description du défaut                                                                                                                                                                                                                                                                                                            |
| Notes de réaffectation | Texte saisi par l'utilisateur lors de la réaffectation d'un travail à un autre coéquipier.                                                                                                                                                                                                                                       |

### Données et cartes personnalisées <a href="#donnees-et-cartes-personnalisees" id="donnees-et-cartes-personnalisees"></a>

La version initiale de la fonctionnalité multilingue ne prendra pas en charge les configurateurs définissant plusieurs langues lors de la création de données personnalisées et de cartes intelligentes dans Builder. Pour ce faire, il faudrait disposer de plusieurs cartes et éléments de données.

### Dans les notifications d'application <a href="#dans-les-notifications-dapplication" id="dans-les-notifications-dapplication"></a>

La version initiale de la fonctionnalité multilingue ne prendra pas en charge la notification dans une langue autre que l'anglais.&#x20;
