# Source: https://docs.infrahub.app/release-notes/infrahub/release-0_12.md

| Release Number   | 0.12.0                                                                                |
| ---------------- | ------------------------------------------------------------------------------------- |
| Release Date     | March 16, 2024                                                                        |
| Release Codename | Beta #1                                                                               |
| Tag              | [infrahub-v0.12.0](https://github.com/opsmill/infrahub/releases/tag/infrahub-v0.12.0) |

# Release 0.12.0 - Beta #1

## Main changes[​](#main-changes "Direct link to Main changes")

### Unified storage[​](#unified-storage "Direct link to Unified storage")

#### Schema update & migrations[​](#schema-update--migrations "Direct link to Schema update & migrations")

It's now possible to update the schema without losing data. Infrahub will automatically apply the validations and the migrations to ensure the data currently in the database is compliant with the new schema.

The validations and the migrations will also be applied :

* As part of a Proposed Change
* During a branch rebase
* During a branch merge

#### Non isolated branches[​](#non-isolated-branches "Direct link to Non isolated branches")

The default behavior for a branch has been updated to keep in sync with the main branch by default.<br /><!-- -->With this new behavior, all changes applied to the main branch will automatically be visible in the branches without the need for rebase.

A new isolated branch mode has been introduced. It allows a branch to be isolated from the main branch. Isolated branches are not kept in sync with the changes in the main branch. With these changes, the `rebase` flag in the API and in the Transformations has been deprecated.

The flag `data_only` on a branch has been renamed to `sync_with_git` to provide a better description of its intent. The meaning of this flag has been switched so `is_data_only=true` is the same as `sync_with_git=false`.

#### Additional constraints for the schema[​](#additional-constraints-for-the-schema "Direct link to Additional constraints for the schema")

A few additional constraints have been added to the schema to enforce your business logic.

##### Multiple uniqueness constraints[​](#multiple-uniqueness-constraints "Direct link to Multiple uniqueness constraints")

On a Node or a Generic, it's now possible to define one or multiple uniqueness constraints composed of multiple attributes or relationships of cardinality one.

In the example below, all Interfaces will be guaranteed to be unique based on their name and the device they are connected to.

```
  - name: Interface
    namespace: Infra
    uniqueness_constraints:
        - [ "device", "name__value"]
    attributes:
      - name: name
        kind: Text
    relationships:
      - name: device
        cardinality: one
        peer: InfraDevice
        kind: Parent
```

##### `min_max` / `max_count` for relationships[​](#min_max--max_count-for-relationships "Direct link to min_max--max_count-for-relationships")

On a relationship of cardinality many, it's now possible to define a minimum or maximum number of peers that should be present.

```
    relationships:
      - name: "tags"
        cardinality: "many"
        peer: "BuiltinTag"
        max_count: 5
        min_count: 2
```

#### New Version of the data & time picker[​](#new-version-of-the-data--time-picker "Direct link to New Version of the data & time picker")

The widget to select the active date and time has been updated to improve its usability. In addition to this change, all edits have been disabled while viewing past data to avoid any confusions and guarantee the immutability of the database.

### CI pipeline[​](#ci-pipeline "Direct link to CI pipeline")

The CI Pipeline as part of a Proposed Change has been significantly improved to provide more visibility to the user.

#### New version of the check view[​](#new-version-of-the-check-view "Direct link to New version of the check view")

The page to display the progression and the results of the checks has been redesigned to provide more visibility.

![Proposed Change ](/assets/images/proposed_change_checks-579866e95df82896ea8b93eb5a9020f2.png) ![Proposed Change ](/assets/images/proposed_change_failed_checks-a799ac681125e588c3db3623b138f262.png)

#### Background tasks[​](#background-tasks "Direct link to Background tasks")

Information about background pipeline tasks are now available in the Tasks tab of the proposed change view.

![schema visualizer](/assets/images/proposed_change_tasks-4bfc5dbbe37fee065aec07f7311b3748.png)

### Schema[​](#schema "Direct link to Schema")

#### Schema visualizer[​](#schema-visualizer "Direct link to Schema visualizer")

The Schema page in the frontend has been redesigned to make it easier to navigate the current schema. All information are now accessible, in the future the page will be updated to modify the schema directly from the frontend as well.

![schema visualizer](/assets/images/schema_visualizer-8cac0a23f899f7d19f04940b2cb2694a.png)

#### Schema documentation[​](#schema-documentation "Direct link to Schema documentation")

The internal schema has been refactored in order to generate better documentation and to be able to provide better validation of new schema. A new definition of the internal schema has been published in JSONSchema format and it's accessible at `https://schema.infrahub.app/infrahub/schema/latest.json`

Multiple Editors are able to leverage this file to provide inline documentation and validation.

In VS Code, [the YAML Plugin](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml) support file with the `yaml-language-server` marker at the top of the file.

```
# yaml-language-server: $schema=https://schema.infrahub.app/infrahub/schema/latest.json
---
version: '1.0'
generics:
  - name: Interface
    namespace: Infra
```

### API / GraphQL[​](#api--graphql "Direct link to API / GraphQL")

#### New `DiffSummary` query[​](#new-diffsummary-query "Direct link to new-diffsummary-query")

The GraphQL query `DiffSummary` has been refactored to expose more information, it's now possible to query information about the attributes and the relationships in addition to the nodes. The previous version of the Query has been migrated to `DiffSummaryOld` and it will be removed in the next release.

### Other[​](#other "Direct link to Other")

#### Enhanced search bar[​](#enhanced-search-bar "Direct link to Enhanced search bar")

The search bar has been enhanced to return more information. In addition to the objects, it's now possible to search the documentation and to navigate directly to other pages in the frontend. The search results view has also been redesigned to make it faster and more accessible.

![search bar](/assets/images/search_bar_02-70b3a8890695faabea023db2d67594bd.png)

#### Performance improvement[​](#performance-improvement "Direct link to Performance improvement")

The processing of the schema internally has been significantly improved and as a result:

* Accessing the schema is 5x to 10x faster
* Loading a new schema is 3x faster
* Loading the frontend for the first time is significantly faster too

#### Sync engine[​](#sync-engine "Direct link to Sync engine")

The Synchronization Engine has been improved to be able to run in standalone mode and it has been integrated with Dagster, to provide more visibility into the process and leverage its orchestration capabilities. The project has been packaged as a dedicated Python package and it's now available on PyPI `infrahub-sync`.

#### Documentation update[​](#documentation-update "Direct link to Documentation update")

There have been multiple improvements to the documentation, including:

* A new topic page about Immutability and Version Control
* A new topic page about the Resources testing framework
* A new guide on how to create your own schema
* The Python SDK section has been reorganized to have Guides, a Reference, and include more information
