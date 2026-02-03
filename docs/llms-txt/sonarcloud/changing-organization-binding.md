# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/changing-organization-binding.md

# Changing organization binding

Sonar is planning to change the organization binding feature in order to allow a simplified change of organization binding. In the meantime, you can use the workaround described below for a SonarQube Cloud organization bound to a GitHub organization or a Bitbucket workspace.

You will first unbind the SonarQube Cloud organization and then rebind it to the new DevOps platform organization. The new organization may be on any DevOps platform (GitHub, Bitbucket, GitLab or Azure DevOps).

{% hint style="warning" %}

* The workaround applies only to a SonarQube Cloud organization bound to a GitHub organization or a Bitbucket workspace.
* You must manually change the binding of the projects within the SonarQube Cloud organization.
  {% endhint %}

The operation is different if the new binding is on a different DevOps platform.

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

To be able to change the binding of a SonarQube Cloud organization, you must:

* Be an admin of the organization.
* Have the required permissions on the new DevOps platform organization. It means, depending on the DevOps platform:
  * GitHub: be an owner of the GitHub organization.
  * Bitbucket workspace: be an administrator of the Bitbucket workspace. You will already be an administrator of your default workspace. For any other workspace, you have to add your Bitbucket account to a user group with the Administer workspace user right enabled.
  * GitLab: be an owner of the GitLab group.
  * Azure DevOps: be an administrator of the Azure DevOps organization.

### On the same DevOps platform <a href="#on-same-platform" id="on-same-platform"></a>

1. Remove the SonarQube Cloud app from the GitHub organization or a Bitbucket workspace (this will unbind the organization in SonarQube Cloud). See:
   * [Deleting a GitHub App](https://docs.github.com/en/apps/maintaining-github-apps/deleting-a-github-app) in the GitHub documentation.
   * [Removing an app](https://support.atlassian.com/bitbucket-cloud/docs/bitbucket-cloud-apps-overview/) in the Altassian documentation.
2. Sign in to SonarQube Cloud.
3. Bind the unbound organization to the new DevOps platform organization. See [binding-unbound-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/binding-unbound-organization "mention") for more information.
4. Change the binding of each project in the SonarQube Cloud organization. See [changing-binding](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/changing-binding "mention") for more information.

### On a different DevOps platform <a href="#on-different-platform" id="on-different-platform"></a>

This section explains the operation in case you want to change the binding of the organization to a different DevOps platform. DevOps platform1 refers to your GitHub organization or Bitbucket workspace that you want to unbind. DevOps platform2 refers to your GitHub organization, Bitbucket workspace, GitLab group, or Azure DevOps organization that you want to bind to.

If you’re a member of an enterprise and DevOps platform2 is not Bitbucket, you may use any of your DevOps Platform accounts or your SSO account to perform the new binding. It means that you can log in to SonarQube Cloud with your account that is an admin of the SonarQube Cloud organization and follow the steps above in *On the same DevOps platform*.

Otherwise, you must use your DevOps platform2’s account (`Account2`) to perform the new binding. You must make sure that `Account2` is also an admin of the SonarQube Cloud organization to be changed. If it’s not the case, you must add it to the organization by using your DevOps platform1’s account (`Account1`) that is an admin of the organization. To do so:

1. Sign in to SonarQube Cloud with `Account1`.
2. Add `Account2` as a member of the SonarQube Cloud organization, see [organization-members](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/users-and-permissions/organization-members "mention") for more details. This operation is not possible if `Account1` and `Account2` have different email addresses, since SonarQube Cloud doesn’t simultaneously support two accounts with the same email address. In that case, another user must perform the procedure and you must first set this user as an admin of the organization.
3. Grant the Administer organization permission to `Account2`, see [organization-permissions](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/users-and-permissions/organization-permissions "mention") for more details.
4. You can now follow the steps above in *On the same DevOps platform* by signing in to SonarQube Cloud with `Account2`*.*
