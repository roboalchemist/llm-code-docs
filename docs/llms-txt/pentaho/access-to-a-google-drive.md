# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/vfs-browser-connecting-to-virtual-file-systems/before-you-begin-vfs-browser/access-to-a-google-drive.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/vfs-browser-connecting-to-virtual-file-systems/access-to-a-google-drive.md

# Access to a Google Drive

Perform the following setup steps to initially access your Google Drive.

1. Follow the "Step 1" procedure in the article ["Build your first Drive app (Java)"](https://developers.google.com/drive/api/v3/quickstart/java) in the [Google Drive APIs documentation](https://developers.google.com/drive/).

   This procedure turns on the Google Drive API and creates a `credentials.json` file.
2. Rename the `credentials.json` file to `client_secret.json`. Copy and paste the renamed file into the `data-integration/plugins/pentaho-googledrive-vfs/credentials` directory.
3. Restart PDI.

   The **Google Drive** option does not appear when creating a VFS connection until you copy and paste the `client_secret.json` file into the `credentials` directory and restart PDI.
4. Log in to your Google account.
5. Enter you Google account credentials and log in. The Google Drive permission window displays.
6. Click **Allow** to access your Google Drive Resources.

After this initialization, Pentaho stores a security token called **StoredCredential** in the `data-integration/plugins/pentaho-googledrive-vfs/credentials` directory. With this token, you can access your Google Drive resources whenever you log in to your Google account. If this security token is deleted, you are prompted to log in to your Google account after restarting PDI. If you change your Google account permissions, you must delete the token and repeat the previous steps to generate a new token.

**Note:** If you want to access your Google Drive via a transformation running directly on your Pentaho Server, copy then paste the **StoredCredential** and the `client_secret.json` files into the `pentaho-server/pentaho-solutions/system/kettle/plugins/pentaho-googledrive-vfs/credentials` directory on your Pentaho Server.
