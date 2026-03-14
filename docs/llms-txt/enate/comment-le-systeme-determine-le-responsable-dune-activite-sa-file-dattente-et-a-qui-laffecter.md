# Source: https://docs.enate.net/enate-help/francais/annexe/comment-le-systeme-determine-le-responsable-dune-activite-sa-file-dattente-et-a-qui-laffecter.md

# Comment le système détermine le responsable d’une activité, sa file d’attente et à qui l’affecter

Dans le cadre de la gestion des Tickets, des Cas et des Actions dans vos flux de travail sur Enate, le système évalue régulièrement à qui le travail est affecté, qui en est le Responsable et à quelle File d'attente l’activité est liée. Des ensembles détaillés de règles sont suivis, dans l'ordre, pour déterminer ces paramètres.

Avant d’examiner ces règles détaillées, il est important de comprendre le modèle de niveau supérieur de la façon dont ces affectations d’activité sont évaluées, et quand elles le sont :

1. [Pour commencer, nous déterminons QUAND de telles réévaluations ont lieu](#determiner-quand-des-reevaluations-doivent-etre-realisees). En général, cela se produit lorsque quelque chose change dans la fiche « Statut » d’une activité.
2. Lorsque le système détermine qu'il doit procéder à une telle évaluation, nous utilisons d'abord le statut/la situation de l’activité pour [déterminer quelles valeurs doivent être définies pour l’utilisateur à qui l’activité est affectée, son Responsable et sa File d’attente, et quelles valeurs doivent être complètement effacées](#determiner-si-la-valeur-pour-lutilisateur-a-qui-lactivite-est-affectee-le-responsable-de-lactivite-e).
3. [Pour celles qui doivent être paramétrées](#comment-la-valeur-pour-lutilisateur-a-qui-lactivite-est-affectee-son-responsable-et-sa-file-dattente) :

   a. Si une File d’attente doit être définie, il suffit de sélectionner la File d'attente référencée dans la règle d’affectation (il n’y a que deux types de règles d'affectation à suivre pour les Files d’attente).

   b. Pour l’utilisateur à qui l’activité est affectée et son Responsable, il y a plus de détails à prendre en compte : nous devons appliquer une série de règles, dans l’ordre, pour ces paramètres, et nous arrêter lorsque la règle est respectée et qu’une cible valide\* est sélectionnée.

\*[Contrôle de validité](#controles-de-validite) : dans le cadre de la vérification de la règle d’affectation de l’utilisateur à qui l’activité est affectée et de son Responsable, nous devons déterminer si la cible est valide (elle doit respecter un certain nombre de règles de contrôle de validité). Si ce n’est pas le cas, nous continuons à appliquer les règles du point 3 jusqu’à ce que nous trouvions une cible valide.

Maintenant que le modèle de niveau supérieur en vigueur a été décrit, nous pouvons examiner chaque ensemble de règles appliqué pour les points 1 à 3 ci-dessus, ainsi que pour les contrôles de validité des cibles.

## Déterminer QUAND des réévaluations doivent être réalisées

Le système réévalue l’utilisateur à qui l’activité a été affectée, son Responsable et sa File d’attente chaque fois que les informations de la fiche Statut sont modifiées, notamment :

* les modifications du statut
* les modifications du type d’attente
* les modifications de la date de suivi
* les modifications de la date pour le statut « En attente de plus d'informations jusqu’à »
* les modifications de l’option « En attente de » (uniquement pour les Cas)
* les modifications du contexte du Ticket
* les modifications de la catégorie du Ticket
* les modifications du statut « En cours d’examen par les associés »
* Nouvelles informations reçues pour l’activité
* Un cas rencontre un problème

## Déterminer si la valeur pour l’utilisateur à qui l’activité est affectée, le Responsable de l’activité et sa File d’attente doivent être définies ou effacées

Lorsque le système détermine qu’il doit procéder à une telle évaluation, nous utilisons d’abord le STATUT de l’activité pour déterminer quelles valeurs doivent être définies pour l’utilisateur à qui l’activité est affectée, son Responsable et sa File d’attente, et quelles valeurs doivent être complètement effacées. Vous pouvez voir ces informations dans le tableau ci-dessous :

| **Statut/Situation de l’activité**               | **Utilisateur à qui l’activité est affectée** | **Responsable**    | **File d’attente** |
| ------------------------------------------------ | --------------------------------------------- | ------------------ | ------------------ |
| Fermé                                            | Effacer la valeur                             | Effacer la valeur  | Effacer la valeur  |
| Brouillon                                        | Définir une valeur                            | Effacer la valeur  | Effacer la valeur  |
| Nouvelles informations reçues                    | Définir une valeur                            | Effacer la valeur  | Définir une valeur |
| Attention requise (uniquement pour les Cas)      | Définir une valeur                            | Effacer la valeur  | Définir une valeur |
| À faire ou En cours pour une Action ou un Ticket | Définir une valeur                            | Effacer la valeur  | Définir une valeur |
| À faire ou En cours pour un Cas                  | Effacer la valeur                             | Définir une valeur | Effacer la valeur  |
| Résolu ou En attente                             | Effacer la valeur                             | Définir une valeur | Effacer la valeur  |

## Comment la valeur pour l’utilisateur à qui l’activité est affectée, son Responsable et sa File d’attente sont-elles définies ?

* **Files d’attente :** si une File d’attente doit être définie, la méthode [configurée d'affectation des Files d'attente](https://docs.enate.net/enate-help/builder/builder-2021.1/shared-standardised-settings-flavours/allocation-flavours#setting-a-queue-method) est simplement exécutée.
* **Utilisateur à qui l’activité est affectée et Responsable :** si l’utilisateur à qui l’activité est affectée et son Responsable doivent être définis, la procédure est plus détaillée. Nous devons appliquer une série de règles, dans l’ordre, pour ces paramètres, et nous arrêter lorsque la règle est respectée et qu’une cible valide est sélectionnée.

Avant d'appliquer la liste des règles, un contrôle de niveau supérieur est effectué : si une valeur est actuellement définie pour l’utilisateur à qui l’activité est affectée ou le Responsable, **ne la changez pas à moins que la catégorie du Ticket n’ait été modifiée**.

Autrement, appliquez les règles suivantes, dans l’ordre, en vous arrêtant lorsqu’une cible valide est identifiée :

1. Si l’option « Maintenir avec moi » a été sélectionnée pour une activité, la valeur pour l’utilisateur à qui l’activité est affectée ou le Responsable est définie comme étant l’utilisateur qui a sélectionné « Maintenir avec moi ». Si ce n’est pas le cas ou si l’utilisateur en question n’est pas valide, alors
2. Si la valeur du Responsable n’est pas nulle, définissez également la valeur de l’utilisateur à qui l’activité est affectée. Si ce n’est pas le cas ou si l’utilisateur en question n’est pas valide, alors
3. Si l’activité est un ticket, que la catégorie du ticket a changé et que le type d’attente a changé ou que le statut est résolu, la valeur pour l’utilisateur à qui l’activité est affectée ou le Responsable est définie comme étant l’utilisateur en train de modifier le ticket. Si ce n’est pas le cas, alors
4. Si l’activité n'est pas un Ticket OU si l’activité est un Ticket (dont la Catégorie de Ticket n’a pas changé ET que nous avons plus de deux lignes d’historique de statut, c’est-à-dire qu’il n'est pas dans son premier statut non brouillon), alors :
   1. Attribuez la valeur de l’utilisateur à qui l’activité est affectée ou du Responsable au dernier utilisateur/robot à avoir modifié l'activité. Si personne ou si l’utilisateur en question n’est pas valide, alors
   2. Attribuez la valeur de l’utilisateur à qui l’activité est affectée ou du Responsable à l’utilisateur/robot dans l’ordre décroissant du moment où ils ont été affectés. Si personne ou si l’utilisateur en question n’est pas valide, alors&#x20;
   3. Si l’Action a été créée par le Flux de travail (c.-à-d. pas manuellement ad hoc), alors attribuez la valeur de l’utilisateur à qui l’activité est affectée ou du Responsable au dernier utilisateur/robot à avoir travaillé sur la même Action précédemment terminée dans le Cas (ou à avoir réalisé un Examen par les associés si l’Action est En cours d’examen par les associés) Si personne ou si l’utilisateur en question n’est pas valide, alors&#x20;
5. Appliquez la [règle d’affectation](https://docs.enate.net/enate-help/builder/builder-2021.1/shared-standardised-settings-flavours/allocation-flavours) pour cette activité :       &#x20;
   1. Si la première affectation de type push est configurée pour un utilisateur spécifique, attribuez la valeur de l’utilisateur à qui l’activité est affectée ou du Responsable. Si personne ou si l’utilisateur en question n’est pas valide, alors&#x20;
   2. Si la deuxième affectation de type push est configurée pour un utilisateur spécifique, attribuez la valeur de l’utilisateur à qui l’activité est affectée ou du Responsable. Si personne ou si l’utilisateur en question n’est pas valide, alors&#x20;
   3. Si la première affectation de type push est configurée pour une Position, attribuez la valeur de l’utilisateur à qui l’activité est affectée ou du Responsable à l’utilisateur avec cette position ayant le moins d’activités dans sa boîte de réception. Si personne ou si l’utilisateur en question n’est pas valide, alors&#x20;
   4. Si la deuxième affectation de type push est configurée pour une Position, attribuez la valeur de l’utilisateur à qui l’activité est affectée ou du Responsable à l’utilisateur avec cette position ayant le moins d’activités dans sa boîte de réception. Si personne ou si l’utilisateur en question n’est pas valide, alors&#x20;
6. Si l’activité est un Cas, attribuez la valeur de l’utilisateur à qui l’activité est affectée ou du Responsable à l’utilisateur/robot qui a créé le Cas.&#x20;

## Contrôles de validité

Dans le cadre de la vérification de la règle d’affectation de l’utilisateur à qui l’activité est affectée ou du Responsable nous devons déterminer si la cible est valide. Pour être valide, elle doit satisfaire à un certain nombre de contrôles de validité. Si ce n'est pas le cas, nous devons continuer à appliquer les règles d’affectation de l’utilisateur à qui l’activité est affectée ou du Responsable jusqu’à ce qu'une cible valide soit trouvée. Les contrôles de validité réalisés sont :

* Si l’utilisateur/le robot n’est pas autorisé à travailler sur des activités de ce type (c'est-à-dire en direct/en test), bloquez l’affectation
* Si l’utilisateur/le robot est mis hors service, bloquez l’affectation
* Si l’utilisateur ne dispose pas des autorisations, bloquez l’affectation (pas de vérification des autorisations pour les robots)
* Si le robot est suspendu, bloquez l’affectation
* Si le robot a exécuté l’action *Obtenir plus de travail* plus de trois fois pour cette activité, bloquez l’affectation
* Si l’utilisateur sélectionné est un robot et que l’activité est une Action en cours d’Examen par les associés, bloquez l’affectation (les robots ne peuvent pas réaliser d’Examen par les associés)
* Si l’utilisateur sélectionné est un robot, que l’activité est une Action et qu’aucune ferme robotisée n'est configurée pour cette Action, bloquez l’affectation
* Si l’utilisateur sélectionné est un robot, que l’activité est une Action et que le robot ne fait pas partie de la ferme robotisée configurée pour l’Action, bloquez l’affectation
* Si l’utilisateur sélectionné est un robot, que l’activité est un Cas, bloquez l’affectation (les robots ne peuvent pas être affectés à des Cas)
* Si l’activité est un manuel avec une Action d’Examen par les associés qui est à l’étape de l’Examen par les associés et que l’utilisateur a effectué une ou plusieurs modifications pendant qu’il se trouvait à l'étape de la réalisation, bloquez l’affectation (les utilisateurs ne peuvent pas réaliser un Examen par les associés de leur propre travail)
* Si l’activité est un manuel avec une Action d’Examen par les associés qui est à l’étape de la réalisation et que l’utilisateur a effectué une ou plusieurs modifications pendant qu’il se trouvait à l'étape de l’Examen par les associés, bloquez l’affectation (les utilisateurs ne peuvent pas travailler sur une activité pour laquelle ils ont réalisé un Examen par les associés)
