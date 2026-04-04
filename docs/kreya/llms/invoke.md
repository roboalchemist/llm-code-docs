# Source: https://kreya.app/docs/cli/commands/script/invoke.md

# Source: https://kreya.app/docs/cli/commands/operation/invoke.md

# Source: https://kreya.app/docs/cli/commands/collection/invoke.md

# collection invoke

Invokes (runs) a single collection or a set of collections

```
kreyac collection invoke [--scripting-timeout] [--relative-to] [--disable-scripts] [--test-report-junit] [Collections]
```

## Example[​](#example "Direct link to Example")

```
kreyac collection invoke my-collection.krcol
```

## Options[​](#options "Direct link to Options")

### scripting-timeout[​](#scripting-timeout "Direct link to scripting-timeout")

`--scripting-timeout`<br /><!-- -->Can also be set via the environment variable `KREYA_SCRIPTINGTIMEOUT`<br /><!-- -->Default: `20`

Timeout of operation scripts in seconds

### relative-to[​](#relative-to "Direct link to relative-to")

`--relative-to`

Default: `project`

Determines the base path for resolving relative paths and globs. Accepted values: `project`, `current-working-directory` (alias: `cwd`)

### disable-scripts[​](#disable-scripts "Direct link to disable-scripts")

`--disable-scripts`

Disable the scripts of all operations for this invocation

### test-report-junit[​](#test-report-junit "Direct link to test-report-junit")

`--test-report-junit`

Enables the JUnit test reporter and writes the JUnit report to the specified file

## Arguments[​](#arguments "Direct link to Arguments")

### Collections `required` `multiple`[​](#collections-required-multiple "Direct link to collections-required-multiple")

Paths of the collections to be invoked, these could be directories, .krcol files or globs (e.g. './my-service/\*\*'). Some shells expand globs automatically, so you should enclose them in quotes. Collections are invoked in alphabetical order.
