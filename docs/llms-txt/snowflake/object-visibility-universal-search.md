# Source: https://docs.snowflake.com/en/user-guide/ui-snowsight/object-visibility-universal-search.md

# Make database objects discoverable in Universal Search

Universal Search helps you discover database objects in the account. By default, you can only discover objects to which you have already been
granted access. Even if you have access to multiple accounts within your Snowflake organization, you aren’t able to see objects outside
of the account you’re signed into because access grants do not cross accounts.

Administrators can enable users to discover objects to which they don’t yet have access, including objects in other accounts within your Snowflake
organization, by managing object visibility.

> **Note:**
>
> You can [associate objects with contact information](../contacts-using.md) so that if a user performs a search and doesn’t have
> the privilege to access an object, they can select Request Access to see contact information.

## OBJECT_VISIBILITY property

The OBJECT_VISIBILITY property controls the discoverability of objects in the account, enabling users without explicit access privileges to
find objects and request access. Expanding visibility of objects in the account can simplify collaboration and streamline access requests.

OBJECT_VISIBILITY can be set on an account, database, or schema and follows Snowflake’s inheritance model: settings at a higher level (for
example, accounts) automatically apply to lower levels (for example, databases) unless overridden.

You can set OBJECT_VISIBILITY to one of the following values:

* A YAML specification describing the visibility in one of the following formats:

  ```sqlexample-yaml
  $$
  organization_targets:
    - all_accounts_including_external
  $$
  ```

  Or

  ```sqlexample-yaml
  $$
  organization_targets:
    - account: <account_name_1>
    - account: <account_name_2>
    - ...
    - organization_user_group: <org_user_group_1>
    - organization_user_group: <org_user_group_2>
  $$
  ```

  In the syntax above:

  * `all_accounts_including_external`: Specifies that all users in all accounts in the organization can see the object. This includes
    all accounts within the organization, even those to which external parties may have been given access, such as
    [reader accounts](../data-sharing-reader-create.md).
  * `account: account_name`: Specifies that all users in the specified account can see the object. You can specify multiple accounts.
    Note that `account` is the account name, not the account locator. You must specify only the account name, excluding the organization name.09-22
  * `organization_user_group: org_user_group`: Specifies that the specified [organization user group](../organization-users.md) can
    see the object in all accounts in the organization where the [organization user group has been imported](../organization-users.md).
* `PRIVILEGED`: Specifies that only roles within the current account that are granted an explicit privilege on the object can see the object.
  This is the default behavior in Snowflake.

You can revert an object to PRIVILEGED visibility at any time.

For specific syntax, usage notes, and examples, see the following topics:

### CREATE commands

* [CREATE DATABASE](../../sql-reference/sql/create-database.md)
* [CREATE SCHEMA](../../sql-reference/sql/create-schema.md)

### ALTER commands

* [ALTER ACCOUNT](../../sql-reference/sql/alter-account.md)
* [ALTER DATABASE](../../sql-reference/sql/alter-database.md)
* [ALTER SCHEMA](../../sql-reference/sql/alter-schema.md)

## Access control requirements

Roles using this property must have the following privileges at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| MANAGE VISIBILITY | Account | Only the SECURITYADMIN role has this privilege by default. The privilege can be granted to additional roles as needed. |
| OWNERSHIP | Database or schema | Required to execute an [ALTER DATABASE](../../sql-reference/sql/alter-database.md) or [ALTER SCHEMA](../../sql-reference/sql/alter-schema.md) statement to set object visibility. OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](../../sql-reference/sql/grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../security-access-control-overview.md), see [Overview of Access Control](../security-access-control-overview.md).

## Examples

### Making a database broadly visible

The following statement makes the `product_analytics` database visible to all users in the current account (ACME_ENGINEERING):

```sqlexample-yaml
ALTER DATABASE product_analytics
SET OBJECT_VISIBILITY =
$$
organization_targets:
  - account: acme_engineering
$$;
```

The following statement makes the database visible to all users in two additional accounts within the organization (ACME_MARKETING and ACME_SALES):

```sqlexample-yaml
ALTER DATABASE product_analytics
SET OBJECT_VISIBILITY =
$$
organization_targets:
  - account: acme_engineering
  - account: acme_marketing
  - account: acme_sales
$$;
```

The following statement makes the database visible to all users in all accounts within the ACME organization:

```sqlexample-yaml
ALTER DATABASE product_analytics
SET OBJECT_VISIBILITY =
$$
organization_targets:
  - all_accounts_including_external
$$;
```

### Making a database visible to specific organization user groups

The following statement makes the database visible to specific organization user groups in all accounts within the ACME organization where the
[organization user group has been imported](../organization-users.md):

```sqlexample-yaml
ALTER DATABASE product_analytics
SET OBJECT_VISIBILITY =
$$
organization_targets:
  - organization_user_group: engineering
  - organization_user_group: marketing
  - organization_user_group: sales
$$;
```

## Limitations

* Objects that are discoverable and not accessible are only displayed in [Universal Search](../ui-snowsight-universal-search.md).
  They are not visible in the [database object explorer](../ui-snowsight-data.md) or SQL commands that show metadata (SHOW commands, etc.).
* For a schema, you can set the OBJECT_VISIBILITY property to PRIVILEGED to override any broader visibility settings that may be inherited
  from the account or database level, ensuring the schema remains accessible only by the owner.
* The OBJECT_VISIBILITY property cannot be set or overridden below the schema level. At the schema level, users can either see all objects or none.
* Search can take a few hours to reflect changes to object visibility.
