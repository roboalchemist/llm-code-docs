# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration.md

# Source: https://docs.sonarsource.com/sonarqube-server/8.9/instance-administration.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/instance-administration.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/instance-administration.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/instance-administration.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/instance-administration.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/instance-administration.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/instance-administration.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/instance-administration.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/instance-administration.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/instance-administration.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/instance-administration.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration.md

# Instance administration

- [Introduction to instance administration](/sonarqube-server/instance-administration/overview.md): This section guides administrators on setting up the instance's functions, configuring analysis features at the instance level, and administering users.
- [Server base URL](/sonarqube-server/instance-administration/server-base-url.md): Configuring your base URL in SonarQube Server.
- [Global analysis setup](/sonarqube-server/instance-administration/analysis-functions.md): Setting up analysis features at the instance level.
- [Choosing a mode for your instance](/sonarqube-server/instance-administration/analysis-functions/instance-mode.md): Your SonarQube Server has two modes for customers to choose from: Standard Experience Mode and Multi-Quality Rule (MQR) Mode.
- [Overview](/sonarqube-server/instance-administration/analysis-functions/instance-mode/instance-mode-overview.md): Your SonarQube Server instance has two modes: Standard Experience Mode and Multi-Quality Rule (MQR) Mode.
- [MQR mode](/sonarqube-server/instance-administration/analysis-functions/instance-mode/mqr-mode.md): MQR Mode more accurately represents the impact an issue has on all software qualities, by assigning a separate severity to a rule for each quality it impacts.
- [Standard Experience](/sonarqube-server/instance-administration/analysis-functions/instance-mode/standard-experience.md): The Standard Experience encompasses the use of rule types such as bugs, code smells, and vulnerabilities, with a single type and severity level for each rule.
- [New code definition](/sonarqube-server/instance-administration/analysis-functions/setting-new-code-definition-at-global-level.md): The global-level new code definition option is applied by default to all new projects. Project administrators can select a specific setting for their project.
- [Quality standards](/sonarqube-server/instance-administration/analysis-functions/quality-standards.md): This page explains how to configure at the global level parameters or features impacting the quality gates or profiles.
- [Analysis scope](/sonarqube-server/instance-administration/analysis-functions/analysis-scope.md): As a System Administrator, you can define in the UI an analysis scope adjustment at the instance level.
- [Introduction](/sonarqube-server/instance-administration/analysis-functions/analysis-scope/introduction.md): As a System Administrator, you can define in the UI an analysis scope adjustment at the global level.
- [Excluding files based on file paths](/sonarqube-server/instance-administration/analysis-functions/analysis-scope/excluding-files-based-on-file-paths.md): To exclude files from the project’s analysis scope based on file paths, you can define file exclusion parameters based on directory and file name patterns.
- [Excluding from coverage or duplication](/sonarqube-server/instance-administration/analysis-functions/analysis-scope/exclude-from-coverage-duplication.md): Excluding specific files from code coverage or duplication check at the global level.
- [Using advanced exclusion features](/sonarqube-server/instance-administration/analysis-functions/analysis-scope/advanced-exclusion-features.md): Information on using the advanced exclusion features in SonarQube Server at the global level.
- [Code metrics](/sonarqube-server/instance-administration/analysis-functions/metrics-parameters.md): Modifying parameters related to the maintainability metrics in SonarQube Server at the global level.
- [Integration with external analyzers at instance level](/sonarqube-server/instance-administration/analysis-functions/integration-with-external-analyzers.md): How to integrate SonarQube Server with external analyzers at the instance level.
- [Various settings at the instance level](/sonarqube-server/instance-administration/analysis-functions/various-settings-at-the-instance-level.md): You need the Administer System permssion to perform settings at the instance level.
- [System functions setup](/sonarqube-server/instance-administration/system-functions.md): Setting system functions in your SonarQube Server instance.
- [Notifications](/sonarqube-server/instance-administration/system-functions/notifications.md): Everything you need to know about configuring SonarQube Server’s email or Slack notifications.
- [Setting up email notifications](/sonarqube-server/instance-administration/system-functions/notifications/email.md): How to set up the email notifications feature on analysis-related events.
- [Setting up Slack notifications](/sonarqube-server/instance-administration/system-functions/notifications/slack.md): With the SonarQube Server integration with Slack, users can receive real-time notifications on analysis results directly in Slack.
- [About SonarQube Server integration with Slack](/sonarqube-server/instance-administration/system-functions/notifications/slack/about.md): This page provides a technical overview of the Slack integration solution in SonarQube Server.
- [Setting up the connection to Slack](/sonarqube-server/instance-administration/system-functions/notifications/slack/setup.md): How to connect your SonarQube Server instance to your Slack workspace.
- [Troubleshooting the Slack connection](/sonarqube-server/instance-administration/system-functions/notifications/slack/troubleshooting.md): How to troubleshoot various issues with your Slack connection.
- [Security features](/sonarqube-server/instance-administration/system-functions/security.md): SonarQube Server comes with a number of global security features.
- [Housekeeping](/sonarqube-server/instance-administration/system-functions/housekeeping.md): Default settings for SonarQube Server’s database cleaner.
- [Telemetry](/sonarqube-server/instance-administration/system-functions/telemetry.md): SonarQube Server sends anonymized telemetry data to Sonar daily. No personally identifiable information is sent.
- [PDF reports](/sonarqube-server/instance-administration/system-functions/pdf-reports.md): As a system administrator, you can change the PDF report subscription frequency for projects, applications, and portfolios.
- [AI features](/sonarqube-server/instance-administration/ai-features.md): Setting up AI features at the instance level in SonarQube Server.
- [Overview](/sonarqube-server/instance-administration/ai-features/overview.md): A quick summary of SonarQube Server’s AI features that can be managed by an instance administrator.
- [Autodetect AI code](/sonarqube-server/instance-administration/ai-features/autodetect-ai-code.md): Autodetect AI-Generated Code is turned on by default, but your DevOps provider must give the appropriate permissions to allow communication with SonarQube.
- [Permissions for AI autodetect](/sonarqube-server/instance-administration/ai-features/permissions-for-ai-autodetect.md): Setting up AI autodetection in SonarQube Server requires that a DevOps platform administrator set the correct permission level in your AI-powered web service.
- [Enable AI CodeFix](/sonarqube-server/instance-administration/ai-features/enable-ai-codefix.md): Sonar’s AI CodeFix can suggest fixes for a select set of rules in Java, JavaScript, TypeScript, Python, C#, and C++.
- [Security](/sonarqube-server/instance-administration/security.md): Security-relevant setups.
- [User accounts](/sonarqube-server/instance-administration/security/user-accounts.md): Security-relevant considerations and setups regarding user accounts.
- [User sessions](/sonarqube-server/instance-administration/security/user-sessions.md): A user’s session will automatically end after a period of inactivity. This is a security measure to prevent unauthorized access to sensitive data.
- [Tokens](/sonarqube-server/instance-administration/security/administering-tokens.md): Generating and revoking user tokens in SonarQube Server.
- [Sensitive settings](/sonarqube-server/instance-administration/security/encrypting-settings.md): Encrypting SonarQube system properties.
- [Audit logs](/sonarqube-server/instance-administration/security/audit-logs.md): Managing the trail of your SonarQube audit logs.
- [User management](/sonarqube-server/instance-administration/user-management.md): Managing your user accounts in SonarQube Server.
- [Introduction to user management](/sonarqube-server/instance-administration/user-management/introduction.md): The User management section is directed at the System Administrator.
- [Viewing user accounts](/sonarqube-server/instance-administration/user-management/viewing-users.md): Retrieving and viewing user accounts in SonarQube Server.
- [Managing groups](/sonarqube-server/instance-administration/user-management/user-groups.md): This page describes the user group concept in SonarQube Server and how to create and populate them.
- [Managing permissions](/sonarqube-server/instance-administration/user-management/user-permissions.md): As a System Administrator, you can grant users and groups global permissions and you can manage the default project permissions.
- [Associating with SCM account](/sonarqube-server/instance-administration/user-management/updating-scm-details.md): As a System Administrator, you can explicitly associate an SCM (Source Control Management) account with a SonarQube Server user account.
- [Creating users manually](/sonarqube-server/instance-administration/user-management/creating-users.md): Creating user accounts manually in SonarQube Server.
- [Deactivating users](/sonarqube-server/instance-administration/user-management/deactivating-users.md): When you deactivate a user in SonarQube Server, any tokens associated with the user are revoked.
- [Changing user password](/sonarqube-server/instance-administration/user-management/changing-user-password.md): System Administrator can change the password of a user whose SonarQube Server account is not tied to a third-party identity provider.
- [Authentication and provisioning](/sonarqube-server/instance-administration/authentication.md): Setting up the user authentication and provisioning in your SonarQube Server instance.
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
- [License administration](/sonarqube-server/instance-administration/license-administration.md): Learn how to retrieve, setup, stage and request new SonarQube Server licenses.
- [Server ID based license key](/sonarqube-server/instance-administration/license-administration/server-id-based-license-key.md): Learn how to retrieve, setup, stage and request your server ID based license key.
- [Online license management](/sonarqube-server/instance-administration/license-administration/online-license-management.md): Learn how to retrieve, setup, stage and request new SonarQube Server license.
- [UI customization](/sonarqube-server/instance-administration/ui-customization.md): Customizing your instance's look and feel and displaying custom messages.
- [Look and feel](/sonarqube-server/instance-administration/ui-customization/look-and-feel.md): You can set your own home logo and use a Gravatar avatar.
- [Custom messages](/sonarqube-server/instance-administration/ui-customization/custom-messages.md): Admins can configure custom messages that will be displayed in the SonarQube Server UI.
- [System info and server ID](/sonarqube-server/instance-administration/system-info-and-server-id.md): This page describes how to gather detailed information about your SonarQube Server instance.
- [Inactive projects](/sonarqube-server/instance-administration/inactive-projects.md): Managing the inactive projects in your SonarQube Server instance.
- [Jira Cloud integration](/sonarqube-server/instance-administration/jira-integration.md): Before you can create Jira work items in SonarQube Server, you need to set up your Jira Cloud integration on the SonarQube Server instance and project levels
