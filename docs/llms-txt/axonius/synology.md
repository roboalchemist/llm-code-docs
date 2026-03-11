# Source: https://docs.axonius.com/docs/synology.md

# Synology

Synology is a network-attached storage provider that offers data management and backup solutions.

### Asset Types Fetched

* Devices, Users

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* User Name/Password

### APIs

Axonius uses the Synology File Station Official API.

### Permissions

To retrieve device-level and file system data from Synology NAS using the File Station API, the API account must have sufficient privileges to:

* Access the File Station application (`session=FileStation`)

* View shared folders and files, including their metadata (e.g., path, size, owner, time stamps)

* Read system volume information, including free space, file ownership, and POSIX/ACL permissions

* List and inspect virtual folders and CIFS/NFS mount points (if using `SYNO.FileStation.VirtualFolder`)

#### Supported From Version

Supported from Axonius version 6.1.68

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Synology server.
2. **User Name** and **Password**  - The credentials for a user account that has the Required Permissions to fetch assets.

![Synology.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Synology.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).