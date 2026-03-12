# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/vfs-browser-connecting-to-virtual-file-systems/before-you-begin-vfs-browser/set-up-hcp-credentials.md

# Set up HCP credentials

To use the VFS browser with your HCP files, you must set up your HCP credentials. Before setting up your credentials, verify you already established access to the HCP platform by performed the tasks specified in [Access to HCP](https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/before-you-begin-vfs-connections/access-to-hcp-rest).

Perform the following steps to set up your HCP credentials.

1. Depending on the operating system, create the following subdirectory in the user’s home directory:
   * Linux: `~/.hcp/`
   * Windows: `C:\Users\*username*\.hcp\`
2. Create a file named `credentials` and save it to the `\.hcp` directory.
3. Open the `credentials` file then add the parameters and values shown in the following code:

   ```
   [default]
   hcp_username=[username]
   hcp_password=[password]
   accept_self_signed_certificates=false

   ```

   Insert the HCP namespace username and password, and change **accept\_self\_signed\_certificates** to `true` if you want to enable a security bypass.

   **Note:** You can also use obfuscated or encrypted usernames and passwords.
4. Save and close the file.
5. For the Pentaho Server setup, stop and start the server.

   For information about stopping and starting the server, see the **Install Pentaho Data Integration and Analytics** document.

This completes the setup for VFS browser access to HCP.
