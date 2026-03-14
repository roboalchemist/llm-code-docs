# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-application-package-release-directive.md

# ALTER APPLICATION PACKAGE … RELEASE DIRECTIVE

Modifies the properties of an existing application package. Use this command to modify a release directive to a new version or patch.

> **Note:**
>
> The syntax described in this topic is only applicable to application packages that do not use release channels. To modify the release directive of an application package that uses release channels, see [ALTER APPLICATION PACKAGE … MODIFY RELEASE CHANNEL](alter-application-package-release-channel.md).

See also:
:   [ALTER APPLICATION PACKAGE](alter-application-package.md) , [ALTER APPLICATION PACKAGE … VERSION](alter-application-package-version.md)

## Syntax

```sqlsyntax
ALTER APPLICATION PACKAGE <name>
  MODIFY RELEASE DIRECTIVE <release_directive>
  VERSION = <version_identifier>
  PATCH = <patch_num>
  [ UPGRADE_AFTER = '<timestamp>' ]

ALTER APPLICATION PACKAGE <name>
  SET DEFAULT RELEASE DIRECTIVE
  VERSION = <version_identifier>
  PATCH = <patch_num>
  [ UPGRADE_AFTER = '<timestamp>' ]

ALTER APPLICATION PACKAGE <name>
  SET RELEASE DIRECTIVE <release_directive>
  ACCOUNTS = ( <organization_name>.<account_name> [ , <organization_name>.<account_name> , ... ] )
  VERSION = <version_identifier>
  PATCH = <patch_num>
  [ UPGRADE_AFTER = '<timestamp>' ]

ALTER APPLICATION PACKAGE <name> UNSET RELEASE DIRECTIVE <release_directive>
```

## Parameters

`name`
:   Specifies the identifier for the application package. If the identifier contains spaces, special characters, or mixed-case characters, the entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive.

`MODIFY RELEASE DIRECTIVE release_directive` . `VERSION = version_identifier` . `PATCH = patch_num`
:   Modifies the version and patch level of the specified custom release directive.

`SET`
:   Specifies one (or more) properties to set for the application package (separated by blank spaces, commas, or new lines). For more details
    about the properties you can set, see [CREATE APPLICATION](create-application.md).

    `DEFAULT RELEASE DIRECTIVE VERSION = version_identifier PATCH = patch_num`
    :   Sets the version and patch level of the application package that should be installed for consumers by default.

    `RELEASE DIRECTIVE release_directive` . `ACCOUNTS = ( organization_name.account_name [ , organization_name.account_name , ... ] )` . `VERSION = version_identifier` . `PATCH = patch_num`
    :   Creates a custom release directive for the specified accounts.

        Use the ACCOUNTS clause to specify the list of accounts to which this release directive applies.

        Use the VERSION and PATCH clauses to specify the version identifier and patch number to be installed for these accounts.

`UPGRADE_AFTER = 'timestamp'`
:   Specifies the date and time when the automated upgrade process begins. Consumers can manually
    upgrade an app to a new version or patch before this date.

    This value can be any valid date and time format.

`UNSET`
:   Specifies one (or more) properties and/or session parameters to unset for the application package, which resets them to the defaults.

    `UNSET RELEASE DIRECTIVE release_directive`
    :   Removes the specified custom release directive from the application package.

## Usage notes

* Modifying the release directive requires the OWNERSHIP privilege on the application or the global MANAGE VERSIONS privilege.
* If you do not specify the values for the optional properties, the command uses the values specified in the application manifest file.

  If you specify values for the properties in the command and in the application manifest file, the values specified in the command take
  precedence.
