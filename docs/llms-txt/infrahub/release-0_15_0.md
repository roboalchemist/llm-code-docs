# Source: https://docs.infrahub.app/release-notes/infrahub/release-0_15_0.md

| Release Number   | 0.15.0                                                                                |
| ---------------- | ------------------------------------------------------------------------------------- |
| Release Date     | July 11th, 2024                                                                       |
| Release Codename | Beta #4                                                                               |
| Tag              | [infrahub-v0.15.0](https://github.com/opsmill/infrahub/releases/tag/infrahub-v0.15.0) |

# Release 0.15.0

We are thrilled to announce the latest release of Infrahub (0.15). This release focuses on enhancing the user experience and laying the groundwork for future features.

## Main changes[​](#main-changes "Direct link to Main changes")

### Unified storage[​](#unified-storage "Direct link to Unified storage")

#### Profiles enhancements[​](#profiles-enhancements "Direct link to Profiles enhancements")

* You can now create Profiles on a Generic, in addition to Nodes.
* A node inheriting from multiple Generics can utilize any Profiles associated with these Generics.
* Introduced a new attribute `generate_profile` in the schema for more precise control over which nodes should have Profiles generated or supported.
* Profiles have been disabled on most core models.

### Schema[​](#schema "Direct link to Schema")

#### Schema validation[​](#schema-validation "Direct link to Schema validation")

Added a new validation to ensure schemas do not require relationships to one another. This will prevent incompatible schemas from being loaded in the future.

### Frontend[​](#frontend "Direct link to Frontend")

#### Tree view for hierarchical model[​](#tree-view-for-hierarchical-model "Direct link to Tree view for hierarchical model")

All [hierarchical models](/topics/schema.md#hierarchical-mode) will now display a tree view in the frontend to simplify navigation across the tree.

#### Hierarchical dropdowns for relationships to parent/component models[​](#hierarchical-dropdowns-for-relationships-to-parentcomponent-models "Direct link to Hierarchical dropdowns for relationships to parent/component models")

When a relationship references a peer model with a parent (identified by a parent relationship), the form will automatically display multiple dropdown fields—one for the parent and one for the object itself, filtered by parent.

#### Refactor form components[​](#refactor-form-components "Direct link to Refactor form components")

The form component in the frontend has been refactored to provide a better foundation for future features that could not be supported by the previous version.

### Helm chart[​](#helm-chart "Direct link to Helm chart")

#### Upstream charts[​](#upstream-charts "Direct link to Upstream charts")

The official helm chart to deploy Infrahub now leverages the upstream charts for Neo4j, Redis, and RabbitMQ instead of defining these components directly. This approach provides more flexibility and allows us to use pod settings such as pod affinity.

### Infrahub sync[​](#infrahub-sync "Direct link to Infrahub sync")

#### Integration with IP Fabric[​](#integration-with-ip-fabric "Direct link to Integration with IP Fabric")

Added the initial version of the Infrahub Sync adapter for IP Fabric.

### Other[​](#other "Direct link to Other")

#### Support for `isnull` filter for attributes and relationships[​](#support-for-isnull-filter-for-attributes-and-relationships "Direct link to support-for-isnull-filter-for-attributes-and-relationships")

In most GraphQL queries, it’s now possible to search for objects based on the absence of an attribute or a relationship using the new isnull filter. For example, the following query returns all groups that have a parent group defined: As an example the following query will return all groups that have a parent group defined.

```
query {
  CoreGroup(parent__isnull: false){
    edges {
      node {
        display_label
      }
    }
  }
}
```

#### Dedicated search anywhere query in GraphQL[​](#dedicated-search-anywhere-query-in-graphql "Direct link to Dedicated search anywhere query in GraphQL")

The search anywhere bar in the frontend now leverages a dedicated GraphQL query.<br /><!-- -->This new query can search for objects by their UUID, improving search results.

#### Generate `Protocol` for `Core` models[​](#generate-protocol-for-core-models "Direct link to generate-protocol-for-core-models")

Protocol for the internal models have been introduced to improve typing and type checking across the backend.

#### Drop support for Pydantic V1 & Python 3.9[​](#drop-support-for-pydantic-v1--python-39 "Direct link to Drop support for Pydantic V1 & Python 3.9")

Internally, Infrahub no longer support Python 3.9 and Pydantic v1.

### Demo environment[​](#demo-environment "Direct link to Demo environment")

#### Cleanup and performance improvement[​](#cleanup-and-performance-improvement "Direct link to Cleanup and performance improvement")

The script infrastructure\_edge.py used to load data in the demo environment has been cleaned up to improve readability and performance. Demo in codespace should start faster now.

#### New `Services` models[​](#new-services-models "Direct link to new-services-models")

A new service model has been added to the demo schema

## Migration guide[​](#migration-guide "Direct link to Migration guide")

To migrate your instance of Infrahub to the latest version, please run the following commands and restart all instances of Infrahub.

```
infrahub db migrate
infrahub db update-core-schema
```

> If you are running in Docker these commands need to run from the container where Infrahub is installed

### Migration of the demo instance[​](#migration-of-the-demo-instance "Direct link to Migration of the demo instance")

If you are using the demo environment, you can migrate to the latest version with the following commands

```
invoke demo.stop
invoke demo.build
invoke demo.migrate
invoke demo.start
```

If you don't want to keep your data, you can start a clean instance with the following command

```
invoke demo.destroy demo.build demo.start demo.load-infra-schema demo.load-infra-data
```

> All data will be lost, please make sure to backup everything you need before running this command.

The repository [infrahub-demo-edge](https://github.com/opsmill/infrahub-demo-edge) has also been updated, it's recommended to pull the latest changes into your fork.
