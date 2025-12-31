# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/rollback-evaluator.md

# firectl rollback evaluator

> Rollback an evaluator to a specific revision

```
firectl rollback evaluator [flags]
```

### Examples

```
firectl rollback evaluator accounts/my-account/evaluators/my-evaluator/versions/abc123
```

### Flags

```
  -h, --help   help for evaluator
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.fireworks.ai/llms.txt