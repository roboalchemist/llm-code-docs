# Source: https://docs.snowflake.com/en/sql-reference/sql/create-organization-profile.md

# CREATE ORGANIZATION PROFILE

Create the organization profile that forms part of the Uniform Listing Locator (ULL)
used to publish organizational listings or query organizational listing information
without mounting the listing. To create an organization profile, you modify the
listing manifest and then move it to a stage where you can publish or unpublish it.

See also:
:   [ALTER ORGANIZATION PROFILE](alter-organization-profile.md), [DESCRIBE AVAILABLE ORGANIZATION PROFILE](desc-available-organization-profile.md), [DESCRIBE ORGANIZATION PROFILE](desc-organization-profile.md), [DROP ORGANIZATION PROFILE](drop-organization-profile.md), [SHOW AVAILABLE ORGANIZATION PROFILES](show-available-organization-profiles.md), [SHOW ORGANIZATION PROFILES](show-organization-profiles.md), [SHOW VERSIONS IN ORGANIZATION PROFILE](show-versions-in-organization-profile.md), [Organization profile manifest reference](../../user-guide/collaboration/organization-profiles/org-profile-manifest-reference.md).

## Syntax

```sqlsyntax
CREATE ORGANIZATION PROFILE [ IF NOT EXISTS ] <name>

CREATE ORGANIZATION PROFILE [ IF NOT EXISTS ] <name>
  AS '<yaml_manifest_string>'
  [ VERSION <version_alias_name> ]
  [ PUBLISH = { TRUE | FALSE } ]

CREATE ORGANIZATION PROFILE [ IF NOT EXISTS ] <name>
  FROM @<yaml_manifest_stage_location>
  [ VERSION <version_alias_name> ]
  [ PUBLISH = { TRUE | FALSE } ]
```

## Required parameters

`name`
:   String that specifies the identifier (name) for the organization profile. It must be unique within the current organization. The identifier must conform to Snowflake identifier requirements. See [Identifier requirements](../identifiers-syntax.md). Additionally, organization profile names can only contain uppercase characters or numbers, they must start with an uppercase character, and the name length cannot exceed 128 characters.

`AS 'yaml_manifest_string'`
:   Specifies the YAML manifest for the organization profile.
    For organizational listing profile manifest fields,
    see [Organization profile manifest reference](../../user-guide/collaboration/organization-profiles/org-profile-manifest-reference.md).

    Inline manifests are normally provided as dollar-quoted strings.
    For more information, see [Dollar-quoted string constants](../data-types-text.md).

`FROM @yaml_manifest_stage_location`
:   Specifies the external stage, internal stage, or Git repository clone YAML format manifest stage location.

## Optional parameters

`VERSION version_alias_name`
:   Optional. Specifies the unique version identifier for the version being added. If `VERSION version_name` isn’t specified, an alias isn’t created. If the identifier contains spaces, special characters, or mixed-case characters, the entire identifier must be enclosed in double quotes. Identifiers enclosed in double quotes are also case sensitive. The FIRST, LAST, DEFAULT or LIVE keywords are reserved as version shortcuts and can’t be used. The unique version identifier can’t start with “version$” and can’t contain slashes ( / ). For information about identifier syntax, see [Identifier requirements](../identifiers-syntax.md).

`PUBLISH = { TRUE | FALSE }`
:   Optional. Specifies how the organization profile should be published.

    If TRUE, the organization profile is published immediately.

    Default: FALSE.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| CREATE ORGANIZATION PROFILE | Account | Organization profiles can only be created from the organization account in an organization. The GLOBALORGADMIN role has been granted the CREATE ORGANIZATION PROFILE privilege. |

## Usage notes

* Organization profiles created using CREATE ORGANIZATION PROFILE are DRAFT until they are published.
* For usage examples of organization profile manifests, see [Manage organizational listings](../../user-guide/collaboration/listings/organizational/org-listing-manage.md).

## Examples

This example creates a database named OrgProfileDB, a stage named my_test_state_org_profile, and an organization profile with a title of MY_ORG_PROFILE. The `title` field represents the provider domain, and it’s shown under the Organization Listing and as a filter option under Providers in an Internal Marketplace.

```sqlexample-yaml
CREATE DATABASE OrgProfileDB;
CREATE STAGE my_test_stage_org_profile;
COPY INTO @my_test_stage_org_profile/manifest.yml
  FROM (
    SELECT $$
      title: "MY_ORG_PROFILE"
      description: "Profile for SE Business Unit"
      contact: "contact_name@myemail.com"
      approver_contact: "approver_name@email.com"
      allowed_publishers:
        access:
          - all_internal_accounts: "true"
      logo: "urn:icon:shieldlock:blue"
    $$
  )
  SINGLE = TRUE
  OVERWRITE = TRUE
  FILE_FORMAT = (
    COMPRESSION = NONE
    ESCAPE_UNENCLOSED_FIELD = NONE
  );
```

This example publishes an organization profile named MYPROFILENAME from the `my_test_stage_org_profile` stage.

```sqlexample
CREATE ORGANIZATION PROFILE MYPROFILENAME
 FROM @my_test_stage_org_profile
 PUBLISH=TRUE;
```
