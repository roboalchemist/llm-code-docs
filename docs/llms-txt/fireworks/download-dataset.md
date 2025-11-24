# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/download-dataset.md

# firectl download dataset

> Downloads a dataset to a local directory.

```
firectl download dataset [flags]
```

### Examples

```
# Download a single dataset
firectl download dataset my-dataset --output-dir /path/to/download

# Download entire lineage chain
firectl download dataset my-dataset --download-lineage --output-dir /path/to/download
```

### Flags

```
      --download-lineage    If true, downloads entire lineage chain (all related datasets)
  -h, --help                help for dataset
      --output-dir string   Directory to download dataset files to (default ".")
      --quiet               If true, does not show download progress
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
