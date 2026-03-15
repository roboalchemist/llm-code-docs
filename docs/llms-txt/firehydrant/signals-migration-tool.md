# Source: https://docs.firehydrant.com/docs/signals-migration-tool.md

# Migration Tool

FireHydrant has released an open-source migration tool, [hosted here on GitHub](https://github.com/FireHydrant/signals-migrator). This tool supports importing resources from legacy alerting tools PagerDuty, Opsgenie, and Splunk On-Call (VictorOps).

The tool runs in a Terminal, and the output is Terraform configuration with the selected components you've chosen to import from the selected alerting tool.

> 🚧 Note:
>
> If you're on Windows, then you should use Go package manager to install with `go install github.com/firehydrant/signals-migrator@latest`. Executables are only supported for Linux/MacOS.

## Installation and Setup

You can download the binary from the [releases section on GitHub](https://github.com/firehydrant/signals-migrator/releases) or you can use the Go toolchain to install the binary:

```
go install github.com/firehydrant/signals-migrator@latest
```

Once downloaded, you will want to ensure the following environmental variables are set:

| Variable              | Description                                                                                                                                    |
| :-------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------- |
| `FIREHYDRANT_API_KEY` | An API key with access to FireHydrant. You can learn more about these on [API Keys](https://docs.firehydrant.com/docs/api-keys).                                             |
| `PROVIDER`            | One of `PagerDuty`, `Opsgenie`, or `VictorOps`. The value is case-insensitive, so for example both `PagerDuty` and `pagerduty` are acceptable. |
| `PROVIDER_API_KEY`    | API key for the alerting provider you're migrating from.                                                                                       |
| `PROVIDER_APP_ID`     | Only required for VictorOps. This will be your API ID, which can be found in VictorOps on the **Integrations > API** page.                     |

## Import Usage

Execute the program by running `signals-migrator import`. You will be taken through an interactive prompt to select and choose Users, Teams, Escalation Policies, and On-Call Schedules to select, depending on your provider.

<Image alt="Example of interacting with the tool" align="center" width="650px" src="https://files.readme.io/c5c21c6-demo-screencast.gif">
  Example of interacting with the tool
</Image>

Any questions or comments as you use the migrator can be directly submitted in the repository as a GitHub issue or reported to FireHydrant support.

Once the tool has finished executing, it will output Terraform configuration into the `output/*` folder. From there, you may choose to apply the Terraform configuration and discard it or alternatively fold it in together with other Terraform configuration for FireHydrant.

```Text Terminal Output
Imported schedules from pagerduty.
Please select (out of 1) which escalation policies to migrate.
You have selected:
  [+] ADD ALL
[+] All escalation policies will be migrated to FireHydrant.
Imported escalation policies from pagerduty.
Terraform file has been written to output/pagerduty_to_fh_signals.tf
```

```clojure Terraform Example Output
terraform {
  required_providers {
    firehydrant = {
      source  = "firehydrant/firehydrant"
      version = "~> 0.13.5"
    }
  }
}

data "firehydrant_user" "john_doe" {
  email = "john.doe@acme.com"
  # [PagerDuty] john.doe@acme.com https://acmeco.pagerduty.com/users/ABCDEFG
}

resource "firehydrant_team" "team_a" {
  name = "Team A"

  # [PagerDuty] PagerDuty Service A https://acmeco.pagerduty.com/service-directory/BCDEFGH
}

import {
  id = "a7955482-ab28-4ca3-99c5-63bb31f568fc"
  to = firehydrant_team.team_a
}

resource "firehydrant_escalation_policy" "ep_pd_example" {
  name    = "ep-pd-example"
  team_id = firehydrant_team.team_a.id

  # [PagerDuty]
  #   ep-pd-example https://acmeco.pagerduty.com/escalation_policies/DEFGHIJ
  # [Services]
  #   - PagerDuty Service A https://acmeco.pagerduty.com/service-directory/PK5I5QF A Vinny Service 123

  step {
    timeout = "PT1M"
  }

  step {
    timeout = "PT30M"

    targets {
      type = "User"
      id   = data.firehydrant_user.john_doe.id
    }
  }

  repetitions = 0
}
```