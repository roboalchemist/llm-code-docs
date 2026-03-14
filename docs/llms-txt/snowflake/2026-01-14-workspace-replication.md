# Source: https://docs.snowflake.com/en/release-notes/2026/other/2026-01-14-workspace-replication.md

# Jan 14, 2026: Workspace replication (*Preview*)

Workspace replication, which allows user workspaces to be included in database replication and failover operations, is now available in [preview](../../preview-features.md).
When a workspace or its owning user is part of a replication or failover group, the workspace is copied to secondary accounts to support business
continuity and disaster recovery.

Replicated workspaces in secondary accounts are read-only. Files can be executed but not modified. When a secondary failover group is promoted
to primary, all contained workspaces become writable.

> **Note:**
>
> Workspace replication and failover require Business Critical Edition or higher.

For more information, see [Workspace replication](../../../user-guide/ui-snowsight/workspaces-replication.md).
