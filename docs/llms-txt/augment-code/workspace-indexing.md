# Source: https://docs.augmentcode.com/vim/setup-augment/workspace-indexing.md

# Source: https://docs.augmentcode.com/setup-augment/workspace-indexing.md

# Source: https://docs.augmentcode.com/jetbrains/setup-augment/workspace-indexing.md

# Source: https://docs.augmentcode.com/cli/setup-auggie/workspace-indexing.md

# Source: https://docs.augmentcode.com/vim/setup-augment/workspace-indexing.md

# Source: https://docs.augmentcode.com/setup-augment/workspace-indexing.md

# Source: https://docs.augmentcode.com/jetbrains/setup-augment/workspace-indexing.md

# Source: https://docs.augmentcode.com/cli/setup-auggie/workspace-indexing.md

# Source: https://docs.augmentcode.com/vim/setup-augment/workspace-indexing.md

# Source: https://docs.augmentcode.com/setup-augment/workspace-indexing.md

# Source: https://docs.augmentcode.com/jetbrains/setup-augment/workspace-indexing.md

# Source: https://docs.augmentcode.com/cli/setup-auggie/workspace-indexing.md

# Source: https://docs.augmentcode.com/setup-augment/workspace-indexing.md

# Source: https://docs.augmentcode.com/jetbrains/setup-augment/workspace-indexing.md

# Source: https://docs.augmentcode.com/cli/setup-auggie/workspace-indexing.md

# Source: https://docs.augmentcode.com/vim/setup-augment/workspace-indexing.md

# Source: https://docs.augmentcode.com/setup-augment/workspace-indexing.md

# Source: https://docs.augmentcode.com/jetbrains/setup-augment/workspace-indexing.md

# Source: https://docs.augmentcode.com/cli/setup-auggie/workspace-indexing.md

# Index your workspace

> When your workspace is indexed, Augment can provide tailored code suggestions and answers based on your unique codebase, best practices, coding patterns, and preferences. You can always control what files are indexed.

## Security and privacy

Augment stores your code securely and privately to enable our powerful context engine. We ensure code privacy through a proof-of-possession API and maintain strict internal data minimization principles. [Read more about our security](https://www.augmentcode.com/security).

## What gets indexed

Augment will index all the files in your workspace, except for the files that match patterns in your `.gitignore` file and the `.augmentignore` file. [Read more about Workspace Context](/cli/setup-auggie/workspace-context).

## Ignoring files with .augmentignore

The `.augmentignore` file is a list of file patterns that Augment will ignore when indexing your workspace. Create an `.augmentignore` file in the root of your workspace. You can use any glob pattern that is supported by the [gitignore](https://git-scm.com/docs/gitignore) file.

## Including files that are .gitignored

If you have a file or directory in your `.gitignore` that you want to be indexed, you can add it to your `.augmentignore` file using the `!` prefix.

For example, you may want your `node_modules` indexed to provide Augment with context about the dependencies in their project, but it is typically included in their `.gitignore`. Add `!node_modules` to your `.augmentignore` file.

<CodeGroup>
  ```bash .augmentignore theme={null}
  # Include .gitignore excluded files with ! prefix
  !node_modules

  # Exclude other files with .gitignore syntax
  data/test.json
  ```

  ```bash .gitignore theme={null}
  # Exclude dependencies
  node_modules

  # Exclude secrets
  .env

  # Exclude build artifacts
  out
  build
  ```
</CodeGroup>
