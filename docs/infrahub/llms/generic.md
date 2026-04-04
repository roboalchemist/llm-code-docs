# Source: https://docs.infrahub.app/reference/schema/generic.md

# Generic

## Summary[​](#summary "Direct link to Summary")

Below is the list of all available options to define a Generic in the schema

| Name                                                   | Type         | Description                                                                                                             | Mandatory |
| ------------------------------------------------------ | ------------ | ----------------------------------------------------------------------------------------------------------------------- | --------- |
| [**branch**](#branch)                                  | Attribute    | Type of branch support for the model.                                                                                   | False     |
| [**default\_filter**](#default_filter)                 | Attribute    | Default filter used to search for a node in addition to its ID. (deprecated: please use human\_friendly\_id instead)    | False     |
| [**description**](#description)                        | Attribute    | Short description of the model, will be visible in the frontend.                                                        | False     |
| [**display\_label**](#display_label)                   | Attribute    | Attribute or Jinja2 template to use to generate the display label                                                       | False     |
| [**display\_labels**](#display_labels)                 | Attribute    | List of attributes to use to generate the display label (deprecated)                                                    | False     |
| [**documentation**](#documentation)                    | Attribute    | Link to a documentation associated with this object, can be internal or external.                                       | False     |
| [**generate\_profile**](#generate_profile)             | Attribute    | Indicate if a profile schema should be generated for this schema                                                        | False     |
| [**hierarchical**](#hierarchical)                      | Attribute    | Defines if the Generic support the hierarchical mode.                                                                   | False     |
| [**human\_friendly\_id**](#human_friendly_id)          | Attribute    | Human friendly and unique identifier for the object.                                                                    | False     |
| [**icon**](#icon)                                      | Attribute    | Defines the icon to use in the menu. Must be a valid value from the MDI library <https://icon-sets.iconify.design/mdi/> | False     |
| [**include\_in\_menu**](#include_in_menu)              | Attribute    | Defines if objects of this kind should be included in the menu.                                                         | False     |
| [**label**](#label)                                    | Attribute    | Human friendly representation of the name/kind                                                                          | False     |
| [**menu\_placement**](#menu_placement)                 | Attribute    | Defines where in the menu this object should be placed.                                                                 | False     |
| [**name**](#name)                                      | Attribute    | Node name, must be unique within a namespace and must start with an uppercase letter.                                   | True      |
| [**namespace**](#namespace)                            | Attribute    | Node Namespace, Namespaces are used to organize models into logical groups and to prevent name collisions.              | True      |
| [**order\_by**](#order_by)                             | Attribute    | List of attributes to use to order the results by default                                                               | False     |
| [**state**](#state)                                    | Attribute    | Expected state of the node/generic after loading the schema                                                             | False     |
| [**uniqueness\_constraints**](#uniqueness_constraints) | Attribute    | List of multi-element uniqueness constraints that can combine relationships and attributes                              | False     |
| [**used\_by**](#used_by)                               | Attribute    | List of Nodes that are referencing this Generic                                                                         | False     |
| [**attributes**](#attributes)                          | Relationship |                                                                                                                         | False     |
| [**relationships**](#relationships)                    | Relationship |                                                                                                                         | False     |

## Reference Guide[​](#reference-guide "Direct link to Reference Guide")

### branch[​](#branch "Direct link to branch")

| Key                 | Value                                 |
| ------------------- | ------------------------------------- |
| **Name**            | branch                                |
| **Kind**            | `Text`                                |
| **Description**     | Type of branch support for the model. |
| **Optional**        | True                                  |
| **Default Value**   | aware                                 |
| **Constraints**     |                                       |
| **Accepted Values** | `aware` `agnostic` `local`            |

### default\_filter[​](#default_filter "Direct link to default_filter")

| Key               | Value                                                                                                                |
| ----------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Name**          | default\_filter                                                                                                      |
| **Kind**          | `Text`                                                                                                               |
| **Description**   | Default filter used to search for a node in addition to its ID. (deprecated: please use human\_friendly\_id instead) |
| **Optional**      | True                                                                                                                 |
| **Default Value** |                                                                                                                      |
| **Constraints**   | Regex: `^[a-z0-9\_]*$`                                                                                               |

### description[​](#description "Direct link to description")

| Key               | Value                                                            |
| ----------------- | ---------------------------------------------------------------- |
| **Name**          | description                                                      |
| **Kind**          | `Text`                                                           |
| **Description**   | Short description of the model, will be visible in the frontend. |
| **Optional**      | True                                                             |
| **Default Value** |                                                                  |
| **Constraints**   | Length: min -, max 128                                           |

### display\_label[​](#display_label "Direct link to display_label")

| Key               | Value                                                             |
| ----------------- | ----------------------------------------------------------------- |
| **Name**          | display\_label                                                    |
| **Kind**          | `Text`                                                            |
| **Description**   | Attribute or Jinja2 template to use to generate the display label |
| **Optional**      | True                                                              |
| **Default Value** |                                                                   |
| **Constraints**   |                                                                   |

### display\_labels[​](#display_labels "Direct link to display_labels")

| Key               | Value                                                                |
| ----------------- | -------------------------------------------------------------------- |
| **Name**          | display\_labels                                                      |
| **Kind**          | `List`                                                               |
| **Description**   | List of attributes to use to generate the display label (deprecated) |
| **Optional**      | True                                                                 |
| **Default Value** |                                                                      |
| **Constraints**   |                                                                      |

### documentation[​](#documentation "Direct link to documentation")

| Key               | Value                                                                             |
| ----------------- | --------------------------------------------------------------------------------- |
| **Name**          | documentation                                                                     |
| **Kind**          | `URL`                                                                             |
| **Description**   | Link to a documentation associated with this object, can be internal or external. |
| **Optional**      | True                                                                              |
| **Default Value** |                                                                                   |
| **Constraints**   |                                                                                   |

### generate\_profile[​](#generate_profile "Direct link to generate_profile")

| Key               | Value                                                            |
| ----------------- | ---------------------------------------------------------------- |
| **Name**          | generate\_profile                                                |
| **Kind**          | `Boolean`                                                        |
| **Description**   | Indicate if a profile schema should be generated for this schema |
| **Optional**      | True                                                             |
| **Default Value** | True                                                             |
| **Constraints**   |                                                                  |

### hierarchical[​](#hierarchical "Direct link to hierarchical")

| Key               | Value                                                 |
| ----------------- | ----------------------------------------------------- |
| **Name**          | hierarchical                                          |
| **Kind**          | `Boolean`                                             |
| **Description**   | Defines if the Generic support the hierarchical mode. |
| **Optional**      | True                                                  |
| **Default Value** | False                                                 |
| **Constraints**   |                                                       |

### human\_friendly\_id[​](#human_friendly_id "Direct link to human_friendly_id")

| Key               | Value                                                |
| ----------------- | ---------------------------------------------------- |
| **Name**          | human\_friendly\_id                                  |
| **Kind**          | `List`                                               |
| **Description**   | Human friendly and unique identifier for the object. |
| **Optional**      | True                                                 |
| **Default Value** |                                                      |
| **Constraints**   |                                                      |

### icon[​](#icon "Direct link to icon")

| Key               | Value                                                                                                                   |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **Name**          | icon                                                                                                                    |
| **Kind**          | `Text`                                                                                                                  |
| **Description**   | Defines the icon to use in the menu. Must be a valid value from the MDI library <https://icon-sets.iconify.design/mdi/> |
| **Optional**      | True                                                                                                                    |
| **Default Value** |                                                                                                                         |
| **Constraints**   |                                                                                                                         |

### include\_in\_menu[​](#include_in_menu "Direct link to include_in_menu")

| Key               | Value                                                           |
| ----------------- | --------------------------------------------------------------- |
| **Name**          | include\_in\_menu                                               |
| **Kind**          | `Boolean`                                                       |
| **Description**   | Defines if objects of this kind should be included in the menu. |
| **Optional**      | True                                                            |
| **Default Value** | True                                                            |
| **Constraints**   |                                                                 |

### label[​](#label "Direct link to label")

| Key               | Value                                          |
| ----------------- | ---------------------------------------------- |
| **Name**          | label                                          |
| **Kind**          | `Text`                                         |
| **Description**   | Human friendly representation of the name/kind |
| **Optional**      | True                                           |
| **Default Value** |                                                |
| **Constraints**   | Length: min -, max 64                          |

### menu\_placement[​](#menu_placement "Direct link to menu_placement")

| Key               | Value                                                   |
| ----------------- | ------------------------------------------------------- |
| **Name**          | menu\_placement                                         |
| **Kind**          | `Text`                                                  |
| **Description**   | Defines where in the menu this object should be placed. |
| **Optional**      | True                                                    |
| **Default Value** |                                                         |
| **Constraints**   |                                                         |

### name[​](#name "Direct link to name")

| Key               | Value                                                                                 |
| ----------------- | ------------------------------------------------------------------------------------- |
| **Name**          | name                                                                                  |
| **Kind**          | `Text`                                                                                |
| **Description**   | Node name, must be unique within a namespace and must start with an uppercase letter. |
| **Optional**      | False                                                                                 |
| **Default Value** |                                                                                       |
| **Constraints**   | Regex: `^[A-Z][a-zA-Z0-9]+$`<br />Length: min 2, max 32                               |

### namespace[​](#namespace "Direct link to namespace")

| Key               | Value                                                                                                      |
| ----------------- | ---------------------------------------------------------------------------------------------------------- |
| **Name**          | namespace                                                                                                  |
| **Kind**          | `Text`                                                                                                     |
| **Description**   | Node Namespace, Namespaces are used to organize models into logical groups and to prevent name collisions. |
| **Optional**      | False                                                                                                      |
| **Default Value** |                                                                                                            |
| **Constraints**   | Regex: `^[A-Z][a-z0-9]+$`<br />Length: min 3, max 64                                                       |

### order\_by[​](#order_by "Direct link to order_by")

| Key               | Value                                                     |
| ----------------- | --------------------------------------------------------- |
| **Name**          | order\_by                                                 |
| **Kind**          | `List`                                                    |
| **Description**   | List of attributes to use to order the results by default |
| **Optional**      | True                                                      |
| **Default Value** |                                                           |
| **Constraints**   |                                                           |

### state[​](#state "Direct link to state")

| Key                 | Value                                                       |
| ------------------- | ----------------------------------------------------------- |
| **Name**            | state                                                       |
| **Kind**            | `Text`                                                      |
| **Description**     | Expected state of the node/generic after loading the schema |
| **Optional**        | True                                                        |
| **Default Value**   | present                                                     |
| **Constraints**     |                                                             |
| **Accepted Values** | `present` `absent`                                          |

### uniqueness\_constraints[​](#uniqueness_constraints "Direct link to uniqueness_constraints")

| Key               | Value                                                                                      |
| ----------------- | ------------------------------------------------------------------------------------------ |
| **Name**          | uniqueness\_constraints                                                                    |
| **Kind**          | `List`                                                                                     |
| **Description**   | List of multi-element uniqueness constraints that can combine relationships and attributes |
| **Optional**      | True                                                                                       |
| **Default Value** |                                                                                            |
| **Constraints**   |                                                                                            |

### used\_by[​](#used_by "Direct link to used_by")

| Key               | Value                                           |
| ----------------- | ----------------------------------------------- |
| **Name**          | used\_by                                        |
| **Kind**          | `List`                                          |
| **Description**   | List of Nodes that are referencing this Generic |
| **Optional**      | True                                            |
| **Default Value** |                                                 |
| **Constraints**   |                                                 |

## attributes[​](#attributes "Direct link to attributes")

| Key             | Value      |
| --------------- | ---------- |
| **Name**        | attributes |
| **Kind**        | `List`     |
| **Description** |            |

## relationships[​](#relationships "Direct link to relationships")

| Key             | Value         |
| --------------- | ------------- |
| **Name**        | relationships |
| **Kind**        | `List`        |
| **Description** |               |
