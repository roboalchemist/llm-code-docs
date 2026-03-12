# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-application-package-release-channel.md

# ALTER APPLICATION PACKAGE … MODIFY RELEASE CHANNEL

Modifies the release channels defined for an existing application package. Use this command
to modify a release channel, change the version or patch assigned to a release channel, or
set the release directive for a release channel.

> **Note:**
>
> The syntax in this topic only applies to application packages that use release channels. For more information, see
> [Publish an app using release channels](../../developer-guide/native-apps/release-channels.md). To set the release directive
> for an application package that does not use release channels, see
> [ALTER APPLICATION PACKAGE … RELEASE DIRECTIVE](alter-application-package-release-directive.md).

See also:
:   [ALTER APPLICATION PACKAGE](alter-application-package.md) , [ALTER APPLICATION PACKAGE … VERSION](alter-application-package-version.md),
    [ALTER APPLICATION PACKAGE … RELEASE DIRECTIVE](alter-application-package-release-directive.md)
    [SHOW RELEASE DIRECTIVES](show-release-directives.md)

## Syntax

```sqlsyntax
ALTER APPLICATION PACKAGE <name>
  MODIFY RELEASE CHANNEL <release_channel>
  SET DEFAULT RELEASE DIRECTIVE
  VERSION = <version_identifier>
  PATCH = <patch_num>
  [ UPGRADE_AFTER = '<timestamp>' ]

ALTER APPLICATION PACKAGE <name>
  MODIFY RELEASE CHANNEL <release_channel>
  SET RELEASE DIRECTIVE <release_directive>
  ACCOUNTS = ( <organization_name>.<account_name> [ , <organization_name>.<account_name> , ... ] )
  VERSION = <version_identifier>
  PATCH = <patch_num>
  [ UPGRADE_AFTER = '<timestamp>' ]

ALTER APPLICATION PACKAGE <name>
 MODIFY RELEASE CHANNEL <release_channel>
 MODIFY RELEASE DIRECTIVE <release_directive>
 VERSION = <version_identifier>
 PATCH = <patch_num>
 [ UPGRADE_AFTER = '<timestamp>' ]

ALTER APPLICATION PACKAGE <name>
  MODIFY RELEASE CHANNEL <release_channel>
  UNSET RELEASE DIRECTIVE <release_directive>
```

## Parameters

`name`
:   Specifies the identifier for the application package. If the identifier contains spaces, special characters, or mixed-case characters, the entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive.

`MODIFY RELEASE CHANNEL release_channel`
:   Specifies the release channel that this release directive applies to. If not specified, the release directive applies to all release channels.

    The supported values are:

    * ALPHA
    * QA
    * DEFAULT

    For more information about release channels, see [Publish an app using release channels](../../developer-guide/native-apps/release-channels.md).

`VERSION = version_identifier` . `PATCH = patch_num`
:   Modifies the version and patch level of the specified custom release directive.

`SET`
:   Specifies one or more properties to set for the application package, separated by blank spaces, commas, or new lines. For more details
    about the properties you can set, see [CREATE APPLICATION](create-application.md).

    `DEFAULT RELEASE DIRECTIVE VERSION = version_identifier PATCH = patch_num`
    :   Sets the version and patch level of the application package that should be installed for consumers by default.

    `RELEASE DIRECTIVE release_directive` . `ACCOUNTS = ( organization_name.account_name [ , organization_name.account_name , ... ] )` . `VERSION = version_identifier` . `PATCH = patch_num`
    :   Creates a custom release directive for the specified accounts.

        Use the ACCOUNTS clause to specify the list of accounts that this release directive applies to.

        Use the VERSION and PATCH clauses to specify the version identifier and patch number to be installed for these accounts.

`UPGRADE_AFTER = 'timestamp'`
:   Specifies the date and time when the automated upgrade process begins. Consumers can manually
    upgrade an app to a new version or patch before this date.

    This value can be any valid date and time format.

`UNSET`
:   Specifies one or more properties and/or session parameters to unset for the application package, which resets them to the defaults.

    `UNSET RELEASE DIRECTIVE release_directive`
    :   Removes the specified custom release directive from the application package.

## Usage notes

* Modifying the release directive requires the OWNERSHIP privilege on the application or the global MANAGE VERSIONS privilege.
* If you do not specify the values for the optional properties, the command uses the values specified in the application
  manifest file.
* If you specify values for the properties in the command and in the application manifest file, the values specified in
  the command take precedence.

## Examples

The following example adds version `V1` to the default release channel:

```sqlexample
ALTER APPLICATION PACKAGE my_app_package
  MODIFY RELEASE CHANNEL DEFAULT
  ADD VERSION V1;
```

```output
+---------------------------------------------------------------------------------------------------------+
| status                                                                                                  |
|---------------------------------------------------------------------------------------------------------|
| Version V1 added to release channel DEFAULT in application package my_app_package                       |
+---------------------------------------------------------------------------------------------------------+
```

The following example modifies the default release directive of the default release channel to set the version to
`V1` and the patch to `0`:

```sqlexample
ALTER APPLICATION PACKAGE my_app_package
  MODIFY RELEASE CHANNEL DEFAULT
  SET DEFAULT RELEASE DIRECTIVE
  VERSION = V1
  PATCH=0;
```

```output
+---------------------------------------------------------------------------------------------------------+
| status                                                                                                  |
|---------------------------------------------------------------------------------------------------------|
| Version V1 added to release channel DEFAULT in application package my_app_package                       |
+---------------------------------------------------------------------------------------------------------+
```

```sqlexample
ALTER APPLICATION PACKAGE my_app_package
  MODIFY RELEASE CHANNEL ALPHA
  ADD ACCOUNTS=(PM.CONNECTORS);
```

```output
+---------------------------------------------------------------------------------------+---------+-------+
| status                                                                                | version | patch |
|---------------------------------------------------------------------------------------+---------+-------|
| TBD                                                                                   |         |       |
+---------------------------------------------------------------------------------------+---------+-------+
```
