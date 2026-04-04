# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/server-update-and-maintenance/upgrade/updating-from-sonarqube-community-build.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-update-and-maintenance/update/updating-from-sonarqube-community-build.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/update/updating-from-sonarqube-community-build.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-update-and-maintenance/update/updating-from-sonarqube-community-build.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-update-and-maintenance/update/updating-from-sonarqube-community-build.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/update/updating-from-sonarqube-community-build.md

# Upgrading from SonarQube Community Build

You can use different options to update your SonarQube Community Build to SonarQube Server depending on your situation.

{% hint style="info" %}
If you are moving to Data Center Edition, since all DCE customers are entitled to commercial support, please [get in touch with the team](http://help.sonarsource.com) to help plan your update.
{% endhint %}

### Option 1: Update your existing database <a href="#upgrade-existing-database" id="upgrade-existing-database"></a>

Use this option if:

* You use an external database for your SonarQube data (not the embedded one).
* You regularly analyzed a substantial amount of code.
* Developers interacted with the results, including resolving and/or accepting issues, and maintaining this history is important for you.

Proceed as follows:

1. Determine the update path as follows:\
   Ensure that the target SonarQube Server version was released after your SonarQube Community Build version.\
   In most cases, migrating to the latest version of the target product will suffice. However, if you are using the latest version of SonarQube Community Build, you may need to wait for the next version of SonarQube Server, typically available within a month.
2. [pre-update-steps](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/update/pre-update-steps "mention").
3. Back up the SonarQube Community Build database and ensure it complies with the [installing-the-database](https://docs.sonarsource.com/sonarqube-server/server-installation/installing-the-database "mention") of the target SonarQube Server version. If you want to migrate to another database vendor, see [sonarqube-db-copy-tool](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/maintenance/sonarqube-db-copy-tool "mention").
4. [update](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/update/update "mention").
5. [post-update-steps](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/update/post-update-steps "mention").

### Option 2: Start over with a fresh installation <a href="#fresh-installation" id="fresh-installation"></a>

Use this option if:

* Your SonarQube Community Build instance is far behind the current version so that the length and complexity of the update path may outweigh the benefits of data preservation for you.
* Your SonarQube Community Build instance was sporadically used, managed inconsistently, or isn’t known to represent the projects you plan to analyze and maintain actively.
* You made extensive use of 3rd party plugins that may conflict with Sonar commercial features.
* You created multiple "projects" representing branches of the same individual code repositories and have a messy Project overview as a result. The cleanup may be more burdensome than a fresh start.

Proceed as follows:

1. [introduction](https://docs.sonarsource.com/sonarqube-server/server-installation/introduction "mention").
2. Re-provision your projects through the SonarQube UI or web API, or else give the user account that will be running analysis permission to [user-permissions](https://docs.sonarsource.com/sonarqube-server/instance-administration/user-management/user-permissions "mention").
3. For existing CI/CD pipelines involving Sonar analysis, revisit the URL and [managing-tokens](https://docs.sonarsource.com/sonarqube-server/user-guide/managing-tokens "mention") used to connect to Sonar and update with values appropriate to your new SonarQube Server instance.
4. You may (of course) keep your old SonarQube Community Build instance online during a transitional period until you’re confident all needed project workflows have been migrated to your new SonarQube Server instance

### Option 3: Move your project data to the new instance <a href="#move-to-new-instance" id="move-to-new-instance"></a>

Use this option if:

* You’d like to preserve project analysis and issue history.
* You’d rather revisit all the administrative details, or you built up valuable history while using the embedded non-updateable product database.
* Your administrators are able to dedicate time and effort to a data migration project.
* You’re migrating to Enterprise or Data Center Edition.

Proceed as follows:

1. Install your SonarQube Server’s Enterprise or Data Center Edition as explained above in *Option 2: Start over with a fresh installation*.
2. [project-move](https://docs.sonarsource.com/sonarqube-server/project-administration/maintaining-project/project-move "mention") from your old SonarQube Community Build instance to your new SonarQube Server instance.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [project-move](https://docs.sonarsource.com/sonarqube-server/project-administration/maintaining-project/project-move "mention")
* [other-procedures](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/update/other-procedures "mention")
* [Other migration-related tasks](https://app.gitbook.com/s/bqrfLGeD0Y9vE5l9Le42/server-update-and-maintenance/update/other-procedures "mention")
