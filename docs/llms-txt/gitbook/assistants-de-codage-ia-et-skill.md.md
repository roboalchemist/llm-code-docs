# Source: https://gitbook.com/docs/documentation/fr/creating-content/assistants-de-codage-ia-et-skill.md.md

# Assistants de codage IA et skill.md

GitBook fournit un [skill.md](https://gitbook.com/docs/skill.md) fichier qui apprend aux assistants de codage IA comment modifier correctement la documentation GitBook. Utilisez-le comme « règles du projet » lors de l’édition des docs GitBook localement. Cela s’accorde bien avec [Git Sync ](https://gitbook.com/docs/documentation/fr/getting-started/git-sync)les flux de travail où vous modifiez vos docs localement puis validez vos changements pour mettre à jour votre site de documentation. Le fichier de référence couvre les extensions Markdown de GitBook, les blocs personnalisés, les fichiers de configuration et les bonnes pratiques.

{% hint style="info" %}
GitBook propose également [GitBook Agent](https://gitbook.com/docs/documentation/fr/agent-gitbook) pour une documentation assistée par IA directement depuis votre éditeur. Ce guide s’adresse aux équipes qui préfèrent utiliser des assistants de codage externes comme Claude Code ou Cursor.
{% endhint %}

### Ce que contient le fichier skill.md

* Référence syntaxique complète pour tous les blocs personnalisés
* Formats de fichiers de configuration (`.gitbook.yaml`, `SUMMARY.md`, `.gitbook/vars.yaml`)
* Options de frontmatter et contrôles de mise en page
* Syntaxe des variables et des expressions
* Tableaux de décision pour choisir le bon type de bloc
* Pièges courants et bonnes pratiques

Ajouter ce fichier à votre assistant de codage IA fournit les informations nécessaires sur la création, l’édition et le formatage du contenu pour vos docs GitBook. Cela signifie que l’assistant suivra des cadres établis et des bonnes pratiques pour les fonctionnalités de GitBook.

### Utiliser le skill.md via URL

La plupart des assistants de codage IA prennent en charge des instructions spécifiques au projet. Vous pouvez référencer le fichier skill dans la configuration de votre projet en fournissant l’URL du fichier skill afin que l’assistant sache comment travailler avec la syntaxe GitBook.

### Utiliser le skill.md localement

Vous pouvez aussi télécharger le fichier skill et l’inclure dans votre dépôt. Tout d’abord, téléchargez le skill.md à la racine de votre dépôt, puis référencez-le dans le fichier de règles de votre assistant de codage : `"Lire skill.md dans la racine du dépôt pour la syntaxe et les bonnes pratiques GitBook"` .&#x20;

Cette approche fonctionne hors ligne et permet des modifications spécifiques à l’équipe.&#x20;

{% hint style="warning" %}
N’oubliez pas de mettre à jour votre dépôt local avec la dernière version du fichier skill.md à mesure que GitBook ajoute de nouvelles fonctionnalités.
{% endhint %}

### Tester le contenu généré par l’IA

Il est important de toujours revoir et tester le contenu généré par les assistants IA — tant pour l’exactitude technique que pour le bon formatage.&#x20;

Lorsque vous travaillez avec des assistants IA formés sur le fichier skill, vous devriez :

* Vérifier que tous les blocs personnalisés s’affichent correctement dans GitBook
* Vérifier que tous les liens internes fonctionnent
* Confirmer que le frontmatter est un YAML valide
* Tester que les variables référencent le bon scope

{% hint style="warning" %}
**Remarque :** Les assistants IA peuvent occasionnellement générer une syntaxe incorrecte ou oublier de fermer des blocs personnalisés. Passez toujours en revue les modifications avant de les valider.
{% endhint %}

### GitBook Agent

Vous préférez travailler directement dans GitBook ? [GitBook Agent](https://gitbook.com/docs/documentation/fr/agent-gitbook/what-is-gitbook-agent) vous offre un flux de travail assisté par IA dans l’éditeur GitBook — que vous utilisiez ou non Git Sync.

L’Agent possède le contexte complet de vos docs et est déjà entraîné à utiliser les blocs et fonctionnalités de GitBook de la meilleure façon possible. L’Agent vous aide à rédiger du contenu, à effectuer des mises à jour et à optimiser vos docs pour différents cas d’utilisation, le tout depuis l’application GitBook.

<a href="../agent-gitbook" class="button primary">Découvrez GitBook Agent</a>
