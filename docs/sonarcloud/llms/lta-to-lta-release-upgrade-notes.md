# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/release-notes-and-notices/lta-to-lta-release-upgrade-notes.md

# LTA to LTA release update notes

Upgrade notes contain information on breaking changes and important updates to be aware of before upgrading.

These upgrade notes are intended for users who are directly upgrading SonarQube Server from 9.9 LTA to 2025.1 LTA. Just upgrading a few minor versions? Refer to the regular [release-upgrade-notes](https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/release-notes-and-notices/release-upgrade-notes "mention").

For a list of new features since the last LTA, see [lta-to-lta-release-notes](https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/release-notes-and-notices/lta-to-lta-release-notes "mention"). For a list of new features in 2025.1 LTA only, see [release-notes](https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/release-notes-and-notices/release-notes "mention").

### Authentication <a href="#authentication" id="authentication"></a>

**SAML configuration update required (2025.1)**

When configuring SAML on your SonarQube Server instance with assertion encryption, response signature must be enforced. You might need to update your SAML configuration:

* If you use SAML with Microsoft Entra, make sure you sign the response by selecting **Sign SAML response** or **Sign SAML response and assertion** as the sign-in response. See **Step 2 > If you use encryption, enforce response signature** in [optional-security-features](https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/authentication/saml/ms-entra-id/optional-security-features "mention").
* If you use SAML with PingID, make sure you sign the response by selecting **Sign Response** or **Sign Assertion & Response** as the sign-in response. See **Step 2 > To enable the encryption of SAML assertions** in [optional-security-features](https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/authentication/saml/ping-identity/optional-security-features "mention").

In addition, the assertion decryption now requires that you store also the public key certificate in SonarQube Server (not only the private key). Make sure the certificate is stored in SonarQube as follows:

1. In SonarQube Community Build, go to **Administration > Configuration > General Settings > Authentication > SAML**.
2. In **SAML Configuration > SAML**, select **Edit**. The **Edit SAML configuration** dialog opens.
3. In **Service provider certificate**, enter the certificate.

**Updated GitLab automatic provisioning feature (10.7)**

Automatic user and group provisioning with GitLab now includes permission synchronization, which automatically synchronizes project visibility. To prevent unwanted updates to project permissions and project visibility, upgrading SonarQube will suspend automatic provisioning until you confirm the choice of provisioning method in the authentication settings.

For more information, see the [setting-up](https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/authentication/gitlab/setting-up "mention") page.

**Updated GitHub automatic provisioning feature (10.2)**

Automatic user and group provisioning with GitHub now includes permission synchronization, which automatically synchronizes project visibility:

* To prevent unwanted updates to project permissions and project visibility, upgrading SonarQube will suspend automatic provisioning until you confirm the choice of provisioning method in the authentication settings.
* The GitHub app requires new permissions to be added and approved.

For more information, see the [github](https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/authentication/github "mention") page.

**SCIM provisioning requires configuration (10.0)**

SCIM provisioning for SAML authentication evolves for a tightened synchronization of users and groups. To use the updated set of user and group SCIM provisioning features, see [overview](https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/authentication/overview "mention").

Without action on your part, upon upgrading, already assigned users are not deleted from SonarQube, but they are no longer bound to your IdP. You’ll need to enable SCIM again in SonarQube and adjust your IdP settings. See [overview](https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/authentication/saml/scim/overview "mention") of SCIM provisioning for more information.

### Analysis <a href="#analysis" id="analysis"></a>

**SonarScanner for Maven recommended command updated**

The recommended command to run the [SonarScanner for Maven](https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/scanners/sonarscanner-for-maven) was updated. You might need to update your configuration. See the full explanation below.

<details>

<summary>Full explanation</summary>

A Maven project is configured using a `pom.xml` file. In this file, you can configure the `sonar-maven-plugin` version and properties:

```
<build>
  <pluginManagement>
    <plugins>
      <plugin>
        <groupId>org.sonarsource.scanner.maven</groupId>
        <artifactId>sonar-maven-plugin</artifactId>
        <version>3.7.0.1746</version>
        <!-- your configuration ... -->
      </plugin>
    </plugins>
  </pluginManagement>
</build>
```

When `sonar-maven-plugin` is defined in the `pom.xml` file, it is safe and has the same effect to execute the two following commands:

`mvn sonar:sonar`

or

`mvn org.sonarsource.scanner.maven:sonar-maven-plugin:sonar`

But if you *don't declare* `sonar-maven-plugin` in your `pom.xml`, file, the two above commands are not recommended.

When Maven sees `mvn sonar:sonar`, it tries to find a plugin called `sonar` in the `pom.xml` hierarchy and fails. Then, Maven will try to download a plugin called `org.codehaus.mojo:sonar-maven-plugin` and succeed. It is a legacy mechanism that Maven still uses, so you don't have to write in full `mvn org.codehaus.mojo:sonar-maven-plugin:sonar`.

The Codehaus services officially ended around May 2015, so Sonar cannot deploy the new version of the scanner to `org.codehaus.mojo`. This is why a new group ID `org.sonarsource.scanner.maven` was created a little later.

Note that when Maven sees `mvn org.sonarsource.scanner.maven:sonar-maven-plugin:sonar` and no `sonar-maven-plugin` is set in your `pom.xml` , Maven downloads the latest version. It means that on a random day, the analysis may change because of a new scanner version. To prevent unintentional changes, we recommend explicitly setting the version. For example: `mvn org.sonarsource.scanner.maven:sonar-maven-plugin:5.2.0.4988:sonar`.

</details>

**Updated built-in Quality Profiles**

The built-in Quality Profiles for each language have been updated, meaning rules may have been added, changed, deprecated or dropped. If you are using or extending any of the "Sonar way" built-in Quality Profiles, make sure to check their Changelog to see what has changed.

**Cognitive complexity calculation updated for Javascript and Typescript (10.5)**

If you analyze Javascript and Typescript projects, note that we’ve updated how cognitive complexity is calculated. Notably, nested function complexity is no longer added to the parent. This will translate as a drop in the metric for some users.

**End of support of Node.js 16 in the scanner environment (10.5)**

Node.js 16 is no longer supported as a scanner runtime environment. If you’re using a custom Node.js installation, we recommend the latest [LTS version](https://nodejs.org/en/about/previous-releases), currently v20.

**JavaScript/TypeScript/CSS configuration (10.4)**

A minimum of 4GB memory is now recommended, use `sonar.javascript.node.maxspace` configuration if you encounter memory issues. Also, file encoding errors will now cause an analysis failure, use `sonar.sourceEncoding=UTF-8` if you encounter problems. See [javascript-typescript-css](https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/languages/javascript-typescript-css "mention") for more information.

**Node.js is no longer a requirement for analysis (10.4)**

In most cases, installing Node.js in the environment where you’re running analysis is no longer a requirement. See [javascript-typescript-css](https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/languages/javascript-typescript-css "mention") for more details.

**End of support of Java 11 as scanner environment (10.4)**

Java 11 is no longer supported as a scanner runtime environment. The minimum required version is Java 17. The impact of this change should be minimal if you use a scanner that supports JRE auto-provisioning. See [general-requirements](https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/scanners/scanner-environment/general-requirements "mention") for more details.

**SonarScanner for .NET compatibility (10.4)**

Starting with SonarQube 10.4, analysis of .NET projects requires [SonarScanner for .NET 5.14+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/5.14.0.78575).

**End of support of MSBuild 14 (10.4)**

MSBuild 14 is no longer supported for scanning .NET code. ​​MSBuild 15 is deprecated and support will be removed in a future version. We recommend using MSBuild 16 as a minimal version.

To know which Web API endpoints and parameters are deprecated after an upgrade, see [api-deprecation](https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/monitoring/api-deprecation "mention").

**Dropping support for NET Framework < 4.6.2 (10.1)**

The minimum supported .NET Framework version is 4.6.2. Support for earlier versions has been dropped. If you’re running an earlier version, you’ll need to upgrade your build environment wherever your analysis is run. See [this release note](https://github.com/SonarSource/sonar-dotnet/releases/tag/9.0.0.68202) for more information.

**Projects displaying modules are no longer supported (10.0)**

The concept of modules was removed in v7.6. SonarQube no longer migrates the structure of projects still displaying modules. Make sure you re-analyze these projects before upgrading to SonarQube 10.0.

### Operations <a href="#operations" id="operations"></a>

**Instance mode feature (10.8)**

Your SonarQube Server instance has two modes to choose from: [standard-experience](https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/analysis-functions/instance-mode/standard-experience "mention") and [mqr-mode](https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/analysis-functions/instance-mode/mqr-mode "mention"). Upon upgrading, existing SonarQube Server 10.1 and earlier are configured with the Standard Experience by default whereas SonarQube Server 10.2 and later are configured with MQR mode.

For details on switching modes, see the [changing-modes](https://docs.sonarsource.com/sonarqube-server/2025.1/user-guide/code-metrics/changing-modes "mention") page.

**Disable the confidential header in portfolio PDF reports (10.7)**

Admin users have a new toggle in the Administration -> Governance -> Portfolio PDF Reports section, allowing them to dynamically enable or disable the "Confidential" header.

For details, see the [managing-portfolios](https://docs.sonarsource.com/sonarqube-server/2025.1/project-administration/managing-portfolios "mention") page.

**Project overview update in MQR mode (10.4)**

If you use MQR Mode, note that issue counts on the overall code of projects reflect the [software-qualities](https://docs.sonarsource.com/sonarqube-server/2025.1/user-guide/rules/software-qualities "mention").

These counts will be displayed when you re-analyze your projects.

**Microsoft SQL Server and Integrated Authentication (10.8)**

If you use Microsoft SQL Server with Integrated Authentication, note that the minimum supported version of the [Microsoft SQL JDBC Driver package](https://learn.microsoft.com/en-us/sql/connect/jdbc/release-notes-for-the-jdbc-driver) has been updated to 12.8.1. See [installing-the-database](https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/install-the-server/installing-the-database "mention") for more information.

**Elasticsearch system call filters required (10.6)**

SonarQube uses Elasticsearch 8.0. System call filters are now required (see the [Elastic docs](https://www.elastic.co/guide/en/elastic-stack/8.0/elasticsearch-breaking-changes.html) for more information). If you disabled these filters, you’ll need to adjust your configuration before starting the server.

**seccomp filter required on kernel (10.0)**

The version of Elasticsearch has been updated and now requires a kernel with seccomp enabled. Make sure that seccomp is available on your kernel. See /pre-installation steps [linux](https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/pre-installation/linux "mention") for more information.

### Plugins <a href="#plugins" id="plugins"></a>

**Updates to custom plugins required (10.5)**

For a faster analysis, SonarQube now optimizes the loading of analyzers by default. To avoid dependency errors, you’ll need to update the configuration of your custom plugins. See [plugin-basics](https://docs.sonarsource.com/sonarqube-server/2025.1/extension-guide/developing-a-plugin/plugin-basics "mention") for more information. Also, if you use third-party plugins, make sure to use the latest ones compatible with this feature.

**Updated security policy for page extensions (10.0)**

To improve security, pages added to the UI by plugins can no longer include inline scripts. If you use this feature, you might need to update your plugins. See [adding-pages-to-the-webapp](https://docs.sonarsource.com/sonarqube-server/2025.1/extension-guide/developing-a-plugin/adding-pages-to-the-webapp "mention") for more information.

### Clean as You Code <a href="#clean-as-you-code" id="clean-as-you-code"></a>

**Updated Sonar Way quality gate condition (10.3)**

The Sonar way quality gate now uses a zero issue condition on new code. If you’re upgrading from version 10.2 or earlier, note that your Sonar way quality gate is preserved as "Sonar way (legacy)" upon upgrading and the associated projects are moved to that custom quality gate. We recommend to start using the new Sonar way quality gate at your earliest convenience to keep up with the latest standards.

**Maximum new code definition value automatically adjusted in existing projects (10.2)**

For existing projects, if the value of the Number of days option is set to a higher value than 90 before the upgrade, SonarQube automatically changes it to 90. As a consequence, some issues might move out of the new code. See the [about-new-code](https://docs.sonarsource.com/sonarqube-server/2025.1/user-guide/about-new-code "mention") page for more information.

**Updated options for new code definition (10.2)**

To make them more in line with the Clean as You Code methodology, the following options have been updated for projects:

* Specific analysis: This setup is now available only via the Web API. Automation is required to ensure the value is kept up to date.
* Number of days: The maximum value allowed when setting it up is now 90. It’s recommended to update your existing projects accordingly.

  See the [about-new-code](https://docs.sonarsource.com/sonarqube-server/2025.1/user-guide/about-new-code "mention") page for more information.

### API <a href="#api-updates" id="api-updates"></a>

**API updates (10.7)**

When querying rules or issues, INFO and BLOCKER may appear as statuses at the quality level (i.e. a rule might have a reliability severity of BLOCKER). You can also create rules and issues with these additional severities. See [Web API](https://next.sonarqube.com/sonarqube/web_api) in the help menu of SonarQube Server.

The affected APIs are:

* api/issues/\*
* api/rules/\*
* api/projects/export\_findings
* api/qualityprofiles/compare
* api/qualityprofiles/changelog

### End of support <a href="#end-of-support" id="end-of-support"></a>

**Deprecated web services and parameters removed (10.0)**

The web services and parameters that were deprecated in versions 8.x and 9.x have been removed. For more information, see [the corresponding list](https://sonarsource.atlassian.net/issues/?jql=project%20%3D%20SONAR%20AND%20labels%20%3D%2010.0-removed-webapi) and read the [API deprecation policy](https://community.sonarsource.com/t/api-deprecation-policy-change/57998).
