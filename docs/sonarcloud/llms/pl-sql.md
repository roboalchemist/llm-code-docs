# Source: https://docs.sonarsource.com/sonarqube-server/8.9/analyzing-source-code/languages/pl-sql.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/analyzing-source-code/languages/pl-sql.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/analyzing-source-code/languages/pl-sql.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/analyzing-source-code/languages/pl-sql.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/analyzing-source-code/languages/pl-sql.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/analyzing-source-code/languages/pl-sql.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/analyzing-source-code/languages/pl-sql.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/analyzing-source-code/languages/pl-sql.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/languages/pl-sql.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/languages/pl-sql.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/languages/pl-sql.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/languages/pl-sql.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/languages/pl-sql.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/languages/pl-sql.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/languages/pl-sql.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/languages/pl-sql.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/languages/pl-sql.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/languages/pl-sql.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/pl-sql.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/pl-sql.md

# PL/SQL

### Language-Specific Properties <a href="#language-specific-properties" id="language-specific-properties"></a>

To discover and update the PL/SQL-specific properties, navigate in SonarQube Cloud to *Your Project* > **Administration** > **General Settings** > **Languages** > **PL/SQL**. See the [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention") page for more information about specific properties.

### Advanced parameters <a href="#advanced-parameters" id="advanced-parameters"></a>

#### Default Schema <a href="#default-schema" id="default-schema"></a>

| **Parameter**               | **Description**                                                                                                                                                                                                                              |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sonar.plsql.defaultSchema` | <p>When a schema object (table, view, index, synonym) is referenced in SQL code without a schema prefix, the analyzer will assume that it belongs to this schema.</p><p>Defaults to <code>sonar.plsql.jdbc.user</code><strong>.</strong></p> |

#### Data Dictionary <a href="#data-dictionary" id="data-dictionary"></a>

Some rules raise issues only when a data dictionary is provided during analysis. To provide a data dictionary, you must define the following properties in the `sonar-project.properties` file or on the scanner command line using the `-D` prefix:

| **Parameter**                   | **Description**                                                                                                                                                       |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sonar.plsql.jdbc.url`          | <p>URL of the JDBC connection. <strong>Required for data dictionary lookup</strong>.<br>For example: <code>jdbc:oracle:thin:@my-oracle-server:1521/my-db</code></p>   |
| `sonar.plsql.jdbc.user`         | <p>JDBC user to authenticate the connection.</p><p>Will be used as the default schema name if not specified otherwise via <code>sonar.plsql.defaultSchema</code>.</p> |
| `sonar.plsql.jdbc.password`     | JDBC password provided to authenticate the connection.                                                                                                                |
| `sonar.plsql.jdbc.driver.path`  | Path or URL of the Oracle jdbc driver jar.                                                                                                                            |
| `sonar.plsql.jdbc.driver.class` | <p>Java class name of the Oracle Driver.<br>For example: <code>oracle.jdbc.OracleDriver</code></p>                                                                    |

Providing this configuration allows SonarPLSQL to query data dictionary views such as `SYS.ALL_TAB_COLUMNS` in order to better analyze your SQL.
