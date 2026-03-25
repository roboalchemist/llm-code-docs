# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/spcs-commands/service-commands/events.md

# snow spcs service events

> **Note:**
>
> You can use Snowpark Container Services from Snowflake CLI only if you have the necessary permissions to use Snowpark Container Services.

Retrieve platform events for a service container.

## Syntax

```console
snow spcs service events
  <name>
  --container-name <container_name>
  --instance-id <instance_id>
  --since <since>
  --until <until>
  --first <first>
  --last <last>
  --all
  --connection <connection>
  --host <host>
  --port <port>
  --account <account>
  --user <user>
  --password <password>
  --authenticator <authenticator>
  --private-key-file <private_key_file>
  --token-file-path <token_file_path>
  --database <database>
  --schema <schema>
  --role <role>
  --warehouse <warehouse>
  --temporary-connection
  --mfa-passcode <mfa_passcode>
  --enable-diag
  --diag-log-path <diag_log_path>
  --diag-allowlist-path <diag_allowlist_path>
  --format <format>
  --verbose
  --debug
  --silent
```

## Arguments

`name`
:   Identifier of the service; for example: my_service.

## Options

`--container-name TEXT`
:   Name of the container.

`--instance-id TEXT`
:   ID of the service instance, starting with 0.

`--since TEXT`
:   Fetch events that occurred after this time, in Snowflake interval syntax.

`--until TEXT`
:   Fetch events that occurred before this time, in Snowflake interval syntax.

`--first INTEGER`
:   Fetch only the first N events. Cannot be used with –last.

`--last INTEGER`
:   Fetch only the last N events. Cannot be used with –first.

`--all`
:   Fetch all columns. Default: False.

`--connection, -c, --environment TEXT`
:   Name of the connection, as defined in your `config.toml` file. Default: `default`.

`--host TEXT`
:   Host address for the connection. Overrides the value specified for the connection.

`--port INTEGER`
:   Port for the connection. Overrides the value specified for the connection.

`--account, --accountname TEXT`
:   Name assigned to your Snowflake account. Overrides the value specified for the connection.

`--user, --username TEXT`
:   Username to connect to Snowflake. Overrides the value specified for the connection.

`--password TEXT`
:   Snowflake password. Overrides the value specified for the connection.

`--authenticator TEXT`
:   Snowflake authenticator. Overrides the value specified for the connection.

`--private-key-file, --private-key-path TEXT`
:   Snowflake private key file path. Overrides the value specified for the connection.

`--token-file-path TEXT`
:   Path to the file that contains the OAuth token to use when connecting to Snowflake.

`--database, --dbname TEXT`
:   Database to use. Overrides the value specified for the connection.

`--schema, --schemaname TEXT`
:   Database schema to use. Overrides the value specified for the connection.

`--role, --rolename TEXT`
:   Role to use. Overrides the value specified for the connection.

`--warehouse TEXT`
:   Warehouse to use. Overrides the value specified for the connection.

`--temporary-connection, -x`
:   Uses a connection defined with command-line parameters, instead of one defined in config. Default: False.

`--mfa-passcode TEXT`
:   Token to use for multi-factor authentication (MFA).

`--enable-diag`
:   Run Python connector diagnostic test. Default: False.

`--diag-log-path TEXT`
:   Diagnostic report path. Default: <temporary_directory>.

`--diag-allowlist-path TEXT`
:   Diagnostic report path to optional allowlist.

`--format [TABLE|JSON]`
:   Specifies the output format. Default: TABLE.

`--verbose, -v`
:   Displays log entries for log levels `info` and higher. Default: False.

`--debug`
:   Displays log entries for log levels `debug` and higher; debug logs contain additional information. Default: False.

`--silent`
:   Turns off intermediate output to console. Default: False.

`--help`
:   Displays the help text for this command.

## Usage notes

> **Note:**
>
> To use this command, you must enable the `enable_spcs_service_events` feature in your `config.toml` file, as shown:
>
> ```toml
> [cli.features]
> enable_spcs_service_events = true
> ```

* The following parameters are required:

  * `name`
  * `--container-name <name>`
  * `--instance-id <ID>`
* You can use the `--since` and `--until` time-based filters to return events for a specified period of time. You can specify the time as a relative time, such as `1h` (hour) or `2d` (days).
* You can use the `--first` and `--last` options to return only a specified number of events. Note that these options are mutually exclusive.

## Examples

* Retrieve all events for a specific service:

  ```snowcli
  snow spcs service events LOG_EVENT --container-name log-printer --instance-id 0
  ```

* Retrieve a subset of events for a specific service:

  ```snowcli
  snow spcs service events LOG_EVENT --container-name log-printer --instance-id 0 --first 5
  snow spcs service events LOG_EVENT --container-name log-printer --instance-id 0 --last 5
  ```

* Fetch events newer than the last five minutes:

  ```snowcli
  snow spcs service events LOG_EVENT --container-name log-printer --instance-id 0 --since '5 minutes'
  ```

* Fetch events older than one hour:

  ```snowcli
  snow spcs service events LOG_EVENT --container-name log-printer --instance-id 0 --until '1 hour'
  ```

* Retrieve all events with all columns displayed:

  ```snowcli
  snow spcs service events LOG_EVENT --container-name log-printer --instance-id 0 --all --last 1
  ```

  ```output
  TIMESTAMP | DATABASE NAME | SCHEMA NAME | SERVICE NAME | INSTANCE NAME | CONTAINER NAME | SEVERITY | EVENT NAME | EVENT VALUE
  -- | -- | -- | -- | -- | -- | -- | -- | --
  2024-12-13 10:01:52.808692 | TESTDB | PUBLIC | LOG_EVENT | 0 | log-printer | INFO | CONTAINER.STATUS_CHANGE | { "message": "Running", "status": "READY" }
  2024-12-14 22:27:25.420489 | TESTDB | PUBLIC | LOG_EVENT | 0 | log-printer | INFO | CONTAINER.STATUS_CHANGE | { "message": "Running", "status": "READY" }
  ```

* Retrieve events formatted for JSON output:

  ```snowcli
  snow spcs service events LOG_EVENT --container-name log-printer --instance-id 0 --last 1 --format json
  ```

  ```output
  [
       {
           "TIMESTAMP": "2024-12-14T22:27:25.420489",
           "DATABASE NAME": "TESTDB",
           "SCHEMA NAME": "PUBLIC",
           "SERVICE NAME": "LOG_EVENT",
           "INSTANCE NAME": "0",
           "CONTAINER NAME": "log-printer",
           "SEVERITY": "INFO",
           "EVENT NAME": "CONTAINER.STATUS_CHANGE",
           "EVENT VALUE": "{\n  \"message\": \"Running\",\n  \"status\": \"READY\"\n}"
       }
   ]
  ```
