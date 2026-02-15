# wp cli info

**Source:** [https://developer.wordpress.org/cli/commands/cli/info/](https://developer.wordpress.org/cli/commands/cli/info/)

# wp cli info

Prints various details about the WP-CLI environment.

## In this article

Table of Contents- Options
- Examples
- Global Parameters

↑Back to top

[View Open Issues(2)](https://github.com/login?return_to=%2Fissues%3Fq%3Dlabel%3Acommand%3Acli-info+sort%3Aupdated-desc+org%3Awp-cli+is%3Aopen)
[View Closed Issues(16)](https://github.com/login?return_to=%2Fissues%3Fq%3Dlabel%3Acommand%3Acli-info+sort%3Aupdated-desc+org%3Awp-cli+is%3Aclosed)
[Create New Issue](https://github.com/wp-cli/wp-cli/issues/new)
This command runs on the `before_wp_load` hook, just before the WP load process begins.

Helpful for diagnostic purposes, this command shares:

- OS information.
- Shell information.
- PHP binary used.
- PHP binary version.
- php.ini configuration file used (which is typically different than web).
- WP-CLI root dir: where WP-CLI is installed (if non-Phar install).
- WP-CLI global config: where the global config YAML file is located.
- WP-CLI project config: where the project config YAML file is located.
- WP-CLI version: currently installed version.

See [config docs](https://make.wordpress.org/cli/handbook/references/config/) for more details on global and project config YAML files.

### Options

See the [argument syntax](https://make.wordpress.org/cli/handbook/references/argument-syntax/) reference for a detailed explanation of the syntax conventions used.

[--format=<format>]
Render output in a particular format.

—
default: list

options:

– list

– json
—

### Examples

```text
# Display various data about the CLI environment.
$ wp cli info
OS:  Linux 4.10.0-42-generic #46~16.04.1-Ubuntu SMP Mon Dec 4 15:57:59 UTC 2017 x86_64
Shell:   /usr/bin/zsh
PHP binary:  /usr/bin/php
PHP version: 7.1.12-1+ubuntu16.04.1+deb.sury.org+1
php.ini used:    /etc/php/7.1/cli/php.ini
WP-CLI root dir:    phar://wp-cli.phar
WP-CLI packages dir:    /home/person/.wp-cli/packages/
WP-CLI global config:
WP-CLI project config:
WP-CLI version: 1.5.0

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

