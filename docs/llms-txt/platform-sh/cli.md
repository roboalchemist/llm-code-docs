# Source: https://docs.upsun.com/administration/cli.md

# Command line interface (CLI)


See how to use and manage your Upsun projects directly from your terminal. Anything you can do within the Console can be done with the CLI.

The CLI uses the git interface and the [Upsun REST API](https://api.platform.sh/docs/) to accomplish tasks.
Its source code is hosted on [GitHub](https://github.com/platformsh/cli).

## 1. Install

To install the CLI, use a [Bash installation script](https://github.com/platformsh/cli#user-content-bash-installer).
You can also install with [Homebrew](https://brew.sh/) (on Linux, macOS, or the Windows Subsystem for Linux)
or [Scoop](https://scoop.sh/) (on Windows. You must also have the [Extras bucket](https://github.com/ScoopInstaller/Extras) already installed for this).

```bash {}
brew install platformsh/tap/upsun-cli

```
```bash {}
scoop bucket add platformsh https://github.com/platformsh/homebrew-tap.git
scoop install upsun

```

**Note**: 

If you are using Scoop, you **must** have the [Extras bucket](https://github.com/ScoopInstaller/Extras) already installed before installing the Upsun CLI.

## 2. Authenticate

To list and manage your projects, authenticate by running the following command:

```bash
upsun
```

This process opens a browser tab for you to log in.
It also creates certificates on your computer for [SSH](https://docs.upsun.com../../development/ssh.md).

Once you are logged in, a list of your projects appears, along with some tips for getting started.
If you experience authentication issues or want to force a login, run the command `upsun login`.

## 3. Use

Now you can run actions on your projects such as branching and merging.
You can also simulate a local build of your codebase as if you were pushing a change to Upsun,
including your services and data.

Get a list of all available commands with:

```bash
upsun list
```

To get more information on a specific command, preface it with `help`:

```bash
upsun help get
```

You get output similar to the following:

```bash
Command: project:get
Aliases: get
Description: Clone a project locally

Usage:
 upsun get [-e|--environment ENVIRONMENT] [--depth DEPTH] [--build] [-p|--project PROJECT] [--host HOST] [-i|--identity-file IDENTITY-FILE] [--] [] []

Arguments:
  project                            The project ID
  directory                          The directory to clone to. Defaults to the project title

Options:
  -e, --environment=ENVIRONMENT      The environment ID to clone. Defaults to the project default, or the first available
                                     environment
      --depth=DEPTH                  Create a shallow clone: limit the number of commits in the history
      --build                        Build the project after cloning
  -p, --project=PROJECT              The project ID or URL
      --host=HOST                    The project's API hostname
  -i, --identity-file=IDENTITY-FILE  An SSH identity (private key) to use
  -h, --help                         Display this help message
  -q, --quiet                        Do not output any message
  -V, --version                      Display this application version
  -y, --yes                          Answer "yes" to any yes/no questions; disable interaction
  -n, --no                           Answer "no" to any yes/no questions; disable interaction
  -v|vv|vvv, --verbose               Increase the verbosity of messages

Examples:
 Clone the project "abc123" into the directory "my-project":
   upsun get abc123 my-project
```

### Select the right project and environment

When you are in an empty directory or a directory not associated with a specific Upsun project,
if you run a command that requires a specific project and environment, you are prompted to select them.

For example, if you run the following command:

```bash
upsun environment:info
```

You get the following output:

```bash
Enter a number to choose a project:
  [0] My project (xb3pfo734qxbeg)
  [1] A great project (3p5fmol45kxp6)
  [2] An even better project (rjify4y564xaa)
>
```

If your working directory is inside a local checkout of your project repository,
your project and environment are detected automatically.

You can always specify the project and environment in two ways:

* As arguments for the command:

  ```bash
  upsun environment:info --project=my-project --environment=staging
  ```
* With environment variables:

  ```bash
  export PLATFORM_PROJECT=my-project;
  export PLATFORM_BRANCH=staging;
  upsun environment:info
  ```

In [multi-app](https://docs.upsun.com../../create-apps/multi-app.md) projects, this applies also to selecting the right app
(the environment variable would be `PLATFORM_APPLICATION_NAME`).

#### RootNotFoundException

If you check out a project via Git directly and not using the `upsun get` command,
the CLI may be unable to determine what project it's in.
You might run a CLI command from within a project directory you've checked out and get an error like this:

```text {no-copy="true"}
[RootNotFoundException] Project root not found. This can only be run from inside a project directory.
```

Then the CLI hasn't been able to determine the project to use.
To fix this, run:

```bash
upsun project:set-remote --project <PROJECT_ID>
```

Replace `<PROJECT_ID>` with the ID of your project.
You can find that in the Console or by running `upsun projects` to list all accessible projects.

### Choose between the CLI and Git commands

Some CLI commands (especially many within the `environment` namespace) have some overlap with Git commands.
Generally, they offer more options than the Git commands alone.
For example, `upsun push` offers options such as `--activate` (to activate an environment before pushing)
and `--no-wait` (so you can continue working without waiting for the push to complete).

For all of them, you don't need to configure a Git remote.
It's enough to have a project ID.

An example of how this affects commands is that when you run `upsun merge`,
it doesn't affect your local codebase.
You don't even need the code locally.
The code is only merged between environments remotely.

### Customize the CLI

You can customize how the CLI operates and what it returns with a configuration file (`~/.upsun-cli/config.yaml`) or environment variables. For details, see the [customization instructions on GitHub](https://github.com/platformsh/legacy-cli#user-content-customization).

#### Automate repetitive tasks

You might want to use the CLI in a script to automate repetitive tasks such as synchronizing your files locally.
In such cases, you want to customize the CLI to bypass any confirmation questions.
You can set the answer to every question as `yes` using the `UPSUN_CLI_NO_INTERACTION` environment variable.

For instance, to locally sync every mount point for your app named `myapp`, you could use this command:

```bash
export PLATFORM_PROJECT=my-project;
export PLATFORM_BRANCH=main;
export UPSUN_CLI_NO_INTERACTION=1;
upsun mount:download --all --app app --target local-backup
```

### Autocomplete commands

The CLI provides tab autocompletion for commands, options, and some values (your projects, valid regions).
To enable autocompletion, follow this step:

Add the following to your shell’s startup (``.bashrc``, ``.zshrc``, or the equivalent):

```bash {}
eval $(upsun completion)
```

### Run commands on your container

You can use the Upsun CLI to run commands on your container.
You can use any command you've added in [dependencies](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#dependencies)
or a [hook](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#hooks).

The syntax looks like the following:

```bash
upsun ssh -- <COMMAND> <ARGUMENTS>
```

For example, to run a specific Python script named `my-script.py` on your current environment,
run the following command:

```bash
upsun ssh -- python my-script.py
```

Or to use [Drush](https://www.drush.org/latest/install/) to rebuild the cache on the `feature` environment,
run this command:

```bash
upsun ssh -e feature -- drush -y cache-rebuild
```

### Update the CLI

To update to the latest version, use the same tool as for [installation](#1-install):

```bash {}
$ scoop update upsun

```

## Upgrade from the legacy CLI

To upgrade from the legacy CLI, follow the [installation instructions](#1-install).
Once you've installed the latest version, the CLI guides you through removing the installed legacy CLI.

