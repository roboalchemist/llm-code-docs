# Source: https://docs.sonarsource.com/sonarqube-community-build/server-update-and-maintenance/troubleshooting/performance-issues.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/server-upgrade-and-maintenance/troubleshooting/performance-issues.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/server-update-and-maintenance/troubleshooting/performance-issues.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-update-and-maintenance/troubleshooting/performance-issues.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-update-and-maintenance/troubleshooting/performance-issues.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/troubleshooting/performance-issues.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-update-and-maintenance/troubleshooting/performance-issues.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-update-and-maintenance/troubleshooting/performance-issues.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/troubleshooting/performance-issues.md

# Performance issues

In case of performance issues, you may try the following:

* Review the [server-host-requirements](https://docs.sonarsource.com/sonarqube-server/server-installation/server-host-requirements "mention") for SonarQube Server linked to **Elasticsearch** usage.
* Move the Elasticsearch storage to a storage with high IOPS and low latency. See [#configure-es-storage-path](https://docs.sonarsource.com/sonarqube-server/server-installation/from-zip-file/basic-installation#configure-es-storage-path "mention") for more information.
* Set the [housekeeping](https://docs.sonarsource.com/sonarqube-server/instance-administration/system-functions/housekeeping "mention") with a reduced retention time, to limit the database size.
* Configure the analysis scope to reduce the number of files analyzed, leading to shorter analysis and smaller database footprint. See [introduction](https://docs.sonarsource.com/sonarqube-server/project-administration/adjusting-analysis/setting-analysis-scope/introduction "mention") for more information.
* From the [Enterprise Edition](https://www.sonarsource.com/plans-and-pricing/enterprise/): increase the number of Compute Engine workers and/or configure the Compute Engine to enable parallel processing of pull requests and branch analyses for each project. See [improving-performance](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/maintenance/improving-performance "mention").
* For the Data Center Edition on Kubernetes: set up autoscaling. See [setting-up-autoscaling](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-autoscaling "mention") for more details.
* If performance issues occur after a PostgreSQL database upgrade, try reindexing the following database tables: issues, rules, and components.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [server-logs](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/troubleshooting/server-logs "mention")
* [database-related-issues](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/troubleshooting/database-related-issues "mention")
* [elasticsearch](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/troubleshooting/elasticsearch "mention")
* [other-issues](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/troubleshooting/other-issues "mention")
* [improving-performance](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/maintenance/improving-performance "mention")
