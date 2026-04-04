# Source: https://docs.sonarsource.com/sonarqube-server/8.9/setup-and-upgrade/lts-to-lts-release-upgrade-notes.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/setup-and-upgrade/lts-to-lts-release-upgrade-notes.md

# LTA to LTA release upgrade notes

These Upgrade Notes are intended for users who are directly upgrading from SonarQube 8.9 LTA. Just upgrading a few minor versions? Refer to the regular [release-upgrade-notes](https://docs.sonarsource.com/sonarqube-server/9.9/setup-and-upgrade/release-upgrade-notes "mention").

### Authentication <a href="#authentication" id="authentication"></a>

**Token expiry (9.6)**\
New tokens can now have an optional expiration date. Expired tokens cannot be used and must be updated. With [Enterprise Edition](https://www.sonarsource.com/plans-and-pricing/enterprise/) and [above](https://www.sonarsource.com/products/sonarqube/downloads/), system administrators can set a maximum lifetime for new tokens. See [security](https://docs.sonarsource.com/sonarqube-server/9.9/instance-administration/security "mention") documentation for more information. ([SONAR-16565](https://sonarsource.atlassian.net/browse/SONAR-16565), [SONAR-16566](https://sonarsource.atlassian.net/browse/SONAR-16566)).

**Project analysis token (9.5)**\
You can now generate tokens of different types and can create a different analysis token for every specific project. The new tokens will include a prefix to help you quickly identify SonarQube tokens and their type. The usage of project analysis tokens is encouraged to limit the access this token has. See [generating-and-using-tokens](https://docs.sonarsource.com/sonarqube-server/9.9/user-guide/user-account/generating-and-using-tokens "mention") documentation for more information. ([SONAR-16260](https://sonarsource.atlassian.net/browse/SONAR-16260)).

**Bitbucket Cloud authentication now built-in (9.2)**\
Support for Bitbucket Cloud authentication is now built-in. If you were using the Bitbucket Cloud authentication plugin before, you need to remove it from SonarQube before upgrading.

SonarQube uses the same settings as the plugin, so you do not need to update them. The Teams restriction has been replaced with the Workspaces restriction and is migrated accordingly.

**Password of old inactive account needs reset (9.4)**\
The support for SHA1 hashed password has been removed. This algorithm was replaced by a stronger hashing algorithm since version 7.2. As a result, local accounts that did not log in since 7.2 will be forced to have their password reset by a SonarQube administrator. Accounts using external authentication such as SAML, LDAP, GitHub authentication, etc., are not impacted. Information about the possibly impacted accounts will appear in the logs during the upgrade. ([SONAR-16204](https://sonarsource.atlassian.net/browse/SONAR-16204)).

### Analysis <a href="#analysis" id="analysis"></a>

**Updated built-in Quality Profiles (9.0-9.9)**

The built-in Quality Profiles for each language have been updated, meaning rules may have been added, changed, deprecated or dropped. If you are using or extending any of the "Sonar way" built-in Quality Profiles, make sure to check their Changelog to see what has changed.

**SonarScanner for .NET compatibility (9.9)**

Incremental analysis of C# / VB.NET in SonarQube requires [sonarscanner-for-dotnet](https://docs.sonarsource.com/sonarqube-server/9.9/analyzing-source-code/scanners/sonarscanner-for-dotnet "mention") 5.11+.

**New main branch names default to "main" (9.8)**\
In the past, newly created projects and applications would have a main branch called "master". This has now been changed to "main". The default value for a newly created main branch name can be changed under **Administration > General > Default main branch name**. See the [branch-analysis](https://docs.sonarsource.com/sonarqube-server/9.9/analyzing-source-code/branches/branch-analysis "mention") documentation for more information. ([SONAR-17524](https://sonarsource.atlassian.net/browse/SONAR-17524))

**JavaScript, TypeScript, and CSS analysis now requires Node.js 14.17+ (9.7)**\
In order to analyze Javascript, Typescript, and CSS code, Node.js 14.17+ must be installed on the machine running the scan. We recommend that you use the latest Node.js LTS, which is currently Node.js 18.

**Secured settings no longer available in web services and on the scanner side (9.1)**\
This change especially affects the analysis of SVN projects but also, possibly, the use of some 3rd-party plugins. Secured settings required to perform the analysis now need to be passed to the scanner as parameters.

**Custom measures feature has been dropped (9.1)**\
The custom measures feature, which was previously deprecated, has been removed. ([SONAR-10762](https://sonarsource.atlassian.net/browse/SONAR-10762)).

**Scanners require Java 11 (9.0)** Java 11 is required for SonarQube scanners. Use of Java 8 is no longer supported. See the documentation on [scanner-environment](https://docs.sonarsource.com/sonarqube-server/9.9/analyzing-source-code/scanner-environment "mention") for more information.

**Reporting Quality Gate status on GitHub branches requires an additional permission (9.0)**\
When working in private GitHub repositories, you need to grant read-only access to the **Contents** permission on the GitHub application that you’re using for SonarQube integration. See the [github-integration](https://docs.sonarsource.com/sonarqube-server/9.9/devops-platform-integration/github-integration "mention") for more information.

### Operations <a href="#operations" id="operations"></a>

**SonarQube server requires Java 17 (9.9)**\
Java 17 is required for SonarQube server. Use of Java 8 and Java 11 is no longer supported. See the documentation on [prerequisites-and-overview](https://docs.sonarsource.com/sonarqube-server/9.9/requirements/prerequisites-and-overview "mention") for more information.

**Microsoft SQL Server with Integrated Authentication changes in configuration (9.9)**

* If you are using Microsoft SQL Server with Integrated Authentication, you will need to replace the `mssql-jdbc_auth` dll file on your `PATH` with `mssql-jdbc_auth-11.2.2.x64.dll` from the [Microsoft SQL JDBC Auth 11.2.2 package](https://github.com/microsoft/mssql-jdbc/releases/download/v11.2.2/mssql-jdbc_auth.zip). See [install-the-server](https://docs.sonarsource.com/sonarqube-server/9.9/setup-and-upgrade/install-the-server "mention") for more information.

**Database support updated (9.9)**

* SonarQube no longer supports Oracle version 12C and 18C.
* Oracle version 21C is now supported.
* SQL Server 2022 is now supported.

**Single Helm chart for Community, Developer, and Enterprise Edition (9.9)**

The [sonarqube-lts](https://artifacthub.io/packages/helm/sonarqube/sonarqube-lts) Helm chart is no longer maintained. Please use the [sonarqube](https://artifacthub.io/packages/helm/sonarqube/sonarqube) Helm chart to install SonarQube 9.9 LTA Community, Developer, or Enterprise Edition. The Data Center Edition is available with the [sonarqube-dce](https://artifacthub.io/packages/helm/sonarqube/sonarqube-dce) Helm chart. Refer to the [upgrade-guide](https://docs.sonarsource.com/sonarqube-server/9.9/setup-and-upgrade/upgrade-the-server/upgrade-guide "mention") for more information.

**Docker images updated (9.9)**

* Recommended [Docker Engine](https://docs.docker.com/engine/) version is 20.10 and later.
* If you use self-signed certificates, you may need to adjust your Docker configuration: the path of the Java installation has changed to `/opt/java/openjdk`. See [install-the-server](https://docs.sonarsource.com/sonarqube-server/9.9/setup-and-upgrade/install-the-server "mention") for more information.
* The deprecated `SONARQUBE_JDBC_USERNAME`, `SONARQUBE_JDBC_PASSWORD`, and `SONARQUBE_JDBC_URL` variables have been removed. See [environment-variables](https://docs.sonarsource.com/sonarqube-server/9.9/setup-and-upgrade/configure-and-operate-a-server/environment-variables "mention") for up-to-date configuration variables.
* The `lts` tag on Docker images is replaced with the new LTA release. If you want to avoid any automatic major upgrades, we recommend using the corresponding `9.9-<edition>` tag instead of `lts-<edition>`.

**Change in the database connection pool (9.7)**\
The database connection pool has been replaced for better performance. The `sonar.jdbc.maxIdle`, `sonar.jdbc.minEvictableIdleTimeMillis` and `sonar.jdbc.timeBetweenEvictionRunsMillis` properties no longer have any effect and should be removed from the configuration. Also, the JMX information that is provided to monitor the connection pool has evolved. See the [monitoring](https://docs.sonarsource.com/sonarqube-server/9.9/instance-administration/monitoring "mention") for more information. ([SONAR-17200](https://sonarsource.atlassian.net/browse/SONAR-17200)).

**Running SonarQube as a Service and Java version selection (9.6)**

* To install, uninstall, start or stop SonarQube as a service on Windows, now you should use `%SONARQUBE-HOME%\bin\windows-x86-64\SonarService.bat install`. See [operating-the-server](https://docs.sonarsource.com/sonarqube-server/9.9/setup-and-upgrade/configure-and-operate-a-server/operating-the-server "mention") and [upgrade-guide](https://docs.sonarsource.com/sonarqube-server/9.9/setup-and-upgrade/upgrade-the-server/upgrade-guide "mention") for more information.
* If there are multiple versions of Java installed on your server, to select specific Java version to be used, set the environment variable `SONAR_JAVA_PATH`. Read more [install-the-server-as-a-cluster](https://docs.sonarsource.com/sonarqube-server/9.9/setup-and-upgrade/install-the-server-as-a-cluster "mention").

**Microsoft SQL Server changes in configuration and Integrated Authentication (9.6)**

* If your Microsoft SQL Server doesn’t support encryption, you will need to add `encrypt=false` to the JDBC URL connection string. ([SONAR-16249](https://sonarsource.atlassian.net/browse/SONAR-16249)).
* If your Microsoft SQL Server requires encryption but you don’t want SonarQube to validate the certificate, you will need to add `trustServerCertificate=true` to the JDBC URL connection string.

### User Interface <a href="#user-interface" id="user-interface"></a>

**Portfolio overview now shows ratings on both New Code and Overall Code (9.3)**\
The Portfolio overview and project breakdown have been redesigned to provide a high-level view on project health according to your New Code definition as well as Overall Code. New Code ratings are shown for Reliability, Security Vulnerabilities, Security Review, and Maintainability. To see these ratings on New Code, Portfolios need to be recomputed after upgrading to 9.3.

Along with this redesign, Portfolios and Applications no longer show users information on projects they don’t have access to, and Application administration has been moved out of the Portfolio administration UI.

**Support for Internet Explorer 11 dropped (9.0)**\
Support for Internet Explorer 11 and other legacy browsers has been dropped. ([SONAR-14387](https://sonarsource.atlassian.net/browse/SONAR-14387)).

### Web/Plugin API <a href="#web-plugin-api" id="web-plugin-api"></a>

**Deprecated WebAPI endpoints and parameters removed (9.1)**\
The WebAPI endpoints and parameters deprecated during the 7.X release cycle have been removed. For a complete list of removed endpoints and parameters see [SONAR-15313](https://sonarsource.atlassian.net/browse/SONAR-15313).

**JavaScript custom rule API removed (9.0)**\
The JavaScript custom rule API, which was previously deprecated, has been removed. Plugins can no longer use this API to implement custom rules. See the [javascript-typescript-css](https://docs.sonarsource.com/sonarqube-server/9.9/analyzing-source-code/languages/javascript-typescript-css "mention") for more information. ([SONAR-14928](https://sonarsource.atlassian.net/browse/SONAR-14928)).

**Deprecated Plugin Java API dropped (9.0)**\
Parts of the Java API for plugins that were deprecated before SonarQube 7.0 have been dropped. You should compile plugins against SonarQube 9.0 to ensure they’re compatible and to check if they’re using a deprecated API that has been dropped. ([SONAR-14925](https://sonarsource.atlassian.net/browse/SONAR-14925), [SONAR-14885](https://sonarsource.atlassian.net/browse/SONAR-14885)).
