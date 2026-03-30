# Source: https://docs.pentaho.com/pdc-10.2-install/install-pentaho-data-catalog/install-data-catalog.md

# Install Data Catalog

This procedure describes how to install Pentaho Data Catalog using the online release package. Use the Data Catalog and Pentaho Data Optimizer installation bundle provided through the Support Portal.

Perform the following steps to install Data Catalog:

**Prerequisites**

Before you begin, ensure that:

* You have the license code identifier provided by your Pentaho representative.
* The server has outbound internet connectivity to complete license activation.
* Docker and Docker Compose are installed and configured.
* System requirements are met.

{% hint style="info" %}

## **Important**

Before starting the installation, back up the existing `conf/.env` file if you are upgrading or reinstalling to retain any environment customizations you have made in case the file is overwritten during the installation process. During installation, Data Catalog checks for the `PDC_DATA_ENCRYPTION_KEY` variable in the `conf/.env` file.

* If the variable exists, the current `conf/.env` file is retained.
* If the variable does not exist, a new `.env` file is generated that includes a new `PDC_DATA_ENCRYPTION_KEY`. If needed, you can add any custom environment variable settings back into the new `.env` file from your saved file.
  {% endhint %}

**Procedure**

1. Verify that you have `root` privileges or have the necessary permissions to run Docker.
2. Open a terminal window on your dedicated Data Catalog deployment server.
3. Save the Data Catalog release package in the Data Catalog server.

   Now you will have two files:

   * The Docker image: `pdc-<version>-images.tgz` (example: `pdc-10.2.5-images.tgz`)
   * The PDC deployment bundle: `pdc-<DEPLOYMENT_PACKAGE_TYPE> -<version>-compose.tgz` The `<DEPLOYMENT_PACKAGE_TYPE>` placeholder corresponds to the type of PDC service and `<version>` is the PDC version you want to deploy. For example:
   * For PDC full services, use: `pdc-full-10.2.5-compose.tgz`
   * For PDC with Pentaho Data Optimizer services, use: `pdc-pdo-10.2.5-compose.tgz`
   * For PDC with Pentaho Data Mastering services, use: `pdc-pdm-10.2.5-compose.tgz` \
     **Note:** If you are unsure which deployment package to use, contact [Pentaho Support](https://support.pentaho.com/) for guidance.
4. Extract the files from the PDC deployment bundle to the `/opt` directory using the following command:

   ```
   tar -xvf [*name of release package*].tgz -C /opt
   ```

   Example: `tar -xvf pdc-full-10.2.5-compose.tgz -C /opt`

   The command creates a `pentaho` directory and extracts the contents of the deployment into a `pdc-docker-deployment` subdirectory.
5. Load the required installation images (that are saved in the Data Catalog server) into Docker:

   ```
   docker load –i pdc-<version>-images.tgz
   cd /opt/pentaho/pdc-docker-deployment
   sudo ./pdc.sh
   ```

   Example: `pdc-10.2.5-images.tgz`
6. (Optional) If you get this message: `GLOBAL_SERVER_HOST_NAME env is not set`, select the number for the environment variable value that you want to set from the listing or enter the number using the keyboard and then press Enter:

   ```
   1.	IP address
   2.	Hostname
   3.	Hostname.localhost.localdomain
   4.	Hostname.localhost.localdomain
   5.	Other 
   #?
   ```

   If you select `1`, the script sets the **`GLOBAL_SERVER_HOST_NAME`** variable to the *IP address* in the `conf/.env` file.

   **Note:** If you select `5`, then enter the valid IP address or the fully qualified domain name.
7. Edit the `conf/.env` file to apply the license for your product, add email domains, and perform Keycloak SMTP configuration:

   **Note:** This SMTP configuration sets up forgot password functionality only. To set up Data Catalog to email users when they are tagged in a comment, data pipes template, or other notification, see [Set up email server to send Data Catalog notifications](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/ldc-advanced-configuration-ut_cp#set-up-an-email-server-to-send-data-catalog-notifications) in the [Administer Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/cUaDtyTop3vo8cjqgjGk/) guide.

   `sudo vi conf/.env`

   1. Add the provided license code identifier to the *License Server ID* variable in the **Licensing Server URL**, as follows:`LICENSING_SERVER_URL=https://pentaho.compliance.flexnetoperations.com/instances/*&lt;License Server ID&gt;*/request`
   2. Add new email allowed domains. By default, Data Catalog includes users that use `hv.com` and `hitachivantara.com` emails. You can add your own domain to this list:

      `EMAIL_DOMAINS='["hv.com", "hitachivantara.com", "abc.com"]'`

      **Note:** Do not overwrite or delete `hv.com` or `hitachivantara.com` as these email domains are used to create the default users in the deployment.
   3. Add configuration for Keycloak SMTP. In the example value below, SMTP configuration is set to use `hitachivantara.com` emails, but you can change these to point to your company’s SMTP server configuration:

      ```
      KEYCLOAK_SMTP='{"replyToDisplayName" : "pdccatalog@hitachivantara.com","starttls" : "true","auth" : "true","envelopeFrom" : "pdccatalog@hitachivantara.com", "ssl" : "true","password" : "fwjx mpvb hcdb yofp","port" : "465","host" : "smtp.hitachivantara.com","replyTo" : "pdccatalog@hitachivantara.com","from" : "pdccatalog@hitachivantara.com","fromDisplayName" : "pdccatalog@hitachivantara.com","user" : "pdccatalog@hitachivantara.com"}'
      ```
   4. Save the file.

   The licensing, email, and SMTP settings are complete.

   **Note:** \
   \- If you want to update email or SMTP settings after installation, this needs to be done using IAM APIs. \
   \- During installation, you can also modify the `COMPOSE_PROFILES` or other variables in the `.env` file to enable or disable specific services (for example, Physical Assets). For details, see [Disable the Physical Assets feature from Data Catalog deployment](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/ldc-advanced-configuration-ut_cp#heading-title-text) in the [Administer Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/cUaDtyTop3vo8cjqgjGk/) guide.
8. Start all the Docker containers using the following command:

   ```
   sh pdc.sh up
   ```

**Result**

The installation is ready for use after all the Docker containers have successfully started.

**Next steps**

Access Data Catalog through your browser (the Chrome browser is recommended) using the value provided in the `GLOBAL_SERVER_HOST_NAME` (in step 7) and confirm that the application is successfully installed and running.

{% hint style="info" %}
For new installations, you are redirected to the PDC login page.
{% endhint %}

Data Catalog provides a set of default users for demonstration and testing purposes. These default users have the following specific roles assigned:

| Role                       | Actions                                                                                                                                                                 |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Business User              | A user who needs to view business-specific glossaries and dictionaries                                                                                                  |
| Data User                  | A user who needs to use Data Catalog to find data for a business operation                                                                                              |
| Business Steward           | A user who needs to maintain business-specific glossaries and dictionaries                                                                                              |
| Data Steward               | A user who needs to update and process data in Data Catalog for use for a business operation, including migrating data if you have a license for Pentaho Data Optimizer |
| Admin                      | A user who needs to configure the product                                                                                                                               |
| Data Developer             | A user who needs to create and update business or metadata rules                                                                                                        |
| Data Storage Administrator | A user who monitors and manages storage utilization across data sources, folders, and schemas.                                                                          |

For more information, see [User roles and permissions in Data Catalog](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/pdc-user-roles-and-permissions "mention") in the [Use Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/RAKLVv06oBKpy9VLbw7P/) guide.

Refer to the installation package for credential details for the default users. This information is found in an encrypted file.

{% hint style="info" %}
**Important:** In Development and Production environments, it is a best practice to create users during installation and deprecate the default users.
{% endhint %}

After installing Data Catalog, you may need to set up additional components, depending on your environment. For more information, see [Advanced configuration](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/ldc-advanced-configuration-ut_cp "mention") in the [Administer Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/cUaDtyTop3vo8cjqgjGk/) guide.
