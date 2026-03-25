# Source: https://docs.vale.sh/topics/cli.md

# CLI

Learn about the Vale command-line interface.

The Vale CLI is a powerful tool for linting your content in a variety of formats. To get started, try running with no arguments:

![Vale's help text](https://content.gitbook.com/content/EMH7s0sC5N9L8xSMXGwW/blobs/JU6lZokySTeBWnu1fWp0/help2.png)

## [Environment variables](#environment-variables)

The following list of environment variables are supported by the `vale` command-line interface:

| Variable           | Description                                                         |
| ------------------ | ------------------------------------------------------------------- |
| `VALE_CONFIG_PATH` | Override the default search process by specifying a .vale.ini file. |
| `VALE_STYLES_PATH` | Specify the location of the default StylesPath.                     |

You can inspect the current environment variables by running:

```
vale ls-vars
```

The exact steps for setting environment variables depend on your operating system, but here are some useful links for [Windows](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/setx) and [macOS](https://support.apple.com/guide/terminal/use-environment-variables-apd382cc5fa-4f58-4449-b20a-41c53c006f8f/mac).

## [CLI options](#cli-options)

| Name              | Description                                                                                                                                                                    |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `sync`            | <p>Download and install packages. See <a href="../keys/packages">Packages</a> for more information.<br><code>\<br>$ vale sync\<br></code></p>                                  |
| `ls-config`       | <p>Print the current configuration options as JSON.<br><code>\<br>$ vale ls-config\<br></code></p>                                                                             |
| `ls-metrics`      | <p>Print the computed metrics for the given file. See <a href="../checks/metric">metric</a> for more information.<br><code>\<br>$ vale ls-metrics path/to/file\<br></code></p> |
| `ls-dirs`         | <p>Print the location of default configuration directories.<br><code>\<br>$ vale ls-dirs\<br></code></p>                                                                       |
| `ls-vars`         | <p>Print the supported environment variables.<br><code>\<br>$ vale ls-vars\<br></code></p>                                                                                     |
| `--config`        | <p>Override the default configuration search process.<br><code>\<br>$ vale --config='path/to/.vale.ini' README.md\<br></code></p>                                              |
| `--ext`           | <p>Assign a file extension to stdin.<br>\`\`\`<br>$ echo "<em>This</em> is Markdown"</p>                                                                                       |
| `--filter`        | <p>An expression to filter rules by. See <a href="filters">Filters</a> for more information.<br><code>\<br>$ vale --filter='"heading" in .Scope' test.md\<br></code></p>       |
| `--glob`          | <p>A glob pattern to match files against. See <a href="../guides/globbing">Globbing</a> for more information.<br><code>\<br>$ vale --glob='\*.md' some-dir\<br></code></p>     |
| `--ignore-syntax` | <p>Treat all input as plain text.<br><code>\<br>$ vale --ignore-syntax README.md\<br></code></p>                                                                               |
| `--no-exit`       | <p>Do not return a non-zero exit code if there are errors.<br><code>\<br>$ vale --no-exit README.md\<br></code></p>                                                            |
| `--no-wrap`       | <p>Do not wrap output.<br><code>\<br>$ vale --no-wrap README.md\<br></code></p>                                                                                                |
| `--no-global`     | <p>Do not load the global configuration.<br><code>\<br>$ vale --no-global README.md\<br></code></p>                                                                            |
| `--output`        | <p>Change the output format. See <a href="templates">Templates</a> for more information.<br><code>\<br>$ vale --output=JSON README.md\<br></code></p>                          |
| `--version`       | <p>Print the version of Vale.<br><code>\<br>$ vale --version\<br></code></p>                                                                                                   |

## [Return codes](#return-codes)

The `vale` CLI returns the following exit codes:

| Code | Description                                                                                  |
| ---- | -------------------------------------------------------------------------------------------- |
| `0`  | No error(s) were found.                                                                      |
| `1`  | Linting error(s) were found. Useful for failing CI builds; can be disabled with `--no-exit`. |
| `2`  | Runtime error(s) occurred.                                                                   |

It will try to respect the value of `--output` when printing to `stderr`. For example:

![Vale's exit codes](https://content.gitbook.com/content/EMH7s0sC5N9L8xSMXGwW/blobs/0e5zXEYacO87tfH7lxBH/error.png)
