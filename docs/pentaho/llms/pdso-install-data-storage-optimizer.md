# Source: https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-data-storage-optimizer.md

# Install Data Optimizer

You can install Data Optimizer into an existing Data Catalog deployment.

## Installing Data Optimizer offline

You must have `root` privileges or have the necessary permissions to run Docker as part of the installation process.

Perform the following steps to install Data Optimizer into Data Catalog:

1. Open a terminal window on your dedicated Data Catalog deployment server.
2. Save the Data Optimizer release package in the Data Catalog server.
3. Open a terminal window on your dedicated Data Catalog deployment server and extract the files from the release package to the `/opt` directory using the following command:

   `tar -xvf [*name of release package*].tar.gz -C /opt`
4. Load the required installation images that are packaged in the vendor directory into Docker using the following command:

   ```
   cd /opt/pentaho/pdc-docker-deployment
   ./pdc.sh load-images
   ```
5. Upon first time installation or if the following message appears:

   ```

   GLOBAL_SERVER_HOST_NAME env is not set, please select an environment variable value from the list or type your own:
   1.	*IP address*
   2.	*Hostname*
   3.	*Hostname.localhost.localdomain*
   4.	Other 
   #?    1
   ```

   Then set the **GLOBAL\_SERVER\_HOST\_NAME** variable to the *Hostname* or *IP address* of the server that Data Catalog is being deployed on. Set the variable by selecting the number for the option that you want to use and then press Enter.

   In the example above, the user selected `1`. The script then sets the **GLOBAL\_SERVER\_HOST\_NAME** variable, in this case, to the *IP address* in the `conf/.env` file.
6. Start all the Dockers using the following command:

   `sh pdc.sh up`

   The installation script uses the packaged Docker images for the Data Optimizer release to create and run Docker containers on your dedicated server.

The installation finishes when each Docker container has been successfully started.

Access Data Catalog through your browser (the Chrome browser is recommended) using the hostname name or IP address and then access Data Optimizer using the hostname or IP address, as follows:

`[*hostname*` or `*IP address*]/pdso`

Confirm that the application is successfully installed and running.

**Note:** For new installations, you are redirected to the PDC login page.

To facilitate initial validation especially in sandbox and demo environments, a set of users are created by default. These users are assigned specific roles. For more information, see [Manage users and permissions](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/ldc-manage-users-and-permissions-cp-ag "mention") in the [Administer Pentaho Data Catalog](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/ "mention") document.

<table><thead><tr><th width="185">Role</th><th>Actions</th></tr></thead><tbody><tr><td>Admin</td><td>A user who is able to configure the product</td></tr><tr><td>Data User</td><td>A user who is interested in leveraging Data Catalog to find data for use for a business operation</td></tr><tr><td>Data Steward</td><td>A user who will update and process data in Data Catalog for use for a business operation, including migrating data for Pentaho Data Optimizer</td></tr><tr><td>Business User</td><td>A user who needs to view business-specific glossaries and dictionaries</td></tr><tr><td>Business Steward</td><td>A user who will maintain business-specific glossaries and dictionaries</td></tr><tr><td>Data Developer</td><td>A user who will create and update business rules in Data Catalog or metadata rules in Data Optimizer</td></tr></tbody></table>

Refer to the installation package for credential details for the default users. This information is found in an encrypted file.

For Development and Production environments, it is a best practice to create users upon installation and deprecate these default users.
