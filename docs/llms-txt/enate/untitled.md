# Source: https://docs.enate.net/enate-help/francais/traitement-dune-action-1/untitled.md

# Actions intégrées ABBYY FlexiCapture

Enate  vous permet d’intégrer [ABBYY FlexiCapture ](https://www.abbyy.com/flexicapture/)grâce à  l’action intégrée ABBYY FlexiCapture (cliquez [ici](https://media.enate.net/Integrations/OCR/EnateABBYYFlexiCapture.mp4) pour regarder comment  créer et configurer ce nouveau type d'Action).

Lorsque cette Action s’applique à un Cas, les documents joints au Cas peuvent être envoyés à ABBYY FlexiCapture pour être scannés par ROC et les fichiers de sortie traités seront renvoyés et automatiquement joints au Cas.

{% hint style="info" %}
Note : Seuls les fichiers pris en charge par ABBYY v12 et ultérieurs peuvent être soumis. Cliquez sur le [lien suivant](https://help.abbyy.com/fr-fr/flexicapture/12/standalone_operator/input_formats/) pour consulter la liste des formats pris en charge par ABBYY.
{% endhint %}

Le système affichera ce message en attendant que vous soumettiez le(s) document(s) au moteur ABBYY FlexiCapture pour traitement :

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2F7AVoC1q5i1HJsv8yu44e%2Fimage.png?alt=media\&token=dd2fb10c-7d1e-47a7-b6b5-f637408257b1)

Vous verrez la confirmation du moment où les documents ont été soumis avec succès à ABBYY pour traitement :

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FQpam6AcNFt2LiW1wbP88%2Fimage.png?alt=media\&token=92c46e01-036a-44a1-bf9b-5909062088df)

Dernière tentative indique quand le(s) document(s) a/ont été envoyé(s) au moteur ABBYY FlexiCapture pour traitement.

Si le format des documents envoyés n’était pas valide ou si le système rencontre un problème avec la mise en forme du document, le message suivant s’affichera :

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2F2tGoi1DYBlloynMEGhI4%2Fimage.png?alt=media\&token=286a9697-cffe-4e87-bcdf-44d5f53f8daf)

### **Nouvelles tentatives automatiques**

Si un problème est survenu lors de l’envoi du document, le système réessaiera automatiquement de l’envoyer un certain nombre de fois, en fonction de la configuration de votre système dans Builder (voir [ici ](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#automated-failure-retry-pattern)pour plus d'informations).

Si le problème persiste après les tentatives automatiques (par exemple, si le paramètre de tentatives est défini sur 5 et que le système ne parvient pas à établir une connexion après 5 tentatives automatiques), le statut de l’Action ABBYY sera changé en « Fermé ».

{% hint style="info" %}
*Si* l’Action ne parvient pas à établir une connexion avec le système externe, le propriétaire du cas en sera informé et l’Action sera marquée comme étant Fermée – Inachevée dans la section Action de l’écran des Cas.
{% endhint %}

## Validation

Après avoir numérisé un document, ABBYY génère une note en fonction de son degré de confiance dans la qualité de la numérisation. Si la note de confiance est supérieure au seuil défini alors aucune vérification n’est nécessaire et il traitera les données et finira la tâche. Si la note de confiance est inférieure à un certain seuil, une vérification par une personne est nécessaire.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWskNwXafCKXzHPD007%2F-MWslty_G4gksJ22CFBo%2Fimage.png?alt=media\&token=8e051fb0-72bd-4144-802f-29c87bc62933)

### Aucune vérification requise <a href="#no-verification-required" id="no-verification-required"></a>

Un message d’état confirme que la validation par une personne n'est pas nécessaire :

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWskNwXafCKXzHPD007%2F-MWsm0__59qGFBexYyWZ%2Fimage.png?alt=media\&token=a49da588-38c2-4784-b771-a144ada2ec54)

Une fois le traitement terminé, l’Action ABBYY se ferme. Les fichiers exportés seront joints au Cas et seront visibles dans la Fiche des fichiers.

{% hint style="info" %}
Remarque : si l’option « Étiquettes de fichier de sortie » a été définie, ABBYY appliquera l’étiquette de sortie à tous les fichiers traités, prêts à être utilisés dans des activités en aval.
{% endhint %}

### Vérification humaine requise

Le système vous avertira si une vérification par une personne est nécessaire :

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FUyOhvojftkQJKK5FYsJM%2Fimage.png?alt=media\&token=a5d56f4c-a87d-4ace-bf65-443889d8859a)

De plus, un texte de rappel s’affichera à côté du statut de l’Action pour réaffirmer que la vérification manuelle doit être effectuée dans ABBYY avant de continuer.

En cliquant sur le bouton « Vérifier », vous accédez à la station de vérification ABBYY où vous pouvez vérifier  les numérisations des documents et ajuster les informations si nécessaire.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWskNwXafCKXzHPD007%2F-MWsuykc2DFaOX6-GsPY%2Fimage.png?alt=media\&token=27953730-e342-4885-9206-fae88572b769)

{% hint style="info" %}
Note : Un compte ABBYY FlexiCapture valide avec les autorisations correspondantes pour effectuer la vérification dans le projet choisi sera nécessaire pour un accès complet.
{% endhint %}

Une fois que connecté, l’écran de la station de vérification d'ABBY FlexiCapture s'affiche et vous pouvez examiner et ajuster les informations si nécessaire.

La station de vérification est composée de trois sections :

1. Les différentes pages du document à numériser.
2. Un gros plan du document original à numériser.
3. Le résultat obtenu - donc la version numérisée du document original.

Le texte surligné en jaune dans l'onglet du document original correspond aux données qu'ABBYY ne peut pas lire. Il est mis en évidence en rouge dans le résultat obtenu.

Certains caractères comme « i » peuvent également être mis en évidence dans la section Résultat obtenu si ABBYY n'est pas sûr de la copie numérisée.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWskNwXafCKXzHPD007%2F-MWsx6MLiLXtXFAmC00W%2Fimage.png?alt=media\&token=adebd784-bdf7-4f4c-b696-4832e40c4ec2)

Une fois que vous avez terminé la vérification manuelle, l’écran confirmera que cela a été fait mais notera qu’une intervention manuelle a été nécessaire :

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWskNwXafCKXzHPD007%2F-MWsx95C9X78E90Y1xnJ%2Fimage.png?alt=media\&token=a8a3caa8-f99e-46d1-8e4a-711769917f69)

Une fois le traitement terminé, les fichiers exportés seront joints au Cas et seront visibles dans la Fiche des fichiers.

Vous pouvez alors marquer l'Action comme terminée.

{% hint style="info" %}
Remarque : si l’option ‘Étiquettes de fichier de sortie’ a été définie, ABBYY appliquera l’étiquette de sortie à tous les fichiers traités, prêts à être utilisés dans des activités en aval.
{% endhint %}
