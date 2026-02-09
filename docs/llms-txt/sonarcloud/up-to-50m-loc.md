# Source: https://docs.sonarsource.com/sonarqube-server/10.6/setup-and-upgrade/reference-architectures/up-to-50m-loc.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/setup-and-upgrade/reference-architectures/up-to-50m-loc.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/setup-and-upgrade/reference-architectures/up-to-50m-loc.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/setup-and-update/reference-architectures/up-to-50m-loc.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/reference-architectures/up-to-50m-loc.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/reference-architectures/up-to-50m-loc.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/reference-architectures/up-to-50m-loc.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/reference-architectures/up-to-50m-loc.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/reference-architectures/up-to-50m-loc.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/reference-architectures/up-to-50m-loc.md

# Up to 50 M LOC

### Overview <a href="#overview" id="overview"></a>

This reference architecture covers the following components:

* A dedicated virtual machine with SonarQube Server Enterprise Edition installed and an nginx HTTPS proxy.
* PostgreSQL database on a dedicated host.
* Analysis integrated with Jenkins CI.
* Pull request reporting and authentication through GitHub Enterprise.
* Monitoring with Prometheus.
* Outbound email notifications using an SMTP relay.

<figure><img src="broken-reference" alt="Architecture schema of a SonarQube Server instance with a PostgreSQL database, connected through an Nginx proxy with CI/CD platform, SonarQube for IDE, Prometheus monitoring system. Data flow or access type are shown. Jenkins is used as CI tool."><figcaption></figcaption></figure>

This architecture favors the use of open-source components when available. These may be substituted with other similarly-capable components and it is recommended that organizations use components that they are comfortable supporting.

### SonarQube Server Host <a href="#sonarqube-host" id="sonarqube-host"></a>

The dedicated SonarQube Server Host will have the SonarQube Server software installed as well as nginx acting as an HTTPS proxy.

<details>

<summary>Host specification</summary>

* **VM configuration**:
  * 8 vCPU
  * 16 GB RAM
  * 50GB SSD Local Storage
* **AWS EC2**: c5d.2xlarge
* **Azure VM**: F8s\_v2
* **GCE**: c3-highcpu-8

</details>

<details>

<summary>Networking</summary>

By source/destination:

* **SonarQube Server host**:
  * **Direction**: Outbound
  * **Port**: 5432
  * **Purpose**: Database
* **SonarQube Server host**:
  * **Direction**: Outbound
  * **Port** (Protocol): 25 (SMTP)
  * **Purpose**: Email notifications
* **Internal network (user desktops):**
  * **Direction**: Inbound
  * **Port (Protocol):** 443 (HTTPS)
  * **Purpose:** Inbound web and API traffic
* **CI platform (Jenkins):**
  * **Direction**: Inbound
  * **Port (Protocol):** 443 (HTTPS)
  * **Purpose:** Analysis reports
* **DevOps platform (GitHub Enterprise):**
  * **Direction**: Inbound
  * **Port (Protocol):** 443 (HTTPS)
  * **Purpose:** Pull Request reports

</details>

<details>

<summary>Software</summary>

* OS - Ubuntu Server (or other Linux distribution)
* OpenJDK 17
* SonarQube Server Developer or Enterprise Edition
  * Four Compute Engine workers (see [Improving performance](https://app.gitbook.com/s/I10pmJWeVVXYITlQJllp/server-upgrade-and-maintenance/maintenance/improving-performance "mention"))
* nginx
  * Configured as a reverse proxy between incoming traffic and SonarQube Server port 9000.
  * Secured with SSL. Use of self-signed SSL certificates will require installation of the certificate on all CI build agents, and developer desktops using SonarQube for IDE.
  * May be substituted with other reverse proxy (ex. haproxy) or a solution from a cloud provider, such as an AWS Application Load Balancer (ALB).

</details>

### Database <a href="#database" id="database"></a>

This architecture utilizes a dedicated PostgreSQL database installed on a separate host.

<details>

<summary>Host specification</summary>

* **VM Configuration:**
  * 4vCPU
  * 16 GB RAM
  * 150 GB table space
* **AWS RDS:**
  * db.t3.xlarge
  * 150 GB table space
* **Azure SQL:**
  * B4ms
  * 150 GB table space
* **Google Cloud SQL:**
  * 4 vCPU
  * 16 GB memory
  * 150 GB table space

{% hint style="info" %}
If you use the Enterprise edition with the Advanced Security add-on, allocate 30% more table space.
{% endhint %}

</details>

Database requirements can vary widely based on the usage patterns of each SonarQube Server installation. Therefore, it is important to monitor and adjust database resources as needed.

PostgreSQL may be substituted with other supported database platforms.

### DevOps platform <a href="#devops-platform" id="devops-platform"></a>

SonarQube Server submits analysis reports back to pull requests to integrate with code review processes. This functionality is enabled in GitHub Enterprise using a GitHub App.

GitHub Enterprise may be substituted with other supported DevOps platforms without changes to other components in this architecture.

### CI/CD platform <a href="#ci-platform" id="ci-platform"></a>

Automated analysis of source code is enabled through the installation of the various SonarScanners into continuous integration pipelines. When using Jenkins, the SonarQube extension for Jenkins manages the installation of the scanners and provides functionality to ease the integration of Sonar analysis into build pipelines.

Other CI platforms may be used without changes to other components in this architecture.

### Authentication <a href="#authentication" id="authentication"></a>

It is recommended that authentication and authorization be handled through an external identity provider. The architecture utilizes the GitHub App to authorize users and synchronize access to SonarQube Server projects.

Other external identity providers such as SAML may be substituted. Features such as group and permission synchronization are not available for all authentication methods.

### Monitoring <a href="#monitoring" id="monitoring"></a>

SonarQube Server exposes endpoints that are easy to monitor using Prometheus or other monitoring solutions. In addition to the overall system health of both the SonarQube Server host and database, it is recommended to monitor SonarQube Server’s Compute Engine performance statistics to ensure incoming analyses are being promptly processed.

### Email notifications <a href="#notifications" id="notifications"></a>

Users can be notified of new issues and events via email. SonarQube Server will deliver these notifications through an SMTP mail relay. The volume of emails is low, dependent on the number of users subscribed, and a dedicated SMTP server is typically not required.

### Resiliency <a href="#resiliency" id="resiliency"></a>

As a single-host installation, this architecture relies on robust monitoring, automated backups of the database, and a rapid recovery process to maximize resiliency. If high availability is critical, SonarQube Server Data Center edition is recommended.

### Scalability <a href="#scalability" id="scalability"></a>

This architecture is designed to support typical production usage for up to 50 million lines of code. Beyond this, it is recommended that organizations use SonarQube Server Enterprise Edition or Data Center Edition to support high-volume workloads.

The following use cases are considered outside of "normal usage" and may require additional capacity:

<details>

<summary>High-frequency analysis</summary>

Normal usage assumes a daily scan of main branches and analysis of several pull requests. Scanning code more frequently may require an increase in the number of Compute Engine workers (using SonarQube Server Enterprise Edition) as well as additional memory and CPU resources allocated to SonarQube Server’s Compute Engine process. Monitoring of the Compute Engine process will ensure that your installation can keep up with demand.

</details>

<details>

<summary>Large repositories</summary>

This architecture assumes analyzed repositories average 50,000 lines of code. If your organization is scanning a majority of very large repositories (where the repositories average 500,000 lines of code or more), additional memory and CPU resources may be required for SonarQube Server’s Compute Engine process.

</details>

<details>

<summary>Heavy API integration</summary>

SonarQube Server exposes a REST-based API for reporting and automation of administration tasks. This architecture assumes occasional use of this API. Heavy use of this API may require the allocation of additional memory and CPU resources to SonarQube Server’s Web process.

</details>

<details>

<summary>Third-party plugins</summary>

This architecture assumes that no third-party plugins are in use. As these extensions are developed by non-sponsored developers, their impact on the performance of a SonarQube Server instance varies based on the function being performed and the quality of the implementation. It is recommended that the use of third-party plugins is carefully considered and monitored for performance throughout the life of your SonarQube Server implementation.

</details>

### Related pages <a href="#related-pages" id="related-pages"></a>

* [server-host-requirements](https://docs.sonarsource.com/sonarqube-server/server-installation/server-host-requirements "mention")
* [#database-requirements](https://docs.sonarsource.com/sonarqube-server/installing-the-database#database-requirements "mention")
* [..](https://docs.sonarsource.com/sonarqube-server/server-installation "mention")
* [securing-behind-proxy](https://docs.sonarsource.com/sonarqube-server/server-installation/network-security/securing-behind-proxy "mention")
* [github-integration](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/github-integration "mention")
* [set-up-monitoring](https://docs.sonarsource.com/sonarqube-server/server-installation/on-kubernetes-or-openshift/set-up-monitoring "mention")
