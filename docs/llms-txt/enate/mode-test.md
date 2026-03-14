# Source: https://docs.enate.net/enate-help/francais/mode-test.md

# Mode test

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2ODI0MA==>" %}

## Passage en mode test <a href="#a-passage-en-mode-test" id="a-passage-en-mode-test"></a>

Si votre compte d'utilisateur est configuré pour vous permettre d'accéder aux données de test, vous pouvez passer votre environnement de travail en mode "Test". Ce lien est disponible dans le menu déroulant utilisateur à droite de la barre d'en-tête.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FQBqRL3WT7fZV1uRUneC0%2F16-Switching-to-Test-Mode.gif?alt=media\&token=f77301ea-53c8-4f5f-b0d3-67cd9cc351da)

## Explication du mode de test <a href="#b-explication-du-mode-de-test" id="b-explication-du-mode-de-test"></a>

Une fois que vous êtes en mode test, vous ne verrez que les données de test, ce qui vous permet de créer et d'exécuter des activités test à travers des versions de test des processus pour les vérifier avant de les mettre en service, le tout sans affecter les données de production en direct.

Comme rappel visuel, la barre d'en-tête est paramétrée sur le rouge lorsque vous êtes en mode Test.

## Définition des différents responsables et membres des files d'attente en mode test <a href="#c-definition-des-differents-responsables-et-membres-des-files-dattente-en-mode-test" id="c-definition-des-differents-responsables-et-membres-des-files-dattente-en-mode-test"></a>

La fonctionnalité du mode Test vous permet désormais de définir un responsable de file d'attente différent selon que vous êtes en mode Test ou en mode Direct.

Exemple : Prenons le cas du **Responsable 1** qui a accès au mode en direct et qui est responsable de la gestion de deux files d'attente, celle du **financement** et celle du **Cas principal**.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Mj_fPGnh7taQAqUE5Pn%2F-MjiI6oD46ANNbcunltc%2Fimage.png?alt=media\&token=39bbdd10-b826-434e-a1cc-ec957d94cd92)

En mode test, les deux mêmes files d'attente peuvent être gérées par un autre utilisateur qui a l'autorisation de chef d'équipe et de mode test - voir l'exemple ci-dessous où le **Responsable 2** a été désigné pour être responsable des files d'attente en mode test.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Mj_fPGnh7taQAqUE5Pn%2F-MjiHacbA9Wz896sZutv%2Fimage.png?alt=media\&token=bc4bbfd6-0989-4d8f-8903-1408bc9aec8b)

## Passer d'un robot à l'autre, en direct ou en test <a href="#d-passer-dun-robot-a-lautre-en-direct-ou-en-test" id="d-passer-dun-robot-a-lautre-en-direct-ou-en-test"></a>

Il est maintenant possible de changer un robot pour qu'il puisse fonctionner en mode test ou en mode réel. Plus précisément, deux nouvelles activités ont été ajoutées aux bibliothèques d'activités pour UiPath, Automation Anywhere et BluePrism (et les API standard ont été ajustées de manière à ce qu'elles puissent être appelées de manière générique) comme suit

* Régler le mode en direct
* Définir le mode de test

Ces actions vous permettent de faire basculer un robot entre l'état de test et l'état réel. Une fois qu'un robot est passé en mode Test, les appels d'activité ultérieurs que le robot peut effectuer, par exemple "Obtenir plus de travail" et "Créer un ticket/un cas, etc. Le robot doit être reparamétré en mode "Direct" une fois le processus mis en route, il faut donc s'assurer qu'il crée ensuite des activités en direct.

## Contacts/ test séparés dans le système <a href="#e-contacts-test-separes-dans-le-systeme" id="e-contacts-test-separes-dans-le-systeme"></a>

Enate prend désormais en charge la création d'enregistrements de contacts séparés en mode Test, c'est-à-dire que tout enregistrement de contact créé en mode Test ne sera accessible qu'aux utilisateurs du mode Test (et les contacts créés en mode Live ne seront accessibles qu'aux utilisateurs du mode Live).  Cela permet de s'assurer que les courriels des paquets de test ne sont pas accidentellement envoyés aux utilisateurs de la production, et vice versa.
