# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/adding-organizations-to-your-enterprise.md

# Adding organizations to your enterprise

You can add an organization to an existing enterprise provided you are an admin of both the enterprise and the organization.

{% hint style="warning" %}
If you add a Team plan organization to your enterprise, the organization’s Team plan subscription will be automatically cancelled and the organization will be moved to the Enterprise plan without a refund. Therefore, we recommend adding your organizations before their next billing date to avoid double charges.
{% endhint %}

{% hint style="info" %}
Currently, Sonar restricts each enterprise to a maximum of 200 organizations.
{% endhint %}

To add an organization to an existing enterprise:

1. Log in to SonarQube Cloud with your enterprise admin account.
2. Retrieve your enterprise.
3. In the **Organizations** tab, select the **Add organization** button. The **Add an organization** dialog opens.
4. Select the organization to be added and select the **Add** button.\
   If you cannot see your organization, it probably means that your enterprise admin account is not admin of the organization. It may be the case if you imported your organization by using another user account (typically, from another DevOps platform’s account). In that case, see *Adding organizations belonging to multiple DevOps platforms* below.

### Adding organizations belonging to multiple DevOps platforms <a href="#add-org-from-multiple-platforms" id="add-org-from-multiple-platforms"></a>

You can add to your enterprise organizations belonging to multiple DevOps platforms (The prerequisites described above in *Adding an organization to an enterprise* apply.).

When possible, use the same admin account to create your enterprise and import the organizations you want to add to your enterprise.

Currently, the following apply (The limitations on Bitbucket organization import will be removed in a future SonarQube Cloud release.):

* To import a Bitbucket workspace, you must log in to SonarQube Cloud with your Bitbucket account.
* To import a GitHub organization, a GitLab group, or an Azure DevOps organization, you can use any account, including your SSO account.

If you use different admin accounts (e.g., if your enterprise should contain GitHub organizations and Bitbucket workspaces), your enterprise admin account may not be an admin of the new organization you want to add to your enterprise. For example, your enterprise admin account is a GitHub account; you have imported a Bitbucket workspace to SonarQube Cloud with your Bitbucket account, and you want to add the so-created organization to your enterprise. In that case, additional steps are necessary as described below:

1. Log in to SonarQube Cloud with your Bitbucket account (the account you used to import your workspace).
2. Add your GitHub account (enterprise admin account) as a member of the organization to be added. See [organization-members](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/users-and-permissions/organization-members "mention") for more information.
3. Give this account the Administer Organization permission. See [organization-permissions](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/users-and-permissions/organization-permissions "mention") for more information.
4. Log in to SonarQube Cloud with your GitHub account and add the new organization to the enterprise as described above in *Adding an organization to an enterprise*.

{% hint style="warning" %}
In the example above, if the Bitbucket account and the enterprise admin account use the same email address, the procedure will not work. To solve the problem, let another user perform steps 1 and 2 with their Bitbucket account.
{% endhint %}

### Removing an organization from your enterprise <a href="#removing-org-from-enterprise" id="removing-org-from-enterprise"></a>

You can remove an organization from an existing enterprise provided:

* You are an admin of both the enterprise and the organization through a SonarQube Cloud account that is not an SSO account.
* The organization to be removed is not the only member of your enterprise (you currently cannot downgrade an entire enterprise).

When you remove an organization, you have to choose the organization’s new subscription plan (Free or Team). Be aware that you’ll loose features. For more information, see [#reviewing-the-plan-changes](https://docs.sonarsource.com/sonarqube-cloud/managing-subscription/changing-plan#reviewing-the-plan-changes "mention").

Proceed as follows:

1. Retrieve the enterprise.
2. In the **Organizations** tab, select the **Remove and downgrade** button at the far right of the organization to be removed. The **Select an alternate plan to downgrade** dialog opens.
3. Select the plan
4. Select the **Confirm removal and downgrade** button and follow the instructions to complete your subscription. Note that you will not be able to analyze your organization’s private projects as long as you haven’t completed your new subscription.

### Related pages <a href="#related-pages" id="related-pages"></a>

[retrieving-and-viewing-your-enterprise](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/retrieving-and-viewing-your-enterprise "mention")\
[creating-your-enterprise](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/creating-your-enterprise "mention")\
[enterprise-security](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security "mention")\
[managing-the-enterprise-related-permissions](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/managing-the-enterprise-related-permissions "mention")\
[managing-the-lines-of-code-within-your-enterprise](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/managing-the-lines-of-code-within-your-enterprise "mention")\
[changing-enterprise-settings](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/changing-enterprise-settings "mention")\
[downgrading-your-enterprise](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/downgrading-your-enterprise "mention")
