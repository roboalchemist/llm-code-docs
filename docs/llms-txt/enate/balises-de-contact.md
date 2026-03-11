# Source: https://docs.enate.net/enate-help/francais/contacts/balises-de-contact.md

# Balises de contact

Les balises de contact servent à lier des contacts à des activités.

## Balises par défaut du système

Les balises de contact disponibles par défaut sont :

* **Contact principal** : la personne principale avec laquelle vous traitez pour cette requête. Il ne peut y avoir qu’un seul contact principal pour une activité. Cette balise est obligatoire pour les tickets. En fonction de la configuration du cas dans Builder, elle peut être obligatoire ou non pour les cas (si elle est définie comme obligatoire pour un type de cas, elle le sera également pour les actions de ce cas).
* **Demandeur d’origine** : la personne qui a introduit la demande originale. Il ne peut y avoir qu’un seul demandeur d’origine par activité, et cette balise est indépendante de la balise *Demandeur*. Le demandeur d’origine sera soit automatiquement défini si un contact valide a envoyé l’e-mail à l’origine de la création de l’activité, soit la première personne qui sera définie manuellement comme demandeur sera également promue au rang de demandeur d’origine. Une fois définie, la balise *Demandeur d’origine* ne peut pas être modifiée et vous ne pouvez pas supprimer le contact marqué comme Demandeur d’origine de l’activité.
* **Demandeur** : la personne qui soumet la requête. Il ne peut y avoir qu’un seul demandeur par activité. Cette balise est obligatoire pour les tickets. En fonction de la configuration du cas dans Builder, elle peut être obligatoire ou non pour les cas (si elle est définie comme obligatoire pour un type de cas, elle le sera également pour les actions de ce cas).
* **Sujet** : le sujet de l'activité (il se peut qu’elle soit différentes des deux personnes ci-dessus). Il ne peut y avoir qu’un seul sujet par activité.

Très souvent, les trois balises seront attribuées à la même personne. Si vous marquez un autre contact de l’une de ces balises par défaut du système, la balise sera supprimée du contact précédent, car il ne peut y avoir qu’une seule personne marquée d’une balise par défaut du système par activité.

Lorsque vous ajoutez manuellement le premier contact à une activité, il sera défini par défaut comme contact principal, demandeur et sujet. Vous pouvez par la suite réattribuer ces balises manuellement à d’autres utilisateurs.

* **Cc** : tout autre contact pouvant être mis en copie de toute correspondance. Si un contact n’est marqué que par la balise Cc, il sera affiché dans la section Cc distincte (masquée jusqu’à ce que l’activité ait des contacts qui ne sont marqués que par la balise Cc).

## Ajouter des balises par défaut supplémentaires à un contact

En plus des balises de contact par défaut du système (Contact principal, Sujet, Cc, Demandeur), vous pouvez ajouter une autre balise de contact par défaut à un contact pour rendre l’utilisation des balises de contact sur les activités plus rapide et plus facile.

Exemple : Si vous savez que « Jane Smith » sera toujours la courtière de toutes les activités auxquelles vous l’ajoutez en tant que contact, vous pouvez donner la balise par défaut « Courtier » à la Fiche contact de Jane afin qu’elle soit automatiquement marquée comme telle dans ses activités, plutôt que de devoir manuellement définir cette balise à chaque fois.

La liste des balises par défaut parmi lesquelles vous pouvez choisir est définie dans Builder, dans la section [Paramètres généraux >> Balises de contact](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/contact-tags).

Vous pouvez définir cette balise par défaut chaque fois que vous ajoutez un nouveau contact dans le système.

<figure><img src="https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2F5Ecz1vZTtQeP8mGluk6o%2Fimage.png?alt=media&#x26;token=21865d25-bd53-4411-b9ca-9e703f245274" alt=""><figcaption></figcaption></figure>

Vous pouvez également ajouter la balise aux contacts existants et modifier la balise par défaut définie pour un contact via la page Contacts.

L'attribut Balise par défaut peut également être modifié en bloc, c’est-à-dire que vous pouvez l’attribuer à plusieurs contacts à la fois. Il suffit de sélectionner un certain nombre de contacts dans la grille de la page Contacts et de cliquer sur Modifier pour accéder à la fenêtre contextuelle de modification en bloc.

<figure><img src="https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FNiTIZZFZx6pq0Oaw95v9%2Fimage.png?alt=media&#x26;token=009ce8ee-1d39-42bb-bcb3-822eecded309" alt=""><figcaption></figcaption></figure>

### Comportement du marquage par défaut des contacts si l’option *Autoriser plusieurs* n’est pas activée

Si une valeur de balise spécifique n’a pas été réglée sur *Autoriser plusieurs*, un seul contact dans une activité sera autorisé à avoir cette valeur. Exemple : il se peut qu'il n'y ait qu'un seul contact « Courtier » pour un Ticket. Cela a évidemment un impact sur le marquage par défaut si deux contacts avec la même balise par défaut « Doit être unique » sont ajoutés à une activité, soit manuellement soit automatiquement. Dans ce scénario, le système attribuera la balise par défaut à un seul contact (et supprimera donc la balise par défaut des autres contacts). Le système attribuera une autre balise existante au contact déjà marqué, dans l’ordre de priorité suivant.

* Contact principal
* Demandeur
* Sujet
* Cc
* Tout autre contact sur l’activité

### Remarques supplémentaires sur les incompatibilités entre les entreprises fournisseurs et les balises de contact :

* Vous ne pourrez pas ajouter une balise par défaut à un contact si l’entreprise à laquelle il est affecté est différente de celle de la balise par défaut.
* Vous ne pourrez pas soumettre un activité ayant un contact dont la balise par défaut est définie sur une entreprise fournisseur différente de celle de l’activité.

## Marquage automatique des contacts dans les activités

### Fiches de contact remplies à partir d’un e-mail initial

#### Contacts connus

Lorsqu’un e-mail est reçu d’une adresse associée à un contact qui se trouve déjà dans le système et que le contact :&#x20;

* a un paramètre de champs d’application global, ou
* a un paramètre de champs d’application local, mais appartient à la même entreprise que celle à laquelle l’activité appartiendra selon les règles de routage des e-mails.

alors ses détails sont automatiquement remplis dans la fiche des contacts lorsque le système crée l’activité, et il est automatiquement marqué comme le Contact principal et le Demandeur de l’activité. De plus, si une balise par défaut lui a été attribuée, il sera également marqué de cette balise. Notez toutefois que vous avez toujours la possibilité de modifier manuellement les balises une fois l’activité créée.

Lorsqu’un e-mail est reçu d’une adresse associée à un contact qui se trouve déjà dans le système, mais qui a un champ d’application local et qui appartient à une entreprise différente de celle à laquelle l’activité appartiendra selon les règles routage des e-mails, les détails de ce contact ne seront PAS remplis automatiquement dans la fiche des contacts lorsque l’activité sera créée par le système (et il ne pourra donc pas être marqué automatiquement pour cette activité). Notez que vous avez toujours la possibilité de modifier manuellement les balises une fois l’activité créée.

#### Contacts inconnus

*Champ d’application Global ou Global et Local par défaut*

Lorsqu’un e-mail est reçu d’une adresse inconnue et que :

* le [paramètre « Permettre la création automatique de contacts »](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#enable-automatic-contact-creation) est activé dans Builder et
* votre système a été configuré pour définir le champ d'application de vos contacts externes sur **Global**, ou **Global et Local**,

alors le contact sera créé automatiquement, aura un champ d’application Global (c’est-à-dire qu'il ne sera pas lié à une entreprise spécifique) et ses détails seront automatiquement remplis dans la fiche des contacts lorsque l’activité est créée par le système. De plus, il sera automatiquement marqué comme étant le Contact principal, le Demandeur d’origine et le Demandeur de l’activité. Comme il n’était pas encore connu du système, il n’aura pas de balise par défaut. Notez que vous avez toujours la possibilité de modifier manuellement les balises une fois l’activité créée.

*Champ d’application Local par défaut*

Lorsqu’un e-mail est reçu en provenance d’une adresse inconnue et que :

* le [paramètre «Permettre la création automatique de contacts»](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#enable-automatic-contact-creation) est activé dans Builder et
* votre système a été configuré pour définir le champ d’application de vos contacts externes sur **Local**,

alors le contact sera créé automatiquement, aura un champ d’application Local (c’est-à-dire qu’il sera lié à une entreprise spécifique) et sera créé au sein l’entreprise sous laquelle l’activité existe. Ses détails seront automatiquement ajoutés à la fiche des contacts lorsque le système créera l’activité et il sera automatiquement marqué comme Contact principal, Demandeur d’origine et Demandeur de l’activité. Comme il n’était pas encore connu du système, il n’aura pas de balise par défaut. Notez que vous avez toujours la possibilité de modifier manuellement les balises une fois l’activité créée.

*Création automatique de contacts désactivée*

Lorsqu’un e-mail est reçu en provenance d'une adresse inconnue et que *:*

* le [paramètre «Permettre la création automatique de contacts»](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#enable-automatic-contact-creation) est désactivé dans Builder,

alors l’activité sera créée sur la base des règles de routage des e-mails, mais les détails de l’expéditeur de l’e-mail ne seront PAS automatiquement ajoutés à la fiche des contacts quand l’activité sera créée par le système (et il ne pourra donc pas être marqué automatiquement pour cette activité). Notez que vous avez toujours la possibilité de modifier manuellement les balises une fois l’activité créée.

### Balises de contact remplies à partir de la page d’activité des contacts

Lorsqu’une activité est créée avec l’option *Créer une activité* de la [page Activité d’un contact](https://docs.enate.net/enate-help/francais/contacts/la-page-des-activites-de-contact), ce contact est automatiquement marqué comme Demandeur d’origine, Demandeur, Sujet et Contact principal de l’activité, et sa balise par défaut est également ajoutée (s’il en a une).
