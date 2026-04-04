# Source: https://archivedocs.stackstate.com/5.1/configure/topology/how_to_create_manual_topology.md

# Create a topology manually

StackState automatically creates a topology based on real-time data sources. *There is typically no need to create a topology manually*. There may be a few exceptions:

* Business processes are typically not discoverable and may therefore be placed on top of the topology manually.
* When developing an automatic topology synchronization, creating a topology manually at first and then exporting the results is a good first step.

## Static Topology StackPack

The [Static Topology StackPack](https://archivedocs.stackstate.com/5.1/stackpacks/integrations/static_topology) can be used to import components and relations from external CSV files.

## How to create components and relations

1. All component types, domains and layers that will be imported need to exist in StackState before the topology can be imported. The Static Topology StackPack installs the common StackPack as a dependency and that imports quite a few useful nodes into the system. If required, you can also add these manually in the StackState UI:
   * **Component types** - Go to `Settings > Component Types > Add Component Types`. The component type consists of a `Name` field, a `Description` field (optional), and an Icon.
   * **Domains** - Go to `Settings > Domains > Add Domain`. A domain consists of a `Name` field, a `Description` field (optional), and an `Order`. Domains are ordered from left to right in the topology visualization, where the left-most domain has the lowest value set for `Order`.
   * **Layers** - Go to `Settings > Layers > Add Layer`. A Layer consists of a `Name` field, a `Description` field (optional), and an `Order`. Layers are ordered from top to bottom in the topology visualization, where the top-most layer has the lowest value set for `Order`.
2. You can now import components and relations from CSV files using the [Static Topology StackPack](https://archivedocs.stackstate.com/5.1/stackpacks/integrations/static_topology).

## Export/import manually created topology

See [manual topology backup/restore](https://archivedocs.stackstate.com/5.1/configure/topology/broken-reference).
