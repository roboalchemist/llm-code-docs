# Source: https://docs.sonarsource.com/sonarqube-community-build/server-update-and-maintenance/update/pre-update-steps.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-update-and-maintenance/update/pre-update-steps.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/update/pre-update-steps.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-update-and-maintenance/update/pre-update-steps.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-update-and-maintenance/update/pre-update-steps.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/update/pre-update-steps.md

# Pre-update steps

### Before you start <a href="#before-you-start" id="before-you-start"></a>

Consider the following before starting your upgdate:

* SonarQube Server releases come with specific recommendations for updating from the previous versions. You should first read the [#upgrade-notes](https://docs.sonarsource.com/sonarqube-server/release-notes#upgrade-notes "mention") for each version between your current version and the target version.
* Database disk usage recommendations: During your update, tables may be duplicated to speed up the migration process. This could cause your database disk usage to temporarily increase to as much as double the normal usage. Because of this, we recommend that your database disk usage is below 50% before starting a migration.

### Backup the database <a href="#backup-database" id="backup-database"></a>

First, we *strongly recommend* creating a backup of your database. A backup dump of the database creates a safety net should anything go wrong during the update process. It also allows for testing the update on a testing instance. See Testing the update section below for details.

### Recommended database maintenance steps <a href="#recommended-database-maintenance-steps" id="recommended-database-maintenance-steps"></a>

For large instances, it can be helpful to perform database maintenance tasks like vacuuming, reindexing, and collecting statistics to ensure a smooth and efficient migration. These steps help eliminate table and index bloat, reclaim disk space, and optimize query performance, preventing unnecessary slowdowns during the update process.

Additionally, gathering fresh statistics ensures that the database query planner can make optimal execution choices. Neglecting these optimizations can lead to longer update times, increased disk usage, and potential indexing issues, affecting responsiveness after the migration.

{% hint style="warning" %}
The following commands will lock your database tables so they should be performed during the downtime window. The best effect will be achieved when they are run one after another.
{% endhint %}

#### PostgreSQL <a href="#postgresql" id="postgresql"></a>

```css-79elbk
VACUUM FULL
REINDEX DATABASE <db>
ANALYZE
```

#### Oracle <a href="#oracle" id="oracle"></a>

```css-79elbk
SELECT 'ALTER TABLE ' || OBJECT_NAME || ' MOVE';
  FROM DBA_OBJECTS WHERE OBJECT_TYPE = 'TABLE' AND OWNER = 'SONARQUBE';

BEGIN
  FOR i IN (SELECT INDEX_NAME FROM USER_INDEXES WHERE TABLE_OWNER = 'SONARQUBE') LOOP
    EXECUTE IMMEDIATE 'ALTER INDEX ' || i.INDEX_NAME || ' REBUILD';
  END LOOP;
END;

BEGIN
   DBMS_STATS.GATHER_SCHEMA_STATS('SONARQUBE');
END;
```

#### Microsoft SQL Server <a href="#microsoft-sql-server" id="microsoft-sql-server"></a>

```css-79elbk
EXEC sp_MSforeachtable 'ALTER INDEX ALL ON ? REBUILD';
EXEC sp_MSforeachtable 'UPDATE STATISTICS ? WITH FULLSCAN';
```

### SonarScanner compatibility <a href="#testing-upgrade" id="testing-upgrade"></a>

Check the minimum required SonarScanner version for the SonarQube Server version that you are updating to. See SonarScanners [general-requirements](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/scanner-environment/general-requirements "mention") and individual scanner pages for more details.

<table><thead><tr><th width="213.6746826171875">SonarScanner</th><th>2026.1</th><th width="124.3671875">2025.6</th><th>2025.5</th><th>2025.4</th><th>2025.1</th><th>9.9</th></tr></thead><tbody><tr><td>SonarScanner for CLI</td><td>8.01</td><td>8.01</td><td>7.2</td><td>7.2</td><td>7.0.1</td><td>4.8</td></tr><tr><td>Azure DevOp Extension</td><td>8.0.1</td><td>8.0.0</td><td>7.4.1</td><td>7.3</td><td>7.1.1</td><td>5.11.1</td></tr><tr><td>Jenkins extension</td><td>2.18</td><td>2.18</td><td>2.18</td><td>2.18</td><td>2.17.3</td><td>2.15</td></tr><tr><td>SonarScanner for Maven</td><td>5.5.0.6356</td><td>5.5.0.6356</td><td>5.2.0.4988</td><td>5.1.0.4751</td><td>5.0.0.4389</td><td>3.9.1.2184</td></tr><tr><td>SonarScanner for Gradle</td><td>7.2.2.6593</td><td>7.2.0.6526</td><td>6.3.1.5724</td><td>6.2.0.5505</td><td>6.0.1.5171</td><td>3.5.0.2730</td></tr><tr><td>SonarScanner for .Net</td><td>11.0.0.126294</td><td>11.0.0.126294</td><td>10.4.0.124828</td><td>10.3.0.120579</td><td>9.0.2</td><td>5.11</td></tr><tr><td>SonarScanner for NPM</td><td>4.3.0</td><td>4.3.0</td><td>4.3.0</td><td>4.3.0</td><td>4.2.6</td><td>3.7.0</td></tr><tr><td>SonarScanner for Python</td><td>1.3.0.4086</td><td>1.3.0.4086</td><td>1.1.0.2035</td><td>1.1.0.2035</td><td>0.2.0.520</td><td>N/A</td></tr></tbody></table>

### Testing the update <a href="#testing-upgrade" id="testing-upgrade"></a>

We recommend testing your update to:

* Make sure your infrastructure can run the update and the new version of SonarQube.
* Get an idea of how long the update will take.
* Gain a better understanding of the update process and anticipate what you’ll need to do when performing the actual update.

To test your update:

1. Create a staging environment using a recent backup of your production database.\
   Your staging environment should be as similar to your production instance as possible because the resources and time needed to update depend on what’s stored in your database.
2. Use this staging environment to test the update.
3. Observe how long it takes to back up and restore systems and complete the process.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [release-cycle-model](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/update/release-cycle-model "mention")
* [determine-path](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/update/determine-path "mention")
* [update](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/update/update "mention")
* [post-update-steps](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/update/post-update-steps "mention")
