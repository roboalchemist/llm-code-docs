# Source: https://docs.infrahub.app/reference/schema/node-extension.md

# Node Extension

Below is the list of all available options to define a node extension in the schema

## Summary[​](#summary "Direct link to Summary")

Below is the list of all available options to define a Node in the schema

| Name                                | Type         | Description                              | Mandatory |
| ----------------------------------- | ------------ | ---------------------------------------- | --------- |
| [**kind**](#kind)                   | Attribute    | Node to extend.                          | True      |
| [**attributes**](#attributes)       | Relationship | List of Attribute to add to the Node.    | True      |
| [**relationships**](#relationships) | Relationship | List of Relationship to add to the Node. | True      |

## Reference Guide[​](#reference-guide "Direct link to Reference Guide")

### kind[​](#kind "Direct link to kind")

| Key             | Value                                                        |
| --------------- | ------------------------------------------------------------ |
| **Name**        | kind                                                         |
| **Kind**        | `Text`                                                       |
| **Description** | Node kind, must exist in the schema and must be in CamelCase |
| **Optional**    | False                                                        |
| **Constraints** | Regex: `^[A-Z][a-zA-Z0-9]+$`<br />Length: min 2, max 32      |

### attributes[​](#attributes "Direct link to attributes")

| Key             | Value                                 |
| --------------- | ------------------------------------- |
| **Name**        | attributes                            |
| **Kind**        | `List`                                |
| **Description** | List of Attribute to add to the Node. |

### relationships[​](#relationships "Direct link to relationships")

| Key             | Value                                    |
| --------------- | ---------------------------------------- |
| **Name**        | relationships                            |
| **Kind**        | `List`                                   |
| **Description** | List of Relationship to add to the Node. |
