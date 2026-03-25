# Source: https://docs.pentaho.com/pdc-10.2-install/install-pentaho-data-catalog/install-and-configure-a-remote-worker.md

# Install and configure a Remote Worker

The Remote Worker in Data Catalog provides a secure and scalable solution for metadata management, facilitating metadata extraction and task execution across distributed environments while complying with required network security requirements. For more information, see the [Remote Worker](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/pdc-remote-worker "mention") section in the [Use Pentaho Data Catalog](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/ "mention") guide.

Perform the following steps to install and configure a Remote Worker:

**Prerequisites**

* Ensure that Docker and Docker Compose are installed on the machine where the Remote Worker will be deployed.
* Ensure you have the latest Data Catalog Docker deployment bundle `pdc-<version>-images.tgz` and Remote Worker bundle `pdc-remote-<version>-compose.tgz`. \
  For example, for PDC 10.2.5, Data Catalog Docker deployment bundle is `pdc-10.2.5-images.tgz` and Remote Worker bundle is `pdc-remote-10.2.5-compose.tgz` . If you don't have, contact [Pentaho support](https://support.pentaho.com/).
* Ensure that `Kafka port 9094` is exposed in the `default-worker` instance when configuring the Remote Worker. This port enables secure communication between the Remote Worker and the Kafka service on the main PDC server.

**Procedure**

1. Load the latest Data Catalog Docker deployment bundle `pdc-<version>-images.tgz` into Docker.
2. Extract the Data Catalog Remote Worker bundle and navigate into the `pdc-deployment` directory:

   ```
   sudo tar -xvf pdc-remote-<version>-compose.tgz -C /opt/
   cd /opt/pentaho/pdc-docker-deployment/

   ```
3. Create the `conf` directory:

   ```
   sudo mkdir conf
   ```
4. Create a .env file, specify the necessary environment variables, and save the .env file:

   1. Copy the variables `PDC_WS_REMOTE_JOB_SERVER_ID` and `PDC_DATA_ENCRYPTION_KEY` along with their values from the base server installation.
   2. Add the `PDC_WS_REMOTE_OPS_URL` , `PDC_WS_REMOTE_GLOSSARY_BASE_URL`, and `PDC_MONGODB_OPS_DATABASE_URL` with the ops and mongodb details.

   ```
   GLOBAL_SERVER_HOST_NAME=<Base Server FQDN or IP Address>
   PDC_WS_REMOTE_JOB_SERVER_ID="eb710d72-9613-a978-42c5-a101343bf6ca"
   PDC_DATA_ENCRYPTION_KEY="2eindcVFPic6uA1o0wRWnXsBKNKiMMhbc2P9qTtvUTE="
   COMPOSE_PROFILES=ws-remote
   PDC_WS_REMOTE_OPS_URL="https://<Base Server FQDN or IP Address>/internal/ops/"
   PDC_WS_REMOTE_GLOSSARY_BASE_URL="https://<Base Server FQDN or IP Address>/glossary-service/api/v1/"
   PDC_MONGODB_OPS_DATABASE_URL="mongodb://root:broot@<Base Server FQDN or IP Address>:27017/ops?directConnection=true&authSource=admin&replicaSet=rs0"
   PDC_WS_REMOTE_DQ_CLIENT_ID=
   PDC_WS_REMOTE_DQ_API_URL=
   PDC_WS_REMOTE_DQ_CLIENT_SECRET=
   LOG_FLUENTBIT_ELASTICSEARCH_HOST=${GLOBAL_SERVER_HOST_NAME}
   ```
5. Copy the `extra-certs` directory and its contents, like certificates, into the Remote Worker machine `conf` directory:

   ```
   cp -r extra-certs/ conf/
   ```
6. Start the Remote Worker:

   ```
   sudo ./pdc.sh up
   ```
7. Verify the Remote Worker deployment in Data Catalog:
   1. Log in to Data Catalog and click **Management** in the left navigation menu.
   2. In the **Resources** card, click **Data Centers**.

      You can see the Remote Worker listed with **Affinity** as **Remote**.

      ![Remote Worker in Data Catalog](https://1897852526-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNjj4joO63OgOTabje2xP%2Fuploads%2FFzzfk9QXgEAydVwE7FHc%2FRemote%20Agent%20in%20PDC.png?alt=media\&token=d29ee30b-fc31-4a97-b19c-e4f9470ec921)

**Result**

You have successfully installed the Remote Worker and registered within Data Catalog.
