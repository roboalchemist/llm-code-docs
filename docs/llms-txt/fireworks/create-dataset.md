# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/create-dataset.md

# Source: https://docs.fireworks.ai/api-reference/create-dataset.md

# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/create-dataset.md

# Source: https://docs.fireworks.ai/api-reference/create-dataset.md

# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/create-dataset.md

# Source: https://docs.fireworks.ai/api-reference/create-dataset.md

# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/create-dataset.md

# Source: https://docs.fireworks.ai/api-reference/create-dataset.md

# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/create-dataset.md

# firectl create dataset

> Creates and uploads a dataset.

```
firectl create dataset [flags]
```

### Examples

```
firectl create dataset my-dataset /path/to/dataset.jsonl
firectl create dataset --trace-from-model-id model_abc --format chat --date 2024-01-10 my-dataset
firectl create dataset my-dataset --external-url gs://bucket-name/object-name
```

### Flags

```
      --display-name string    The display name of the dataset.
      --end-time string        The end time for which to trace data (format: YYYY-MM-DD). Only specify for traced dataset.
      --eval-protocol-output   If true, the dataset is in eval protocol output format.
      --external-url string    The GCS URI that points to the dataset file.
      --filter string          Filter condition to apply to the source dataset.
  -h, --help                   help for dataset
      --quiet                  If true, does not print the upload progress bar.
      --source string          Source dataset ID to filter from.
      --start-time string      The start time for which to trace data (format: YYYY-MM-DD). Only specify for traced dataset.
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```
