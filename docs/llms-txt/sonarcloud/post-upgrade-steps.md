# Source: https://docs.sonarsource.com/sonarqube-server/10.4/setup-and-upgrade/upgrade-the-server/post-upgrade-steps.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/setup-and-upgrade/upgrade-the-server/post-upgrade-steps.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/setup-and-upgrade/upgrade-the-server/post-upgrade-steps.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/server-upgrade-and-maintenance/upgrade/upgrade-the-server/post-upgrade-steps.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/server-upgrade-and-maintenance/upgrade/upgrade-the-server/post-upgrade-steps.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/server-update-and-maintenance/upgrade/post-upgrade-steps.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-update-and-maintenance/upgrade/post-upgrade-steps.md

# Post-update steps

### Post-update checklist <a href="#checklist" id="checklist"></a>

Here’s a list of steps to perform after the update:

* Verify the SonarScanner version (see below).
* For an Oracle database: clean up the database (see below).
* For a PostgreSQL database: clean up the database (see below).
* For a Microsoft SQL database with Windows authentication: verify the JDBC driver version (see below).
* If using an external configuration to control SonarQube Server (through a script or running as a service): update the service to point to the new installation directory (see below).
* If SonarQube Server is running as a service on Linux with SystemD, then you must configure SonarQube Server to run as a service by updating the `sonarqube.service` file.
* If you use the Web API, check at some point the usage of deprecated Web API endpoints and parameters: see [monitoring-api-deprecation](https://docs.sonarsource.com/sonarqube-server/2025.3/server-update-and-maintenance/maintenance/deprecations/monitoring-api-deprecation "mention").

See the sections below for more details on each step.

{% hint style="info" %}
If some projects fail to reindex after the update, see **Reindexing a single project** in [reindexing](https://docs.sonarsource.com/sonarqube-server/2025.3/server-update-and-maintenance/maintenance/reindexing "mention").
{% endhint %}

### Verifying the installed SonarScanner version <a href="#verify-sonarscanner-version" id="verify-sonarscanner-version"></a>

When updating SonarQube Server, you should also make sure you’re using the latest versions of the SonarScanners to take advantage of features and fixes on the scanner side. Please check the documentation pages of the scanners you use for the most recent version compatible with SonarQube Server and your build tools: [sonarscanner-for-maven](https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/scanners/sonarscanner-for-maven "mention"), [sonarscanner-for-gradle](https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/scanners/sonarscanner-for-gradle "mention"), [installing](https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/scanners/dotnet/installing "mention"), [installing](https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/scanners/npm/installing "mention"), [sonarscanner-for-python](https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/scanners/sonarscanner-for-python "mention").

### Cleaning up the Oracle database <a href="#clean-up-oracle-db" id="clean-up-oracle-db"></a>

On Oracle, the database columns to be dropped are marked as UNUSED and are not physically dropped. To reclaim disk space, Oracle administrators must drop these unused columns manually. The SQL request is:

```css-79elbk
ALTER TABLE foo DROP UNUSED COLUMNS
```

The relevant tables are listed in the system table `all_unused_col_tabs`.

### Cleaning up the PostgreSQL database <a href="#clean-up-postgresql" id="clean-up-postgresql"></a>

You can fix the table and index bloating by performing [vacuuming](https://www.postgresql.org/docs/16/routine-vacuuming.html#VACUUM-FOR-SPACE-RECOVERY) in order to reclaim unused disk space. In some specific cases, a [reindex](https://www.postgresql.org/docs/16/routine-reindex.html)is required afterward.

### Verifying the Microsoft SQL JDBC driver version <a href="#verify-jdbc-version" id="verify-jdbc-version"></a>

If you use Microsoft SQL Server with Windows Authentication, make sure that you’re using a supported version of the Microsoft SQL JDBC Driver package. The minimum supported version is the one mentioned on the [installing-the-database](https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/installing-the-database "mention") page.

### Updating a service to point to the new installation directory <a href="#update-external-service" id="update-external-service"></a>

If you use an external configuration, such as a script or Windows Service to control your server, you’ll need to update it to point to the new value of installation directory (\<newSonarQubeHome>).

For Linux it depends how you implemented the service.

For Windows, update your service by running the following commands:

```css-79elbk
sc delete SonarQube
<newSonarQubeHome>\bin\windows-x86-64\SonarService.bat install
```
