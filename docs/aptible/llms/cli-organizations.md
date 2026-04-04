# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-organizations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# aptible organizations

This command lists all organizations you have access to, along with your roles in each organization.

# Synopsis

```
Usage:
  aptible organizations

Options:
  None
```

# Output

The command displays each organization with its ID, name, and your roles within that organization.

## Text Format

By default, the command outputs in a human-readable text format:

```
Id: 5ca1ab1e-0000-0000-0000-000000000000
Name: Acme Prod
Roles:
  Id: 5afe5afe-0000-0000-0000-000000000000
  Name: Deploy Owners

  Id: acce5500-0000-0000-0000-000000000000
  Name: Read Only

Id: cafecafe-cafe-cafe-cafe-cafecafecafe
Name: Acme Test
Roles:
  Id: c0ffee50-0000-0000-0000-000000000000
  Name: Account Owners
```

## JSON Format

Set the `APTIBLE_OUTPUT_FORMAT=json` environment variable for machine-readable JSON output:

```shell  theme={null}
APTIBLE_OUTPUT_FORMAT=json aptible organizations
```

```json  theme={null}
[
  {
    "id": "5ca1ab1e-0000-0000-0000-000000000000",
    "name": "Acme Prod",
    "roles": [
      {
        "id": "5afe5afe-0000-0000-0000-000000000000",
        "name": "Deploy Owners"
      },
      {
        "id": "acce5500-0000-0000-0000-000000000000",
        "name": "Read Only"
      }
    ]
  },
  {
    "id": "cafecafe-cafe-cafe-cafe-cafecafecafe",
    "name": "Acme Test",
    "roles": [
      {
        "id": "c0ffee50-0000-0000-0000-000000000000",
        "name": "Account Owners"
      }
    ]
  }
]
```

# Examples

```shell  theme={null}
aptible organizations
```

```shell  theme={null}
APTIBLE_OUTPUT_FORMAT=json aptible organizations
```

# Related Commands

* [aptible environment:list](/reference/aptible-cli/cli-commands/cli-environment-list) - List environments within an organization
* [aptible login](/reference/aptible-cli/cli-commands/cli-login) - Log in to Aptible
