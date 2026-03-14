# Source: https://docs.anyscale.com/reference/scim.md

# SCIM API Reference

[View Markdown](/reference/scim.md)

# SCIM API Reference

#### Customer-hosted cloud features[​](#customer-hosted-only "Direct link to Customer-hosted cloud features")

note

Some features are only available on customer-hosted clouds. Reach out to <support@anyscale.com> for info.

## SCIM CLI[​](#scim-cli "Direct link to SCIM CLI")

### `anyscale scim enforce-groups` Beta[​](#anyscale-scim-enforce-groups-beta "Direct link to anyscale-scim-enforce-groups-beta")

warning

This command undergoes rapid iteration. Users must be tolerant of change.

**Usage**

`anyscale scim enforce-groups [OPTIONS]`

Enforce SCIM-based user group permissions by removing individual user permissions.

This command removes ALL direct user permissions so that users only derive permissions from their user groups.

Use --dry-run to preview what permission changes users will experience before actually applying them.

**Options**

* **`--dry-run`**: Preview permission changes without applying them. Shows only actual changes from users' perspective.

#### Examples[​](#examples "Direct link to Examples")

* CLI

```
# Preview permission changes before applying (dry-run mode)
$ anyscale scim enforce-groups --dry-run
(anyscale +0.5s) Running in dry-run mode. Analyzing permission changes...

=== Permission Changes Preview ===

user1@example.com:
  - clouds:
      - prod-cloud: collaborator -> readonly
      - staging-cloud: owner -> (removed)
  - projects:
      - proj-1: collaborator -> readonly
  - organization: owner -> collaborator

user2@example.com:
  - clouds:
      - dev-cloud: collaborator -> (removed)

--- Users to be removed (not in any active user group) ---
  - orphan-user@example.com

(No changes were applied. Remove --dry-run to apply changes.)

# Apply the changes (live mode)
$ anyscale scim enforce-groups
(anyscale +0.5s) Analyzing permission changes...

=== Permission Changes Preview ===

user1@example.com:
  - clouds:
      - prod-cloud: collaborator -> readonly
      - staging-cloud: owner -> (removed)
  - projects:
      - proj-1: collaborator -> readonly
  - organization: owner -> collaborator

user2@example.com:
  - clouds:
      - dev-cloud: collaborator -> (removed)

--- Users to be removed (not in any active user group) ---
  - orphan-user@example.com

╭─────────────────── ⚠️  Confirmation Required ───────────────────╮
│ WARNING: This is a destructive operation that cannot be undone. │
│                                                                  │
│ All role bindings on users will be removed.                      │
│ Role bindings on user groups and service accounts are unchanged. │
╰──────────────────────────────────────────────────────────────────╯
Do you want to proceed? [y/N]: y
(anyscale +1.5s) Starting SCIM permission migration...

=== Applied Permission Changes ===

user1@example.com:
  - clouds:
      - prod-cloud: collaborator -> readonly
      - staging-cloud: owner -> (removed)
  - projects:
      - proj-1: collaborator -> readonly
  - organization: owner -> collaborator

user2@example.com:
  - clouds:
      - dev-cloud: collaborator -> (removed)

--- Users to be removed (not in any active user group) ---
  - orphan-user@example.com

(anyscale +2.0s) SCIM permission migration completed successfully.
```
