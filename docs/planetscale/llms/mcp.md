# Source: https://planetscale.com/docs/vitess/connecting/mcp.md

# Source: https://planetscale.com/docs/cli/mcp.md

# PlanetScale CLI commands: mcp

## Getting Started

Make sure to first [set up your PlanetScale developer environment](/docs/cli/planetscale-environment-setup). Once you've installed the `pscale` CLI, you can interact with PlanetScale and manage your databases straight from the command line.

## The `mcp` command

This command installs and enables support for a PlanetScale MCP server.

**Usage:**

```bash  theme={null}
pscale mcp <SUB-COMMAND> <FLAG>
```

### Available sub-commands

| **Sub-command** | **Product**      | **Description**        |
| :-------------- | :--------------- | :--------------------- |
| `install`       | Postgres, Vitess | Install the MCP server |
| `server`        | Postgres, Vitess | Start the MCP server   |

### Available flags

| **Flag**       | **Description**                                                                                  |
| :------------- | :----------------------------------------------------------------------------------------------- |
| `--target`     | The target installation for the MCP server. `claude` and `cursor` are the only supported values. |
| `-h`, `--help` | View help for `mcp` command                                                                      |

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

## Examples

### The `mcp` command with `list` sub-command

**Command:**

```bash  theme={null}
pscale mcp install --target cursor
```

**Output:**

```bash  theme={null}
MCP server successfully configured for cursor at /Users/your-name/.cursor/mcp.json
```

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt