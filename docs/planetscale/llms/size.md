# Source: https://planetscale.com/docs/cli/size.md

# PlanetScale CLI commands: size

Lists the sizes for various components within PlanetScale.

## Usage

```bash  theme={null}
pscale size [command]
```

## Available commands

| **Command** | **Product**      | **Description**                          |
| :---------- | :--------------- | :--------------------------------------- |
| `cluster`   | Postgres, Vitess | List the sizes for PlanetScale databases |

## Flags

| **Flag**       | **Description**                       |
| :------------- | :------------------------------------ |
| `-h`, `--help` | Help for size                         |
| `--org string` | The organization for the current user |

### Global flags

| **Command**                 | **Description**                                                                                                    |
| :-------------------------- | :----------------------------------------------------------------------------------------------------------------- |
| `--api-token string`        | The API token to use for authenticating against the PlanetScale API                                                |
| `--api-url string`          | The base URL for the PlanetScale API. (default "\<[https://api.planetscale.com/>](https://api.planetscale.com/>)") |
| `--config string`           | Config file (default is \$HOME/.config/planetscale/pscale.yml)                                                     |
| `--debug`                   | Enable debug mode                                                                                                  |
| `-f`, `--format string`     | Show output in a specific format. Possible values: \[human, json, csv] (default "human")                           |
| `--no-color`                | Disable color output                                                                                               |
| `--service-token string`    | The service token for authenticating                                                                               |
| `--service-token-id string` | The service token ID for authenticating                                                                            |

## The `cluster` sub-command

List the sizes for PlanetScale databases.

**Usage:**

```bash  theme={null}
pscale size cluster [command]
```

**Aliases:** `cluster`, `clusters`

### Available sub-commands

| **Command** | **Product** | **Description**                                              |
| :---------- | :---------- | :----------------------------------------------------------- |
| `list`      | All         | List the sizes that are available for a PlanetScale database |

## The `list` sub-command

List the sizes that are available for a PlanetScale database. Use `--engine` to specify the database engine type.

**Usage:**

```bash  theme={null}
pscale size cluster list [flags]
```

**Aliases:** `list`, `ls`

### Available flags

| **Flag**          | **Description**                                                                                        |
| :---------------- | :----------------------------------------------------------------------------------------------------- |
| `--engine string` | The database engine to show cluster sizes for. Supported values: mysql, postgresql. Defaults to mysql. |
| `-h`, `--help`    | Help for list                                                                                          |
| `--metal`         | View cluster sizes and rates for clusters with metal storage                                           |
| `--region string` | View cluster sizes and rates for a specific region                                                     |

## Examples

### List all available cluster sizes (defaults to Vitess)

```bash  theme={null}
pscale size cluster list
```

### List Vitess cluster sizes explicitly

```bash  theme={null}
pscale size cluster list --engine mysql
```

### List PostgreSQL cluster sizes

```bash  theme={null}
pscale size cluster list --engine postgresql
```

### List cluster sizes for a specific organization

```bash  theme={null}
pscale size cluster list --org <ORG_NAME>
```

### List cluster sizes for a specific region

```bash  theme={null}
pscale size cluster list --region <REGION_NAME>
```

### List PostgreSQL cluster sizes for a specific region

```bash  theme={null}
pscale size cluster list --engine postgresql --region us-east
```

### List Metal cluster sizes (Vitess only)

```bash  theme={null}
pscale size cluster list --metal
```

For more information about PlanetScale cluster sizes and pricing, see:

* [PlanetScale Postgres pricing](https://planetscale.com/docs/postgres/pricing)
* [PlanetScale Vitess plans documentation](https://planetscale.com/docs/planetscale-plans)

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt