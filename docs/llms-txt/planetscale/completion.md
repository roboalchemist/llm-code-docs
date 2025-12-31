# Source: https://planetscale.com/docs/cli/completion.md

# PlanetScale CLI commands: completion

## Getting Started

Make sure to first [set up your PlanetScale developer environment](/docs/cli/planetscale-environment-setup). Once you've installed the `pscale` CLI, you can interact with PlanetScale and manage your databases straight from the command line.

## The `completion` command

This command allows you to generate a completion script for the specified shell.

**Usage:**

```bash  theme={null}
pscale completion <SUB-COMMAND> <FLAG>
```

### Available sub-commands

| **Sub-command** | **Description**                             | **Product** |
| :-------------- | :------------------------------------------ | :---------- |
| `bash`          | Generated completion for `bash` shell       | All         |
| `zsh`           | Generated completion for `zsh` shell        | All         |
| `fish`          | Generated completion for `fish` shell       | All         |
| `powershell`    | Generated completion for `powershell` shell | All         |

### Available flags

| **Flag**       | **Description**                    |
| :------------- | :--------------------------------- |
| `-h`, `--help` | View help for `completion` command |

### Global flags

| **Command**                     | **Description**                                                                      |
| :------------------------------ | :----------------------------------------------------------------------------------- |
| `--api-token <TOKEN>`           | The API token to use for authenticating against the PlanetScale API.                 |
| `--api-url <URL>`               | The base URL for the PlanetScale API. Default is `https://api.planetscale.com/`.     |
| `--config <CONFIG_FILE>`        | Config file. Default is `$HOME/.config/planetscale/pscale.yml`.                      |
| `--debug`                       | Enable debug mode.                                                                   |
| `-f`, `--format <FORMAT>`       | Show output in a specific format. Possible values: `human` (default), `json`, `csv`. |
| `--no-color`                    | Disable color output.                                                                |
| `--service-token <TOKEN>`       | The service token for authenticating.                                                |
| `--service-token-id <TOKEN_ID>` | The service token ID for authenticating.                                             |

## How to load completions

### Bash

```bash  theme={null}
source <(pscale completion bash)

# To load completions for each session, execute once:
# Linux:
pscale completion bash > /etc/bash_completion.d/pscale
# macOS:
pscale completion bash > /usr/local/etc/bash_completion.d/pscale
```

### Zsh

```bash  theme={null}
# If shell completion is not already enabled in your environment,
# you will need to enable it.  You can execute the following once:

echo "autoload -U compinit; compinit" >> ~/.zshrc

# To load completions for each session, execute once:
pscale completion zsh > "${fpath[1]}/_yourprogram"

# You will need to start a new shell for this setup to take effect.
```

### fish

```bash  theme={null}
pscale completion fish | source

# To load completions for each session, execute once:
pscale completion fish > ~/.config/fish/completions/pscale.fish
```

### PowerShell

```bash  theme={null}
pscale completion powershell | Out-String | Invoke-Expression

# To load completions for every new session, run:
pscale completion powershell > pscale.ps1
# and source this file from your PowerShell profile.
```

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt