# Source: https://docs.sonarsource.com/sonarqube-community-build/server-update-and-maintenance/troubleshooting/elasticsearch.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/server-upgrade-and-maintenance/troubleshooting/elasticsearch.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/server-update-and-maintenance/troubleshooting/elasticsearch.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-update-and-maintenance/troubleshooting/elasticsearch.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-update-and-maintenance/troubleshooting/elasticsearch.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/troubleshooting/elasticsearch.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-update-and-maintenance/troubleshooting/elasticsearch.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-update-and-maintenance/troubleshooting/elasticsearch.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/troubleshooting/elasticsearch.md

# Elasticsearch-related issues

### Recovering from Elasticsearch read-only indices <a href="#recovering-from-elasticsearch-read-only-indices" id="recovering-from-elasticsearch-read-only-indices"></a>

You may encounter issues with Elasticsearch (ES) indices becoming locked in read-only mode. ES requires free disk space available and implements a safety mechanism to prevent the disk from being flooded with index data that:

* **For non-DCE** – locks all indices in read-only mode when the 95% used disk usage watermark is reached.
* **For DCE** – locks all or some indices in read-only mode when one or more node reaches the 95% used disk usage watermark.

ES shows warnings in the logs as soon as disk usage reaches 85% and 90%. At 95% usage and above, indices turning read-only causes errors in the web and compute engine.

Freeing disk space will *not* automatically make the indices return to read-write. To make indices read-write, you also need to:

* **For non-DCE** – restart SonarQube Server.
* **For DCE** – restart *ALL* application nodes (the first application node restarted after all have been stopped will make the indices read-write).

SonarQube Server’s built-in resilience mechanism allows SonarQube Server to eventually recover from the indices being behind data in the DB (this process can take a while).

If you still have inconsistencies, you’ll need to rebuild the indices (this operation can take a long time depending on the number of issues and components):

**non-DCE:**

1. Stop SonarQube Server.
2. Delete the `data/es8` directory.
3. Restart SonarQube Server.

**DCE:**

1. Stop the whole cluster (ES and application nodes).
2. Delete the `data/es8` directory on each ES node.
3. Restart the whole cluster.

See [starting-stopping-cluster](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/starting-stopping-cluster "mention") for more information.

### Failed background tasks during reindexing <a href="#failed-tasks-during-reindexing" id="failed-tasks-during-reindexing"></a>

During Elasticsearch reindexing, you may have failed tasks in your branches or pull requests:

* If you only have a few failed tasks, you can reanalyze your branch or pull request. You may want to use web services to remove branches and pull requests that can’t be reanalyzed because they have been removed from version control.
* If you have many failed tasks, you may want to delete your Elasticsearch directory and reindex again. To do so, see [#forcing-es-reindex](https://docs.sonarsource.com/sonarqube-server/maintenance/reindexing#forcing-es-reindex "mention") for more information.

If background tasks of type **Project Data Reload** fail for a particular project, see the [#reindexing-single-project](https://docs.sonarsource.com/sonarqube-server/maintenance/reindexing#reindexing-single-project "mention") page.

### Exception java.lang.RuntimeException: cannot run elasticsearch as root <a href="#elasticsearch" id="elasticsearch"></a>

SonarQube Server starts an Elasticsearch process, and the same account that is running SonarQube Server itself will be used for the Elasticsearch process. Since Elasticsearch cannot be run as root, that means SonarQube Server can’t be either. You must choose some other, non-root account with which to run SonarQube Server, preferably an account dedicated to the purpose.

### Exception: Failed to allocate closure <a href="#exception-failed-to-allocate-closure" id="exception-failed-to-allocate-closure"></a>

This issue is only relevant to Linux. See [Ensure JNA temporary directory permits executables](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/executable-jna-tmpdir) for detailed information. There are two options to ensure the JNA temp directory matches Elasticsearch’s requirements:

1. Remove `noexec` flag on the `/tmp` or wherever `sonar.path.temp` is set to, e.g. `mount -o remount,rw,exec /tmp`
2. Change ES temp directory to a different location that is not so restrictive via `sonar.path.temp`, which will define `-Djna.tmpdir`

### SonarQube cannot read PKCS12 keystore / truststore <a href="#cannot-read-pkcs12-keystore-truststore" id="cannot-read-pkcs12-keystore-truststore"></a>

Make sure that the keystore/truststore in question was generated with an algorithm that is known to Java 17. See [JDK-8267599](https://bugs.openjdk.java.net/browse/JDK-8267599) for reference.

### Error: `Unable to open socket file /tmp/.java_pid<PID>`

SonarQube Server 2026.1 LTA and later includes Elasticsearch 8.x, which requires read and write access to the `/tmp` directory. This is a requirement from Elasticsearch itself and cannot be disabled. For more information and a solution, see [#fonts](https://docs.sonarsource.com/sonarqube-server/server-installation/pre-installation/linux#fonts "mention").

### Related pages <a href="#related-pages" id="related-pages"></a>

* [server-logs](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/troubleshooting/server-logs "mention")
* [performance-issues](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/troubleshooting/performance-issues "mention")
* [database-related-issues](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/troubleshooting/database-related-issues "mention")
* [other-issues](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/troubleshooting/other-issues "mention")
