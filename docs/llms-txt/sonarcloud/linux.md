# Source: https://docs.sonarsource.com/sonarqube-community-build/server-installation/pre-installation/linux.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/setup-and-upgrade/pre-installation/linux.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/setup-and-upgrade/pre-installation/linux.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/setup-and-upgrade/pre-installation/linux.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/setup-and-upgrade/pre-installation/linux.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/setup-and-update/pre-installation/linux.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/pre-installation/linux.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/pre-installation/linux.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/pre-installation/linux.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/pre-installation/linux.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/pre-installation/linux.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/pre-installation/linux.md

# On Linux systems

### Configuring the host to comply with Elasticsearch <a href="#elasticsearch" id="elasticsearch"></a>

Because SonarQube Server uses an embedded Elasticsearch, make sure that your host configuration complies with the [Elasticsearch production mode requirements](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html#docker-prod-prerequisites) and [File Descriptors configuration](https://www.elastic.co/guide/en/elasticsearch/reference/current/file-descriptors.html).

#### Configuring the maximum number of open files and other limits <a href="#configuring-the-maximum-number-of-open-files-and-other-limits" id="configuring-the-maximum-number-of-open-files-and-other-limits"></a>

You must ensure that:

* The maximum number of memory map areas a process may have (vm.max\_map\_count) is greater than or equal to 524288.
* The maximum number of open file descriptors (fs.file-max) is greater than or equal to 131072.
* The user running SonarQube Server can open **at least** 131072 file descriptors.
* The user running SonarQube Server can open **at least** 8192 threads.

You must set these limits on the host system, whatever the installation type:

* For a Docker installation: These settings will then apply to the Docker container.
* For a Kubernetes deployment: Check also these [guidelines](https://artifacthub.io/packages/helm/sonarqube/sonarqube#elasticsearch-prerequisites).

To check and change these limits, login as the user used to run SonarQube Server and proceed as described below depending on the type of this user.

<details>

<summary>For a non-systemd user</summary>

1\. Verify the values listed above with the following commands:

```sh
sysctl vm.max_map_count
sysctl fs.file-max
ulimit -n
ulimit -u
```

2\. To change the max map count and the file-max, insert the following in `/etc/sysctl.d/99-sonarqube.conf` (or in `/etc/sysctl.conf` if you use the default file (not recommended)). To apply the changes, run the corresponding Linux command.

```sh
 vm.max_map_count=524288
 fs.file-max=131072
```

3\. To change the limits on the user running SonarQube Server, insert the following in /etc/security/limits.d/99-sonarqube.conf (or in /etc/security/limits.conf if you use the default file (not recommended)) where SonarQube Server is the user used to run SonarQube Server. To apply the changes, run the corresponding Linux command.

```sh
sonarqube   -   nofile   131072
sonarqube   -   nproc    8192
```

</details>

<details>

<summary>For a systemd user</summary>

Specify those limits inside your unit file in the section `[Service]` :

```sh
[Service]
...
LimitNOFILE=131072
LimitNPROC=8192
...
```

</details>

{% hint style="info" %}
To change these values dynamically for the current session, run the following commands as `root`:

```sh
sysctl -w vm.max_map_count=524288
sysctl -w fs.file-max=131072
ulimit -n 131072
ulimit -u 8192
```

{% endhint %}

#### Enabling seccomp on the Linux kernel <a href="#enabling-seccomp-on-the-linux-kernel" id="enabling-seccomp-on-the-linux-kernel"></a>

By default, Elasticsearch uses the seccomp filter. Make sure you use a kernel with seccomp enabled.

To check that seccomp is available on your kernel, use:

```sh
$ grep SECCOMP /boot/config-$(uname -r)
```

If your kernel has seccomp, you’ll see the following:

```sh
CONFIG_HAVE_ARCH_SECCOMP_FILTER=y
CONFIG_SECCOMP_FILTER=y
CONFIG_SECCOMP=y
```

#### Elasticsearch filesystem requirements <a href="#fonts" id="fonts"></a>

Elasticsearch 8.x requires read and write access to the `/tmp` directory. This is a requirement from Elasticsearch itself and cannot be disabled.

This change affects you if your deployment uses read-only filesystem restrictions:

* Docker Compose with `read_only: true`
* Kubernetes with `readOnlyRootFilesystem: true`
* Any custom deployment with read-only filesystem policies including `/tmp`

When the `/tmp` directory is not writable you will see the following error:

```
java.lang.IllegalStateException: Unable to attach entitlement agent
Caused by: com.sun.tools.attach.AttachNotSupportedException: Unable to open socket file /tmp/.java_pid<PID>
```

**For Docker Compose**

You can keep your root filesystem read-only while providing a writable `/tmp` directory using a `tmpfs` mount (in-memory temporary filesystem).

<details>

<summary>Developer / Enterprise editions</summary>

```
services:
  sonarqube:
    image: sonarqube:2025.1-community
    read_only: true
    environment:
      SONAR_JDBC_URL: jdbc:postgresql://db:5432/sonar
      SONAR_JDBC_USERNAME: sonar
      SONAR_JDBC_PASSWORD: sonar
    volumes:
      - sonarqube_data:/opt/sonarqube/data
      - sonarqube_logs:/opt/sonarqube/logs
      - sonarqube_temp:/opt/sonarqube/temp
    tmpfs:
      - /tmp:size=256M,mode=1777  # Add this line
volumes:
  sonarqube_data:
  sonarqube_logs:
  sonarqube_temp:
```

</details>

<details>

<summary>Data Center Edition (Search Nodes)</summary>

```
services:
  search-1:
    read_only: true
    environment:
      SONAR_JDBC_URL: jdbc:postgresql://db:5432/sonar
      SONAR_JDBC_USERNAME: sonar
      SONAR_JDBC_PASSWORD: sonar
      SONAR_CLUSTER_ES_HOSTS: "search-1,search-2"
      SONAR_CLUSTER_NODE_NAME: "search-1"
    volumes:
      - search_data-1:/opt/sonarqube/data
      - search_temp-1:/opt/sonarqube/temp
    tmpfs:
      - /tmp:size=256M,mode=1777  # Add this line
volumes:
  search_data-1:
  search_temp-1:
```

</details>

### Managing SonarQube Server access to fonts <a href="#fonts" id="fonts"></a>

Generating executive reports requires that fonts be installed on the server hosting SonarQube Server.

If you use a Linux server, you should ensure that Fontconfig is installed on the server host.

{% hint style="info" %}
A package of FreeType fonts is installed on the SonarQube Server host. The exact packages available will vary by distribution, but a commonly used package is libfreetype6.
{% endhint %}

### If using an Oracle database <a href="#if-oracle" id="if-oracle"></a>

In case your SonarQube Server is running on Linux and you are using Oracle, the Oracle JDBC Driver may be blocked due to `/dev/random`. See [this Oracle article](http://www.usn-it.de/index.php/2009/02/20/oracle-11g-jdbc-driver-hangs-blocked-by-devrandom-entropy-pool-empty/) for more details about this problem.

To avoid it, you may want to add this JVM parameter to your SonarQube Server’s web server (`sonar.web.javaOpts`) configuration:

```sh
-Djava.security.egd=file:///dev/urandom
```

### Configuring SonarQube Server to run in FIPS mode <a href="#fips-mode" id="fips-mode"></a>

SonarQube Server on RedHat Linux can run in FIPS (Federal Information Processing Standard) mode with some limitations. The FIPS mode may require an update of your webhooks configuration as explained below.

#### Known limitations of the FIPS mode <a href="#known-limitations-of-the-fips-mode" id="known-limitations-of-the-fips-mode"></a>

A FIPS-enabled SonarQube Server presents the following known limitations.

* Elasticsearch authentication in the Data Center Edition of SonarQube Server will not work on FIPS because PEM certificates are not supported as of today (but we plan to bring this support in the future).
* SAML authentication with signature and encryption of the assertion is not supported yet.

#### Updating the webhooks configuration <a href="#updating-the-webhooks-configuration" id="updating-the-webhooks-configuration"></a>

In the FIPS mode, the webhook secrets must be at least 16 characters long; otherwise, the webhook messages will not be sent to the FIPS environment.

Proceed as follows:

* Check that the secret of each existing webhook is at least 16 characters long. If it’s not the case, update it. See [webhooks](https://docs.sonarsource.com/sonarqube-server/project-administration/webhooks "mention").

{% hint style="info" %}
If you create a new webhook with a secret, you’ll be forced to enter a secret of at least 16 characters.
{% endhint %}
