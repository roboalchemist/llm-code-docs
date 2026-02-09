# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-db-clone.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# aptible db:clone

This command clones an existing Database.\
\
❗️ Warning: Consider using [`aptible backup:restore`](/reference/aptible-cli/cli-commands/cli-backup-restore) instead.

> `db:clone` connects to your existing Database to copy data out and imports it into your new Database.

> This means `db:clone` creates load on your existing Database, and can be slow or disruptive if you have a lot of data to copy. It might even fail if the new Database is underprovisioned, since this is a resource-intensive process.

> This also means `db:clone` only works for a subset of [Supported Databases](/core-concepts/managed-databases/supported-databases/overview) (those that allow for convenient import / export of data).

> In contrast, `backup:restore` instead uses a snapshot of your existing Database's disk, which means it doesn't affect your existing Database at all and supports all Aptible-supported Databases.

# Synopsis

```
Usage:
  aptible db:clone SOURCE DEST

Options:
  --env, [--environment=ENVIRONMENT]
```
