# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/acquire-and-install-enterprise-licenses/install-and-manage-a-local-license-server/uninstall-a-local-license-server-windows.md

# Uninstall a local license server (Windows)

To uninstall the local license server from your Windows environment, complete the following steps:

1. Shut down the *flexnetls-pentaho* service using the following command:

   ```
   flexnetls.bat -stop
   ```
2. Uninstall the license server service using the following command:

   ```
   flexnetls.bat -uninstall
   ```
3. To properly clean up your environment, run the following command:

   ```
   sc delete FNLS-pentaho
   ```
4. Delete the files in the license server’s installation directory.
5. (Optional) If you are planning to do a clean re-install, remove the following files as well:

   | Files                 | Default file location                                                                        |
   | --------------------- | -------------------------------------------------------------------------------------------- |
   | Trusted storage files | `C:\Windows\ServiceProfiles\NetworkService\flexnetls\pentaho` (`.ks`, `.db`, and `.0` files) |
   | Log files             | `C:\Windows\ServiceProfiles\NetworkService\flexnetls\pentaho\logs`                           |

   **Note:**

   Trusted storage and log file locations are defined by the license server policies `server.trustedStorageDir` and `logging.directory`, respectively, the defaults for which are based on `${bases.dir}`. Depending on the values set for these policies on your server, your trusted storage and log files might be in different locations than those mentioned in this step.
