# Source: https://buildkite.com/docs/platform/cli/reference/api.md

# Buildkite CLI api command

The `bk api` command allows you to interact with the Buildkite API from the command line.

Interact with the Buildkite API Interact with either the REST or GraphQL Buildkite APIs.

```bash
bk api [<endpoint>] [flags]
```

## Arguments

| Argument | Description |
| --- | --- |
| `[<endpoint>]` | API endpoint to call |

## Flags

| Flag | Description |
| --- | --- |
| `-d`, `--data=STRING` | Data to send in the request body |
| `-f`, `--file=STRING` | File containing GraphQL query |
| `-H`, `--headers=HEADERS,...` | Headers to include in the request |
| `-X`, `--method=STRING` | HTTP method to use |
| `--analytics` | Use the Test Analytics endpoint |
| `--debug` | Enable debug output for REST API calls |
| `--verbose` | Enable verbose output (currently only provides information about rate limit exceeded retries) |

## Examples

To get a build:

```bash
bk api /pipelines/example-pipeline/builds/420
```

To create a pipeline:

```bash
bk api --method POST /pipelines --data '
{
"name": "My Cool Pipeline",
"repository": "git@github.com:acme-inc/my-pipeline.git",
"configuration": "steps:\n - command: env"
}
'
```

To update a cluster:

```bash
bk api --method PUT /clusters/CLUSTER_UUID --data '
{
"name": "My Updated Cluster",
}
'
```

To get all test suites:

```bash
bk api --analytics /suites
```

Run GraphQL query from file:

```bash
bk api --file get_build.graphql
```
