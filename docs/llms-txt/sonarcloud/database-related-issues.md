# Source: https://docs.sonarsource.com/sonarqube-community-build/server-update-and-maintenance/troubleshooting/database-related-issues.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/server-upgrade-and-maintenance/troubleshooting/database-related-issues.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/server-update-and-maintenance/troubleshooting/database-related-issues.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-update-and-maintenance/troubleshooting/database-related-issues.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-update-and-maintenance/troubleshooting/database-related-issues.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/troubleshooting/database-related-issues.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-update-and-maintenance/troubleshooting/database-related-issues.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-update-and-maintenance/troubleshooting/database-related-issues.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/troubleshooting/database-related-issues.md

# Database-related issues

We recommend reading the [server-logs](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/troubleshooting/server-logs "mention") first.

### Timeout issues when setting up Database Connection Pool <a href="#time-out-database-connection-pool" id="time-out-database-connection-pool"></a>

In some configurations when there is a firewall between SonarQube Server and the data you may experience timeout issues. The firewall may interrupt idle DB connections after a specific timeout which can lead to resetting connections. See also **Issues with MS SQL Server connection** below.

You can customize the [HikariCP](https://github.com/brettwooldridge/HikariCP#gear-configuration-knobs-baby) settings to the defaults listed below to avoid timeout isssues.

```css-79elbk
sonar.jdbc.idleTimeout=600000
sonar.jdbc.keepaliveTime=300000
sonar.jdbc.maxLifetime=1800000
sonar.jdbc.validationTimeout=5000
```

Additionally, it is now possible to configure HikariCP properties described [here](https://github.com/brettwooldridge/HikariCP#frequently-used) using the following naming convention: `sonar.jdbc.{HikariCP property name}`.

### Issues with MS SQL Server connection <a href="#hikaricp-connection-issue" id="hikaricp-connection-issue"></a>

HikariCP may get exhausted from connections causing SonarQube Server to be unresponsive. In this case, the error may display something like `HikariPool-1 - Connection is not available` or `HikariPool-1 - Cannot acquire connection from data source`.

In this case, customize the [HikariCP](https://github.com/brettwooldridge/HikariCP#gear-configuration-knobs-baby) settings as follows:

```css-79elbk
sonar.jdbc.minIdle=25
sonar.jdbc.maxActive=25
sonar.jdbc.maxLifetime=0
sonar.jdbc.maxWait=30000
```

### Oracle JDBC driver blocked <a href="#oracle-driver-blocked" id="oracle-driver-blocked"></a>

See [#if-oracle](https://docs.sonarsource.com/sonarqube-server/server-installation/pre-installation/linux#if-oracle "mention") for more information.

### Connectivity issue between SonarQube Server and MS SQL Server <a href="#connectivity-issue" id="connectivity-issue"></a>

If the TCP/IP connection is refused, make sure that Named Pipes and TCP/IP connections are enabled on your SQL Server.

### Duplicate keys during background task processing after upgrading to RHEL 8 <a href="#duplicate-keys-after-upgrade" id="duplicate-keys-after-upgrade"></a>

If you performed an in-place OS upgrade to RHEL 8 or [with any similar operating systems](https://wiki.postgresql.org/wiki/Locale_data_changes#What_Linux_distributions_are_affected) and you use PostgreSQL, the new version of glibc may affect locale data changes.

To prevent this, avoid in-place OS upgrades and perform dump-and-restore of the database to an already-upgraded OS.

To correct the issue, restore from a known good backup copy of the database and perform the maintenance steps:

```css-79elbk
VACUUM FULL;
REINDEX DATABASE <database-name>;
ANALYZE;
```

### Related pages <a href="#related-pages" id="related-pages"></a>

* [server-logs](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/troubleshooting/server-logs "mention")
* [performance-issues](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/troubleshooting/performance-issues "mention")
* [elasticsearch](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/troubleshooting/elasticsearch "mention")
* [other-issues](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/troubleshooting/other-issues "mention")
