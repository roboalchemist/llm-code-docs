# Source: https://docs.sonarsource.com/sonarqube-server/10.3/setup-and-upgrade/install-the-server/installing-sonarqube-from-zip-file.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/setup-and-upgrade/install-the-server/installing-sonarqube-from-zip-file.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/setup-and-upgrade/install-the-server/installing-sonarqube-from-zip-file.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/setup-and-upgrade/install-the-server/installing-sonarqube-from-zip-file.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/setup-and-upgrade/install-the-server/installing-sonarqube-from-zip-file.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/setup-and-upgrade/install-the-server/installing-sonarqube-from-zip-file.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/setup-and-update/install-the-server/installing-sonarqube-from-zip-file.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/install-the-server/installing-sonarqube-from-zip-file.md

# Installing from the ZIP file

First, check the requirements (see [server-host](https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/installation-requirements/server-host "mention"), in particular, make sure the [correct Java version 17](https://adoptium.net/en-GB/temurin/releases/?version=17) or [Java version 21](https://adoptium.net/en-GB/temurin/releases/?version=21) is installed) and perform the pre-installation steps (see [pre-installation](https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/pre-installation "mention")). Then follow these steps for your installation:

### Download the distribution <a href="#download-zip" id="download-zip"></a>

Download and unzip the [distribution](https://www.sonarsource.com/products/sonarqube/downloads/) (do not unzip into a directory starting with a digit).

`<sonarqubeHome>` (below) refers to the path of the directory where the SonarQube Server’s distribution has been unzipped.

### Perform various settings <a href="#various-settings" id="various-settings"></a>

#### Set access to the database <a href="#set-access-to-the-database" id="set-access-to-the-database"></a>

Edit `<sonarqubeHome>/conf/sonar.properties` to configure the database settings. Templates are available for every supported database. Just uncomment and configure the template you need and comment out the lines dedicated to H2:

```css-79elbk
Example for PostgreSQL
sonar.jdbc.username=sonarqube
sonar.jdbc.password=mypassword
sonar.jdbc.url=jdbc:postgresql://localhost/sonarqube
```

#### Add the JDBC driver <a href="#add-the-jdbc-driver" id="add-the-jdbc-driver"></a>

Drivers for the supported databases (except Oracle) are already provided. Do not replace the provided drivers; they are the only ones supported.

For Oracle, copy the JDBC driver into `<sonarqubeHome>/extensions/jdbc-driver/oracle`.

#### Configure the Elasticsearch storage path <a href="#configure-the-elasticsearch-storage-path" id="configure-the-elasticsearch-storage-path"></a>

By default, Elasticsearch data is stored in `<sonarqubeHome>/data`, but this is not recommended for production instances. Instead, you should store this data elsewhere, ideally in a dedicated volume with fast I/O. In addition to maintaining performance, upgrading your instance of SonarQube Server will be easier.

Edit `<sonarqubeHome>/conf/sonar.properties` to configure the following settings:

<details>

<summary>Linux</summary>

```css-79elbk
sonar.path.data=/var/sonarqube/data
sonar.path.temp=/var/sonarqube/temp
```

</details>

<details>

<summary>Windows</summary>

```css-79elbk
sonar.path.data=H:\sonarqube\data
sonar.path.temp=H:\sonarqube\temp
```

</details>

The user launching SonarQube Server must have read and write access to those directories.

#### Adjust the Java executable path <a href="#adjust-the-java-executable-path" id="adjust-the-java-executable-path"></a>

By default, the scripts will use the Java executable available in the PATH. If multiple versions of Java are installed on your server, you may need to explicitly define which version is used.

It is possible to overwrite the default Java executable by setting the environmental variable `SONAR_JAVA_PATH`.

<details>

<summary>Linux</summary>

`export SONAR_JAVA_PATH="path/to/java_home/bin/java"`

</details>

<details>

<summary>Windows</summary>

`setx SONAR_JAVA_PATH "C:\Program Files\java_home\bin\java.exe"`

</details>

### Start the web server <a href="#start-server" id="start-server"></a>

1. Execute the following script to start the server:
   * On Linux: `<sonarqubeHome>/bin/linux-x86-64/sonar.sh start`
   * On macOS: `<sonarqubeHome>/bin/macosx-universal-64/sonar.sh start`
   * On Windows: `<sonarqubeHome>\bin\windows-x86-64\StartSonar.bat`
2. You can now open SonarQube Server at [http://localhost:9000](http://localhost:9000/) (the default system administrator credentials are **admin**/**admin**).
3. Once your server is installed and running, you’re ready to begin [overview](https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/overview "mention").

### Post-installation steps <a href="#post-installation" id="post-installation"></a>

You can encrypt sensitive properties stored in `<sonarqubeHome>/conf/sonar.properties`. See [encrypting-settings](https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/encrypting-settings "mention").
