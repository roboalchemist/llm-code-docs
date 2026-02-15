# wp cli cache<command>

**Source:** [https://developer.wordpress.org/cli/commands/cli/cache/](https://developer.wordpress.org/cli/commands/cli/cache/)

# wp cli cache<command>

Manages the internal WP-CLI cache,.

## In this article

Table of Contents- Examples
- Subcommands

↑Back to top

[View Open Issues(1)](https://github.com/login?return_to=%2Fissues%3Fq%3Dlabel%3Acommand%3Acli-cache+sort%3Aupdated-desc+org%3Awp-cli+is%3Aopen)
[View Closed Issues(4)](https://github.com/login?return_to=%2Fissues%3Fq%3Dlabel%3Acommand%3Acli-cache+sort%3Aupdated-desc+org%3Awp-cli+is%3Aclosed)
[Create New Issue](https://github.com/wp-cli/wp-cli/issues/new)
Unless overridden, these commands run on the `before_wp_load` hook, just before the WP load process begins.

### Examples

```text
# Remove all cached files.
$ wp cli cache clear
Success: Cache cleared.

# Remove all cached files except for the newest version of each one.
$ wp cli cache prune
Success: Cache pruned.

```text

### Subcommands

 NameDescription[wp cli cache clear](https://developer.wordpress.org/cli/commands/cli/cache/clear/)Clears the internal cache.

[wp cli cache prune](https://developer.wordpress.org/cli/commands/cli/cache/prune/)Prunes the internal cache.



Command documentation is regenerated at every release. To add or update an example, please submit a pull request against the corresponding part of the codebase.

