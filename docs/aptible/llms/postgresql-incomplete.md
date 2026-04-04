# Source: https://www.aptible.com/docs/how-to-guides/troubleshooting/common-errors-issues/postgresql-incomplete.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# PostgreSQL Incomplete Startup Packet

## Cause

When you add a [Database Endpoint](/core-concepts/managed-databases/connecting-databases/database-endpoints) to a [PostgreSQL](/core-concepts/managed-databases/supported-databases/postgresql) Database, Aptible automatically performs periodic TCP health checks to ensure the Endpoint can reach the Database.

These health checks consist of opening a TCP connection to the Database and closing it once that succeeds. As a result, PostgreSQL will log a `incomplete startup packet` error message every time the Endpoint performs a health check.

## Resolution

If you have a Database Endpoint associated with your PostgreSQL Database, you can safely ignore these messages. You might want to consider adding filtering rules in your logging provider to drop the messages entirely.
