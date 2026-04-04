# wp cli<command>

**Source:** [https://developer.wordpress.org/cli/](https://developer.wordpress.org/cli/)

# wp cli<command>

Reviews current WP-CLI info, checks for updates, or views defined aliases.

## In this article

Table of Contents- Examples
- Subcommands

↑Back to top

[View Open Issues(31)](https://github.com/login?return_to=%2Fissues%3Fq%3Dlabel%3Acommand%3Acli+sort%3Aupdated-desc+org%3Awp-cli+is%3Aopen)
[View Closed Issues(48)](https://github.com/login?return_to=%2Fissues%3Fq%3Dlabel%3Acommand%3Acli+sort%3Aupdated-desc+org%3Awp-cli+is%3Aclosed)
[Create New Issue](https://github.com/wp-cli/wp-cli/issues/new)
Unless overridden, these commands run on the `before_wp_load` hook, just before the WP load process begins.

### Examples

```text
# Display the version currently installed.
$ wp cli version
WP-CLI 0.24.1

# Check for updates to WP-CLI.
$ wp cli check-update
Success: WP-CLI is at the latest version.

# Update WP-CLI to the latest stable release.
$ wp cli update
You have version 0.24.0. Would you like to update to 0.24.1? [y/n] y
Downloading from https://github.com/wp-cli/wp-cli/releases/download/v0.24.1/wp-cli-0.24.1.phar...
New version works. Proceeding to replace.
Success: Updated WP-CLI to 0.24.1.

# Clear the internal WP-CLI cache.
$ wp cli cache clear
Success: Cache cleared.

```text

### Subcommands

 NameDescription[wp cli alias](https://developer.wordpress.org/cli/commands/cli/alias/)Retrieves, sets and updates aliases for WordPress Installations.

[wp cli cache](https://developer.wordpress.org/cli/commands/cli/cache/)Manages the internal WP-CLI cache,.

[wp cli check-update](https://developer.wordpress.org/cli/commands/cli/check-update/)Checks to see if there is a newer version of WP-CLI available.

[wp cli cmd-dump](https://developer.wordpress.org/cli/commands/cli/cmd-dump/)Dumps the list of installed commands, as JSON.

[wp cli completions](https://developer.wordpress.org/cli/commands/cli/completions/)Generates tab completion strings.

[wp cli has-command](https://developer.wordpress.org/cli/commands/cli/has-command/)Detects if a command exists

[wp cli info](https://developer.wordpress.org/cli/commands/cli/info/)Prints various details about the WP-CLI environment.

[wp cli param-dump](https://developer.wordpress.org/cli/commands/cli/param-dump/)Dumps the list of global parameters, as JSON or in var_export format.

[wp cli update](https://developer.wordpress.org/cli/commands/cli/update/)Updates WP-CLI to the latest release.

[wp cli version](https://developer.wordpress.org/cli/commands/cli/version/)Prints WP-CLI version.



Command documentation is regenerated at every release. To add or update an example, please submit a pull request against the corresponding part of the codebase.

