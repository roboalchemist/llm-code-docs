# wp cli update

**Source:** [https://developer.wordpress.org/cli/commands/cli/update/](https://developer.wordpress.org/cli/commands/cli/update/)

# wp cli update

Updates WP-CLI to the latest release.

## In this article

Table of Contents- Options
- Examples
- Global Parameters

↑Back to top

[View Open Issues(3)](https://github.com/login?return_to=%2Fissues%3Fq%3Dlabel%3Acommand%3Acli-update+sort%3Aupdated-desc+org%3Awp-cli+is%3Aopen)
[View Closed Issues(30)](https://github.com/login?return_to=%2Fissues%3Fq%3Dlabel%3Acommand%3Acli-update+sort%3Aupdated-desc+org%3Awp-cli+is%3Aclosed)
[Create New Issue](https://github.com/wp-cli/wp-cli/issues/new)
This command runs on the `before_wp_load` hook, just before the WP load process begins.

Default behavior is to check the releases API for the newest stable version, and prompt if one is available.

Use `--stable` to install or reinstall the latest stable version.

Use `--nightly` to install the latest built version of the master branch. While not recommended for production, nightly contains the latest and greatest, and should be stable enough for development and staging environments.

Only works for the Phar installation mechanism.

### Options

See the [argument syntax](https://make.wordpress.org/cli/handbook/references/argument-syntax/) reference for a detailed explanation of the syntax conventions used.

[--patch]
Only perform patch updates.
[--minor]
Only perform minor updates.
[--major]
Only perform major updates.
[--stable]
Update to the latest stable release. Skips update check.
[--nightly]
Update to the latest built version of the master branch. Potentially unstable.
[--yes]
Do not prompt for confirmation.
[--insecure]
Retry without certificate validation if TLS handshake fails. Note: This makes the request vulnerable to a MITM attack.

### Examples

```text
# Update CLI.
$ wp cli update
You are currently using WP-CLI version 0.24.0. Would you like to update to 0.24.1? [y/n] y
Downloading from https://github.com/wp-cli/wp-cli/releases/download/v0.24.1/wp-cli-0.24.1.phar...
New version works. Proceeding to replace.
Success: Updated WP-CLI to 0.24.1.

```text

### Global Parameters

These [global parameters](https://make.wordpress.org/cli/handbook/config/) have the same behavior across all commands and affect how WP-CLI interacts with WordPress.

**Argument**
**Description**

`--path=<path>`
Path to the WordPress files.

`--url=<url>`
Pretend request came from given URL. In multisite, this argument is how the target site is specified.

`--ssh=[<scheme>:][<user>@]<host\|container>[:<port>][<path>]`
Perform operation against a remote server over SSH (or a container using scheme of “docker”, “docker-compose”, “docker-compose-run”, “vagrant”).

`--http=<http>`
Perform operation against a remote WordPress installation over HTTP.

`--user=<id\|login\|email>`
Set the WordPress user.

`--skip-plugins[=<plugins>]`
Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded.

`--skip-themes[=<themes>]`
Skip loading all themes, or a comma-separated list of themes.

`--skip-packages`
Skip loading all installed packages.

`--require=<path>`
Load PHP file before running the command (may be used more than once).

`--exec=<php-code>`
Execute PHP code before running the command (may be used more than once).

`--context=<context>`
Load WordPress in a given context.

`--[no-]color`
Whether to colorize the output.

`--debug[=<group>]`
Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap, commandfactory, and help.

`--prompt[=<assoc>]`
Prompt the user to enter values for all command arguments, or a subset specified as comma-separated values.

`--quiet`
Suppress informational messages.

Command documentation is regenerated at every release. To add or update an example, please submit a pull request against the corresponding part of the codebase.

