# Source: https://docs.baseten.co/reference/cli/chains/chains-cli.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Chains CLI reference

> Deploy, manage, and develop Chains using the Truss CLI.

```sh  theme={"system"}
truss chains [OPTIONS] COMMAND [ARGS]...
```

| Command           | Description                |
| ----------------- | -------------------------- |
| [`init`](#init)   | Initialize a Chain project |
| [`push`](#push)   | Deploy a Chain             |
| [`watch`](#watch) | Live reload development    |

***

## `init`

Initialize a Chain project.

```sh  theme={"system"}
truss chains init [OPTIONS] [DIRECTORY]
```

* `DIRECTORY` (optional): Path to a new or empty directory for the Chain. Defaults to the current directory if omitted.

**Options:**

* `--log` `[humanfriendly | INFO | DEBUG]`: Set log verbosity.
* `--help`: Show this message and exit.

**Example:**

To create a new Chain project in a directory called `my-chain`, use the following:

```sh  theme={"system"}
truss chains init my-chain
```

***

## `push`

Deploy a Chain.

```sh  theme={"system"}
truss chains push [OPTIONS] SOURCE [ENTRYPOINT]
```

* `SOURCE`: Path to a Python file that contains the entrypoint chainlet.
* `ENTRYPOINT` (optional): Class name of the entrypoint chainlet. If omitted, the chainlet tagged with `@chains.mark_entrypoint` is used.

**Options:**

* `--name` (TEXT): Custom name for the Chain (defaults to entrypoint name).
* `--publish / --no-publish`: Create chainlets as a published deployment.
* `--promote / --no-promote`: Promote newly deployed chainlets into production.
* `--environment` (TEXT): Deploy chainlets into a particular environment.
* `--wait / --no-wait`: Wait until all chainlets are ready (or deployment failed).
* `--watch / --no-watch`: Watch the Chains source code and apply live patches. Using this option waits for the Chain to be deployed (the `--wait` flag is applied) before starting to watch for changes. This option requires the deployment to be a development deployment.
* `--experimental-chainlet-names` (TEXT): Run `watch`, but only apply patches to specified chainlets. The option is a comma-separated list of chainlet (display) names. This option can give faster dev loops, but also lead to inconsistent deployments. Use with caution and refer to [docs](/development/chain/watch).
* `--dryrun`: Produce only generated files, but don't deploy anything.
* `--remote` (TEXT): Name of the remote in .trussrc to push to.
* `--team` (TEXT): Name of the team to deploy to. If not specified, Truss infers the team or prompts for selection.
* `--log` `[humanfriendly|I|INFO|D|DEBUG]`: Customize logging.
* `--help`: Show this message and exit.

<Note>
  The `--team` flag is only available if your organization has teams enabled. [Contact us](mailto:support@baseten.co) to enable teams, or see [Teams](/organization/teams) for more information.
</Note>

**Example:**

To deploy a Chain as a development deployment, use the following:

```sh  theme={"system"}
truss chains push my_chain.py
```

To deploy and promote to production, use the following:

```sh  theme={"system"}
truss chains push my_chain.py --publish --promote
```

To deploy to a specific team, use the following:

```sh  theme={"system"}
truss chains push my_chain.py --team my-team-name
```

***

## `watch`

Live reload development.

```sh  theme={"system"}
truss chains watch [OPTIONS] SOURCE [ENTRYPOINT]
```

* `SOURCE`: Path to a Python file containing the entrypoint chainlet.
* `ENTRYPOINT` (optional): Class name of the entrypoint chainlet. If omitted, the chainlet tagged with `@chains.mark_entrypoint` is used.

**Options:**

* `--name` (TEXT): Name of the Chain to be deployed. If not given, the entrypoint name is used.
* `--remote` (TEXT): Name of the remote in .trussrc to push to.
* `--team` (TEXT): Name of the team to deploy to. If not specified, Truss infers the team or prompts for selection.

<Note>
  The `--team` flag is only available if your organization has teams enabled. [Contact us](mailto:support@baseten.co) to enable teams, or see [Teams](/organization/teams) for more information.
</Note>

* `--experimental-chainlet-names` (TEXT): Run `watch`, but only apply patches to specified chainlets. The option is a comma-separated list of chainlet (display) names. This option can give faster dev loops, but also lead to inconsistent deployments. Use with caution and refer to [docs](/development/chain/watch).
* `--log` `[humanfriendly|W|WARNING|I|INFO|D|DEBUG]`: Customize logging.
* `--help`: Show this message and exit.

**Example:**

To watch a Chain for live reload during development, use the following:

```sh  theme={"system"}
truss chains watch my_chain.py
```
