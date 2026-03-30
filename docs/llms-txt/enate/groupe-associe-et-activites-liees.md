# Source: https://docs.enate.net/enate-help/francais/travailler-avec-des-activites-liees/groupe-associe-et-activites-liees.md

# Groupe Associé et Activités Liées

## Groupe d’activités associées

Les activités associées sont un groupe d’activités étroitement liées qui, bien qu’elles se comportent selon leur propre configuration, ont un impact actif sur leur activité « parent ». En particulier, l'activité parent ne sera pas terminée tant que tous ses « enfants » ne le sont pas.

Les communications seront automatiquement partagées entre les activités du groupe associé, de sorte qu’elles seront toujours visibles, et lorsque vous répondez à un e-mail dans une activité, la réponse peut être consultée dans toutes les autres activités.

De plus, les fichiers, les liens, les défauts, les fiches et les contacts sont également automatiquement partagés entre tous les activités du groupe. Par exemple, la mise à jour d'un fichier dans une activité entraîne la mise à jour du fichier dans toutes les autres activités du groupe associé.

Les groupes d'activités associées sont :

* Un cas et ses Actions
* Un cas et son ou ses Sous-cas
* Le Ticket restant et les autres Tickets « résolus » si plusieurs Tickets ont été fusionnés
* Un Cas « enfant » et son Ticket parent si un Ticket a été converti en Cas

{% hint style="info" %}
Attention, pour les Tickets fractionnés, une capture instantanée des fichiers, des liens, des défauts, des fiches et des contacts du parent est transmise à ses Tickets enfants. Par exemple, mettre à jour un fichier dans une activité ne mettra pas à jour le fichier dans toutes les autres activités du groupe. Cependant, le Ticket parent, dont le statut est passé à « En attente », ne sera pas terminé tant que tous ses tickets « enfants » ne le sont pas. Notez également que si le Ticket parent reçoit un e-mail, il sera copié sur ses Tickets enfants plutôt que d'être partagé.
{% endhint %}

## Activités liées

Lorsque des activités n’ont pas d'impact actif l’une sur l'autre (c’est-à-dire qu’elles ne font pas partie d’un groupe d’activités associées), mais qu’il existe tout de même une légère connexion entre elles et que vous souhaitez pouvoir passer rapidement de l’une à l’autre, vous pouvez utiliser la fonctionnalité d’activités liées d’Enate.

Les activités liées se comportent selon leur propre configuration et n’ont pas besoin d'attendre la fin des autres activités pour se terminer. Vous pouvez facilement lier deux ou plusieurs activités à tout moment et il s’agit la d’un moyen très utile et flexible de connecter des activités afin que les membres de différents départements, par exemple, puissent facilement être au courant de l'évolution des activités liées au Ticket/Cas sur lequel ils travaillent.

Les communications ne seront pas non plus partagées automatiquement entre les activités liées, mais vous pouvez choisir de copier une capture instantanée des communications d’une activité vers une activité à laquelle elle est liée.

Notez que vous avez également la possibilité de partager des e-mails entre des activités liées. [Pour plus d'informations sur le partage d’e-mails entre des activités liées, cliquez ici](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/working-with-linked-work-items/sharing-emails-between-linked-work-items).

De plus, les fichiers, les liens, les défauts, les données personnalisées et les contacts ne seront pas partagés automatiquement lors de la création d'une nouvelle activité liée, mais vous pouvez choisir d’en copier une capture instantanée. Toute mise à jour de ces éléments ne sera pas répercutée sur les autres activités liées.

Les activités liées s’affichent dans [l’onglet « Activités liées »](https://docs.enate.net/enate-help/francais/travailler-avec-des-activites-liees/consulter-les-activites-liees) dans les Cas et les Tickets.

<figure><img src="https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FHiVRYRgqkRofHW6wpok1%2Fimage.png?alt=media&#x26;token=65e71fc5-d08d-4391-9b3b-8f7de9bdea4e" alt=""><figcaption></figcaption></figure>

Utiliser ce type de connexion est utile si, par exemple, la date d’échéance d’un Cas ne dépend pas de l’achèvement d’un autre travail (par exemple, par un autre département), mais il est toujours considéré utile pour les personnes travaillant sur un Cas de rester au courant de l’activité sur un autre Cas et, surtout, d’avoir un point d’accès rapide sur ce dernier.

Les activités peuvent être liées entre elles de la manière suivante :&#x20;

* Un Cas ou un Ticket créé directement à partir d’un Cas ou d'un Ticket existant.
* En ajoutant manuellement un lien d’un Cas/Ticket vers un autre Cas ou Ticket existant.
