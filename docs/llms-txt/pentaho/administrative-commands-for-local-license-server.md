# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/acquire-and-install-enterprise-licenses/install-and-manage-a-local-license-server/administrative-commands-for-local-license-server.md

# Administrative commands for local license server

You can use various CLI commands to perform basic license management operations.

## Logs

| File                 | Location                                   | Description                  |
| -------------------- | ------------------------------------------ | ---------------------------- |
| `access_request.log` | `/var/opt/flexnetls/<*identityName*>/logs` | Server endpoint request logs |
| `flexnetls.log`      | `/var/opt/flexnetls/<*identityName*>/logs` | Various server logs          |

## Installation setup commands

**Note:** If security is enabled, which it is by default, you must provide user credentials for each of these commands. For example:

```
-authorize admin <password>
```

* Default username: `admin`
* Default password: `Password\!01`

| File/command                                                                                                                                   | Location                                                         | Description                                                                               |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `./flexnetlsadmin.sh -authorize admin <*password*> -server <http://<*server\_ip\_address*>:7070/api/1.0/instances/~> -status`                  | `/home/<user>/revenera/flexnetls-x64_linux-2023.05.0/enterprise` | Checks the status of the Flex Net service.                                                |
| `./flexnetlsadmin -authorize admin <*password*> -server <http://<*server\_ip\_address*>:7070/api/1.0/instances/~> -config`                     | `/home/<user>/revenera/flexnetls-x64_linux-2023.05.0/enterprise` | Checks the configuration of the license server.                                           |
| `./flexnetlsadmin.sh -authorize admin <*password*> -server <http://<*server\_ip\_address*>:7070/api/1.0/instances/~> -licenses -verbose`       | `/home/<user>/revenera/flexnetls-x64_linux-2023.05.0/enterprise` | Checks which entitlements have been activated.                                            |
| `./flexnetlsadmin.sh -authorize admin <*password*> -server <*licenseServer\_baseURL*> -activate -id <*activation\_id*> -count <*no\_of\_lic*>` | `/home/<user>/revenera/flexnetls-x64_linux-2023.05.0/enterprise` | Activates or populates the pool of licenses on the server after entitlements are created. |

## Other files and commands

| File/command                       | Location                 | Description                                                                                                                                      |
| ---------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `local-configuration.yaml`         | `/opt/flexnetls/pentaho` | Local license server configuration.                                                                                                              |
| `producer-settings.xml`            | `/opt/flexnetls/pentaho` | Server configuration that has been set up by Hitachi Vantara.                                                                                    |
| `sudo systemctl daemon-reload`     | Not applicable           | The `systemctl` commands must be executed when updating the server configuration, such as when performing updates to `local-configuration.yaml`. |
| `sudo systemctl stop flexnetls`    | Not applicable           | System-wide commands.                                                                                                                            |
| `sudo systemctl enable flexnetls`  |                          |                                                                                                                                                  |
| `sudo systemctl disable flexnetls` |                          |                                                                                                                                                  |
| sudo systemctl status flexnetls    |                          |                                                                                                                                                  |
