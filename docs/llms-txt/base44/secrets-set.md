# Source: https://docs.base44.com/developers/references/cli/commands/secrets-set.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# secrets set

> Set one or more project secrets

Set secrets for your project. Secrets are available to your [backend functions](/developers/backend/resources/backend-functions/overview) as environment variables via `Deno.env.get()`. When you set a secret, any deployed backend functions that reference it are automatically redeployed with the new value.

If a secret with the same name already exists, its value is overwritten. You can provide secrets as inline `KEY=VALUE` pairs or load them from an `.env` file.

## Usage

Set one or more secrets inline, separated by spaces:

```bash  theme={null}
base44 secrets set <KEY=VALUE...>
```

Or load from an `.env` file:

```bash  theme={null}
base44 secrets set --env-file <path>
```

<Warning>
  You cannot combine inline KEY=VALUE pairs with `--env-file` in the same
  command.
</Warning>

## Arguments

| Argument         | Description                                      | Required                        |
| ---------------- | ------------------------------------------------ | ------------------------------- |
| `<KEY=VALUE...>` | One or more KEY=VALUE pairs, separated by spaces | Yes (unless using `--env-file`) |

## Flags

| Flag                | Description                                        |
| ------------------- | -------------------------------------------------- |
| `--env-file <path>` | Path to a `.env` file containing `KEY=VALUE` pairs |

## Example

```bash  theme={null}
base44 secrets set API_KEY=sk-abc123 DATABASE_URL=postgres://localhost/mydb
```

## See also

* [`secrets list`](/developers/references/cli/commands/secrets-list): List configured secrets
* [`secrets delete`](/developers/references/cli/commands/secrets-delete): Delete one or more secrets
* [Backend Functions](/developers/backend/resources/backend-functions/overview): Use secrets as environment variables in your functions


Built with [Mintlify](https://mintlify.com).