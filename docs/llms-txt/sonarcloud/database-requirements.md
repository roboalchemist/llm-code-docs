# Source: https://docs.sonarsource.com/sonarqube-server/10.5/setup-and-upgrade/installation-requirements/database-requirements.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/setup-and-upgrade/installation-requirements/database-requirements.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/setup-and-upgrade/installation-requirements/database-requirements.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/setup-and-upgrade/installation-requirements/database-requirements.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/setup-and-update/installation-requirements/database-requirements.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/installation-requirements/database-requirements.md

# Database

Supported database engines:

<table><thead><tr><th width="151">Database engine</th><th>Requirement</th></tr></thead><tbody><tr><td>PostgreSQL</td><td>Version: 13 to 17</td></tr><tr><td>Microsoft SQL server</td><td><p>Version:</p><p>• 2022 (MSSQL Server 16.0); 2019 (MSSQL Server 15.0); 2017 (MSSQL Server 14.0); 2016 (MSSQL Server 13.0).</p><p>• With bundled Microsoft JDBC driver.</p><p><strong>Notes</strong>:</p><p>• Express Edition is supported.</p><p>• Windows and SQL Server authentication are both supported.</p></td></tr><tr><td>Oracle</td><td><p>Version: 23ai, 21C, 19C, XE Editions.</p><p><strong>Recommendation</strong>: Use the latest Oracle JDBC driver.</p><p><strong>Notes:</strong></p><p>• The driver ojdbc14.jar is not supported.</p><p>• Only the thin mode is supported, not OCI.</p><p>• Only MAX_STRING_SIZE=STANDARD parameter is supported, not EXTENDED.</p><p>• Must be configured to use a UTF8-family charset (see the NLS_CHARACTERSET).</p><p>• The Oracle JDBC driver versions 12.1.0.1 and 12.1.0.2 have major bugs, and are not recommended for use with SonarQube Server (see more details).</p></td></tr><tr><td>H2</td><td><p><strong>Recommendation</strong>: Use the H2 embedded database for non-production use cases:</p><p>• Development/Testing: H2 is ideal for quick prototypes, unit or integration tests, or CI/CD pipelines due to its lightweight setup.</p><p>• Trials: H2 allows users to try SonarQube without configuring a full database setup like PostgreSQL, Oracle, or MS SQL.</p><p><strong>Why avoid H2 in production</strong>:</p><p>• Scalability Limits: H2 cannot handle high transaction volumes or concurrent users.</p><p>• Data Risks: In-memory mode risks data loss; file-based mode lacks robust durability.</p><p>• Concurrency Issues: H2 struggles with heavy concurrent access, which could cause slowdowns or deadlocks.</p><p>• Limited Features: H2 lacks replication, high availability, advanced security, or robust backups.</p><p>• SQL Compatibility: H2 may differ from production databases, risking transition issues.</p><p>Use PostgreSQL, Oracle, or MS SQL for production to ensure reliability and scalability. Limit H2 to development, testing, or trials.</p></td></tr></tbody></table>

{% hint style="info" %}
We recommend that for production installation, the database used by SonarQube Server is hosted on a machine that is physically separate from the SonarQube Server host, with low latency between both hosts.
{% endhint %}
