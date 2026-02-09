# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-bitbucket-workspace.md

# Importing Bitbucket workspace

When you import a Bitbucket Cloud workspace to SonarQube Cloud, the corresponding [organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/about-sonarqube-cloud-solution/ressources-structure/organization "mention") is created in SonarQube Cloud and is bound to the DevOps platform organization. Each SonarQube Cloud organization corresponds one-to-one with a Bitbucket Cloud workspace. See [binding-with-dop](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/about-sonarqube-cloud-solution/ressources-structure/binding-with-dop "mention") for more information.

{% hint style="warning" %}
SonarQube Cloud does not support linking an organization to more than one DevOps platform. If you want to link to more than one, you will need to create a separate organization to link to each DevOps platform.
{% endhint %}

The user account you used for the import is automatically assigned to the organization’s owners group which grants you administration rights on the organization. See [user-group-concept](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/about-sonarqube-cloud-solution/user-management/user-group-concept "mention") for more details.

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

You must be an administrator of the Bitbucket workspace:

* You will already be an administrator of your default workspace.
* For any other workspace, you have to add your Bitbucket account to a user group with the **Administer workspace** user right enabled.

In SonarQube Cloud, each organization is assigned a subscription plan. Before importing your organization, choose the subscription plan suited to your needs, see [subscription-plans](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans "mention") for more details. In particular, determine the number of Lines of Code (LOC) you need. See [#loc-based-pricing](https://docs.sonarsource.com/sonarqube-cloud/managing-subscription/subscription-plans#loc-based-pricing "mention") for more information.

{% hint style="info" %}
To avoid exceeding [Bitbucket Cloud API rate limits](https://support.atlassian.com/bitbucket-cloud/docs/api-request-limits/), it is recommended to use a dedicated Bitbucket user for SonarQube Cloud integration.
{% endhint %}

### Import procedure <a href="#import-procedure" id="import-procedure"></a>

To import a Bitbucket Cloud workspace to SonarQube Cloud:

1. Log in to SonarQube Cloud with your Bitbucket account.
2. At the top right of the SonarQube Cloud interface, select the ✚ (plus) menu and select **Create new organization**. The **Create an organization** page opens.
3. Under **Import from a DevOps platform**, select the **Bitbucket** button.
4. When prompted, grant access to the SonarQube Cloud application to read your Bitbucket Cloud workspace. SonarQube Cloud requests access for:
   * Reading your account information.
   * Reading your repositories and their pull requests.
   * Reading your team membership information.
5. In SonarQube Cloud, in **Import organization details**, SonarQube Cloud suggests a **Name** and **Key** for your SonarQube Cloud organization. The key is unique across all organizations within SonarQube Cloud. You can accept the suggestion or change it manually. The interface will prevent you from changing it to an already existing key.
6. Select **Add additional info** to add:
   * An avatar: a small image representing the organization and displayed on the UI near the organization name.
   * A description of the organization.
   * A URL: the URL of the homepage of the organization displayed on the UI.
7. Select the subscription plan for your organization. See [subscription-plans](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans "mention") for more information.
8. If you selected a paid plan, select the number of Lines of Code (LOC) for your plan and follow the instructions to enter your billing and payment information.
9. Select **Create Organization**. The organization is created and opened in SonarQube Cloud.

{% hint style="info" %}
If the import fails because the organization already exists in SonarQube Cloud and you’ve lost administrator access to this organization, send a request to <contact@sonarsource.com> with all the necessary details.
{% endhint %}

### Related pages <a href="#related-pages" id="related-pages"></a>

* [importing-github-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-github-organization "mention")
* [importing-gitlab-group](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-gitlab-group "mention")
* [importing-azure-devops-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-azure-devops-organization "mention")
* [creating-organization-manually](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/creating-organization-manually "mention")
* [binding-unbound-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/binding-unbound-organization "mention")
* [changing-organization-binding](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/changing-organization-binding "mention")
* [changing-organization-settings](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/changing-organization-settings "mention")
* [deleting-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/deleting-organization "mention")
* [importing-from-multiple-platforms](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-from-multiple-platforms "mention")
