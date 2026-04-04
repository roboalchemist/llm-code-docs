# Source: https://docs.api7.ai/apisix/reference/apisix-cli.md

# APISIX CLI

The APISIX CLI (Command Line Interface) is a tool that allows you to start, stop, and manage your APISIX instances.

```
apisix [action] <argument>
```

## Commands[â](#commands "Direct link to Commands")

### `apisix help`[â](#apisix-help "Direct link to apisix-help")

Print the APISIX CLI help menu.

### `apisix init`[â](#apisix-init "Direct link to apisix-init")

Initialize the `nginx.conf` configuration.

### `apisix init_etcd`[â](#apisix-init_etcd "Direct link to apisix-init_etcd")

Initialize data in etcd.

### `apisix start`[â](#apisix-start "Direct link to apisix-start")

Initialize and start the APISIX instance.

**Options:**

* `-h` or `--help`: print help menu.

* `-c` or `--config`: specify the path to the custom [configuration file](https://docs.api7.ai/apisix/reference/configuration-files.md) when starting APISIX. For example:

  ```
  apisix start -c /path/to/custom_config.yaml
  ```

  APISIX will fall back to the default configuration if `-c` is not set.

* `--verbose`: show `init_etcd` debug information.

### `apisix stop`[â](#apisix-stop "Direct link to apisix-stop")

Stop the running APISIX instance immediately. APISIX will stop all worker processes without waiting for them to finish serving any outstanding requests.

### `apisix quit`[â](#apisix-quit "Direct link to apisix-quit")

Quit the running APISIX instance gracefully. APISIX will wait for all worker processes to finish serving any outstanding requests before stopping.

### `apisix restart`[â](#apisix-restart "Direct link to apisix-restart")

Restart the APISIX instance. This command checks the generated `nginx.conf` configuration first before stopping and restarting APISIX.

### `apisix reload`[â](#apisix-reload "Direct link to apisix-reload")

Reload the APISIX instance. Reinitialize `nginx.conf` and apply configuration changes without interrupting existing connections.

### `apisix test`[â](#apisix-test "Direct link to apisix-test")

Test the generated `nginx.conf` to validate the configuration.

### `apisix version`[â](#apisix-version "Direct link to apisix-version")

Print APISIX version.
