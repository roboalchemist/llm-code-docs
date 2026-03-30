# Source: https://docs.infrahub.app/python-sdk/sdk_ref/infrahub_sdk/node/related_node.md

# `infrahub_sdk.node.related_node`

## Classes[​](#classes "Direct link to Classes")

### `RelatedNodeBase`[​](#relatednodebase "Direct link to relatednodebase")

Base class for representing a related node in a relationship.

**Methods:**

#### `id`[​](#id "Direct link to id")

```
id(self) -> str | None
```

#### `hfid`[​](#hfid "Direct link to hfid")

```
hfid(self) -> list[Any] | None
```

#### `hfid_str`[​](#hfid_str "Direct link to hfid_str")

```
hfid_str(self) -> str | None
```

#### `is_resource_pool`[​](#is_resource_pool "Direct link to is_resource_pool")

```
is_resource_pool(self) -> bool
```

#### `initialized`[​](#initialized "Direct link to initialized")

```
initialized(self) -> bool
```

#### `display_label`[​](#display_label "Direct link to display_label")

```
display_label(self) -> str | None
```

#### `typename`[​](#typename "Direct link to typename")

```
typename(self) -> str | None
```

#### `kind`[​](#kind "Direct link to kind")

```
kind(self) -> str | None
```

#### `is_from_profile`[​](#is_from_profile "Direct link to is_from_profile")

```
is_from_profile(self) -> bool
```

Return whether this relationship was set from a profile. Done by checking if the source is of a profile kind.

#### `get_relationship_metadata`[​](#get_relationship_metadata "Direct link to get_relationship_metadata")

```
get_relationship_metadata(self) -> RelationshipMetadata | None
```

Returns the relationship metadata (updated\_at, updated\_by) if fetched.

### `RelatedNode`[​](#relatednode "Direct link to relatednode")

Represents a RelatedNodeBase in an asynchronous context.

**Methods:**

#### `fetch`[​](#fetch "Direct link to fetch")

```
fetch(self, timeout: int | None = None) -> None
```

#### `peer`[​](#peer "Direct link to peer")

```
peer(self) -> InfrahubNode
```

#### `get`[​](#get "Direct link to get")

```
get(self) -> InfrahubNode
```

### `RelatedNodeSync`[​](#relatednodesync "Direct link to relatednodesync")

Represents a related node in a synchronous context.

**Methods:**

#### `fetch`[​](#fetch-1 "Direct link to fetch-1")

```
fetch(self, timeout: int | None = None) -> None
```

#### `peer`[​](#peer-1 "Direct link to peer-1")

```
peer(self) -> InfrahubNodeSync
```

#### `get`[​](#get-1 "Direct link to get-1")

```
get(self) -> InfrahubNodeSync
```
