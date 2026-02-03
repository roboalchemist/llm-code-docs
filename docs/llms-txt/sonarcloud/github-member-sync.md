# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/users-and-permissions/github-member-sync.md

# Disabling GitHub member synchronization

When you disable the [GitHub member synchronization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/about-sonarqube-cloud-solution/user-management/github-member-synchronization), members will no longer be added or removed automatically and membership in GitHub-based organizations must be managed manually, as it is with other repository platforms.

{% hint style="warning" %}
When you enable synchronization manually, members of the SonarQube Cloud organization who aren’t members of the corresponding GitHub organization will be removed from the organization.
{% endhint %}

To enable/disable the GitHub member synchronization for your organization

1. Retrieve your organization. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") for more details.
2. Open the **Members** page.
3. Select **Configure synchronization**. The Members Management dialog opens.
4. Select the manual or automatic option and **Save**.
