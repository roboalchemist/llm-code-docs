# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/binding-unbound-organization.md

# Binding an unbound organization

If you created your organization manually, then it’s not bound to its corresponding DevOps platform organization and you don’t benefit from many advantages. This procedure explains how to bind your unbound organization. See [binding-with-dop](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/about-sonarqube-cloud-solution/ressources-structure/binding-with-dop "mention") for more information. To do so, you need the corresponding permissions on your DevOps platform.

{% hint style="warning" %}

* You cannot unbind nor change the binding of an organization bound to a GitLab group or an Azure organization.
* If the binding fails because the organization already exists in SonarQube Cloud and you’ve lost administrator access to this organization, send a request to <contact@sonarsource.com> with all the necessary details.
  {% endhint %}

### Binding to a GitHub organization <a href="#github-organization" id="github-organization"></a>

You must be an owner of the GitHub organization.

To bind your unbound organization to a GitHub organization:

1. Log in to SonarQube Cloud with your GitHub account.\
   If you’re a member of an enterprise, you may use any of your DevOps Platform accounts or your SSO account. In that case, see [importing-from-multiple-platforms](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-from-multiple-platforms "mention") for important insights.
2. Retrieve your organization. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") for more information.
3. Go to **Administration** > **Organization settings** > **Organization binding**.
4. Select the **GitHub** button. The **Install SonarQube Cloud** page opens. The SonarQube Cloud app is required to allow SonarQube Cloud to access your GitHub organization.
5. Select the GitHub organization you want to import.
6. In **Repository access**, you can restrict access to the Git repositories that can be imported to SonarQube Cloud for analysis. You can always change this setting later, see [importing-github-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-github-organization "mention") for more details.
7. Select **Save**. Your SonarQube Cloud organization is bound.

### Binding to a Bitbucket Cloud workspace <a href="#bitbucket-workspace" id="bitbucket-workspace"></a>

You must be an administrator of the Bitbucket workspace:

* You will already be an administrator of your default workspace.
* For any other workspace, you have to add your Bitbucket account to a user group with the **Administer workspace** user right enabled.

To bind your unbound organization to a Bitbucket workspace:

1. Log in to SonarQube Cloud with your Bitbucket account.
2. Retrieve your organization. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") for more information.
3. Go to **Administration** > **Organization settings** > **Organization binding**.
4. Select the **Bitbucket** button.
5. When prompted, grant access to the SonarQube Cloud application to read your Bitbucket Cloud workspace. SonarQube Cloud requests access for:
   * Reading your account information.
   * Reading your repositories and their pull requests.
   * Reading your team membership information.

### Binding to a GitLab group <a href="#gitlab-group" id="gitlab-group"></a>

You can bind your SonarQube Cloud organization to:

* Any GitLab parent group of which you’re the owner.
* Your personal GitLab group. This group refers to the repositories that are under your personal namespace.

To bind your unbound organization to a GitLab group:

1. In GitLab, create the personal access token required by SonarQube Cloud to access the GitLab group. See [#create-personal-access-token](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/importing-gitlab-group#create-personal-access-token "mention") for more details.
2. Log in to SonarQube Cloud with your GitLab account.\
   If you’re a member of an enterprise, you may use any of your DevOps Platform accounts or your SSO account. In that case, see [importing-from-multiple-platforms](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-from-multiple-platforms "mention") for important insights.
3. Retrieve your organization. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") for more information.
4. Go to **Administration** > **Organization settings** > **Organization binding**.
5. Select the **GitLab** button.
6. Select either
   * **Import any GitLab group**, if you want to import a GitLab group other than your personal one, or
   * **Import my personal GitLab group**, if you want to import only the repositories that are under your personal namespace.
7. **In GitLab group key** (if you don’t import your personal GitLab group), enter the group key. To retrieve the key, see [#retrieve-group-key](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/importing-gitlab-group#retrieve-group-key "mention") for more information.
8. In **Personal Access Token**, paste the personal access token you created in the first step.

### Binding to an Azure DevOps organization <a href="#azure-devops-organization" id="azure-devops-organization"></a>

You must be an administrator of the Azure DevOps organization.

To bind your unbound organization to an Azure DevOps organization:

1. In Azure DevOps, create the Personal Access Token (PAT) required by SonarQube Cloud to access the Azure DevOps organization. See [#create-pat](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/importing-azure-devops-organization#create-pat "mention") for more information.
2. Log in to SonarQube Cloud with your Azure DevOps account.\
   If you’re a member of an enterprise, you may use any of your DevOps Platform accounts or your SSO account. In that case, see [importing-from-multiple-platforms](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-from-multiple-platforms "mention") for important insights.
3. Retrieve your organization. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") for more information.
4. Go to **Administration** > **Organization settings** > **Organization binding**.
5. Select the **Azure DevOps** button.
6. Follow the instructions.
7. In **Personal Access Token**, paste the PAT you created in the first step.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [importing-github-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-github-organization "mention")
* [importing-bitbucket-workspace](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-bitbucket-workspace "mention")
* [importing-gitlab-group](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-gitlab-group "mention")
* [importing-azure-devops-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-azure-devops-organization "mention")
* [creating-organization-manually](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/creating-organization-manually "mention")
* [changing-organization-binding](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/changing-organization-binding "mention")
* [changing-organization-settings](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/changing-organization-settings "mention")
* [deleting-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/deleting-organization "mention")
* [importing-from-multiple-platforms](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-from-multiple-platforms "mention")
