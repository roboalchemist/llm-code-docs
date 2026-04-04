# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/get-evaluator-revision.md

# firectl get evaluator-revision

> Get an evaluator revision

```
firectl get evaluator-revision [flags]
```

### Examples

```
firectl get evaluator-revision accounts/my-account/evaluators/my-evaluator/versions/latest
```

### Flags

```
  -h, --help   help for evaluator-revision
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.fireworks.ai/llms.txt