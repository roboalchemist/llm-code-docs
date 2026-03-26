# Source: https://docs.infrahub.app/ansible.md

# opsmill.infrahub Ansible collection

Collection version 1.8.0

## Collection overview[​](#collection-overview "Direct link to Collection overview")

The OpsMill Infrahub Ansible Collection provides is intend to help interact with Infrahub through Ansible.

This Ansible collection consists of a set of modules and plugins designed to work seamlessly with your existing infrastructure, enabling you to define and enforce the desired state of your infrastructure with ease.

## Guides[​](#guides "Direct link to Guides")

To begin using the OpsMill Infrahub Ansible Collection, please follow our step-by-step guides:

* **[Installation Guide](/ansible/guides/installation.md)**: Learn how to install the collection, including Python module and Ansible setup, as well as alternative installation options.
* **[Dynamic Inventory Guide](/ansible/guides/dynamic-inventory.md)**: Discover how to leverage the collection's dynamic inventory features to streamline your infrastructure management.
* **[Query & Lookup Guide](/ansible/guides/query-and-lookup.md)**: Learn how to retrieve structured GraphQL data from Infrahub using Query and Lookup plugins.
* **[Create, Update and Delete Nodes Guide](/ansible/guides/node.md)**: Learn how to create, update and delete nodes in Infrahub using GraphQL action plugin or the node module.
* **[Manipulate Branch Guide](/ansible/guides/branch.md)**: Learn how to manipulate Branch in Infrahub.

## References[​](#references "Direct link to References")

### Plugins[​](#plugins "Direct link to Plugins")

These are the plugins in the `opsmill.infrahub` collection:

#### Modules[​](#modules "Direct link to Modules")

* [artifact\_fetch](/ansible/references/plugins/artifact_fetch_module.md) – Fetch the content of an artifact from Infrahub
* [schema](/ansible/references/plugins/schema_module.md) – Load, check, or export schemas in Infrahub
* [node](/ansible/references/plugins/node_module.md) – Creates, Updates or Deletes a node in Infrahub
* [artifact\_generate](/ansible/references/plugins/artifact_generate_module.md) – Trigger artifact regeneration in Infrahub
* [query\_graphql](/ansible/references/plugins/query_graphql_module.md) – Queries and returns elements from Infrahub GraphQL API
* [branch](/ansible/references/plugins/branch_module.md) – Creates, Updates or Deletes a branch in Infrahub

#### Inventory[​](#inventory "Direct link to Inventory")

* [inventory](/ansible/references/plugins/inventory_inventory.md) – Infrahub inventory source (using GraphQL)

#### Lookup[​](#lookup "Direct link to Lookup")

* [lookup](/ansible/references/plugins/lookup_lookup.md) – Queries and returns elements from Infrahub (using GraphQL)

### Roles[​](#roles "Direct link to Roles")

These are the roles in the `opsmill.infrahub` collection:

* [install](/ansible/references/roles/install.md) – Install Infrahub
