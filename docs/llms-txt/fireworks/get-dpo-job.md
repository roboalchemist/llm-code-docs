# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/get-dpo-job.md

# Source: https://docs.fireworks.ai/api-reference/get-dpo-job.md

# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/get-dpo-job.md

# firectl get dpo-job

> Retrieves information about a dpo job.

```
firectl get dpo-job [flags]
```

### Examples

```
firectl get dpo-job my-dpo-job
firectl get dpo-job accounts/my-account/dpo-jobs/my-dpo-job
```

### Flags

```
  -h, --help   help for dpo-job
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```
