# Source: https://docs.api7.ai/enterprise/high-availability/prepare-for-high-availability.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/high-availability/prepare-for-high-availability.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/high-availability/prepare-for-high-availability.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/high-availability/prepare-for-high-availability.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/high-availability/prepare-for-high-availability.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/high-availability/prepare-for-high-availability.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/high-availability/prepare-for-high-availability.md

# Source: https://docs.api7.ai/enterprise/3.8.x/high-availability/prepare-for-high-availability.md

# Source: https://docs.api7.ai/enterprise/3.7.x/high-availability/prepare-for-high-availability.md

# Source: https://docs.api7.ai/enterprise/3.6.x/high-availability/prepare-for-high-availability.md

# Source: https://docs.api7.ai/enterprise/3.5.x/high-availability/prepare-for-high-availability.md

# Source: https://docs.api7.ai/enterprise/3.4.x/high-availability/prepare-for-high-availability.md

# Source: https://docs.api7.ai/enterprise/3.3.x/high-availability/prepare-for-high-availability.md

# Prepare for High Availability

This document describes recommended options for configuring high availability (HA).

## Get Installation Packages[â](#get-installation-packages "Direct link to Get Installation Packages")

Please [contact](https://api7.ai/contact) API7 experts to get proper installation packages for you.

## Prepare the Host Machines[â](#prepare-the-host-machines "Direct link to Prepare the Host Machines")

To deploy an API7 Enterprise high availability architecture, a minimum of 4 host machines is required (2 for control plane high availability, and 2 for data plane high availability).

Please note that while database high availability is an important aspect to consider, it is not covered in the documentation. It is advisable to separately address this crucial aspect to ensure the resilience and fault tolerance of your data storage system. For details about how to configure high availability for PostgreSQL, see [PostgreSQL documentation](https://www.postgresql.org/docs/current/high-availability.html).

Prometheus is indeed an optional component, and it is utilized only when you wish to leverage the embedded monitoring feature of API7 Enterprise. For details about how to configure high availability for Prometheus, see [Prometheus documentation](https://prometheus.io/docs/introduction/faq/#can-prometheus-be-made-highly-available).

In practical scenarios, the high availability architecture may vary depending on specific cases. Please [contact](https://api7.ai/contact) API7 experts, who will be delighted to customize a solution tailored to your needs.

## Minimum Hardware Requirements[â](#minimum-hardware-requirements "Direct link to Minimum Hardware Requirements")

| Host     | Processor | CPU     | RAM | Free Disk Space | Deployed Components        |
| -------- | --------- | ------- | --- | --------------- | -------------------------- |
| CP Host1 | x86\_64   | 2 Cores | 4G  | 80 GB           | API7 Dashboard, DP Manager |
| CP Host2 | x86\_64   | 2 Cores | 4G  | 80 GB           | API7 Dashboard, DP Manager |
| DP Host3 | x86\_64   | 2 Cores | 4G  | 80 GB           | API7 Gateway               |
| DP Host4 | x86\_64   | 2 Cores | 4G  | 80 GB           | API7 Gateway               |

## Minimum Software Requirements[â](#minimum-software-requirements "Direct link to Minimum Software Requirements")

For each host, the following requirements must be met:

* Operating system: It is recommended to use Linux CentOS 7.6 or higher versions. It is known that Linux CentOS 7.2 or previous versions are incompatible.
* Linux Kernel: It is recommended to use 3.10.0-927 or higher versions. It is known that 3.10.0-327 or previous versions are incompatible.

## Security[â](#security "Direct link to Security")

As you should expose nodes for each component, you should configure SELinux and firewall on these hosts.

| Components     | Ports | Description                                                                                                                         |
| -------------- | ----- | ----------------------------------------------------------------------------------------------------------------------------------- |
| API7 Gateway   | 9080  | Listen for user HTTP requests                                                                                                       |
| API7 Gateway   | 9443  | Listen for user HTTPS requests                                                                                                      |
| API7 Dashboard | 7080  | User Interface for Administrators                                                                                                   |
| DP Manager     | 7900  | Manage nodes on the data plane, including applying configurations, performing heartbeat checks, and reporting metrics to Prometheus |
| Prometheus     | 9090  | Collect and show API7 metrics                                                                                                       |
| PostgreSQL     | 5432  | Version 15, Store configuration data, and can be replaced with other relational databases such as MySQL 5.7 or OceanBase 4.2.2      |
