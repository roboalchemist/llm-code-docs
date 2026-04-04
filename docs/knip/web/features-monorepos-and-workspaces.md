# Monorepos & Workspaces

Source: https://knip.dev/features/monorepos-and-workspaces

Workspaces are handled out-of-the-box by Knip.

Workspaces are sometimes also referred to as package-based monorepos, or as
packages in a monorepo. Knip uses the term workspace exclusively to indicate a
directory that has apackage.json.

## Configuration

Here’s example configuration with customentryandprojectpatterns:

```typescript
{"workspaces":{".":{"entry":"scripts/*.js","project":"scripts/**/*.js"},"packages/*":{"entry":"{index,cli}.ts","project":"**/*.ts"},"packages/cli":{"entry":"bin/cli.js"}}}
```

Run Knip without any configuration to see if and where customentryand/orprojectfiles are necessary per workspace.

Each workspace has the samedefault configuration.

The root workspace is named"."underworkspaces(like in the example
above).

In a project with workspaces, theentryandprojectoptions at the root
level are ignored. Use the workspace named"."for those (like in the example
above).

## Workspaces

Knip reads workspaces from four possible locations:

- Theworkspacesarray inpackage.json(npm, Bun, Yarn, Lerna)
- Thepackagesarray inpnpm-workspace.yaml(pnpm)
- Theworkspaces.packagesarray inpackage.json(legacy)
- Theworkspacesobject in Knip configuration

Theworkspacesin Knip configuration (4) not already defined in the rootpackage.jsonorpnpm-workspace.yaml(1, 2, 3) are added to the analysis.

A workspace must have apackage.jsonfile.

For projects with only a rootpackage.json, please seeintegrated
monorepos.

## Additional workspaces

If a workspaces is not configured as such inpackage.json#workspaces(orpnpm-workspace.yaml) it can be added to the Knip configuration manually. Add
their path to theworkspacesconfiguration object the same way as"packages/cli": {}in the example above.

## Source mapping

SeeSource Mapping.

## Additional options

The following options are available inside workspace configurations:

- ignore
- ignoreBinaries
- ignoreDependencies
- ignoreMembers
- ignoreUnresolved
- includeEntryExports

Pluginscan be configured separately per workspace.

Use--debugfor verbose output and see the workspaces Knip includes, their
configurations, enabled plugins, glob options and resolved files.

## Lint a single workspace

Use the--workspace(or-W) argument to focus on a single workspace (and let
Knip run faster). Example:

```typescript
knip--workspacepackages/my-lib
```

This will include the target workspace, but also ancestor and dependent
workspaces. For two reasons:

- Ancestor workspaces may list dependencies inpackage.jsonthe linted
workspace uses.
- Dependent workspaces may reference exports from the linted workspace.

To lint the workspace in isolation, there are two options:

- Combine theworkspaceargument withstrict production mode.
- Run Knip from inside the workspace directory.

ISC License© 2024Lars Kappert

