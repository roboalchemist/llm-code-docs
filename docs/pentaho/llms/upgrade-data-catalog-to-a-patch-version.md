# Source: https://docs.pentaho.com/pdc-10.2-install/install-pentaho-data-catalog/upgrade-data-catalog/upgrade-data-catalog-to-a-patch-version.md

# Upgrade Data Catalog to a patch version

This document provides the steps required to upgrade Pentaho Data Catalog (PDC) to a specific patch version. Applying a patch ensures that your environment receives the latest defect fixes, performance improvements, and security updates, while maintaining compatibility with the corresponding GA version.

Each patch release includes two components:

* **pdc-\<version>-cp.\<patch number>-images.tgz**: A file containing the Docker images included in the patch release.
* **pdc-\<version>-cp.\<patch number>.patch**: A smaller text file with the Docker image tags that need updating.

**Prerequisites**

Before you begin, ensure:

* You have administrative access to the server where Data Catalog is installed.
* The GA version related to the patch must be installed on your server. For example, if you are installing a PDC 10.2.7 patch, you must first have PDC 10.2.7 GA installed.
* You have a backup of your configuration and data.
* The `pdc-<version>-cp.<patch number>-images.tgz` and `pdc-<version>-cp.<patch number>.patch` files must be placed in the Data Catalog server.
* PDC is installed via Docker at `/opt/pentaho/pdc-docker-deployment`.

**Assumptions**

It is assumed that Data Catalog has been installed with Docker at the installation path: `/opt/pentaho/pdc-docker-deployment`

**Procedure**

Perform the following steps to upgrade Data Catalog to a specific patch version:

1. Go to the Data Catalog installation folder, where Data Catalog is installed.

   ```bash
   cd /opt/pentaho/pdc-docker-deployment/
   ```
2. Stop the currently running Data Catalog services.

   ```bash
   ./pdc.sh stop
   ```
3. Back up configuration files:
   1. Create a backup folder in `/opt`  to store the container data and configuration backups.

      ```bash
      mkdir /opt/pdc_backup_<pdc_version>
      ```
   2. Copy the `config` folder to the backup folder you have created.

      ```bash
      cp -a /opt/pentaho/pdc-docker-deployment/conf/ /opt/pdc_backup_<pdc_version>
      ```
   3. Copy the `vendor` folder to the backup folder you have created:

      ```bash
      cp -a /opt/pentaho/pdc-docker-deployment/vendor/ /opt/pdc_backup_<pdc_version>
      ```
4. Back up Docker volumes:
   1. Identify Data Catalog Docker volumes.

      ```bash
      docker volume ls | grep pdc*
      ```
   2. Go to the Docker volumes path.

      ```bash
      cd /var/lib/docker/volumes
      ```
   3. Copy Data Catalog Docker volumes to the backup folder:

      ```bash
      cp -a pdc* /opt/pdc_backup_<pdc_version>/
      ```
5. Verify that all configuration files and Docker volumes are backed up correctly in the backup folder.
6. Load the new images into the Docker repository.

   ```bash
   docker load -i pdc-<version>-cp.<patch number>-images.tgz
   ```
7. Apply the patch using the correct method for your version.
   * **For versions prior to 10.2.8**: back up `.env.default` and update it with the new tags from the patch file.

     ```bash
     cp vendor/.env.default vendor/.env.default.bkp
     ```

     <pre><code><strong>awk -F= 'NR==FNR {a[$1]=$2; next} $1 in a {$2=a[$1]}1' OFS== \
     </strong>  &#x3C;path-to-patch>/pdc-&#x3C;version>-cp.&#x3C;patch number>.patch \
       vendor/.env.default.bkp > vendor/.env.default
     </code></pre>
   * **For versions 10.2.8 and later**: run the patch helper.

     ```bash
     ./pdc.sh apply-patch pdc-<version>-cp.<patch number>.patch
     ```
8. Start PDC services.

   ```bash
   ./pdc.sh up
   ```
9. Log in to Data Catalog and navigate to the Management section, then confirm that the version has been updated to match the patch version.<br>

   <figure><img src="https://1897852526-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNjj4joO63OgOTabje2xP%2Fuploads%2F7JBvuOFJewPRpI1KAKMW%2Fimage.png?alt=media&#x26;token=27ee927f-63f4-403a-beb6-1e6e0994ffac" alt="" width="563"><figcaption></figcaption></figure>
10. Repeat steps from 1 to 9 on each server that runs a PDC remote worker.

**Result**

You have successfully upgraded the Data Catalog patch version.

You can also refer to the [Advanced configuration](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/ldc-advanced-configuration-ut_cp "mention") section in the [Administer Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/cUaDtyTop3vo8cjqgjGk/) guide for additional configurations required.
