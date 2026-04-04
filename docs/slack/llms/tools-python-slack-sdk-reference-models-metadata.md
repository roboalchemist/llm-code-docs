Source: https://docs.slack.dev/tools/python-slack-sdk/reference/models/metadata

# Module slack_sdk.models.metadata

## Global variables

`var EntityType`

Custom field types

## Classes

`class ContentItemEntityFields (preview: Dict[str, Any] | [EntityImageField](#slack_sdk.models.metadata.EntityImageField "slack_sdk.models.metadata.EntityImageField") | None = None,   description: Dict[str, Any] | [EntityStringField](#slack_sdk.models.metadata.EntityStringField "slack_sdk.models.metadata.EntityStringField") | None = None,   created_by: Dict[str, Any] | [EntityTypedField](#slack_sdk.models.metadata.EntityTypedField "slack_sdk.models.metadata.EntityTypedField") | None = None,   date_created: Dict[str, Any] | [EntityTimestampField](#slack_sdk.models.metadata.EntityTimestampField "slack_sdk.models.metadata.EntityTimestampField") | None = None,   date_updated: Dict[str, Any] | [EntityTimestampField](#slack_sdk.models.metadata.EntityTimestampField "slack_sdk.models.metadata.EntityTimestampField") | None = None,   last_modified_by: Dict[str, Any] | [EntityTypedField](#slack_sdk.models.metadata.EntityTypedField "slack_sdk.models.metadata.EntityTypedField") | None = None,   **kwargs)`

Expand source code

```typescript
class ContentItemEntityFields(JsonObject):
    """Fields specific to content item entities"""

    attributes = {
        "preview",
        "description",
        "created_by",
        "date_created",
        "date_updated",
        "last_modified_by",
    }

    def __init__(
        self,
        preview: Optional[Union[Dict[str, Any], EntityImageField]] = None,
        description: Optional[Union[Dict[str, Any], EntityStringField]] = None,
        created_by: Optional[Union[Dict[str, Any], EntityTypedField]] = None,
        date_created: Optional[Union[Dict[str, Any], EntityTimestampField]] = None,
        date_updated: Optional[Union[Dict[str, Any], EntityTimestampField]] = None,
        last_modified_by: Optional[Union[Dict[str, Any], EntityTypedField]] = None,
        **kwargs,
    ):
        self.preview = preview
        self.description = description
        self.created_by = created_by
        self.date_created = date_created
        self.date_updated = date_updated
        self.last_modified_by = last_modified_by
        self.additional_attributes = kwargs

    def __str__(self):
        return str(self.get_non_null_attributes())

    def __repr__(self):
        return self.__str__()
```

Fields specific to content item entities

### Ancestors

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables

`var attributes`

The type of the None singleton.

### Inherited members

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class EntityActionButton (text: str,   action_id: str,   value: str | None = None,   style: str | None = None,   url: str | None = None,   accessibility_label: str | None = None,   processing_state: Dict[str, Any] | [EntityActionProcessingState](#slack_sdk.models.metadata.EntityActionProcessingState "slack_sdk.models.metadata.EntityActionProcessingState") | None = None,   **kwargs)`

Expand source code

```typescript
class EntityActionButton(JsonObject):
    """Action button for entity"""

    attributes = {
        "text",
        "action_id",
        "value",
        "style",
        "url",
        "accessibility_label",
        "processing_state",
    }

    def __init__(
        self,
        text: str,
        action_id: str,
        value: Optional[str] = None,
        style: Optional[str] = None,
        url: Optional[str] = None,
        accessibility_label: Optional[str] = None,
        processing_state: Optional[Union[Dict[str, Any], EntityActionProcessingState]] = None,
        **kwargs,
    ):
        self.text = text
        self.action_id = action_id
        self.value = value
        self.style = style
        self.url = url
        self.accessibility_label = accessibility_label
        self.processing_state = processing_state
        self.additional_attributes = kwargs

    def __str__(self):
        return str(self.get_non_null_attributes())

    def __repr__(self):
        return self.__str__()
```

Action button for entity

### Ancestors (2)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (2)

`var attributes`

The type of the None singleton.

### Inherited members (2)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class EntityActionProcessingState (enabled: bool, interstitial_text: str | None = None, **kwargs)`

Expand source code

```typescript
class EntityActionProcessingState(JsonObject):
    """Processing state configuration for entity action button"""

    attributes = {
        "enabled",
        "interstitial_text",
    }

    def __init__(
        self,
        enabled: bool,
        interstitial_text: Optional[str] = None,
        **kwargs,
    ):
        self.enabled = enabled
        self.interstitial_text = interstitial_text
        self.additional_attributes = kwargs

    def __str__(self):
        return str(self.get_non_null_attributes())

    def __repr__(self):
        return self.__str__()
```

Processing state configuration for entity action button

### Ancestors (3)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (3)

`var attributes`

The type of the None singleton.

### Inherited members (3)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class EntityActions (primary_actions: List[Dict[str, Any] | [EntityActionButton](#slack_sdk.models.metadata.EntityActionButton "slack_sdk.models.metadata.EntityActionButton")] | None = None,   overflow_actions: List[Dict[str, Any] | [EntityActionButton](#slack_sdk.models.metadata.EntityActionButton "slack_sdk.models.metadata.EntityActionButton")] | None = None,   **kwargs)`

Expand source code

```typescript
class EntityActions(JsonObject):
    """Actions configuration for entity"""

    attributes = {
        "primary_actions",
        "overflow_actions",
    }

    def __init__(
        self,
        primary_actions: Optional[List[Union[Dict[str, Any], EntityActionButton]]] = None,
        overflow_actions: Optional[List[Union[Dict[str, Any], EntityActionButton]]] = None,
        **kwargs,
    ):
        self.primary_actions = primary_actions
        self.overflow_actions = overflow_actions
        self.additional_attributes = kwargs

    def __str__(self):
        return str(self.get_non_null_attributes())

    def __repr__(self):
        return self.__str__()
```

Actions configuration for entity

### Ancestors (4)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (4)

`var attributes`

The type of the None singleton.

### Inherited members (4)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class EntityArrayItemField (type: str | None = None,   label: str | None = None,   value: str | int | None = None,   link: str | None = None,   icon: Dict[str, Any] | [EntityIconField](#slack_sdk.models.metadata.EntityIconField "slack_sdk.models.metadata.EntityIconField") | None = None,   long: bool | None = None,   format: str | None = None,   image_url: str | None = None,   slack_file: Dict[str, Any] | None = None,   alt_text: str | None = None,   edit: Dict[str, Any] | [EntityEditSupport](#slack_sdk.models.metadata.EntityEditSupport "slack_sdk.models.metadata.EntityEditSupport") | None = None,   tag_color: str | None = None,   user: Dict[str, Any] | [EntityUserIDField](#slack_sdk.models.metadata.EntityUserIDField "slack_sdk.models.metadata.EntityUserIDField") | [EntityUserField](#slack_sdk.models.metadata.EntityUserField "slack_sdk.models.metadata.EntityUserField") | None = None,   entity_ref: Dict[str, Any] | [EntityRefField](#slack_sdk.models.metadata.EntityRefField "slack_sdk.models.metadata.EntityRefField") | None = None,   **kwargs)`

Expand source code

```typescript
class EntityArrayItemField(JsonObject):
    """Array item field for entity (similar to EntityTypedField but with optional type)"""

    attributes = {
        "type",
        "label",
        "value",
        "link",
        "icon",
        "long",
        "format",
        "image_url",
        "slack_file",
        "alt_text",
        "edit",
        "tag_color",
        "user",
        "entity_ref",
    }

    def __init__(
        self,
        type: Optional[str] = None,
        label: Optional[str] = None,
        value: Optional[Union[str, int]] = None,
        link: Optional[str] = None,
        icon: Optional[Union[Dict[str, Any], EntityIconField]] = None,
        long: Optional[bool] = None,
        format: Optional[str] = None,
        image_url: Optional[str] = None,
        slack_file: Optional[Dict[str, Any]] = None,
        alt_text: Optional[str] = None,
        edit: Optional[Union[Dict[str, Any], EntityEditSupport]] = None,
        tag_color: Optional[str] = None,
        user: Optional[Union[Dict[str, Any], EntityUserIDField, EntityUserField]] = None,
        entity_ref: Optional[Union[Dict[str, Any], EntityRefField]] = None,
        **kwargs,
    ):
        self.type = type
        self.label = label
        self.value = value
        self.link = link
        self.icon = icon
        self.long = long
        self.format = format
        self.image_url = image_url
        self.slack_file = slack_file
        self.alt_text = alt_text
        self.edit = edit
        self.tag_color = tag_color
        self.user = user
        self.entity_ref = entity_ref
        self.additional_attributes = kwargs

    def __str__(self):
        return str(self.get_non_null_attributes())

    def __repr__(self):
        return self.__str__()
```

Array item field for entity (similar to EntityTypedField but with optional type)

### Ancestors (5)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (5)

`var attributes`

The type of the None singleton.

### Inherited members (5)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class EntityAttributes (title: Dict[str, Any] | [EntityTitle](#slack_sdk.models.metadata.EntityTitle "slack_sdk.models.metadata.EntityTitle"),   display_type: str | None = None,   display_id: str | None = None,   product_icon: Dict[str, Any] | [EntityIconField](#slack_sdk.models.metadata.EntityIconField "slack_sdk.models.metadata.EntityIconField") | None = None,   product_name: str | None = None,   locale: str | None = None,   full_size_preview: Dict[str, Any] | [EntityFullSizePreview](#slack_sdk.models.metadata.EntityFullSizePreview "slack_sdk.models.metadata.EntityFullSizePreview") | None = None,   metadata_last_modified: int | None = None,   **kwargs)`

Expand source code

```typescript
class EntityAttributes(JsonObject):
    """Attributes for an entity"""

    attributes = {
        "title",
        "display_type",
        "display_id",
        "product_icon",
        "product_name",
        "locale",
        "full_size_preview",
        "metadata_last_modified",
    }

    def __init__(
        self,
        title: Union[Dict[str, Any], EntityTitle],
        display_type: Optional[str] = None,
        display_id: Optional[str] = None,
        product_icon: Optional[Union[Dict[str, Any], EntityIconField]] = None,
        product_name: Optional[str] = None,
        locale: Optional[str] = None,
        full_size_preview: Optional[Union[Dict[str, Any], EntityFullSizePreview]] = None,
        metadata_last_modified: Optional[int] = None,
        **kwargs,
    ):
        self.title = title
        self.display_type = display_type
        self.display_id = display_id
        self.product_icon = product_icon
        self.product_name = product_name
        self.locale = locale
        self.full_size_preview = full_size_preview
        self.metadata_last_modified = metadata_last_modified
        self.additional_attributes = kwargs

    def __str__(self):
        return str(self.get_non_null_attributes())

    def __repr__(self):
        return self.__str__()
```

Attributes for an entity

### Ancestors (6)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (6)

`var attributes`

The type of the None singleton.

### Inherited members (6)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class EntityBooleanCheckboxField (type: str, text: str, description: str | None, **kwargs)`

Expand source code

```typescript
class EntityBooleanCheckboxField(JsonObject):
    """Boolean checkbox properties"""

    attributes = {"type", "text", "description"}

    def __init__(
        self,
        type: str,
        text: str,
        description: Optional[str],
        **kwargs,
    ):
        self.type = type
        self.text = text
        self.description = description
        self.additional_attributes = kwargs

    def __str__(self):
        return str(self.get_non_null_attributes())

    def __repr__(self):
        return self.__str__()
```

Boolean checkbox properties

### Ancestors (7)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (7)

`var attributes`

The type of the None singleton.

### Inherited members (7)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class EntityBooleanTextField (type: str,   true_text: str,   false_text: str,   true_description: str | None,   false_description: str | None,   **kwargs)`

Expand source code

```typescript
class EntityBooleanTextField(JsonObject):
    """Boolean text properties"""

    attributes = {"type", "true_text", "false_text", "true_description", "false_description"}

    def __init__(
        self,
        type: str,
        true_text: str,
        false_text: str,
        true_description: Optional[str],
        false_description: Optional[str],
        **kwargs,
    ):
        self.type = type
        self.true_text = (true_text,)
        self.false_text = (false_text,)
        self.true_description = (true_description,)
        self.false_description = (false_description,)
        self.additional_attributes = kwargs

    def __str__(self):
        return str(self.get_non_null_attributes())

    def __repr__(self):
        return self.__str__()
```

Boolean text properties

### Ancestors (8)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (8)

`var attributes`

The type of the None singleton.

### Inherited members (8)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class EntityCustomField (label: str,   key: str,   type: str,   value: str | int | List[Dict[str, Any] | [EntityArrayItemField](#slack_sdk.models.metadata.EntityArrayItemField "slack_sdk.models.metadata.EntityArrayItemField")] | None = None,   link: str | None = None,   icon: Dict[str, Any] | [EntityIconField](#slack_sdk.models.metadata.EntityIconField "slack_sdk.models.metadata.EntityIconField") | None = None,   long: bool | None = None,   format: str | None = None,   image_url: str | None = None,   slack_file: Dict[str, Any] | None = None,   alt_text: str | None = None,   tag_color: str | None = None,   edit: Dict[str, Any] | [EntityEditSupport](#slack_sdk.models.metadata.EntityEditSupport "slack_sdk.models.metadata.EntityEditSupport") | None = None,   item_type: str | None = None,   user: Dict[str, Any] | [EntityUserIDField](#slack_sdk.models.metadata.EntityUserIDField "slack_sdk.models.metadata.EntityUserIDField") | [EntityUserField](#slack_sdk.models.metadata.EntityUserField "slack_sdk.models.metadata.EntityUserField") | None = None,   entity_ref: Dict[str, Any] | [EntityRefField](#slack_sdk.models.metadata.EntityRefField "slack_sdk.models.metadata.EntityRefField") | None = None,   boolean: Dict[str, Any] | [EntityBooleanCheckboxField](#slack_sdk.models.metadata.EntityBooleanCheckboxField "slack_sdk.models.metadata.EntityBooleanCheckboxField") | [EntityBooleanTextField](#slack_sdk.models.metadata.EntityBooleanTextField "slack_sdk.models.metadata.EntityBooleanTextField") | None = None,   **kwargs)`

Expand source code

```typescript
class EntityCustomField(JsonObject):
    """Custom field for entity with flexible types"""

    attributes = {
        "label",
        "key",
        "type",
        "value",
        "link",
        "icon",
        "long",
        "format",
        "image_url",
        "slack_file",
        "alt_text",
        "tag_color",
        "edit",
        "item_type",
        "user",
        "entity_ref",
        "boolean",
    }

    def __init__(
        self,
        label: str,
        key: str,
        type: str,
        value: Optional[Union[str, int, List[Union[Dict[str, Any], EntityArrayItemField]]]] = None,
        link: Optional[str] = None,
        icon: Optional[Union[Dict[str, Any], EntityIconField]] = None,
        long: Optional[bool] = None,
        format: Optional[str] = None,
        image_url: Optional[str] = None,
        slack_file: Optional[Dict[str, Any]] = None,
        alt_text: Optional[str] = None,
        tag_color: Optional[str] = None,
        edit: Optional[Union[Dict[str, Any], EntityEditSupport]] = None,
        item_type: Optional[str] = None,
        user: Optional[Union[Dict[str, Any], EntityUserIDField, EntityUserField]] = None,
        entity_ref: Optional[Union[Dict[str, Any], EntityRefField]] = None,
        boolean: Optional[Union[Dict[str, Any], EntityBooleanCheckboxField, EntityBooleanTextField]] = None,
        **kwargs,
    ):
        self.label = label
        self.key = key
        self.type = type
        self.value = value
        self.link = link
        self.icon = icon
        self.long = long
        self.format = format
        self.image_url = image_url
        self.slack_file = slack_file
        self.alt_text = alt_text
        self.tag_color = tag_color
        self.edit = edit
        self.item_type = item_type
        self.user = user
        self.entity_ref = entity_ref
        self.boolean = boolean
        self.additional_attributes = kwargs

    def __str__(self):
        return str(self.get_non_null_attributes())

    def __repr__(self):
        return self.__str__()

    @EnumValidator("type", CustomFieldType)
    def type_valid(self):
        return self.type is None or self.type in CustomFieldType
```

Custom field for entity with flexible types

### Ancestors (9)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (9)

`var attributes`

The type of the None singleton.

### Methods

`def type_valid(self)`

Expand source code

```typescript
@EnumValidator("type", CustomFieldType)
def type_valid(self):
    return self.type is None or self.type in CustomFieldType
```

### Inherited members (9)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class EntityEditNumberConfig (is_decimal_allowed: bool | None = None,   min_value: int | float | None = None,   max_value: int | float | None = None,   **kwargs)`

Expand source code

```typescript
class EntityEditNumberConfig(JsonObject):
    """Number configuration for entity edit support"""

    attributes = {
        "is_decimal_allowed",
        "min_value",
        "max_value",
    }

    def __init__(
        self,
        is_decimal_allowed: Optional[bool] = None,
        min_value: Optional[Union[int, float]] = None,
        max_value: Optional[Union[int, float]] = None,
        **kwargs,
    ):
        self.is_decimal_allowed = is_decimal_allowed
        self.min_value = min_value
        self.max_value = max_value
        self.additional_attributes = kwargs

    def __str__(self):
        return str(self.get_non_null_attributes())

    def __repr__(self):
        return self.__str__()
```

Number configuration for entity edit support

### Ancestors (10)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (10)

`var attributes`

The type of the None singleton.

### Inherited members (10)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class EntityEditSelectConfig (current_value: str | None = None,   current_values: List[str] | None = None,   static_options: List[Dict[str, Any]] | None = None,   fetch_options_dynamically: bool | None = None,   min_query_length: int | None = None,   **kwargs)`

Expand source code

```typescript
class EntityEditSelectConfig(JsonObject):
    """Select configuration for entity edit support"""

    attributes = {
        "current_value",
        "current_values",
        "static_options",
        "fetch_options_dynamically",
        "min_query_length",
    }

    def __init__(
        self,
        current_value: Optional[str] = None,
        current_values: Optional[List[str]] = None,
        static_options: Optional[List[Dict[str, Any]]] = None,  # Option[]
        fetch_options_dynamically: Optional[bool] = None,
        min_query_length: Optional[int] = None,
        **kwargs,
    ):
        self.current_value = current_value
        self.current_values = current_values
        self.static_options = static_options
        self.fetch_options_dynamically = fetch_options_dynamically
        self.min_query_length = min_query_length
        self.additional_attributes = kwargs

    def __str__(self):
        return str(self.get_non_null_attributes())

    def __repr__(self):
        return self.__str__()
```

Select configuration for entity edit support

### Ancestors (11)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (11)

`var attributes`

The type of the None singleton.

### Inherited members (11)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class EntityEditSupport (enabled: bool,   placeholder: Dict[str, Any] | None = None,   hint: Dict[str, Any] | None = None,   optional: bool | None = None,   select: Dict[str, Any] | [EntityEditSelectConfig](#slack_sdk.models.metadata.EntityEditSelectConfig "slack_sdk.models.metadata.EntityEditSelectConfig") | None = None,   number: Dict[str, Any] | [EntityEditNumberConfig](#slack_sdk.models.metadata.EntityEditNumberConfig "slack_sdk.models.metadata.EntityEditNumberConfig") | None = None,   text: Dict[str, Any] | [EntityEditTextConfig](#slack_sdk.models.metadata.EntityEditTextConfig "slack_sdk.models.metadata.EntityEditTextConfig") | None = None,   **kwargs)`

Expand source code

```typescript
class EntityEditSupport(JsonObject):
    """Edit support configuration for entity fields"""

    attributes = {
        "enabled",
        "placeholder",
        "hint",
        "optional",
        "select",
        "number",
        "text",
    }

    def __init__(
        self,
        enabled: bool,
        placeholder: Optional[Dict[str, Any]] = None,  # PlainTextElement
        hint: Optional[Dict[str, Any]] = None,  # PlainTextElement
        optional: Optional[bool] = None,
        select: Optional[Union[Dict[str, Any], EntityEditSelectConfig]] = None,
        number: Optional[Union[Dict[str, Any], EntityEditNumberConfig]] = None,
        text: Optional[Union[Dict[str, Any], EntityEditTextConfig]] = None,
        **kwargs,
    ):
        self.enabled = enabled
        self.placeholder = placeholder
        self.hint = hint
        self.optional = optional
        self.select = select
        self.number = number
        self.text = text
        self.additional_attributes = kwargs

    def __str__(self):
        return str(self.get_non_null_attributes())

    def __repr__(self):
        return self.__str__()
```

Edit support configuration for entity fields

### Ancestors (12)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (12)

`var attributes`

The type of the None singleton.

### Inherited members (12)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class EntityEditTextConfig (min_length: int | None = None, max_length: int | None = None, **kwargs)`

Expand source code

```typescript
class EntityEditTextConfig(JsonObject):
    """Text configuration for entity edit support"""

    attributes = {
        "min_length",
        "max_length",
    }

    def __init__(
        self,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
        **kwargs,
    ):
        self.min_length = min_length
        self.max_length = max_length
        self.additional_attributes = kwargs

    def __str__(self):
        return str(self.get_non_null_attributes())

    def __repr__(self):
        return self.__str__()
```

Text configuration for entity edit support

### Ancestors (13)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (13)

`var attributes`

The type of the None singleton.

### Inherited members (13)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class EntityFullSizePreview (is_supported: bool,   preview_url: str | None = None,   mime_type: str | None = None,   error: Dict[str, Any] | [EntityFullSizePreviewError](#slack_sdk.models.metadata.EntityFullSizePreviewError "slack_sdk.models.metadata.EntityFullSizePreviewError") | None = None,   **kwargs)`

Expand source code

```typescript
class EntityFullSizePreview(JsonObject):
    """Full-size preview configuration for entity"""

    attributes = {
        "is_supported",
        "preview_url",
        "mime_type",
        "error",
    }

    def __init__(
        self,
        is_supported: bool,
        preview_url: Optional[str] = None,
        mime_type: Optional[str] = None,
        error: Optional[Union[Dict[str, Any], EntityFullSizePreviewError]] = None,
        **kwargs,
    ):
        self.is_supported = is_supported
        self.preview_url = preview_url
        self.mime_type = mime_type
        self.error = error
        self.additional_attributes = kwargs

    def __str__(self):
        return str(self.get_non_null_attributes())

    def __repr__(self):
        return self.__str__()
```

Full-size preview configuration for entity

### Ancestors (14)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (14)

`var attributes`

The type of the None singleton.

### Inherited members (14)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class EntityFullSizePreviewError (code: str, message: str | None = None, **kwargs)`

Expand source code

```typescript
class EntityFullSizePreviewError(JsonObject):
    """Error information for full-size preview"""

    attributes = {
        "code",
        "message",
    }

    def __init__(
        self,
        code: str,
        message: Optional[str] = None,
        **kwargs,
    ):
        self.code = code
        self.message = message
        self.additional_attributes = kwargs

    def __str__(self):
        return str(self.get_non_null_attributes())

    def __repr__(self):
        return self.__str__()
```

Error information for full-size preview

### Ancestors (15)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (15)

`var attributes`

The type of the None singleton.

### Inherited members (15)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class EntityIconField (alt_text: str,   url: str | None = None,   slack_file: Dict[str, Any] | [EntityIconSlackFile](#slack_sdk.models.metadata.EntityIconSlackFile "slack_sdk.models.metadata.EntityIconSlackFile") | None = None,   **kwargs)`

Expand source code

```typescript
class EntityIconField(JsonObject):
    """Icon field for entity attributes"""

    attributes = {
        "alt_text",
        "url",
        "slack_file",
    }

    def __init__(
        self,
        alt_text: str,
        url: Optional[str] = None,
        slack_file: Optional[Union[Dict[str, Any], EntityIconSlackFile]] = None,
        **kwargs,
    ):
        self.alt_text = alt_text
        self.url = url
        self.slack_file = slack_file
        self.additional_attributes = kwargs

    def __str__(self):
        return str(self.get_non_null_attributes())

    def __repr__(self):
        return self.__str__()
```

Icon field for entity attributes

### Ancestors (16)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (16)

`var attributes`

The type of the None singleton.

### Inherited members (16)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class EntityIconSlackFile (id: str | None = None, url: str | None = None, **kwargs)`

Expand source code

```typescript
class EntityIconSlackFile(JsonObject):
    """Slack file reference for entity icon"""

    attributes = {
        "id",
        "url",
    }

    def __init__(
        self,
        id: Optional[str] = None,
        url: Optional[str] = None,
        **kwargs,
    ):
        self.id = id
        self.url = url
        self.additional_attributes = kwargs

    def __str__(self):
        return str(self.get_non_null_attributes())

    def __repr__(self):
        return self.__str__()
```

Slack file reference for entity icon

### Ancestors (17)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (17)

`var attributes`

The type of the None singleton.

### Inherited members (17)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class EntityImageField (alt_text: str,   label: str | None = None,   image_url: str | None = None,   slack_file: Dict[str, Any] | None = None,   title: str | None = None,   type: str | None = None,   **kwargs)`

Expand source code

```typescript
class EntityImageField(JsonObject):
    """Image field for entity"""

    attributes = {
        "alt_text",
        "label",
        "image_url",
        "slack_file",
        "title",
        "type",
    }

    def __init__(
        self,
        alt_text: str,
        label: Optional[str] = None,
        image_url: Optional[str] = None,
        slack_file: Optional[Dict[str, Any]] = None,
        title: Optional[str] = None,
        type: Optional[str] = None,
        **kwargs,
    ):
        self.alt_text = alt_text
        self.label = label
        self.image_url = image_url
        self.slack_file = slack_file
        self.title = title
        self.type = type
        self.additional_attributes = kwargs

    def __str__(self):
        return str(self.get_non_null_attributes())

    def __repr__(self):
        return self.__str__()
```

Image field for entity

### Ancestors (18)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (18)

`var attributes`

The type of the None singleton.

### Inherited members (18)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class EntityMetadata (entity_type: str,   entity_payload: Dict[str, Any] | [EntityPayload](#slack_sdk.models.metadata.EntityPayload "slack_sdk.models.metadata.EntityPayload"),   external_ref: Dict[str, Any] | [ExternalRef](#slack_sdk.models.metadata.ExternalRef "slack_sdk.models.metadata.ExternalRef"),   url: str,   app_unfurl_url: str | None = None,   **kwargs)`

Expand source code

```typescript
class EntityMetadata(JsonObject):
    """Work object entity metadata

    https://docs.slack.dev/messaging/work-objects/
    """

    attributes = {
        "entity_type",
        "entity_payload",
        "external_ref",
        "url",
        "app_unfurl_url",
    }

    def __init__(
        self,
        entity_type: str,
        entity_payload: Union[Dict[str, Any], EntityPayload],
        external_ref: Union[Dict[str, Any], ExternalRef],
        url: str,
        app_unfurl_url: Optional[str] = None,
        **kwargs,
    ):
        self.entity_type = entity_type
        self.entity_payload = entity_payload
        self.external_ref = external_ref
        self.url = url
        self.app_unfurl_url = app_unfurl_url
        self.additional_attributes = kwargs

    def __str__(self):
        return str(self.get_non_null_attributes())

    def __repr__(self):
        return self.__str__()

    @EnumValidator("entity_type", EntityType)
    def entity_type_valid(self):
        return self.entity_type is None or self.entity_type in EntityType
```

Work object entity metadata

[https://docs.slack.dev/messaging/work-objects/](https://docs.slack.dev/messaging/work-objects/)

### Ancestors (19)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (19)

`var attributes`

The type of the None singleton.

### Methods (2)

`def entity_type_valid(self)`

Expand source code

```typescript
@EnumValidator("entity_type", EntityType)
def entity_type_valid(self):
    return self.entity_type is None or self.entity_type in EntityType
```

### Inherited members (19)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class EntityPayload (attributes: Dict[str, Any] | [EntityAttributes](#slack_sdk.models.metadata.EntityAttributes "slack_sdk.models.metadata.EntityAttributes"),   fields: Dict[str, Any] | [ContentItemEntityFields](#slack_sdk.models.metadata.ContentItemEntityFields "slack_sdk.models.metadata.ContentItemEntityFields") | [FileEntityFields](#slack_sdk.models.metadata.FileEntityFields "slack_sdk.models.metadata.FileEntityFields") | [IncidentEntityFields](#slack_sdk.models.metadata.IncidentEntityFields "slack_sdk.models.metadata.IncidentEntityFields") | [TaskEntityFields](#slack_sdk.models.metadata.TaskEntityFields "slack_sdk.models.metadata.TaskEntityFields") | None = None,   custom_fields: List[Dict[str, Any] | [EntityCustomField](#slack_sdk.models.metadata.EntityCustomField "slack_sdk.models.metadata.EntityCustomField")] | None = None,   slack_file: Dict[str, Any] | [FileEntitySlackFile](#slack_sdk.models.metadata.FileEntitySlackFile "slack_sdk.models.metadata.FileEntitySlackFile") | None = None,   display_order: List[str] | None = None,   actions: Dict[str, Any] | [EntityActions](#slack_sdk.models.metadata.EntityActions "slack_sdk.models.metadata.EntityActions") | None = None,   **kwargs)`

Expand source code

```typescript
class EntityPayload(JsonObject):
    """Payload schema for an entity"""

    attributes = {
        "attributes",
        "fields",
        "custom_fields",
        "slack_file",
        "display_order",
        "actions",
    }

    def __init__(
        self,
        attributes: Union[Dict[str, Any], EntityAttributes],
        fields: Optional[
            Union[Dict[str, Any], ContentItemEntityFields, FileEntityFields, IncidentEntityFields, TaskEntityFields]
        ] = None,
        custom_fields: Optional[List[Union[Dict[str, Any], EntityCustomField]]] = None,
        slack_file: Optional[Union[Dict[str, Any], FileEntitySlackFile]] = None,
        display_order: Optional[List[str]] = None,
        actions: Optional[Union[Dict[str, Any], EntityActions]] = None,
        **kwargs,
    ):
        # Store entity attributes data with a different internal name to avoid
        # shadowing the class-level 'attributes' set used for JSON serialization
        self._entity_attributes = attributes
        self.fields = fields
        self.custom_fields = custom_fields
        self.slack_file = slack_file
        self.display_order = display_order
        self.actions = actions
        self.additional_attributes = kwargs

    @property
    def entity_attributes(self) -> Union[Dict[str, Any], EntityAttributes]:
        """Get the entity attributes data.

        Note: Use this property to access the attributes data. The class-level
        'attributes' is reserved for the JSON serialization schema.
        """
        return self._entity_attributes

    @entity_attributes.setter
    def entity_attributes(self, value: Union[Dict[str, Any], EntityAttributes]):
        """Set the entity attributes data."""
        self._entity_attributes = value

    def get_object_attribute(self, key: str):
        if key == "attributes":
            return self._entity_attributes
        else:
            return getattr(self, key, None)

    def __str__(self):
        return str(self.get_non_null_attributes())

    def __repr__(self):
        return self.__str__()
```

Payload schema for an entity

### Ancestors (20)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (20)

`var attributes`

The type of the None singleton.

### Instance variables

`prop entity_attributes : Dict[str, Any] | [EntityAttributes](#slack_sdk.models.metadata.EntityAttributes "slack_sdk.models.metadata.EntityAttributes")`

Expand source code

```python
@property
def entity_attributes(self) -> Union[Dict[str, Any], EntityAttributes]:
    """Get the entity attributes data.

    Note: Use this property to access the attributes data. The class-level
    'attributes' is reserved for the JSON serialization schema.
    """
    return self._entity_attributes
```

Get the entity attributes data.

Note: Use this property to access the attributes data. The class-level 'attributes' is reserved for the JSON serialization schema.

### Methods (3)

`def get_object_attribute(self, key: str)`

Expand source code

```python
def get_object_attribute(self, key: str):
    if key == "attributes":
        return self._entity_attributes
    else:
        return getattr(self, key, None)
```

### Inherited members (20)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class EntityRefField (entity_url: str,   external_ref: Dict[str, Any] | [ExternalRef](#slack_sdk.models.metadata.ExternalRef "slack_sdk.models.metadata.ExternalRef"),   title: str,   display_type: str | None = None,   icon: Dict[str, Any] | [EntityIconField](#slack_sdk.models.metadata.EntityIconField "slack_sdk.models.metadata.EntityIconField") | None = None,   **kwargs)`

Expand source code

```typescript
class EntityRefField(JsonObject):
    """Entity reference field"""

    attributes = {
        "entity_url",
        "external_ref",
        "title",
        "display_type",
        "icon",
    }

    def __init__(
        self,
        entity_url: str,
        external_ref: Union[Dict[str, Any], ExternalRef],
        title: str,
        display_type: Optional[str] = None,
        icon: Optional[Union[Dict[str, Any], EntityIconField]] = None,
        **kwargs,
    ):
        self.entity_url = entity_url
        self.external_ref = external_ref
        self.title = title
        self.display_type = display_type
        self.icon = icon
        self.additional_attributes = kwargs

    def __str__(self):
        return str(self.get_non_null_attributes())

    def __repr__(self):
        return self.__str__()
```

Entity reference field

### Ancestors (21)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (21)

`var attributes`

The type of the None singleton.

### Inherited members (21)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class EntityStringField (value: str,   label: str | None = None,   format: str | None = None,   link: str | None = None,   icon: Dict[str, Any] | [EntityIconField](#slack_sdk.models.metadata.EntityIconField "slack_sdk.models.metadata.EntityIconField") | None = None,   long: bool | None = None,   type: str | None = None,   tag_color: str | None = None,   edit: Dict[str, Any] | [EntityEditSupport](#slack_sdk.models.metadata.EntityEditSupport "slack_sdk.models.metadata.EntityEditSupport") | None = None,   **kwargs)`

Expand source code

```typescript
class EntityStringField(JsonObject):
    """String field for entity"""

    attributes = {
        "value",
        "label",
        "format",
        "link",
        "icon",
        "long",
        "type",
        "tag_color",
        "edit",
    }

    def __init__(
        self,
        value: str,
        label: Optional[str] = None,
        format: Optional[str] = None,
        link: Optional[str] = None,
        icon: Optional[Union[Dict[str, Any], EntityIconField]] = None,
        long: Optional[bool] = None,
        type: Optional[str] = None,
        tag_color: Optional[str] = None,
        edit: Optional[Union[Dict[str, Any], EntityEditSupport]] = None,
        **kwargs,
    ):
        self.value = value
        self.label = label
        self.format = format
        self.link = link
        self.icon = icon
        self.long = long
        self.type = type
        self.tag_color = tag_color
        self.edit = edit
        self.additional_attributes = kwargs

    def __str__(self):
        return str(self.get_non_null_attributes())

    def __repr__(self):
        return self.__str__()
```

String field for entity

### Ancestors (22)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (22)

`var attributes`

The type of the None singleton.

### Inherited members (22)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class EntityTimestampField (value: int,   label: str | None = None,   type: str | None = None,   edit: Dict[str, Any] | [EntityEditSupport](#slack_sdk.models.metadata.EntityEditSupport "slack_sdk.models.metadata.EntityEditSupport") | None = None,   **kwargs)`

Expand source code

```typescript
class EntityTimestampField(JsonObject):
    """Timestamp field for entity"""

    attributes = {
        "value",
        "label",
        "type",
        "edit",
    }

    def __init__(
        self,
        value: int,
        label: Optional[str] = None,
        type: Optional[str] = None,
        edit: Optional[Union[Dict[str, Any], EntityEditSupport]] = None,
        **kwargs,
    ):
        self.value = value
        self.label = label
        self.type = type
        self.edit = edit
        self.additional_attributes = kwargs

    def __str__(self):
        return str(self.get_non_null_attributes())

    def __repr__(self):
        return self.__str__()
```

Timestamp field for entity

### Ancestors (23)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (23)

`var attributes`

The type of the None singleton.

### Inherited members (23)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class EntityTitle (text: str,   edit: Dict[str, Any] | [EntityEditSupport](#slack_sdk.models.metadata.EntityEditSupport "slack_sdk.models.metadata.EntityEditSupport") | None = None,   **kwargs)`

Expand source code

```typescript
class EntityTitle(JsonObject):
    """Title for entity attributes"""

    attributes = {
        "text",
        "edit",
    }

    def __init__(
        self,
        text: str,
        edit: Optional[Union[Dict[str, Any], EntityEditSupport]] = None,
        **kwargs,
    ):
        self.text = text
        self.edit = edit
        self.additional_attributes = kwargs

    def __str__(self):
        return str(self.get_non_null_attributes())

    def __repr__(self):
        return self.__str__()
```

Title for entity attributes

### Ancestors (24)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (24)

`var attributes`

The type of the None singleton.

### Inherited members (24)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class EntityTypedField (type: str,   label: str | None = None,   value: str | int | None = None,   link: str | None = None,   icon: Dict[str, Any] | [EntityIconField](#slack_sdk.models.metadata.EntityIconField "slack_sdk.models.metadata.EntityIconField") | None = None,   long: bool | None = None,   format: str | None = None,   image_url: str | None = None,   slack_file: Dict[str, Any] | None = None,   alt_text: str | None = None,   edit: Dict[str, Any] | [EntityEditSupport](#slack_sdk.models.metadata.EntityEditSupport "slack_sdk.models.metadata.EntityEditSupport") | None = None,   tag_color: str | None = None,   user: Dict[str, Any] | [EntityUserIDField](#slack_sdk.models.metadata.EntityUserIDField "slack_sdk.models.metadata.EntityUserIDField") | [EntityUserField](#slack_sdk.models.metadata.EntityUserField "slack_sdk.models.metadata.EntityUserField") | None = None,   entity_ref: Dict[str, Any] | [EntityRefField](#slack_sdk.models.metadata.EntityRefField "slack_sdk.models.metadata.EntityRefField") | None = None,   **kwargs)`

Expand source code

```typescript
class EntityTypedField(JsonObject):
    """Typed field for entity with various display options"""

    attributes = {
        "type",
        "label",
        "value",
        "link",
        "icon",
        "long",
        "format",
        "image_url",
        "slack_file",
        "alt_text",
        "edit",
        "tag_color",
        "user",
        "entity_ref",
    }

    def __init__(
        self,
        type: str,
        label: Optional[str] = None,
        value: Optional[Union[str, int]] = None,
        link: Optional[str] = None,
        icon: Optional[Union[Dict[str, Any], EntityIconField]] = None,
        long: Optional[bool] = None,
        format: Optional[str] = None,
        image_url: Optional[str] = None,
        slack_file: Optional[Dict[str, Any]] = None,
        alt_text: Optional[str] = None,
        edit: Optional[Union[Dict[str, Any], EntityEditSupport]] = None,
        tag_color: Optional[str] = None,
        user: Optional[Union[Dict[str, Any], EntityUserIDField, EntityUserField]] = None,
        entity_ref: Optional[Union[Dict[str, Any], EntityRefField]] = None,
        **kwargs,
    ):
        self.type = type
        self.label = label
        self.value = value
        self.link = link
        self.icon = icon
        self.long = long
        self.format = format
        self.image_url = image_url
        self.slack_file = slack_file
        self.alt_text = alt_text
        self.edit = edit
        self.tag_color = tag_color
        self.user = user
        self.entity_ref = entity_ref
        self.additional_attributes = kwargs

    def __str__(self):
        return str(self.get_non_null_attributes())

    def __repr__(self):
        return self.__str__()
```

Typed field for entity with various display options

### Ancestors (25)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (25)

`var attributes`

The type of the None singleton.

### Inherited members (25)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class EntityUserField (text: str,   url: str | None = None,   email: str | None = None,   icon: Dict[str, Any] | [EntityIconField](#slack_sdk.models.metadata.EntityIconField "slack_sdk.models.metadata.EntityIconField") | None = None,   **kwargs)`

Expand source code

```typescript
class EntityUserField(JsonObject):
    """User field for entity"""

    attributes = {
        "text",
        "url",
        "email",
        "icon",
    }

    def __init__(
        self,
        text: str,
        url: Optional[str] = None,
        email: Optional[str] = None,
        icon: Optional[Union[Dict[str, Any], EntityIconField]] = None,
        **kwargs,
    ):
        self.text = text
        self.url = url
        self.email = email
        self.icon = icon
        self.additional_attributes = kwargs

    def __str__(self):
        return str(self.get_non_null_attributes())

    def __repr__(self):
        return self.__str__()
```

User field for entity

### Ancestors (26)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (26)

`var attributes`

The type of the None singleton.

### Inherited members (26)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class EntityUserIDField (user_id: str, **kwargs)`

Expand source code

```typescript
class EntityUserIDField(JsonObject):
    """User ID field for entity"""

    attributes = {
        "user_id",
    }

    def __init__(
        self,
        user_id: str,
        **kwargs,
    ):
        self.user_id = user_id
        self.additional_attributes = kwargs

    def __str__(self):
        return str(self.get_non_null_attributes())

    def __repr__(self):
        return self.__str__()
```

User ID field for entity

### Ancestors (27)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (27)

`var attributes`

The type of the None singleton.

### Inherited members (27)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class EventAndEntityMetadata (event_type: str | None = None,   event_payload: Dict[str, Any] | None = None,   entities: List[Dict[str, Any] | [EntityMetadata](#slack_sdk.models.metadata.EntityMetadata "slack_sdk.models.metadata.EntityMetadata")] | None = None,   **kwargs)`

Expand source code

```typescript
class EventAndEntityMetadata(JsonObject):
    """Message metadata with entities

    https://docs.slack.dev/messaging/message-metadata/
    https://docs.slack.dev/messaging/work-objects/
    """

    attributes = {"event_type", "event_payload", "entities"}

    def __init__(
        self,
        event_type: Optional[str] = None,
        event_payload: Optional[Dict[str, Any]] = None,
        entities: Optional[List[Union[Dict[str, Any], EntityMetadata]]] = None,
        **kwargs,
    ):
        self.event_type = event_type
        self.event_payload = event_payload
        self.entities = entities
        self.additional_attributes = kwargs

    def __str__(self):
        return str(self.get_non_null_attributes())

    def __repr__(self):
        return self.__str__()
```

Message metadata with entities

[https://docs.slack.dev/messaging/message-metadata/](https://docs.slack.dev/messaging/message-metadata/) [https://docs.slack.dev/messaging/work-objects/](https://docs.slack.dev/messaging/work-objects/)

### Ancestors (28)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (28)

`var attributes`

The type of the None singleton.

### Inherited members (28)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class ExternalRef (id: str, type: str | None = None, **kwargs)`

Expand source code

```typescript
class ExternalRef(JsonObject):
    """Reference (and optional type) used to identify an entity within the developer's system"""

    attributes = {
        "id",
        "type",
    }

    def __init__(
        self,
        id: str,
        type: Optional[str] = None,
        **kwargs,
    ):
        self.id = id
        self.type = type
        self.additional_attributes = kwargs

    def __str__(self):
        return str(self.get_non_null_attributes())

    def __repr__(self):
        return self.__str__()
```

Reference (and optional type) used to identify an entity within the developer's system

### Ancestors (29)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (29)

`var attributes`

The type of the None singleton.

### Inherited members (29)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class FileEntityFields (preview: Dict[str, Any] | [EntityImageField](#slack_sdk.models.metadata.EntityImageField "slack_sdk.models.metadata.EntityImageField") | None = None,   created_by: Dict[str, Any] | [EntityTypedField](#slack_sdk.models.metadata.EntityTypedField "slack_sdk.models.metadata.EntityTypedField") | None = None,   date_created: Dict[str, Any] | [EntityTimestampField](#slack_sdk.models.metadata.EntityTimestampField "slack_sdk.models.metadata.EntityTimestampField") | None = None,   date_updated: Dict[str, Any] | [EntityTimestampField](#slack_sdk.models.metadata.EntityTimestampField "slack_sdk.models.metadata.EntityTimestampField") | None = None,   last_modified_by: Dict[str, Any] | [EntityTypedField](#slack_sdk.models.metadata.EntityTypedField "slack_sdk.models.metadata.EntityTypedField") | None = None,   file_size: Dict[str, Any] | [EntityStringField](#slack_sdk.models.metadata.EntityStringField "slack_sdk.models.metadata.EntityStringField") | None = None,   mime_type: Dict[str, Any] | [EntityStringField](#slack_sdk.models.metadata.EntityStringField "slack_sdk.models.metadata.EntityStringField") | None = None,   full_size_preview: Dict[str, Any] | [EntityFullSizePreview](#slack_sdk.models.metadata.EntityFullSizePreview "slack_sdk.models.metadata.EntityFullSizePreview") | None = None,   **kwargs)`

Expand source code

```typescript
class FileEntityFields(JsonObject):
    """Fields specific to file entities"""

    attributes = {
        "preview",
        "created_by",
        "date_created",
        "date_updated",
        "last_modified_by",
        "file_size",
        "mime_type",
        "full_size_preview",
    }

    def __init__(
        self,
        preview: Optional[Union[Dict[str, Any], EntityImageField]] = None,
        created_by: Optional[Union[Dict[str, Any], EntityTypedField]] = None,
        date_created: Optional[Union[Dict[str, Any], EntityTimestampField]] = None,
        date_updated: Optional[Union[Dict[str, Any], EntityTimestampField]] = None,
        last_modified_by: Optional[Union[Dict[str, Any], EntityTypedField]] = None,
        file_size: Optional[Union[Dict[str, Any], EntityStringField]] = None,
        mime_type: Optional[Union[Dict[str, Any], EntityStringField]] = None,
        full_size_preview: Optional[Union[Dict[str, Any], EntityFullSizePreview]] = None,
        **kwargs,
    ):
        self.preview = preview
        self.created_by = created_by
        self.date_created = date_created
        self.date_updated = date_updated
        self.last_modified_by = last_modified_by
        self.file_size = file_size
        self.mime_type = mime_type
        self.full_size_preview = full_size_preview
        self.additional_attributes = kwargs

    def __str__(self):
        return str(self.get_non_null_attributes())

    def __repr__(self):
        return self.__str__()
```

Fields specific to file entities

### Ancestors (30)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (30)

`var attributes`

The type of the None singleton.

### Inherited members (30)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class FileEntitySlackFile (id: str, type: str | None = None, **kwargs)`

Expand source code

```typescript
class FileEntitySlackFile(JsonObject):
    """Slack file reference for file entities"""

    attributes = {
        "id",
        "type",
    }

    def __init__(
        self,
        id: str,
        type: Optional[str] = None,
        **kwargs,
    ):
        self.id = id
        self.type = type
        self.additional_attributes = kwargs

    def __str__(self):
        return str(self.get_non_null_attributes())

    def __repr__(self):
        return self.__str__()
```

Slack file reference for file entities

### Ancestors (31)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (31)

`var attributes`

The type of the None singleton.

### Inherited members (31)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class IncidentEntityFields (status: Dict[str, Any] | [EntityStringField](#slack_sdk.models.metadata.EntityStringField "slack_sdk.models.metadata.EntityStringField") | None = None,   priority: Dict[str, Any] | [EntityStringField](#slack_sdk.models.metadata.EntityStringField "slack_sdk.models.metadata.EntityStringField") | None = None,   urgency: Dict[str, Any] | [EntityStringField](#slack_sdk.models.metadata.EntityStringField "slack_sdk.models.metadata.EntityStringField") | None = None,   created_by: Dict[str, Any] | [EntityTypedField](#slack_sdk.models.metadata.EntityTypedField "slack_sdk.models.metadata.EntityTypedField") | None = None,   assigned_to: Dict[str, Any] | [EntityTypedField](#slack_sdk.models.metadata.EntityTypedField "slack_sdk.models.metadata.EntityTypedField") | None = None,   date_created: Dict[str, Any] | [EntityTimestampField](#slack_sdk.models.metadata.EntityTimestampField "slack_sdk.models.metadata.EntityTimestampField") | None = None,   date_updated: Dict[str, Any] | [EntityTimestampField](#slack_sdk.models.metadata.EntityTimestampField "slack_sdk.models.metadata.EntityTimestampField") | None = None,   description: Dict[str, Any] | [EntityStringField](#slack_sdk.models.metadata.EntityStringField "slack_sdk.models.metadata.EntityStringField") | None = None,   service: Dict[str, Any] | [EntityStringField](#slack_sdk.models.metadata.EntityStringField "slack_sdk.models.metadata.EntityStringField") | None = None,   **kwargs)`

Expand source code

```typescript
class IncidentEntityFields(JsonObject):
    """Fields specific to incident entities"""

    attributes = {
        "status",
        "priority",
        "urgency",
        "created_by",
        "assigned_to",
        "date_created",
        "date_updated",
        "description",
        "service",
    }

    def __init__(
        self,
        status: Optional[Union[Dict[str, Any], EntityStringField]] = None,
        priority: Optional[Union[Dict[str, Any], EntityStringField]] = None,
        urgency: Optional[Union[Dict[str, Any], EntityStringField]] = None,
        created_by: Optional[Union[Dict[str, Any], EntityTypedField]] = None,
        assigned_to: Optional[Union[Dict[str, Any], EntityTypedField]] = None,
        date_created: Optional[Union[Dict[str, Any], EntityTimestampField]] = None,
        date_updated: Optional[Union[Dict[str, Any], EntityTimestampField]] = None,
        description: Optional[Union[Dict[str, Any], EntityStringField]] = None,
        service: Optional[Union[Dict[str, Any], EntityStringField]] = None,
        **kwargs,
    ):
        self.status = status
        self.priority = priority
        self.urgency = urgency
        self.created_by = created_by
        self.assigned_to = assigned_to
        self.date_created = date_created
        self.date_updated = date_updated
        self.description = description
        self.service = service
        self.additional_attributes = kwargs

    def __str__(self):
        return str(self.get_non_null_attributes())

    def __repr__(self):
        return self.__str__()
```

Fields specific to incident entities

### Ancestors (32)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (32)

`var attributes`

The type of the None singleton.

### Inherited members (32)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class Metadata (event_type: str, event_payload: Dict[str, Any], **kwargs)`

Expand source code

```typescript
class Metadata(JsonObject):
    """Message metadata

    https://docs.slack.dev/messaging/message-metadata/
    """

    attributes = {
        "event_type",
        "event_payload",
    }

    def __init__(
        self,
        event_type: str,
        event_payload: Dict[str, Any],
        **kwargs,
    ):
        self.event_type = event_type
        self.event_payload = event_payload
        self.additional_attributes = kwargs

    def __str__(self):
        return str(self.get_non_null_attributes())

    def __repr__(self):
        return self.__str__()
```

Message metadata

[https://docs.slack.dev/messaging/message-metadata/](https://docs.slack.dev/messaging/message-metadata/)

### Ancestors (33)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (33)

`var attributes`

The type of the None singleton.

### Inherited members (33)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class TaskEntityFields (description: Dict[str, Any] | [EntityStringField](#slack_sdk.models.metadata.EntityStringField "slack_sdk.models.metadata.EntityStringField") | None = None,   created_by: Dict[str, Any] | [EntityTypedField](#slack_sdk.models.metadata.EntityTypedField "slack_sdk.models.metadata.EntityTypedField") | None = None,   date_created: Dict[str, Any] | [EntityTimestampField](#slack_sdk.models.metadata.EntityTimestampField "slack_sdk.models.metadata.EntityTimestampField") | None = None,   date_updated: Dict[str, Any] | [EntityTimestampField](#slack_sdk.models.metadata.EntityTimestampField "slack_sdk.models.metadata.EntityTimestampField") | None = None,   assignee: Dict[str, Any] | [EntityTypedField](#slack_sdk.models.metadata.EntityTypedField "slack_sdk.models.metadata.EntityTypedField") | None = None,   status: Dict[str, Any] | [EntityStringField](#slack_sdk.models.metadata.EntityStringField "slack_sdk.models.metadata.EntityStringField") | None = None,   due_date: Dict[str, Any] | [EntityTypedField](#slack_sdk.models.metadata.EntityTypedField "slack_sdk.models.metadata.EntityTypedField") | None = None,   priority: Dict[str, Any] | [EntityStringField](#slack_sdk.models.metadata.EntityStringField "slack_sdk.models.metadata.EntityStringField") | None = None,   **kwargs)`

Expand source code

```typescript
class TaskEntityFields(JsonObject):
    """Fields specific to task entities"""

    attributes = {
        "description",
        "created_by",
        "date_created",
        "date_updated",
        "assignee",
        "status",
        "due_date",
        "priority",
    }

    def __init__(
        self,
        description: Optional[Union[Dict[str, Any], EntityStringField]] = None,
        created_by: Optional[Union[Dict[str, Any], EntityTypedField]] = None,
        date_created: Optional[Union[Dict[str, Any], EntityTimestampField]] = None,
        date_updated: Optional[Union[Dict[str, Any], EntityTimestampField]] = None,
        assignee: Optional[Union[Dict[str, Any], EntityTypedField]] = None,
        status: Optional[Union[Dict[str, Any], EntityStringField]] = None,
        due_date: Optional[Union[Dict[str, Any], EntityTypedField]] = None,
        priority: Optional[Union[Dict[str, Any], EntityStringField]] = None,
        **kwargs,
    ):
        self.description = description
        self.created_by = created_by
        self.date_created = date_created
        self.date_updated = date_updated
        self.assignee = assignee
        self.status = status
        self.due_date = due_date
        self.priority = priority
        self.additional_attributes = kwargs

    def __str__(self):
        return str(self.get_non_null_attributes())

    def __repr__(self):
        return self.__str__()
```

Fields specific to task entities

### Ancestors (34)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (34)

`var attributes`

The type of the None singleton.

### Inherited members (34)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`
