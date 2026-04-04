# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/batch-inference-job-delete.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# firectl batch-inference-job delete

> Deletes a batch inference job.

```
firectl batch-inference-job delete [flags]
```

### Examples

```
firectl batch-inference-job delete my-batch-job
firectl batch-inference-job delete accounts/my-account/batchInferenceJobs/my-batch-job
```

### Flags

```
      --dry-run                 Print the request proto without running it.
  -h, --help                    help for delete
  -o, --output Output           Set the output format to "text", "json", or "flag". (default text)
      --wait                    Wait until the batch inference job is deleted.
      --wait-timeout duration   Maximum time to wait when using --wait flag. (default 30m0s)
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
