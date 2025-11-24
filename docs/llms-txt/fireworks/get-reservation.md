# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/get-reservation.md

# firectl get reservation

> Prints information about a reservation.

```
firectl get reservation [flags]
```

### Examples

```
firectl get reservation abcdef
firectl get reservation accounts/my-account/reservations/abcdef
```

### Flags

```
  -h, --help   help for reservation
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```
