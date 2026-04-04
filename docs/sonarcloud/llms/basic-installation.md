# Source: https://docs.sonarsource.com/sonarqube-community-build/server-installation/from-zip-file/basic-installation.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/from-docker-image/basic-installation.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/from-zip-file/basic-installation.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/from-zip-file/basic-installation.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/from-zip-file/basic-installation.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/from-zip-file/basic-installation.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/from-zip-file/basic-installation.md

# Basic installation

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

You have:

* Checked the host requirements. See [server-host-requirements](https://docs.sonarsource.com/sonarqube-server/server-installation/server-host-requirements "mention").\
  In particular, make sure the correct Java version is installed. To check the Java version on your computer, you can use the command line. In Windows, open the Command Prompt and type `java -version`. In macOS, open Terminal and type the same command. This will display the Java version installed on your system.
* Performed the pre-installation checks:
  * [linux](https://docs.sonarsource.com/sonarqube-server/server-installation/pre-installation/linux "mention")
  * [unix](https://docs.sonarsource.com/sonarqube-server/server-installation/pre-installation/unix "mention")
  * [macos](https://docs.sonarsource.com/sonarqube-server/server-installation/pre-installation/macos "mention")
* Installed your database (except if you want to install SonarQube for test purposes and want to use the embedded database H2). See [installing-the-database](https://docs.sonarsource.com/sonarqube-server/server-installation/installing-the-database "mention").

### Download the distribution <a href="#download-zip" id="download-zip"></a>

1. Download the [distribution](https://www.sonarsource.com/products/sonarqube/downloads/).
2. Unzip the downloaded ZIP file into the directory you want to use to install your SonarQube (except a directory starting with a digit). The figure below shows this directory. It is called `<sonarqubeHome>` in this documentation.

<figure><img src="broken-reference" alt="SonarQube installation directory with its subdirectories"><figcaption></figcaption></figure>

### Set access to the database <a href="#set-access-to-database" id="set-access-to-database"></a>

You must configure the access to your database (except if you want to use SonarQube for test purposes and want to use the embedded database H2):

1. Open `<sonarqubeHome>/conf/sonar.properties`.
2. Set the user credentials required to connect to your database. To do so, uncomment and configure the lines related to:
   * `sonar.jdbc.username` (JDBC user name)
   * `sonar.jdbc.password` (JDBC user password)
3. Specify how to connect to your database. To do so, uncomment and configure the line related to `sonar.jdbc.url` and corresponding to your database type. For more information, see [#general](https://docs.sonarsource.com/sonarqube-server/system-properties/common-properties#general "mention").
4. Comment out the lines dedicated to the embedded database H2.

<details>

<summary>Example for a PostgreSQL database</summary>

```css-79elbk
sonar.jdbc.username=sonarqube
sonar.jdbc.password=mypassword
sonar.jdbc.url=jdbc:postgresql://localhost/sonarqube
```

</details>

### Oracle database: add the JDBC driver <a href="#add-jdbc-driver" id="add-jdbc-driver"></a>

If you use an Oracle database, copy the JDBC driver into `<sonarqubeHome>/extensions/jdbc-driver/oracle`.

Drivers for the other supported databases are already provided. Do not replace the provided drivers; they are the only ones supported.

### Configure the Elasticsearch storage path <a href="#configure-es-storage-path" id="configure-es-storage-path"></a>

By default, Elasticsearch data is stored in `<sonarqubeHome>/data`, but this is not recommended for production instances. Instead, you should store this data elsewhere, ideally in a dedicated volume with fast I/O. In addition to maintaining performance, upgrading your instance of SonarQube will be easier.

To configure the path to the `data` and `temp` directories:

1\. Edit `<sonarqubeHome>/conf/sonar.properties` to configure the following settings:

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

2\. Make sure the user launching SonarQube has read and write access to those directories.

### Check the web server connection parameters <a href="#check-web-server-connection-parameters" id="check-web-server-connection-parameters"></a>

Check the default values of the web server connection parameters in [#web-server-connection](https://docs.sonarsource.com/sonarqube-server/system-properties/common-properties#web-server-connection "mention"). Change the parameter values in `<sonarqubeHome>/conf/sonar.properties` if necessary.

### Start the web server <a href="#start-server" id="start-server"></a>

To start SonarQube Server from the console, see [from-zip-file](https://docs.sonarsource.com/sonarqube-server/server-installation/from-zip-file/starting-stopping-server/from-zip-file "mention").

To install and start SonarQube Server as a service, see [running-as-a-service](https://docs.sonarsource.com/sonarqube-server/server-installation/from-zip-file/starting-stopping-server/running-as-a-service "mention").

The message "SonarQube is operational" appears in the console output or in the server logs after a successful installation and startup. You can now open SonarQube Server at the configured address (by default `http://localhost:9000`). The default system administrator credentials are **admin**/**admin**.

{% hint style="info" %}
Once SonarQube Server UI is up, you can encrypt sensitive properties stored in `<sonarqubeHome>/conf/sonar.properties`. See [encrypting-settings](https://docs.sonarsource.com/sonarqube-server/instance-administration/security/encrypting-settings "mention").
{% endhint %}

### Related pages <a href="#related-pages" id="related-pages"></a>

* [overview](https://docs.sonarsource.com/sonarqube-server/server-installation/from-zip-file/overview "mention")
* [advanced-setup](https://docs.sonarsource.com/sonarqube-server/server-installation/from-zip-file/advanced-setup "mention")
* **Configuring network security features:**
  * [securing-behind-proxy](https://docs.sonarsource.com/sonarqube-server/server-installation/network-security/securing-behind-proxy "mention")
  * [network-rules](https://docs.sonarsource.com/sonarqube-server/server-installation/network-security/network-rules "mention")
* [starting-stopping-server](https://docs.sonarsource.com/sonarqube-server/server-installation/from-zip-file/starting-stopping-server "mention")
* [running-as-a-service](https://docs.sonarsource.com/sonarqube-server/server-installation/from-zip-file/starting-stopping-server/running-as-a-service "mention")
* Installing the Data Center Edition from the ZIP file:[from-zip-file](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/from-zip-file "mention")
