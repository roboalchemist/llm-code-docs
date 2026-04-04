# Source: https://docs.infrahub.app/guides/import-schema.md

# Schema files

The recommended way to manage and load a schema is to create a schema file in YAML format. With a schema file it's possible to:

* Define new nodes
* Extend nodes, by adding attributes or relationships to the existing nodes

At a high level, the format of the schema file looks like the following:

```
---
version: '1.0'
nodes:
    - <new nodes are defined here>
extensions:
  nodes:
    - <node extensions are defined here>
```

Example of schema file that is defining new nodes and adding a relationship to an existing one

```
# yaml-language-server: $schema=https://schema.infrahub.app/infrahub/schema/latest.json
---
version: '1.0'
nodes:
  - name: Rack
    namespace: Infra
    description: "A Rack represents a physical two- or four-post equipment rack in which devices can be installed"
    label: "Rack"
    default_filter: name__value
    icon: clarity:rack-server-solid
    display_label: "{{ name__value }}"
    attributes:
      - name: name
        kind: Text
        # unique: true
      - name: description
        kind: Text
        optional: true
      - name: height
        kind: Text
      - name: facility_id
        label: Facility ID
        kind: Text
        optional: true
      - name: serial_number
        label: Serial Number
        kind: Text
        optional: true
      - name: asset_tag
        label: Asset Tag
        kind: Text
        optional: true
      - name: status
        kind: Dropdown
        choices:
          - name: active
            label: Active
            description: "Functional and ready for production"
            color: "#009933"
          - name: planned
            label: Planned
            description: "Not physically present yet"
            color: "#cc66ff"
        default_value: "active"
      - name: role
        kind: Dropdown
        choices:
          - name: compute
            description: "Rack mainly composed of compute"
            color: "#0099ff"
          - name: storage
            description: "Rack mainly composed of Storage devices"
            color: "#993399"
          - name: networking
            description: "Rack mainly composed of Network devices"
            color: "#ff6600"
        optional: true
    relationships:
      - name: site
        peer: InfraSite
        optional: false
        cardinality: one
        kind: Attribute
      - name: tags
        peer: BuiltinTag
        optional: true
        cardinality: many
        kind: Attribute
extensions:
  nodes:
    - kind: InfraSite
      relationships:
        - name: racks
          peer: InfraRack
          optional: true
          cardinality: many
          kind: Generic
```

note

To help with the development process of a schema definition file, you can leverage [schema validation](/reference/schema-validation.md) within your editor.

## Load a schema file[​](#load-a-schema-file "Direct link to Load a schema file")

Schema files can be loaded into Infrahub with the `infrahubctl` command or directly via the Git integration.

### infrahubctl command[​](#infrahubctl-command "Direct link to infrahubctl command")

The `infrahubctl` command can be used to load individual schema files or multiple files as part of a directory.

```
infrahubctl schema load <path to schema file or a directory> <path to schema file or a directory>
```

### Git integration[​](#git-integration "Direct link to Git integration")

You can define a schema in an [external repository](/topics/repository.md). The schemas that should be loaded must be declared in the `.infrahub.yml` file, under schemas.

Individual files and directories are both supported.

```
---
schemas:
  - schemas/demo_edge_fabric.yml
```
