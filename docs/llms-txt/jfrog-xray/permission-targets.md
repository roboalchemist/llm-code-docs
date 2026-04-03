# Source: https://docs.jfrog.com/artifactory/docs/permission-targets.md

# Permission targets in Artifactory

Permission targets control which users and groups can access repositories, builds, and release bundles in Artifactory, and what actions they are allowed to perform. Use the JFrog CLI to create, update, and delete permission targets programmatically — useful for infrastructure-as-code workflows and CI/CD pipelines.

## Workflow Overview

The CLI commands are usually combined in this order:

* [jf rt permission-target-template](/docs/jf-rt-permission-target-template) (`rt ptt`) — generate a JSON template interactively in a terminal.
* [jf rt permission-target-create](/docs/jf-rt-permission-target-create) (`rt ptc`) — create a new permission target from a template file.
* [jf rt permission-target-update](/docs/jf-rt-permission-target-update) (`rt ptu`) — replace an existing permission target from a template file.
* [jf rt permission-target-delete](/docs/jf-rt-permission-target-delete) (`rt ptdel`) — permanently remove a permission target.

## Commands

| Command                                                                    | Alias      | Description                                                |
| -------------------------------------------------------------------------- | ---------- | ---------------------------------------------------------- |
| [jf rt permission-target-template](/docs/jf-rt-permission-target-template) | `rt ptt`   | Create a JSON template interactively (requires a terminal) |
| [jf rt permission-target-create](/docs/jf-rt-permission-target-create)     | `rt ptc`   | Create a new permission target from a template file        |
| [jf rt permission-target-update](/docs/jf-rt-permission-target-update)     | `rt ptu`   | Replace an existing permission target from a template file |
| [jf rt permission-target-delete](/docs/jf-rt-permission-target-delete)     | `rt ptdel` | Permanently delete a permission target                     |