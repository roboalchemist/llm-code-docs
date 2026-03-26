# Source: https://docs.infrahub.app/reference/schema/validator-migration.md

# Schema Update

For each element\* of the schema, when its value is being updated, Infrahub will determine what should be done from the list of possible actions:

* **allowed** : Nothing is required, the update of this element is allowed
* **migration\_required** : The existing data must be migrated to the new schema
* **validate\_constraint** : The existing data needs to be validated to ensure that its compatible with the new schema
* **not\_supported** : The update of this element is not supported

info

In this context, an element represent either a Node, a Generic, an Attribute or a Relationship

## Reference Guide[​](#reference-guide "Direct link to Reference Guide")

### Node[​](#node "Direct link to Node")

| Name                        | Status               |
| --------------------------- | -------------------- |
| **name**                    | migration\_required  |
| **namespace**               | migration\_required  |
| **description**             | allowed              |
| **label**                   | allowed              |
| **branch**                  | not\_supported       |
| **default\_filter**         | allowed              |
| **human\_friendly\_id**     | allowed              |
| **display\_label**          | allowed              |
| **display\_labels**         | allowed              |
| **include\_in\_menu**       | allowed              |
| **menu\_placement**         | allowed              |
| **icon**                    | allowed              |
| **order\_by**               | allowed              |
| **uniqueness\_constraints** | validate\_constraint |
| **documentation**           | allowed              |
| **inherit\_from**           | validate\_constraint |
| **generate\_profile**       | validate\_constraint |
| **generate\_template**      | allowed              |
| **hierarchy**               | validate\_constraint |
| **parent**                  | validate\_constraint |
| **children**                | validate\_constraint |

### Attribute[​](#attribute "Direct link to Attribute")

| Name                    | Status               |
| ----------------------- | -------------------- |
| **name**                | migration\_required  |
| **kind**                | migration\_required  |
| **enum**                | validate\_constraint |
| **computed\_attribute** | allowed              |
| **choices**             | validate\_constraint |
| **regex**               | validate\_constraint |
| **max\_length**         | validate\_constraint |
| **min\_length**         | validate\_constraint |
| **label**               | allowed              |
| **description**         | allowed              |
| **read\_only**          | migration\_required  |
| **unique**              | validate\_constraint |
| **optional**            | migration\_required  |
| **branch**              | not\_supported       |
| **order\_weight**       | allowed              |
| **default\_value**      | allowed              |
| **allow\_override**     | allowed              |
| **parameters**          | validate\_constraint |
| **deprecation**         | allowed              |

### Relationship[​](#relationship "Direct link to Relationship")

| Name                  | Status               |
| --------------------- | -------------------- |
| **name**              | allowed              |
| **peer**              | validate\_constraint |
| **kind**              | allowed              |
| **label**             | allowed              |
| **description**       | allowed              |
| **identifier**        | allowed              |
| **cardinality**       | validate\_constraint |
| **min\_count**        | validate\_constraint |
| **max\_count**        | validate\_constraint |
| **common\_parent**    | validate\_constraint |
| **common\_relatives** | allowed              |
| **order\_weight**     | allowed              |
| **optional**          | validate\_constraint |
| **branch**            | not\_supported       |
| **direction**         | not\_supported       |
| **hierarchical**      | not\_supported       |
| **on\_delete**        | allowed              |
| **allow\_override**   | allowed              |
| **read\_only**        | allowed              |
| **deprecation**       | allowed              |

### Generic[​](#generic "Direct link to Generic")

| Name                        | Status               |
| --------------------------- | -------------------- |
| **name**                    | migration\_required  |
| **namespace**               | migration\_required  |
| **description**             | allowed              |
| **label**                   | allowed              |
| **branch**                  | not\_supported       |
| **default\_filter**         | allowed              |
| **human\_friendly\_id**     | allowed              |
| **display\_label**          | allowed              |
| **display\_labels**         | allowed              |
| **include\_in\_menu**       | allowed              |
| **menu\_placement**         | allowed              |
| **icon**                    | allowed              |
| **order\_by**               | allowed              |
| **uniqueness\_constraints** | validate\_constraint |
| **documentation**           | allowed              |
| **hierarchical**            | validate\_constraint |
| **generate\_profile**       | validate\_constraint |
