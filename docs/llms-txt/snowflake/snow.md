# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/snow.md

# snow

Snowflake CLI tool for developers.

## Syntax

```console
snow [<resource-commands>]
  --version
  --info
  --config-file <configuration_file>
  --install-completion
  --show-completion
  --help
```

## Arguments

`[resource-commands]`
:   Optional commands for managing Snowflake CLI resources.

## Options

`--version`
:   Shows the version of the Snowflake CLI.

`--info`
:   Shows information about the Snowflake CLI.

`--config-file configuration_file`
:   Specifies Snowflake CLI configuration file that should be used.

`--install-completion`
:   Install completion for the current shell.

`--show-completion`
:   Show completion for the current shell, to copy it or customize the installation.

`--help`
:   Displays the help text for this command.

## Usage notes

The **snow** command supports the following commands to manage Snowflake resources:

* [snow app commands](native-apps-commands/overview.md)
* [snow connection commands](connection-commands/overview.md)
* [snow git commands](git-commands/overview.md)
* [snow helpers commands](helpers-commands/overview.md)
* [snow notebook commands](notebook-commands/overview.md)
* [snow object commands](object-commands/overview.md)
* [snow snowpark commands](snowpark-commands/overview.md)
* [snow spcs service commands](spcs-commands/service-commands/overview.md)
* [snow sql commands](sql-commands/overview.md)
* [snow stage commands](stage-commands/overview.md)
* [snow streamlit commands](streamlit-commands/overview.md)

## Examples

* To display the Snowflake CLI version, run the following command:

  ```snowcli
  snow --version
  ```

  ```output
  Snowflake CLI version: 3.0.0
  ```

* To display information about Snowflake CLI, run the following command:

  ```snowcli
  snow --info
  ```

  ```output
  [
    {
        "key": "version",
        "value": "3.2.0"
    },
    {
        "key": "default_config_file_path",
        "value": "<user-home>/.snowflake/config.toml"
    },
    {
        "key": "python_version",
        "value": "3.11.6 (v3.11.6:8b6ee5ba3b, Oct  2 2023, 11:18:21) [Clang 13.0.0 (clang-1300.0.29.30)]"
    },
    {
        "key": "system_info",
        "value": "macOS-14.4.1-x86_64-i386-64bit"
    },
    {
        "key": "feature_flags",
        "value": {}
    },
    {
        "key": "SNOWFLAKE_HOME",
        "value": null
    }
  ]
  ```

* To display command-line help for the `snow` command, run the following command:

  ```bash
  snow --help
  ```

  ```output
  Usage: snow [OPTIONS] COMMAND [ARGS]...

  Snowflake CLI tool for developers.

  ╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
  │ --version                           Shows version of the Snowflake CLI                                                                   │
  │ --info                              Shows information about the Snowflake CLI                                                            │
  │ --config-file                 FILE  Specifies Snowflake CLI configuration file that should be used [default: None]                       │
  │ --install-completion                Install completion for the current shell.                                                            │
  │ --show-completion                   Show completion for the current shell, to copy it or customize the installation.                     │
  │ --help                -h            Show this message and exit.                                                                          │
  ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
  ╭─ Commands ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
  │ app          Manages a Snowflake Native App                                                                                              │
  │ connection   Manages connections to Snowflake.                                                                                           │
  │ cortex       Provides access to Snowflake Cortex.                                                                                        │
  │ git          Manages git repositories in Snowflake.                                                                                      │
  │ notebook     Manages notebooks in Snowflake.                                                                                             │
  │ object       Manages Snowflake objects like warehouses and stages                                                                        │
  │ snowpark     Manages procedures and functions.                                                                                           │
  │ spcs         Manages Snowpark Container Services compute pools, services, image registries, and image repositories.                      │
  │ sql          Executes Snowflake query.                                                                                                   │
  │ stage        Manages stages.                                                                                                             │
  │ streamlit    Manages a Streamlit app in Snowflake.                                                                                       │
  ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
  ```

* To display command-line help resource commands, run a command similar to the following that displays help for the `snow spcs` commands:

  ```snowcli
  snow spcs --help
  ```

  ```output
  Usage: snow spcs [OPTIONS] COMMAND [ARGS]...

  Manages Snowpark Container Services compute pools, services, image registries, and image repositories.

  ╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
  │ --help  -h        Show this message and exit.                                                                        │
  ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
  ╭─ Commands ───────────────────────────────────────────────────────────────────────────────────────────────────────────╮
  │ compute-pool       Manages compute pools.                                                                            │
  │ image-registry     Manages image registries.                                                                         │
  │ image-repository   Manages image repositories.                                                                       │
  │ service            Manages services.                                                                                 │
  ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
  ```
