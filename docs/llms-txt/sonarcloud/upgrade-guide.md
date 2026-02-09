# Source: https://docs.sonarsource.com/sonarqube-server/9.8/setup-and-upgrade/upgrade-the-server/upgrade-guide.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/setup-and-upgrade/upgrade-the-server/upgrade-guide.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/setup-and-upgrade/upgrade-the-server/upgrade-guide.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/setup-and-upgrade/upgrade-the-server/upgrade-guide.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/setup-and-upgrade/upgrade-the-server/upgrade-guide.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/setup-and-upgrade/upgrade-the-server/upgrade-guide.md

# Upgrade guide

This is a generic guide for upgrading across versions of SonarQube. Carefully read the [release-upgrade-notes](https://docs.sonarsource.com/sonarqube-server/10.3/setup-and-upgrade/release-upgrade-notes "mention") of your target version and of any intermediate version(s).

Before upgrading, we recommend practicing your upgrade on a staging environment that’s as similar to your production environment as possible. For more on this and other important upgrading concepts, read through the [before-you-upgrade](https://docs.sonarsource.com/sonarqube-server/10.3/setup-and-upgrade/upgrade-the-server/before-you-upgrade "mention") page.

If you need to upgrade a cluster, see [configure-and-operate-a-cluster](https://docs.sonarsource.com/sonarqube-server/10.3/setup-and-upgrade/configure-and-operate-a-cluster "mention").

{% hint style="warning" %}
Before upgrading, back up your SonarQube database. Upgrade problems are rare, but you’ll want the backup if anything does happen.
{% endhint %}

### Database disk usage recommendations <a href="#database-disk-usage-recommendations" id="database-disk-usage-recommendations"></a>

During your upgrade, tables may be duplicated to speed up the migration process. This could cause your database disk usage to temporarily increase to as much as double the normal usage. Because of this, we recommend that your database disk usage is below 50% before starting a migration.

### Upgrading instructions <a href="#upgrading-instructions" id="upgrading-instructions"></a>

You can upgrade your SonarQube instance using the ZIP file, Docker image, or Helm Chart. To expand the upgrading instructions, click the option below that corresponds to your setup.

{% hint style="info" %}
After an upgrade, some projects might be temporarily greyed out in the UI. This is because SonarQube is reindexing your projects, and they become available in the UI as they are reindexed. Note that you can already run analyses on these projects. See [reindexing](https://docs.sonarsource.com/sonarqube-server/10.3/instance-administration/reindexing "mention") for more information.
{% endhint %}

<details>

<summary>Upgrading from the ZIP file</summary>

Before you upgrade, make sure you know how to [installing-sonarqube-from-zip-file](https://docs.sonarsource.com/sonarqube-server/10.3/setup-and-upgrade/install-the-server/installing-sonarqube-from-zip-file "mention") from the ZIP file and check that your environment [prerequisites-and-overview](https://docs.sonarsource.com/sonarqube-server/10.3/requirements/prerequisites-and-overview "mention") of the version you’re upgrading to.

**To upgrade from the ZIP file:**

1. Download and unzip the SonarQube distribution of your edition in a fresh directory, let’s say `<NEW_SONARQUBE_HOME>`
2. If you’re using third-party plugins, Manually install plugins that are compatible with your version of SonarQube. Use the [plugin-version-matrix](https://docs.sonarsource.com/sonarqube-server/10.3/instance-administration/plugin-version-matrix "mention") to ensure that the versions you install are compatible with your server version. Simply copying plugins from the old server to the new is not recommended; incompatible or duplicate plugins could cause startup errors. Analysis of all languages provided by your edition is available by default without plugins.
3. Update the contents of `sonar.properties` file (in `<NEW_SONARQUBE_HOME>/conf`) with the settings in the `<OLD_SONARQUBE_HOME>/conf` directory (web server URL, database, ldap settings, etc.). Do not copy-paste the old files. If you are using the Oracle DB, copy its JDBC driver into `<NEW_SONARQUBE_HOME>/extensions/jdbc-driver/oracle`
4. Stop your old SonarQube Server
5. Start your new SonarQube Server
6. Browse to `http://yourSonarQubeServerURL/setup` and follow the setup instructions
7. Reanalyze your projects to get fresh data.

</details>

<details>

<summary>Upgrading from the Docker image</summary>

{% hint style="info" %}
If you’re upgrading with an Oracle database or you’re using plugins, you can reuse your extensions volume from the previous version to avoid moving plugins or drivers. Use the [Broken link](https://docs.sonarsource.com/sonarqube-server/10.3/setup-and-upgrade/upgrade-the-server/broken-reference "mention") to ensure that your plugins are compatible with your version. Analysis of all languages provided by your edition is available by default without plugins.
{% endhint %}

**To upgrade SonarQube using the Docker image:**

1. Stop and remove the existing SonarQube container (a restart from the UI is not enough as the environment variables are only evaluated during the first run, not during a restart):

```css-79elbk
$ docker stop <container_id>
$ docker rm <container_id>
```

2\. Run Docker

```css-79elbk
$> docker run -d --name sonarqube \
    -p 9000:9000 \
    -e SONAR_JDBC_URL=... \
    -e SONAR_JDBC_USERNAME=... \
    -e SONAR_JDBC_PASSWORD=... \
    -v sonarqube_data:/opt/sonarqube/data \
    -v sonarqube_extensions:/opt/sonarqube/extensions \
    -v sonarqube_logs:/opt/sonarqube/logs \
    <image_name>
```

3\. Go to `http://yourSonarQubeServerURL/setup` and follow the setup instructions.

4\. Reanalyze your projects to get fresh data.

**From 8.9.x LTS to 9.9.x LTS**

Please note that the `lts` tag on Docker images is replaced with every new LTS release. If you want to avoid an automatic major upgrade, we recommend using the corresponding `9.9-<edition>` tag instead of relying on the `lts-<edition>` tag.

{% hint style="info" %}

* Unless you intend to delete the database and start new when running your image, be careful not to use `-v` to `docker-compose down` and, be careful when running commands like `docker system prune` or `docker volume prune`; regardless if you use an `external: true` parameter, your database volumes will not persist beyond the initial startup and shutdown of SonarQube.
  {% endhint %}

</details>

<details>

<summary>Upgrading from the Helm chart</summary>

{% hint style="info" %}
If you’re upgrading with an Oracle database or you’re using plugins, you can reuse your extensions PVC from the previous version to avoid moving plugins or drivers. Use the [plugin-version-matrix](https://docs.sonarsource.com/sonarqube-server/10.3/instance-administration/plugin-version-matrix "mention") to ensure that your plugins are compatible with your version. Analysis of all languages provided by your edition is available by default without plugins.
{% endhint %}

**To upgrade SonarQube using our official Helm Chart:**

1. Change the SonarQube version on your `values.yaml`.
2. Redeploy SonarQube with the same helm chart:

```css-79elbk
helm upgrade --install -f values.yaml -n <your namespace> <your release name> <path to sonarqube helm chart>
```

3\. If you’re upgrading a Data Center Edition: after SonarQube search pods are running and ready, only one application (app) replica will be running and ready. You can confirm that it’s because of the ongoing upgrade by inspecting the logs of the pod for this text: `The database must be manually upgraded. Please backup the database and browse /setup`

4\. Go to `http://yourSonarQubeServerURL/setup` and follow the setup instructions.

5\. Reanalyze your projects to get fresh data.

{% hint style="warning" %}
Please verify that any custom configurations or custom `values.yaml` files contain *only parameters that are still compatible with the targeted chart*, and adjust them if needed. Some default parameters may have changed between versions of the chart.
{% endhint %}

**From 8.9.x LTS to 9.9.x LTS**

To install SonarQube 9.9 LTS, use the [sonarqube](https://artifacthub.io/packages/helm/sonarqube/sonarqube) Helm chart. The [sonarqube-lts](https://artifacthub.io/packages/helm/sonarqube/sonarqube-lts) Helm chart is no longer maintained and cannot be used to install the new LTS.

* For SonarQube 9.9 LTS Community, Developer, and Enterprise Editions, the [Helm chart ](https://artifacthub.io/packages/helm/sonarqube/sonarqube)version to use is `8.x.x` . See [`sonarqube` ArtifactHub](https://artifacthub.io/packages/helm/sonarqube/sonarqube#installing-the-sonarqube-9-9-lts-chart) for more information.
* For SonarQube 9.9 LTS Data Center Edition, the [Helm chart ](https://artifacthub.io/packages/helm/sonarqube/sonarqube)version to use is `7.x.x` . See [`sonarqube-dce` ArtifactHub](https://artifacthub.io/packages/helm/sonarqube/sonarqube-dce#installing-the-sonarqube-9-9-lts-chart) for more information.

Remember to verify that any custom configurations or custom `values.yaml` files contain *only parameters that are still compatible with the targeted chart*, as mentioned in the warning above.

As SonarQube only requires to persist the database, the general upgrade process will consist of uninstalling your instance before installing the new LTS.

If you are using an external database, you don’t have any persistent data inside kubernetes. Therefore, there is no action required.

Instead, if you rely on the embedded PostgreSQL chart (**not recommended**), uninstalling the chart will keep the PVC alive. The PVC can then be reused either:

* by specifying `postgresql.existingClaim` in the `values.yaml` file
* by not changing parameter values, but making sure you install the new chart in the same namespace (auto-generated name will be the same).

</details>

### Reverting to the previous version <a href="#reverting-to-the-previous-version" id="reverting-to-the-previous-version"></a>

If you need to revert to the previous version of SonarQube, the high-level rollback procedure for all deployments is as follows:

1. Shutdown your SonarQube instance or cluster.
2. Roll back your database to the backup you took before starting the upgrade.
3. Switch back to the previous version of your SonarQube installation.
4. Start your SonarQube instance or cluster.

### Changing your edition <a href="#changing-your-edition" id="changing-your-edition"></a>

You can move to a different SonarQube edition (for example, moving from Community Edition to a commercial edition) while you’re upgrading your version. Just use the appropriate edition file or Docker image tag in the upgrade instructions above.

If you want to move to a different edition without upgrading your SonarQube version, the steps are exactly the same as in the upgrading instructions above without needing to navigate to `http://yourSonarQubeServerURL/setup` or reanalyze your projects.

### Migrating from a ZIP file instance to a Docker instance <a href="#migrating-from-zip-file-instance-to-docker" id="migrating-from-zip-file-instance-to-docker"></a>

To migrate from the ZIP file to Docker:

1. Configure your Docker instance to point to your existing database.
2. Shut down your ZIP instance.
3. Start your Docker instance.

### Additional steps and information <a href="#additional-steps-and-information" id="additional-steps-and-information"></a>

#### Oracle clean-up <a href="#oracle-cleanup" id="oracle-cleanup"></a>

There’s an additional step you may want to perform if you’re using Oracle. On Oracle, the database columns to be dropped are now marked as UNUSED and are not physically dropped anymore. To reclaim disk space, Oracle administrators must drop these unused columns manually. The SQL request is `ALTER TABLE foo DROP UNUSED COLUMNS`. The relevant tables are listed in the system table `all_unused_col_tabs`.

#### PostgreSQL clean-up <a href="#postgresql-cleanup" id="postgresql-cleanup"></a>

Once you’ve finished a technical upgrade, **you should rebuild database indexes and refresh database statistics** before starting SonarQube and reanalyzing your projects.

For PostgreSQL, that means executing three operations:

1. `VACUUM FULL`
2. `REINDEX DATABASE <db>`
3. `ANALYZE`

According to the PostgreSQL documentation:

```css-79elbk
In normal PostgreSQL operation, tuples that are deleted or obsoleted by an update are not physically removed from their table; they remain present until a VACUUM is done.
```

#### Scanner update <a href="#scanner-update" id="scanner-update"></a>

When upgrading SonarQube, you should also make sure you’re using the latest versions of the SonarQube scanners to take advantage of features and fixes on the scanner side. Please check the documentation pages of the scanners you use for the most recent version compatible with SonarQube and your build tools.

See also this section for [overview](https://docs.sonarsource.com/sonarqube-server/10.3/user-guide/rules/overview "mention").

#### Microsoft SQL Server and Integrated Authentication <a href="#microsoft-sql-server-and-integrated-authentication" id="microsoft-sql-server-and-integrated-authentication"></a>

If you use Microsoft SQL Server with Integrated Authentication, make sure that you’re using a supported version of the [Microsoft SQL JDBC Driver package](https://learn.microsoft.com/en-us/sql/connect/jdbc/release-notes-for-the-jdbc-driver). The minimum supported version is the one mentioned on the [installing-the-database](https://docs.sonarsource.com/sonarqube-server/10.3/setup-and-upgrade/install-the-server/installing-the-database "mention") page.

### SonarQube as Linux or Windows service <a href="#sonarqube-as-linux-or-windows-service" id="sonarqube-as-linux-or-windows-service"></a>

If you use an external configuration, such as a script or Windows Service to control your server, you’ll need to update it to point to `<NEW_SONARQUBE_HOME>`.

* For Linux it depends how you implemented the service
* For Windows you can update your service by running:

```css-79elbk
> sc delete SonarQube
> $NEW_SONARQUBE_HOME\bin\windows-x86-64\SonarService.bat install
```

### Release upgrade notes <a href="#release-upgrade-notes" id="release-upgrade-notes"></a>

Usually, SonarQube releases come with some specific recommendations for upgrading from the previous version. You should read the upgrade notes for each version between your current version and the target version.
