# Source: https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/managing-your-project-as-developer.md

# Managing your project as a developer

This page explains various procedures you can perform on your project without being a project admin.

### Connecting your project to SonarQube for IDE <a href="#connecting-to-sonarlint" id="connecting-to-sonarlint"></a>

[SonarQube for IDE](https://www.sonarsource.com/products/sonarlint/) is a free IDE extension that integrates with SonarQube Cloud using connected mode. This way, SonarQube for IDE can catch issues immediately, right in the IDE, before you even commit them.

Check the SonarQube for IDE documentation for the details about setting up Connected Mode:

* [Connected mode](https://docs.sonarsource.com/sonarqube-for-intellij/connect-your-ide/connected-mode) for SonarQube for IntelliJ
* [Connected mode](https://docs.sonarsource.com/sonarqube-for-visual-studio/connect-your-ide/connected-mode) for SonarQube for Visual Studio
* [Connected mode](https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/connected-mode) for SonarQube for VS Code
* [Connected mode](https://docs.sonarsource.com/sonarqube-for-eclipse/connect-your-ide/connected-mode) for SonarQube for Eclipse

### Generating a token for your project analysis <a href="#generating-token" id="generating-token"></a>

From the Team plan, see [scoped-organization-tokens](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/scoped-organization-tokens "mention").

With the Free plan, see[managing-tokens](https://docs.sonarsource.com/sonarqube-cloud/managing-your-account/managing-tokens "mention").

### Subscribing to notifications on project events <a href="#subscribing-to-notifications" id="subscribing-to-notifications"></a>

You can choose to receive email notifications when specific events occur in your project. See [notifications](https://docs.sonarsource.com/sonarqube-cloud/managing-your-account/notifications "mention").

### Marking a project as favorite <a href="#mark-as-favorite" id="mark-as-favorite"></a>

Favorite projects are displayed on **My projects** page.

{% hint style="info" %}
When you create a project, it’s automatically marked as favorite.
{% endhint %}

To mark a project as a favorite:

1. Retrieve the project. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/retrieving-projects "mention") for more information.
2. In the top of the left-side panel, select the star icon.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-a82dbaa0910d76a7113a740865de89071f00af09%2Ff88623a1a63615655872219dd926eda11f06f9dc.png?alt=media" alt="SonarQube Cloud provides an easy way to mark your favorite projects. From the Project&#x27;s Overview page, select the star in the upper left corner." width="375"><figcaption></figcaption></figure></div>

Alternatively, you can select or unselect the star in a list of projects as illustrated below.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-5832cf5ef7e9592418881f2e56374afbf5db0104%2F2dda544be80ab9d31e787b9fc3c4568d09bcedc9.png?alt=media" alt="SonarQube Cloud also lets you mark your favorite projects from the My Projects page. Simply select the start next to the project name."><figcaption></figcaption></figure></div>

### Using a project badge <a href="#using-project-badge" id="using-project-badge"></a>

If you have project access, you can include dynamic SonarQube Cloud badges on your web pages to display information about the project such as:

* The current value of specific metrics.
* The current quality gate status.
* The fact that you are using SonarQube Cloud.
* That your [ai-code-assurance](https://docs.sonarsource.com/sonarqube-cloud/ai-capabilities/ai-code-assurance "mention") has been analyzed, available for Team and Enterprise plans.

Markdown snippets and simple image URLs are provided to generate the badge code.

To generate the code of your dynamic project badge:

1. Retrieve the project. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/retrieving-projects "mention") for more information.
2. In the left navigation bar, select **Information**.
3. In the **Badges** section:
   1. Select the information type you want to display:
      * Metric value
      * Quality gate status
      * SonarQube Cloud user
   2. If you selected the metric value information type, select the metric in **Customize badge**.
   3. In Code format, select **Markdown** (markdown snippet) or **Image URL** depending on how you want to include your badge.
   4. Select the **Copy** button to copy the code of your badge.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-a757322f82228c8cddf3193c4ffa81bd3820b562%2F4d29bc7a225ed5ffcac0e766cb46b844d65373aa.png?alt=media" alt="From your SonarQube Cloud project Information page, go to the Badges section to define metrics and grab the markdown snippet that links to the correct image URL for badges to display on your website." width="545"><figcaption></figcaption></figure></div>
