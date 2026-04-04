# Source: https://docs.infrahub.app/topics/order-weight.md

# Order weight

The `order_weight` property controls how attributes and relationships are ordered in the Infrahub frontend, including table views and detailed object views. **Lower `order_weight` values appear first.** This means items with smaller numbers are displayed before those with larger numbers. Understanding how default values are assigned and how to work with them effectively is crucial for creating well-organized schemas.

[Customize field ordering guide../guides/customize-field-ordering](../guides/customize-field-ordering)

## Ordering principle[​](#ordering-principle "Direct link to Ordering principle")

**Lower `order_weight` values appear first.** This means items with smaller numbers are displayed before those with larger numbers.

## Default assignment logic[​](#default-assignment-logic "Direct link to Default assignment logic")

When you don't explicitly specify an `order_weight` value, Infrahub automatically assigns default values using a predictable pattern:

### The 1000-increment pattern[​](#the-1000-increment-pattern "Direct link to The 1000-increment pattern")

* **First attribute/relationship**: Gets `order_weight: 1000`
* **Second attribute/relationship**: Gets `order_weight: 2000`
* **Third attribute/relationship**: Gets `order_weight: 3000`
* **And so on**: Each subsequent field increments by 1000

This happens for both attributes and relationships, in the order they appear in your schema definition.

Example Schema with Default Weights

```
nodes:
  - name: Device
    namespace: Infra
    attributes:
      - name: name          # Gets order_weight: 1000
        kind: Text
      - name: description   # Gets order_weight: 2000
        kind: Text
        optional: true
      - name: serial_number # Gets order_weight: 3000
        kind: Text
    relationships:
      - name: site          # Gets order_weight: 4000
        peer: InfraSite
        cardinality: one
      - name: interfaces    # Gets order_weight: 5000
        peer: InfraInterface
        cardinality: many
```

### When default assignment occurs[​](#when-default-assignment-occurs "Direct link to When default assignment occurs")

Default `order_weight` values are assigned during **schema post-validation processing**, which happens when you:

* Load a new schema (for example with `infrahubctl schema load`)
* Update an existing schema
* Process schema changes during branch operations (merge, rebase)

Only fields **without an existing `order_weight`** receive default values. If you've explicitly set a value, it won't be overridden.

## Inheritance and generics[​](#inheritance-and-generics "Direct link to Inheritance and generics")

### Generic inheritance[​](#generic-inheritance "Direct link to Generic inheritance")

When a node inherits from a generic, the order weight assignment follows this pattern:

Generic with Order Weights

```
generics:
  - name: BaseDevice
    namespace: Infra
    attributes:
      - name: name          # Gets order_weight: 1000
        kind: Text
      - name: description   # Gets order_weight: 2000
        kind: Text
        optional: true

nodes:
  - name: Router
    namespace: Infra
    inherit_from: ["InfraBaseDevice"]
    attributes:
      - name: model         # Gets order_weight: 3000
        kind: Text
      - name: os_version    # Gets order_weight: 4000
        kind: Text
```

The inherited attributes maintain their original weights (1000, 2000), while new attributes continue the sequence (3000, 4000).

### Multiple inheritance[​](#multiple-inheritance "Direct link to Multiple inheritance")

With multiple generics, order weight assignment prioritizes the **first generic** in the `inherit_from` list:

Multiple Inheritance Example

```
generics:
  - name: NetworkDevice
    namespace: Infra
    attributes:
      - name: ip_address    # Gets order_weight: 1000
        kind: IPHost

  - name: ManagedDevice
    namespace: Infra
    attributes:
      - name: snmp_community # Gets order_weight: 1000 (but NetworkDevice takes precedence)
        kind: Text

nodes:
  - name: Switch
    namespace: Infra
    inherit_from: ["InfraNetworkDevice", "InfraManagedDevice"]  # NetworkDevice first
    attributes:
      - name: vlan_count    # Gets order_weight: 2000
        kind: Number
```

## Template handling[​](#template-handling "Direct link to Template handling")

For object templates, a special rule applies:

* If a template field corresponds to a node field, it gets: **node field weight + 10000**
* If no corresponding node field exists, it gets `None`

Template Weight Example

```
# If the base node has name with order_weight: 1000
# The template field gets order_weight: 11000 (1000 + 10000)
```

## Mental models for working with order weight[​](#mental-models-for-working-with-order-weight "Direct link to Mental models for working with order weight")

### Think in ranges[​](#think-in-ranges "Direct link to Think in ranges")

Instead of thinking about exact numbers, think in ranges:

* **1-999**: Reserved for high-priority fields you want to appear first
* **1000-9999**: Default range (system-assigned values)
* **10000+**: Low-priority fields or those you want to appear last

### Common spacing patterns[​](#common-spacing-patterns "Direct link to Common spacing patterns")

**Conservative spacing (recommended)**:

```
order_weight: 100   # Primary identifier
order_weight: 500   # Secondary important field
order_weight: 1500  # Between first and second default fields
order_weight: 2500  # Between second and third default fields
```

**Aggressive spacing**:

```
order_weight: 10    # Highest priority
order_weight: 50    # High priority
order_weight: 99    # Just before defaults
order_weight: 9999  # Just after all defaults
```

## Why the large increment?[​](#why-the-large-increment "Direct link to Why the large increment?")

The 1000-increment pattern provides flexibility for users to:

1. **Insert fields easily**: Use values like 1500, 2500 to place fields between defaults
2. **Group related fields**: Reserve ranges like 3000-3999 for a specific category
3. **Avoid conflicts**: Reduce chance of accidentally using the same weight twice

## Best practices[​](#best-practices "Direct link to Best practices")

### For new schemas[​](#for-new-schemas "Direct link to For new schemas")

* **Let defaults work for you**: Don't specify `order_weight` unless you need custom ordering
* **Use logical field ordering**: Place fields in your schema definition in the order you want them displayed
* **Reserve low numbers**: Keep 1-999 for fields that must appear first

### For existing schemas[​](#for-existing-schemas "Direct link to For existing schemas")

* **Check current weights first**: Use the schema explorer at `/schema` to see existing values
* **Use gaps effectively**: Insert new fields using values between existing ones
* **Consider reorganization**: If you have many custom weights, consider a systematic renumbering

### For field insertion[​](#for-field-insertion "Direct link to For field insertion")

Inserting Between Existing Fields

```
# Existing fields have weights 1000, 2000, 3000
# To insert between first and second:
attributes:
  - name: new_field
    kind: Text
    order_weight: 1500  # Will appear between 1000 and 2000
```

## Common scenarios[​](#common-scenarios "Direct link to Common scenarios")

### Promoting a field to first position[​](#promoting-a-field-to-first-position "Direct link to Promoting a field to first position")

```
attributes:
  - name: primary_field
    kind: Text
    order_weight: 100  # Well below the 1000 default range
```

### Grouping related fields[​](#grouping-related-fields "Direct link to Grouping related fields")

```
attributes:
  # Network settings group (3100-3199)
  - name: ip_address
    kind: IPHost
    order_weight: 3100
  - name: subnet_mask
    kind: IPNetwork
    order_weight: 3110
  - name: gateway
    kind: IPHost
    order_weight: 3120

  # Hardware settings group (3200-3299)
  - name: cpu_count
    kind: Number
    order_weight: 3200
  - name: memory_gb
    kind: Number
    order_weight: 3210
```

## Relationships of kind "attribute"[​](#relationships-of-kind-attribute "Direct link to Relationships of kind \"attribute\"")

Relationships with `kind: Attribute` are a special type of relationship in Infrahub that behave more like attributes in the UI but maintain the power and flexibility of relationships. They're commonly used for connecting to resource pools, IP addresses, and other managed resources.

For more details on relationships, refer to the [schema topic](/topics/schema.md).

### Order weight behavior[​](#order-weight-behavior "Direct link to Order weight behavior")

Relationships of kind "Attribute" follow the same order weight rules as regular attributes and relationships:

Example with Attribute Relationships

```
nodes:
  - name: Device
    namespace: Infra
    attributes:
      - name: name              # Gets order_weight: 1000
        kind: Text
      - name: description       # Gets order_weight: 2000
        kind: Text
    relationships:
      - name: ip_address        # Gets order_weight: 3000
        peer: InfraIPAddress
        kind: Attribute
        cardinality: one
      - name: asn               # Gets order_weight: 4000
        peer: InfraAutonomousSystem
        kind: Attribute
        cardinality: one
      - name: location          # Gets order_weight: 5000
        peer: InfraLocation
        kind: Generic           # Regular relationship
        cardinality: one
```

### UI presentation[​](#ui-presentation "Direct link to UI presentation")

Relationships of kind "Attribute" appear alongside regular attributes in forms and tables, making them feel like native attributes to users while maintaining referential integrity:

* **In forms**: Displayed as dropdowns or select fields like attributes
* **In tables**: Shown in columns alongside attribute values
* **In filters**: Available for filtering just like attributes

### Common use cases[​](#common-use-cases "Direct link to Common use cases")

IP Address Management

```
relationships:
  - name: primary_ip
    peer: InfraIPAddress
    kind: Attribute
    cardinality: one
    order_weight: 1500  # Position between name and description
```

Resource Pool Assignment

```
relationships:
  - name: vlan_id
    peer: InfraVLAN
    kind: Attribute
    cardinality: one
    optional: false
    order_weight: 500   # Prioritize before most attributes
```

### Best practices for attribute relationships[​](#best-practices-for-attribute-relationships "Direct link to Best practices for attribute relationships")

1. **Positioning**: Place attribute relationships logically with related fields
2. **Naming**: Use attribute-like names (for example `ip_address` not `has_ip_address`)
3. **Grouping**: Keep attribute relationships close to related attributes in order weight

Grouped Attribute Relationships

```
attributes:
  # Network identity group (1000-1999)
  - name: hostname
    kind: Text
    order_weight: 1000
  # Hardware info group (2000-2999)
  - name: serial_number
    kind: Text
    order_weight: 2000

relationships:
  - name: primary_ip4      # Attribute relationship
    peer: InfraIPAddress
    kind: Attribute
    order_weight: 1100
  - name: primary_ip6      # Attribute relationship
    peer: InfraIPAddress
    kind: Attribute
    order_weight: 1200
```

## Related concepts[​](#related-concepts "Direct link to Related concepts")

* **Menu placement**: Affects how models are organized in the frontend sidebar
* **Display labels**: Determines which fields appear in list views and detailed views
* **GraphQL schema**: Influences the order of fields in API responses
* **[Schema changes](/topics/schema.md)**: Order weight changes are allowed during schema updates

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

### "My field with order\_weight: 999 still appears after defaults"[​](#my-field-with-order_weight-999-still-appears-after-defaults "Direct link to \"My field with order_weight: 999 still appears after defaults\"")

* Check if other fields have even lower weights (1-998)
* Verify the schema was successfully loaded with your changes
* Use the schema explorer to confirm the current weights

### "I want to reorganize all fields efficiently"[​](#i-want-to-reorganize-all-fields-efficiently "Direct link to \"I want to reorganize all fields efficiently\"")

* Consider using systematic numbering (100, 200, 300) for major reorganization
* Update your schema definition order to match your desired display order
* Test changes in a branch before applying to main
