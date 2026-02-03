# Source: https://docs.turso.tech/cli/db/export.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# db export

Export a database snapshot from Turso to a SQLite file.

This command exports a snapshot of the current generation of a Turso database to a local SQLite file. Note that the exported file may not contain the latest changes. Use SDK to sync the database after exporting to ensure you have the most recent version.

```bash  theme={null}
turso db export <database> [flags]
```

## Flags

| Flag              | Description                                             |
| ----------------- | ------------------------------------------------------- |
| `--output-file`   | Specify the output file name (default: `<database>.db`) |
| `--overwrite`     | Overwrite output file if it exists                      |
| `--with-metadata` | Include metadata in the export                          |
| `-h`, `--help`    | Help for export                                         |
