# Source: https://docs.baseten.co/reference/cli/chains/chains-cli.md

# Chains CLI reference

> Deploy, manage, and develop Chains using the Truss CLI.

# Deploy a Chain

## `push`

```sh  theme={"system"}
truss chains push [OPTIONS] SOURCE [ENTRYPOINT]
```

Deploys a chain to a remote environment.

* `SOURCE`: Path to a python file that contains the entrypoint chainlet.
* `ENTRYPOINT` (optional): Class name of the entrypoint chainlet. If omitted, the chainlet tagged with `@chains.mark_entrypoint` is used.

**Options:**

* `--name` (TEXT): Custom name for the chain (defaults to entrypoint name).
* `--publish / --no-publish`: Create chainlets as a published deployment.
* `--promote / --no-promote`: Promote newly deployed chainlets into production.
* `--environment` (TEXT): Deploy chainlets into a particular environment.
* `--wait / --no-wait`: Wait until all chainlets are ready (or deployment
  failed).
* `--watch / --no-watch`: Watches the chains source code and applies live
  patches. Using this option will wait for the chain to be deployed
  (i.e.`--wait` flag is applied), before starting to watch for changes.
  This option requires the deployment to be a development deployment.
* `--experimental-chainlet-names`: (TEXT): Runs `watch`, but only applies
  patches to specified chainlets. The option is a comma-separated list of
  chainlet (display) names. This option can give faster dev loops, but also
  lead to inconsistent deployments. Use with caution and refer to
  [docs](/development/chain/watch).
* `--dryrun`: Produces only generated files, but doesn't deploy anything.
* `--remote` (TEXT): Name of the remote in .trussrc to push to.
* `--log` `[humanfriendly|I|INFO|D|DEBUG]`: Customizes logging.
* `--help`: Show this message and exit.

***

# Live Reload Development

## `watch`

```sh  theme={"system"}
truss chains watch [OPTIONS] SOURCE [ENTRYPOINT]
```

Watches for source code changes and applies live updates to a development deployment.

* `SOURCE`: Path to a Python file containing the entrypoint chainlet.
* `ENTRYPOINT` (optional): Class name of the entrypoint chainlet. If omitted, the chainlet tagged with `@chains.mark_entrypoint` is used.

**Options:**

* `--name` (TEXT): Name of the chain to be deployed, if not given, the
  entrypoint name is used.
* `--remote`: (TEXT): Name of the remote in .trussrc to
  push to.
* `--experimental-chainlet-names`: (TEXT): Runs `watch`, but only applies
  patches to specified chainlets. The option is a comma-separated list of
  chainlet (display) names. This option can give faster dev loops, but also
  lead to inconsistent deployments. Use with caution and refer to
  [docs](/development/chain/watch).
* `--log [humanfriendly|W|WARNING|I|INFO|D|DEBUG]`: Customizes logging.
* `--help`: Show this message and exit.

***

# Initialize a Chain Project

## `init`

```sh  theme={"system"}
truss chains init [OPTIONS] [DIRECTORY]
```

Initializes a chains project directory.

* `DIRECTORY` (optional): Path to a **new or empty directory** for the chain. Defaults to the **current directory** if omitted.

Options:

* `--log LEVEL` → Set log verbosity `[humanfriendly | INFO | DEBUG]`.
* `--help` → Show command details.
