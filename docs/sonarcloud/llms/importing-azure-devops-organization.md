# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-azure-devops-organization.md

# Importing Azure DevOps organization

When you import an Azure DevOps organization to SonarQube Cloud, the corresponding [organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/about-sonarqube-cloud-solution/ressources-structure/organization "mention") is created in SonarQube Cloud and is bound to the DevOps platform organization. Each SonarQube Cloud organization corresponds one-to-one with an Azure DevOps organization. See [binding-with-dop](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/about-sonarqube-cloud-solution/ressources-structure/binding-with-dop "mention") for more information.

{% hint style="warning" %}
SonarQube Cloud does not support linking an organization to more than one DevOps platform. If you want to link to more than one, you will need to create a separate organization to link to each DevOps platform.
{% endhint %}

The user account you used for the import is automatically assigned to the organization’s owners group which grants you administration rights on the organization. See [user-group-concept](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/about-sonarqube-cloud-solution/user-management/user-group-concept "mention") for more details.

{% hint style="warning" %}
You cannot unbind nor change the binding of an organization bound on Azure DevOps.
{% endhint %}

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

You must be an administrator of the Azure DevOps organization.

In SonarQube Cloud, each organization is assigned a subscription plan. Before importing your organization, choose the subscription plan suited to your needs. See [subscription-plans](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans "mention") for more information. In particular, determine the number of Lines of Code (LOC) you need. See [#loc-based-pricing](https://docs.sonarsource.com/sonarqube-cloud/managing-subscription/subscription-plans#loc-based-pricing "mention") for more details.

### Step 1: Create a PAT on the Azure organization <a href="#create-pat" id="create-pat"></a>

SonarQube Cloud uses an Azure DevOps user account to import your Azure DevOps organization and repositories. You must provide a [Personal Access Token](https://docs.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=tfs-2017\&tabs=preview-page) (PAT) from this account. The PAT will be stored in the respective SonarQube Cloud organization. We highly recommend that you use a dedicated technical user account in Azure DevOps.

{% hint style="warning" %}
Be aware of the following PAT failure points:

* Azure PATs require an expiration date. Check the [Microsoft documentation](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops\&tabs=Windows#create-a-pat) for details when creating your PAT.
* Azure requires that a user log in every 30 days, or it automatically stops a PAT; this action may cause your related pipeline to fail. Here is [an Azure Q\&A](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops\&tabs=Windows#q-why-did-my-pat-stop-working) on this topic.
  {% endhint %}

<details>

<summary>Creating a technical user account</summary>

We highly recommend that you use a dedicated technical user account in Azure DevOps to manage the integration with SonarQube.

* Do not set the technical user’s account with a **Stakeholder** access type. Use the **Basic** access type instead. (Users with the **Stakeholder** access type can have problems finding their repos when trying to analyze projects.)
* We recommend that you add the account to the **Contributors** security group.

See the Azure documentation for more information [about access levels](https://learn.microsoft.com/en-us/azure/devops/organizations/security/access-levels?view=azure-devops).

</details>

<details>

<summary>Generating your Azure PAT</summary>

1\. Log in to Azure DevOps with the technical user account created before.

2\. Go to your Azure DevOps organization **User settings** > **Personal access tokens** and select **+ New token**.

![](https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-a50fc8ccb44c771677b29ef4a4f4cfd4b73bd865%2F5a0d50d23b0ee669d5b7c953e2c59e6764178f51.png?alt=media)

3\. On the next page, under **Scopes**, make sure that you specify at least the scope **Code** > **Read & write**.

<div align="left"><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-128158af9fcfb34259657ffb547b9742a4fc5c06%2F927ace9131ea5be54812d65f3dae0f2624a4b674.png?alt=media" alt="" width="563"></div>

4\. Click **Create** to generate the token.

5\. When the personal access token is displayed, copy it (you will have to paste it to SonarQube’s configuration record as described below).

</details>

{% hint style="info" %}

* If you create a project manually, you can set the Azure PAT at the project level but this is not recommended. You should create a bound organization and make sure that the PAT is entered only at the organization level, not at the project level. The project-level field should be left blank.
* If you need to change the PAT stored in the SonarQube Cloud organization, see [changing-organization-settings](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/changing-organization-settings "mention") for more information.
  {% endhint %}

### Step 2: Import your Azure organization <a href="#import" id="import"></a>

To import your Azure organization to SonarQube Cloud:

1. Log in to SonarQube Cloud with your Azure DevOps account.\
   If you’re a member of an enterprise, you may use any of your DevOps Platform accounts or your SSO account. In that case, see [importing-from-multiple-platforms](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-from-multiple-platforms "mention") for important insights.
2. At the top right of the SonarQube Cloud interface, select the ✚ (plus) menu and select **Create new organization**. The **Create an organization** page opens.
3. Under **Import from a DevOps platform**, select the **Azure DevOps** button.
4. Follow the instructions.
5. Paste the PAT you created in Step 1 to **Personal Access Token**,.
6. Select **Continue**.
7. In **Import organization details**, SonarQube Cloud suggests a **Name** and **Key** for your SonarQube Cloud organization. The key is unique across all organizations within SonarQube Cloud. You can accept the suggestion or change it manually. The interface will prevent you from changing it to an already existing key.
8. Select **Add additional info** to add:
   * An avatar: a small image representing the organization and displayed on the UI near the organization name.
   * A description of the organization.
   * A URL: the URL of the homepage of the organization displayed on the UI.
9. Select the subscription plan for your organization. See [subscription-plans](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans "mention") for more details.
10. If you selected a paid plan, select the number of Lines of Code (LOC) for your plan and follow the instructions to enter your billing and payment information.
11. Select **Create Organization**. The organization is created and opened in SonarQube Cloud.

{% hint style="info" %}
If the import fails because the organization already exists in SonarQube Cloud and you’ve lost administrator access to this organization, send a request to <contact@sonarsource.com> with all the necessary details.
{% endhint %}

### Related pages <a href="#related-pages" id="related-pages"></a>

* [importing-github-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-github-organization "mention")
* [importing-bitbucket-workspace](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-bitbucket-workspace "mention")
* [importing-gitlab-group](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-gitlab-group "mention")
* [importing-from-multiple-platforms](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-from-multiple-platforms "mention")
* [creating-organization-manually](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/creating-organization-manually "mention")
* [binding-unbound-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/binding-unbound-organization "mention")
* [changing-organization-binding](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/changing-organization-binding "mention")
* [changing-organization-settings](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/changing-organization-settings "mention")
* [deleting-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/deleting-organization "mention")
