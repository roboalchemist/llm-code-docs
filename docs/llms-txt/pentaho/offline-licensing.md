# Source: https://docs.pentaho.com/pdc-admin/offline-licensing.md

# Offline licensing

Offline licensing in Pentaho Data Catalog enables you to activate and validate product licenses without requiring network connectivity to an external licensing server. This is ideal for secure or air-gapped environments. The license validation is performed locally using an offline license file provided by Pentaho support. Feature enforcement behavior remains consistent with online licensing. Switching between online and offline licensing affects only the license validation mechanism and does not modify existing metadata, assets, or configuration data within Data Catalog.

### Configure offline licensing in Data Catalog

Configuring offline licensing in Data Catalog determines how the application validates license entitlements. Data Catalog uses the `LICENSING_OFFLINE_INSTALL` environment variable to determine whether to validate licenses via an external licensing service or an offline license file stored locally.

This configuration applies at the application level and affects all license validation behavior.

Perform the following steps to configure Data Catalog to use offline licensing instead of online licensing.

**Before you begin**

* Ensure that you have administrator access to the PDC deployment environment.
* Verify that you have access to the PDC deployment configuration files.
* Obtain the offline license file from Pentaho support. The license file is uploaded in a later step.

**Procedure**

1. Log in to the server where Pentaho Data Catalog is installed.
2. Go to the Data Catalog Docker deployment configuration directory.

   ```
   cd /opt/pentaho/pdc-docker-deployment/conf
   ```
3. Open the .env (environment configuration) file.

   ```
   vi .env
   ```

   If the .env file does not exist, create it and save the file before proceeding.
4. Add or update the following environment variable to true to enable offline licensing.

   ```
   LICENSING_OFFLINE_INSTALL = true
   ```

   By default, this variable is set to false, which enables online licensing.
5. Save the configuration file and restart Data Catalog.

   ```
   ./pdc.sh up
   ```

**Result**

Data Catalog starts in offline licensing mode when `LICENSING_OFFLINE_INSTALL` is set to `true`. In this mode, Data Catalog does not attempt to connect to an external licensing server and waits for an offline license file to be uploaded.

Licensed features remain unavailable until a valid offline license file is uploaded.

**Next steps**

[Upload the offline license file](#upload-an-offline-license-file) to activate licensed features. See [#upload-an-offline-license-file](#upload-an-offline-license-file "mention") for the instructions.

### Upload an offline license file

Once you [configure offline licensing](#configure-offline-licensing-in-data-catalog) by setting LICENSING\_OFFLINE\_INSTALL=true in the deployment configuration and restarting PDC, you should upload an offline license file to Data Catalog using PDC APIs and activate licensed features.

Perform the following steps to upload the offline license file using PDC Licensing APIs:

**Before you begin**

* Ensure that you have administrator credentials to authenticate with the PDC Public APIs.
* Obtain the offline license file provided by Pentaho support.

**Procedure**

1. Access the PDC API Swagger UI for your environment.

   ```
   https://<your-domain>/api/public/swagger/
   ```

   This page lists all available PDC API endpoints grouped by domain.
2. Authenticate to obtain an access token. For more information, see the [Authentication](https://app.gitbook.com/s/nQdK93m35DUFgZ08FhMD/get-started-with-pdc-api-v1/authentication "mention") section in the [PDC API documentation](https://app.gitbook.com/s/nQdK93m35DUFgZ08FhMD/).\
   Use the same authentication method and credentials that you use to access the PDC user interface. The authentication process returns a bearer token that you must include in subsequent API requests.
3. Upload the offline license file using the licensing upload API.
   1. Use the following endpoint to upload the license file and associate it with a device identifier:\
      [Licensing #POST /api/public/v1/licensing/uploadLicense](https://app.gitbook.com/s/nQdK93m35DUFgZ08FhMD/pdc-api-ref-v1/licensing#post-api-public-v1-licensing-uploadlicense "mention")
   2. Include the required request parameters:
      * deviceId: A unique identifier for the deployment. This value can be any valid identifier.
      * fileData: The offline license file provided by Hitachi Vantara.\
        The following example shows a sample curl request:

        ```
        curl -X POST \
          'http://<pdc-host>:3002/api/public/v1/licensing/uploadLicense' \
          -H 'accept: application/json' \
          -H 'Authorization: Bearer <access-token>' \
          -H 'Content-Type: multipart/form-data' \
          -F 'deviceId=<device-id>' \
          -F 'fileData=@license.bin;type=application/octet-stream'
        ```
4. Submit the request.

**Result**

When the upload is successful, Data Catalog stores the offline license file in its internal database and processes the license entitlements. Licensed features become available immediately based on the permissions and limits defined in the license file.

If the upload fails, the response indicates the reason for the failure, such as an invalid license file or missing authentication.

**Next steps**

* Verify that the licensed features are available in the Data Catalog user interface.
* Securely store the offline license file in accordance with your organization’s security policies.
