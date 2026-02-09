# Source: https://docs.turso.tech/cli/plan/show.md

# Source: https://docs.turso.tech/cli/db/show.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# db show

You can obtain details about the database, including the name, ID, libSQL server version, group, size and location.

```bash  theme={null}
turso db show <database-name> [flags]
```

You can also obtain the different URLs for the database using the following:

## Flags

| Flag         | Description                              |
| ------------ | ---------------------------------------- |
| `--url`      | Show URL for the database HTTP API.      |
| `--http-url` | Show HTTP URL for the database HTTP API. |
