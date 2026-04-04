# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/alias-evaluator-revision.md

# firectl alias evaluator-revision

> Alias an evaluator revision

```
firectl alias evaluator-revision [flags]
```

### Examples

```
firectl alias evaluator-revision accounts/my-account/evaluators/my-evaluator/versions/abc123 --alias-id current
```

### Flags

```
      --alias-id string   Alias ID to assign (e.g. current)
  -h, --help              help for evaluator-revision
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.fireworks.ai/llms.txt