# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/server-update-and-maintenance/upgrade/pre-upgrade-steps.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-update-and-maintenance/upgrade/pre-upgrade-steps.md

# Pre-update steps

### Before you start <a href="#before-you-start" id="before-you-start"></a>

Consider the following before starting your upgdate:

* SonarQube Server releases come with specific recommendations for updating from the previous versions. You should first read the [#upgrade-notes](https://docs.sonarsource.com/sonarqube-server/2025.3/release-notes#upgrade-notes "mention") for each version between your current version and the target version.
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

* [release-cycle-model](https://docs.sonarsource.com/sonarqube-server/2025.3/server-update-and-maintenance/upgrade/release-cycle-model "mention")
* [determine-path](https://docs.sonarsource.com/sonarqube-server/2025.3/server-update-and-maintenance/upgrade/determine-path "mention")
* [upgrade](https://docs.sonarsource.com/sonarqube-server/2025.3/server-update-and-maintenance/upgrade/upgrade "mention")
* [post-upgrade-steps](https://docs.sonarsource.com/sonarqube-server/2025.3/server-update-and-maintenance/upgrade/post-upgrade-steps "mention")
