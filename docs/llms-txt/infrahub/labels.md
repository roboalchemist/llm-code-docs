# Source: https://docs.infrahub.app/topics/labels.md

# Understanding labels

Labels in Infrahub provide human-friendly names and identifiers for schema elements and object instances. They serve as the primary way users interact with and identify objects throughout the system, from the user interface to GraphQL queries.

This topic explains the different types of labels in Infrahub, how they work together, and how they enhance the user experience.

## Why labels matter[​](#why-labels-matter "Direct link to Why labels matter")

In a database system, technical identifiers like UUIDs and internal field names are essential for system operations, but they're not intuitive for human users. Labels bridge this gap by providing:

* **Readable names** in the user interface instead of technical identifiers
* **Contextual information** that helps users understand what they're looking at
* **Consistent presentation** across different views and interfaces
* **Dynamic representation** that adapts to the actual data

Infrahub uses labels at two distinct levels: schema labels that define how types of objects are named, and instance labels that identify individual objects.

## Schema labels[​](#schema-labels "Direct link to Schema labels")

Schema labels define the human-friendly names for the building blocks of your data model. These labels appear in menus, forms, and throughout the user interface to represent types of objects rather than individual instances.

### Automatic label generation[​](#automatic-label-generation "Direct link to Automatic label generation")

If you don't specify a label, Infrahub automatically generates one from the name.

For example, a node named `NetworkDevice` automatically gets the label `Networkdevice`.

info

`_` characters are converted to spaces, and each word is capitalized.

For example, an attribute named `serial_number` automatically gets the label `Serial Number`.

This automatic generation means you only need to specify labels when you want something different from the default formatting.

### Node labels[​](#node-labels "Direct link to Node labels")

A node label provides a human-friendly name for a node kind. When you define a node in your schema, the `label` property specifies how that type of object appears in the UI.

```
nodes:
  - name: NetworkDevice
    namespace: Infra
    label: Network Device
    attributes:
      - name: hostname
        kind: Text
```

In this example, users see `Network Device` in menus and page titles.

### Attribute labels[​](#attribute-labels "Direct link to Attribute labels")

Attribute labels define how attribute names appear in forms, tables, and detailed views. Like node labels, they transform technical field names into user-friendly text.

```
attributes:
  - name: serial_number
    kind: Text
    label: Serial Number
  - name: mac_address
    kind: MacAddress
    label: MAC Address
  - name: weight
    kind: Number
    label: Weight (kg)
```

### Relationship labels[​](#relationship-labels "Direct link to Relationship labels")

Relationship labels describe connections between nodes in a human-friendly way. They're particularly important because relationships often represent complex concepts that benefit from clear naming.

```
relationships:
  - name: primary_owner
    peer: OrganizationPerson
    kind: Attribute
    cardinality: one
    label: Owner
  - name: backup_contacts
    peer: OrganizationPerson
    kind: Generic
    cardinality: many
    label: Backup Contact(s)
```

The relationship labels appear in the UI when displaying connections between objects, making it clear what role each relationship plays.

### Dropdown choice labels[​](#dropdown-choice-labels "Direct link to Dropdown choice labels")

For attributes of kind `Dropdown`, each choice can have its own label to provide clear, descriptive text for selection options.

```
attributes:
  - name: status
    kind: Dropdown
    choices:
      - name: active
        label: "Active"
        color: "#00ff00"
      - name: maintenance
        label: "Under Maintenance"
        color: "#ff9900"
      - name: decommissioned
        label: "Decommissioned"
        color: "#ff0000"
```

These labels appear in dropdown menus and status displays, helping users understand the meaning of each choice.

## Display labels[​](#display-labels "Direct link to Display labels")

While schema labels identify types of objects, display labels identify individual instances of those objects. A display label is a dynamic, computed value that represents a specific object based on its attributes and relationships.

### How display labels work[​](#how-display-labels-work "Direct link to How display labels work")

Display labels are defined in the node schema using Jinja2 template syntax. The template references attributes and relationships to build a meaningful identifier for each object instance.

```
nodes:
  - name: Circuit
    namespace: Dcim
    display_label: "{{ reference_id__value }} ({{ provider__name__value }})"
    attributes:
      - name: reference_id
        kind: Text
        unique: true
    relationships:
      - name: provider
        peer: DcimProvider
        optional: false
        cardinality: one
```

When you create a circuit with reference ID `CIR-12345` from a provider named `GlobalNet`, the display label becomes `CIR-12345 (GlobalNet)`.

### Default behavior[​](#default-behavior "Direct link to Default behavior")

If no `display_label` is specified, Infrahub UI defaults to using the HFID (Human-Friendly Identifier) as the display label.

If neither a `display_label` nor an HFID is defined, the system falls back to showing the object's UUID.

For example, if you have a `DcimCircuit` node without a defined `display_label`, it appears as: `187c22fb-962d-5c78-326d-c517082cdbd4`

warning

This fallback behavior may lead to less user-friendly identifiers appearing in the UI, so it's recommended to define meaningful display labels for every node type.

### Display label templates[​](#display-label-templates "Direct link to Display label templates")

The Jinja2 template system provides powerful flexibility for creating meaningful display labels.

#### Single attribute reference[​](#single-attribute-reference "Direct link to Single attribute reference")

The most basic display label references a single attribute:

```
display_label: "{{ name__value }}"
```

Or

```
display_label: "name__value"
```

#### Multiple attributes[​](#multiple-attributes "Direct link to Multiple attributes")

Combine multiple attributes to create more descriptive labels:

```
display_label: "{{ hostname__value }} - {{ serial_number__value }}"
```

#### Relationship traversal[​](#relationship-traversal "Direct link to Relationship traversal")

Display labels can traverse relationships to include information from related objects:

```
display_label: "{{ device__name__value }}>{{ name__value }}"
```

This creates labels like `router-01>GigabitEthernet0/1` for an interface, showing both the device name and interface name.

#### Jinja2 filters[​](#jinja2-filters "Direct link to Jinja2 filters")

Use Jinja2 filters to transform values in the display label:

```
display_label: "{{ name__value|upper }}: {{ status__value|lower }}"
```

Common filters include `upper`, `lower`, and other standard Jinja2 transformations.

### When display labels are computed[​](#when-display-labels-are-computed "Direct link to When display labels are computed")

Display labels are automatically computed and stored when:

* An object is created
* An object's attributes are updated
* Related objects referenced in the display label change
* The schema definition is modified

This automatic computation ensures display labels always reflect current data without requiring manual updates.

### Display labels in the user interface[​](#display-labels-in-the-user-interface "Direct link to Display labels in the user interface")

Display labels appear throughout Infrahub:

* **Object lists**: Instead of UUIDs, you see meaningful identifiers
* **Relationship selectors**: When choosing related objects, display labels help identify options
* **Breadcrumbs and navigation**: Display labels provide context about where you are
* **Diff and merge views**: Changes show display labels to clarify what's being modified

### Display labels in GraphQL[​](#display-labels-in-graphql "Direct link to Display labels in GraphQL")

Display labels are accessible in GraphQL queries as a standard field:

```
query {
  DcimCircuit {
    edges {
      node {
        id
        display_label
        reference_id {
          value
        }
      }
    }
  }
}
```

The `display_label` field returns the computed label for each object.

## Relationship between schema labels and display labels[​](#relationship-between-schema-labels-and-display-labels "Direct link to Relationship between schema labels and display labels")

Schema labels and display labels work together to create a complete identification system:

* **Schema labels** tell you what type of thing you're looking at ("Circuit", "Device", "Interface")
* **Display labels** tell you which specific instance you're looking at ("CIR-12345 (GlobalNet)", "router-01")

For example, in a list view, you might see a page titled "Circuits" (from the node label) with a list of items like "CIR-12345 (GlobalNet)" and "CIR-67890 (LocalISP)" (from display labels).

## Label inheritance[​](#label-inheritance "Direct link to Label inheritance")

When using generics with inheritance, labels follow specific rules:

### Inherited node labels[​](#inherited-node-labels "Direct link to Inherited node labels")

Node labels are inherited from the first generic in the `inherit_from` list if not explicitly defined at the node level:

```
generics:
  - name: GenericDevice
    namespace: Infra
    label: Device
    display_label: "{{ name__value }}"

nodes:
  - name: Router
    namespace: Infra
    inherit_from:
      - InfraGenericDevice
    # Inherits label "Device" and display_label "{{ name__value }}"
```

warning

Please note that after the initial inheritance, changes to the generic's label or display\_label do not propagate to existing nodes. Each node maintains its own copy of the `label` and `display_label` once created.

### Overriding inherited labels[​](#overriding-inherited-labels "Direct link to Overriding inherited labels")

Nodes can override inherited labels by specifying their own:

```
nodes:
  - name: Router
    namespace: Infra
    inherit_from:
      - "InfraGenericDevice"
    label: "Network Router"  # Overrides inherited label
    display_label: "{{ hostname__value }} (Router)"  # Overrides inherited display_label
```

## Label constraints and limitations[​](#label-constraints-and-limitations "Direct link to Label constraints and limitations")

### Display label limitations[​](#display-label-limitations "Direct link to Display label limitations")

Display labels have specific constraints to ensure reliable operation:

* **Relationship cardinality**: Relationships referenced in display labels must have cardinality `one`
* **Traversal depth**: Display labels support only one level of relationship traversal
* **Template syntax**: Must use valid Jinja2 syntax with the `{{ attribute__value }}` format

### Label length limits[​](#label-length-limits "Direct link to Label length limits")

Schema labels have maximum lengths to ensure consistent display:

* **Node labels**: Maximum 64 characters
* **Attribute labels**: Maximum 32 characters
* **Relationship labels**: Maximum 32 characters

These limits apply to the label text itself, not the underlying field names.

## Best practices[​](#best-practices "Direct link to Best practices")

### Choosing meaningful display labels[​](#choosing-meaningful-display-labels "Direct link to Choosing meaningful display labels")

Good display labels balance brevity with descriptiveness:

* **Include unique identifiers**: Use attributes that help distinguish objects (names, IDs, serial numbers)
* **Add context where helpful**: Include parent object names or categories when they clarify meaning
* **Keep them concise**: Display labels appear in lists and dropdowns where space is limited
* **Use consistent patterns**: Apply similar display label patterns across related node types

### Examples of effective display labels[​](#examples-of-effective-display-labels "Direct link to Examples of effective display labels")

```
# Device: Show name and location
display_label: "{{ name__value }} ({{ site__name__value }})"

# Interface: Show device and interface name
display_label: "{{ device__name__value }}>{{ name__value }}"

# IP Address: Show address and namespace
display_label: "{{ address__value }} [{{ ip_namespace__name__value }}]"

# Circuit: Show ID and provider
display_label: "{{ circuit_id__value }} - {{ provider__name__value }}"
```

### When to use explicit schema labels[​](#when-to-use-explicit-schema-labels "Direct link to When to use explicit schema labels")

While automatic label generation handles most cases well, specify explicit labels when:

* The automatic conversion doesn't match your terminology
* You need abbreviations or industry-specific terms
* The technical name and user-facing name should differ significantly

## Related topics and references[​](#related-topics-and-references "Direct link to Related topics and references")

Labels integrate with several other Infrahub concepts:

* [Schema definition](/topics/schema.md) - Comprehensive guide to defining schemas
* [Human-friendly identifiers (HFID)](/topics/schema.md#human-friendly-identifier-hfid) - Alternative identification system for API operations
* [Menu placement](/guides/menu.md) - How node labels appear in the UI menu structure
