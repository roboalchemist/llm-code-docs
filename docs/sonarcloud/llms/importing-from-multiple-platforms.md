# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-from-multiple-platforms.md

# Using multiple accounts

When you import an organization to SonarQube Cloud, the account you use for the import is added as a member of the organization (with the Administer Organization permission). If you want that your other SonarQube Cloud account(s) be also part of the organization, you must [organization-members](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/users-and-permissions/organization-members "mention").

For example, if you import a GitHub organization from your GitHub account and need to view and manage this organization from your Azure DevOps account, then you must add your Azure DevOps account as a member of the organization. The procedure differs depending on whether your GitHub and Azure DevOps accounts have different email addresses or not as described below.

### Accounts with different email addresses <a href="#accounts-with-different-email-addresses" id="accounts-with-different-email-addresses"></a>

1. Log in to SonarQube Cloud with your GitHub account.
2. Retrieve the GitHub organization and go to **Members**.
3. Select the **Add a member** button. The **Add member** dialog opens.
4. Enter the exact email address of your Azure DevOps account.
5. Select **Add member**.
6. Go to **Administration > Permissions** to grant the Administer Organization permission to this new member.

### Accounts with the same email address <a href="#accounts-with-same-email-address" id="accounts-with-same-email-address"></a>

Since SonarQube Cloud doesn’t simultaneously support two accounts with the same email address, another user with an Azure DevOps account must perform the procedure. You must first set this user as an admin of the organization.

Proceed as follows:

1. Log in to SonarQube Cloud with your GitHub account (your Azure DevOps account is dissociated from SonarQube Cloud).
2. Retrieve the GitHub organization and go to **Members**.
3. Select the **Add a member** button. The **Add member** dialog opens.
4. Enter the exact email address of the other user’s Azure DevOps account.
5. Select **Add member**.
6. Go to **Administration** > **Permissions** to grant the Administer Organization permission to this new member.
7. Log out from SonarQube Cloud.
8. Log in to SonarQube Cloud with your Azure DevOps account (your Azure DevOps account is reassociated with SonarQube Cloud).
9. The other user logs in to SonarQube Cloud with their Azure DevOps account and adds your Azure DevOps account as a member of the organization as described in steps 2 to 6.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [importing-github-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-github-organization "mention")
* [importing-bitbucket-workspace](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-bitbucket-workspace "mention")
* [importing-gitlab-group](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-gitlab-group "mention")
* [importing-azure-devops-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-azure-devops-organization "mention")
* [organization-members](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/users-and-permissions/organization-members "mention")
* [creating-organization-manually](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/creating-organization-manually "mention")
* [binding-unbound-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/binding-unbound-organization "mention")
* [changing-organization-settings](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/changing-organization-settings "mention")
* [deleting-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/deleting-organization "mention")
