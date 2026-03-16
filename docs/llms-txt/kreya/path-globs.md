# Source: https://kreya.app/docs/cli/path-globs.md

# Path globs

Some commands, such as [`kreyac operation invoke`](/docs/cli/commands/operation/invoke.md) or [`kreyac script invoke`](/docs/cli/commands/script/invoke.md), accept a list of globs. With globs, you can specify a range of files and folders without repeating yourself.

info

Be careful when using globs in some shells, for example, bash. When running

```
kreyac script invoke ./my-scripts/**
```

the shell would expand the glob **before** it is passed to Kreya. We recommend enclosing the globs in single quotes to disable this behavior:

```
kreyac script invoke './my-scripts/**'
```

## Excluding files and folders[​](#excluding-files-and-folders "Direct link to Excluding files and folders")

If a glob starts with an exclamation mark `!`, it marks the matched files and folders as excluded.

```
kreyac operation invoke '**' '!directory-to-ignore/'
```

This example would invoke all operations, except those located in the `directory-to-ignore` folder.

## Relative path resolution[​](#relative-path-resolution "Direct link to Relative path resolution")

By default, all paths and globs are resolved relative to the **Kreya project directory**. You can change this behavior with the `--relative-to` option.

### Accepted values[​](#accepted-values "Direct link to Accepted values")

| Value                       | Alias | Description                                                     |
| --------------------------- | ----- | --------------------------------------------------------------- |
| `project`                   |       | Resolve paths relative to the Kreya project directory (default) |
| `current-working-directory` | `cwd` | Resolve paths relative to the current working directory         |

### Examples[​](#examples "Direct link to Examples")

Invoke operations relative to the project directory (default behavior):

```
kreyac operation invoke 'gRPC/**'
```

Invoke operations relative to the current working directory:

```
kreyac operation invoke 'subfolder/**' --relative-to cwd
```

This is useful when your working directory is not the project's root directory and you want to reference paths relative to where you are, rather than the project root:

```
cd my-project/gRPC
kreyac operation invoke --relative-to cwd '.'
```
