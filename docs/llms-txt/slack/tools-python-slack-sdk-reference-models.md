Source: https://docs.slack.dev/tools/python-slack-sdk/reference/models

# Module slack_sdk.models

Classes for constructing Slack-specific data structure

## Sub-modules

`[slack_sdk.models.attachments](attachments/index.html "slack_sdk.models.attachments")`

`[slack_sdk.models.basic_objects](basic_objects.html "slack_sdk.models.basic_objects")`

`[slack_sdk.models.blocks](blocks/index.html "slack_sdk.models.blocks")`

Block Kit data model objects …

`[slack_sdk.models.dialoags](dialoags.html "slack_sdk.models.dialoags")`

`[slack_sdk.models.dialogs](dialogs/index.html "slack_sdk.models.dialogs")`

`[slack_sdk.models.messages](messages/index.html "slack_sdk.models.messages")`

`[slack_sdk.models.metadata](metadata/index.html "slack_sdk.models.metadata")`

`[slack_sdk.models.views](views/index.html "slack_sdk.models.views")`

## Functions

`def extract_json(item_or_items: [JsonObject](basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject") | Sequence[[JsonObject](basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")],   *format_args) ‑> Dict[Any, Any] | List[Dict[Any, Any]] | Sequence[[JsonObject](basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")]`

Expand source code

```python
def extract_json(
    item_or_items: Union[JsonObject, Sequence[JsonObject]], *format_args
) -> Union[Dict[Any, Any], List[Dict[Any, Any]], Sequence[JsonObject]]:
    """
    Given a sequence (or single item), attempt to call the to_dict() method on each
    item and return a plain list. If item is not the expected type, return it
    unmodified, in case it's already a plain dict or some other user created class.

    Args:
      item_or_items: item(s) to go through
      format_args: Any formatting specifiers to pass into the object's to_dict
            method
    """
    try:
        return [
            elem.to_dict(*format_args) if isinstance(elem, JsonObject) else elem
            for elem in item_or_items  # type: ignore[union-attr]
        ]
    except TypeError:  # not iterable, so try returning it as a single item
        return item_or_items.to_dict(*format_args) if isinstance(item_or_items, JsonObject) else item_or_items
```

Given a sequence (or single item), attempt to call the to\_dict() method on each item and return a plain list. If item is not the expected type, return it unmodified, in case it's already a plain dict or some other user created class.

## Args

**`item_or_items`**

item(s) to go through

**`format_args`**

Any formatting specifiers to pass into the object's to\_dict method

`def show_unknown_key_warning(name: str | object, others: dict)`

Expand source code

```python
def show_unknown_key_warning(name: Union[str, object], others: dict):
    if "type" in others:
        others.pop("type")
    if len(others) > 0:
        keys = ", ".join(others.keys())
        logger = logging.getLogger(__name__)
        if isinstance(name, object):
            name = name.__class__.__name__
        logger.debug(
            f"!!! {name}'s constructor args ({keys}) were ignored."
            f"If they should be supported by this library, report this issue to the project :bow: "
            f"https://github.com/slackapi/python-slack-sdk/issues"
        )
```

## Classes

`class BaseObject`

Expand source code

```typescript
class BaseObject:
    """The base class for all model objects in this module"""

    def __str__(self):
        return f"<slack_sdk.{self.__class__.__name__}>"
```

The base class for all model objects in this module

### Subclasses

* [JsonObject](basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [Link](messages/index.html#slack_sdk.models.messages.Link "slack_sdk.models.messages.Link")

`class EnumValidator (attribute: str, enum: Iterable[str])`

Expand source code

```python
class EnumValidator(JsonValidator):
    def __init__(self, attribute: str, enum: Iterable[str]):
        super().__init__(f"{attribute} attribute must be one of the following values: " f"{', '.join(enum)}")
```

Decorate a method on a class to mark it as a JSON validator. Validation functions should return true if valid, false if not.

## Args (2)

**`message`**

Message to be attached to the thrown SlackObjectFormationError

### Ancestors

* [JsonValidator](basic_objects.html#slack_sdk.models.basic_objects.JsonValidator "slack_sdk.models.basic_objects.JsonValidator")

`class JsonObject`

Expand source code

```typescript
class JsonObject(BaseObject, metaclass=ABCMeta):
    """The base class for JSON serializable class objects"""

    @property
    @abstractmethod
    def attributes(self) -> Set[str]:
        """Provide a set of attributes of this object that will make up its JSON structure"""
        return set()

    def validate_json(self) -> None:
        """
        Raises:
          SlackObjectFormationError if the object was not valid
        """
        for attribute in (func for func in dir(self) if not func.startswith("__")):
            method = getattr(self, attribute, None)
            if callable(method) and hasattr(method, "validator"):
                method()

    def get_object_attribute(self, key: str):
        return getattr(self, key, None)

    def get_non_null_attributes(self) -> dict:
        """
        Construct a dictionary out of non-null keys (from attributes property)
        present on this object
        """

        def to_dict_compatible(value: Union[dict, list, object, tuple]) -> Union[dict, list, Any]:
            if isinstance(value, (list, tuple)):
                return [to_dict_compatible(v) for v in value]
            else:
                to_dict = getattr(value, "to_dict", None)
                if to_dict and callable(to_dict):
                    return {k: to_dict_compatible(v) for k, v in value.to_dict().items()}  # type: ignore[attr-defined]
                else:
                    return value

        def is_not_empty(self, key: str) -> bool:
            value = self.get_object_attribute(key)
            if value is None:
                return False

            # Usually, Block Kit components do not allow an empty array for a property value, but there are some exceptions.
            # The following code deals with these exceptions:
            type_value = getattr(self, "type", None)
            for empty_allowed in EMPTY_ALLOWED_TYPE_AND_PROPERTY_LIST:
                if type_value == empty_allowed["type"] and key == empty_allowed["property"]:
                    return True

            has_len = getattr(value, "__len__", None) is not None
            if has_len:
                return len(value) > 0
            else:
                return value is not None

        return {
            key: to_dict_compatible(value=self.get_object_attribute(key))
            for key in sorted(self.attributes)
            if is_not_empty(self, key)
        }

    def to_dict(self, *args) -> dict:
        """
        Extract this object as a JSON-compatible, Slack-API-valid dictionary

        Args:
          *args: Any specific formatting args (rare; generally not required)

        Raises:
          SlackObjectFormationError if the object was not valid
        """
        self.validate_json()
        return self.get_non_null_attributes()

    def __repr__(self):
        dict_value = self.get_non_null_attributes()
        if dict_value:
            return f"<slack_sdk.{self.__class__.__name__}: {dict_value}>"
        else:
            return self.__str__()

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, JsonObject):
            return False
        return self.to_dict() == other.to_dict()
```

The base class for JSON serializable class objects

### Ancestors (2)

* [BaseObject](basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Subclasses (2)

* [Action](attachments/index.html#slack_sdk.models.attachments.Action "slack_sdk.models.attachments.Action")
* [Attachment](attachments/index.html#slack_sdk.models.attachments.Attachment "slack_sdk.models.attachments.Attachment")
* [AttachmentField](attachments/index.html#slack_sdk.models.attachments.AttachmentField "slack_sdk.models.attachments.AttachmentField")
* [ConfirmObject](blocks/basic_components.html#slack_sdk.models.blocks.basic_components.ConfirmObject "slack_sdk.models.blocks.basic_components.ConfirmObject")
* [DispatchActionConfig](blocks/basic_components.html#slack_sdk.models.blocks.basic_components.DispatchActionConfig "slack_sdk.models.blocks.basic_components.DispatchActionConfig")
* [FeedbackButtonObject](blocks/basic_components.html#slack_sdk.models.blocks.basic_components.FeedbackButtonObject "slack_sdk.models.blocks.basic_components.FeedbackButtonObject")
* [Option](blocks/basic_components.html#slack_sdk.models.blocks.basic_components.Option "slack_sdk.models.blocks.basic_components.Option")
* [OptionGroup](blocks/basic_components.html#slack_sdk.models.blocks.basic_components.OptionGroup "slack_sdk.models.blocks.basic_components.OptionGroup")
* [SlackFile](blocks/basic_components.html#slack_sdk.models.blocks.basic_components.SlackFile "slack_sdk.models.blocks.basic_components.SlackFile")
* [TextObject](blocks/basic_components.html#slack_sdk.models.blocks.basic_components.TextObject "slack_sdk.models.blocks.basic_components.TextObject")
* [Workflow](blocks/basic_components.html#slack_sdk.models.blocks.basic_components.Workflow "slack_sdk.models.blocks.basic_components.Workflow")
* [WorkflowTrigger](blocks/basic_components.html#slack_sdk.models.blocks.basic_components.WorkflowTrigger "slack_sdk.models.blocks.basic_components.WorkflowTrigger")
* [BlockElement](blocks/block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement")
* [ConversationFilter](blocks/block_elements.html#slack_sdk.models.blocks.block_elements.ConversationFilter "slack_sdk.models.blocks.block_elements.ConversationFilter")
* [Block](blocks/blocks.html#slack_sdk.models.blocks.blocks.Block "slack_sdk.models.blocks.blocks.Block")
* [AbstractDialogSelector](dialogs/index.html#slack_sdk.models.dialogs.AbstractDialogSelector "slack_sdk.models.dialogs.AbstractDialogSelector")
* [DialogBuilder](dialogs/index.html#slack_sdk.models.dialogs.DialogBuilder "slack_sdk.models.dialogs.DialogBuilder")
* [DialogTextComponent](dialogs/index.html#slack_sdk.models.dialogs.DialogTextComponent "slack_sdk.models.dialogs.DialogTextComponent")
* [Chunk](messages/chunk.html#slack_sdk.models.messages.chunk.Chunk "slack_sdk.models.messages.chunk.Chunk")
* [Message](messages/message.html#slack_sdk.models.messages.message.Message "slack_sdk.models.messages.message.Message")
* [ContentItemEntityFields](metadata/index.html#slack_sdk.models.metadata.ContentItemEntityFields "slack_sdk.models.metadata.ContentItemEntityFields")
* [EntityActionButton](metadata/index.html#slack_sdk.models.metadata.EntityActionButton "slack_sdk.models.metadata.EntityActionButton")
* [EntityActionProcessingState](metadata/index.html#slack_sdk.models.metadata.EntityActionProcessingState "slack_sdk.models.metadata.EntityActionProcessingState")
* [EntityActions](metadata/index.html#slack_sdk.models.metadata.EntityActions "slack_sdk.models.metadata.EntityActions")
* [EntityArrayItemField](metadata/index.html#slack_sdk.models.metadata.EntityArrayItemField "slack_sdk.models.metadata.EntityArrayItemField")
* [EntityAttributes](metadata/index.html#slack_sdk.models.metadata.EntityAttributes "slack_sdk.models.metadata.EntityAttributes")
* [EntityBooleanCheckboxField](metadata/index.html#slack_sdk.models.metadata.EntityBooleanCheckboxField "slack_sdk.models.metadata.EntityBooleanCheckboxField")
* [EntityBooleanTextField](metadata/index.html#slack_sdk.models.metadata.EntityBooleanTextField "slack_sdk.models.metadata.EntityBooleanTextField")
* [EntityCustomField](metadata/index.html#slack_sdk.models.metadata.EntityCustomField "slack_sdk.models.metadata.EntityCustomField")
* [EntityEditNumberConfig](metadata/index.html#slack_sdk.models.metadata.EntityEditNumberConfig "slack_sdk.models.metadata.EntityEditNumberConfig")
* [EntityEditSelectConfig](metadata/index.html#slack_sdk.models.metadata.EntityEditSelectConfig "slack_sdk.models.metadata.EntityEditSelectConfig")
* [EntityEditSupport](metadata/index.html#slack_sdk.models.metadata.EntityEditSupport "slack_sdk.models.metadata.EntityEditSupport")
* [EntityEditTextConfig](metadata/index.html#slack_sdk.models.metadata.EntityEditTextConfig "slack_sdk.models.metadata.EntityEditTextConfig")
* [EntityFullSizePreview](metadata/index.html#slack_sdk.models.metadata.EntityFullSizePreview "slack_sdk.models.metadata.EntityFullSizePreview")
* [EntityFullSizePreviewError](metadata/index.html#slack_sdk.models.metadata.EntityFullSizePreviewError "slack_sdk.models.metadata.EntityFullSizePreviewError")
* [EntityIconField](metadata/index.html#slack_sdk.models.metadata.EntityIconField "slack_sdk.models.metadata.EntityIconField")
* [EntityIconSlackFile](metadata/index.html#slack_sdk.models.metadata.EntityIconSlackFile "slack_sdk.models.metadata.EntityIconSlackFile")
* [EntityImageField](metadata/index.html#slack_sdk.models.metadata.EntityImageField "slack_sdk.models.metadata.EntityImageField")
* [EntityMetadata](metadata/index.html#slack_sdk.models.metadata.EntityMetadata "slack_sdk.models.metadata.EntityMetadata")
* [EntityPayload](metadata/index.html#slack_sdk.models.metadata.EntityPayload "slack_sdk.models.metadata.EntityPayload")
* [EntityRefField](metadata/index.html#slack_sdk.models.metadata.EntityRefField "slack_sdk.models.metadata.EntityRefField")
* [EntityStringField](metadata/index.html#slack_sdk.models.metadata.EntityStringField "slack_sdk.models.metadata.EntityStringField")
* [EntityTimestampField](metadata/index.html#slack_sdk.models.metadata.EntityTimestampField "slack_sdk.models.metadata.EntityTimestampField")
* [EntityTitle](metadata/index.html#slack_sdk.models.metadata.EntityTitle "slack_sdk.models.metadata.EntityTitle")
* [EntityTypedField](metadata/index.html#slack_sdk.models.metadata.EntityTypedField "slack_sdk.models.metadata.EntityTypedField")
* [EntityUserField](metadata/index.html#slack_sdk.models.metadata.EntityUserField "slack_sdk.models.metadata.EntityUserField")
* [EntityUserIDField](metadata/index.html#slack_sdk.models.metadata.EntityUserIDField "slack_sdk.models.metadata.EntityUserIDField")
* [EventAndEntityMetadata](metadata/index.html#slack_sdk.models.metadata.EventAndEntityMetadata "slack_sdk.models.metadata.EventAndEntityMetadata")
* [ExternalRef](metadata/index.html#slack_sdk.models.metadata.ExternalRef "slack_sdk.models.metadata.ExternalRef")
* [FileEntityFields](metadata/index.html#slack_sdk.models.metadata.FileEntityFields "slack_sdk.models.metadata.FileEntityFields")
* [FileEntitySlackFile](metadata/index.html#slack_sdk.models.metadata.FileEntitySlackFile "slack_sdk.models.metadata.FileEntitySlackFile")
* [IncidentEntityFields](metadata/index.html#slack_sdk.models.metadata.IncidentEntityFields "slack_sdk.models.metadata.IncidentEntityFields")
* [Metadata](metadata/index.html#slack_sdk.models.metadata.Metadata "slack_sdk.models.metadata.Metadata")
* [TaskEntityFields](metadata/index.html#slack_sdk.models.metadata.TaskEntityFields "slack_sdk.models.metadata.TaskEntityFields")
* [View](views/index.html#slack_sdk.models.views.View "slack_sdk.models.views.View")
* [ViewState](views/index.html#slack_sdk.models.views.ViewState "slack_sdk.models.views.ViewState")
* [ViewStateValue](views/index.html#slack_sdk.models.views.ViewStateValue "slack_sdk.models.views.ViewStateValue")

### Instance variables

`prop attributes : Set[str]`

Expand source code

```python
@property
@abstractmethod
def attributes(self) -> Set[str]:
    """Provide a set of attributes of this object that will make up its JSON structure"""
    return set()
```

Provide a set of attributes of this object that will make up its JSON structure

### Methods

`def get_non_null_attributes(self) ‑> dict`

Expand source code

```python
def get_non_null_attributes(self) -> dict:
    """
    Construct a dictionary out of non-null keys (from attributes property)
    present on this object
    """

    def to_dict_compatible(value: Union[dict, list, object, tuple]) -> Union[dict, list, Any]:
        if isinstance(value, (list, tuple)):
            return [to_dict_compatible(v) for v in value]
        else:
            to_dict = getattr(value, "to_dict", None)
            if to_dict and callable(to_dict):
                return {k: to_dict_compatible(v) for k, v in value.to_dict().items()}  # type: ignore[attr-defined]
            else:
                return value

    def is_not_empty(self, key: str) -> bool:
        value = self.get_object_attribute(key)
        if value is None:
            return False

        # Usually, Block Kit components do not allow an empty array for a property value, but there are some exceptions.
        # The following code deals with these exceptions:
        type_value = getattr(self, "type", None)
        for empty_allowed in EMPTY_ALLOWED_TYPE_AND_PROPERTY_LIST:
            if type_value == empty_allowed["type"] and key == empty_allowed["property"]:
                return True

        has_len = getattr(value, "__len__", None) is not None
        if has_len:
            return len(value) > 0
        else:
            return value is not None

    return {
        key: to_dict_compatible(value=self.get_object_attribute(key))
        for key in sorted(self.attributes)
        if is_not_empty(self, key)
    }
```

Construct a dictionary out of non-null keys (from attributes property) present on this object

`def get_object_attribute(self, key: str)`

Expand source code

```python
def get_object_attribute(self, key: str):
    return getattr(self, key, None)
```

`def to_dict(self, *args) ‑> dict`

Expand source code

```python
def to_dict(self, *args) -> dict:
    """
    Extract this object as a JSON-compatible, Slack-API-valid dictionary

    Args:
      *args: Any specific formatting args (rare; generally not required)

    Raises:
      SlackObjectFormationError if the object was not valid
    """
    self.validate_json()
    return self.get_non_null_attributes()
```

Extract this object as a JSON-compatible, Slack-API-valid dictionary

## Args (3)

**`*args`**

Any specific formatting args (rare; generally not required)

## Raises

SlackObjectFormationError if the object was not valid

`def validate_json(self) ‑> None`

Expand source code

```python
def validate_json(self) -> None:
    """
    Raises:
      SlackObjectFormationError if the object was not valid
    """
    for attribute in (func for func in dir(self) if not func.startswith("__")):
        method = getattr(self, attribute, None)
        if callable(method) and hasattr(method, "validator"):
            method()
```

## Raises (2)

SlackObjectFormationError if the object was not valid

`class JsonValidator (message: str)`

Expand source code

```typescript
class JsonValidator:
    def __init__(self, message: str):
        """
        Decorate a method on a class to mark it as a JSON validator. Validation
            functions should return true if valid, false if not.

        Args:
            message: Message to be attached to the thrown SlackObjectFormationError
        """
        self.message = message

    def __call__(self, func: Callable) -> Callable[..., None]:
        @wraps(func)
        def wrapped_f(*args, **kwargs):
            if not func(*args, **kwargs):
                raise SlackObjectFormationError(self.message)

        wrapped_f.validator = True  # type: ignore[attr-defined]
        return wrapped_f
```

Decorate a method on a class to mark it as a JSON validator. Validation functions should return true if valid, false if not.

## Args (4)

**`message`**

Message to be attached to the thrown SlackObjectFormationError

### Subclasses (3)

* [EnumValidator](basic_objects.html#slack_sdk.models.basic_objects.EnumValidator "slack_sdk.models.basic_objects.EnumValidator")
