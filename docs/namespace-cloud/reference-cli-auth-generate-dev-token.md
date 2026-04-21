<!-- Source: https://namespace.so/docs/reference/cli/auth-generate-dev-token -->

# nsc auth generate-dev-token

Generate a Namespace Cloud token for development purposes.

`nsc auth generate-dev-token` generates a token that can be used to access the [Namespace API](/docs/reference/api-sdk)
and for direct calls to the [Container Registry](/docs/architecture/storage/container-registry#programmatic-access)

## Usage

```
nsc auth generate-dev-token [--output_to path]
```

### Example

Logged in:

```
$ nsc auth generate-dev-token
nsct_eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.tyh-VfuzIxCyGYDlkBA7DfyjrqmSHu6pQ2hoZuFqUSLPNY2N0mpHb3nk5K17HWP_3cYHBw7AhHale5wky6-sVA
```

## Options

### --output\_to string

If specified, write the access token to this path.

Last updated July 8, 2025
