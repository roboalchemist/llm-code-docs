# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/about/automatic-group-synchronization.md

# Automatic group synchronization

The automatic synchronization of user groups is used with the Single Sign-On (SSO) authentication. See the [user-group-concept](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/about-sonarqube-cloud-solution/user-management/user-group-concept "mention") page for more information about user groups in SonarQube Cloud.

With the automatic group synchronization:

* A user in SonarQube Cloud is automatically added to an organization’s group within the enterprise if the user is a member of a group with the same name in the IdP. (The check is case-sensitive and excludes the organization’s default **Members** group.)
* The users added to a SonarQube Cloud group become members of the respective organization.

<figure><img src="broken-reference" alt="Users in SonarQube Cloud are automatically added to an organization&#x27;s group if they are members of a group with the same name in the IdP. These users then become members of the respective SonarQube Cloud organization."><figcaption></figcaption></figure>

{% hint style="info" %}
If a group with the same name is assigned to several organizations, the user account is added to all these groups and thus, is a member of all these organizations.
{% endhint %}

{% hint style="warning" %}
If a user cannot be added to any group in SonarQube Cloud, they will land on an empty organization page.
{% endhint %}

### Related pages

* [..](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso "mention")
* [user-groups](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/users-and-permissions/user-groups "mention")
