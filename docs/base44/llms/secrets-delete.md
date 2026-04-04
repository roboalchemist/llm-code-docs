# Source: https://docs.base44.com/developers/references/cli/commands/secrets-delete.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# secrets delete

> Delete one or more project secrets

Delete secrets from your project. When you delete a secret, any deployed backend functions that reference it are automatically redeployed.

<Warning>
  If a backend function references a deleted secret, it may fail when trying to
  access the missing value. Remove the secret from your function code before
  deleting it.
</Warning>

## Usage

```bash  theme={null}
base44 secrets delete <secret_names>
```

## Arguments

| Argument         | Description                                   | Required |
| ---------------- | --------------------------------------------- | -------- |
| `<secret_names>` | One or more secret names, separated by spaces | Yes      |

## Example

```bash  theme={null}
base44 secrets delete API_KEY DATABASE_URL
```

## See also

* [`secrets list`](/developers/references/cli/commands/secrets-list): List configured secrets
* [`secrets set`](/developers/references/cli/commands/secrets-set): Set one or more secrets
* [Backend Functions](/developers/backend/resources/backend-functions/overview): Use secrets as environment variables in your functions


Built with [Mintlify](https://mintlify.com).