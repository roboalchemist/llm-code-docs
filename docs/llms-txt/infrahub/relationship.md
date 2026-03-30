# Source: https://docs.infrahub.app/reference/schema/relationship.md

# Source: https://docs.infrahub.app/python-sdk/sdk_ref/infrahub_sdk/node/relationship.md

# `infrahub_sdk.node.relationship`

## Classes[​](#classes "Direct link to Classes")

### `RelationshipManagerBase`[​](#relationshipmanagerbase "Direct link to relationshipmanagerbase")

Base class for RelationshipManager and RelationshipManagerSync

**Methods:**

#### `peer_ids`[​](#peer_ids "Direct link to peer_ids")

```
peer_ids(self) -> list[str]
```

#### `peer_hfids`[​](#peer_hfids "Direct link to peer_hfids")

```
peer_hfids(self) -> list[list[Any]]
```

#### `peer_hfids_str`[​](#peer_hfids_str "Direct link to peer_hfids_str")

```
peer_hfids_str(self) -> list[str]
```

#### `has_update`[​](#has_update "Direct link to has_update")

```
has_update(self) -> bool
```

#### `is_from_profile`[​](#is_from_profile "Direct link to is_from_profile")

```
is_from_profile(self) -> bool
```

Return whether this relationship was set from a profile. All its peers must be from a profile.

### `RelationshipManager`[​](#relationshipmanager "Direct link to relationshipmanager")

Manages relationships of a node in an asynchronous context.

**Methods:**

#### `fetch`[​](#fetch "Direct link to fetch")

```
fetch(self) -> None
```

#### `add`[​](#add "Direct link to add")

```
add(self, data: str | RelatedNode | dict) -> None
```

Add a new peer to this relationship.

#### `extend`[​](#extend "Direct link to extend")

```
extend(self, data: Iterable[str | RelatedNode | dict]) -> None
```

Add new peers to this relationship.

#### `remove`[​](#remove "Direct link to remove")

```
remove(self, data: str | RelatedNode | dict) -> None
```

### `RelationshipManagerSync`[​](#relationshipmanagersync "Direct link to relationshipmanagersync")

Manages relationships of a node in a synchronous context.

**Methods:**

#### `fetch`[​](#fetch-1 "Direct link to fetch-1")

```
fetch(self) -> None
```

#### `add`[​](#add-1 "Direct link to add-1")

```
add(self, data: str | RelatedNodeSync | dict) -> None
```

Add a new peer to this relationship.

#### `extend`[​](#extend-1 "Direct link to extend-1")

```
extend(self, data: Iterable[str | RelatedNodeSync | dict]) -> None
```

Add new peers to this relationship.

#### `remove`[​](#remove-1 "Direct link to remove-1")

```
remove(self, data: str | RelatedNodeSync | dict) -> None
```
