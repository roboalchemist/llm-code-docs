# Source: https://docs.pentaho.com/pdc-10.2-install/install-pentaho-data-catalog/upgrade-data-catalog.md

# Upgrade Data Catalog

Upgrading Pentaho Data Catalog ensures that you can take advantage of the latest features,  improvements, and security updates while maintaining your existing configurations and data. This section provides step-by-step instructions to upgrade your Data Catalog deployment from earlier versions to newer releases.

## Supported upgrades

Pentaho Data Catalog supports upgrades only across the next two versions. You can upgrade directly to the immediate next version or the version after that, but skipping more than two versions in a single upgrade is not supported. If your target version is more than two versions ahead, you must perform the upgrade in multiple stages by first upgrading to an intermediate supported version and then moving to the final target version.

The following matrix shows the supported upgrade paths:

<table><thead><tr><th>From \ To</th><th>10.2.1</th><th>10.2.5</th><th>10.2.6</th><th width="128">10.2.7</th><th>10.2.8</th><th>10.2.9</th><th>10.2.11</th></tr></thead><tbody><tr><td><strong>10.2.0</strong></td><td>✅ Direct</td><td>❌</td><td>❌</td><td>❌</td><td>❌</td><td></td><td></td></tr><tr><td><strong>10.2.1</strong></td><td>—</td><td>✅ Direct</td><td>❌<br>via 10.2.5</td><td>❌ <br>via 10.2.5 → 10.2.7</td><td>❌ <br>via 10.2.5 → 10.2.8</td><td></td><td></td></tr><tr><td><strong>10.2.5</strong></td><td>—</td><td>—</td><td>✅ Direct</td><td>✅ Direct</td><td>❌</td><td>—</td><td></td></tr><tr><td><strong>10.2.6</strong></td><td>—</td><td>—</td><td>—</td><td>✅ Direct</td><td>✅ Direct</td><td>—</td><td>—</td></tr><tr><td><strong>10.2.7</strong></td><td>—</td><td>—</td><td>—</td><td>—</td><td>✅ Direct</td><td>✅ Direct</td><td>—</td></tr><tr><td><strong>10.2.8</strong></td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>✅ Direct</td><td>✅ Direct</td></tr><tr><td><strong>10.2.9</strong></td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>✅ Direct</td></tr></tbody></table>

{% hint style="warning" %}
To avoid problems, always back up configuration files and Docker volumes before upgrading, and review any custom changes in Docker compose files so they can be reapplied after extracting the new package.
{% endhint %}

## Upgrade procedures

The topics in this section guide you through the specific upgrade paths supported for Pentaho Data Catalog 10.2.x:

* [#upgrade-pdc-10.2.5-to-10.2.6-10.2.7-10.2.8-10.2.9-or-10.2.11](#upgrade-pdc-10.2.5-to-10.2.6-10.2.7-10.2.8-10.2.9-or-10.2.11 "mention"): Follow this procedure if your current deployment is on version 10.2.5 and you want to upgrade to 10.2.6, 10.2.7, 10.2.8, or 10.2.9.
* [#upgrade-pdc-10.2.1-to-10.2.5](#upgrade-pdc-10.2.1-to-10.2.5 "mention"): Follow this procedure if your current deployment is on version 10.2.1 and you want to upgrade to 10.2.5.
* [#upgrade-pdc-10.2.0-to-10.2.1](#upgrade-pdc-10.2.0-to-10.2.1 "mention"): Follow this procedure if your current deployment is on version 10.2.0 and you want to upgrade to 10.2.1.

{% hint style="info" %}
If you want to upgrade Data Catalog to a patch version, see [upgrade-data-catalog-to-a-patch-version](https://docs.pentaho.com/pdc-10.2-install/install-pentaho-data-catalog/upgrade-data-catalog/upgrade-data-catalog-to-a-patch-version "mention").
{% endhint %}

Before starting, ensure you review the prerequisites, back up your configuration and data, and prepare the deployment environment as described in the respective upgrade topics.

### Upgrade PDC 10.2.5 to 10.2.6, 10.2.7, 10.2.8, 10.2.9, or 10.2.11

Upgrading Pentaho Data Catalog (PDC) to the latest version ensures access to new features, improved performance, and security updates.

Perform the following steps to upgrade from PDC 10.2.5 to PDC 10.2.6, 10.2.7, 10.2.8, 10.2.9, or 10.2.11:

**Prerequisites**

Before you begin, make sure that:

* PDC 10.2.5 or higher version is installed. For the new installation of Data Catalog, see [Installing Data Catalog](https://docs.pentaho.com/pdc-10.2-install/install-pentaho-data-catalog).
* You have a backup of your configurations and data.
* You have administrative access to the server where Data Catalog is installed.

{% hint style="info" %}
Data Catalog supports upgrades only across the next two versions. From version 10.2.5, you can upgrade directly to 10.2.6 or 10.2.7. Direct upgrade from 10.2.5 to 10.2.8, 10.2.9, or 10.2.11 is not supported. To move to 10.2.11, you must first upgrade to 10.2.8 and then perform a second upgrade to 10.2.9 or 10.2.11. For details, see the [#supported-upgrades](#supported-upgrades "mention") section.
{% endhint %}

**Procedure**

1. Go to the Data Catalog installation folder, where PDC 10.2.5 or higher version is installed:

   ```
   cd /opt/pentaho/pdc-docker-deployment/
   ```
2. Stop the currently running PDC services.

   ```
   ./pdc.sh stop
   ```
3. Back up configuration files:
   1. Create a backup folder in `/opt/` to store the container data and configuration backups:

      ```
      mkdir /opt/pdc_backup_10_2_5
      ```
   2. Copy the `config` folder to the backup folder you have created:

      ```
      cp -a /opt/pentaho/pdc-docker-deployment/conf/ /opt/pdc_backup_10_2_5
      ```
   3. Copy the `vendor` folder to the backup folder you have created:

      ```
      cp -a /opt/pentaho/pdc-docker-deployment/vendor/ /opt/pdc_backup_10_2_5
      ```
4. Back up Docker volumes:
   1. Identify PDC Docker volumes:

      ```
      docker volume ls | grep 'pdc*'
      ```
   2. Go to the Docker volumes path:

      ```
      cd /var/lib/docker/volumes/
      ```
   3. Copy PDC Docker volumes to the backup folder:

      ```
      cp -a pdc* /opt/pdc_backup_10_2_5/
      ```
5. Verify that all configuration files and Docker volumes are backed up correctly in the backup folder.
6. Remove the `vendor` folder of PDC 10.2.5 build:

   ```
   rm –rf /opt/pentaho/pdc-docker-deployment/vendor/
   ```
7. Load the new images (choose either 10.2.6, 10.2.7, 10.2.8, 10.2.9, or 10.2.11) into the Docker repository:

   ```
   docker load -i pdc-<version>-images.tgz
   ```

   Replace `<version>` with `10.2.6`, `10.2.7`, `10.2.8`, `10.2.9` , or `10.2.11` depending on the upgrade target.
8. Extract the contents of the new package and overwrite the existing files in the deployment folder (`/opt/pentaho/pdc-docker-deployment/`):

   **Important:** Before overriding the files, review any custom configurations made in the Docker compose files and ensure those changes are noted and applied to the new files.

   ```
   tar -xzvf pdc-<DEPLOYMENT_PACKAGE_TYPE>-<version>-compose.tgz -C /opt/
   ```

   The `<DEPLOYMENT_PACKAGE_TYPE>` placeholder corresponds to the type of PDC service you want to deploy. For example, in the case of PDC 10.2.6:

   * For PDC full services, use: `pdc-full-10.2.6-compose.tgz`
   * For PDC with Pentaho Data Optimizer services, use: `pdc-pdo-10.2.6-compose.tgz`
   * For PDC with Pentaho Data Mastering services, use: `pdc-pdm-10.2.6-compose.tgz` .&#x20;

   Similarly, for PDC 10.2.7, replace it with 10.2.7, for PDC 10.2.8, replace it with 10.2.8, for PDC 10.2.9, replace it with 10.2.9, or for PDC 10.2.11, replace it with 10.2.11. If you are unsure which deployment package to use, contact [Pentaho Support](https://support.pentaho.com/) for guidance.
9. Start PDC services with the new version:

   ```
   ./pdc.sh up
   ```

**Result**

You have successfully upgraded Pentaho Data Catalog version 10.2.5 to 10.2.6, 10.2.7, 10.2.8, 10.2.9, or 10.2.11.

### Upgrade PDC 10.2.1 to 10.2.5

Upgrading Pentaho Data Catalog (PDC) to the latest version ensures access to new features, improved performance, and security updates.

Perform the following steps to upgrade from PDC 10.2.1 to PDC 10.2.5:

**Prerequisites**

Before you begin, make sure that:

* PDC 10.2.1 is installed. For the new installation of Data Catalog, see [Installing Data Catalog](https://docs.pentaho.com/pdc-10.2-install/install-pentaho-data-catalog/install-data-catalog).
* You have a backup of your configurations and data.
* You have administrative access to the server where Data Catalog is installed.

**Procedure**

1. Go to the Data Catalog installation folder, where PDC 10.2.1 is installed:

   ```
   cd /opt/pentaho/pdc-docker-deployment/
   ```
2. Stop the currently running PDC services.

   ```
   ./pdc.sh stop
   ```
3. Back up configuration files:
   1. Create a backup folder in `/opt/` to store the container data and configuration backups:

      ```
      mkdir /opt/pdc_backup_10_2_1
      ```
   2. Copy the `config` folder to the backup folder you have created:

      ```
      cp -a /opt/pentaho/pdc-docker-deployment/conf/ /opt/ pdc_backup_10_2_1
      ```
   3. Copy the `vendor` folder to the backup folder you have created:

      ```
      cp -a /opt/pentaho/pdc-docker-deployment/vendor/ /opt/ pdc_backup_10_2_1
      ```
4. Back up Docker volumes:
   1. Identify PDC Docker volumes:

      ```
      docker volume ls | grep pdc*
      ```
   2. Go to the Docker volumes path:

      ```
      cd /var/lib/docker/volumes/
      ```
   3. Copy PDC Docker volumes to the backup folder:

      ```
      cp -a pdc* /opt/pdc_backup_10_2_1/
      ```
5. Verify that all configuration files and docker volumes are backed up correctly in the backup folder.
6. Remove the `vendor` folder of PDC 10.2.1 build:

   ```
   rm –rf /opt/pentaho/pdc-docker-deployment/vendor
   ```
7. Load the PDC 10.2.5 images into the Docker repository:

   ```
   docker load –i pdc-10.2.5-images.tgz
   ```
8. Extract the contents of the PDC 10.2.5 package and overwrite the existing files in the deployment folder (`/opt/pentaho/pdc-docker-deployment/`):

   **Important:** Before overriding the files, review any custom configurations made in the Docker compose files and ensure those changes are noted and applied to the new files.

   ```
   tar -xzvf pdc-<DEPLOYMENT_PACKAGE_TYPE>-10.2.5-compose.tgz -C /opt/
   ```

   The `<DEPLOYMENT_PACKAGE_TYPE>` placeholder corresponds to the type of PDC service you want to deploy. For example:

   * For PDC full services, use: `pdc-full-10.2.5-compose.tgz`
   * For PDC with Pentaho Data Optimizer services, use: `pdc-pdo-10.2.5-compose.tgz`
   * For PDC with Pentaho Data Mastering services, use: `pdc-pdm-10.2.5-compose.tgz` If you are unsure which deployment package to use, contact [Pentaho Support](https://support.pentaho.com/) for guidance.
9. Start PDC services with the new version:

   ```
   ./pdc.sh up
   ```

**Result**

You have successfully upgraded PDC version 10.2.1 to 10.2.5.

### Upgrade PDC 10.2.0 to 10.2.1

Upgrading Pentaho Data Catalog (PDC) to the latest version ensures access to new features, improved performance, and security updates.

Perform the following steps to upgrade from PDC 10.2.0 to PDC 10.2.1:

**Prerequisites**

Before you begin, make sure you have a backup of your configurations and data, and you have administrative access to the server where Data Catalog is installed.

**Procedure**

1. Go to the Data Catalog installation directory, where PDC 10.2.0 is installed.

   ```
   cd /opt/pentaho/pdc-docker-deployment/
   ```
2. Stop the currently running PDC services.

   ```
   ./pdc.sh stop
   ```
3. Back up configuration files:
   1. Create a backup folder in `/opt/` to store the container data and configuration backups:

      ```
      mkdir pdc_backup_10_2_0
      ```
   2. Copy the `config` directory to the backup folder you have created:

      ```
      cp -a /opt/pentaho/pdc-docker-deployment/conf/ /opt/pdc_backup_10_2_0/
      ```
4. Back up Docker volumes:
   1. Identify PDC Docker volumes:

      ```
      docker volume ls | grep pdc*
      ```
   2. Go to the Docker volumes directory:

      ```
      cd /var/lib/docker/volumes/
      ```
   3. Copy PDC Docker volumes to the backup folder.

      ```
      cp -a pdc* /opt/pdc_backup_10_2_0/
      ```
5. Verify that all configuration files and docker volumes are backed up correctly in the backup folder.
6. Extract the contents of the PDC 10.2.1 package and overwrite the existing files in the deployment directory (`/opt/pentaho/pdc-docker-deployment/`):

   **Important:** Before overriding the files, review any custom configurations made in the Docker-compose files and ensure those changes are noted and applied to the new files.

   ```
   tar -xzvf pdc-10.2.0.tar.gz -C /opt/
   ```
7. Open the `.env` file located in the `/opt/pentaho/pdc-docker-deployment/conf/` path and add or update the licensing URL in a line such as the following, and save the `.env` file.

   ```
   LICENSING_SERVER_URL=<your_license_server_url>
   ```
8. After updating the configurations, load the Docker images for PDC 10.2.1.

   ```
   ./pdc.sh load-images
   ```
9. Start PDC services with the new version:

   ```
   ./pdc.sh up
   ```

**Result**

You have successfully upgraded PDC from 10.2.0 to 10.2.1.
