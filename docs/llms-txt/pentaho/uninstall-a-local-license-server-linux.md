# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/acquire-and-install-enterprise-licenses/install-and-manage-a-local-license-server/uninstall-a-local-license-server-linux.md

# Uninstall a local license server (Linux)

To uninstall the local license server from your Linux environment, complete the following steps:

**Note:**

If a device is associated with your Linux machine from FlexNet Operations before you uninstall and there are activated entitlements, change the state of that device to `obsolete` before re-installing the local license server. Otherwise, you might encounter an activation ID mismatch.

1. Shut down the *flexnetls-pentaho* service using the following command:

   ```
   sudo systemctl stop flexnetls-pentaho
   ```
2. Prevent the service from starting automatically when rebooting the system using the following command:

   ```
   sudo systemctl disable flexnetls-pentaho
   ```
3. Remove the following files that are associated with the service:

   ```
   sudo rm /etc/systemd/system/flexnetls-pentaho.service
   sudo rm -r /etc/systemd/system/flexnetls-pentaho.service.d

   ```
4. (Optional) If you are planning to do a clean re-install, remove the following files as well:

| File location                                                                              | Command                              |
| ------------------------------------------------------------------------------------------ | ------------------------------------ |
| Trusted storage files in`/var/opts/flexnetls/producer_name` (`.ks`, `.db`, and `.0` files) | `rm -rf /var/opts/flexnetls/pentaho` |
| Log files in`/var/opts/flexnetls/producer_nama/logs`                                       | `rm -rf /opt/flexnetls/pentaho`      |
