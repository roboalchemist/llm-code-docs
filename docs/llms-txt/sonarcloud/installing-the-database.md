# Source: https://docs.sonarsource.com/sonarqube-community-build/server-installation/installing-the-database.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/setup-and-upgrade/install-the-server/installing-the-database.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/setup-and-upgrade/install-the-server/installing-the-database.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/setup-and-upgrade/install-the-server/installing-the-database.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/setup-and-upgrade/install-the-server/installing-the-database.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/setup-and-upgrade/install-the-server/installing-the-database.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/setup-and-upgrade/install-the-server/installing-the-database.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/setup-and-update/install-the-server/installing-the-database.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/installing-the-database.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/installing-the-database.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/install-the-server/installing-the-database.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/installing-the-database.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/installing-the-database.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/installing-the-database.md

# Installing database

{% hint style="info" %}
We recommend that for production installation, the database used by SonarQube Server is hosted on a machine that is physically separate from the SonarQube Server host, with low latency between both hosts.
{% endhint %}

{% hint style="info" %}
The embedded H2 database is used by default. It is recommended for tests but not for production use.
{% endhint %}

### Database requirements <a href="#database-requirements" id="database-requirements"></a>

Several external database engines are supported.

<table><thead><tr><th width="152">Database engine</th><th>Requirement</th></tr></thead><tbody><tr><td>PostgreSQL</td><td>Version: 14 to 18</td></tr><tr><td>Microsoft SQL Server</td><td><p>Version:</p><p>• 2022 (MSSQL Server 16.0); 2019 (MSSQL Server 15.0); 2017 (MSSQL Server 14.0)</p><p>• With bundled Microsoft JDBC driver.</p><p><strong>Notes</strong>:</p><p>• Express Edition is supported.</p><p>• Windows and SQL Server authentication are both supported.</p></td></tr><tr><td>Oracle</td><td><p>Version: 23ai, 21C, 19C, XE Editions.</p><p><strong>Recommendation</strong>: Use the latest Oracle JDBC driver.</p><p><strong>Notes:</strong></p><p>• The driver ojdbc14.jar is not supported.</p><p>• Only the thin mode is supported, not OCI.</p><p>• Only MAX_STRING_SIZE=STANDARD parameter is supported, not EXTENDED.</p><p>• Must be configured to use a UTF8-family charset (see the NLS_CHARACTERSET).</p><p>• The Oracle JDBC driver versions 12.1.0.1 and 12.1.0.2 have major bugs, and are not recommended for use with SonarQube (see more details).</p></td></tr></tbody></table>

#### H2 database not recommended in production <a href="#creating-database-instance" id="creating-database-instance"></a>

While SonarQube Server comes with an embedded H2 database, we do not recommend using it in production. The H2 database can be useful for:

• Development/Testing: H2 is ideal for quick prototypes, unit or integration tests, or CI/CD pipelines due to its lightweight setup.

• Trials: H2 allows users to try SonarQube without configuring a full database setup like PostgreSQL, Oracle, or MS SQL.

**Why avoid H2 in production**:

• Scalability Limits: H2 cannot handle high transaction volumes or concurrent users.

• Data Risks: In-memory mode risks data loss; file-based mode lacks robust durability.

• Concurrency Issues: H2 struggles with heavy concurrent access, which could cause slowdowns or deadlocks.

• Limited Features: H2 lacks replication, high availability, advanced security, or robust backups.

• SQL Compatibility: H2 may differ from production databases, risking transition issues.

Use PostgreSQL, Oracle, or MS SQL for production to ensure reliability and scalability. Limit H2 to development, testing, or trials.

### Creating a new database instance for SonarQube <a href="#creating-database-instance" id="creating-database-instance"></a>

1. Create or use an empty schema for SonarQube to populate.
2. Create a `sonarqube` user. Grant this `sonarqube` user permissions to `create`, `update`, and `delete` objects for this schema.
3. Perform the setup as described below depending on your database type.

### Setup if using an MS SQL Server database <a href="#ms-sql-server" id="ms-sql-server"></a>

This page describes operations to be performed on your MS SQL Server instance for SonarQube.

#### Set collation to CS and AS <a href="#set-collation-to-cs-and-as" id="set-collation-to-cs-and-as"></a>

Collation **MUST** be case-sensitive (CS) and accent-sensitive (AS).

#### Enable READ\_COMMITTED\_SNAPSHOT <a href="#enable-readcommittedsnapshot" id="enable-readcommittedsnapshot"></a>

`READ_COMMITTED_SNAPSHOT` **MUST** be set on the SonarQube database.

MS SQL database’s shared lock strategy may impact SonarQube Server runtime. Making sure that `is_read_committed_snapshot_on` is set to `true` will prevent SonarQube from facing potential deadlocks under heavy loads.

To check `is_read_committed_snapshot_on`, you may use the following query:

```sql
SELECT is_read_committed_snapshot_on FROM sys.databases WHERE name='YourSonarQubeDatabase';
```

To update `is_read_committed_snapshot_on`, you may use the following query:

```sql
ALTER DATABASE YourSonarQubeDatabase SET READ_COMMITTED_SNAPSHOT ON WITH ROLLBACK IMMEDIATE;
```

#### Encryption-related setup <a href="#encryptionrelated-setup" id="encryptionrelated-setup"></a>

If your Microsoft SQL Server doesn’t support encryption, you must add `encrypt=false` to the JDBC URL connection string.

If your Microsoft SQL Server requires encryption but you don’t want SonarQube to validate the certificate, you must add `trustServerCertificate=true` to the JDBC URL connection string.

#### Using integrated security <a href="#using-integrated-security" id="using-integrated-security"></a>

To use integrated security:

1. Download the [Microsoft SQL JDBC Auth 12.10.2](https://github.com/microsoft/mssql-jdbc/releases/download/v12.10.2/mssql-jdbc_auth.zip) package and copy `mssql-jdbc_auth-12.10.2.x64.dll` to a folder location set in the PATH environment variable on SonarQube Server host.
2. If you’re running SonarQube as a Windows service, make sure the Windows account under which the service is running has permission to connect your SQL server.

### Setup if using an Oracle database <a href="#oracle" id="oracle"></a>

If there are two SonarQube schemas on the same Oracle instance, especially if they are for two different versions, SonarQube gets confused and picks the first it finds. To avoid this issue:

* Either privileges associated to the SonarQube’s Oracle user should be decreased.
* Or a trigger should be defined on the Oracle side to automatically alter the SonarQube’s Oracle user session when establishing a new connection:

```sql
ALTER SESSION SET current_schema="MY_SONARQUBE_SCHEMA".
```

### Setup if using a PostgreSQL database <a href="#postgresql" id="postgresql"></a>

Your PostgreSQL instance for SonarQube:

* Must be configured to use UTF-8 charset.
* If you want to use a custom schema and not the default "public" one: the PostgreSQL `search_path` property must be set:

```sql
ALTER USER mySonarUser SET search_path to mySonarQubeSchema
```
