# Source: https://buildkite.com/docs/apis/rest-api/user.md

# Source: https://buildkite.com/docs/platform/cli/reference/user.md

# Buildkite CLI user command

The `bk user` command allows you to manage users in your Buildkite organization from the command line.

## Commands

| Command | Description |
| --- | --- |
| `bk user invite` | Invite users to your organization. |

## Invite user

Invite users to your organization.

```bash
bk user invite <emails> ...
```

### Flags

| Flag | Description |
| --- | --- |
| `--debug` | Enable debug output for REST API calls |

### Examples

Invite a single user to your organization:

```bash
bk user invite bob@supercoolorg.com
```

Invite multiple users to your organization:

```bash
bk user invite bob@supercoolorg.com bobs_mate@supercoolorg.com
```
