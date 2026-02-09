# Source: https://docs.turso.tech/cli/db/import.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# db import

You can import an existing SQLite file to Turso Cloud using the following command:

```bash  theme={null}
turso db import ~/path/to/database.db
```

<Info>
  Make sure the SQLite file has WAL journal mode enabled.
</Info>

<Info>
  If you have more than one group, you will need to pass the `--group` flag.
</Info>

## Flags

| Flag           | Description                                 |
| -------------- | ------------------------------------------- |
| `--group`      | Import the database in the specified group. |
| `-h`, `--help` | Get help for import.                        |
