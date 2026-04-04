# Source: https://docs.sonarsource.com/sonarqube-community-build/server-update-and-maintenance/maintenance/sonarqube-db-copy-tool.md

# Source: https://docs.sonarsource.com/sonarqube-server/8.9/instance-administration/sonarqube-db-copy-tool.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/instance-administration/sonarqube-db-copy-tool.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/instance-administration/sonarqube-db-copy-tool.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/instance-administration/sonarqube-db-copy-tool.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/instance-administration/sonarqube-db-copy-tool.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/instance-administration/sonarqube-db-copy-tool.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/instance-administration/sonarqube-db-copy-tool.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/instance-administration/sonarqube-db-copy-tool.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/instance-administration/sonarqube-db-copy-tool.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/instance-administration/sonarqube-db-copy-tool.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/server-upgrade-and-maintenance/maintenance/sonarqube-db-copy-tool.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/server-upgrade-and-maintenance/maintenance/sonarqube-db-copy-tool.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/server-update-and-maintenance/maintenance/sonarqube-db-copy-tool.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-update-and-maintenance/maintenance/sonarqube-db-copy-tool.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-update-and-maintenance/maintenance/sonarqube-db-copy-tool.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/maintenance/sonarqube-db-copy-tool.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-update-and-maintenance/maintenance/sonarqube-db-copy-tool.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-update-and-maintenance/maintenance/sonarqube-db-copy-tool.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/maintenance/sonarqube-db-copy-tool.md

# Migrating database

Download the [SonarQube DB Copy Tool](https://binaries.sonarsource.com/CommercialDistribution/sonar-db-copy/sonar-db-copy-1.6.0.2092-jar-with-dependencies.jar).

We provide SonarQube DB Copy Tool to help you migrate your SonarQube Server database from one database vendor to another. For example, if you’ve been using your SonarQube Server instance with Oracle and want to migrate to PostgreSQL, the **SonarQube DB Copy Tool** will help. DB Copy is preferred for database migration because it does SonarQube-specific checks, ensures data consistency, and outputs meaningful logs.

On this page, *source* refers to your current database and *target* refers to the database you are moving to.

{% hint style="info" %}
After completing the migration, your SonarQube Server ID will change, which invalidates your current license key. For details on how to avoid license invalidation or how to renew your license, see [license-administration](https://docs.sonarsource.com/sonarqube-server/instance-administration/license-administration "mention").
{% endhint %}

### 1. DB Copy - preparation phase <a href="#preparation-phase" id="preparation-phase"></a>

DB Copy only copies data, not the schema. This is why the purpose of this step is to populate *target* with an empty SonarQube schema. For this, you have to install a temporary SonarQube Server instance.

{% hint style="info" %}
As creating the database schema is a quick operation, you don’t need to provision a specific server to do this. A workstation or any non-production server with Java 17 available would be enough.
{% endhint %}

1. Make sure you can connect to your *target* database.
2. Install a SonarQube Server that matches the version and edition of your *source* instance:
   * For a ZIP installation (for more information, see [basic-installation](https://docs.sonarsource.com/sonarqube-server/server-installation/from-zip-file/basic-installation "mention")):
     1. Download the distribution.
     2. Unzip and put it in a relevant place on the machine.
     3. Configure SonarQube Server to connect to your *target* database (ie. provide JDBC parameters in the `<sonarqubeHome>/conf/sonar.properties` file).
     4. Start SonarQube Server using the script matching your operating system. See [from-zip-file](https://docs.sonarsource.com/sonarqube-server/server-installation/from-zip-file/starting-stopping-server/from-zip-file "mention") for more details.
   * For a Docker installation:
     1. Follow the steps in Docker [prepare-installation](https://docs.sonarsource.com/sonarqube-server/server-installation/from-docker-image/prepare-installation "mention") by configuring SonarQube Server to connect to your *target* database.
     2. [set-up-and-start-container](https://docs.sonarsource.com/sonarqube-server/server-installation/from-docker-image/set-up-and-start-container "mention").
3. Verify that the SonarQube schema was correctly created. To do this, look at the `logs/web.log` file to see the line *"Executed DB migrations: success"*. Once this is done, it means that your *target* database had been populated with the SonarQube schema.
4. Stop SonarQube Server:
   * For a ZIP installation: see [starting-stopping-server](https://docs.sonarsource.com/sonarqube-server/server-installation/from-zip-file/starting-stopping-server "mention").
5. You can now delete this temporary SonarQube Server instance.

### 2. DB Copy - execution phase <a href="#execution-phase" id="execution-phase"></a>

Because this step is about copying data from *source* to *target*, the overall performance makes a difference. Make sure you execute this on a powerful machine that has fast network access to both database servers.

1. Unzip the DB Copy package provided by Sonar Support on the machine where it will be executed. Java is required.
2. Stop the SonarQube Server instance connected to your *source* database. This is to ensure that we don’t have records being inserted/updated while copying.
3. Execute the base command with the correct parameters. See below how to do it.
4. If you see something else other than the success message \*\**THE COPY HAS FINISHED SUCCESSFULLY\*\** please open a [Sonar Support Ticket](https://help.sonarsource.com/) and provide the complete DB Copy logs for investigation (logs are just the standard output of the tool).

#### Base command and parameters <a href="#base-command-and-parameters" id="base-command-and-parameters"></a>

**Migrating with an Oracle database**

If you wish to migrate with an Oracle database, you need to include the Oracle driver in the classpath so it is available to the sonar-db-copy tool. In this case, the syntax is:

```css-79elbk
java -cp ojdbc11-21.8.0.0.jar:sonar-db-copy-1.6.0.2092.jar com.sonar.dbcopy.StartApp
```

{% hint style="warning" %}
On Windows, the classpath arguments separator is a semicolon (;), while on a Unix system (like in the example) it is a colon (:).
{% endhint %}

**Migrating with all other databases**

If you are not migrating from or to an Oracle database, then the syntax is:

```css-79elbk
java -jar sonar-db-copy-1.6.0.2092-jar-with-dependencies.jar
```

|                      |                                   |              |
| -------------------- | --------------------------------- | ------------ |
| **Parameter**        | **Description**                   | **Required** |
| `-help`              | Print this help information       | no           |
| `-urlSrc JDBC_URL`   | JDBC URL of the *source* database | yes          |
| `-userSrc USERNAME`  | Username of the *source* database | yes          |
| `-pwdSrc PASSWORD`   | Password of the *source* database | yes          |
| `-urlDest JDBC_URL`  | JDBC URL of the *target* database | yes          |
| `-userDest USERNAME` | Username of the *target* database | yes          |
| `-pwdDest PASSWORD`  | Password of the *target* database | yes          |

Here is an example of a copy from an Oracle to a Postgres database. Note that each parameter is on one line and there are \ (backslash) characters to continue the command. While this works on most shell command-line interpreters, it is not necessarily the case. Use only one line and remove backslashes in that case.

```css-79elbk
java \
-cp ojdbc11-21.8.0.0.jar:sonar-db-copy-1.6.0.2092.jar com.sonar.dbcopy.StartApp \
-urlSrc jdbc:oracle:thin:@10.18.51.1:1521/XEPDB1 \
-userSrc sonar \
-pwdSrc 05xlAz1EhgQb9Pl8 \
-urlDest jdbc:postgresql://10.10.1.138/sonarqube \
-userDest sonar \
-pwdDest Ck23L1OpqF4BdwJv
```
