# Source: https://docs.infrahub.app/release-notes/infrahub/release-0_9.md

| Release Number   | 0.9.0                                                    |
| ---------------- | -------------------------------------------------------- |
| Release Date     | Dec 20, 2023                                             |
| Release Codename | Alpha #3                                                 |
| URL              | <https://github.com/opsmill/infrahub/releases/tag/0.9.0> |

# Release 0.9.0 - Alpha #3

## Main Changes[​](#main-changes "Direct link to Main Changes")

Ability to run checks on a proposed change based on a target group With this change any check you define in an external Git repository can be tied to a group. This enables you to run the same check across all members of a group. For instance a custom check that gets executed on for all devices.

# Upsert mutations

The upsert mutations allows you to update or create a resource with a single mutation. It can be useful if you are not sure if an object exists and you want to either update or create the object.

## Add new attribute type: Dropdown[​](#add-new-attribute-type-dropdown "Direct link to Add new attribute type: Dropdown")

The dropdown works in the same way as an enum with the difference that the dropdown also supports assigning a color and description to make them stand out more. The description is visible when choosing the options, and the color will be displayed in the different views.

## Add mutations and ability to add or remove enums and dropdowns as a user[​](#add-mutations-and-ability-to-add-or-remove-enums-and-dropdowns-as-a-user "Direct link to Add mutations and ability to add or remove enums and dropdowns as a user")

A user can now add or remove enum and dropdown attribute choices using a mutation or the frontend.

## Add new storage options[​](#add-new-storage-options "Direct link to Add new storage options")

With the redesigned storage engine it's now possible to store artefacts in AWS S3 (or S3 compatible) aside from the local storage on disk.

## Extend IPHost and IPNetwork types[​](#extend-iphost-and-ipnetwork-types "Direct link to Extend IPHost and IPNetwork types")

Instead of just returning the ip interface (i.e., 172.16.1.1/24) or the ip network (i.e., 172.16.1.0/24) Infrahub now exposes additional options aside from value so you can query for ip, prefix\_len, netmask etc. This should simplify some tasks when creating Jinja templates or Transforms.

## Add markdown editor for textarea fields[​](#add-markdown-editor-for-textarea-fields "Direct link to Add markdown editor for textarea fields")

A markdown editor has been added and will be used for all textarea type fields, and for comments in the proposed changes.
