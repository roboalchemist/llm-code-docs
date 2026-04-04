# Harbor docs | Harbor Administration

**Source:** https://goharbor.io/docs/2.14.0/administration/

Harbor Administration

[Harbor version 2.14.0](/docs/2.14.0)

[Harbor Installation and Configuration](/docs/2.14.0/install-config/)

[Harbor Administration](/docs/2.14.0/administration/)

* [Configuring Authentication](/docs/2.14.0/administration/configure-authentication/)
* [Managing Users](/docs/2.14.0/administration/managing-users/)
* [Configure Global Settings](/docs/2.14.0/administration/general-settings/)
* [Configure Project Quotas](/docs/2.14.0/administration/configure-project-quotas/)
* [User-defined OCI artifact](/docs/2.14.0/administration/user-defined-oci-artifact/)
* [Configuring Replication](/docs/2.14.0/administration/configuring-replication/)
* [P2P Preheat](/docs/2.14.0/administration/p2p-preheat/)
* [Configure Proxy Cache](/docs/2.14.0/administration/configure-proxy-cache/)
* [Vulnerability Scanning](/docs/2.14.0/administration/vulnerability-scanning/)
* [Access Metrics](/docs/2.14.0/administration/metrics/)
* [Distributed Tracing](/docs/2.14.0/administration/distributed-tracing/)
* [Create System Robot Accounts](/docs/2.14.0/administration/robot-accounts/)
* [Garbage Collection](/docs/2.14.0/administration/garbage-collection/)
* [Audit Log](/docs/2.14.0/administration/audit-log/)
* [Log Rotation](/docs/2.14.0/administration/log-rotation/)
* [SBOM Generation Capabilities](/docs/2.14.0/administration/sbom-integration/)
* [Security Hub](/docs/2.14.0/administration/security-hub/)
* [Job Service Dashboard](/docs/2.14.0/administration/jobservice-dashboard/)
* [Upgrade Harbor and Migrate Data](/docs/2.14.0/administration/upgrade/)
* [Backup And Restore Harbor With Velero](/docs/2.14.0/administration/backup-restore/)

[Working with Projects](/docs/2.14.0/working-with-projects/)

[Building, Customizing, and Contributing to Harbor](/docs/2.14.0/build-customize-contribute/)

This section describes how to configure and maintain Harbor after deployment. These operations are performed by the Harbor system administrator. The Harbor system administrator performs global configuration operations that apply to the whole Harbor instance.

The operations that are performed by the Harbor system administrator are the following.

* Select database, LDAP/Active Directory, or OIDC based authentication. For information, see
  [Configuring Authentication](/docs/2.14.0/administration/configure-authentication/).
* Add users in database authentication mode and assign the system administrator role to other users. For information, see
  [Managing Users](/docs/2.14.0/administration/managing-users/).
* Configure global settings, such as setting the registry to read-only mode, and restriction who can create projects. For information, see
  [Configure Global Settings](/docs/2.14.0/administration/general-settings/).
* Apply resource quotas to projects. For information, see
  [Configure Project Quotas](/docs/2.14.0/administration/configure-project-quotas/).
* Set up replication of images between Harbor and another Harbor instance or a 3rd party replication target. For information, see
  [Configuring Replication](/docs/2.14.0/administration/configuring-replication/).
* Set up vulnerability scanners to check the images in the registry for CVE vulnerabilities. For information, see
  [Vulnerability Scanning](/docs/2.14.0/administration/vulnerability-scanning/).
* Perform garbage collection, to remove unnecessary data from Harbor. For information, see
  [Garbage Collection](/docs/2.14.0/administration/garbage-collection/).
* Manage audit logs by configuring an audit log retention window and setting a syslog endpoint to forward audit logs. For information, see
  [Log Rotation](/docs/2.14.0/administration/log-rotation/).
* Upgrade Harbor when a new version becomes available. For information, see
  [Upgrading Harbor](/docs/2.14.0/administration/upgrade/).
* Set up P2P preheat provider instances to preheat the specified images into the P2P network. For information, see
  [P2P preheat](/docs/2.14.0/administration/p2p-preheat/).
* Details of defining a user-defined OCI artifact so that Harbor can manage it. For information, see
  [user-defined OCI artifact](/docs/2.14.0/administration/user-defined-oci-artifact/).

---

## Subsections

* [Configuring Authentication](/docs/2.14.0/administration/configure-authentication/)
* [Managing Users](/docs/2.14.0/administration/managing-users/)
* [Configure Global Settings](/docs/2.14.0/administration/general-settings/)
* [Configure Project Quotas](/docs/2.14.0/administration/configure-project-quotas/)
* [User-defined OCI artifact](/docs/2.14.0/administration/user-defined-oci-artifact/)
* [Configuring Replication](/docs/2.14.0/administration/configuring-replication/)
* [P2P Preheat](/docs/2.14.0/administration/p2p-preheat/)
* [Configure Proxy Cache](/docs/2.14.0/administration/configure-proxy-cache/)
* [Vulnerability Scanning](/docs/2.14.0/administration/vulnerability-scanning/)
* [Access Metrics](/docs/2.14.0/administration/metrics/)
* [Distributed Tracing](/docs/2.14.0/administration/distributed-tracing/)
* [Create System Robot Accounts](/docs/2.14.0/administration/robot-accounts/)
* [Garbage Collection](/docs/2.14.0/administration/garbage-collection/)
* [Audit Log](/docs/2.14.0/administration/audit-log/)
* [Log Rotation](/docs/2.14.0/administration/log-rotation/)
* [SBOM Generation Capabilities](/docs/2.14.0/administration/sbom-integration/)
* [Security Hub](/docs/2.14.0/administration/security-hub/)
* [Job Service Dashboard](/docs/2.14.0/administration/jobservice-dashboard/)
* [Upgrade Harbor and Migrate Data](/docs/2.14.0/administration/upgrade/)
* [Backup And Restore Harbor With Velero](/docs/2.14.0/administration/backup-restore/)

Contributing

[Page source](https://github.com/goharbor/website/blob/release-2.14.0/docs/administration/_index.md)
[Create issue](https://github.com/goharbor/harbor/issues)
