# Source: https://docs.enate.net/enate-help/francais/traitement-dune-action-1/actions-extraction-du-document.md

# Actions « Extraction du document »

## Aperçu

La fonction Extraction du document permet d’extraire automatiquement les données pertinentes des fichiers joints aux e-mails entrants afin qu’elles puissent être utilisées pour le traitement ultérieur de l’activité. Cela permet à vos agents de gagner du temps et d’économiser leurs efforts. Cela signifie également que les documents tels que les PDF peuvent être numérisés et utilisés à la fois pour créer des cas dans Enate et pour être intégrés dans les activités du processus en cours.

Lorsqu’une action Extraction du document est exécutée pour un cas, les documents joints au cas peuvent être soumis à la technologie de votre choix pour être numérisés, et les fichiers de sortie traités seront renvoyés et automatiquement joints au cas.

Si, à un certain moment, la technologie que vous utilisez n’est pas suffisamment sûre des résultats, en fonction d’un seuil de confiance que vous pouvez définir, Enate transfère immédiatement la tâche à un agent dans Work Manager pour qu’il puisse l’examiner et la vérifier, ce qui vous permet de bénéficier du soutien d’un « humain dans le circuit ».

Cette fonction peut être activée par votre administrateur dans la section [Marketplace ](https://docs.enate.net/enate-help/builder/builder-2021.1/integrations-marketplace)de Builder.

Regardez la vidéo ci-dessous pour en savoir plus :&#x20;

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTgwNzUwMw==>" %}

## Fonctionnement

Lorsque le cas est traité dans Work Manager, les données pertinentes des fichiers joints aux e-mails entrants sont automatiquement analysées et extraites.

Si la technologie que vous utilisez est suffisamment sûre de ses résultats d’extraction de données, cette action n’aura même pas besoin d’être examinée par un humain, elle sera simplement achevée automatiquement et le cas passera à l’action suivante. L’action d’extraction de données terminée peut toujours être examinée si vous cliquez dessus, mais il n’est pas nécessaire de la confier spécifiquement à un humain pour qu’il en contrôle le résultat.

<figure><img src="https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2F7YNGRuClAG6RgIavjivN%2Fimage.png?alt=media&#x26;token=2257f58c-f51a-4d06-b8b6-358fba103775" alt=""><figcaption></figcaption></figure>

Cependant, si la technologie d'extraction n'est pas sûre des résultats de l'extraction des données, l'Action sera transmise à un utilisateur humain lorsque vous cliquerez sur « extraire de la file d'attente » dans leur page d'accueil, afin qu'il la récupère et la vérifie. Lorsqu'un agent ouvre l'Action, vous verrez qu'elle lui a été attribuée car des contrôles supplémentaires sont nécessaires.

<figure><img src="https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FHXkWgQh9yKO5F84w5aWE%2Fimage.png?alt=media&#x26;token=37e15bfb-f3e1-4f68-9ab7-59ab979cba37" alt=""><figcaption></figcaption></figure>

Pour afficher et valider chaque document, cliquez sur l'icône pour l'ouvrir, puis faites défiler jusqu'à l'écran « station de validation » dans Action, qui affiche l'image numérisée du document et le tableau des valeurs extraites. Vous pouvez ainsi voir où les niveaux de confiance les plus faibles sont mis en évidence, les examiner et apporter les corrections nécessaires manuellement. Vous pouvez les consulter sur place ou les agrandir dans une fenêtre contextuelle pour les afficher en plein écran.

<figure><img src="https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FJovVBhP0XekkxmCsSd6a%2Fimage.png?alt=media&#x26;token=fa50604d-9bf7-474a-908e-360b8b3957d1" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Note : Un seul document peut être consulté à la fois.
{% endhint %}

<figure><img src="https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FJWmNoDtB46Evef92apwr%2Fimage.png?alt=media&#x26;token=1407b4ff-f3d5-42df-a05a-edeff7e131f1" alt=""><figcaption></figcaption></figure>

Sur cet écran de validation, l'agent pourra voir une copie numérisée du fichier, qui peut comporter plusieurs pages, ainsi que deux onglets affichant les données extraites.

* L'onglet Données extraites affiche les paires clé-valeur de l'agent pour les données extraites, ainsi que le niveau de confiance attribué par EnateAI. Les valeurs peuvent être ajustées si nécessaire et sont enregistrées lorsque l'agent clique sur le bouton « Mettre à jour » correspondant à cette valeur. Cela permet de définir la valeur de confiance à 100 % pour cette clé.
* L'onglet  Tableaux  affiche toutes les données répétitives qui ont été sélectionnées sous forme de tableau. Vous pouvez utiliser le bouton  Supprimer  pour supprimer les lignes dont vous n'avez pas besoin.

Si l'agent doit quitter l'écran de la station de validation à tout moment, il lui suffit de cliquer sur « Enregistrer comme brouillon » pour enregistrer ses modifications pour un document particulier.

{% hint style="info" %}
Note : Si un agent accède à l'écran de validation d'une action qui ne lui est pas attribuée, les données seront en mode lecture seule et ne pourront pas être modifiées. Pour pouvoir modifier les données, l'agent doit d'abord s'attribuer l'action.
{% endhint %}

Une fois qu'un agent est satisfait des données, il lui suffit de cliquer sur le bouton « Soumettre » pour envoyer les données mises à jour. EnateAI termine le traitement en arrière-plan et met à jour l'écran Action pour confirmer que le processus est terminé. Le traitement en arrière-plan permet à l'agent de passer à tout autre document nécessitant une vérification.

Une fois que vous avez cliqué sur « Soumettre » pour le dernier document à valider, l'écran Action se ferme automatiquement. Là encore, EnateAI termine le traitement en arrière-plan et marque l'Action comme Résolue après un court laps de temps, puis la déplace vers Fermer.

*Note : chaque fois que vous vérifiez et mettez à jour des éléments de données, EnateAI apprend et améliore légèrement ses suggestions d'extraction de données. Si vous remarquez que la technologie fournit régulièrement des suggestions erronées, demandez à votre équipe administrative de modifier le seuil de confiance.*
