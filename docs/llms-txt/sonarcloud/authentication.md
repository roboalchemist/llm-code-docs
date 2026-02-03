# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration/authentication.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/instance-administration/authentication.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/instance-administration/authentication.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/instance-administration/authentication.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/instance-administration/authentication.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/instance-administration/authentication.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/instance-administration/authentication.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/instance-administration/authentication.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/instance-administration/authentication.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/instance-administration/authentication.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/instance-administration/authentication.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/authentication.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/authentication.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/authentication.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/authentication.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/authentication.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/authentication.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/authentication.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication.md

# Authentication and provisioning

- [Overview of authentication and provisioning](/sonarqube-server/instance-administration/authentication/overview.md): SonarQube Server can delegate authentication via HTTP Headers, GitHub Authentication, GitLab Authentication, Bitbucket Cloud Authentication, SAML, or LDAP.
- [HTTP header](/sonarqube-server/instance-administration/authentication/http-header.md): Setting up the HTTP header authentication in your SonarQube Server instance.
- [LDAP](/sonarqube-server/instance-administration/authentication/ldap.md): Setting up the LDAP authentication in your SonarQube Server instance.
- [SAML](/sonarqube-server/instance-administration/authentication/saml.md): Setting up SAML authentication in your SonarQube Server instance.
- [Overview of SAML support](/sonarqube-server/instance-administration/authentication/saml/overview.md): You can delegate authentication to a SAML 2.0 identity provider using SAML authentication. SonarQube Server uses the Service Provider (SP) initiated SAML.
- [With Microsoft Entra ID](/sonarqube-server/instance-administration/authentication/saml/ms-entra-id.md): Setting up SAML authentication with Microsoft Entra ID in your SonarQube Server instance.
- [Introduction to SAML with Microsoft Entra ID](/sonarqube-server/instance-administration/authentication/saml/ms-entra-id/introduction.md): Main steps of SAML authentication setup with Microsoft Entra ID.
- [Setup in Microsoft Entra ID](/sonarqube-server/instance-administration/authentication/saml/ms-entra-id/setup-in-entra-id.md): This page describes how to register SonarQube Server in Microsoft Entra ID.
- [Setup in SonarQube Server](/sonarqube-server/instance-administration/authentication/saml/ms-entra-id/setup-in-sq.md): This page describes how to setup in SonarQube Server SAML with Microsoft Entra ID.
- [Setup of security features](/sonarqube-server/instance-administration/authentication/saml/ms-entra-id/optional-security-features.md): To improve security, you can set up the encryption of SAML assertions sent by Microsoft Entra ID and the signing of SAML requests sent by SonarQube Server.
- [With Keycloak](/sonarqube-server/instance-administration/authentication/saml/how-to-set-up-keycloak.md): Setting up SAML authentication with Keycloak in your SonarQube Server instance.
- [With Okta](/sonarqube-server/instance-administration/authentication/saml/how-to-set-up-okta.md): Setting up SAML authentication with Okta in your SonarQube Server instance.
- [With Ping Identity](/sonarqube-server/instance-administration/authentication/saml/ping-identity.md): Setting up SAML authentication with Ping Identity in your SonarQube Server instance.
- [Introduction to SAML with Ping Identity](/sonarqube-server/instance-administration/authentication/saml/ping-identity/introduction.md): Main steps of SAML setup with Ping Identity.
- [Setup in Ping Identity](/sonarqube-server/instance-administration/authentication/saml/ping-identity/setup-in-ping-identity.md): This page explains how to register SonarQube Server in PingOne or PingFederate.
- [Setup in SonarQube Server](/sonarqube-server/instance-administration/authentication/saml/ping-identity/setup-in-sq.md): This page describes how to set up SAML with Ping Identity in SonarQube Server.
- [Setup of security features](/sonarqube-server/instance-administration/authentication/saml/ping-identity/optional-security-features.md): To improve security, you can set up the encryption of SAML assertions sent by Ping Identity and the signing of SAML requests sent by SonarQube Server.
- [With SCIM provisioning](/sonarqube-server/instance-administration/authentication/saml/scim.md): Setting up automatic provisioning between SonarQube Server and Microsoft Entra ID or Okta using SCIM.
- [SCIM overview](/sonarqube-server/instance-administration/authentication/saml/scim/overview.md): SCIM helps you automatically provision user and groups to SonarQube Server.
- [SCIM with Microsoft Entra ID](/sonarqube-server/instance-administration/authentication/saml/scim/scim-provisioning-with-azure-ad.md): Enable SCIM to automate user and group provisioning from Microsoft Entra ID to SonarQube Server.
- [SCIM with Okta](/sonarqube-server/instance-administration/authentication/saml/scim/scim-provisioning-with-okta.md): Enable SCIM to automate user and group provisioning from Okta to SonarQube Server.
- [GitHub](/sonarqube-server/instance-administration/authentication/github.md): Setting up the GitHub authentication in your SonarQube Server instance.
- [Bitbucket Cloud](/sonarqube-server/instance-administration/authentication/bitbucket-cloud.md): Setting up the Bitbucket Cloud authentication in your SonarQube Server instance.
- [GitLab](/sonarqube-server/instance-administration/authentication/gitlab.md): Setting up the GitLab authentication in your SonarQube Server instance.
- [Provisioning modes](/sonarqube-server/instance-administration/authentication/gitlab/provisioning-modes.md): This section describes GitLab provisioning modes
- [Introduction to GitLab provisioning modes](/sonarqube-server/instance-administration/authentication/gitlab/provisioning-modes/introduction.md): Overview of the GitLab authentication's provisioning modes.
- [Just-in-Time provisioning](/sonarqube-server/instance-administration/authentication/gitlab/provisioning-modes/just-in-time.md): With the Just-in-Time (JIT) provisioning mode, user accounts are automatically created in SonarQube Server when GitLab users log in for the first time.
- [Automatic provisioning](/sonarqube-server/instance-administration/authentication/gitlab/provisioning-modes/automatic.md): With GitLab automatic provisioning mode, you can benefit from automatic user provisioning, deprovisioning and synchronization of groups and permissions in SonarQube Server.
- [Setting up authentication](/sonarqube-server/instance-administration/authentication/gitlab/setting-up.md): Setting up the GitLab authentication and provisioning in SonarQube Server.
- [Managing JIT provisioning](/sonarqube-server/instance-administration/authentication/gitlab/managing-jit-mode.md): Once you’ve set up GitLab authentication and provisioning with the Just-in-Time (JIT) provisioning mode, you can set or change JIT provisioning mode options.
- [Managing automatic provisioning](/sonarqube-server/instance-administration/authentication/gitlab/managing-automatic-provisioning.md): Starting from the Developer Edition, you can enable the automatic user and group provisioning in SonarQube Server.
- [Disabling authentication](/sonarqube-server/instance-administration/authentication/gitlab/disabling.md): To disable GitLab authentication and provisioning in SonarQube Server, you must disable the GitLab authentication configuration.
- [Troubleshooting](/sonarqube-server/instance-administration/authentication/troubleshooting.md): Troubleshooting authentication and provisioning.
