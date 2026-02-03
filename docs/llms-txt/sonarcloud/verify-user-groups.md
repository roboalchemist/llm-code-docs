# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/setup/verify-user-groups.md

# Step 1: Verify the user groups

Before configuring [about](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/about "mention"), you must ensure that the [automatic-group-synchronization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/about/automatic-group-synchronization "mention") can take place properly. To do so, verify that:

* The user groups defined in your IdP service exist in the relevant organizations of your SonarQube Cloud enterprise (i.e. a group with the same (context-sensitive) name exists in the relevant organization(s)).
* The user groups in SonarQube Cloud have the correct permissions.

To manage the user groups in SonarQube Cloud, see [user-groups](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/users-and-permissions/user-groups "mention").

### In Okta <a href="#okta" id="okta"></a>

The automatic group synchronization of a group applies if the group in Okta and the corresponding group in the SonarQube Cloud organization have the same (case-sensitive) name. Note that the default SonarQube Cloud’s Members group is excluded from the synchronization.

The figure below shows on the left groups defined in Okta and on the right the corresponding groups defined in SonarQube Cloud in two different organizations (`OrgA` and `OrgB`). In this example, the SSO users belonging to `ENT_ORGA_ADMINS` will be automatically added to the corresponding `EN_ORG_ADMINS` group in SonarQube Cloud. it means that they will have access to `OrgA` with the permissions defined in SonarQube Cloud.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-ec5c691e7e965d7e844d77914312cd4e05eeb10f%2F02fbdbff622df1152926bc75d1ad8573150940af.png?alt=media" alt="Okta groups (shown on left as your SSO application) map to SonarQube Cloud groups (shown on right as OrgA and OrgB) in different organizations."><figcaption></figcaption></figure></div>

### In Microsoft Entra ID <a href="#entra-id" id="entra-id"></a>

The automatic group synchronization of a group applies if the group in Microsoft Entra ID and the corresponding group in the SonarQube Cloud organization have the same (case-sensitive) name. Note that the default SonarQube Cloud’s Members group is excluded from the synchronization.

The figure below shows on the left groups defined in Microsoft Entra ID and on the right the corresponding groups defined in SonarQube Cloud in two different organizations (`Docs-Team` and `claudiasonarova 2023`). In this example, the SSO users belonging to `Communications` will be automatically added to the corresponding `Communications` group in SonarQube Cloud. it means that they will have access to the `Docs-Team` organization with the permissions defined in SonarQube Cloud.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-ea8da8d67217c89265eada0a51a131b25d7f14d8%2F9d52adf2061ffd948720829f2d07a24faa939b8f.png?alt=media" alt="Microsoft Entra ID groups (shown on left as your SSO application) map to SonarQube Cloud groups (shown on right as OrgA and OrgB) in different organizations."><figcaption></figcaption></figure></div>

{% hint style="warning" %}

* Group synchronization doesn’t work with Microsoft Entra ID’s nested groups.
* Microsoft Entra ID’s SAML tokens have a limit regarding the number of groups a user can belong to (see the description of groups in the [Claims in SAML Token](https://learn.microsoft.com/en-us/entra/identity-platform/reference-saml-tokens#claims-in-saml-tokens) table). In such cases, you might need to reduce the number of groups the user is in.
  {% endhint %}

### Related pages <a href="#related-pages" id="related-pages"></a>

[configure-sso](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/setup/configure-sso "mention")\
[inviting-users-to-sign-in](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/setup/inviting-users-to-sign-in "mention")\
[terminate-setup](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/setup/terminate-setup "mention")\
[editing-sso-configuration](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/editing-sso-configuration "mention")\
[deleting-sso-configuration](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/deleting-sso-configuration "mention")
