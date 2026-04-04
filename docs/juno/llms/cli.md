# Source: https://juno.build/docs/reference/cli.md

# CLI

The Juno CLI provides a variety of tools for managing and deploying projects.

## Installing the Juno CLI

To download and install Juno CLI, run the following command:

```
npm i -g @junobuild/cli
```

---

## Commands

The following is a complete list of commands available in the Juno CLI.

**Tip:**

The CLI automatically runs in non-interactive mode if either a `JUNO_TOKEN` is set or the `--headless` argument is used.

The former is set when you set up a [GitHub Actions](/docs/guides/github-actions.md).

---

### Login

**Important:**

Authenticating your terminal saves sensitive information on your device. We recommend setting up a password to encrypt this file when prompted.

Generate an authentication for use in non-interactive environments.

```
Usage: juno login [options]Options:  -b, --browser         A particular browser to open. supported: chrome|firefox|edge.  -e, --emulator        Skips the Console UI and logs in your terminal with the emulator (â ï¸  local development only).  -m, --mode            Choose which environment to use (production, staging, development). Defaults to production if omitted.  -p, --profile         Specify an optional profile to use (e.g. personal, team). Useful when managing multiple Mission Controls.  -h, --help            Output usage information.
```

The authentication process requires a browser.

#### Reusing Access Key

If you've previously authenticated your terminal and decide to log in again, the CLI will prompt you about reusing your existing access key.

This allows you to reuse your authorization, especially when creating new modules like Satellites or Orbiters.

---

### Logout

**Caution:**

This action currently does not remove the controllers from Satellites and/or Mission Control and/or Orbiter. It only logs out your local machine by removing the locally saved key (principal).

Log out of the current device. â ï¸ This action does not remove the access keys from the module.

```
Usage: juno logout [options]Options:  -h, --help            Output usage information.
```

---

### Hosting

Deploy or clear the frontend code of your app on your satellite.

```
Usage: juno hosting <subcommand> [options]Subcommands:  clear               Remove frontend files (JS, HTML, CSS, etc.) from your satellite.  deploy              Deploy your app to your satellite.
```

---

#### Clear

Remove frontend files (JS, HTML, CSS, etc.) from your satellite.

```
Usage: juno hosting clear [options]Options:  -f, --fullPath        Clear a particular file of your app.  -m, --mode            Choose which environment to use (production, staging, development). Defaults to production if omitted.  -p, --profile         Specify an optional profile to use (e.g. personal, team). Useful when managing multiple Mission Controls.  --container-url       Override a custom container URL. If not provided, defaults to production or the local container in development mode.  --console-url         Specify a custom URL to access the developer Console.  -h, --help            Output usage information.
```

**Note:**

This command removes existing files from the Satellite and only affects the app assets, your frontend. Your user's uploaded files will not be cleared from your custom collections in the storage.

---

#### Deploy

Deploy your app to your satellite.

```
Usage: juno hosting deploy [options]Options:  --batch               Number of files to upload in parallel per batch (default: 50).  --clear               Clear existing app files before proceeding with deployment.  --config              Apply configuration after deployment succeeds.  --no-apply            Submit the deployment as a change but do not apply it yet.  -k, --keep-staged     Keep staged assets in memory after applying the change.  -i, --immediate       Deploy files instantly (bypasses the change workflow).  -m, --mode            Choose which environment to use (production, staging, development). Defaults to production if omitted.  -p, --profile         Specify an optional profile to use (e.g. personal, team). Useful when managing multiple Mission Controls.  --container-url       Override a custom container URL. If not provided, defaults to production or the local container in development mode.  --console-url         Specify a custom URL to access the developer Console.  -h, --help            Output usage information.Notes:- The option --keep-staged only applies when --no-apply is NOT used (i.e. the change is applied immediately).
```

---

### Config

Manage your project configuration

```
Usage: juno config <subcommand> [options]Subcommands:  apply               Apply configuration to satellite.  init                Set up your project by creating a config file.
```

---

#### Apply

Apply configuration to satellite.

```
Usage: juno config apply [options]Options:  --force               Overwrite configuration without checks.  -m, --mode            Choose which environment to use (production, staging, development). Defaults to production if omitted.  -p, --profile         Specify an optional profile to use (e.g. personal, team). Useful when managing multiple Mission Controls.  --container-url       Override a custom container URL. If not provided, defaults to production or the local container in development mode.  --console-url         Specify a custom URL to access the developer Console.  -h, --help            Output usage information.
```

---

#### Init

Set up your project by creating a config file.

```
Usage: juno config init [options]Options:  --minimal             Skip few prompts and generate a config file with a placeholder satellite ID.  -m, --mode            Choose which environment to use (production, staging, development). Defaults to production if omitted.  -p, --profile         Specify an optional profile to use (e.g. personal, team). Useful when managing multiple Mission Controls.  --container-url       Override a custom container URL. If not provided, defaults to production or the local container in development mode.  --console-url         Specify a custom URL to access the developer Console.  -h, --help            Output usage information.
```

The `juno config init` command creates a `juno.config` file in the root directory of your project.

Depending on your project, it will either create a TypeScript, JavaScript, or JSON file.

**Tip:**

We recommend using the first two options because they can leverage your IDE's IntelliSense with type hints.

This file is necessary for deploying, configuring, or running any other CLI commands for your app.

Read more about the [configuration](/docs/reference/configuration.md).

---

### Snapshot

Handle snapshot-related tasks.

```
Usage: juno snapshot <subcommand> [options]Subcommands:  create               Create a snapshot of your current state.  delete               Delete an existing snapshot.  download             Download a snapshot to offline files.  list                 List the existing snapshot.  upload               Upload a snapshot from offline files.  restore              Restore a previously created snapshot.Options:  -t, --target          Which module type should be snapshotted? Valid targets are satellite, mission-control or orbiter.  -m, --mode            Choose which environment to use (production, staging, development). Defaults to production if omitted.  -p, --profile         Specify an optional profile to use (e.g. personal, team). Useful when managing multiple Mission Controls.  --container-url       Override a custom container URL. If not provided, defaults to production or the local container in development mode.  --console-url         Specify a custom URL to access the developer Console.  -h, --help            Output usage information.Notes:- Targets can be shortened to s for satellite, m for mission-control and o for orbiter.
```

---

#### Upload

Upload a snapshot from offline files.

```
Usage: juno snapshot upload [options]Options:  --dir                 Path to the snapshot directory that contains the metadata.json and chunks.  -t, --target          Which module type should be snapshotted? Valid targets are satellite, mission-control or orbiter.  --target-id           The module ID of a specific target to upload the snapshot to.  -m, --mode            Choose which environment to use (production, staging, development). Defaults to production if omitted.  -p, --profile         Specify an optional profile to use (e.g. personal, team). Useful when managing multiple Mission Controls.  --container-url       Override a custom container URL. If not provided, defaults to production or the local container in development mode.  --console-url         Specify a custom URL to access the developer Console.  -h, --help            Output usage information.Notes:- Targets can be shortened to s for satellite, m for mission-control and o for orbiter.
```

---

### Stop

Stop a module.

```
Usage: juno stop [options]Options:  -t, --target          Which module type should be stopped? Valid targets are satellite, mission-control or orbiter.  -m, --mode            Choose which environment to use (production, staging, development). Defaults to production if omitted.  -p, --profile         Specify an optional profile to use (e.g. personal, team). Useful when managing multiple Mission Controls.  --container-url       Override a custom container URL. If not provided, defaults to production or the local container in development mode.  --console-url         Specify a custom URL to access the developer Console.  -h, --help            Output usage information.Notes:- Targets can be shortened to s for satellite, m for mission-control and o for orbiter.
```

---

### Start

Start a module.

```
Usage: juno start [options]Options:  -t, --target          Which module type should be started? Valid targets are satellite, mission-control or orbiter.  -m, --mode            Choose which environment to use (production, staging, development). Defaults to production if omitted.  -p, --profile         Specify an optional profile to use (e.g. personal, team). Useful when managing multiple Mission Controls.  --container-url       Override a custom container URL. If not provided, defaults to production or the local container in development mode.  --console-url         Specify a custom URL to access the developer Console.  -h, --help            Output usage information.Notes:- Targets can be shortened to s for satellite, m for mission-control and o for orbiter.
```

---

### Upgrade

Upgrade a module to a new version.

```
Usage: juno upgrade [options]Options:  -t, --target          Which module type should be upgraded? Valid targets are satellite, mission-control or orbiter.  -s, --src             A path to a specific local gzipped WASM file to publish.  --clear-chunks        Clear any previously uploaded WASM chunks (applies if the WASM size is greater than 2MB).  --no-snapshot         Skip creating a snapshot before upgrading.  -r, --reset           Reset to the initial state.  -m, --mode            Choose which environment to use (production, staging, development). Defaults to production if omitted.  -p, --profile         Specify an optional profile to use (e.g. personal, team). Useful when managing multiple Mission Controls.  --container-url       Override a custom container URL. If not provided, defaults to production or the local container in development mode.  --console-url         Specify a custom URL to access the developer Console.  -h, --help            Output usage information.Notes:- Resetting a mission control is not possible.- Targets can be shortened to s for satellite, m for mission-control and o for orbiter.
```

**Important:**

*   We recommend that you stay current with the Juno releases, as some features may not perform correctly in the [console](/docs/terminology.md#console) if your modules are outdated.
*   Upgrading requires a stable internet connection for a successful process.

The CLI automatically runs in non-interactive mode if either a JUNO\_TOKEN is set or the --headless argument is used.

---

### Changes

Review and apply changes submitted to your module.

```
Usage: juno changes <subcommand> [options]Subcommands:  apply               Apply a submitted change.  list                List all submitted or applied changes.  reject              Reject a change.
```

---

#### Apply

Apply a submitted change.

```
Usage: juno changes apply [options]Options:  -i, --id              The ID of the change to apply.  --snapshot            Create a snapshot before applying.  --hash                The expected hash of all included changes (for verification).  -k, --keep-staged     Keep staged assets in memory after applying the change.  -h, --help            Output usage information.
```

---

#### List

List all submitted or applied changes.

```
Usage: juno changes list [options]Options:  -a, --all           Search through all changes, not just the 100 most recent.  -e, --every         Include changes of any status (default is only submitted ones).  -h, --help          Output usage information.
```

---

#### Reject

Reject a change.

```
Usage: juno changes reject [options]Options:  -i, --id              The ID of the change to reject.  --hash                The expected hash of all included changes (for verification).  -k, --keep-staged     Keep staged assets in memory after applying the change.  -h, --help            Output usage information.
```

---

### Emulator

Handle tasks related to the emulator like starting/stopping a local network.

```
Usage: juno emulator <subcommand> [options]Subcommands:  start               Start the emulator for local development.  stop                Stop the local network.  wait                Wait until the emulator is ready.
```

---

#### Start

Start the emulator for local development.

```
Usage: juno emulator start [options]Options:  -l, --lang            Specify the language for building the serverless functions: rust, typescript or javascript.  --cargo-path          Path to the Rust manifest.  --source-path         Optional path to the TypeScript or JavaScript entry file.  -w, --watch           Rebuild your functions automatically when source files change.  -h, --help            Output usage information.Notes:- The language and path options are only used in combination with watch.- If no language is provided, the CLI attempts to determine the appropriate build.- Language can be shortened to rs for Rust, ts for TypeScript and mjs for JavaScript.- Use --cargo-path to specify a specific crate path. For Rust builds, this maps to --manifest-path for cargo build. For TypeScript and JavaScript, it points to the Rust crate (commonly "Sputnik") that imports the functions.- An optional --source-path to specify the source file for TypeScript and JavaScript (e.g. index.ts or index.mjs).- The watch option rebuilds when source files change, with a default debounce delay of 10 seconds; optionally, pass a delay in milliseconds.
```

---

#### Wait

Wait until the emulator is ready.

```
Usage: juno dev wait [options]Options:  -t, --timeout         Timeout for the emulator to be ready (in ms, default 2min).  -h, --help            Output usage information.
```

---

### Functions

Build and upgrade your satellite's serverless functions.

```
Usage: juno functions <subcommand> [options]Subcommands:  build                Build your functions.  eject                Scaffold the necessary files for developing your serverless functions.  init                 Alias for eject.  publish              Publish a new version of your functions.  upgrade              Upgrade your satellite's serverless functions.Notes:- The local server supports live reloading.- You can use fn as a shortcut for functions.
```

---

#### Build

Build your serverless functions.

```
Usage: juno functions build [options]Options:  -l, --lang            Specify the language for building the serverless functions: rust, typescript or javascript.  --cargo-path          Path to the Rust manifest.  --source-path         Optional path to the TypeScript or JavaScript entry file.  -w, --watch           Rebuild your functions automatically when source files change.  -h, --help            Output usage information.Notes:- If no language is provided, the CLI attempts to determine the appropriate build.- Language can be shortened to rs for Rust, ts for TypeScript and mjs for JavaScript.- Use --cargo-path to specify a specific crate path. For Rust builds, this maps to --manifest-path for cargo build. For TypeScript and JavaScript, it points to the Rust crate (commonly "Sputnik") that imports the functions.- An optional --source-path to specify the source file for TypeScript and JavaScript (e.g. index.ts or index.mjs).- The watch option rebuilds when source files change, with a default debounce delay of 10 seconds; optionally, pass a delay in milliseconds.
```

---

#### Eject

Generate the required files to begin developing serverless functions in your project.

```
Usage: juno functions eject [options]Options:  -l, --lang            Specify the language for building the serverless functions: rust, typescript or javascript.  -h, --help            Output usage information.Notes:- Language can be shortened to rs for Rust, ts for TypeScript and mjs for JavaScript.
```

---

#### Publish

Publish a new version of your serverless functions.

```
Usage: juno functions publish [options]Options:  --no-apply            Submit the release as a change but do not apply it yet.  -k, --keep-staged     Keep staged assets in memory after applying the change.  -s, --src             A path to a specific local gzipped WASM file to publish.  -m, --mode            Choose which environment to use (production, staging, development). Defaults to production if omitted.  -p, --profile         Specify an optional profile to use (e.g. personal, team). Useful when managing multiple Mission Controls.  --container-url       Override a custom container URL. If not provided, defaults to production or the local container in development mode.  --console-url         Specify a custom URL to access the developer Console.  -h, --help            Output usage information.Notes:- The option --keep-staged only applies when --no-apply is NOT used (i.e. the change is applied immediately).
```

---

#### Upgrade

Upgrade your serverless functions.

```
Usage: juno functions upgrade [options]Options:  --cdn                 Select a previously published WASM file from the CDN (interactive).  --cdn-path            Use a specific published WASM file from the CDN.  -s, --src             A path to a specific local gzipped WASM file to publish.  --clear-chunks        Clear any previously uploaded WASM chunks (applies if the WASM size is greater than 2MB).  --no-snapshot         Skip creating a snapshot before upgrading.  -r, --reset           Reset to the initial state.  -m, --mode            Choose which environment to use (production, staging, development). Defaults to production if omitted.  -p, --profile         Specify an optional profile to use (e.g. personal, team). Useful when managing multiple Mission Controls.  --container-url       Override a custom container URL. If not provided, defaults to production or the local container in development mode.  --console-url         Specify a custom URL to access the developer Console.  -h, --help            Output usage information.Notes:- If no option is provided, the default local build output will be used.- If --src is specified, it takes precedence over any CDN options.- Use --cdn to interactively select from recent published releases.
```

---

### Run

Run a custom script in the CLI context.

```
Usage: juno run [options]Options:  -s, --src             The path to your JavaScript or TypeScript script.  -m, --mode            Choose which environment to use (production, staging, development). Defaults to production if omitted.  -p, --profile         Specify an optional profile to use (e.g. personal, team). Useful when managing multiple Mission Controls.  --container-url       Override a custom container URL. If not provided, defaults to production or the local container in development mode.  -h, --help            Output usage information.
```

---

### Open

Open your satellite in your browser.

```
Usage: juno open [options]Options:  -b, --browser         A particular browser to open. supported: chrome|firefox|edge.  -c, --console         Open satellite in the console.  -m, --mode            Choose which environment to use (production, staging, development). Defaults to production if omitted.  -p, --profile         Specify an optional profile to use (e.g. personal, team). Useful when managing multiple Mission Controls.  --container-url       Override a custom container URL. If not provided, defaults to production or the local container in development mode.  --console-url         Specify a custom URL to access the developer Console.  -h, --help            Output usage information.
```

---

### Status

Check the status of the modules.

```
Usage: juno status [options]Options:  -m, --mode            Choose which environment to use (production, staging, development). Defaults to production if omitted.  -p, --profile         Specify an optional profile to use (e.g. personal, team). Useful when managing multiple Mission Controls.  --container-url       Override a custom container URL. If not provided, defaults to production or the local container in development mode.  --console-url         Specify a custom URL to access the developer Console.  -h, --help            Output usage information.
```

---

### Version

Check the version of the CLI.

```
Usage: juno version [options]Options:  -h, --help            Output usage information.
```

---

### Who am I?

Display your current profile, access key, and links to your satellite.

```
Usage: juno whoami [options]Options:  -h, --help            Output usage information.  -m, --mode            Choose which environment to use (production, staging, development). Defaults to production if omitted.  -p, --profile         Specify an optional profile to use (e.g. personal, team). Useful when managing multiple Mission Controls.  --container-url       Override a custom container URL. If not provided, defaults to production or the local container in development mode.  --console-url         Specify a custom URL to access the developer Console.
```

---

## Environment

Some CLI flags affect the context of your commands, such as which environment you're working in or which identity you're using. These flags are global and apply to most commands.

---

### Mode

The `--mode` flag lets you target a specific environment when executing CLI commands. This is useful for working across development, staging, and production setups.

```
juno login --mode developmentjuno hosting deploy --mode staging
```

The value for `--mode` can be any string. If omitted, it defaults to production.

**Important:**

The `development` value is reserved. When you use `--mode development`, the tooling automatically understands that you are working with the local emulator.

---

### Profile

The optional `--profile` flag lets you switch between different identities. Useful when working with multiple Mission Controls.

```
juno login --profile teamjuno hosting deploy --profile team --mode staging
```

It accepts any string. If omitted, no profile is used.

---

### Local Persistence

Unless you run it in headless mode with a token, the Juno CLI stores data locally in the following OS-specific user's variables path to work properly.

| OS  | Path |
| --- | --- |
| Mac | `~/Library/Preferences/juno-nodejs` |
| Windows | `%APPDATA%\juno-nodejs\Config` (for example, `C:\Users\USERNAME\AppData\Roaming\juno-nodejs\Config`) |
| Linux | `~/.config/juno-nodejs` (or `$XDG_CONFIG_HOME/juno-nodejs`) |

These config files are created based on the selected `--profile` and `--mode`:

| File | Encrypted | Purpose |
| --- | --- | --- |
| `juno[-profile][-mode]` | â   | Stores the [access key](/docs/miscellaneous/access-keys.md) ([principal](/docs/terminology.md#principal)) and list of modules. |
| `juno[-profile][-mode]-cli-settings` |     | Stores CLI preferences, e.g. whether the access key file is encrypted (to avoid unnecessary prompts). |
| `juno[-profile][-mode]-cli-state` |     | Stores ephemeral state like applied config hashes. |