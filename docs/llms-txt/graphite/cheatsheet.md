# Source: https://graphite-58cc94ce.mintlify.dev/docs/cheatsheet.md

# Command Cheatsheet

While you can find a full list of `gt` commands in the [command reference](/command-reference), there are a handful of common commands and combinations to remember.

This list is grouped by primary function.

## Basic workflow commands

These commands are constantly in use when creating and pushing changes to a repository with Graphite.

| Command                                               | Alias                        | Description                                                                                                                            |
| ----------------------------------------------------- | ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `gt log short`                                        | `gt ls`                      | List Graphite-tracked stacks and branches in your repository in a minimized format                                                     |
| `gt create --all --message <COMMIT_MESSAGE>`          | `gt c -am <COMMIT_MESSAGE>`  | Create changes, stage the changes, create a new branch and commit the changes to the new branch all at once                            |
| `gt submit --stack`                                   | `gt ss`                      | Submit your changes across all PRs on a stack                                                                                          |
| `gt submit --stack --update-only`                     | `gt ss -u`                   | Update all PRs for branches in your stack that already have PRs, but do not create new ones                                            |
| `gt modify`                                           | `gt m -a`                    | Update an existing branch with all new changes by amending the existing commit on that branch                                          |
| `gt modify --all --commit --message <COMMIT_MESSAGE>` | `gt m -cam <COMMIT_MESSAGE>` | Update an existing branch with all new changes by creating an entirely new commit on that branch                                       |
| `gt undo`                                             | `gt undo`                    | Undo the most recent Graphite mutations                                                                                                |
| `gt sync --force`                                     | `gt sync -f`                 | Pull your trunk branch, automatically clean up any branches corresponding to merged PRs, and restack any branches that do not conflict |

## Collaborate on a stack

Commands to view teammates' code and communicate changes.

| Command                | Alias   | Description                                                                                                                                        |
| ---------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `gt get <BRANCH_NAME>` |         | Get a stack locally that's been created or manipulated by someone else. Often followed up with \`gt delete\` to delete irrelevant branches locally |
| `gt checkout`          | `gt co` | Often used when to check out a singular branch for collaboration OR personal use                                                                   |

## Stack navigation/manipulation commands

Commands to move up and down the stack, and to restack branches (if necessary).

| Command             | Alias        | Description                                                                                                                                                                        |
| ------------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `gt up, gt down`    | `gt u, gt d` | Quickly move up and down a stack of branches. By default, it takes a step argument of 1, but can add a step value (for example, \`gt up 2\`) to skip a certain number of branches. |
| `gt top, gt bottom` | `gt t, gt b` | Quickly move all the way down (b) or all the way up (t) a stack                                                                                                                    |
