# Source: https://docs.augmentcode.com/cli/setup-auggie/workspace-context.md

# Workspace context

> Auggie will automatically index the current working directory or directory you specify to give Augment a full view of your system.

## About Workspace Context

Augment is powered by its deep understanding of your code. Your codebase will be automatically indexed when you run `auggie` from a git directory or you can specify a directory to index. If you run Auggie from a non-git directory, a temporary workspace will be created for you.

## Specifying a directory to index

To specify a directory other than the current working directory pass the target directory to the `--workspace-root` flag.

```sh  theme={null}
auggie --workspace-root /path/to/your/project
```

To learn more about what files are indexed and how to ignore files, see [Workspace indexing](/cli/setup-auggie/workspace-indexing).
