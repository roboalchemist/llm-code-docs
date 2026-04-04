# Source: https://planetscale.com/docs/cli/region.md

# PlanetScale CLI commands: region

## Getting Started

Make sure to first [set up your PlanetScale developer environment](/docs/cli/planetscale-environment-setup). Once you've installed the `pscale` CLI, you can interact with PlanetScale and manage your databases straight from the command line.

## The `region` command

This command lists all available [PlanetScale regions](/docs/vitess/regions).

**Usage:**

```bash  theme={null}
pscale region <SUB-COMMAND> <FLAG>
```

### Available sub-commands

| **Sub-command** | **Product**      | **Description**  |
| :-------------- | :--------------- | :--------------- |
| `list`          | Postgres, Vitess | List all regions |

### Available flags

| **Flag**       | **Description**                |
| :------------- | :----------------------------- |
| `-h`, `--help` | View help for `region` command |

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

### The `region` command with `list` sub-command

**Command:**

```bash  theme={null}
pscale region list
```

**Output:**

```bash  theme={null}
  NAME                                             SLUG                         ENABLED
 ------------------------------------------------- ---------------------------- ---------
  AWS us-east-2 (Ohio)                             aws-us-east-2                 Yes
  AWS us-east-1 (N. Virginia)                      us-east                       Yes
  AWS us-west-2 (Oregon)                           us-west                       Yes
  AWS eu-west-1 (Dublin)                           eu-west                       Yes
  AWS ap-south-1 (Mumbai)                          ap-south                      Yes
  AWS ap-southeast-1 (Singapore)                   ap-southeast                  Yes
  AWS ap-northeast-1 (Tokyo)                       ap-northeast                  Yes
  AWS eu-central-1 (Frankfurt)                     eu-central                    Yes
  AWS ap-southeast-2 (Sydney)                      aws-ap-southeast-2            Yes
  AWS sa-east-1 (Sao Paulo)                        aws-sa-east-1                 Yes
  GCP us-central1 (Council Bluffs, Iowa)           gcp-us-central1               Yes
  AWS eu-west-2 (London)                           aws-eu-west-2                 Yes
  GCP us-east4 (Ashburn, Virginia)                 gcp-us-east4                  Yes
  GCP northamerica-northeast1 (Montréal, Québec)   gcp-northamerica-northeast1   Yes
  GCP asia-northeast3 (Seoul, South Korea)         gcp-asia-northeast3           Yes
  GCP europe-west1 (St Ghislain, Belgium)          gcp-europe-west1              Yes
  AWS ca-central-1 (Montreal)                      aws-ca-central-1              Yes
```

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt