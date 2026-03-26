# Source: https://docs.socket.dev/docs/v1-migration-guide.md

# v1 Migration guide

This is the socket (to) v1 migration guide.

If you were using the Socket CLI before v1.0.0 you may need to go through this guide to see if something changed.

If you use the CLI locally you may want to `socket login` again to set the default org, or otherwise it will ask you to confirm the org when you run commands that need it. In CI you can use `--org xyz` instead.

## commands

In general: We tried to streamline usage of the CLI (:

* the mandatory org name (slug) argument has been dropped from all commands that had it in favor of a stored default org. When this config value is not set but required by a command (which many commands do) an interactive prompt will try to resolve it for you.
  * If you want to specify the org explicitly anyways (like probably in CI) you can use `--org <orgname>` instead. It should work for all commands that might use an org and will show up in `--help`.
* the mandatory cwd arg or flag has been dropped from many commands in favor of an optional argument, using the current directory as the default. A few commands will still use a --cwd flag if that just makes more sense.
* Any shortcuts for flags were removed (they were not advertised)

### socket analytics

The command flags were changed to args.

Before:

* `socket analytics --scope org --time Y`
* `socket analytics --scope repo --repo X --time Y`\
  after:
* `socket analytics org Y`
* `socket analytics repo X Y`

The args are optional but the order is fixed. When you use "repo" the repo name is mandatory.\
The repo/scope/time flags are no longer supported.

### socket audit-log

The command now defaults to the default org setting. It will prompt you if none is set. You can use `--no-interactive` to prevent this prompt which will cause the command to fail.

You can override that and explicitly set the org through the `--org` flag instead.

The type filter has now become the first argument, still optional.

Before:

* `socket audit-log --page 10 --perPage 50`
* `socket audit-log --type createLabel --page 10 --perPage 50`\
  after:
* `socket audit-log --page 10 --perPage 50`
* `socket audit-log createLabel --page 10 --perPage 50`

### socket dependencies

This command moved to a sub-command of orgs: `socket organization dependencies` (but you can use the secret alias `socket deps` or keep using the secret alias `socket dependencies` too ;) )

### socket diff-scan

This command was sunset in favor of `socket scan diff`

### socket info

This command was sunset in favor of `socket package shallow`.

Note that there is also `socket package score`, which will give you a transitive score (the `info` command was always shallow).

The new score commands also supports any ecosystem, whereas the `info` command was bound to the `npm` ecosystem.

### socket organization

If you were using `socket organization` directly for information, you now have to use `socket organization list` instead. Same otherwise but we removed the toplevel to show help instead.

### socket organization policy security

The command now defaults to the default org setting. It will prompt you if none is set. You can use `--no-interactive` to prevent this prompt which will cause the command to fail.

You can override that and explicitly set the org through the `--org` flag instead.

### socket report

This command was sunset in favor of `socket scan report` and `socket scan --report`

### socket repos

This command was renamed to `socket repository` (but `repos` was added as a secret alias ;) ).

### socket repository create

The command now defaults to the default org setting. It will prompt you if none is set. You can use `--no-interactive` to prevent this prompt which will cause the command to fail.

You can override that and explicitly set the org through the `--org` flag instead.

The `--repoName` flag was removed in favor of the repo being the (mandatory) first arg of the command. This should still be a "slug".

### socket repository del

The command now defaults to the default org setting. It will prompt you if none is set. You can use `--no-interactive` to prevent this prompt which will cause the command to fail.

You can override that and explicitly set the org through the `--org` flag instead.

The `--repoName` flag was removed in favor of the repo being the (mandatory) first arg of the command. This should still be a "slug".

### socket repository list

The command now defaults to the default org setting. It will prompt you if none is set. You can use `--no-interactive` to prevent this prompt which will cause the command to fail.

You can override that and explicitly set the org through the `--org` flag instead.

### socket repository update

The command now defaults to the default org setting. It will prompt you if none is set. You can use `--no-interactive` to prevent this prompt which will cause the command to fail.

You can override that and explicitly set the org through the `--org` flag instead.

### socket repository view

The command now defaults to the default org setting. It will prompt you if none is set. You can use `--no-interactive` to prevent this prompt which will cause the command to fail.

You can override that and explicitly set the org through the `--org` flag instead.

### socket scan create

The command now defaults to the default org setting. It will prompt you if none is set. You can use `--no-interactive` to prevent this prompt which will cause the command to fail.

You can override that and explicitly set the org through the `--org` flag instead.

Note: this command has been expanded with various tools, like generating manifests for certain ecosystem and waiting for the report to complete.

The TARGET dir/file is now optional, defaulting to the current dir where you ran the command. Note that controlling the CWD explicitly is still by setting the `--cwd` flag.

### socket scan del

The command now defaults to the default org setting. It will prompt you if none is set. You can use `--no-interactive` to prevent this prompt which will cause the command to fail.

You can override that and explicitly set the org through the `--org` flag instead.

### socket scan list

The command now defaults to the default org setting. It will prompt you if none is set. You can use `--no-interactive` to prevent this prompt which will cause the command to fail.

You can override that and explicitly set the org through the `--org` flag instead.

The `--repo` flag has been changed to the first argument: `socket scan list my-repo`

The `--branch` flag has been kept but if you specify a repo, you can pass in a second argument as branch name: `socket scan list my-repo test-branch`. You can still use `--branch`, which you would need to if you don't specify a repo arg.

### socket scan metadata

The command now defaults to the default org setting. It will prompt you if none is set. You can use `--no-interactive` to prevent this prompt which will cause the command to fail.

You can override that and explicitly set the org through the `--org` flag instead.

### socket scan report

The command now defaults to the default org setting. It will prompt you if none is set. You can use `--no-interactive` to prevent this prompt which will cause the command to fail.

You can override that and explicitly set the org through the `--org` flag instead.

### socket scan view

The command now defaults to the default org setting. It will prompt you if none is set. You can use `--no-interactive` to prevent this prompt which will cause the command to fail.

You can override that and explicitly set the org through the `--org` flag instead.

### socket threat-feed

The command now defaults to the default org setting. It will prompt you if none is set. You can use `--no-interactive` to prevent this prompt which will cause the command to fail.

You can override that and explicitly set the org through the `--org` flag instead.

You can specify the filters on the command line now. The CLI will try to detect the type of filter each arg belongs to by matching the value against the enum for ecosystem and filter type, or by checking `v?\d+.\d+.\d+`. First value that does not match one of these three becomes the package name filter.

```
socket threat-feed npm eslint 1.0.0
socket thread-feed mal babel
socket thread-feed typo log4j
```

Since it's inconvenient to search for certain package names this way you can still use the flags too. Args will override flags in case of conflict so if you want to be safe you should use explicitly use flags. This will also allow you to use less common version specifiers or prefixes when you need to.

```
socket threat-feed --eco=npm --name=eslint --version=1.0.0
socket thread-feed --type=mal --name=babel
socket thread-feed --type=typo --name=log4j
```

### socket wrapper

The `--enable` and `--disable` flag were replaced by a first argument "on" and "off" (or "enable(d)" and "disable(d)" if you prefer).