# Source: https://docs.enate.net/enate-help/francais/les-differents-types-decran-des-activites/carte-des-fichiers.md

# Fiche Fichiers

## Aperçu <a href="#apercu" id="apercu"></a>

L’onglet Fichiers permet de consulter tous les fichiers et les liens qui ont été ajoutés à cette activité et aux activités qui lui sont liées, ainsi que les pièces jointes des e-mails entrants et sortants.

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTc5Nw==>" %}

Tous les fichiers/liens pour l’activité ouverte en cours sont affichés en haut de l’onglet Fichiers, et tous les fichiers/liens pour les activités liées sont affichés dans une section séparée en dessous. Les activités sont triées en fonction de la date et de l’heure auxquelles ils ont été téléchargés, les plus récentes apparaissant en premier.

Vous pouvez voir le nom du fichier, le type de fichier, sa taille, qui l’a téléchargé (et quand), ainsi que le numéro de référence et l’activité dans laquelle il a été téléchargé. Vous pouvez également voir les [balises ](#tagging-files)et les [notes](#ajouter-des-notes-aux-fichiers) qui ont été ajoutées aux fichiers.

Diverses icônes vous aident à trouver des informations supplémentaires :

* Les pièces jointes classiques sont marquées d’une icône en forme de trombone :<img src="https://2979960330-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWgljwAko09GniIfAyZrJ%2Fuploads%2FN0uCjbEkyjRegJ3fC9gS%2Fimage.png?alt=media&#x26;token=ec257baf-4cee-4f08-9ece-fb143368be1f" alt="" data-size="line">​
* Les liens sont marqués d’une icône de liens :​ ![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FleC5qQxTSpv6d12MH1tg%2Fimage.png?alt=media\&token=78410f17-951c-474a-9ad6-6abb49d0020a)
* Les pièces jointes des e-mails entrants sont marquées d’une icône verte :![](https://2979960330-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWgljwAko09GniIfAyZrJ%2Fuploads%2Ft39EccipUrtZQ6XiwJLR%2Fimage.png?alt=media\&token=dcaca8e5-ffaa-4607-be1b-4cc57c50a14f)​
* Les pièces jointes des e-mails sortants sont marquées d’une icône bleue :<img src="https://2979960330-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWgljwAko09GniIfAyZrJ%2Fuploads%2FbgYCrhQkivksvjy1nKKZ%2Fimage.png?alt=media&#x26;token=bd3891e4-cc3c-49b9-9c28-76caf2647cb1" alt="" data-size="line">​

Tous les fichiers de l’onglet Fichiers peuvent être ajoutés en tant que pièces jointes aux e-mails sortants [ajoutés en tant que pièces jointes aux e-mails sortants](https://docs.enate.net/enate-help/francais/courriels/joindre-des-fichiers-a-un-courriel), et les liens peuvent être ajoutés au corps de l’e-mail.

{% hint style="info" %}
Lorsque vous effectuez une mise à jour à partir de versions antérieures à la version 2022.3, les fichiers joints directement à une activité apparaîtront tous dans la section Autres activités sans numéro de référence. Les pièces jointes aux e-mails de cette activité apparaîtront cependant dans la section Actuel.
{% endhint %}

## Ajouter des fichiers/liens à une activité <a href="#ajouter-des-fichiers-liens-a-une-activite" id="ajouter-des-fichiers-liens-a-une-activite"></a>

Si l’activité vous est affectée, vous pouvez lui ajouter des fichiers et des liens dans l’onglet Fichiers. Plusieurs fichiers peuvent être téléchargés en même temps. Cliquez sur les liens de téléchargement en haut de l’onglet pour les télécharger.

<figure><img src="https://2979960330-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWgljwAko09GniIfAyZrJ%2Fuploads%2FDM6PiB68DAOCBFtO60tN%2Fimage.png?alt=media&#x26;token=b7711b50-9d45-46f8-96d0-1ac2a28f0648" alt=""><figcaption></figcaption></figure>

Vous pouvez également faire glisser des fichiers dans l’onglet pour les ajouter à l’activité.

{% hint style="info" %}
Remarque : la taille maximale par fichier est de 100,00 Mo.
{% endhint %}

### Restrictions des types de fichiers <a href="#tagging-files-1" id="tagging-files-1"></a>

Par défaut, tous les types de fichiers peuvent être téléchargés, mais les types de fichiers peuvent être limités en spécifiant les types acceptables dans la section [Paramètres généraux](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#allowed-file-types) de Builder.

## Marquer des fichiers et des liens <a href="#tagging-files" id="tagging-files"></a>

Des balises peuvent être ajoutées aux fichiers et aux liens. Le balisage peut être particulièrement utile pour donner plus de structure aux informations de vos fichiers et active des fonctionnalités, telles que la mise en pièce jointe automatique des fichiers avec certaines balises à des e-mails envoyés automatiquement par le système et à des réponses prédéfinies dans les e-mails que vous rédigez Il permet également aux routines d’automatisation externes de savoir quels fichiers spécifiques récupérer à partir d’une activité.

Le marquage des fichiers est également une fonctionnalité importante pour les processus qui impliquent une technologie d’automatisation.

Exemple : si une action automatisée en aval doit savoir quel fichier ajouté en pièce jointe à votre cas est le fichier de « confirmation de la facture », vous pouvez marquer les fichiers concernés comme tels et, quel que soit le nom du fichier, la technologie d’automatisation saura quels fichiers sélectionner en fonction de leur balise. Cette technologie d’automatisation externe peut également fournir des balises dans le cadre du téléchargement de documents dans des activités sur Enate, en vue d’une utilisation manuelle ou automatisée en aval.

Les titres des balises disponibles sont définis dans Builder. Si vous constatez qu’une balise spécifique n’est pas disponible, contactez votre administrateur pour qu’elle soit ajoutée.

Vous pouvez ajouter une balise à un fichier en cliquant sur le **+** et en sélectionnant une balise dans la liste qui s’affiche.

<figure><img src="https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FHinz4xVjEtWxd1KOIfrH%2Fimage.png?alt=media&#x26;token=fbee60ce-2f39-4729-bd79-3070562fc2ed" alt=""><figcaption></figcaption></figure>

Vous pouvez également ajouter des balises à plusieurs fichiers et liens à la fois en sélectionnant un ou plusieurs éléments et en utilisant l’icône qui s’affiche alors dans l’en-tête de l’onglet Fichiers.

<figure><img src="https://2979960330-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWgljwAko09GniIfAyZrJ%2Fuploads%2F0x6YMFlAFKHvSdKupUqy%2Fimage.png?alt=media&#x26;token=56a298e9-30aa-4d20-99ed-7ef02335619d" alt=""><figcaption></figcaption></figure>

Enate peut également vous aider à automatiser le balisage des pièces jointes aux e-mails. Diverses options sont disponibles dans la section [Marketplace ](https://docs.enate.net/enate-help/builder/builder-2021.1/integrations-marketplace)de Builder pour activer des composants (d’Enate ou de tiers) qui analysent le contenu des e-mails reçus, y compris la possibilité de suggérer des balises pour leurs pièces jointes en fonction de leur contenu.

Si votre administrateur a activé un composant de balisage automatique, vous verrez des informations supplémentaires dans la section de balisage des fichiers, où des suggestions automatiques de valeurs de balisage pour une pièce jointe ont été faites.

<figure><img src="https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2Fnd68rUAn8STK6qo9Hfmn%2Fimage.png?alt=media&#x26;token=c774b47e-6c8a-4c1a-a04d-b344c90a0baa" alt=""><figcaption></figcaption></figure>

Si la technologie que vous utilisez est suffisamment sûre de sa suggestion de balisage, celle-ci apparaîtra en vert. Si vous êtes d’accord avec la suggestion, vous n’avez rien à faire, mais si ce n’est pas le cas, il vous suffit de cliquer dessus pour la modifier.

<figure><img src="https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2F5cLg5sQ9zjrXiAoCyRxn%2Fimage.png?alt=media&#x26;token=69209bd9-a2a5-47e7-9a41-078ec438731e" alt=""><figcaption></figcaption></figure>

Si la technologie est moins sûre de sa suggestion de balisage, celle-ci apparaîtra en orange. Si vous êtes d’accord avec la suggestion, assurez-vous de la confirmer, mais si ce n’est pas le cas, modifiez-la selon vos préférences. Chaque fois que vous procédez de la sorte, la technologie apprend et améliore un peu plus sa capacité à suggérer des balises. Si vous remarquez que la technologie se trompe régulièrement dans ses suggestions, demandez à votre administrateur de modifier le seuil de confiance.

<figure><img src="https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2F5i6SaQUOo82PyNvwbEI2%2Fimage.png?alt=media&#x26;token=5658bc3c-5a5b-43d8-983c-fc9f7eed63dd" alt=""><figcaption></figcaption></figure>

Une fois que les balises ont été ajoutées, les fichiers/liens pourront être ajoutés automatiquement aux e-mails avec les balises correspondantes, ce qui vous permet de vous assurer que tous les documents d’un type donné sont inclus dans des e-mails spécifiques ou dans le corps de l’e-mail.

Lorsqu’un [texte de réponse prédéfini](https://docs.enate.net/enate-help/francais/courriels/textes-memorises) est inséré dans un e-mail écrit manuellement ou lorsqu’un nouvel e-mail est créé automatiquement et envoyé en cours de traitement, le système identifie toutes les balises liées au texte prédéfini ou au modèle d’e-mail et ajoute automatiquement en pièce jointe tous les fichiers de l’activité qui partagent la même balise. Les balises sont liées à la réponse prédéfinie / au contenu de l’e-mail dans le cadre de la configuration du système par les administrateurs dans Builder lors de la création des [modèles d’e-mail](https://docs.enate.net/enate-help/builder/builder-2021.1/email-template-configuration).

{% hint style="info" %}
Remarque : si les balises de fichier ne sont pas [configurées dans votre système](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/file-tags), l’option « Ajouter une balise de fichier » ne sera pas affichée.
{% endhint %}

## Ajouter des notes aux fichiers <a href="#ajouter-des-notes-aux-fichiers" id="ajouter-des-notes-aux-fichiers"></a>

Vous pouvez également ajouter des notes aux fichiers et aux liens pour donner une brève description de leur contenu ou pour fournir toute autre information qui pourrait être utile.

Vous pouvez également ajouter des notes à plusieurs fichiers et liens à la fois en sélectionnant un ou plusieurs éléments et en utilisant l’icône qui s’affiche alors dans l’en-tête de l’onglet Fichiers.

<figure><img src="https://2979960330-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWgljwAko09GniIfAyZrJ%2Fuploads%2FOlcR8BFoN8kiaqbRgc3w%2Fimage.png?alt=media&#x26;token=ce5e04ce-6e40-4a5d-a91e-bbb16a3167bb" alt=""><figcaption></figcaption></figure>

## Prévisualiser les fichiers <a href="#previsualiser-les-fichiers" id="previsualiser-les-fichiers"></a>

Le menu sur la droite vous permet de prévisualiser un fichier individuel. L’aperçu s’ouvre dans un nouvel onglet.

<figure><img src="https://2979960330-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWgljwAko09GniIfAyZrJ%2Fuploads%2FZAE2lZ9iI0B5rBvNdLs9%2Fimage.png?alt=media&#x26;token=5e4a2e80-8485-4be9-bcdc-5f48303a5253" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Si le fichier ne peut pas être prévisualisé, une bannière de confirmation apparaîtra pour l’expliquer et proposer une option de téléchargement du fichier. Les types de fichiers pris en charge pour la prévisualisation sont les suivants : **txt**, **pdf**, **jpg**, **jpeg**, **jpe**, **jif**, **jfif**, **jfi**, **png**, **gif**, **web**, **tiff**, **tif**, **heif**,**heic**, **svg**, **svgz**.
{% endhint %}

## Télécharger des fichiers <a href="#telecharger-des-fichiers" id="telecharger-des-fichiers"></a>

Vous pouvez télécharger des fichiers individuels en cliquant sur l’option correspondante dans le menu de droite.

<figure><img src="https://2979960330-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWgljwAko09GniIfAyZrJ%2Fuploads%2FU1sm128TjbXTXIoIRtJF%2Fimage.png?alt=media&#x26;token=0698a894-6b34-4256-a5b2-4b9213d1dccc" alt=""><figcaption></figcaption></figure>

Vous pouvez télécharger plusieurs fichiers à la fois en sélectionnant les fichiers que vous souhaitez télécharger et en cliquant sur l’option en haut de l’écran. Ils peuvent être téléchargés en plusieurs fichiers individuels ou en un seul fichier ZIP compressé via l’option de téléchargement ZIP ici.

<figure><img src="https://2979960330-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWgljwAko09GniIfAyZrJ%2Fuploads%2FurBEuoxVne9kNmDGHsRH%2Fimage.png?alt=media&#x26;token=1f4b9102-7530-4aa7-b563-2ccbebbc21db" alt=""><figcaption></figcaption></figure>

## **Supprimer des fichiers/liens** <a href="#supprimer-des-fichiers-liens" id="supprimer-des-fichiers-liens"></a>

Vous pouvez supprimer des fichiers ou des liens individuellement en cliquant sur le menu de droite.

<figure><img src="https://2979960330-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWgljwAko09GniIfAyZrJ%2Fuploads%2FOhx4rIvsMEOSL2qJGxEx%2Fimage.png?alt=media&#x26;token=650fde9c-dfb7-4e1c-a2aa-395172a7ae3a" alt=""><figcaption></figcaption></figure>

Vous pouvez également supprimer plusieurs fichiers/liens en sélectionnant les fichiers/liens que vous souhaitez supprimer et en sélectionnant l’option Supprimer en haut de l’écran.

<figure><img src="https://2979960330-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWgljwAko09GniIfAyZrJ%2Fuploads%2F1l3MkNjNF6qiCeR9WwqD%2Fimage.png?alt=media&#x26;token=9d7e7b5a-4125-412b-952e-3273b38543d5" alt=""><figcaption></figcaption></figure>

## Filtrer les fichiers/liens <a href="#drag-and-drop-of-attachments-into-email-section" id="drag-and-drop-of-attachments-into-email-section"></a>

Vous pouvez filtrer les fichiers et les liens affichés dans l’onglet Fichiers grâce à l’option de filtrage en haut de l’écran. Vous pouvez filtrer par : pièces jointes, pièces jointes des e-mails sortants, pièces jointes des e-mails entrants et liens.

<figure><img src="https://2979960330-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWgljwAko09GniIfAyZrJ%2Fuploads%2FCHsu2nXB7XBvGZhklM4I%2Fimage.png?alt=media&#x26;token=4cf0f348-5a6e-484d-8cce-9b236badd334" alt=""><figcaption></figcaption></figure>

### Recherche en texte libre de fichiers <a href="#recherche-en-texte-libre-de-fichiers" id="recherche-en-texte-libre-de-fichiers"></a>

Une recherche en texte libre est également disponible pour vous aider à localiser des fichiers ou des liens individuels. Vous pouvez effectuer une recherche sur la base des différents groupes de texte affichés : nom de fichier, informations sur les balises et texte des notes.

<figure><img src="https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FXwpjZHOoQPbHcunY283b%2Fimage.png?alt=media&#x26;token=8c72b253-faea-4f84-a255-14e47094b260" alt=""><figcaption></figcaption></figure>
