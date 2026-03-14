# Source: https://buildkite.com/docs/platform/cli/reference/package.md

# Buildkite CLI package command

The `bk package` command allows you to manage packages from the command line.

## Commands

| Command | Description |
| --- | --- |
| `bk package push` | Push a new package to a Buildkite registry |

## Push package

Push a new package to a Buildkite registry

```bash
bk package push <registry-slug> [<std-in-arg>] [flags]
```

### Arguments

| Argument | Description |
| --- | --- |
| `<registry-slug>` | The slug of the registry to push the package to |
| `[<std-in-arg>]` | Use '-' as value to pass package via stdin. Required if --stdin-file-name is used. |

### Flags

| Flag | Description |
| --- | --- |
| `-w`, `--web` | Open the pipeline in a web browser. |
| `--debug` | Enable debug output for REST API calls |
| `--file-path=STRING` | Path to the package file to push |
| `--stdin-file-name=STRING` | The filename to use when reading the package from stdin |

### Examples

Push package from file:

```bash
bk package push my-registry --file-path my-package.tar.gz
```

Push package via stdin:

```bash
cat my-package.tar.gz | bk package push my-registry --stdin-file-name my-package.tar.gz - # Pass package via stdin, note hyphen as the argument
```

add -w to open the build in your web browser:

```bash
bk package push my-registry --file-path my-package.tar.gz -w
```
