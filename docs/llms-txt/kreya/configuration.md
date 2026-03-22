# Source: https://kreya.app/docs/configuration.md

# Configuration

This guide explains how to configure the Kreya application using various methods. Kreya resolves configuration settings from multiple sources in order of priority. Settings specified in higher-priority sources will overwrite those in lower-priority sources. To configure the proxy settings, check out the [proxy documentation](/docs/proxy.md).

info

After adjusting the configuration, you must restart the Kreya application for the changes to take effect.

## Configuration Sources[​](#configuration-sources "Direct link to Configuration Sources")

Kreya reads configuration settings from the following sources, in order of priority:

1. **Command Line Arguments**<br /><!-- -->Settings provided as command-line arguments take the highest priority.

2. **Environment Variables**<br /><!-- -->Environment variables prefixed with `KREYA_` are used to configure Kreya. Environment variables used for configuration are case-insensitive.

3. **JSON Configuration Files**<br /><!-- -->Kreya supports JSON configuration files, which are loaded from platform-specific locations:

   * **Windows**:

     <!-- -->

     * `%APPDATA%\Kreya\kreya.config.json`
     * `<working directory>\kreya.config.json`

   * **Linux**:

     <!-- -->

     * `$XDG_CONFIG_HOME/Kreya/kreya.config.json`
     * `~/Kreya/kreya.config.json`
     * `<working directory>/kreya.config.json`

   * **macOS**:

     <!-- -->

     * `~/Library/Application Support/Kreya/kreya.config.json`
     * `<working directory>/kreya.config.json`

## Available Configuration Options[​](#available-configuration-options "Direct link to Available Configuration Options")

The following options can be configured using JSON files or environment variables:

| JSON Key                        | Environment Variable                  | Description                                                                                                                                                                                                                                            |
| ------------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `DisableAutoUpdates`            | `KREYA_DisableAutoUpdates`            | Disables automatic updates.                                                                                                                                                                                                                            |
| `Logging.LogLevel.Default`      | `KREYA_Logging_LogLevel_Default`      | Configures the default log level.<br />Available levels are `None`, `Critical`, `Error`, `Warning`, `Information` and `Debug`.                                                                                                                         |
| `Logging.LogLevel.{Category}`   | `KREYA_Logging_LogLevel_{Category}`   | Configures the log level of a logging category.<br />Available categories are `KREYA` and `SYSTEM`.                                                                                                                                                    |
| `RestMaxResponseSize`           | `KREYA_RestMaxResponseSize`           | Sets the maximum response size for REST APIs.                                                                                                                                                                                                          |
| `ScriptingTimeout`              | `KREYA_ScriptingTimeout`              | Configures the timeout for scripts.                                                                                                                                                                                                                    |
| `DisableTelemetry`              | `KREYA_DisableTelemetry`              | Disables [telemetry](/docs/telemetry.md) data collection.                                                                                                                                                                                              |
| `MaxHistoryEntries`             | `KREYA_MaxHistoryEntries`             | Configures the maximum number of history entries.                                                                                                                                                                                                      |
| `MaxHistoryEntriesPerProject`   | `KREYA_MaxHistoryEntriesPerProject`   | Configures the maximum number of history entries per project.                                                                                                                                                                                          |
| `MaxHistoryEntriesPerOperation` | `KREYA_MaxHistoryEntriesPerOperation` | Configures the maximum number of history entries per operation.                                                                                                                                                                                        |
| `ProductKey`                    | `KREYA_ProductKey`                    | Sets the product key for a Kreya Enterprise Offline license. This takes precedence over `ProductKeyPath`.                                                                                                                                              |
| `ProductKeyPath`                | `KREYA_ProductKeyPath`                | Configures the path to a file which contains a Kreya Enterprise Offline product key. Defaults to - `%APPDATA%\Kreya\key.txt` on Windows<br />- `~/Library/Application Support/Kreya/key.txt` on macOS<br />- `$XDG_CONFIG_HOME/Kreya/key.txt` on Linux |

## Example JSON Configuration File[​](#example-json-configuration-file "Direct link to Example JSON Configuration File")

Below is an example of a JSON configuration file:

```
{
  "RestMaxResponseSize": 1048576,
  "ScriptingTimeout": 30000,
  "Logging": {
    "LogLevel": {
      "Default": "Warning",
      "Kreya": "Information"
    }
  }
}
```
