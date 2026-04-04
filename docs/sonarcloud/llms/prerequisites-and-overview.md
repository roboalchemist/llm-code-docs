# Source: https://docs.sonarsource.com/sonarqube-server/8.9/requirements/prerequisites-and-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/requirements/prerequisites-and-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/requirements/prerequisites-and-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/requirements/prerequisites-and-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/requirements/prerequisites-and-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/requirements/prerequisites-and-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/requirements/prerequisites-and-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/requirements/prerequisites-and-overview.md

# Prerequisites and overview

### Prerequisite <a href="#prerequisite" id="prerequisite"></a>

You must be able to install Java (Oracle JRE or OpenJDK) on the machine where you plan to run SonarQube.

### Hardware requirements <a href="#hardware-requirements" id="hardware-requirements"></a>

1. A small-scale (individual or small team) instance of the SonarQube server requires at least 2GB of RAM to run efficiently and 1GB of free RAM for the OS. If you are installing an instance for a large team or an enterprise, please consider the additional recommendations below.
2. The amount of disk space you need will depend on how much code you analyze with SonarQube.
3. SonarQube must be installed on hard drives that have excellent read & write performance. Most importantly, the "data" folder houses the Elasticsearch indices on which a huge amount of I/O will be done when the server is up and running. Read and write hard drive performance will therefore have a big impact on the overall SonarQube server performance.
4. SonarQube and the SonarScanner support only 64-bit systems.

{% hint style="info" %}
Support for 32-bit Java Runtime Environments has been dropped in all Sonar products. This drop affects all Sonar products: SonarLint (for all IDEs), SonarQube, and SonarCloud, including the scanners.
{% endhint %}

#### Enterprise hardware recommendations <a href="#enterprise-hardware-recommendations" id="enterprise-hardware-recommendations"></a>

For large teams or enterprise-scale installations of SonarQube, additional hardware is required. At the enterprise level, [instance](https://docs.sonarsource.com/sonarqube-server/10.4/instance-administration/monitoring/instance "mention") is essential and should guide further hardware upgrades as your instance grows. A starting configuration should include at least:

* 8 cores, to allow the main SonarQube platform to run with multiple compute engine workers
* 16GB of RAM For additional requirements and recommendations relating to database and Elasticsearch, see [hardware-recommendations](https://docs.sonarsource.com/sonarqube-server/10.4/requirements/hardware-recommendations "mention").

### Supported platforms <a href="#supported-platforms" id="supported-platforms"></a>

#### Java <a href="#java" id="java"></a>

The SonarQube server requires Java version 17.

For the SonarScanners, the minimum recommended version is Java 17.

SonarQube is able to analyze any kind of Java source files regardless of the version of Java they comply with.

We recommend using the *critical patch update* (CPU) releases.

| **Java**   | **Server**                                                                                                                                                                                                                                             | **Scanners**                                                                                                                                                                                                                                           |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Oracle JRE | <p><img src="https://2155789048-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FL4urx4YsPFYDefLTrxao%2Fuploads%2Fgit-blob-51435de4153f60f46883a8cb66af53e3ff29d70c%2Fgreen-check.svg?alt=media" alt="Checkmark icon"></p><p>17</p> | <p><img src="https://2155789048-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FL4urx4YsPFYDefLTrxao%2Fuploads%2Fgit-blob-51435de4153f60f46883a8cb66af53e3ff29d70c%2Fgreen-check.svg?alt=media" alt="Checkmark icon"></p><p>17</p> |
| OpenJDK    | <p><img src="https://2155789048-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FL4urx4YsPFYDefLTrxao%2Fuploads%2Fgit-blob-51435de4153f60f46883a8cb66af53e3ff29d70c%2Fgreen-check.svg?alt=media" alt="Checkmark icon"></p><p>17</p> | <p><img src="https://2155789048-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FL4urx4YsPFYDefLTrxao%2Fuploads%2Fgit-blob-51435de4153f60f46883a8cb66af53e3ff29d70c%2Fgreen-check.svg?alt=media" alt="Checkmark icon"></p><p>17</p> |

#### Database <a href="#database" id="database"></a>

| **Database**                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ----------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [PostgreSQL](http://www.postgresql.org/)                    | <p><img src="https://2155789048-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FL4urx4YsPFYDefLTrxao%2Fuploads%2Fgit-blob-51435de4153f60f46883a8cb66af53e3ff29d70c%2Fgreen-check.svg?alt=media" alt="Checkmark icon"></p><p>15</p>                                                                                                                                                                                                                                                                                                                             |
| <p><br></p>                                                 | <p><img src="https://2155789048-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FL4urx4YsPFYDefLTrxao%2Fuploads%2Fgit-blob-51435de4153f60f46883a8cb66af53e3ff29d70c%2Fgreen-check.svg?alt=media" alt="Checkmark icon"></p><p>14</p>                                                                                                                                                                                                                                                                                                                             |
| <p><br></p>                                                 | <p><img src="https://2155789048-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FL4urx4YsPFYDefLTrxao%2Fuploads%2Fgit-blob-51435de4153f60f46883a8cb66af53e3ff29d70c%2Fgreen-check.svg?alt=media" alt="Checkmark icon"></p><p>13</p>                                                                                                                                                                                                                                                                                                                             |
| <p><br></p>                                                 | <p><img src="https://2155789048-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FL4urx4YsPFYDefLTrxao%2Fuploads%2Fgit-blob-51435de4153f60f46883a8cb66af53e3ff29d70c%2Fgreen-check.svg?alt=media" alt="Checkmark icon"></p><p>12</p>                                                                                                                                                                                                                                                                                                                             |
| <p><br></p>                                                 | <p><img src="https://2155789048-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FL4urx4YsPFYDefLTrxao%2Fuploads%2Fgit-blob-51435de4153f60f46883a8cb66af53e3ff29d70c%2Fgreen-check.svg?alt=media" alt="Checkmark icon"></p><p>11</p>                                                                                                                                                                                                                                                                                                                             |
| <p><br></p>                                                 | <p><img src="https://2155789048-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FL4urx4YsPFYDefLTrxao%2Fuploads%2Fgit-blob-7b1e8da81920424698c86c69c8201d47c933bd72%2F53461ea24385e3549d8e20706bfa594dc6dc1709.svg?alt=media" alt="exclamation icon"></p><p>Must be configured to use UTF-8 charset</p>                                                                                                                                                                                                                                                         |
| [Microsoft SQL Server](http://www.microsoft.com/sqlserver/) | <p><img src="https://2155789048-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FL4urx4YsPFYDefLTrxao%2Fuploads%2Fgit-blob-51435de4153f60f46883a8cb66af53e3ff29d70c%2Fgreen-check.svg?alt=media" alt="Checkmark icon"></p><p>2022 (MSSQL 16.0) with bundled Microsoft JDBC driver. Express Edition is supported.</p>                                                                                                                                                                                                                                            |
| <p><br></p>                                                 | <p><img src="https://2155789048-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FL4urx4YsPFYDefLTrxao%2Fuploads%2Fgit-blob-51435de4153f60f46883a8cb66af53e3ff29d70c%2Fgreen-check.svg?alt=media" alt="Checkmark icon"></p><p>2019 (MSSQL Server 15.0) with bundled Microsoft JDBC driver. Express Edition is supported.</p>                                                                                                                                                                                                                                     |
| <p><br></p>                                                 | <p><img src="https://2155789048-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FL4urx4YsPFYDefLTrxao%2Fuploads%2Fgit-blob-51435de4153f60f46883a8cb66af53e3ff29d70c%2Fgreen-check.svg?alt=media" alt="Checkmark icon"></p><p>2017 (MSSQL Server 14.0) with bundled Microsoft JDBC driver. Express Edition is supported.</p>                                                                                                                                                                                                                                     |
| <p><br></p>                                                 | <p><img src="https://2155789048-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FL4urx4YsPFYDefLTrxao%2Fuploads%2Fgit-blob-51435de4153f60f46883a8cb66af53e3ff29d70c%2Fgreen-check.svg?alt=media" alt="Checkmark icon"></p><p>2016 (MSSQL Server 13.0) with bundled Microsoft JDBC driver. Express Edition is supported.</p>                                                                                                                                                                                                                                     |
| <p><br></p>                                                 | <p><img src="https://2155789048-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FL4urx4YsPFYDefLTrxao%2Fuploads%2Fgit-blob-51435de4153f60f46883a8cb66af53e3ff29d70c%2Fgreen-check.svg?alt=media" alt="Checkmark icon"></p><p>2014 (MSSQL Server 12.0) with bundled Microsoft JDBC driver. Express Edition is supported.</p>                                                                                                                                                                                                                                     |
| <p><br></p>                                                 | <p><img src="https://2155789048-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FL4urx4YsPFYDefLTrxao%2Fuploads%2Fgit-blob-7b1e8da81920424698c86c69c8201d47c933bd72%2F53461ea24385e3549d8e20706bfa594dc6dc1709.svg?alt=media" alt="exclamation icon"></p><p>Collation must be case-sensitive (CS) and accent-sensitive (AS) (example: <code>Latin1\_General\_CS\_AS</code>).</p>                                                                                                                                                                                |
| <p><br></p>                                                 | <p><img src="https://2155789048-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FL4urx4YsPFYDefLTrxao%2Fuploads%2Fgit-blob-7b1e8da81920424698c86c69c8201d47c933bd72%2F53461ea24385e3549d8e20706bfa594dc6dc1709.svg?alt=media" alt="exclamation icon"></p><p><code>READ\_COMMITTED\_SNAPSHOT</code> must be set on the SonarQube database to avoid potential deadlocks under heavy load.</p>                                                                                                                                                                     |
| <p><br></p>                                                 | <p><img src="https://2155789048-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FL4urx4YsPFYDefLTrxao%2Fuploads%2Fgit-blob-c794429034aa4e7bc46e0c9c43d2e14a611f0d21%2F358a8bd3f114a86d9e02920f690588bf17ea1c87.svg?alt=media" alt="Info"></p><p>Both Windows authentication ("Integrated Security") and SQL Server authentication are supported. See the Microsoft SQL Server section in <a data-mention href="../setup-and-upgrade/install-the-server/installing-the-database">installing-the-database</a> for instructions on configuring authentication.</p> |
| [Oracle](http://www.oracle.com/database/)                   | <p><img src="https://2155789048-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FL4urx4YsPFYDefLTrxao%2Fuploads%2Fgit-blob-51435de4153f60f46883a8cb66af53e3ff29d70c%2Fgreen-check.svg?alt=media" alt="Checkmark icon"></p><p>21C</p>                                                                                                                                                                                                                                                                                                                            |
| <p><br></p>                                                 | <p><img src="https://2155789048-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FL4urx4YsPFYDefLTrxao%2Fuploads%2Fgit-blob-51435de4153f60f46883a8cb66af53e3ff29d70c%2Fgreen-check.svg?alt=media" alt="Checkmark icon"></p><p>19C</p>                                                                                                                                                                                                                                                                                                                            |
| <p><br></p>                                                 | <p><img src="https://2155789048-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FL4urx4YsPFYDefLTrxao%2Fuploads%2Fgit-blob-51435de4153f60f46883a8cb66af53e3ff29d70c%2Fgreen-check.svg?alt=media" alt="Checkmark icon"></p><p>XE Editions</p>                                                                                                                                                                                                                                                                                                                    |
| <p><br></p>                                                 | <p><img src="https://2155789048-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FL4urx4YsPFYDefLTrxao%2Fuploads%2Fgit-blob-7b1e8da81920424698c86c69c8201d47c933bd72%2F53461ea24385e3549d8e20706bfa594dc6dc1709.svg?alt=media" alt="exclamation icon"></p><p>Must be configured to use a UTF8-family charset (see <code>NLS\_CHARACTERSET</code>).</p>                                                                                                                                                                                                           |
| <p><br></p>                                                 | <p><img src="https://2155789048-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FL4urx4YsPFYDefLTrxao%2Fuploads%2Fgit-blob-7b1e8da81920424698c86c69c8201d47c933bd72%2F53461ea24385e3549d8e20706bfa594dc6dc1709.svg?alt=media" alt="exclamation icon"></p><p>The driver <code>ojdbc14.jar</code> is not supported.</p>                                                                                                                                                                                                                                           |
| <p><br></p>                                                 | <p><img src="https://2155789048-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FL4urx4YsPFYDefLTrxao%2Fuploads%2Fgit-blob-c794429034aa4e7bc46e0c9c43d2e14a611f0d21%2F358a8bd3f114a86d9e02920f690588bf17ea1c87.svg?alt=media" alt="Info"></p><p>We recommend using the latest Oracle JDBC driver.</p>                                                                                                                                                                                                                                                           |
| <p><br></p>                                                 | <p><img src="https://2155789048-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FL4urx4YsPFYDefLTrxao%2Fuploads%2Fgit-blob-7b1e8da81920424698c86c69c8201d47c933bd72%2F53461ea24385e3549d8e20706bfa594dc6dc1709.svg?alt=media" alt="exclamation icon"></p><p>Only the thin mode is supported, not OCI.</p>                                                                                                                                                                                                                                                       |
| <p><br></p>                                                 | <p><img src="https://2155789048-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FL4urx4YsPFYDefLTrxao%2Fuploads%2Fgit-blob-7b1e8da81920424698c86c69c8201d47c933bd72%2F53461ea24385e3549d8e20706bfa594dc6dc1709.svg?alt=media" alt="exclamation icon"></p><p>Only <code>MAX\_STRING\_SIZE=STANDARD</code> parameter is supported, not <code>EXTENDED</code>.</p>                                                                                                                                                                                                 |

#### Web browser <a href="#web-browser" id="web-browser"></a>

To get the full experience SonarQube has to offer, you must enable JavaScript in your browser.

| **Browser**     |                                                                                                                                                                                                                                                            |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Microsoft Edge  | <p><img src="https://2155789048-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FL4urx4YsPFYDefLTrxao%2Fuploads%2Fgit-blob-51435de4153f60f46883a8cb66af53e3ff29d70c%2Fgreen-check.svg?alt=media" alt="Checkmark icon"></p><p>Latest</p> |
| Mozilla Firefox | <p><img src="https://2155789048-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FL4urx4YsPFYDefLTrxao%2Fuploads%2Fgit-blob-51435de4153f60f46883a8cb66af53e3ff29d70c%2Fgreen-check.svg?alt=media" alt="Checkmark icon"></p><p>Latest</p> |
| Google Chrome   | <p><img src="https://2155789048-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FL4urx4YsPFYDefLTrxao%2Fuploads%2Fgit-blob-51435de4153f60f46883a8cb66af53e3ff29d70c%2Fgreen-check.svg?alt=media" alt="Checkmark icon"></p><p>Latest</p> |
| Safari          | <p><img src="https://2155789048-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FL4urx4YsPFYDefLTrxao%2Fuploads%2Fgit-blob-51435de4153f60f46883a8cb66af53e3ff29d70c%2Fgreen-check.svg?alt=media" alt="Checkmark icon"></p><p>Latest</p> |

### Platform notes <a href="#platform-notes" id="platform-notes"></a>

#### Linux <a href="#linux" id="linux"></a>

If you’re running on Linux, you must ensure that:

* `vm.max_map_count` is greater than or equal to 524288
* `fs.file-max` is greater than or equal to 131072
* the user running SonarQube can open at least 131072 file descriptors
* the user running SonarQube can open at least 8192 threads

You can see the values with the following commands:

```css-79elbk
sysctl vm.max_map_count
sysctl fs.file-max
ulimit -n
ulimit -u
```

You can set them dynamically for the current session by running the following commands as `root`:

```css-79elbk
sysctl -w vm.max_map_count=524288
sysctl -w fs.file-max=131072
ulimit -n 131072
ulimit -u 8192
```

To set these values more permanently, you must update either `/etc/sysctl.d/99-sonarqube.conf` (or `/etc/sysctl.conf` as you wish) to reflect these values.

If the user running SonarQube (`sonarqube` in this example) does not have permission to have at least 131072 open descriptors, you must insert this line in `/etc/security/limits.d/99-sonarqube.conf` (or `/etc/security/limits.conf` as you wish):

```css-79elbk
sonarqube   -   nofile   131072
sonarqube   -   nproc    8192
```

If you are using `systemd` to start SonarQube, you must specify those limits inside your unit file in the section `[Service]` :

```css-79elbk
[Service]
...
LimitNOFILE=131072
LimitNPROC=8192
...
```

#### macOS <a href="#macos" id="macos"></a>

Same as for Linux: If you’re running into maximum file limit issues on macOS, you can fix them by setting the file limit values by running the following commands:

```css-79elbk
sudo sysctl -w kern.maxfiles=131072
sudo sysctl -w kern.maxfilesperproc=131072
ulimit -n 131072
```

#### seccomp filter <a href="#seccomp-filter" id="seccomp-filter"></a>

By default, Elasticsearch uses the [`seccomp` filter](https://www.kernel.org/doc/Documentation/prctl/seccomp_filter.txt). Make sure you use a kernel with seccomp enabled.

To check that `seccomp` is available on your kernel, use:

```css-79elbk
$ grep SECCOMP /boot/config-$(uname -r)
```

If your kernel has `seccomp`, you’ll see the following:

```css-79elbk
CONFIG_HAVE_ARCH_SECCOMP_FILTER=y
CONFIG_SECCOMP_FILTER=y
CONFIG_SECCOMP=y
```

#### Fonts <a href="#fonts" id="fonts"></a>

Generating [pdf-reports](https://docs.sonarsource.com/sonarqube-server/10.4/project-administration/pdf-reports "mention") requires that fonts be installed on the server hosting SonarQube. On Windows servers, this is a given. However, this is not always the case for Linux servers.

The following should be ensured:

* [Fontconfig](https://en.wikipedia.org/wiki/Fontconfig) is installed on the server hosting SonarQube
* A package of [FreeType](https://www.freetype.org/) fonts is installed on the SonarQube server. The exact packages available will vary by distribution, but a commonly used package is `libfreetype6`

#### FIPS <a href="#fips" id="fips"></a>

SonarQube will not run on Linux hosts where FIPS (Federal Information Processing Standard) is enforced.

### Azure App Service not supported <a href="#azure-app-service-not-supported" id="azure-app-service-not-supported"></a>

While SonarQube is provider agnostic, some environments do not work well as platforms for a SonarQube installation.

The issue with Azure App Service is linked to the fact that SonarQube’s Elasticsearch component runs bootstrap checks on values at startup. This includes the prerequisites for Linux platforms documented above. If the values are too low for any of these properties, the SonarQube startup will fail. These values need to be set on the host system, which Azure does not make possible for this service.
