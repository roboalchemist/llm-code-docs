# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-environment-ca-cert.md

# aptible environment:ca_cert

# Synopsis

```
Usage:
  aptible environment:ca_cert

Options:
  --env, [--environment=ENVIRONMENT]

Retrieve the CA certificate associated with the environment
```

> 📘 Since most Database clients will want you to provide a PEM formatted certificate as a file, you will most likely want to simply redirect the output of this command directly to a file, eg: "aptible environment:ca\_cert &> all-aptible-CAs.pem" or "aptible environment:ca\_cert --environment=production &> production-CA.pem".
