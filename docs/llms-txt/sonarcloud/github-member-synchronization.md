# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/about-sonarqube-cloud-solution/user-management/github-member-synchronization.md

# GitHub member synchronization

*This feature is only available in the Team and Enterprise plans. See* [subscription-plans](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans "mention") *for more information.*

When you import a GitHub organization to SonarQube Cloud, the member synchronization is enabled by default on the new SonarQube Cloud organization provided Single Sign-On (SSO) authentication is not enabled. It means that:

* Existing SonarQube Cloud users who are members of the GitHub organization will be automatically added to the SonarQube Cloud organization during the import.
* New SonarQube Cloud users who are members of the GitHub organization will be automatically added to the SonarQube Cloud organization when they first sign up with SonarQube Cloud.
* Adding or removing GitHub organization members will be automatically synchronized in SonarQube Cloud, provided the corresponding SonarQube Cloud user exists.
* Note that user groups and permissions are not synchronized.

You can enable or disable the synchronization of bound organizations manually.&#x20;

### Related pages

[github-member-sync](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/users-and-permissions/github-member-sync "mention")
