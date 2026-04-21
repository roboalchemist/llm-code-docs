<!-- Source: https://namespace.so/docs/workspaces -->

# Workspaces

Learn about workspaces at Namespace, how ownership and isolation works and why a multi-tenant account can be helpful.

## What is a workspace?

Your workspace - sometimes also referred to as a tenant - can enable collaboration on a set of resources.

When joining Namespace, a personal workspace gets created for you.
You can immediately start running instances on that workspace.
[More on how to get started](/docs/solutions/github-actions)

You can also create multiple workspaces via the dashboard:

![Workspace selector dropdown menu, cursor on New Workspace button](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fworkspace-selector-new-workspace.a1f0329d.png&w=750&q=75)

Workspace selector in the top-left of the Dashboard

![New Workspace Dialog](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fnew-workspace-dialog.e5856787.png&w=750&q=75)

New Workspace Dialog

## Where do I find my workspace ID (tenant ID)?

In order for the Namespace team to be able to identify your workspace, it is helpful to share your unique workspace ID.
You can find your Workspace ID on the [Settings page](https://cloud.namespace.so/workspace/settings).

## Who can access my workspace?

From creation, each workspace is completely isolated and personal.
Namespace ensures high security standards and comprehensive access control mechanisms
to help you manage who can access your workspace and what actions they can perform.

An invitation from an owner or admin of the workspace is required to add additional users.

[More information on Workspace access](/docs/workspaces/access)

## How to handle multiple teams from the same company using Namespace?

Namespace can support different scenarios for multiple teams from the same company using Namespace.
Depending on the use case, the following setup is recommended:

|  | Multiple teams running in the **same workspace** | Each team has their own workspace connected as a **multi-tenant account** | Each team has their own **independent workspace** |
| --- | --- | --- | --- |
| **Shared invoice** One invoice including accumulated usage. | Yes | Yes | No |
| **Shared usage budget** Teams share the included unit minutes, builds, etc. | Yes | Yes | No |
| **Shared dashboard** The dashboard is the same for all members: Usage details, instance details, etc. | Yes | No | No |
| **Shared concurrency limits** Teams use the same concurrency budget | Yes | Limits can be set globally and per-workspace | No |
| **Sharing cache volumes possible** Share common caches between teams | Yes | No | No |
| **Can share a GitHub Installation** | Yes | No | No |
| **Shared audit logs** Including workspace event audits | Yes | Same audit log export sink can be configured | No |

Last updated July 8, 2025
