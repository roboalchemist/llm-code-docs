# Source: https://www.aptible.com/docs/core-concepts/managed-databases/connecting-databases/database-tunnels.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Database Tunnels

# Overview

Database Tunnels are ephemeral connections between your local workstation and a [Database](/core-concepts/managed-databases/overview) running on Aptible. Database Tunnels are the most convenient way to get ad-hoc access to your Database. However, tunnels time out after 24 hours, so they're not ideal for long-term access or integrations. For those, you'll be better suited by [Database Endpoints](/core-concepts/managed-databases/connecting-databases/database-endpoints).

<Warning> A Database Tunnel listens on `localhost`, and instructs you to connect via the host name `localhost.aptible.in`. Be aware that some software may make assumptions about this database based on the host name or IP, with possible consequences such as bypassing safeguards for running against a remote (production) database.</Warning>

# Getting Started

<Accordion title="Creating Database Tunnels">
  Database Tunnels can be created using the [`aptible db:tunnel`](/reference/aptible-cli/cli-commands/cli-db-tunnel) command.
</Accordion>
