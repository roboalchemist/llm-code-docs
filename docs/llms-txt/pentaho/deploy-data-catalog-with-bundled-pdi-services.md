# Source: https://docs.pentaho.com/pdc-10.2-install/install-pentaho-data-catalog/install-data-catalog/deploy-data-catalog-with-bundled-pdi-services.md

# Deploy Data Catalog with bundled PDI services

Data Pipe templates in Data Catalog let you move data between different data sources. The execution of these pipelines is powered by the Pentaho Data Integration (PDI) engine. In earlier versions, Data Catalog had to be configured with a separate PDI installation to run Data Pipes, which added deployment complexity.

Starting with version 10.2.7, PDC bundles two PDI services, Tray and Carte, within the Docker deployment. Carte acts as the execution engine to run transformations and jobs, while Tray serves as the controller and load balancer, receiving requests from Data Catalog, distributing them to Carte, and monitoring job execution. Together, Tray and Carte form the runtime layer for Data Pipes, eliminating the need for separate installation, ensuring version alignment, and simplifying production deployment.

Perform the following steps to deploy Data Catalog bundled with Carte and Tray in a single flow using the provided Docker images and deployment package:

**Prerequisites**

Before you begin:

* Ensure Docker and Docker Compose are installed and running on your host.
* Obtain credentials for the Hitachi JFrog repository. If you do not have JFrog credentials, contact your system administrator or Pentaho Support.
* Collect valid Data Catalog and PDI license URLs.
* Obtain the es-license-key.txt file from Sales Operations for the Tray server.
* Prepare any required JDBC drivers for your environment.

**Procedure**

1. Download the container images from the JFrog repository.

   <pre data-overflow="wrap"><code>curl -u &#x3C;jfrog_username>:&#x3C;jfrog_token> -L -O "https://hitachi.jfrog.io/artifactory/pdc-generic-release/pentaho/pdc-docker-deployment/release-v&#x3C;version>/pdc-&#x3C;version>-images.tgz"
   </code></pre>
2. Load the downloaded container images into Docker.

   ```
   sudo docker image load -i pdc-<version>-images.tgz
   ```

   \
   This makes the Data Catalog and Data Pipes images available locally for deployment.
3. Download the deployment bundle from the JFrog repository.

   <pre data-overflow="wrap"><code>curl -u &#x3C;jfrog_username>:&#x3C;jfrog_token> -L -O "https://hitachi.jfrog.io/artifactory/pdc-generic-release/pentaho/pdc-docker-deployment/release-v&#x3C;version>/pdc-full-&#x3C;version>-compose.tgz"
   </code></pre>
4. Extract the deployment bundle into the /opt directory.

   ```
   sudo tar -xvf pdc-full-<version>-compose.tgz -C /opt/
   ```

   \
   The extraction creates a pentaho/pdc-docker-deployment directory with all required files.
5. Navigate to the deployment directory.

   ```
   cd /opt/pentaho/pdc-docker-deployment/
   ```
6. Run the helper script to specify the application hostname.

   ```
   sudo ./pdc.sh
   ```

   \
   This command will provide a list of hostnames.

   1. If the required hostname is present in the list, enter the corresponding number.
   2. If the required hostname is not in the list, enter a number that has another value, press Enter, and enter the hostname.
7. Edit the .env file to configure license details.

   ```
   sudo vi /opt/pentaho/pdc-docker-deployment/conf/.env
   ```

   \
   Add the following entries and close the vi editor.

   ```
   LICENSING_SERVER_URL=<PDC License>

   PDI_LICENSE_URL=<pdi_license_url>
   ```
8. Place the ES license file for the tray component in the following directory.

   ```
   /opt/pentaho/pdc-docker-deployment/conf/datapipes/tray/es-license-key.txt
   ```

   \
   Obtain these license files from Sales Operations, as it is generated based on customer contract terms.
9. Copy the required JDBC drivers into the `jdbc_drivers/lib` folder.

   ```
   /opt/pentaho/pdc-docker-deployment/conf/datapipes/jdbc_drivers/lib
   ```

   \
   Use the same JDBC drivers supported by Data Catalog for your database connections.
10. Start the deployment to bring up all services.

    ```
    sudo ./pdc.sh up
    ```

**Result**

This initiates the Data Catalog stack, including the integrated PDI services: Carte and Tray.  Both Tray and Carte services run as Docker containers within the PDC stack. You can verify this by running:

```
docker ps
```

All Data Catalog services, along with Carte and Tray, should be listed as running. Access Data Catalog in a browser at the hostname you configured.

**Next steps**

To confirm Data Pipes connectivity, log in to Data Catalog and try to create a data pipe template with the Data Integration engine. For more information, see Create a data pipe template in the Administer Pentaho Data Catalog guide. To know more, see [Data Pipe Templates](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/pdc-data-pipe-templates) in [Use Pentaho Data Catalog](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/) guide.
