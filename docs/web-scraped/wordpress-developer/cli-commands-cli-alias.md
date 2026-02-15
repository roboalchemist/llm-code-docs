# wp cli alias<command>

**Source:** [https://developer.wordpress.org/cli/commands/cli/alias/](https://developer.wordpress.org/cli/commands/cli/alias/)




# wp cli alias<command>

Retrieves, sets and updates aliases for WordPress Installations.




## In this article


Table of Contents- Examples
- Subcommands



↑Back to top






[View Open Issues(16)](https://github.com/login?return_to=%2Fissues%3Fq%3Dlabel%3Acommand%3Acli-alias+sort%3Aupdated-desc+org%3Awp-cli+is%3Aopen)
[View Closed Issues(20)](https://github.com/login?return_to=%2Fissues%3Fq%3Dlabel%3Acommand%3Acli-alias+sort%3Aupdated-desc+org%3Awp-cli+is%3Aclosed)
[Create New Issue](https://github.com/wp-cli/wp-cli/issues/new)
Unless overridden, these commands run on the `before_wp_load` hook, just before the WP load process begins.

Aliases are shorthand references to WordPress installs. For instance, `@dev` could refer to a development install and `@prod` could refer to a production install. This command gives you and option to add, update and delete, the registered aliases you have available.

### Examples


```
# List alias information.
$ wp cli alias list
list
---
@all: Run command against every registered alias.
@local:
  user: wpcli
  path: /Users/wpcli/sites/testsite

# Get alias information.
$ wp cli alias get @dev
ssh: dev@somedeve.env:12345/home/dev/

# Add alias.
$ wp cli alias add @prod --set-ssh=login@host --set-path=/path/to/wordpress/install/ --set-user=wpcli
Success: Added '@prod' alias.

# Update alias.
$ wp cli alias update @prod --set-user=newuser --set-path=/new/path/to/wordpress/install/
Success: Updated 'prod' alias.

# Delete alias.
$ wp cli alias delete @prod
Success: Deleted '@prod' alias.

```



### Subcommands

 NameDescription[wp cli alias add](https://developer.wordpress.org/cli/commands/cli/alias/add/)Creates an alias.


[wp cli alias delete](https://developer.wordpress.org/cli/commands/cli/alias/delete/)Deletes an alias.


[wp cli alias get](https://developer.wordpress.org/cli/commands/cli/alias/get/)Gets the value for an alias.


[wp cli alias is-group](https://developer.wordpress.org/cli/commands/cli/alias/is-group/)Check whether an alias is a group.


[wp cli alias list](https://developer.wordpress.org/cli/commands/cli/alias/list/)Lists available WP-CLI aliases.


[wp cli alias update](https://developer.wordpress.org/cli/commands/cli/alias/update/)Updates an alias.


 

Command documentation is regenerated at every release. To add or update an example, please submit a pull request against the corresponding part of the codebase.



