# Source: https://docs.infrahub.app/release-notes/infrahub/release-1_2_4.md

| Release Number   | 1.2.4                                                                               |
| ---------------- | ----------------------------------------------------------------------------------- |
| Release Date     | April 4th, 2025                                                                     |
| Release Codename | Chicago, Patch #4                                                                   |
| Tag              | [infrahub-v1.2.4](https://github.com/opsmill/infrahub/releases/tag/infrahub-v1.2.4) |

# Release 1.2.4

This release brings some changes and bug-fixes to resolve issues found in Infrahub v1.2.3 and prior.

## Main changes[​](#main-changes "Direct link to Main changes")

The complete list of changes can always be found in the `CHANGELOG.md` file in the Infrahub Git repository.

### Fixed[​](#fixed "Direct link to Fixed")

* Fixed the migration to remove an attribute from a schema to correctly ignore overridden attributes from a generic schema. ([#6073](https://github.com/opsmill/infrahub/issues/6073))

* Fixed an issue where HFID and uniqueness constraints for component templates would end up having duplicate elements after loading several schemas.

* Fixed an issue where optional unique attributes having a NULL value could be duplicated. Upgrading Infrahub to a version containing this fix will perform a check identifying such duplicates. If some duplicates are found, data or schema should be fixed in order to complete the upgrade:

  <!-- -->

  * Either the uniqueness constraint on corresponding attributes should be removed within schema.
  * Or duplicated unique attributes values should be modified.

* Properly clear references to old branches and schema objects from the registry when deleting branches.

* Restricted event.related payload for CoreGraphQLQueryGroup events.

## Upgrade guide[​](#upgrade-guide "Direct link to Upgrade guide")

Please refer to the Upgrade Guide in the documentation for more information on how to upgrade your Infrahub instance.

[Upgrade Guide](/guides/upgrade.md)
