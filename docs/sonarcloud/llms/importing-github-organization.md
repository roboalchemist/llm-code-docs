# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-github-organization.md

# Importing GitHub organization

When you import your GitHub organization or personal account to SonarQube Cloud, the corresponding [organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/about-sonarqube-cloud-solution/ressources-structure/organization "mention") is created in SonarQube Cloud and is bound to the DevOps platform organization. Each SonarQube Cloud organization corresponds one-to-one with a GitHub organization or personal account. See [binding-with-dop](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/about-sonarqube-cloud-solution/ressources-structure/binding-with-dop "mention") for more information.

{% hint style="warning" %}
SonarQube Cloud does not support linking an organization to more than one DevOps platform. If you want to link to more than one, you will need to create a separate organization to link to each DevOps platform.
{% endhint %}

The user account you used for the import is automatically assigned to the organization’s owners group which grants you administration rights on the organization. See [user-group-concept](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/about-sonarqube-cloud-solution/user-management/user-group-concept "mention") for more details.

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

You must be an owner of the GitHub organization.

In SonarQube Cloud, each organization is assigned a subscription plan. Before importing your organization, choose the subscription plan suited to your needs, see [subscription-plans](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans "mention") for more details. In particular, determine the number of Lines of Code (LOC) you need. See [#loc-based-pricing](https://docs.sonarsource.com/sonarqube-cloud/managing-subscription/subscription-plans#loc-based-pricing "mention") for more information.

### Importing the organization <a href="#import-procedure" id="import-procedure"></a>

To import your GitHub organization or personal account to SonarQube Cloud:

1. Log in to SonarQube Cloud with your GitHub account. If you’re a member of an enterprise, you may use any of your DevOps Platform accounts or your SSO account. In that case, see [importing-from-multiple-platforms](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-from-multiple-platforms "mention") for important insights.
2. At the top right of the SonarQube Cloud interface, select the ✚ (plus) menu and select **Create new organization**. The **Create an organization** page opens.
3. Under **Import from a DevOps platform**, select the **GitHub** button. The **Install SonarQubeCloud** page opens with the list of GitHub organizations you have access to. The SonarQube Cloud app is required to allow SonarQube Cloud to access your GitHub organization.\
   Note that if the GitHub organization you want to import has the SonarQube Cloud application already installed, it will be listed on the page with the **Configure** button. If this organization is not already bound to an organization in SonarQube Cloud, you will be able to import it after the configuration step. To do so, select it in the list. The application configuration opens in GitHub. Check the configuration and select the **Save** button. You’ll be redirected to SonarQube Cloud. You can then follow the instructions from step 6 below.

<figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-11716fecc3c2967e3ea2c3e739b6909bc5f928ce%2F65561929c2002cc37e19285f95e5c03bdf06cb90.png?alt=media" alt="When importing your GitHub organization into SonarQube Cloud, and your GitHub organization already has SonarQUbe Cloud installed, you&#x27;ll see a list of those organizations that are ready to import."><figcaption></figcaption></figure>

4\. Select the GitHub organization you want to import.

5\. In **Repository access**, you can restrict access to the Git repositories that can be imported to SonarQube Cloud for analysis (you can always change this setting later: see below).\
Once you’ve completed the app installation, you’ll be redirected to SonarQube Cloud’s **Create an organization** page.

6\. In **Import organization details**, SonarQube Cloud suggests a GitHub Actions secret **Name** and **Key** for your SonarQube Cloud organization. The key is unique across all organizations within SonarQube Cloud. You can accept the suggestion or change it manually. The interface will prevent you from changing it to an already existing key.

7\. Select **Add additional info** to add:

* An avatar: a small image representing the organization and displayed on the UI near the organization name.
* A description of the organization.
* A URL: the URL of the homepage of the organization displayed on the UI.

8\. Select the subscription plan for your organization. See [subscription-plans](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans "mention") for more details.

9\. If you selected a paid plan, select the number of Lines of Code (LOC) for your plan and follow the instructions to enter your billing and payment information.

10\. Select **Create Organization**. The organization is created and opened in SonarQube Cloud.

{% hint style="info" %}
If the import fails because the organization already exists in SonarQube Cloud and you’ve lost administrator access to this organization, send a request to <contact@sonarsource.com> with all the necessary details.
{% endhint %}

### Modifying the repository access rights of the organization <a href="#modifying-repository-access" id="modifying-repository-access"></a>

1. At the top right of the SonarQube Cloud interface, select the ✚ (plus) menu and select **Create new organization**. The **Create an organization** page opens.
2. Under **Import from a DevOps platform**, select the **GitHub** button. The **Install SonarQube Cloud** page opens.
   * Alternatively, directly select (on the page) the organization whose repository access you want to change.
3. Select **Configure** in front of the organization whose repository access you want to change and authenticate to GitHub. The GitHub’s **SonarQubeCloud** page opens.
4. Scroll down to **Repository access**.
5. Change the access option and select **Save**.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [importing-bitbucket-workspace](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-bitbucket-workspace "mention")
* [importing-gitlab-group](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-gitlab-group "mention")
* [importing-azure-devops-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-azure-devops-organization "mention")
* [creating-organization-manually](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/creating-organization-manually "mention")
* [binding-unbound-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/binding-unbound-organization "mention")
* [changing-organization-binding](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/changing-organization-binding "mention")
* [changing-organization-settings](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/changing-organization-settings "mention")
* [deleting-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/deleting-organization "mention")
