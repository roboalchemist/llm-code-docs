# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/connecting/configure-cli.md

# Configuring Snowflake CLI

Snowflake CLI uses a global configuration file called `config.toml` to configure connections and logs for Snowflake CLI.
If the file does not exist, running any `snow` command for the first time automatically creates an
empty `config.toml` file that you can then populate with the desired connections.
For more information about `toml` file formats, see [TOML (Tom’s Obvious Minimal Language)](https://toml.io/en/).
Snowflake Python libraries currently support TOML version 1.0.0.

The `config.toml` supports the following sections:

* `[connections]` for defining and managing connections
* `[logs]` for configuring which types of messages are saved to log files

A Snowflake CLI configuration file has the following structure:

```toml
default_connection_name = "myconnection"

[connections]
[connections.myconnection]
account = "myorganization-myaccount"
user = "jdoe"
...

[connections.testingconnection]
account = "myorganization-myaccount"
user = "jdoe"
...

[cli.logs]
save_logs = true
level = "info"
path = "/home/<username>/.snowflake/logs"
```

You can generate the basic settings for the TOML configuration file in Snowsight. For information, see
[Configuring a client, driver, library, or third-party application to connect to Snowflake](../../../user-guide/gen-conn-config.md).

> **Note:**
>
> If a `connections.toml` file exists, Snowflake CLI uses the connections defined in it instead of those defined in the `config.toml` file.

## Location of the `.toml` configuration file

By default Snowflake CLI looks for the `config.toml` file in the `~/.snowflake` directory or, in case this directory does not exist, in a system-specific location, as listed below.
You can also specify which configuration file should be used using `--config-file` flag or `SNOWFLAKE_HOME` environment variable.

* If you specify the `--config-file` option (such as, `snow --config-file ./my-config-file-path`), Snowflake CLI uses the specified configuration file.
* If the `SNOWFLAKE_HOME` environment variable is set, Snowflake CLI uses the location specified by this variable.
* If a `~/.snowflake` directory exists on your machine, Snowflake CLI uses the `~/.snowflake/config.toml` file.
* Otherwise, Snowflake CLI uses the `config.toml` file in the one of the following locations, based on your operating system:

  > * Linux: `~/.config/snowflake/config.toml`, but you can update it with XDG vars
  > * Windows: `%USERPROFILE%\AppData\Local\snowflake\config.toml`
  > * Mac: `~/Library/Application Support/snowflake/config.toml`

> **Note:**
>
> For MacOS and Linux systems, Snowflake CLI requires the `config.toml` file to limit its file permissions to read and write for the file owner only. To
> set the file required file permissions execute the following commands:
>
> ```bash
> chown $USER config.toml
> chmod 0600 config.toml
> ```

### Choose a different configuration file

In some situations, such as a continuous integration and continuous deployment (CI/CD) environments, you might prefer to create dedicated configuration files for testing and deployment pipelines instead of defining all of the possible configurations in a single Snowflake default configuration file.

To use a different configuration file that your default file, you can use the `--config-file` option for the `snow` command, as shown:

```snowcli
snow --config-file="my_config.toml" connection test
```

### Support for system environment variables

Snowflake CLI supports using system environment variables to override parameter values defined in your `config.toml` file, using the following format:

```bash
SNOWFLAKE_<config-section>_<variable>=<value>
```

where:

* `<config_section>` is the name of a section in the configuration file with periods (`.`) replaced with underscores (`_`), such as `CLI_LOGS`.
* variable is the name of a variable defined in that section, such as `path`.

Some examples include:

* Override the `path` parameter in the `[cli.logs]` section in the `config.toml` file:

  ```bash
  export SNOWFLAKE_CLI_LOGS_PATH="/Users/jondoe/snowcli_logs"
  ```

* Set the password for the `myconnection` connection:

  ```bash
  export SNOWFLAKE_CONNECTIONS_MYCONNECTION_PASSWORD="*******"
  ```

* Set the default connection name:

  ```bash
  export SNOWFLAKE_DEFAULT_CONNECTION_NAME="myconnection"
  ```

## Add an authentication policy that limits access to Snowflake CLI only

Users can create an [authentication policy](../../../user-guide/authentication-policies.md) that limits access permission to drivers, as well as Snowflake CLI.
If you want to allow access to Snowflake CLI only (and exclude the drivers), you can do the following:

* Create a new authentication policy that limits access strictly to Snowflake CLI.
* Enable the policy in the `config.toml` file.

### Create an authentication policy limited to Snowflake CLI

To create a new authentication policy for only Snowflake CLI, follow these steps:

1. Execute the [CREATE AUTHENTICATION POLICY](../../../sql-reference/sql/create-authentication-policy.md) SQL command, setting the CLIENT_TYPES parameter to include `'SNOWFLAKE_CLI'`.

   ```sqlexample
   CREATE AUTHENTICATION POLICY snowflake_cli_only
     CLIENT_TYPES = ('SNOWFLAKE_CLI');
   ```

2. Add the policy to the user, as shown:

   ```sqlexample
   ALTER USER user1
     SET AUTHENTICATION POLICY snowflake_cli_only;
   ```

### Enable the policy in the Snowflake CLI configuration

The `enable_separate_authentication_policy_id` configuration parameter lets you enable access to Snowflake CLI separately from the drivers.
When this access is enabled, specified users can access Snowflake CLI but not the other Snowflake drivers.

> **Warning:**
>
> If you already have an authentication policy that allows access only to drivers and don’t have one that allows access to Snowflake CLI only, enabling the `enable_separate_authentication_policy_id` parameter will cause the users to lose access to Snowflake CLI if you don’t create the new policy first. Make sure to add SNOWFLAKE_CLI to your authentication policy before enabling the configuration parameter.

To enable the SNOWFLAKE_CLI policy, add the `enable_separate_authentication_policy_id` parameter to the `[cli.features]` section in the `config.toml` file, as shown:

```toml
[cli.features]
enable_separate_authentication_policy_id = true
```

> **Note:**
>
> Enabling this parameter affects all connections made by Snowflake CLI.

## Use a proxy server

To use a proxy server, configure the following environment variables:

* HTTP_PROXY
* HTTPS_PROXY
* NO_PROXY

For example:

Linux or macOS:
:   ```bash
    export HTTP_PROXY='http://username:password@proxyserver.example.com:80'
    export HTTPS_PROXY='http://username:password@proxyserver.example.com:80'
    ```

Windows:
:   ```bash
    set HTTP_PROXY=http://username:password@proxyserver.example.com:80
    set HTTPS_PROXY=http://username:password@proxyserver.example.com:80
    ```

> **Tip:**
>
> Snowflake’s security model does not allow Secure Sockets Layer (SSL) proxies (using an HTTPS certificate). Your proxy server must use a publicly-available Certificate Authority (CA), reducing potential security risks such as a MITM (Man In The Middle) attack through a compromised proxy.
>
> If you must use your SSL proxy, we strongly recommend that you update the server policy to pass through the Snowflake certificate such that no certificate is altered in the middle of
> communications.
>
> Optionally `NO_PROXY` can be used to bypass the proxy for specific communications. For example, access to Amazon S3 can bypass the proxy server by specifying `NO_PROXY=".amazonaws.com"`.
>
> `NO_PROXY` does not support wildcards. Each value specified should be one of the following:
>
> * The end of a hostname (or a complete hostname), for example:
>
>   * .amazonaws.com
>   * myorganization-myaccount.snowflakecomputing.com
> * An IP address, for example:
>
>   * 192.196.1.15
>
> If more than one value is specified, values should be separated by commas, for example:
>
> > ```none
> > localhost,.example.com,.snowflakecomputing.com,192.168.1.15,192.168.1.16
> > ```

## Configure logging

By default, Snowflake CLI automatically saves `INFO`, `WARNING`, and `ERROR` level messages to log files. To disable or customize logging, create a `[cli.logs]` section in your `config.toml` file:

```toml
[cli.logs]
save_logs = true
level = "info"
path = "/home/<username>/.snowflake/logs"
```

where:

* `save_logs` indicates whether to save logs to files. Default: `true`.
* `level` specifies which levels of messages to save to log files. Choose from the following levels, which includes all levels below the selected one:

  * `debug`

    > **Warning:**
    >
    > Switching to the `debug` logging level can expose sensitive information, such as executed SQL queries. Use caution when enabling this level.
  * `info`
  * `warning`
  * `error`

  Default: `info`
* `path` specifies the absolute path to save the log files. The format of the path varies based on your operating system, as shown:

  * Linux: `path = "/home/<your_username>/.config/snowflake/logs"`
  * MacOS: `path = "/Users/<your_username>/Library/Application Support/snowflake/logs"`
  * Windows: `path = "C:\\Users\\<your_username>\\AppData\\Local\\snowflake\\logs"`

  If not specified, the command creates a `logs` directory in the default `config.toml` file location.

If your `config.toml` was created automatically, the `config.toml` file contains the `|cli.logs|` section filled with default values.

Logs from a single day are appended to file `snowflake-cli.log`, which is later renamed to `snowflake-cli.log.YYYY-MM-DD`, as shown.

```bash
ls logs/
```

```output
snowflake-cli.log            snowflake-cli.log.2024-10-22
```

For troubleshooting purposes, you’ll typically also need to configure logging for the Snowflake Connector for Python by adding a `[log]` section to the `config.toml` file, as shown in the following example:

```toml
[log]
save_logs = true
path = "/home/<username>/.snowflake/logs"
level = "DEBUG"
```

For more information about logging for the Snowflake Connector for Python, see [Logging configuration file](../../python-connector/python-connector-example.md) in the Snowflake Connector for Python documentation.

## Suppress version update notifications

By default, Snowflake CLI checks for newer versions and displays a notification message when a newer version is available. You can suppress these notifications using either a configuration file setting or an environment variable, as follows:

* Add the `ignore_new_version_warning` setting to the `config.toml` file:

  ```toml
  [cli]
  ignore_new_version_warning = true
  ```

* Set the `SNOWFLAKE_CLI_IGNORE_NEW_VERSION_WARNING` environment variable:

  ```bash
  export SNOWFLAKE_CLI_IGNORE_NEW_VERSION_WARNING=true
  ```
