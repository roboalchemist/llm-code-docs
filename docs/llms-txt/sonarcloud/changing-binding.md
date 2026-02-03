# Source: https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/changing-binding.md

# Changing project binding

### Changing the binding of your project <a href="#changing-binding" id="changing-binding"></a>

You can bind a project to another repository or you can bind an unbound project to a repository. See [binding-with-dop](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/about-sonarqube-cloud-solution/ressources-structure/binding-with-dop "mention") for more information.

<details>

<summary>Binding a project to another repository</summary>

You can change the repository binding of a project provided you have Administer permission on that project and Create projects permission. The following limitations apply:

* The source and target repositories must be in the same organization.
* A public project cannot be bound to a private repository.

{% hint style="info" %}
The repository change will not impact the automatic analysis activation status of your project except if the target repository is a monorepo and automatic analysis was enabled for your project. In that case, the automatic analysis will be disabled since it’s not supported for monorepos and you will need to manually configure a CI-based analysis for your project. See [overview-of-integrated-cis](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/overview-of-integrated-cis "mention") for more details.
{% endhint %}

{% hint style="warning" %}
Changing the binding of a project configured with a CI-based analysis may require that you change the CI/CD process configuration for this project.
{% endhint %}

To bind a project to another repository:

1. Retrieve your project. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/retrieving-projects "mention") for more details.
2. Go to **Administration** > **General Settings** > **Repository binding**.
3. In the list of repositories, select the target repository and select **Save**.

</details>

<details>

<summary>Binding an unbound project to a repository</summary>

You can bind an unbound project to a repository provided you have Administer permission on that project and Create project permission. Note that a public project cannot be bound to a private repository.

{% hint style="info" %}
In case you had manually linked your project to a repository, you should remove this manual setup.
{% endhint %}

To bind an unbound project to a repository:

1. Retrieve your project. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/retrieving-projects "mention") for more details.
2. Go to **Administration** > **General Settings** > **Repository binding**.
3. In the list of repositories, select the repository and select **Save**.

{% hint style="info" %}
You may want to enable the automatic analysis on your newly bound project. To do so, see [#activating-automatic-analysis](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/automatic-analysis#activating-automatic-analysis "mention").
{% endhint %}

</details>

<details>

<summary>Updating the project binding on repository URL change</summary>

In case you renamed your repository or moved it within the same organization, you can update the repository binding to your SonarQube Cloud project as follows:

1. Retrieve your project. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/retrieving-projects "mention") for more details.
2. Go to **Administration** > **General Settings** > **Repository binding**.
3. In the list of repositories, re-select the target repository and select **Save**.

</details>

### Changing the project key <a href="#changing-project-key" id="changing-project-key"></a>

1. Retrieve your project. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/retrieving-projects "mention") for more information.
2. In the left sidebar, select **Administration** > **Update Key**. The **Update Key** page opens.
3. Enter the new key and select **Update**.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [setting-up-project](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/setting-up-project "mention")
* [introduction](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/devops-platform-integration/introduction "mention") to Setting up the integration of your project with your DevOps platform
* [setting-permissions](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/setting-permissions "mention")
* [customizing-info-page](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/customizing-info-page "mention")
* [deleting-project](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/deleting-project "mention")
