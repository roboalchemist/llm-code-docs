# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/get-supervised-fine-tuning-job.md

# firectl get supervised-fine-tuning-job

> Retrieves information about a supervised fine-tuning job.

```
firectl get supervised-fine-tuning-job [flags]
```

### Examples

```
firectl get supervised-fine-tuning-job my-sft-job
firectl get supervised-fine-tuning-job accounts/my-account/supervised-fine-tuning-jobs/my-sft-job
```

### Flags

```
  -h, --help   help for supervised-fine-tuning-job
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```
