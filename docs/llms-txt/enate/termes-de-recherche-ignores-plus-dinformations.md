# Source: https://docs.enate.net/enate-help/francais/annexe/termes-de-recherche-ignores-plus-dinformations.md

# Termes de recherche ignorés : plus d’informations

Parmi les fonctions sous-jacentes standards d’Enate destinées à optimiser les recherches effectuées par ses utilisateurs, certains termes couramment utilisés sont supprimés des recherches s’ils ont été saisis manuellement. Cela permet de garantir la rapidité des réponses aux résultats de recherche et d’éviter de renvoyer des volumes trop importants de résultats qualifiés qui pourraient masquer les résultats souhaités par les utilisateurs. L’une des approches utilisées à cette fin est l’utilisation de « listes de mots vides ».

## Liste de mots vides

Une liste de mots vides est une liste standard de mots communs, tels que « le », « et », « une », « des », etc., qui ne sont pas pris en compte par le moteur de recherche afin d’éviter d’obtenir trop de résultats.

Vous trouverez ci-dessous une liste complète de tous les mots vides qui ne seront pas pris en compte par TOUTES les recherches effectuées dans Enate. Cela ne concerne pas seulement les recherches effectuées avec la Recherche rapide, mais aussi les recherches d’utilisateurs, d’e-mails, d’activités comme les Tickets lorsque vous fusionnez des Tickets, etc. Si vous saisissez l’un de ces termes, il ne sera pas pris en compte dans les résultats de votre recherche.

{% file src="<https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FEKEyTzrk4RPuIRXbfM11%2FEnate%20SQL%20Stop%20List.xlsx?alt=media&token=68329945-d3a5-4dcc-8356-ed1aceee8e54>" %}

Plusieurs listes de mots vides sont prises en charge pour différentes langues.&#x20;

{% hint style="info" %}
Remarque : La liste de mots vides en anglais (britannique) est toujours utilisée lorsque vous recherchez des utilisateurs et des e-mails. Pour les activités (titre, nom de client, nom de contrat, nom de service, Cas/Ticket, nom, etc.), nous utilisons la langue de l’utilisateur connecté pour trouver la liste de mots vides pertinente. Veuillez noter que le hongrois n’est pas directement pris en charge par SQL. La liste de mots vides utilisée pour les recherches des utilisateurs hongrois est donc également la liste anglaise.
{% endhint %}

## Caractères ignorés dans la Recherche rapide

D’autres caractères spécifiques ne sont pas pris en compte lors des recherches effectuées avec la Recherche rapide, par exemple « \* », « ? », « @ », etc. Cela signifie, par exemple, que si vous recherchez “client.com” avec la Recherche rapide, seuls les mots « client » et « com » seront recherchés. Il est donc recommandé de saisir ces combinaisons de mots entre guillemets afin de les rechercher en tant que phrase spécifique. En d’autres termes, si vous saisissez « client.com », vous obtiendrez probablement les résultats que vous recherchez.

Vous trouverez ci-dessous une liste de tous les caractères qui ne seront pas pris en compte par la Recherche rapide :

{% file src="<https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FMeN4esHXN77aOS6QIpOu%2FCharacters%20ignored%20in%20Quickfind.pdf?alt=media&token=9668e40b-4ddd-4fe8-92ce-4f8c3edd7c97>" %}
