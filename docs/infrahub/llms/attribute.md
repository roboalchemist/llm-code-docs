# Source: https://docs.infrahub.app/reference/schema/attribute.md

# Source: https://docs.infrahub.app/python-sdk/sdk_ref/infrahub_sdk/node/attribute.md

# `infrahub_sdk.node.attribute`

## Classes[​](#classes "Direct link to Classes")

### `Attribute`[​](#attribute "Direct link to attribute")

Represents an attribute of a Node, including its schema, value, and properties.

**Methods:**

#### `value`[​](#value "Direct link to value")

```
value(self) -> Any
```

#### `value`[​](#value-1 "Direct link to value-1")

```
value(self, value: Any) -> None
```

#### `is_from_pool_attribute`[​](#is_from_pool_attribute "Direct link to is_from_pool_attribute")

```
is_from_pool_attribute(self) -> bool
```

Check whether this attribute's value is sourced from a resource pool.

**Returns:**

* True if the attribute value is a resource pool node or was explicitly allocated from a pool.
