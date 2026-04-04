# Source: https://docs.infrahub.app/sync/guides/run.md

# Running sync tasks

Learn how to use Infrahub Sync's commands to generate sync adapters, calculate differences, and synchronize data between your source and destination systems.

![Infrahub-Sync process](/assets/images/infrahub_sync_process.excalidraw-77809c6d9cf8697772543001bc5ad1a8.svg)

::: info

Before generating the necessary Python code for your sync adapters and models and synchronizing, you need to created a configuration. To create a new configuration, please refer to the guide [Creating a new Sync Instance](/sync/guides/creation.md)

:::

## Generating sync adapters and models[​](#generating-sync-adapters-and-models "Direct link to Generating sync adapters and models")

### Command[​](#command "Direct link to Command")

```
infrahub-sync generate --name <sync_project_name> --directory <your_configuration_directory>
```

### Parameters[​](#parameters "Direct link to Parameters")

* `--name`: The name of the sync project you want to generate code for.
* `--directory`: The directory where your sync configuration files are located.

This command reads your configuration file and generates Python code for the sync adapters and models required for the synchronization task.

## Calculating differences[​](#calculating-differences "Direct link to Calculating differences")

The `diff` command lets you see the differences between your source and destination before actually performing the synchronization. This is useful for verifying what will be synchronized.

### Command[​](#command-1 "Direct link to Command")

```
infrahub-sync diff --name <sync_project_name> --directory <your_configuration_directory>
```

### Parameters[​](#parameters-1 "Direct link to Parameters")

* `--name`: Specifies the sync project for which you want to calculate differences.
* `--directory`: The directory where your sync configuration files are located.

Running this command will output the differences detected based on the current state of your source and destination systems.

## Synchronizing data[​](#synchronizing-data "Direct link to Synchronizing data")

Once you're ready to synchronize the data between your source and destination, you can use the `sync` command.

### Command[​](#command-2 "Direct link to Command")

```
infrahub-sync sync --name <sync_project_name> --directory <your_configuration_directory>
```

### Parameters[​](#parameters-2 "Direct link to Parameters")

* `--name`: The name of the sync project you wish to run.
* `--directory`: The directory where your sync configuration files are located.

This command performs the synchronization, applying the changes from the source to the destination based on the differences calculated by the `diff` command.

### Progress and logging[​](#progress-and-logging "Direct link to Progress and logging")

The `sync` command also supports additional flags for displaying progress and managing logging:

* `--show-progress`: Displays a progress bar during synchronization.
* `--diff`: Print the differences between the source and the destination before syncing.

For example:

```
infrahub-sync sync --name my_project --directory configs --diff --show-progress
```
