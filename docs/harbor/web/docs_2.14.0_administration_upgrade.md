# Harbor docs | Upgrade Harbor and Migrate Data

**Source:** https://goharbor.io/docs/2.14.0/administration/upgrade/

Upgrade Harbor and Migrate Data

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
  * [Upgrading Harbor Deployed with Helm](/docs/2.14.0/administration/upgrade/helm-upgrade/)
  * [Roll Back from an Upgrade](/docs/2.14.0/administration/upgrade/roll-back-upgrade/)
  * [Test Harbor Upgrade](/docs/2.14.0/administration/upgrade/upgrade-test/)
* [Backup And Restore Harbor With Velero](/docs/2.14.0/administration/backup-restore/)

[Working with Projects](/docs/2.14.0/working-with-projects/)

[Building, Customizing, and Contributing to Harbor](/docs/2.14.0/build-customize-contribute/)

This guide covers upgrade and migration to v2.14.0. This guide only covers migration from v2.11.0 and later to the current version. If you are upgrading from an earlier version, refer to the migration guide for an earlier Harbor version.

* [Upgrade to Harbor v2.12.0](/docs/2.12.0/administration/upgrade/)
* [Upgrade to Harbor v2.11.0](/docs/2.11.0/administration/upgrade/)
* [Upgrade to Harbor v2.10.0](/docs/2.10.0/administration/upgrade/)
* [Upgrade to Harbor v2.9.0](/docs/2.9.0/administration/upgrade/)
* [Upgrade to Harbor v2.8.0](/docs/2.8.0/administration/upgrade/)
* [Upgrade to Harbor v2.7.0](/docs/2.7.0/administration/upgrade/)
* [Upgrade to Harbor v2.6.0](/docs/2.6.0/administration/upgrade/)
* [Upgrade to Harbor v2.5.0](/docs/2.5.0/administration/upgrade/)
* [Upgrade to Harbor v2.4.0](/docs/2.4.0/administration/upgrade/)
* [Upgrade to Harbor v2.3.0](/docs/2.3.0/administration/upgrade/)

If you are upgrading a Harbor instance that you deployed with Helm, see
[Upgrading Harbor Deployed with Helm](/docs/2.14.0/administration/upgrade/helm-upgrade/).

When upgrading an existing Harbor instance to a newer version, you might need to migrate the settings in `harbor.yml`.
Since the migration might alter the database schema and the settings of `harbor.yml`, you should **always** back up your data before any migration.

## Important Upgrade Notes

* Again, you MUST backup your data before any data migration.
* In Harbor v2.9, if you are using an external database, make sure the version of PostgreSQL >= 12.

## Upgrading Harbor and Migrating Data

1. Log in to the Harbor host and, if it is still running, stop and remove the existing Harbor instance.

   ```bash
   cd harbor
   docker compose down

   ```

2. Back up Harbor’s current files so that you can roll back to the current version if necessary.

   ```bash
   mv harbor /my_backup_dir/harbor

   ```

3. Back up the database, which by default is in the directory `/data/database`.

   ```bash
   cp -r /data/database /my_backup_dir/

   ```

4. Get the latest Harbor release package from
   <https://github.com/goharbor/harbor/releases> and extract it.

   For more information see
   [Download the Harbor Installer](/docs/2.14.0/install-config/download-installer/).
5. Before upgrading Harbor, perform migration.

   The migration tool is in harbor-prepare tools delivered as a docker image. You can pull the image from docker hub. in the following command:

   ```bash
   docker pull goharbor/prepare:[tag]
   ```

   Alternatively, if you are using an offline installer package, you can load it from the image tarball that is included in the offline installer package. Replace [tag] with the new Harbor version, for example v1.10.0, in the following command:

   ```bash
   tar zxf <offline package>
   docker image load -i harbor/harbor.[version].tar.gz

   ```

6. Copy the `/path/to/old/harbor.yml` to `harbor.yml` and upgrade it.

   ```bash
   docker run -it --rm -v /:/hostfs goharbor/prepare:[tag] migrate -i ${path to harbor.yml}
   ```

   **NOTE:** The schema upgrade and data migration of the database is performed by core when Harbor starts. If the migration fails, check the core log to debug.
7. In the `./harbor` directory, run the `./install.sh` script to install the new Harbor instance.

   To install Harbor with Trivy, see
   [Run the Installer Script](/docs/2.14.0/install-config/run-installer-script/) for more information.

If you need to roll back to the previous version of Harbor, see
[Roll Back from an Upgrade](/docs/2.14.0/administration/upgrade/roll-back-upgrade/).

---

## Pages in this section

* [Upgrading Harbor Deployed with Helm](/docs/2.14.0/administration/upgrade/helm-upgrade/)
* [Roll Back from an Upgrade](/docs/2.14.0/administration/upgrade/roll-back-upgrade/)
* [Test Harbor Upgrade](/docs/2.14.0/administration/upgrade/upgrade-test/)

On this page

Contributing

[Page source](https://github.com/goharbor/website/blob/release-2.14.0/docs/administration/upgrade/_index.md)
[Create issue](https://github.com/goharbor/harbor/issues)
