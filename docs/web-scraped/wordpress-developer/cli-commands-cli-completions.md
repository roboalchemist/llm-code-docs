# wp cli completions

**Source:** [https://developer.wordpress.org/cli/commands/cli/completions/](https://developer.wordpress.org/cli/commands/cli/completions/)

# wp cli completions

Generates tab completion strings.

## In this article

Table of Contents- Options
- Examples
- Global Parameters

↑Back to top

[View Open Issues(1)](https://github.com/login?return_to=%2Fissues%3Fq%3Dlabel%3Acommand%3Acli-completions+sort%3Aupdated-desc+org%3Awp-cli+is%3Aopen)
[View Closed Issues(5)](https://github.com/login?return_to=%2Fissues%3Fq%3Dlabel%3Acommand%3Acli-completions+sort%3Aupdated-desc+org%3Awp-cli+is%3Aclosed)
[Create New Issue](https://github.com/wp-cli/wp-cli/issues/new)
This command runs on the `before_wp_load` hook, just before the WP load process begins.

### Options

See the [argument syntax](https://make.wordpress.org/cli/handbook/references/argument-syntax/) reference for a detailed explanation of the syntax conventions used.

--line=<line>
The current command line to be executed.
--point=<point>
The index to the current cursor position relative to the beginning of the command.

### Examples

```text
# Generate tab completion strings.
$ wp cli completions --line='wp eva' --point=100
eval
eval-file

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

