# Source: https://configcat.com/docs/advanced/cli.md

# Command Line Interface (CLI)

The [ConfigCat Command Line Interface (CLI)](https://github.com/configcat/cli) allows you to interact with the [Public Management API](https://configcat.com/docs/docs/api/reference/configcat-public-management-api/.md) via the command line. It supports most functionality found on the ConfigCat Dashboard. You can manage ConfigCat resources like Feature Flags, Targeting / Percentage rules, Products, Configs, Environments, and more.

The CLI also has the ability to [scan your source code](https://configcat.com/docs/docs/advanced/code-references/overview/.md) for feature flag and setting usage and upload the found code references to ConfigCat.

Finally, the CLI provides a few useful utilities, such as validating a config JSON file, downloading one from the ConfigCat CDN by SDK Key, etc. These can come in handy when you use [flag overrides](https://configcat.com/docs/docs/sdk-reference/js/overview/.md#flag-overrides) in your application.

```
configcat
  This is the Command Line Tool of ConfigCat.
  ConfigCat is a hosted feature flag service: https://configcat.com
  For more information, see the documentation here: https://configcat.com/docs/advanced/cli

Usage:
  configcat [command] [options]

Options:
  -v, --verbose           Print detailed execution information
  -ni, --non-interactive  Turn off progress rendering and interactive features
  --version               Show version information
  -?, -h, --help          Show help and usage information

Commands:
  setup                        Setup the CLI with Public Management API host and credentials
  ls                           List all Product, Config, and Environment IDs
  p, product                   Manage Products
  c, config                    Manage Configs
  webhook, wh                  Manage Webhooks
  e, environment               Manage Environments
  f, flag, s, setting          Manage Feature Flags & Settings
  f2, flag-v2, s2, setting-v2  Manage V2 Feature Flags & Settings
  seg, segment                 Manage Segments
  permission-group, pg         Manage Permission Groups
  m, member                    Manage Members
  t, tag                       Manage Tags
  k, sdk-key                   List SDK Keys
  scan <directory>             Scan files for Feature Flag & Setting usages
  config-json                  Config JSON-related utilities
  w, workspace                 Manage the CLI workspace. When set, the CLI's interactive mode
                               filters Product and Config selectors by the values set in the
                               workspace

Use "configcat [command] -?" for more information about a command.
```

## Reference[​](#reference "Direct link to Reference")

See the [command reference documentation](https://configcat.github.io/cli/) for more information about each available command.

## Getting started[​](#getting-started "Direct link to Getting started")

The following instructions will guide you through the first steps to start using this tool.

### Installation[​](#installation "Direct link to Installation")

You can install the CLI on multiple operating systems using the following sources.

**Homebrew (macOS / Linux)**

Install the CLI with [Homebrew](https://brew.sh) from [ConfigCat's tap](https://github.com/configcat/homebrew-tap) by executing the following command:

```
brew tap configcat/tap
brew install configcat
```

**Snap (Linux)**

Install the CLI with [Snapcraft](https://snapcraft.io) by executing the following command:

```
sudo snap install configcat
```

**Scoop (Windows)**

Install the CLI with [Scoop](https://scoop.sh) from [ConfigCat's bucket](https://github.com/configcat/scoop-configcat) by executing the following command:

```
scoop bucket add configcat https://github.com/configcat/scoop-configcat
scoop install configcat
```

**Chocolatey (Windows)**

Install the CLI with [Chocolatey](https://chocolatey.org/) by executing the following command:

```
choco install configcat
```

**.NET tool / NuGet.org**

The CLI can be installed as a [.NET tool](https://learn.microsoft.com/en-us/dotnet/core/tools/global-tools) via the .NET SDK.

```
dotnet tool install -g configcat-cli
```

After installing, you can execute the CLI using the `configcat` command:

```
configcat scan "/repository" --print --config-id <CONFIG-ID>
```

**Docker**

The CLI can be executed from a [Docker](https://www.docker.com/) image.

```
docker pull configcat/cli
```

An example of how to scan a repository for feature flag & setting references with the docker image.

```
docker run --rm \
    --env CONFIGCAT_API_HOST=<API-HOST> \
    --env CONFIGCAT_API_USER=<API-USER> \
    --env CONFIGCAT_API_PASS=<API-PASSWORD> \
    -v /path/to/repository:/repository \
  configcat/cli scan "/repository" --print --config-id <CONFIG-ID>
```

**Install Script**

On Unix platforms, you can install the CLI by executing an install script.

```
curl -fsSL "https://raw.githubusercontent.com/configcat/cli/main/scripts/install.sh" | bash
```

By default, the script downloads the OS specific artifact from the latest [GitHub Release](https://github.com/configcat/cli/releases) with `curl` and moves it into the `/usr/local/bin` directory.

It might happen that you don't have permissions to write into `/usr/local/bin`, then you should execute the install script with `sudo`.

```
curl -fsSL "https://raw.githubusercontent.com/configcat/cli/main/scripts/install.sh" | sudo bash
```

The script accepts the following input parameters:

| Parameter         | Description                                      | Default value    |
| ----------------- | ------------------------------------------------ | ---------------- |
| `-d`, `--dir`     | The directory where the CLI should be installed. | `/usr/local/bin` |
| `-v`, `--version` | The desired version to install.                  | `latest`         |
| `-a`, `--arch`    | The desired architecture to install.             | `x64`            |

Available **architecture** values for Linux: `x64`, `musl-x64`, `arm`, `arm64`.

Available **architecture** values for macOS: `x64`, `arm64`.

**Script usage examples**:

*Custom installation directory*:

```
curl -fsSL "https://raw.githubusercontent.com/configcat/cli/main/scripts/install.sh" | bash -s -- -d=/path/to/install
```

*Install a different version*:

```
curl -fsSL "https://raw.githubusercontent.com/configcat/cli/main/scripts/install.sh" | bash -s -- -v=1.4.2
```

*Install with custom architecture*:

```
curl -fsSL "https://raw.githubusercontent.com/configcat/cli/main/scripts/install.sh" | bash -s -- -a=arm
```

**Standalone executables**

You can download the executables directly from [GitHub Releases](https://github.com/configcat/cli/releases) for your desired platform.

### Setup[​](#setup "Direct link to Setup")

After a successful installation, the CLI must be set up with your [ConfigCat Public Management API credentials](https://app.configcat.com/my-account/public-api-credentials).

You can do this by using the `configcat setup` command.

![interactive](/docs/assets/cli/cli-setup.gif)

#### Environment variables[​](#environment-variables "Direct link to Environment variables")

Besides the `setup` command above, the CLI can read your credentials from the following environment variables.

| Name                 | Description                              |
| -------------------- | ---------------------------------------- |
| `CONFIGCAT_API_HOST` | API host (default: `api.configcat.com`). |
| `CONFIGCAT_API_USER` | API basic auth user name.                |
| `CONFIGCAT_API_PASS` | API basic auth password.                 |

caution

When any of these environment variables are set, the CLI will use them over the local values set by the `configcat setup` command.

## Modes[​](#modes "Direct link to Modes")

The CLI supports both interactive and argument driven execution. When no arguments provided for a command and user input is enabled (stdout is not redirected), the CLI automatically activates interactive mode.

### Interactive[​](#interactive "Direct link to Interactive")

![interactive](/docs/assets/cli/cli-flag-create.gif)

### With arguments[​](#with-arguments "Direct link to With arguments")

The same operation with command arguments would look like this:

```
configcat flag-v2 create \
  --config-id <config-id> \
  --name "My awesome feature" \
  --hint "This is my awesome feature" \
  --key my_awesome_feature
  --type boolean \
  --tag-ids <tag-id-1> <tag-id-2> \
  --init-values-per-environment <environment-id>:<initial-value> \
```

info

Each `create` command writes the newly created resource's ID to the standard output so you can save that for further operations.

Example:

```
#!/bin/bash

ORGANIZATION_ID="<your-organization-id>"
PRODUCT_ID=$(configcat product create -o $ORGANIZATION_ID -n "<product-name>")
CONFIG_ID=$(configcat config create -p $PRODUCT_ID -n "<config-name>")
```

info

You can change the output format of several commands' result to JSON with the `--json` option, like: `configcat flag ls --json`. See more about these commands in the [command reference documentation](https://configcat.github.io/cli/).

## Scan & upload code references[​](#scan--upload-code-references "Direct link to Scan & upload code references")

The CLI has the ability to scan your source code for feature flag and setting usage and upload the found code references to ConfigCat. You can read more about this feature [here](https://configcat.com/docs/docs/advanced/code-references/overview/.md).

## Examples[​](#examples "Direct link to Examples")

Here are a few examples showing the true power of the CLI.

### Create a feature flag[​](#create-a-feature-flag "Direct link to Create a feature flag")

The following example shows how you can create a feature flag in a specific config.

![create flag](/docs/assets/cli/cli-flag-create.gif)

### Value update[​](#value-update "Direct link to Value update")

The following example shows how you can update the value of a feature flag in a specific environment.

![flag value update](/docs/assets/cli/cli-flag-update.gif)

### Add targeting rules[​](#add-targeting-rules "Direct link to Add targeting rules")

The following example shows how you can add targeting rules to a feature flag.

![flag targeting add](/docs/assets/cli/cli-flag-targeting-add.gif)

### Add percentage options[​](#add-percentage-options "Direct link to Add percentage options")

The following example shows how you can set percentage options in a feature flag.

![flag percentage add](/docs/assets/cli/cli-flag-targeting-percentage.gif)
