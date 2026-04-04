# Source: https://docs.sonarsource.com/sonarqube-community-build/server-update-and-maintenance/update/other-procedures.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/setup-and-upgrade/upgrade-the-server/other-procedures.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/setup-and-upgrade/upgrade-the-server/other-procedures.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/setup-and-upgrade/upgrade-the-server/other-procedures.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/server-upgrade-and-maintenance/upgrade/upgrade-the-server/other-procedures.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/server-upgrade-and-maintenance/upgrade/upgrade-the-server/other-procedures.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/server-update-and-maintenance/upgrade/other-procedures.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-update-and-maintenance/upgrade/other-procedures.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-update-and-maintenance/update/other-procedures.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/update/other-procedures.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-update-and-maintenance/update/other-procedures.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-update-and-maintenance/update/other-procedures.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/update/other-procedures.md

# Other migration-related tasks

### Reverting to the previous version <a href="#revert-previous" id="revert-previous"></a>

If you need to revert to the previous version of SonarQube Server, the high-level rollback procedure for all deployments is as follows:

1. Shut down your SonarQube Server instance or cluster.
2. Roll back your database to the backup you took before starting the update.
3. Switch back to the previous version of your SonarQube Server installation.
4. Start your SonarQube Server instance or cluster.

### Migrating the SonarQube Server database to another vendor <a href="#another-db-vendor" id="another-db-vendor"></a>

To migrate your SonarQube Server database from one database vendor to another, use the [sonarqube-db-copy-tool](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/maintenance/sonarqube-db-copy-tool "mention").

### Moving from a ZIP file installation to a Docker installation <a href="#from-zip-to-docker" id="from-zip-to-docker"></a>

To move from a ZIP file installation to a Docker installation:

1. Configure your Docker container to point to your existing database.
2. Shut down your ZIP instance.
3. [set-up-and-start-container](https://docs.sonarsource.com/sonarqube-server/server-installation/from-docker-image/set-up-and-start-container "mention").

### Updating a plugin <a href="#upgrading-pluging" id="upgrading-pluging"></a>

You need to manually install plugins when using SonarQube Server, you cannot use the SonarQube Marketplace. See [install-a-plugin](https://docs.sonarsource.com/sonarqube-server/server-installation/plugins/install-a-plugin "mention") for more information.

### Downgrading to SonarQube Community Build <a href="#downgrading-to-community-build" id="downgrading-to-community-build"></a>

Ensure the target SonarQube Community Build version was released after the source SonarQube Server version. See [Releases - Sonar Community](https://community.sonarsource.com/c/sq/releases/24) for release dates of SonarQube Community Build and SonarQube Server. In most cases, migrating to the latest version of the target product will suffice.

However, if you are using the latest version of SonarQube Server, you may need to wait for the next version of SonarQube Community Build accordingly, typically available within a month.

Once the target version is confirmed, proceed with the standard update procedure.

{% hint style="info" %}
To update your SonarQube Community Build to SonarQube Server, see [updating-from-sonarqube-community-build](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/update/updating-from-sonarqube-community-build "mention").
{% endhint %}

### Moving between SonarQube Server editions <a href="#upgrading-or-downgrading-between-sonarqube-server-editions" id="upgrading-or-downgrading-between-sonarqube-server-editions"></a>

If you’re moving to a different SonarQube Server edition (Data Center Edition, Enterprise Edition, or Developer Edition) with the same version, the steps are the same as described in [roadmap](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/update/roadmap "mention") without the need to browse to `http://yourSonarQubeServerURL/setup` or reanalyze your projects.
