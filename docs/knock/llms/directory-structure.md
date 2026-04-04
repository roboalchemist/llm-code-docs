# Source: https://docs.knock.app/cli/overview/directory-structure.md

# Directory structure

There is no required directory structure when working with Knock resources locally. However, if you use the `knock pull` or `knock push` commands, they will produce and expect the directory structure outlined below.

For forward compatibility, we recommend using this structure to ensure your local files work seamlessly with future CLI updates.

When you use `knock pull`, resources will be grouped by resource type within subdirectories. The following directory structure will be created:

{`./knock/
├── guides/
├── layouts/
├── message-types/
├── partials/
├── translations/
└── workflows/`}

Each resource type has its own directory structure, which is described in detail in the sections below for each resource type.
