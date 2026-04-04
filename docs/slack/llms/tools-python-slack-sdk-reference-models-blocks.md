Source: https://docs.slack.dev/tools/python-slack-sdk/reference/models/blocks

# Module slack_sdk.models.blocks

Block Kit data model objects

To learn more about Block Kit, please check the following resources and tools:

* [https://docs.slack.dev/block-kit/](https://docs.slack.dev/block-kit/)
* [https://docs.slack.dev/reference/block-kit/blocks](https://docs.slack.dev/reference/block-kit/blocks)
* [https://app.slack.com/block-kit-builder](https://app.slack.com/block-kit-builder)

## Sub-modules

`[slack_sdk.models.blocks.basic_components](basic_components.html "slack_sdk.models.blocks.basic_components")`

`[slack_sdk.models.blocks.block_elements](block_elements.html "slack_sdk.models.blocks.block_elements")`

`[slack_sdk.models.blocks.blocks](blocks.html "slack_sdk.models.blocks.blocks")`

## Classes

`class ActionsBlock (*,   elements: Sequence[dict | [InteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement "slack_sdk.models.blocks.block_elements.InteractiveElement")],   block_id: str | None = None,   **others: dict)`

Expand source code

```typescript
class ActionsBlock(Block):
    type = "actions"
    elements_max_length = 25

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union({"elements"})

    def __init__(
        self,
        *,
        elements: Sequence[Union[dict, InteractiveElement]],
        block_id: Optional[str] = None,
        **others: dict,
    ):
        """A block that is used to hold interactive elements.
        https://docs.slack.dev/reference/block-kit/blocks/actions-block

        Args:
            elements (required): An array of interactive element objects - buttons, select menus, overflow menus,
                or date pickers. There is a maximum of 25 elements in each action block.
            block_id: A string acting as a unique identifier for a block.
                If not specified, a block_id will be generated.
                You can use this block_id when you receive an interaction payload to identify the source of the action.
                Maximum length for this field is 255 characters.
                block_id should be unique for each message and each iteration of a message.
                If a message is updated, use a new block_id.
        """
        super().__init__(type=self.type, block_id=block_id)
        show_unknown_key_warning(self, others)

        self.elements = BlockElement.parse_all(elements)

    @JsonValidator(f"elements attribute cannot exceed {elements_max_length} elements")
    def _validate_elements_length(self):
        return self.elements is None or len(self.elements) <= self.elements_max_length
```

Blocks are a series of components that can be combined to create visually rich and compellingly interactive messages. [https://docs.slack.dev/reference/block-kit/blocks](https://docs.slack.dev/reference/block-kit/blocks)

A block that is used to hold interactive elements. [https://docs.slack.dev/reference/block-kit/blocks/actions-block](https://docs.slack.dev/reference/block-kit/blocks/actions-block)

## Args

**`elements`** : `required`

An array of interactive element objects - buttons, select menus, overflow menus, or date pickers. There is a maximum of 25 elements in each action block.

**`block_id`**

A string acting as a unique identifier for a block. If not specified, a block\_id will be generated. You can use this block\_id when you receive an interaction payload to identify the source of the action. Maximum length for this field is 255 characters. block\_id should be unique for each message and each iteration of a message. If a message is updated, use a new block\_id.

### Ancestors

* [Block](blocks.html#slack_sdk.models.blocks.blocks.Block "slack_sdk.models.blocks.blocks.Block")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables

`var elements_max_length`

The type of the None singleton.

`var type`

The type of the None singleton.

### Instance variables

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union({"elements"})
```

Build an unordered collection of unique elements.

### Inherited members

* `**[Block](blocks.html#slack_sdk.models.blocks.blocks.Block "slack_sdk.models.blocks.blocks.Block")**`:
  * `[block_id_max_length](blocks.html#slack_sdk.models.blocks.blocks.Block.block_id_max_length "slack_sdk.models.blocks.blocks.Block.block_id_max_length")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.blocks.Block.get_non_null_attributes")`
  * `[logger](blocks.html#slack_sdk.models.blocks.blocks.Block.logger "slack_sdk.models.blocks.blocks.Block.logger")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.blocks.Block.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.blocks.Block.validate_json")`

`class Block (*,   type: str | None = None,   subtype: str | None = None,   block_id: str | None = None)`

Expand source code

```typescript
class Block(JsonObject):
    """Blocks are a series of components that can be combined
    to create visually rich and compellingly interactive messages.
    https://docs.slack.dev/reference/block-kit/blocks
    """

    attributes = {"block_id", "type"}
    block_id_max_length = 255
    logger = logging.getLogger(__name__)

    def _subtype_warning(self):
        warnings.warn(
            "subtype is deprecated since slackclient 2.6.0, use type instead",
            DeprecationWarning,
        )

    @property
    def subtype(self) -> Optional[str]:
        return self.type

    def __init__(
        self,
        *,
        type: Optional[str] = None,
        subtype: Optional[str] = None,  # deprecated
        block_id: Optional[str] = None,
    ):
        if subtype:
            self._subtype_warning()
        self.type = type if type else subtype
        self.block_id = block_id
        self.color = None

    @JsonValidator(f"block_id cannot exceed {block_id_max_length} characters")
    def _validate_block_id_length(self):
        return self.block_id is None or len(self.block_id) <= self.block_id_max_length

    @classmethod
    def parse(cls, block: Union[dict, "Block"]) -> Optional["Block"]:
        if block is None:
            return None
        elif isinstance(block, Block):
            return block
        else:
            if "type" in block:
                type = block["type"]
                if type == SectionBlock.type:
                    return SectionBlock(**block)
                elif type == DividerBlock.type:
                    return DividerBlock(**block)
                elif type == ImageBlock.type:
                    return ImageBlock(**block)
                elif type == ActionsBlock.type:
                    return ActionsBlock(**block)
                elif type == ContextBlock.type:
                    return ContextBlock(**block)
                elif type == ContextActionsBlock.type:
                    return ContextActionsBlock(**block)
                elif type == InputBlock.type:
                    return InputBlock(**block)
                elif type == FileBlock.type:
                    return FileBlock(**block)
                elif type == CallBlock.type:
                    return CallBlock(**block)
                elif type == HeaderBlock.type:
                    return HeaderBlock(**block)
                elif type == MarkdownBlock.type:
                    return MarkdownBlock(**block)
                elif type == VideoBlock.type:
                    return VideoBlock(**block)
                elif type == RichTextBlock.type:
                    return RichTextBlock(**block)
                elif type == TableBlock.type:
                    return TableBlock(**block)
                elif type == TaskCardBlock.type:
                    return TaskCardBlock(**block)
                elif type == PlanBlock.type:
                    return PlanBlock(**block)
                else:
                    cls.logger.warning(f"Unknown block detected and skipped ({block})")
                    return None
            else:
                cls.logger.warning(f"Unknown block detected and skipped ({block})")
                return None

    @classmethod
    def parse_all(cls, blocks: Optional[Sequence[Union[dict, "Block"]]]) -> List["Block"]:
        return [cls.parse(b) for b in blocks or []]  # type: ignore[misc]
```

Blocks are a series of components that can be combined to create visually rich and compellingly interactive messages. [https://docs.slack.dev/reference/block-kit/blocks](https://docs.slack.dev/reference/block-kit/blocks)

### Ancestors (2)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Subclasses

* [ActionsBlock](blocks.html#slack_sdk.models.blocks.blocks.ActionsBlock "slack_sdk.models.blocks.blocks.ActionsBlock")
* [CallBlock](blocks.html#slack_sdk.models.blocks.blocks.CallBlock "slack_sdk.models.blocks.blocks.CallBlock")
* [ContextActionsBlock](blocks.html#slack_sdk.models.blocks.blocks.ContextActionsBlock "slack_sdk.models.blocks.blocks.ContextActionsBlock")
* [ContextBlock](blocks.html#slack_sdk.models.blocks.blocks.ContextBlock "slack_sdk.models.blocks.blocks.ContextBlock")
* [DividerBlock](blocks.html#slack_sdk.models.blocks.blocks.DividerBlock "slack_sdk.models.blocks.blocks.DividerBlock")
* [FileBlock](blocks.html#slack_sdk.models.blocks.blocks.FileBlock "slack_sdk.models.blocks.blocks.FileBlock")
* [HeaderBlock](blocks.html#slack_sdk.models.blocks.blocks.HeaderBlock "slack_sdk.models.blocks.blocks.HeaderBlock")
* [ImageBlock](blocks.html#slack_sdk.models.blocks.blocks.ImageBlock "slack_sdk.models.blocks.blocks.ImageBlock")
* [InputBlock](blocks.html#slack_sdk.models.blocks.blocks.InputBlock "slack_sdk.models.blocks.blocks.InputBlock")
* [MarkdownBlock](blocks.html#slack_sdk.models.blocks.blocks.MarkdownBlock "slack_sdk.models.blocks.blocks.MarkdownBlock")
* [PlanBlock](blocks.html#slack_sdk.models.blocks.blocks.PlanBlock "slack_sdk.models.blocks.blocks.PlanBlock")
* [RichTextBlock](blocks.html#slack_sdk.models.blocks.blocks.RichTextBlock "slack_sdk.models.blocks.blocks.RichTextBlock")
* [SectionBlock](blocks.html#slack_sdk.models.blocks.blocks.SectionBlock "slack_sdk.models.blocks.blocks.SectionBlock")
* [TableBlock](blocks.html#slack_sdk.models.blocks.blocks.TableBlock "slack_sdk.models.blocks.blocks.TableBlock")
* [TaskCardBlock](blocks.html#slack_sdk.models.blocks.blocks.TaskCardBlock "slack_sdk.models.blocks.blocks.TaskCardBlock")
* [VideoBlock](blocks.html#slack_sdk.models.blocks.blocks.VideoBlock "slack_sdk.models.blocks.blocks.VideoBlock")

### Class variables (2)

`var attributes`

The type of the None singleton.

`var block_id_max_length`

The type of the None singleton.

`var logger`

The type of the None singleton.

### Static methods

`def parse(block: dict | [Block](#slack_sdk.models.blocks.Block "slack_sdk.models.blocks.Block")) ‑> [Block](blocks.html#slack_sdk.models.blocks.blocks.Block "slack_sdk.models.blocks.blocks.Block") | None`

`def parse_all(blocks: Sequence[dict | [Block](#slack_sdk.models.blocks.Block "slack_sdk.models.blocks.Block")] | None) ‑> List[[Block](blocks.html#slack_sdk.models.blocks.blocks.Block "slack_sdk.models.blocks.blocks.Block")]`

### Instance variables (2)

`prop subtype : str | None`

Expand source code

```python
@property
def subtype(self) -> Optional[str]:
    return self.type
```

### Inherited members (2)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class BlockElement (*, type: str | None = None, subtype: str | None = None, **others: dict)`

Expand source code

```typescript
class BlockElement(JsonObject, metaclass=ABCMeta):
    """Block Elements are things that exists inside of your Blocks.
    https://docs.slack.dev/reference/block-kit/block-elements/
    """

    attributes = {"type"}
    logger = logging.getLogger(__name__)

    def _subtype_warning(self):
        warnings.warn(
            "subtype is deprecated since slackclient 2.6.0, use type instead",
            DeprecationWarning,
        )

    @property
    def subtype(self) -> Optional[str]:
        return self.type

    def __init__(
        self,
        *,
        type: Optional[str] = None,
        subtype: Optional[str] = None,
        **others: dict,
    ):
        if subtype:
            self._subtype_warning()
        self.type = type if type else subtype
        show_unknown_key_warning(self, others)

    @classmethod
    def parse(cls, block_element: Union[dict, "BlockElement"]) -> Optional[Union["BlockElement", TextObject]]:
        if block_element is None:
            return None
        elif isinstance(block_element, dict):
            if "type" in block_element:
                d = copy.copy(block_element)
                t = d.pop("type")
                for subclass in cls._get_sub_block_elements():
                    if t == subclass.type:
                        return subclass(**d)
                if t == PlainTextObject.type:
                    return PlainTextObject(**d)
                elif t == MarkdownTextObject.type:
                    return MarkdownTextObject(**d)
        elif isinstance(block_element, (TextObject, BlockElement)):
            return block_element
        cls.logger.warning(f"Unknown element detected and skipped ({block_element})")
        return None

    @classmethod
    def parse_all(
        cls, block_elements: Sequence[Union[dict, "BlockElement", TextObject]]
    ) -> List[Union["BlockElement", TextObject]]:
        return [cls.parse(e) for e in block_elements or []]  # type: ignore[arg-type, misc]

    @classmethod
    def _get_sub_block_elements(cls: Type["BlockElement"]) -> Iterator[Type["BlockElement"]]:
        for subclass in cls.__subclasses__():
            if hasattr(subclass, "type"):
                yield subclass
            yield from subclass._get_sub_block_elements()
```

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

### Ancestors (3)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Subclasses (2)

* [ImageElement](block_elements.html#slack_sdk.models.blocks.block_elements.ImageElement "slack_sdk.models.blocks.block_elements.ImageElement")
* [InteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement "slack_sdk.models.blocks.block_elements.InteractiveElement")
* [RichTextElement](block_elements.html#slack_sdk.models.blocks.block_elements.RichTextElement "slack_sdk.models.blocks.block_elements.RichTextElement")
* [UrlSourceElement](block_elements.html#slack_sdk.models.blocks.block_elements.UrlSourceElement "slack_sdk.models.blocks.block_elements.UrlSourceElement")

### Class variables (3)

`var attributes`

The type of the None singleton.

`var logger`

The type of the None singleton.

### Static methods (2)

`def parse(block_element: dict | [BlockElement](#slack_sdk.models.blocks.BlockElement "slack_sdk.models.blocks.BlockElement")) ‑> [BlockElement](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement") | [TextObject](basic_components.html#slack_sdk.models.blocks.basic_components.TextObject "slack_sdk.models.blocks.basic_components.TextObject") | None`

`def parse_all(block_elements: Sequence[dict | [BlockElement](#slack_sdk.models.blocks.BlockElement "slack_sdk.models.blocks.BlockElement") | [TextObject](basic_components.html#slack_sdk.models.blocks.basic_components.TextObject "slack_sdk.models.blocks.basic_components.TextObject")]) ‑> List[[BlockElement](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement") | [TextObject](basic_components.html#slack_sdk.models.blocks.basic_components.TextObject "slack_sdk.models.blocks.basic_components.TextObject")]`

### Instance variables (3)

`prop subtype : str | None`

Expand source code

```python
@property
def subtype(self) -> Optional[str]:
    return self.type
```

### Inherited members (3)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class ButtonElement (*,   text: str | dict | [TextObject](basic_components.html#slack_sdk.models.blocks.basic_components.TextObject "slack_sdk.models.blocks.basic_components.TextObject"),   action_id: str | None = None,   url: str | None = None,   value: str | None = None,   style: str | None = None,   confirm: dict | [ConfirmObject](basic_components.html#slack_sdk.models.blocks.basic_components.ConfirmObject "slack_sdk.models.blocks.basic_components.ConfirmObject") | None = None,   accessibility_label: str | None = None,   **others: dict)`

Expand source code

```typescript
class ButtonElement(InteractiveElement):
    type = "button"
    text_max_length = 75
    url_max_length = 3000
    value_max_length = 2000

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union({"text", "url", "value", "style", "confirm", "accessibility_label"})

    def __init__(
        self,
        *,
        text: Union[str, dict, TextObject],
        action_id: Optional[str] = None,
        url: Optional[str] = None,
        value: Optional[str] = None,
        style: Optional[str] = None,  # primary, danger
        confirm: Optional[Union[dict, ConfirmObject]] = None,
        accessibility_label: Optional[str] = None,
        **others: dict,
    ):
        """An interactive element that inserts a button. The button can be a trigger for
        anything from opening a simple link to starting a complex workflow.
        https://docs.slack.dev/reference/block-kit/block-elements/button-element/

        Args:
            text (required): A text object that defines the button's text.
                Can only be of type: plain_text.
                Maximum length for the text in this field is 75 characters.
            action_id (required): An identifier for this action.
                You can use this when you receive an interaction payload to identify the source of the action.
                Should be unique among all other action_ids in the containing block.
                Maximum length for this field is 255 characters.
            url: A URL to load in the user's browser when the button is clicked.
                Maximum length for this field is 3000 characters.
                If you're using url, you'll still receive an interaction payload
                and will need to send an acknowledgement response.
            value: The value to send along with the interaction payload.
                Maximum length for this field is 2000 characters.
            style: Decorates buttons with alternative visual color schemes. Use this option with restraint.
                "primary" gives buttons a green outline and text, ideal for affirmation or confirmation actions.
                "primary" should only be used for one button within a set.
                "danger" gives buttons a red outline and text, and should be used when the action is destructive.
                Use "danger" even more sparingly than "primary".
                If you don't include this field, the default button style will be used.
            confirm: A confirm object that defines an optional confirmation dialog after the button is clicked.
            accessibility_label: A label for longer descriptive text about a button element.
                This label will be read out by screen readers instead of the button text object.
                Maximum length for this field is 75 characters.
        """
        super().__init__(action_id=action_id, type=self.type)
        show_unknown_key_warning(self, others)

        # NOTE: default_type=PlainTextObject.type here is only for backward-compatibility with version 2.5.0
        self.text = TextObject.parse(text, default_type=PlainTextObject.type)
        self.url = url
        self.value = value
        self.style = style
        self.confirm = ConfirmObject.parse(confirm)  # type: ignore[arg-type]
        self.accessibility_label = accessibility_label

    @JsonValidator(f"text attribute cannot exceed {text_max_length} characters")
    def _validate_text_length(self) -> bool:
        return self.text is None or self.text.text is None or len(self.text.text) <= self.text_max_length

    @JsonValidator(f"url attribute cannot exceed {url_max_length} characters")
    def _validate_url_length(self) -> bool:
        return self.url is None or len(self.url) <= self.url_max_length

    @JsonValidator(f"value attribute cannot exceed {value_max_length} characters")
    def _validate_value_length(self) -> bool:
        return self.value is None or len(self.value) <= self.value_max_length

    @EnumValidator("style", ButtonStyles)
    def _validate_style_valid(self):
        return self.style is None or self.style in ButtonStyles

    @JsonValidator(f"accessibility_label attribute cannot exceed {text_max_length} characters")
    def _validate_accessibility_label_length(self) -> bool:
        return self.accessibility_label is None or len(self.accessibility_label) <= self.text_max_length
```

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

An interactive element that inserts a button. The button can be a trigger for anything from opening a simple link to starting a complex workflow. [https://docs.slack.dev/reference/block-kit/block-elements/button-element/](https://docs.slack.dev/reference/block-kit/block-elements/button-element/)

## Args (2)

**`text`** : `required`

A text object that defines the button's text. Can only be of type: plain\_text. Maximum length for the text in this field is 75 characters.

**`action_id`** : `required`

An identifier for this action. You can use this when you receive an interaction payload to identify the source of the action. Should be unique among all other action\_ids in the containing block. Maximum length for this field is 255 characters.

**`url`**

A URL to load in the user's browser when the button is clicked. Maximum length for this field is 3000 characters. If you're using url, you'll still receive an interaction payload and will need to send an acknowledgement response.

**`value`**

The value to send along with the interaction payload. Maximum length for this field is 2000 characters.

**`style`**

Decorates buttons with alternative visual color schemes. Use this option with restraint. "primary" gives buttons a green outline and text, ideal for affirmation or confirmation actions. "primary" should only be used for one button within a set. "danger" gives buttons a red outline and text, and should be used when the action is destructive. Use "danger" even more sparingly than "primary". If you don't include this field, the default button style will be used.

**`confirm`**

A confirm object that defines an optional confirmation dialog after the button is clicked.

**`accessibility_label`**

A label for longer descriptive text about a button element. This label will be read out by screen readers instead of the button text object. Maximum length for this field is 75 characters.

### Ancestors (4)

* [InteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement "slack_sdk.models.blocks.block_elements.InteractiveElement")
* [BlockElement](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Subclasses (3)

* [LinkButtonElement](block_elements.html#slack_sdk.models.blocks.block_elements.LinkButtonElement "slack_sdk.models.blocks.block_elements.LinkButtonElement")

### Class variables (4)

`var text_max_length`

The type of the None singleton.

`var type`

The type of the None singleton.

`var url_max_length`

The type of the None singleton.

`var value_max_length`

The type of the None singleton.

### Inherited members (4)

* `**[InteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement "slack_sdk.models.blocks.block_elements.InteractiveElement")**`:
  * `[action_id_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement.action_id_max_length "slack_sdk.models.blocks.block_elements.InteractiveElement.action_id_max_length")`
  * `[attributes](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement.attributes "slack_sdk.models.blocks.block_elements.InteractiveElement.attributes")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.block_elements.InteractiveElement.get_non_null_attributes")`
  * `[logger](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement.logger "slack_sdk.models.blocks.block_elements.InteractiveElement.logger")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.block_elements.InteractiveElement.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.block_elements.InteractiveElement.validate_json")`

`class CallBlock (*,   call_id: str,   api_decoration_available: bool | None = None,   call: Dict[str, Dict[str, Any]] | None = None,   block_id: str | None = None,   **others: dict)`

Expand source code

```typescript
class CallBlock(Block):
    type = "call"

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union({"call_id", "api_decoration_available", "call"})

    def __init__(
        self,
        *,
        call_id: str,
        api_decoration_available: Optional[bool] = None,
        call: Optional[Dict[str, Dict[str, Any]]] = None,
        block_id: Optional[str] = None,
        **others: dict,
    ):
        """Displays a call information
        https://docs.slack.dev/reference/block-kit/blocks#call
        """
        super().__init__(type=self.type, block_id=block_id)
        show_unknown_key_warning(self, others)

        self.call_id = call_id
        self.api_decoration_available = api_decoration_available
        self.call = call
```

Blocks are a series of components that can be combined to create visually rich and compellingly interactive messages. [https://docs.slack.dev/reference/block-kit/blocks](https://docs.slack.dev/reference/block-kit/blocks)

Displays a call information [https://docs.slack.dev/reference/block-kit/blocks#call](https://docs.slack.dev/reference/block-kit/blocks#call)

### Ancestors (5)

* [Block](blocks.html#slack_sdk.models.blocks.blocks.Block "slack_sdk.models.blocks.blocks.Block")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (5)

`var type`

The type of the None singleton.

### Instance variables (4)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union({"call_id", "api_decoration_available", "call"})
```

Build an unordered collection of unique elements.

### Inherited members (5)

* `**[Block](blocks.html#slack_sdk.models.blocks.blocks.Block "slack_sdk.models.blocks.blocks.Block")**`:
  * `[block_id_max_length](blocks.html#slack_sdk.models.blocks.blocks.Block.block_id_max_length "slack_sdk.models.blocks.blocks.Block.block_id_max_length")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.blocks.Block.get_non_null_attributes")`
  * `[logger](blocks.html#slack_sdk.models.blocks.blocks.Block.logger "slack_sdk.models.blocks.blocks.Block.logger")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.blocks.Block.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.blocks.Block.validate_json")`

`class ChannelMultiSelectElement (*,   placeholder: str | dict | [TextObject](basic_components.html#slack_sdk.models.blocks.basic_components.TextObject "slack_sdk.models.blocks.basic_components.TextObject") | None = None,   action_id: str | None = None,   initial_channels: Sequence[str] | None = None,   confirm: dict | [ConfirmObject](basic_components.html#slack_sdk.models.blocks.basic_components.ConfirmObject "slack_sdk.models.blocks.basic_components.ConfirmObject") | None = None,   max_selected_items: int | None = None,   focus_on_load: bool | None = None,   **others: dict)`

Expand source code

```typescript
class ChannelMultiSelectElement(InputInteractiveElement):
    type = "multi_channels_select"

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union({"initial_channels", "max_selected_items"})

    def __init__(
        self,
        *,
        placeholder: Optional[Union[str, dict, TextObject]] = None,
        action_id: Optional[str] = None,
        initial_channels: Optional[Sequence[str]] = None,
        confirm: Optional[Union[dict, ConfirmObject]] = None,
        max_selected_items: Optional[int] = None,
        focus_on_load: Optional[bool] = None,
        **others: dict,
    ):
        """
        This multi-select menu will populate its options with a list of public channels visible
        to the current user in the active workspace.
        https://docs.slack.dev/reference/block-kit/block-elements/multi-select-menu-element#channel_multi_select

        Args:
            placeholder (required): A plain_text only text object that defines the placeholder text shown on the menu.
                Maximum length for the text in this field is 150 characters.
            action_id (required): An identifier for the action triggered when a menu option is selected.
                You can use this when you receive an interaction payload to identify the source of the action.
                Should be unique among all other action_ids in the containing block.
                Maximum length for this field is 255 characters.
            initial_channels: An array of one or more IDs of any valid public channel
                to be pre-selected when the menu loads.
            confirm: A confirm object that defines an optional confirmation dialog that appears
                before the multi-select choices are submitted.
            max_selected_items: Specifies the maximum number of items that can be selected in the menu.
                Minimum number is 1.
            focus_on_load: Indicates whether the element will be set to auto focus within the view object.
                Only one element can be set to true. Defaults to false.
        """
        super().__init__(
            type=self.type,
            action_id=action_id,
            placeholder=TextObject.parse(placeholder, PlainTextObject.type),  # type: ignore[arg-type]
            confirm=ConfirmObject.parse(confirm),  # type: ignore[arg-type]
            focus_on_load=focus_on_load,
        )
        show_unknown_key_warning(self, others)

        self.initial_channels = initial_channels
        self.max_selected_items = max_selected_items
```

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

This multi-select menu will populate its options with a list of public channels visible to the current user in the active workspace. [https://docs.slack.dev/reference/block-kit/block-elements/multi-select-menu-element#channel\_multi\_select](https://docs.slack.dev/reference/block-kit/block-elements/multi-select-menu-element#channel_multi_select)

## Args (3)

**`placeholder`** : `required`

A plain\_text only text object that defines the placeholder text shown on the menu. Maximum length for the text in this field is 150 characters.

**`action_id`** : `required`

An identifier for the action triggered when a menu option is selected. You can use this when you receive an interaction payload to identify the source of the action. Should be unique among all other action\_ids in the containing block. Maximum length for this field is 255 characters.

**`initial_channels`**

An array of one or more IDs of any valid public channel to be pre-selected when the menu loads.

**`confirm`**

A confirm object that defines an optional confirmation dialog that appears before the multi-select choices are submitted.

**`max_selected_items`**

Specifies the maximum number of items that can be selected in the menu. Minimum number is 1.

**`focus_on_load`**

Indicates whether the element will be set to auto focus within the view object. Only one element can be set to true. Defaults to false.

### Ancestors (6)

* [InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")
* [InteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement "slack_sdk.models.blocks.block_elements.InteractiveElement")
* [BlockElement](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (6)

`var type`

The type of the None singleton.

### Instance variables (5)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union({"initial_channels", "max_selected_items"})
```

Build an unordered collection of unique elements.

### Inherited members (6)

* `**[InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")**`:
  * `[action_id_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement.action_id_max_length "slack_sdk.models.blocks.block_elements.InputInteractiveElement.action_id_max_length")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.block_elements.InputInteractiveElement.get_non_null_attributes")`
  * `[logger](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement.logger "slack_sdk.models.blocks.block_elements.InputInteractiveElement.logger")`
  * `[placeholder_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement.placeholder_max_length "slack_sdk.models.blocks.block_elements.InputInteractiveElement.placeholder_max_length")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.block_elements.InputInteractiveElement.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.block_elements.InputInteractiveElement.validate_json")`

`class ChannelSelectElement (*,   placeholder: str | dict | [TextObject](basic_components.html#slack_sdk.models.blocks.basic_components.TextObject "slack_sdk.models.blocks.basic_components.TextObject") | None = None,   action_id: str | None = None,   initial_channel: str | None = None,   confirm: dict | [ConfirmObject](basic_components.html#slack_sdk.models.blocks.basic_components.ConfirmObject "slack_sdk.models.blocks.basic_components.ConfirmObject") | None = None,   response_url_enabled: bool | None = None,   focus_on_load: bool | None = None,   **others: dict)`

Expand source code

```typescript
class ChannelSelectElement(InputInteractiveElement):
    type = "channels_select"

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union({"initial_channel", "response_url_enabled"})

    def __init__(
        self,
        *,
        placeholder: Optional[Union[str, dict, TextObject]] = None,
        action_id: Optional[str] = None,
        initial_channel: Optional[str] = None,
        confirm: Optional[Union[dict, ConfirmObject]] = None,
        response_url_enabled: Optional[bool] = None,
        focus_on_load: Optional[bool] = None,
        **others: dict,
    ):
        """
        This select menu will populate its options with a list of public channels
        visible to the current user in the active workspace.
        https://docs.slack.dev/reference/block-kit/block-elements/select-menu-element/#channels_select

        Args:
            placeholder (required): A plain_text only text object that defines the placeholder text shown on the menu.
                Maximum length for the text in this field is 150 characters.
            action_id (required): An identifier for the action triggered when a menu option is selected.
                You can use this when you receive an interaction payload to identify the source of the action.
                Should be unique among all other action_ids in the containing block.
                Maximum length for this field is 255 characters.
            initial_channel: The ID of any valid public channel to be pre-selected when the menu loads.
            confirm: A confirm object that defines an optional confirmation dialog that appears
                after a menu item is selected.
            response_url_enabled: This field only works with menus in input blocks in modals.
                When set to true, the view_submission payload from the menu's parent view will contain a response_url.
                This response_url can be used for message responses.
                The target channel for the message will be determined by the value of this select menu
            focus_on_load: Indicates whether the element will be set to auto focus within the view object.
                Only one element can be set to true. Defaults to false.
        """
        super().__init__(
            type=self.type,
            action_id=action_id,
            placeholder=TextObject.parse(placeholder, PlainTextObject.type),  # type: ignore[arg-type]
            confirm=ConfirmObject.parse(confirm),  # type: ignore[arg-type]
            focus_on_load=focus_on_load,
        )
        show_unknown_key_warning(self, others)

        self.initial_channel = initial_channel
        self.response_url_enabled = response_url_enabled
```

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

This select menu will populate its options with a list of public channels visible to the current user in the active workspace. [https://docs.slack.dev/reference/block-kit/block-elements/select-menu-element/#channels\_select](https://docs.slack.dev/reference/block-kit/block-elements/select-menu-element/#channels_select)

## Args (4)

**`placeholder`** : `required`

A plain\_text only text object that defines the placeholder text shown on the menu. Maximum length for the text in this field is 150 characters.

**`action_id`** : `required`

An identifier for the action triggered when a menu option is selected. You can use this when you receive an interaction payload to identify the source of the action. Should be unique among all other action\_ids in the containing block. Maximum length for this field is 255 characters.

**`initial_channel`**

The ID of any valid public channel to be pre-selected when the menu loads.

**`confirm`**

A confirm object that defines an optional confirmation dialog that appears after a menu item is selected.

**`response_url_enabled`**

This field only works with menus in input blocks in modals. When set to true, the view\_submission payload from the menu's parent view will contain a response\_url. This response\_url can be used for message responses. The target channel for the message will be determined by the value of this select menu

**`focus_on_load`**

Indicates whether the element will be set to auto focus within the view object. Only one element can be set to true. Defaults to false.

### Ancestors (7)

* [InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")
* [InteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement "slack_sdk.models.blocks.block_elements.InteractiveElement")
* [BlockElement](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (7)

`var type`

The type of the None singleton.

### Instance variables (6)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union({"initial_channel", "response_url_enabled"})
```

Build an unordered collection of unique elements.

### Inherited members (7)

* `**[InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")**`:
  * `[action_id_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement.action_id_max_length "slack_sdk.models.blocks.block_elements.InputInteractiveElement.action_id_max_length")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.block_elements.InputInteractiveElement.get_non_null_attributes")`
  * `[logger](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement.logger "slack_sdk.models.blocks.block_elements.InputInteractiveElement.logger")`
  * `[placeholder_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement.placeholder_max_length "slack_sdk.models.blocks.block_elements.InputInteractiveElement.placeholder_max_length")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.block_elements.InputInteractiveElement.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.block_elements.InputInteractiveElement.validate_json")`

`class CheckboxesElement (*,   action_id: str | None = None,   options: Sequence[dict | [Option](basic_components.html#slack_sdk.models.blocks.basic_components.Option "slack_sdk.models.blocks.basic_components.Option")] | None = None,   initial_options: Sequence[dict | [Option](basic_components.html#slack_sdk.models.blocks.basic_components.Option "slack_sdk.models.blocks.basic_components.Option")] | None = None,   confirm: dict | [ConfirmObject](basic_components.html#slack_sdk.models.blocks.basic_components.ConfirmObject "slack_sdk.models.blocks.basic_components.ConfirmObject") | None = None,   focus_on_load: bool | None = None,   **others: dict)`

Expand source code

```typescript
class CheckboxesElement(InputInteractiveElement):
    type = "checkboxes"

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union({"options", "initial_options"})

    def __init__(
        self,
        *,
        action_id: Optional[str] = None,
        options: Optional[Sequence[Union[dict, Option]]] = None,
        initial_options: Optional[Sequence[Union[dict, Option]]] = None,
        confirm: Optional[Union[dict, ConfirmObject]] = None,
        focus_on_load: Optional[bool] = None,
        **others: dict,
    ):
        """A checkbox group that allows a user to choose multiple items from a list of possible options.
        https://docs.slack.dev/reference/block-kit/block-elements/checkboxes-element/

        Args:
            action_id (required): An identifier for the action triggered when the checkbox group is changed.
                You can use this when you receive an interaction payload to identify the source of the action.
                Should be unique among all other action_ids in the containing block.
                Maximum length for this field is 255 characters.
            options (required): An array of option objects. A maximum of 10 options are allowed.
            initial_options: An array of option objects that exactly matches one or more of the options.
                These options will be selected when the checkbox group initially loads.
            confirm: A confirm object that defines an optional confirmation dialog that appears
                after clicking one of the checkboxes in this element.
            focus_on_load: Indicates whether the element will be set to auto focus within the view object.
                Only one element can be set to true. Defaults to false.
        """
        super().__init__(
            type=self.type,
            action_id=action_id,
            confirm=ConfirmObject.parse(confirm),  # type: ignore[arg-type]
            focus_on_load=focus_on_load,
        )
        show_unknown_key_warning(self, others)

        self.options = Option.parse_all(options)
        self.initial_options = Option.parse_all(initial_options)
```

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

A checkbox group that allows a user to choose multiple items from a list of possible options. [https://docs.slack.dev/reference/block-kit/block-elements/checkboxes-element/](https://docs.slack.dev/reference/block-kit/block-elements/checkboxes-element/)

## Args (5)

**`action_id`** : `required`

An identifier for the action triggered when the checkbox group is changed. You can use this when you receive an interaction payload to identify the source of the action. Should be unique among all other action\_ids in the containing block. Maximum length for this field is 255 characters.

**`options`** : `required`

An array of option objects. A maximum of 10 options are allowed.

**`initial_options`**

An array of option objects that exactly matches one or more of the options. These options will be selected when the checkbox group initially loads.

**`confirm`**

A confirm object that defines an optional confirmation dialog that appears after clicking one of the checkboxes in this element.

**`focus_on_load`**

Indicates whether the element will be set to auto focus within the view object. Only one element can be set to true. Defaults to false.

### Ancestors (8)

* [InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")
* [InteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement "slack_sdk.models.blocks.block_elements.InteractiveElement")
* [BlockElement](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (8)

`var type`

The type of the None singleton.

### Instance variables (7)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union({"options", "initial_options"})
```

Build an unordered collection of unique elements.

### Inherited members (8)

* `**[InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")**`:
  * `[action_id_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement.action_id_max_length "slack_sdk.models.blocks.block_elements.InputInteractiveElement.action_id_max_length")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.block_elements.InputInteractiveElement.get_non_null_attributes")`
  * `[logger](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement.logger "slack_sdk.models.blocks.block_elements.InputInteractiveElement.logger")`
  * `[placeholder_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement.placeholder_max_length "slack_sdk.models.blocks.block_elements.InputInteractiveElement.placeholder_max_length")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.block_elements.InputInteractiveElement.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.block_elements.InputInteractiveElement.validate_json")`

`class ConfirmObject (*,   title: str | Dict[str, Any] | [PlainTextObject](basic_components.html#slack_sdk.models.blocks.basic_components.PlainTextObject "slack_sdk.models.blocks.basic_components.PlainTextObject"),   text: str | Dict[str, Any] | [TextObject](basic_components.html#slack_sdk.models.blocks.basic_components.TextObject "slack_sdk.models.blocks.basic_components.TextObject"),   confirm: str | Dict[str, Any] | [PlainTextObject](basic_components.html#slack_sdk.models.blocks.basic_components.PlainTextObject "slack_sdk.models.blocks.basic_components.PlainTextObject") = 'Yes',   deny: str | Dict[str, Any] | [PlainTextObject](basic_components.html#slack_sdk.models.blocks.basic_components.PlainTextObject "slack_sdk.models.blocks.basic_components.PlainTextObject") = 'No',   style: str | None = None)`

Expand source code

```typescript
class ConfirmObject(JsonObject):
    attributes: Set[str] = set()

    title_max_length = 100
    text_max_length = 300
    confirm_max_length = 30
    deny_max_length = 30

    @classmethod
    def parse(cls, confirm: Union["ConfirmObject", Dict[str, Any]]):
        if confirm:
            if isinstance(confirm, ConfirmObject):
                return confirm
            elif isinstance(confirm, dict):
                return ConfirmObject(**confirm)
            else:
                # Not yet implemented: show some warning here
                return None
        return None

    def __init__(
        self,
        *,
        title: Union[str, Dict[str, Any], PlainTextObject],
        text: Union[str, Dict[str, Any], TextObject],
        confirm: Union[str, Dict[str, Any], PlainTextObject] = "Yes",
        deny: Union[str, Dict[str, Any], PlainTextObject] = "No",
        style: Optional[str] = None,
    ):
        """
        An object that defines a dialog that provides a confirmation step to any
        interactive element. This dialog will ask the user to confirm their action by
        offering a confirm and deny button.
        https://docs.slack.dev/reference/block-kit/composition-objects/confirmation-dialog-object/
        """
        self._title = TextObject.parse(title, default_type=PlainTextObject.type)
        self._text = TextObject.parse(text, default_type=MarkdownTextObject.type)
        self._confirm = TextObject.parse(confirm, default_type=PlainTextObject.type)
        self._deny = TextObject.parse(deny, default_type=PlainTextObject.type)
        self._style = style

        # for backward-compatibility with version 2.0-2.5, the following fields return str values
        self.title = self._title.text if self._title else None
        self.text = self._text.text if self._text else None
        self.confirm = self._confirm.text if self._confirm else None
        self.deny = self._deny.text if self._deny else None
        self.style = self._style

    @JsonValidator(f"title attribute cannot exceed {title_max_length} characters")
    def title_length(self) -> bool:
        return self._title is None or len(self._title.text) <= self.title_max_length

    @JsonValidator(f"text attribute cannot exceed {text_max_length} characters")
    def text_length(self) -> bool:
        return self._text is None or len(self._text.text) <= self.text_max_length

    @JsonValidator(f"confirm attribute cannot exceed {confirm_max_length} characters")
    def confirm_length(self) -> bool:
        return self._confirm is None or len(self._confirm.text) <= self.confirm_max_length

    @JsonValidator(f"deny attribute cannot exceed {deny_max_length} characters")
    def deny_length(self) -> bool:
        return self._deny is None or len(self._deny.text) <= self.deny_max_length

    @JsonValidator('style for confirm must be either "primary" or "danger"')
    def _validate_confirm_style(self) -> bool:
        return self._style is None or self._style in ["primary", "danger"]

    def to_dict(self, option_type: str = "block") -> Dict[str, Any]:
        if option_type == "action":
            # deliberately skipping JSON validators here - can't find documentation
            # on actual limits here
            json: Dict[str, Union[str, dict]] = {
                "ok_text": self._confirm.text if self._confirm and self._confirm.text != "Yes" else "Okay",
                "dismiss_text": self._deny.text if self._deny and self._deny.text != "No" else "Cancel",
            }
            if self._title:
                json["title"] = self._title.text
            if self._text:
                json["text"] = self._text.text
            return json

        else:
            self.validate_json()
            json = {}
            if self._title:
                json["title"] = self._title.to_dict()
            if self._text:
                json["text"] = self._text.to_dict()
            if self._confirm:
                json["confirm"] = self._confirm.to_dict()
            if self._deny:
                json["deny"] = self._deny.to_dict()
            if self._style:
                json["style"] = self._style
            return json
```

The base class for JSON serializable class objects

An object that defines a dialog that provides a confirmation step to any interactive element. This dialog will ask the user to confirm their action by offering a confirm and deny button. [https://docs.slack.dev/reference/block-kit/composition-objects/confirmation-dialog-object/](https://docs.slack.dev/reference/block-kit/composition-objects/confirmation-dialog-object/)

### Ancestors (9)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (9)

`var attributes : Set[str]`

The type of the None singleton.

`var confirm_max_length`

The type of the None singleton.

`var deny_max_length`

The type of the None singleton.

`var text_max_length`

The type of the None singleton.

`var title_max_length`

The type of the None singleton.

### Static methods (3)

`def parse(confirm: [ConfirmObject](#slack_sdk.models.blocks.ConfirmObject "slack_sdk.models.blocks.ConfirmObject") | Dict[str, Any])`

### Methods

`def confirm_length(self) ‑> bool`

Expand source code

```python
@JsonValidator(f"confirm attribute cannot exceed {confirm_max_length} characters")
def confirm_length(self) -> bool:
    return self._confirm is None or len(self._confirm.text) <= self.confirm_max_length
```

`def deny_length(self) ‑> bool`

Expand source code

```python
@JsonValidator(f"deny attribute cannot exceed {deny_max_length} characters")
def deny_length(self) -> bool:
    return self._deny is None or len(self._deny.text) <= self.deny_max_length
```

`def text_length(self) ‑> bool`

Expand source code

```python
@JsonValidator(f"text attribute cannot exceed {text_max_length} characters")
def text_length(self) -> bool:
    return self._text is None or len(self._text.text) <= self.text_max_length
```

`def title_length(self) ‑> bool`

Expand source code

```python
@JsonValidator(f"title attribute cannot exceed {title_max_length} characters")
def title_length(self) -> bool:
    return self._title is None or len(self._title.text) <= self.title_max_length
```

### Inherited members (9)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class ContextActionsBlock (*,   elements: Sequence[dict | [FeedbackButtonsElement](block_elements.html#slack_sdk.models.blocks.block_elements.FeedbackButtonsElement "slack_sdk.models.blocks.block_elements.FeedbackButtonsElement") | [IconButtonElement](block_elements.html#slack_sdk.models.blocks.block_elements.IconButtonElement "slack_sdk.models.blocks.block_elements.IconButtonElement")],   block_id: str | None = None,   **others: dict)`

Expand source code

```typescript
class ContextActionsBlock(Block):
    type = "context_actions"
    elements_max_length = 5

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union({"elements"})

    def __init__(
        self,
        *,
        elements: Sequence[Union[dict, FeedbackButtonsElement, IconButtonElement]],
        block_id: Optional[str] = None,
        **others: dict,
    ):
        """Displays actions as contextual info, which can include both feedback buttons and icon buttons.
        https://docs.slack.dev/reference/block-kit/blocks/context-actions-block

        Args:
            elements (required): An array of feedback_buttons or icon_button block elements. Maximum number of items is 5.
            block_id: A string acting as a unique identifier for a block. If not specified, one will be generated.
                Maximum length for this field is 255 characters.
                block_id should be unique for each message and each iteration of a message.
                If a message is updated, use a new block_id.
        """
        super().__init__(type=self.type, block_id=block_id)
        show_unknown_key_warning(self, others)

        self.elements = BlockElement.parse_all(elements)

    @JsonValidator("elements attribute must be specified")
    def _validate_elements(self):
        return self.elements is None or len(self.elements) > 0

    @JsonValidator(f"elements attribute cannot exceed {elements_max_length} elements")
    def _validate_elements_length(self):
        return self.elements is None or len(self.elements) <= self.elements_max_length
```

Blocks are a series of components that can be combined to create visually rich and compellingly interactive messages. [https://docs.slack.dev/reference/block-kit/blocks](https://docs.slack.dev/reference/block-kit/blocks)

Displays actions as contextual info, which can include both feedback buttons and icon buttons. [https://docs.slack.dev/reference/block-kit/blocks/context-actions-block](https://docs.slack.dev/reference/block-kit/blocks/context-actions-block)

## Args (6)

**`elements`** : `required`

An array of feedback\_buttons or icon\_button block elements. Maximum number of items is 5.

**`block_id`**

A string acting as a unique identifier for a block. If not specified, one will be generated. Maximum length for this field is 255 characters. block\_id should be unique for each message and each iteration of a message. If a message is updated, use a new block\_id.

### Ancestors (10)

* [Block](blocks.html#slack_sdk.models.blocks.blocks.Block "slack_sdk.models.blocks.blocks.Block")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (10)

`var elements_max_length`

The type of the None singleton.

`var type`

The type of the None singleton.

### Instance variables (8)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union({"elements"})
```

Build an unordered collection of unique elements.

### Inherited members (10)

* `**[Block](blocks.html#slack_sdk.models.blocks.blocks.Block "slack_sdk.models.blocks.blocks.Block")**`:
  * `[block_id_max_length](blocks.html#slack_sdk.models.blocks.blocks.Block.block_id_max_length "slack_sdk.models.blocks.blocks.Block.block_id_max_length")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.blocks.Block.get_non_null_attributes")`
  * `[logger](blocks.html#slack_sdk.models.blocks.blocks.Block.logger "slack_sdk.models.blocks.blocks.Block.logger")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.blocks.Block.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.blocks.Block.validate_json")`

`class ContextBlock (*,   elements: Sequence[dict | [ImageElement](block_elements.html#slack_sdk.models.blocks.block_elements.ImageElement "slack_sdk.models.blocks.block_elements.ImageElement") | [TextObject](basic_components.html#slack_sdk.models.blocks.basic_components.TextObject "slack_sdk.models.blocks.basic_components.TextObject")],   block_id: str | None = None,   **others: dict)`

Expand source code

```typescript
class ContextBlock(Block):
    type = "context"
    elements_max_length = 10

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union({"elements"})

    def __init__(
        self,
        *,
        elements: Sequence[Union[dict, ImageElement, TextObject]],
        block_id: Optional[str] = None,
        **others: dict,
    ):
        """Displays message context, which can include both images and text.
        https://docs.slack.dev/reference/block-kit/blocks/context-block

        Args:
            elements (required): An array of image elements and text objects. Maximum number of items is 10.
            block_id: A string acting as a unique identifier for a block. If not specified, one will be generated.
                Maximum length for this field is 255 characters.
                block_id should be unique for each message and each iteration of a message.
                If a message is updated, use a new block_id.
        """
        super().__init__(type=self.type, block_id=block_id)
        show_unknown_key_warning(self, others)

        self.elements = BlockElement.parse_all(elements)

    @JsonValidator(f"elements attribute cannot exceed {elements_max_length} elements")
    def _validate_elements_length(self):
        return self.elements is None or len(self.elements) <= self.elements_max_length
```

Blocks are a series of components that can be combined to create visually rich and compellingly interactive messages. [https://docs.slack.dev/reference/block-kit/blocks](https://docs.slack.dev/reference/block-kit/blocks)

Displays message context, which can include both images and text. [https://docs.slack.dev/reference/block-kit/blocks/context-block](https://docs.slack.dev/reference/block-kit/blocks/context-block)

## Args (7)

**`elements`** : `required`

An array of image elements and text objects. Maximum number of items is 10.

**`block_id`**

A string acting as a unique identifier for a block. If not specified, one will be generated. Maximum length for this field is 255 characters. block\_id should be unique for each message and each iteration of a message. If a message is updated, use a new block\_id.

### Ancestors (11)

* [Block](blocks.html#slack_sdk.models.blocks.blocks.Block "slack_sdk.models.blocks.blocks.Block")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (11)

`var elements_max_length`

The type of the None singleton.

`var type`

The type of the None singleton.

### Instance variables (9)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union({"elements"})
```

Build an unordered collection of unique elements.

### Inherited members (11)

* `**[Block](blocks.html#slack_sdk.models.blocks.blocks.Block "slack_sdk.models.blocks.blocks.Block")**`:
  * `[block_id_max_length](blocks.html#slack_sdk.models.blocks.blocks.Block.block_id_max_length "slack_sdk.models.blocks.blocks.Block.block_id_max_length")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.blocks.Block.get_non_null_attributes")`
  * `[logger](blocks.html#slack_sdk.models.blocks.blocks.Block.logger "slack_sdk.models.blocks.blocks.Block.logger")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.blocks.Block.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.blocks.Block.validate_json")`

`class ConversationFilter (*,   include: Sequence[str] | None = None,   exclude_bot_users: bool | None = None,   exclude_external_shared_channels: bool | None = None)`

Expand source code

```typescript
class ConversationFilter(JsonObject):
    attributes = {"include", "exclude_bot_users", "exclude_external_shared_channels"}
    logger = logging.getLogger(__name__)

    def __init__(
        self,
        *,
        include: Optional[Sequence[str]] = None,
        exclude_bot_users: Optional[bool] = None,
        exclude_external_shared_channels: Optional[bool] = None,
    ):
        """Provides a way to filter the list of options in a conversations select menu
        or conversations multi-select menu.
        https://docs.slack.dev/reference/block-kit/composition-objects/conversation-filter-object

        Args:
            include: Indicates which type of conversations should be included in the list.
                When this field is provided, any conversations that do not match will be excluded.
                You should provide an array of strings from the following options:
                "im", "mpim", "private", and "public". The array cannot be empty.
            exclude_bot_users: Indicates whether to exclude bot users from conversation lists. Defaults to false.
            exclude_external_shared_channels: Indicates whether to exclude external shared channels
                from conversation lists. Defaults to false.
        """
        self.include = include
        self.exclude_bot_users = exclude_bot_users
        self.exclude_external_shared_channels = exclude_external_shared_channels

    @classmethod
    def parse(cls, filter: Union[dict, "ConversationFilter"]):
        if filter is None:
            return None
        elif isinstance(filter, ConversationFilter):
            return filter
        elif isinstance(filter, dict):
            d = copy.copy(filter)
            return ConversationFilter(**d)
        else:
            cls.logger.warning(f"Unknown conversation filter object detected and skipped ({filter})")
            return None
```

The base class for JSON serializable class objects

Provides a way to filter the list of options in a conversations select menu or conversations multi-select menu. [https://docs.slack.dev/reference/block-kit/composition-objects/conversation-filter-object](https://docs.slack.dev/reference/block-kit/composition-objects/conversation-filter-object)

## Args (8)

**`include`**

Indicates which type of conversations should be included in the list. When this field is provided, any conversations that do not match will be excluded. You should provide an array of strings from the following options: "im", "mpim", "private", and "public". The array cannot be empty.

**`exclude_bot_users`**

Indicates whether to exclude bot users from conversation lists. Defaults to false.

**`exclude_external_shared_channels`**

Indicates whether to exclude external shared channels from conversation lists. Defaults to false.

### Ancestors (12)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (12)

`var attributes`

The type of the None singleton.

`var logger`

The type of the None singleton.

### Static methods (4)

`def parse(filter: dict | [ConversationFilter](#slack_sdk.models.blocks.ConversationFilter "slack_sdk.models.blocks.ConversationFilter"))`

### Inherited members (12)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class ConversationMultiSelectElement (*,   placeholder: str | dict | [TextObject](basic_components.html#slack_sdk.models.blocks.basic_components.TextObject "slack_sdk.models.blocks.basic_components.TextObject") | None = None,   action_id: str | None = None,   initial_conversations: Sequence[str] | None = None,   confirm: dict | [ConfirmObject](basic_components.html#slack_sdk.models.blocks.basic_components.ConfirmObject "slack_sdk.models.blocks.basic_components.ConfirmObject") | None = None,   max_selected_items: int | None = None,   default_to_current_conversation: bool | None = None,   filter: dict | [ConversationFilter](block_elements.html#slack_sdk.models.blocks.block_elements.ConversationFilter "slack_sdk.models.blocks.block_elements.ConversationFilter") | None = None,   focus_on_load: bool | None = None,   **others: dict)`

Expand source code

```typescript
class ConversationMultiSelectElement(InputInteractiveElement):
    type = "multi_conversations_select"

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union(
            {
                "initial_conversations",
                "max_selected_items",
                "default_to_current_conversation",
                "filter",
            }
        )

    def __init__(
        self,
        *,
        placeholder: Optional[Union[str, dict, TextObject]] = None,
        action_id: Optional[str] = None,
        initial_conversations: Optional[Sequence[str]] = None,
        confirm: Optional[Union[dict, ConfirmObject]] = None,
        max_selected_items: Optional[int] = None,
        default_to_current_conversation: Optional[bool] = None,
        filter: Optional[Union[dict, ConversationFilter]] = None,
        focus_on_load: Optional[bool] = None,
        **others: dict,
    ):
        """
        This multi-select menu will populate its options with a list of public and private channels,
        DMs, and MPIMs visible to the current user in the active workspace.
        https://docs.slack.dev/reference/block-kit/block-elements/multi-select-menu-element/#conversation_multi_select

        Args:
            placeholder (required): A plain_text only text object that defines the placeholder text shown on the menu.
                Maximum length for the text in this field is 150 characters.
            action_id (required): An identifier for the action triggered when a menu option is selected.
                You can use this when you receive an interaction payload to identify the source of the action.
                Should be unique among all other action_ids in the containing block.
                Maximum length for this field is 255 characters.
            initial_conversations: An array of one or more IDs of any valid conversations to be pre-selected
                when the menu loads. If default_to_current_conversation is also supplied,
                initial_conversations will be ignored.
            confirm: A confirm object that defines an optional confirmation dialog that appears
                before the multi-select choices are submitted.
            max_selected_items: Specifies the maximum number of items that can be selected in the menu.
                Minimum number is 1.
            default_to_current_conversation: Pre-populates the select menu with the conversation that
                the user was viewing when they opened the modal, if available. Default is false.
            filter: A filter object that reduces the list of available conversations using the specified criteria.
            focus_on_load: Indicates whether the element will be set to auto focus within the view object.
                Only one element can be set to true. Defaults to false.
        """
        super().__init__(
            type=self.type,
            action_id=action_id,
            placeholder=TextObject.parse(placeholder, PlainTextObject.type),  # type: ignore[arg-type]
            confirm=ConfirmObject.parse(confirm),  # type: ignore[arg-type]
            focus_on_load=focus_on_load,
        )
        show_unknown_key_warning(self, others)

        self.initial_conversations = initial_conversations
        self.max_selected_items = max_selected_items
        self.default_to_current_conversation = default_to_current_conversation
        self.filter = ConversationFilter.parse(filter)  # type: ignore[arg-type]
```

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

This multi-select menu will populate its options with a list of public and private channels, DMs, and MPIMs visible to the current user in the active workspace. [https://docs.slack.dev/reference/block-kit/block-elements/multi-select-menu-element/#conversation\_multi\_select](https://docs.slack.dev/reference/block-kit/block-elements/multi-select-menu-element/#conversation_multi_select)

## Args (9)

**`placeholder`** : `required`

A plain\_text only text object that defines the placeholder text shown on the menu. Maximum length for the text in this field is 150 characters.

**`action_id`** : `required`

An identifier for the action triggered when a menu option is selected. You can use this when you receive an interaction payload to identify the source of the action. Should be unique among all other action\_ids in the containing block. Maximum length for this field is 255 characters.

**`initial_conversations`**

An array of one or more IDs of any valid conversations to be pre-selected when the menu loads. If default\_to\_current\_conversation is also supplied, initial\_conversations will be ignored.

**`confirm`**

A confirm object that defines an optional confirmation dialog that appears before the multi-select choices are submitted.

**`max_selected_items`**

Specifies the maximum number of items that can be selected in the menu. Minimum number is 1.

**`default_to_current_conversation`**

Pre-populates the select menu with the conversation that the user was viewing when they opened the modal, if available. Default is false.

**`filter`**

A filter object that reduces the list of available conversations using the specified criteria.

**`focus_on_load`**

Indicates whether the element will be set to auto focus within the view object. Only one element can be set to true. Defaults to false.

### Ancestors (13)

* [InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")
* [InteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement "slack_sdk.models.blocks.block_elements.InteractiveElement")
* [BlockElement](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (13)

`var type`

The type of the None singleton.

### Instance variables (10)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union(
        {
            "initial_conversations",
            "max_selected_items",
            "default_to_current_conversation",
            "filter",
        }
    )
```

Build an unordered collection of unique elements.

### Inherited members (13)

* `**[InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")**`:
  * `[action_id_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement.action_id_max_length "slack_sdk.models.blocks.block_elements.InputInteractiveElement.action_id_max_length")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.block_elements.InputInteractiveElement.get_non_null_attributes")`
  * `[logger](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement.logger "slack_sdk.models.blocks.block_elements.InputInteractiveElement.logger")`
  * `[placeholder_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement.placeholder_max_length "slack_sdk.models.blocks.block_elements.InputInteractiveElement.placeholder_max_length")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.block_elements.InputInteractiveElement.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.block_elements.InputInteractiveElement.validate_json")`

`class ConversationSelectElement (*,   placeholder: str | dict | [TextObject](basic_components.html#slack_sdk.models.blocks.basic_components.TextObject "slack_sdk.models.blocks.basic_components.TextObject") | None = None,   action_id: str | None = None,   initial_conversation: str | None = None,   confirm: dict | [ConfirmObject](basic_components.html#slack_sdk.models.blocks.basic_components.ConfirmObject "slack_sdk.models.blocks.basic_components.ConfirmObject") | None = None,   response_url_enabled: bool | None = None,   default_to_current_conversation: bool | None = None,   filter: [ConversationFilter](block_elements.html#slack_sdk.models.blocks.block_elements.ConversationFilter "slack_sdk.models.blocks.block_elements.ConversationFilter") | None = None,   focus_on_load: bool | None = None,   **others: dict)`

Expand source code

```typescript
class ConversationSelectElement(InputInteractiveElement):
    type = "conversations_select"

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union(
            {
                "initial_conversation",
                "response_url_enabled",
                "filter",
                "default_to_current_conversation",
            }
        )

    def __init__(
        self,
        *,
        placeholder: Optional[Union[str, dict, TextObject]] = None,
        action_id: Optional[str] = None,
        initial_conversation: Optional[str] = None,
        confirm: Optional[Union[dict, ConfirmObject]] = None,
        response_url_enabled: Optional[bool] = None,
        default_to_current_conversation: Optional[bool] = None,
        filter: Optional[ConversationFilter] = None,
        focus_on_load: Optional[bool] = None,
        **others: dict,
    ):
        """
        This select menu will populate its options with a list of public and private
        channels, DMs, and MPIMs visible to the current user in the active workspace.
        https://docs.slack.dev/reference/block-kit/block-elements/select-menu-element/#conversations_select

        Args:
            placeholder (required): A plain_text only text object that defines the placeholder text shown on the menu.
                Maximum length for the text in this field is 150 characters.
            action_id (required): An identifier for the action triggered when a menu option is selected.
                You can use this when you receive an interaction payload to identify the source of the action.
                Should be unique among all other action_ids in the containing block.
                Maximum length for this field is 255 characters.
            initial_conversation: The ID of any valid conversation to be pre-selected when the menu loads.
                If default_to_current_conversation is also supplied, initial_conversation will take precedence.
            confirm: A confirm object that defines an optional confirmation dialog
                that appears after a menu item is selected.
            response_url_enabled: This field only works with menus in input blocks in modals.
                When set to true, the view_submission payload from the menu's parent view will contain a response_url.
                This response_url can be used for message responses. The target conversation for the message
                will be determined by the value of this select menu.
            default_to_current_conversation: Pre-populates the select menu with the conversation
                that the user was viewing when they opened the modal, if available. Default is false.
            filter: A filter object that reduces the list of available conversations using the specified criteria.
            focus_on_load: Indicates whether the element will be set to auto focus within the view object.
                Only one element can be set to true. Defaults to false.
        """
        super().__init__(
            type=self.type,
            action_id=action_id,
            placeholder=TextObject.parse(placeholder, PlainTextObject.type),  # type: ignore[arg-type]
            confirm=ConfirmObject.parse(confirm),  # type: ignore[arg-type]
            focus_on_load=focus_on_load,
        )
        show_unknown_key_warning(self, others)

        self.initial_conversation = initial_conversation
        self.response_url_enabled = response_url_enabled
        self.default_to_current_conversation = default_to_current_conversation
        self.filter = filter
```

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

This select menu will populate its options with a list of public and private channels, DMs, and MPIMs visible to the current user in the active workspace. [https://docs.slack.dev/reference/block-kit/block-elements/select-menu-element/#conversations\_select](https://docs.slack.dev/reference/block-kit/block-elements/select-menu-element/#conversations_select)

## Args (10)

**`placeholder`** : `required`

A plain\_text only text object that defines the placeholder text shown on the menu. Maximum length for the text in this field is 150 characters.

**`action_id`** : `required`

An identifier for the action triggered when a menu option is selected. You can use this when you receive an interaction payload to identify the source of the action. Should be unique among all other action\_ids in the containing block. Maximum length for this field is 255 characters.

**`initial_conversation`**

The ID of any valid conversation to be pre-selected when the menu loads. If default\_to\_current\_conversation is also supplied, initial\_conversation will take precedence.

**`confirm`**

A confirm object that defines an optional confirmation dialog that appears after a menu item is selected.

**`response_url_enabled`**

This field only works with menus in input blocks in modals. When set to true, the view\_submission payload from the menu's parent view will contain a response\_url. This response\_url can be used for message responses. The target conversation for the message will be determined by the value of this select menu.

**`default_to_current_conversation`**

Pre-populates the select menu with the conversation that the user was viewing when they opened the modal, if available. Default is false.

**`filter`**

A filter object that reduces the list of available conversations using the specified criteria.

**`focus_on_load`**

Indicates whether the element will be set to auto focus within the view object. Only one element can be set to true. Defaults to false.

### Ancestors (14)

* [InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")
* [InteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement "slack_sdk.models.blocks.block_elements.InteractiveElement")
* [BlockElement](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (14)

`var type`

The type of the None singleton.

### Instance variables (11)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union(
        {
            "initial_conversation",
            "response_url_enabled",
            "filter",
            "default_to_current_conversation",
        }
    )
```

Build an unordered collection of unique elements.

### Inherited members (14)

* `**[InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")**`:
  * `[action_id_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement.action_id_max_length "slack_sdk.models.blocks.block_elements.InputInteractiveElement.action_id_max_length")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.block_elements.InputInteractiveElement.get_non_null_attributes")`
  * `[logger](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement.logger "slack_sdk.models.blocks.block_elements.InputInteractiveElement.logger")`
  * `[placeholder_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement.placeholder_max_length "slack_sdk.models.blocks.block_elements.InputInteractiveElement.placeholder_max_length")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.block_elements.InputInteractiveElement.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.block_elements.InputInteractiveElement.validate_json")`

`class DatePickerElement (*,   action_id: str | None = None,   placeholder: str | dict | [TextObject](basic_components.html#slack_sdk.models.blocks.basic_components.TextObject "slack_sdk.models.blocks.basic_components.TextObject") | None = None,   initial_date: str | None = None,   confirm: dict | [ConfirmObject](basic_components.html#slack_sdk.models.blocks.basic_components.ConfirmObject "slack_sdk.models.blocks.basic_components.ConfirmObject") | None = None,   focus_on_load: bool | None = None,   **others: dict)`

Expand source code

```typescript
class DatePickerElement(InputInteractiveElement):
    type = "datepicker"

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union({"initial_date"})

    def __init__(
        self,
        *,
        action_id: Optional[str] = None,
        placeholder: Optional[Union[str, dict, TextObject]] = None,
        initial_date: Optional[str] = None,
        confirm: Optional[Union[dict, ConfirmObject]] = None,
        focus_on_load: Optional[bool] = None,
        **others: dict,
    ):
        """
        An element which lets users easily select a date from a calendar style UI.
        Date picker elements can be used inside of SectionBlocks and ActionsBlocks.
        https://docs.slack.dev/reference/block-kit/block-elements/date-picker-element

        Args:
            action_id (required): An identifier for the action triggered when a menu option is selected.
                You can use this when you receive an interaction payload to identify the source of the action.
                Should be unique among all other action_ids in the containing block.
                Maximum length for this field is 255 characters.
            placeholder: A plain_text only text object that defines the placeholder text shown on the datepicker.
                Maximum length for the text in this field is 150 characters.
            initial_date: The initial date that is selected when the element is loaded.
                This should be in the format YYYY-MM-DD.
            confirm: A confirm object that defines an optional confirmation dialog
                that appears after a date is selected.
            focus_on_load: Indicates whether the element will be set to auto focus within the view object.
                Only one element can be set to true. Defaults to false.
        """
        super().__init__(
            type=self.type,
            action_id=action_id,
            placeholder=TextObject.parse(placeholder, PlainTextObject.type),  # type: ignore[arg-type]
            confirm=ConfirmObject.parse(confirm),  # type: ignore[arg-type]
            focus_on_load=focus_on_load,
        )
        show_unknown_key_warning(self, others)

        self.initial_date = initial_date

    @JsonValidator("initial_date attribute must be in format 'YYYY-MM-DD'")
    def _validate_initial_date_valid(self) -> bool:
        return (
            self.initial_date is None
            or re.match(r"\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])", self.initial_date) is not None
        )
```

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

An element which lets users easily select a date from a calendar style UI. Date picker elements can be used inside of SectionBlocks and ActionsBlocks. [https://docs.slack.dev/reference/block-kit/block-elements/date-picker-element](https://docs.slack.dev/reference/block-kit/block-elements/date-picker-element)

## Args (11)

**`action_id`** : `required`

An identifier for the action triggered when a menu option is selected. You can use this when you receive an interaction payload to identify the source of the action. Should be unique among all other action\_ids in the containing block. Maximum length for this field is 255 characters.

**`placeholder`**

A plain\_text only text object that defines the placeholder text shown on the datepicker. Maximum length for the text in this field is 150 characters.

**`initial_date`**

The initial date that is selected when the element is loaded. This should be in the format YYYY-MM-DD.

**`confirm`**

A confirm object that defines an optional confirmation dialog that appears after a date is selected.

**`focus_on_load`**

Indicates whether the element will be set to auto focus within the view object. Only one element can be set to true. Defaults to false.

### Ancestors (15)

* [InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")
* [InteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement "slack_sdk.models.blocks.block_elements.InteractiveElement")
* [BlockElement](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (15)

`var type`

The type of the None singleton.

### Instance variables (12)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union({"initial_date"})
```

Build an unordered collection of unique elements.

### Inherited members (15)

* `**[InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")**`:
  * `[action_id_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement.action_id_max_length "slack_sdk.models.blocks.block_elements.InputInteractiveElement.action_id_max_length")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.block_elements.InputInteractiveElement.get_non_null_attributes")`
  * `[logger](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement.logger "slack_sdk.models.blocks.block_elements.InputInteractiveElement.logger")`
  * `[placeholder_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement.placeholder_max_length "slack_sdk.models.blocks.block_elements.InputInteractiveElement.placeholder_max_length")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.block_elements.InputInteractiveElement.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.block_elements.InputInteractiveElement.validate_json")`

`class DateTimePickerElement (*,   action_id: str | None = None,   initial_date_time: int | None = None,   confirm: dict | [ConfirmObject](basic_components.html#slack_sdk.models.blocks.basic_components.ConfirmObject "slack_sdk.models.blocks.basic_components.ConfirmObject") | None = None,   focus_on_load: bool | None = None,   **others: dict)`

Expand source code

```typescript
class DateTimePickerElement(InputInteractiveElement):
    type = "datetimepicker"

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union({"initial_date_time"})

    def __init__(
        self,
        *,
        action_id: Optional[str] = None,
        initial_date_time: Optional[int] = None,
        confirm: Optional[Union[dict, ConfirmObject]] = None,
        focus_on_load: Optional[bool] = None,
        **others: dict,
    ):
        """
        An element that allows the selection of a time of day formatted as a UNIX timestamp.
        On desktop clients, this time picker will take the form of a dropdown list and the
        date picker will take the form of a dropdown calendar. Both options will have free-text
        entry for precise choices. On mobile clients, the time picker and date
        picker will use native UIs.
        https://docs.slack.dev/reference/block-kit/block-elements/date-picker-element/

        Args:
            action_id (required): An identifier for the action triggered when a time is selected. You can use this
                when you receive an interaction payload to identify the source of the action. Should be unique among
                all other action_ids in the containing block. Maximum length for this field is 255 characters.
            initial_date_time: The initial date and time that is selected when the element is loaded, represented as
                a UNIX timestamp in seconds. This should be in the format of 10 digits, for example 1628633820
                represents the date and time August 10th, 2021 at 03:17pm PST.
                and mm is minutes with leading zeros (00 to 59), for example 22:25 for 10:25pm.
            confirm: A confirm object that defines an optional confirmation dialog
                that appears after a time is selected.
            focus_on_load: Indicates whether the element will be set to auto focus within the view object.
                Only one element can be set to true. Defaults to false.
        """
        super().__init__(
            type=self.type,
            action_id=action_id,
            confirm=ConfirmObject.parse(confirm),  # type: ignore[arg-type]
            focus_on_load=focus_on_load,
        )
        show_unknown_key_warning(self, others)

        self.initial_date_time = initial_date_time

    @JsonValidator("initial_date_time attribute must be between 0 and 99999999 seconds")
    def _validate_initial_date_time_valid(self) -> bool:
        return self.initial_date_time is None or (0 <= self.initial_date_time <= 9999999999)
```

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

An element that allows the selection of a time of day formatted as a UNIX timestamp. On desktop clients, this time picker will take the form of a dropdown list and the date picker will take the form of a dropdown calendar. Both options will have free-text entry for precise choices. On mobile clients, the time picker and date picker will use native UIs. [https://docs.slack.dev/reference/block-kit/block-elements/date-picker-element/](https://docs.slack.dev/reference/block-kit/block-elements/date-picker-element/)

## Args (12)

**`action_id`** : `required`

An identifier for the action triggered when a time is selected. You can use this when you receive an interaction payload to identify the source of the action. Should be unique among all other action\_ids in the containing block. Maximum length for this field is 255 characters.

**`initial_date_time`**

The initial date and time that is selected when the element is loaded, represented as a UNIX timestamp in seconds. This should be in the format of 10 digits, for example 1628633820 represents the date and time August 10th, 2021 at 03:17pm PST. and mm is minutes with leading zeros (00 to 59), for example 22:25 for 10:25pm.

**`confirm`**

A confirm object that defines an optional confirmation dialog that appears after a time is selected.

**`focus_on_load`**

Indicates whether the element will be set to auto focus within the view object. Only one element can be set to true. Defaults to false.

### Ancestors (16)

* [InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")
* [InteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement "slack_sdk.models.blocks.block_elements.InteractiveElement")
* [BlockElement](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (16)

`var type`

The type of the None singleton.

### Instance variables (13)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union({"initial_date_time"})
```

Build an unordered collection of unique elements.

### Inherited members (16)

* `**[InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")**`:
  * `[action_id_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement.action_id_max_length "slack_sdk.models.blocks.block_elements.InputInteractiveElement.action_id_max_length")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.block_elements.InputInteractiveElement.get_non_null_attributes")`
  * `[logger](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement.logger "slack_sdk.models.blocks.block_elements.InputInteractiveElement.logger")`
  * `[placeholder_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement.placeholder_max_length "slack_sdk.models.blocks.block_elements.InputInteractiveElement.placeholder_max_length")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.block_elements.InputInteractiveElement.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.block_elements.InputInteractiveElement.validate_json")`

`class DividerBlock (*, block_id: str | None = None, **others: dict)`

Expand source code

```typescript
class DividerBlock(Block):
    type = "divider"

    def __init__(
        self,
        *,
        block_id: Optional[str] = None,
        **others: dict,
    ):
        """A content divider, like an <hr>, to split up different blocks inside of a message.
        https://docs.slack.dev/reference/block-kit/blocks/divider-block

        Args:
            block_id: A string acting as a unique identifier for a block. If not specified, one will be generated.
                You can use this block_id when you receive an interaction payload to identify the source of the action.
                Maximum length for this field is 255 characters.
                block_id should be unique for each message and each iteration of a message.
                If a message is updated, use a new block_id.
        """
        super().__init__(type=self.type, block_id=block_id)
        show_unknown_key_warning(self, others)
```

Blocks are a series of components that can be combined to create visually rich and compellingly interactive messages. [https://docs.slack.dev/reference/block-kit/blocks](https://docs.slack.dev/reference/block-kit/blocks)

A content divider, like an

* * *

, to split up different blocks inside of a message. [https://docs.slack.dev/reference/block-kit/blocks/divider-block](https://docs.slack.dev/reference/block-kit/blocks/divider-block)

## Args (13)

**`block_id`**

A string acting as a unique identifier for a block. If not specified, one will be generated. You can use this block\_id when you receive an interaction payload to identify the source of the action. Maximum length for this field is 255 characters. block\_id should be unique for each message and each iteration of a message. If a message is updated, use a new block\_id.

### Ancestors (17)

* [Block](blocks.html#slack_sdk.models.blocks.blocks.Block "slack_sdk.models.blocks.blocks.Block")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (17)

`var type`

The type of the None singleton.

### Inherited members (17)

* `**[Block](blocks.html#slack_sdk.models.blocks.blocks.Block "slack_sdk.models.blocks.blocks.Block")**`:
  * `[attributes](blocks.html#slack_sdk.models.blocks.blocks.Block.attributes "slack_sdk.models.blocks.blocks.Block.attributes")`
  * `[block_id_max_length](blocks.html#slack_sdk.models.blocks.blocks.Block.block_id_max_length "slack_sdk.models.blocks.blocks.Block.block_id_max_length")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.blocks.Block.get_non_null_attributes")`
  * `[logger](blocks.html#slack_sdk.models.blocks.blocks.Block.logger "slack_sdk.models.blocks.blocks.Block.logger")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.blocks.Block.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.blocks.Block.validate_json")`

`class EmailInputElement (*,   action_id: str | None = None,   initial_value: str | None = None,   dispatch_action_config: dict | [DispatchActionConfig](basic_components.html#slack_sdk.models.blocks.basic_components.DispatchActionConfig "slack_sdk.models.blocks.basic_components.DispatchActionConfig") | None = None,   focus_on_load: bool | None = None,   placeholder: str | dict | [TextObject](basic_components.html#slack_sdk.models.blocks.basic_components.TextObject "slack_sdk.models.blocks.basic_components.TextObject") | None = None,   **others: dict)`

Expand source code

```typescript
class EmailInputElement(InputInteractiveElement):
    type = "email_text_input"

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union(
            {
                "initial_value",
                "dispatch_action_config",
            }
        )

    def __init__(
        self,
        *,
        action_id: Optional[str] = None,
        initial_value: Optional[str] = None,
        dispatch_action_config: Optional[Union[dict, DispatchActionConfig]] = None,
        focus_on_load: Optional[bool] = None,
        placeholder: Optional[Union[str, dict, TextObject]] = None,
        **others: dict,
    ):
        """
        https://docs.slack.dev/reference/block-kit/block-elements/email-input-element

        Args:
            action_id (required): An identifier for the input value when the parent modal is submitted.
                You can use this when you receive a view_submission payload to identify the value of the input element.
                Should be unique among all other action_ids in the containing block.
                Maximum length for this field is 255 characters.
            initial_value: The initial value in the email input when it is loaded.
            dispatch_action_config:  dispatch configuration object that determines when during
                text input the element returns a block_actions payload.
            focus_on_load: Indicates whether the element will be set to auto focus within the view object.
                Only one element can be set to true. Defaults to false.
            placeholder: A plain_text only text object that defines the placeholder text shown in the
                email input. Maximum length for the text in this field is 150 characters.
        """
        super().__init__(
            type=self.type,
            action_id=action_id,
            placeholder=TextObject.parse(placeholder, PlainTextObject.type),  # type: ignore[arg-type]
            focus_on_load=focus_on_load,
        )
        show_unknown_key_warning(self, others)

        self.initial_value = initial_value
        self.dispatch_action_config = dispatch_action_config
```

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

[https://docs.slack.dev/reference/block-kit/block-elements/email-input-element](https://docs.slack.dev/reference/block-kit/block-elements/email-input-element)

## Args (14)

**`action_id`** : `required`

An identifier for the input value when the parent modal is submitted. You can use this when you receive a view\_submission payload to identify the value of the input element. Should be unique among all other action\_ids in the containing block. Maximum length for this field is 255 characters.

**`initial_value`**

The initial value in the email input when it is loaded.

**`dispatch_action_config`**

dispatch configuration object that determines when during text input the element returns a block\_actions payload.

**`focus_on_load`**

Indicates whether the element will be set to auto focus within the view object. Only one element can be set to true. Defaults to false.

**`placeholder`**

A plain\_text only text object that defines the placeholder text shown in the email input. Maximum length for the text in this field is 150 characters.

### Ancestors (18)

* [InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")
* [InteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement "slack_sdk.models.blocks.block_elements.InteractiveElement")
* [BlockElement](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (18)

`var type`

The type of the None singleton.

### Instance variables (14)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union(
        {
            "initial_value",
            "dispatch_action_config",
        }
    )
```

Build an unordered collection of unique elements.

### Inherited members (18)

* `**[InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")**`:
  * `[action_id_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement.action_id_max_length "slack_sdk.models.blocks.block_elements.InputInteractiveElement.action_id_max_length")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.block_elements.InputInteractiveElement.get_non_null_attributes")`
  * `[logger](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement.logger "slack_sdk.models.blocks.block_elements.InputInteractiveElement.logger")`
  * `[placeholder_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement.placeholder_max_length "slack_sdk.models.blocks.block_elements.InputInteractiveElement.placeholder_max_length")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.block_elements.InputInteractiveElement.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.block_elements.InputInteractiveElement.validate_json")`

`class ExternalDataMultiSelectElement (*,   placeholder: str | dict | [TextObject](basic_components.html#slack_sdk.models.blocks.basic_components.TextObject "slack_sdk.models.blocks.basic_components.TextObject") | None = None,   action_id: str | None = None,   min_query_length: int | None = None,   initial_options: Sequence[dict | [Option](basic_components.html#slack_sdk.models.blocks.basic_components.Option "slack_sdk.models.blocks.basic_components.Option")] | None = None,   confirm: dict | [ConfirmObject](basic_components.html#slack_sdk.models.blocks.basic_components.ConfirmObject "slack_sdk.models.blocks.basic_components.ConfirmObject") | None = None,   max_selected_items: int | None = None,   focus_on_load: bool | None = None,   **others: dict)`

Expand source code

```typescript
class ExternalDataMultiSelectElement(InputInteractiveElement):
    type = "multi_external_select"

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union({"min_query_length", "initial_options", "max_selected_items"})

    def __init__(
        self,
        *,
        placeholder: Optional[Union[str, dict, TextObject]] = None,
        action_id: Optional[str] = None,
        min_query_length: Optional[int] = None,
        initial_options: Optional[Sequence[Union[dict, Option]]] = None,
        confirm: Optional[Union[dict, ConfirmObject]] = None,
        max_selected_items: Optional[int] = None,
        focus_on_load: Optional[bool] = None,
        **others: dict,
    ):
        """
        This select menu will load its options from an external data source, allowing
        for a dynamic list of options.
        https://docs.slack.dev/reference/block-kit/block-elements/multi-select-menu-element#external_multi_select

        Args:
            placeholder (required): A plain_text only text object that defines the placeholder text shown on the menu.
                Maximum length for the text in this field is 150 characters.
            action_id (required): An identifier for the action triggered when a menu option is selected.
                You can use this when you receive an interaction payload to identify the source of the action.
                Should be unique among all other action_ids in the containing block.
                Maximum length for this field is 255 characters.
            min_query_length: When the typeahead field is used, a request will be sent on every character change.
                If you prefer fewer requests or more fully ideated queries,
                use the min_query_length attribute to tell Slack
                the fewest number of typed characters required before dispatch.
                The default value is 3
            initial_options: An array of option objects that exactly match one or more of the options
                within options or option_groups. These options will be selected when the menu initially loads.
            confirm: A confirm object that defines an optional confirmation dialog that appears
                before the multi-select choices are submitted.
            max_selected_items: Specifies the maximum number of items that can be selected in the menu.
                Minimum number is 1.
            focus_on_load: Indicates whether the element will be set to auto focus within the view object.
                Only one element can be set to true. Defaults to false.
        """
        super().__init__(
            type=self.type,
            action_id=action_id,
            placeholder=TextObject.parse(placeholder, PlainTextObject.type),  # type: ignore[arg-type]
            confirm=ConfirmObject.parse(confirm),  # type: ignore[arg-type]
            focus_on_load=focus_on_load,
        )
        show_unknown_key_warning(self, others)

        self.min_query_length = min_query_length
        self.initial_options = Option.parse_all(initial_options)
        self.max_selected_items = max_selected_items
```

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

This select menu will load its options from an external data source, allowing for a dynamic list of options. [https://docs.slack.dev/reference/block-kit/block-elements/multi-select-menu-element#external\_multi\_select](https://docs.slack.dev/reference/block-kit/block-elements/multi-select-menu-element#external_multi_select)

## Args (15)

**`placeholder`** : `required`

A plain\_text only text object that defines the placeholder text shown on the menu. Maximum length for the text in this field is 150 characters.

**`action_id`** : `required`

An identifier for the action triggered when a menu option is selected. You can use this when you receive an interaction payload to identify the source of the action. Should be unique among all other action\_ids in the containing block. Maximum length for this field is 255 characters.

**`min_query_length`**

When the typeahead field is used, a request will be sent on every character change. If you prefer fewer requests or more fully ideated queries, use the min\_query\_length attribute to tell Slack the fewest number of typed characters required before dispatch. The default value is 3

**`initial_options`**

An array of option objects that exactly match one or more of the options within options or option\_groups. These options will be selected when the menu initially loads.

**`confirm`**

A confirm object that defines an optional confirmation dialog that appears before the multi-select choices are submitted.

**`max_selected_items`**

Specifies the maximum number of items that can be selected in the menu. Minimum number is 1.

**`focus_on_load`**

Indicates whether the element will be set to auto focus within the view object. Only one element can be set to true. Defaults to false.

### Ancestors (19)

* [InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")
* [InteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement "slack_sdk.models.blocks.block_elements.InteractiveElement")
* [BlockElement](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (19)

`var type`

The type of the None singleton.

### Instance variables (15)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union({"min_query_length", "initial_options", "max_selected_items"})
```

Build an unordered collection of unique elements.

### Inherited members (19)

* `**[InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")**`:
  * `[action_id_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement.action_id_max_length "slack_sdk.models.blocks.block_elements.InputInteractiveElement.action_id_max_length")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.block_elements.InputInteractiveElement.get_non_null_attributes")`
  * `[logger](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement.logger "slack_sdk.models.blocks.block_elements.InputInteractiveElement.logger")`
  * `[placeholder_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement.placeholder_max_length "slack_sdk.models.blocks.block_elements.InputInteractiveElement.placeholder_max_length")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.block_elements.InputInteractiveElement.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.block_elements.InputInteractiveElement.validate_json")`

`class ExternalDataSelectElement (*,   action_id: str | None = None,   placeholder: str | [TextObject](basic_components.html#slack_sdk.models.blocks.basic_components.TextObject "slack_sdk.models.blocks.basic_components.TextObject") | None = None,   initial_option: [Option](basic_components.html#slack_sdk.models.blocks.basic_components.Option "slack_sdk.models.blocks.basic_components.Option") | [OptionGroup](basic_components.html#slack_sdk.models.blocks.basic_components.OptionGroup "slack_sdk.models.blocks.basic_components.OptionGroup") | None = None,   min_query_length: int | None = None,   confirm: dict | [ConfirmObject](basic_components.html#slack_sdk.models.blocks.basic_components.ConfirmObject "slack_sdk.models.blocks.basic_components.ConfirmObject") | None = None,   focus_on_load: bool | None = None,   **others: dict)`

Expand source code

```typescript
class ExternalDataSelectElement(InputInteractiveElement):
    type = "external_select"

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union({"min_query_length", "initial_option"})

    def __init__(
        self,
        *,
        action_id: Optional[str] = None,
        placeholder: Optional[Union[str, TextObject]] = None,
        initial_option: Union[Optional[Option], Optional[OptionGroup]] = None,
        min_query_length: Optional[int] = None,
        confirm: Optional[Union[dict, ConfirmObject]] = None,
        focus_on_load: Optional[bool] = None,
        **others: dict,
    ):
        """
        This select menu will load its options from an external data source, allowing
        for a dynamic list of options.
        https://docs.slack.dev/reference/block-kit/block-elements/select-menu-element#external_select

        Args:
            action_id (required): An identifier for the action triggered when a menu option is selected.
                You can use this when you receive an interaction payload to identify the source of the action.
                Should be unique among all other action_ids in the containing block.
                Maximum length for this field is 255 characters.
            placeholder (required): A plain_text only text object that defines the placeholder text shown on the menu.
                Maximum length for the text in this field is 150 characters.
            initial_option: A single option that exactly matches one of the options
                within the options or option_groups loaded from the external data source.
                This option will be selected when the menu initially loads.
            min_query_length: When the typeahead field is used, a request will be sent on every character change.
                If you prefer fewer requests or more fully ideated queries,
                use the min_query_length attribute to tell Slack
                the fewest number of typed characters required before dispatch.
                The default value is 3.
            confirm: A confirm object that defines an optional confirmation dialog
                that appears after a menu item is selected.
            focus_on_load: Indicates whether the element will be set to auto focus within the view object.
                Only one element can be set to true. Defaults to false.
        """
        super().__init__(
            type=self.type,
            action_id=action_id,
            placeholder=TextObject.parse(placeholder, PlainTextObject.type),  # type: ignore[arg-type]
            confirm=ConfirmObject.parse(confirm),  # type: ignore[arg-type]
            focus_on_load=focus_on_load,
        )
        show_unknown_key_warning(self, others)

        self.min_query_length = min_query_length
        self.initial_option = initial_option
```

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

This select menu will load its options from an external data source, allowing for a dynamic list of options. [https://docs.slack.dev/reference/block-kit/block-elements/select-menu-element#external\_select](https://docs.slack.dev/reference/block-kit/block-elements/select-menu-element#external_select)

## Args (16)

**`action_id`** : `required`

An identifier for the action triggered when a menu option is selected. You can use this when you receive an interaction payload to identify the source of the action. Should be unique among all other action\_ids in the containing block. Maximum length for this field is 255 characters.

**`placeholder`** : `required`

A plain\_text only text object that defines the placeholder text shown on the menu. Maximum length for the text in this field is 150 characters.

**`initial_option`**

A single option that exactly matches one of the options within the options or option\_groups loaded from the external data source. This option will be selected when the menu initially loads.

**`min_query_length`**

When the typeahead field is used, a request will be sent on every character change. If you prefer fewer requests or more fully ideated queries, use the min\_query\_length attribute to tell Slack the fewest number of typed characters required before dispatch. The default value is 3.

**`confirm`**

A confirm object that defines an optional confirmation dialog that appears after a menu item is selected.

**`focus_on_load`**

Indicates whether the element will be set to auto focus within the view object. Only one element can be set to true. Defaults to false.

### Ancestors (20)

* [InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")
* [InteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement "slack_sdk.models.blocks.block_elements.InteractiveElement")
* [BlockElement](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (20)

`var type`

The type of the None singleton.

### Instance variables (16)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union({"min_query_length", "initial_option"})
```

Build an unordered collection of unique elements.

### Inherited members (20)

* `**[InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")**`:
  * `[action_id_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement.action_id_max_length "slack_sdk.models.blocks.block_elements.InputInteractiveElement.action_id_max_length")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.block_elements.InputInteractiveElement.get_non_null_attributes")`
  * `[logger](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement.logger "slack_sdk.models.blocks.block_elements.InputInteractiveElement.logger")`
  * `[placeholder_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement.placeholder_max_length "slack_sdk.models.blocks.block_elements.InputInteractiveElement.placeholder_max_length")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.block_elements.InputInteractiveElement.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.block_elements.InputInteractiveElement.validate_json")`

`class FeedbackButtonObject (*,   text: str | Dict[str, Any] | [PlainTextObject](basic_components.html#slack_sdk.models.blocks.basic_components.PlainTextObject "slack_sdk.models.blocks.basic_components.PlainTextObject"),   accessibility_label: str | None = None,   value: str,   **others: Dict[str, Any])`

Expand source code

```typescript
class FeedbackButtonObject(JsonObject):
    attributes: Set[str] = set()

    text_max_length = 75
    value_max_length = 2000

    @classmethod
    def parse(cls, feedback_button: Union["FeedbackButtonObject", Dict[str, Any]]):
        if feedback_button:
            if isinstance(feedback_button, FeedbackButtonObject):
                return feedback_button
            elif isinstance(feedback_button, dict):
                return FeedbackButtonObject(**feedback_button)
            else:
                # Not yet implemented: show some warning here
                return None
        return None

    def __init__(
        self,
        *,
        text: Union[str, Dict[str, Any], PlainTextObject],
        accessibility_label: Optional[str] = None,
        value: str,
        **others: Dict[str, Any],
    ):
        """
        A feedback button element object for either positive or negative feedback.
        https://docs.slack.dev/reference/block-kit/block-elements/feedback-buttons-element#button-object-fields

        Args:
            text (required): An object containing some text. Maximum length for this field is 75 characters.
            accessibility_label: A label for longer descriptive text about a button element. This label will be read out by
                screen readers instead of the button `text` object.
            value (required): The button value. Maximum length for this field is 2000 characters.
        """
        self._text: Optional[TextObject] = PlainTextObject.parse(text, default_type=PlainTextObject.type)
        self._accessibility_label: Optional[str] = accessibility_label
        self._value: Optional[str] = value
        show_unknown_key_warning(self, others)

    @JsonValidator(f"text attribute cannot exceed {text_max_length} characters")
    def text_length(self) -> bool:
        return self._text is None or len(self._text.text) <= self.text_max_length

    @JsonValidator(f"value attribute cannot exceed {value_max_length} characters")
    def value_length(self) -> bool:
        return self._value is None or len(self._value) <= self.value_max_length

    def to_dict(self) -> Dict[str, Any]:
        self.validate_json()
        json: Dict[str, Union[str, dict]] = {}
        if self._text:
            json["text"] = self._text.to_dict()
        if self._accessibility_label:
            json["accessibility_label"] = self._accessibility_label
        if self._value:
            json["value"] = self._value
        return json
```

The base class for JSON serializable class objects

A feedback button element object for either positive or negative feedback. [https://docs.slack.dev/reference/block-kit/block-elements/feedback-buttons-element#button-object-fields](https://docs.slack.dev/reference/block-kit/block-elements/feedback-buttons-element#button-object-fields)

## Args (17)

**`text`** : `required`

An object containing some text. Maximum length for this field is 75 characters.

**`accessibility_label`**

A label for longer descriptive text about a button element. This label will be read out by screen readers instead of the button `text` object.

**`value`** : `required`

The button value. Maximum length for this field is 2000 characters.

### Ancestors (21)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (21)

`var attributes : Set[str]`

The type of the None singleton.

`var text_max_length`

The type of the None singleton.

`var value_max_length`

The type of the None singleton.

### Static methods (5)

`def parse(feedback_button: [FeedbackButtonObject](#slack_sdk.models.blocks.FeedbackButtonObject "slack_sdk.models.blocks.FeedbackButtonObject") | Dict[str, Any])`

### Methods (2)

`def text_length(self) ‑> bool`

Expand source code

```python
@JsonValidator(f"text attribute cannot exceed {text_max_length} characters")
def text_length(self) -> bool:
    return self._text is None or len(self._text.text) <= self.text_max_length
```

`def value_length(self) ‑> bool`

Expand source code

```python
@JsonValidator(f"value attribute cannot exceed {value_max_length} characters")
def value_length(self) -> bool:
    return self._value is None or len(self._value) <= self.value_max_length
```

### Inherited members (21)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class FeedbackButtonsElement (*,   action_id: str | None = None,   positive_button: dict | [FeedbackButtonObject](basic_components.html#slack_sdk.models.blocks.basic_components.FeedbackButtonObject "slack_sdk.models.blocks.basic_components.FeedbackButtonObject"),   negative_button: dict | [FeedbackButtonObject](basic_components.html#slack_sdk.models.blocks.basic_components.FeedbackButtonObject "slack_sdk.models.blocks.basic_components.FeedbackButtonObject"),   **others: dict)`

Expand source code

```typescript
class FeedbackButtonsElement(InteractiveElement):
    type = "feedback_buttons"

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union({"positive_button", "negative_button"})

    def __init__(
        self,
        *,
        action_id: Optional[str] = None,
        positive_button: Union[dict, FeedbackButtonObject],
        negative_button: Union[dict, FeedbackButtonObject],
        **others: dict,
    ):
        """Buttons to indicate positive or negative feedback.
        https://docs.slack.dev/reference/block-kit/block-elements/feedback-buttons-element

        Args:
            action_id (required): An identifier for this action.
                You can use this when you receive an interaction payload to identify the source of the action.
                Should be unique among all other action_ids in the containing block.
                Maximum length for this field is 255 characters.
            positive_button (required): A button to indicate positive feedback.
            negative_button (required): A button to indicate negative feedback.
        """
        super().__init__(action_id=action_id, type=self.type)
        show_unknown_key_warning(self, others)

        self.positive_button = FeedbackButtonObject.parse(positive_button)
        self.negative_button = FeedbackButtonObject.parse(negative_button)
```

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

Buttons to indicate positive or negative feedback. [https://docs.slack.dev/reference/block-kit/block-elements/feedback-buttons-element](https://docs.slack.dev/reference/block-kit/block-elements/feedback-buttons-element)

## Args (18)

**`action_id`** : `required`

An identifier for this action. You can use this when you receive an interaction payload to identify the source of the action. Should be unique among all other action\_ids in the containing block. Maximum length for this field is 255 characters.

**`positive_button`** : `required`

A button to indicate positive feedback.

**`negative_button`** : `required`

A button to indicate negative feedback.

### Ancestors (22)

* [InteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement "slack_sdk.models.blocks.block_elements.InteractiveElement")
* [BlockElement](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (22)

`var type`

The type of the None singleton.

### Inherited members (22)

* `**[InteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement "slack_sdk.models.blocks.block_elements.InteractiveElement")**`:
  * `[action_id_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement.action_id_max_length "slack_sdk.models.blocks.block_elements.InteractiveElement.action_id_max_length")`
  * `[attributes](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement.attributes "slack_sdk.models.blocks.block_elements.InteractiveElement.attributes")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.block_elements.InteractiveElement.get_non_null_attributes")`
  * `[logger](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement.logger "slack_sdk.models.blocks.block_elements.InteractiveElement.logger")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.block_elements.InteractiveElement.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.block_elements.InteractiveElement.validate_json")`

`class FileBlock (*,   external_id: str,   source: str = 'remote',   block_id: str | None = None,   **others: dict)`

Expand source code

```typescript
class FileBlock(Block):
    type = "file"

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union({"external_id", "source"})

    def __init__(
        self,
        *,
        external_id: str,
        source: str = "remote",
        block_id: Optional[str] = None,
        **others: dict,
    ):
        """Displays a remote file.
        https://docs.slack.dev/reference/block-kit/blocks/file-block

        Args:
            external_id (required): The external unique ID for this file.
            source (required): At the moment, source will always be remote for a remote file.
            block_id: A string acting as a unique identifier for a block. If not specified, one will be generated.
                Maximum length for this field is 255 characters.
                block_id should be unique for each message and each iteration of a message.
                If a message is updated, use a new block_id.
        """
        super().__init__(type=self.type, block_id=block_id)
        show_unknown_key_warning(self, others)

        self.external_id = external_id
        self.source = source
```

Blocks are a series of components that can be combined to create visually rich and compellingly interactive messages. [https://docs.slack.dev/reference/block-kit/blocks](https://docs.slack.dev/reference/block-kit/blocks)

Displays a remote file. [https://docs.slack.dev/reference/block-kit/blocks/file-block](https://docs.slack.dev/reference/block-kit/blocks/file-block)

## Args (19)

**`external_id`** : `required`

The external unique ID for this file.

**`source`** : `required`

At the moment, source will always be remote for a remote file.

**`block_id`**

A string acting as a unique identifier for a block. If not specified, one will be generated. Maximum length for this field is 255 characters. block\_id should be unique for each message and each iteration of a message. If a message is updated, use a new block\_id.

### Ancestors (23)

* [Block](blocks.html#slack_sdk.models.blocks.blocks.Block "slack_sdk.models.blocks.blocks.Block")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (23)

`var type`

The type of the None singleton.

### Instance variables (17)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union({"external_id", "source"})
```

Build an unordered collection of unique elements.

### Inherited members (23)

* `**[Block](blocks.html#slack_sdk.models.blocks.blocks.Block "slack_sdk.models.blocks.blocks.Block")**`:
  * `[block_id_max_length](blocks.html#slack_sdk.models.blocks.blocks.Block.block_id_max_length "slack_sdk.models.blocks.blocks.Block.block_id_max_length")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.blocks.Block.get_non_null_attributes")`
  * `[logger](blocks.html#slack_sdk.models.blocks.blocks.Block.logger "slack_sdk.models.blocks.blocks.Block.logger")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.blocks.Block.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.blocks.Block.validate_json")`

`class HeaderBlock (*,   block_id: str | None = None,   text: str | dict | [TextObject](basic_components.html#slack_sdk.models.blocks.basic_components.TextObject "slack_sdk.models.blocks.basic_components.TextObject") | None = None,   **others: dict)`

Expand source code

```typescript
class HeaderBlock(Block):
    type = "header"
    text_max_length = 150

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union({"text"})

    def __init__(
        self,
        *,
        block_id: Optional[str] = None,
        text: Optional[Union[str, dict, TextObject]] = None,
        **others: dict,
    ):
        """A header is a plain-text block that displays in a larger, bold font.
        https://docs.slack.dev/reference/block-kit/blocks/header-block

        Args:
            block_id: A string acting as a unique identifier for a block. If not specified, one will be generated.
                Maximum length for this field is 255 characters.
                block_id should be unique for each message and each iteration of a message.
                If a message is updated, use a new block_id.
            text (required): The text for the block, in the form of a plain_text text object.
                Maximum length for the text in this field is 150 characters.
        """
        super().__init__(type=self.type, block_id=block_id)
        show_unknown_key_warning(self, others)

        self.text = TextObject.parse(text, default_type=PlainTextObject.type)  # type: ignore[arg-type]

    @JsonValidator("text attribute must be specified")
    def _validate_text(self):
        return self.text is not None

    @JsonValidator(f"text attribute cannot exceed {text_max_length} characters")
    def _validate_alt_text_length(self):
        return self.text is None or len(self.text.text) <= self.text_max_length
```

Blocks are a series of components that can be combined to create visually rich and compellingly interactive messages. [https://docs.slack.dev/reference/block-kit/blocks](https://docs.slack.dev/reference/block-kit/blocks)

A header is a plain-text block that displays in a larger, bold font. [https://docs.slack.dev/reference/block-kit/blocks/header-block](https://docs.slack.dev/reference/block-kit/blocks/header-block)

## Args (20)

**`block_id`**

A string acting as a unique identifier for a block. If not specified, one will be generated. Maximum length for this field is 255 characters. block\_id should be unique for each message and each iteration of a message. If a message is updated, use a new block\_id.

**`text`** : `required`

The text for the block, in the form of a plain\_text text object. Maximum length for the text in this field is 150 characters.

### Ancestors (24)

* [Block](blocks.html#slack_sdk.models.blocks.blocks.Block "slack_sdk.models.blocks.blocks.Block")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (24)

`var text_max_length`

The type of the None singleton.

`var type`

The type of the None singleton.

### Instance variables (18)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union({"text"})
```

Build an unordered collection of unique elements.

### Inherited members (24)

* `**[Block](blocks.html#slack_sdk.models.blocks.blocks.Block "slack_sdk.models.blocks.blocks.Block")**`:
  * `[block_id_max_length](blocks.html#slack_sdk.models.blocks.blocks.Block.block_id_max_length "slack_sdk.models.blocks.blocks.Block.block_id_max_length")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.blocks.Block.get_non_null_attributes")`
  * `[logger](blocks.html#slack_sdk.models.blocks.blocks.Block.logger "slack_sdk.models.blocks.blocks.Block.logger")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.blocks.Block.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.blocks.Block.validate_json")`

`class IconButtonElement (*,   action_id: str | None = None,   icon: str,   text: str | dict | [TextObject](basic_components.html#slack_sdk.models.blocks.basic_components.TextObject "slack_sdk.models.blocks.basic_components.TextObject"),   accessibility_label: str | None = None,   value: str | None = None,   visible_to_user_ids: List[str] | None = None,   confirm: dict | [ConfirmObject](basic_components.html#slack_sdk.models.blocks.basic_components.ConfirmObject "slack_sdk.models.blocks.basic_components.ConfirmObject") | None = None,   **others: dict)`

Expand source code

```typescript
class IconButtonElement(InteractiveElement):
    type = "icon_button"

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union({"icon", "text", "accessibility_label", "value", "visible_to_user_ids", "confirm"})

    def __init__(
        self,
        *,
        action_id: Optional[str] = None,
        icon: str,
        text: Union[str, dict, TextObject],
        accessibility_label: Optional[str] = None,
        value: Optional[str] = None,
        visible_to_user_ids: Optional[List[str]] = None,
        confirm: Optional[Union[dict, ConfirmObject]] = None,
        **others: dict,
    ):
        """An icon button to perform actions.
        https://docs.slack.dev/reference/block-kit/block-elements/icon-button-element

        Args:
            action_id: An identifier for this action.
                You can use this when you receive an interaction payload to identify the source of the action.
                Should be unique among all other action_ids in the containing block.
                Maximum length for this field is 255 characters.
            icon (required): The icon to show (e.g., 'trash').
            text (required): Defines an object containing some text.
            accessibility_label: A label for longer descriptive text about a button element.
                This label will be read out by screen readers instead of the button text object.
                Maximum length for this field is 75 characters.
            value: The button value.
                Maximum length for this field is 2000 characters.
            visible_to_user_ids: User IDs for which the icon appears.
                Maximum length for this field is 10 user IDs.
            confirm: A confirm object that defines an optional confirmation dialog after the button is clicked.
        """
        super().__init__(action_id=action_id, type=self.type)
        show_unknown_key_warning(self, others)

        self.icon = icon
        self.text = TextObject.parse(text, PlainTextObject.type)
        self.accessibility_label = accessibility_label
        self.value = value
        self.visible_to_user_ids = visible_to_user_ids
        self.confirm = ConfirmObject.parse(confirm) if confirm else None
```

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

An icon button to perform actions. [https://docs.slack.dev/reference/block-kit/block-elements/icon-button-element](https://docs.slack.dev/reference/block-kit/block-elements/icon-button-element)

## Args (21)

**`action_id`**

An identifier for this action. You can use this when you receive an interaction payload to identify the source of the action. Should be unique among all other action\_ids in the containing block. Maximum length for this field is 255 characters.

**`icon`** : `required`

The icon to show (e.g., 'trash').

**`text`** : `required`

Defines an object containing some text.

**`accessibility_label`**

A label for longer descriptive text about a button element. This label will be read out by screen readers instead of the button text object. Maximum length for this field is 75 characters.

**`value`**

The button value. Maximum length for this field is 2000 characters.

**`visible_to_user_ids`**

User IDs for which the icon appears. Maximum length for this field is 10 user IDs.

**`confirm`**

A confirm object that defines an optional confirmation dialog after the button is clicked.

### Ancestors (25)

* [InteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement "slack_sdk.models.blocks.block_elements.InteractiveElement")
* [BlockElement](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (25)

`var type`

The type of the None singleton.

### Inherited members (25)

* `**[InteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement "slack_sdk.models.blocks.block_elements.InteractiveElement")**`:
  * `[action_id_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement.action_id_max_length "slack_sdk.models.blocks.block_elements.InteractiveElement.action_id_max_length")`
  * `[attributes](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement.attributes "slack_sdk.models.blocks.block_elements.InteractiveElement.attributes")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.block_elements.InteractiveElement.get_non_null_attributes")`
  * `[logger](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement.logger "slack_sdk.models.blocks.block_elements.InteractiveElement.logger")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.block_elements.InteractiveElement.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.block_elements.InteractiveElement.validate_json")`

`class ImageBlock (*,   alt_text: str,   image_url: str | None = None,   slack_file: Dict[str, Any] | [SlackFile](basic_components.html#slack_sdk.models.blocks.basic_components.SlackFile "slack_sdk.models.blocks.basic_components.SlackFile") | None = None,   title: str | dict | [PlainTextObject](basic_components.html#slack_sdk.models.blocks.basic_components.PlainTextObject "slack_sdk.models.blocks.basic_components.PlainTextObject") | None = None,   block_id: str | None = None,   **others: dict)`

Expand source code

```typescript
class ImageBlock(Block):
    type = "image"

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union({"alt_text", "image_url", "title", "slack_file"})

    image_url_max_length = 3000
    alt_text_max_length = 2000
    title_max_length = 2000

    def __init__(
        self,
        *,
        alt_text: str,
        image_url: Optional[str] = None,
        slack_file: Optional[Union[Dict[str, Any], SlackFile]] = None,
        title: Optional[Union[str, dict, PlainTextObject]] = None,
        block_id: Optional[str] = None,
        **others: dict,
    ):
        """A simple image block, designed to make those cat photos really pop.
        https://docs.slack.dev/reference/block-kit/blocks/image-block

        Args:
            alt_text (required): A plain-text summary of the image. This should not contain any markup.
                Maximum length for this field is 2000 characters.
            image_url: The URL of the image to be displayed.
                Maximum length for this field is 3000 characters.
            slack_file: A Slack image file object that defines the source of the image.
            title: An optional title for the image in the form of a text object that can only be of type: plain_text.
                Maximum length for the text in this field is 2000 characters.
            block_id: A string acting as a unique identifier for a block. If not specified, one will be generated.
                Maximum length for this field is 255 characters.
                block_id should be unique for each message and each iteration of a message.
                If a message is updated, use a new block_id.
        """
        super().__init__(type=self.type, block_id=block_id)
        show_unknown_key_warning(self, others)

        self.image_url = image_url
        self.alt_text = alt_text
        parsed_title = None
        if title is not None:
            if isinstance(title, str):
                parsed_title = PlainTextObject(text=title)
            elif isinstance(title, dict):
                if title.get("type") != PlainTextObject.type:
                    raise SlackObjectFormationError(f"Unsupported type for title in an image block: {title.get('type')}")
                parsed_title = PlainTextObject(text=title.get("text"), emoji=title.get("emoji"))  # type: ignore[arg-type]
            elif isinstance(title, PlainTextObject):
                parsed_title = title
            else:
                raise SlackObjectFormationError(f"Unsupported type for title in an image block: {type(title)}")
        if slack_file is not None:
            self.slack_file = (
                slack_file if slack_file is None or isinstance(slack_file, SlackFile) else SlackFile(**slack_file)
            )
        self.title = parsed_title

    @JsonValidator(f"image_url attribute cannot exceed {image_url_max_length} characters")
    def _validate_image_url_length(self):
        return self.image_url is None or len(self.image_url) <= self.image_url_max_length

    @JsonValidator(f"alt_text attribute cannot exceed {alt_text_max_length} characters")
    def _validate_alt_text_length(self):
        return len(self.alt_text) <= self.alt_text_max_length

    @JsonValidator(f"title attribute cannot exceed {title_max_length} characters")
    def _validate_title_length(self):
        return self.title is None or self.title.text is None or len(self.title.text) <= self.title_max_length
```

Blocks are a series of components that can be combined to create visually rich and compellingly interactive messages. [https://docs.slack.dev/reference/block-kit/blocks](https://docs.slack.dev/reference/block-kit/blocks)

A simple image block, designed to make those cat photos really pop. [https://docs.slack.dev/reference/block-kit/blocks/image-block](https://docs.slack.dev/reference/block-kit/blocks/image-block)

## Args (22)

**`alt_text`** : `required`

A plain-text summary of the image. This should not contain any markup. Maximum length for this field is 2000 characters.

**`image_url`**

The URL of the image to be displayed. Maximum length for this field is 3000 characters.

**`slack_file`**

A Slack image file object that defines the source of the image.

**`title`**

An optional title for the image in the form of a text object that can only be of type: plain\_text. Maximum length for the text in this field is 2000 characters.

**`block_id`**

A string acting as a unique identifier for a block. If not specified, one will be generated. Maximum length for this field is 255 characters. block\_id should be unique for each message and each iteration of a message. If a message is updated, use a new block\_id.

### Ancestors (26)

* [Block](blocks.html#slack_sdk.models.blocks.blocks.Block "slack_sdk.models.blocks.blocks.Block")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (26)

`var alt_text_max_length`

The type of the None singleton.

`var image_url_max_length`

The type of the None singleton.

`var title_max_length`

The type of the None singleton.

`var type`

The type of the None singleton.

### Instance variables (19)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union({"alt_text", "image_url", "title", "slack_file"})
```

Build an unordered collection of unique elements.

### Inherited members (26)

* `**[Block](blocks.html#slack_sdk.models.blocks.blocks.Block "slack_sdk.models.blocks.blocks.Block")**`:
  * `[block_id_max_length](blocks.html#slack_sdk.models.blocks.blocks.Block.block_id_max_length "slack_sdk.models.blocks.blocks.Block.block_id_max_length")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.blocks.Block.get_non_null_attributes")`
  * `[logger](blocks.html#slack_sdk.models.blocks.blocks.Block.logger "slack_sdk.models.blocks.blocks.Block.logger")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.blocks.Block.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.blocks.Block.validate_json")`

`class ImageElement (*,   alt_text: str | None = None,   image_url: str | None = None,   slack_file: Dict[str, Any] | [SlackFile](basic_components.html#slack_sdk.models.blocks.basic_components.SlackFile "slack_sdk.models.blocks.basic_components.SlackFile") | None = None,   **others: dict)`

Expand source code

```typescript
class ImageElement(BlockElement):
    type = "image"
    image_url_max_length = 3000
    alt_text_max_length = 2000

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union({"alt_text", "image_url", "slack_file"})

    def __init__(
        self,
        *,
        alt_text: Optional[str] = None,
        image_url: Optional[str] = None,
        slack_file: Optional[Union[Dict[str, Any], SlackFile]] = None,
        **others: dict,
    ):
        """An element to insert an image - this element can be used in section and
        context blocks only. If you want a block with only an image in it,
        you're looking for the image block.
        https://docs.slack.dev/reference/block-kit/block-elements/image-element

        Args:
            alt_text (required): A plain-text summary of the image. This should not contain any markup.
            image_url: The URL of the image to be displayed.
            slack_file: A Slack image file object that defines the source of the image.
        """
        super().__init__(type=self.type)
        show_unknown_key_warning(self, others)

        self.image_url = image_url
        self.alt_text = alt_text
        self.slack_file = slack_file if slack_file is None or isinstance(slack_file, SlackFile) else SlackFile(**slack_file)

    @JsonValidator(f"image_url attribute cannot exceed {image_url_max_length} characters")
    def _validate_image_url_length(self) -> bool:
        return self.image_url is None or len(self.image_url) <= self.image_url_max_length

    @JsonValidator(f"alt_text attribute cannot exceed {alt_text_max_length} characters")
    def _validate_alt_text_length(self) -> bool:
        return len(self.alt_text) <= self.alt_text_max_length  # type: ignore[arg-type]
```

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

An element to insert an image - this element can be used in section and context blocks only. If you want a block with only an image in it, you're looking for the image block. [https://docs.slack.dev/reference/block-kit/block-elements/image-element](https://docs.slack.dev/reference/block-kit/block-elements/image-element)

## Args (23)

**`alt_text`** : `required`

A plain-text summary of the image. This should not contain any markup.

**`image_url`**

The URL of the image to be displayed.

**`slack_file`**

A Slack image file object that defines the source of the image.

### Ancestors (27)

* [BlockElement](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (27)

`var alt_text_max_length`

The type of the None singleton.

`var image_url_max_length`

The type of the None singleton.

`var type`

The type of the None singleton.

### Instance variables (20)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union({"alt_text", "image_url", "slack_file"})
```

Build an unordered collection of unique elements.

### Inherited members (27)

* `**[BlockElement](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.block_elements.BlockElement.get_non_null_attributes")`
  * `[logger](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement.logger "slack_sdk.models.blocks.block_elements.BlockElement.logger")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.block_elements.BlockElement.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.block_elements.BlockElement.validate_json")`

`class InputBlock (*,   label: str | dict | [PlainTextObject](basic_components.html#slack_sdk.models.blocks.basic_components.PlainTextObject "slack_sdk.models.blocks.basic_components.PlainTextObject"),   element: str | dict | [InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement"),   block_id: str | None = None,   hint: str | dict | [PlainTextObject](basic_components.html#slack_sdk.models.blocks.basic_components.PlainTextObject "slack_sdk.models.blocks.basic_components.PlainTextObject") | None = None,   dispatch_action: bool | None = None,   optional: bool | None = None,   **others: dict)`

Expand source code

```typescript
class InputBlock(Block):
    type = "input"
    label_max_length = 2000
    hint_max_length = 2000

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union({"label", "hint", "element", "optional", "dispatch_action"})

    def __init__(
        self,
        *,
        label: Union[str, dict, PlainTextObject],
        element: Union[str, dict, InputInteractiveElement],
        block_id: Optional[str] = None,
        hint: Optional[Union[str, dict, PlainTextObject]] = None,
        dispatch_action: Optional[bool] = None,
        optional: Optional[bool] = None,
        **others: dict,
    ):
        """A block that collects information from users - it can hold a plain-text input element,
        a select menu element, a multi-select menu element, or a datepicker.
        https://docs.slack.dev/reference/block-kit/blocks/input-block

        Args:
            label (required): A label that appears above an input element in the form of a text object
                that must have type of plain_text. Maximum length for the text in this field is 2000 characters.
            element (required): An plain-text input element, a checkbox element, a radio button element,
                a select menu element, a multi-select menu element, or a datepicker.
            block_id: A string acting as a unique identifier for a block. If not specified, one will be generated.
                Maximum length for this field is 255 characters.
                block_id should be unique for each message or view and each iteration of a message or view.
                If a message or view is updated, use a new block_id.
            hint: An optional hint that appears below an input element in a lighter grey.
                It must be a text object with a type of plain_text.
                Maximum length for the text in this field is 2000 characters.
            dispatch_action: A boolean that indicates whether or not the use of elements in this block
                should dispatch a block_actions payload. Defaults to false.
            optional: A boolean that indicates whether the input element may be empty when a user submits the modal.
                Defaults to false.
        """
        super().__init__(type=self.type, block_id=block_id)
        show_unknown_key_warning(self, others)

        self.label = TextObject.parse(label, default_type=PlainTextObject.type)
        self.element = BlockElement.parse(element)  # type: ignore[arg-type]
        self.hint = TextObject.parse(hint, default_type=PlainTextObject.type)  # type: ignore[arg-type]
        self.dispatch_action = dispatch_action
        self.optional = optional

    @JsonValidator(f"label attribute cannot exceed {label_max_length} characters")
    def _validate_label_length(self):
        return self.label is None or self.label.text is None or len(self.label.text) <= self.label_max_length

    @JsonValidator(f"hint attribute cannot exceed {hint_max_length} characters")
    def _validate_hint_length(self):
        return self.hint is None or self.hint.text is None or len(self.hint.text) <= self.label_max_length

    @JsonValidator(
        (
            "element attribute must be a string, select element, multi-select element, "
            "or a datepicker. (Sub-classes of InputInteractiveElement)"
        )
    )
    def _validate_element_type(self):
        return self.element is None or isinstance(self.element, (str, InputInteractiveElement))
```

Blocks are a series of components that can be combined to create visually rich and compellingly interactive messages. [https://docs.slack.dev/reference/block-kit/blocks](https://docs.slack.dev/reference/block-kit/blocks)

A block that collects information from users - it can hold a plain-text input element, a select menu element, a multi-select menu element, or a datepicker. [https://docs.slack.dev/reference/block-kit/blocks/input-block](https://docs.slack.dev/reference/block-kit/blocks/input-block)

## Args (24)

**`label`** : `required`

A label that appears above an input element in the form of a text object that must have type of plain\_text. Maximum length for the text in this field is 2000 characters.

**`element`** : `required`

An plain-text input element, a checkbox element, a radio button element, a select menu element, a multi-select menu element, or a datepicker.

**`block_id`**

A string acting as a unique identifier for a block. If not specified, one will be generated. Maximum length for this field is 255 characters. block\_id should be unique for each message or view and each iteration of a message or view. If a message or view is updated, use a new block\_id.

**`hint`**

An optional hint that appears below an input element in a lighter grey. It must be a text object with a type of plain\_text. Maximum length for the text in this field is 2000 characters.

**`dispatch_action`**

A boolean that indicates whether or not the use of elements in this block should dispatch a block\_actions payload. Defaults to false.

**`optional`**

A boolean that indicates whether the input element may be empty when a user submits the modal. Defaults to false.

### Ancestors (28)

* [Block](blocks.html#slack_sdk.models.blocks.blocks.Block "slack_sdk.models.blocks.blocks.Block")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (28)

`var hint_max_length`

The type of the None singleton.

`var label_max_length`

The type of the None singleton.

`var type`

The type of the None singleton.

### Instance variables (21)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union({"label", "hint", "element", "optional", "dispatch_action"})
```

Build an unordered collection of unique elements.

### Inherited members (28)

* `**[Block](blocks.html#slack_sdk.models.blocks.blocks.Block "slack_sdk.models.blocks.blocks.Block")**`:
  * `[block_id_max_length](blocks.html#slack_sdk.models.blocks.blocks.Block.block_id_max_length "slack_sdk.models.blocks.blocks.Block.block_id_max_length")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.blocks.Block.get_non_null_attributes")`
  * `[logger](blocks.html#slack_sdk.models.blocks.blocks.Block.logger "slack_sdk.models.blocks.blocks.Block.logger")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.blocks.Block.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.blocks.Block.validate_json")`

`class InputInteractiveElement (*,   action_id: str | None = None,   placeholder: str | [TextObject](basic_components.html#slack_sdk.models.blocks.basic_components.TextObject "slack_sdk.models.blocks.basic_components.TextObject") | None = None,   type: str | None = None,   subtype: str | None = None,   confirm: dict | [ConfirmObject](basic_components.html#slack_sdk.models.blocks.basic_components.ConfirmObject "slack_sdk.models.blocks.basic_components.ConfirmObject") | None = None,   focus_on_load: bool | None = None,   **others: dict)`

Expand source code

```typescript
class InputInteractiveElement(InteractiveElement, metaclass=ABCMeta):
    placeholder_max_length = 150

    attributes = {"type", "action_id", "placeholder", "confirm", "focus_on_load"}

    @property
    def subtype(self) -> Optional[str]:
        return self.type

    def __init__(
        self,
        *,
        action_id: Optional[str] = None,
        placeholder: Optional[Union[str, TextObject]] = None,
        type: Optional[str] = None,
        subtype: Optional[str] = None,
        confirm: Optional[Union[dict, ConfirmObject]] = None,
        focus_on_load: Optional[bool] = None,
        **others: dict,
    ):
        """InteractiveElement that is usable in input blocks

        We generally recommend using the concrete subclasses for better supports of available properties.
        """
        if subtype:
            self._subtype_warning()
        super().__init__(action_id=action_id, type=type or subtype)

        # Note that we don't intentionally have show_unknown_key_warning for the unknown key warnings here.
        # It's fine to pass any kwargs to the held dict here although the class does not do any validation.
        # show_unknown_key_warning(self, others)

        self.placeholder = TextObject.parse(placeholder)  # type: ignore[arg-type]
        self.confirm = ConfirmObject.parse(confirm)  # type: ignore[arg-type]
        self.focus_on_load = focus_on_load

    @JsonValidator(f"placeholder attribute cannot exceed {placeholder_max_length} characters")
    def _validate_placeholder_length(self) -> bool:
        return (
            self.placeholder is None
            or self.placeholder.text is None
            or len(self.placeholder.text) <= self.placeholder_max_length
        )
```

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

InteractiveElement that is usable in input blocks

We generally recommend using the concrete subclasses for better supports of available properties.

### Ancestors (29)

* [InteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement "slack_sdk.models.blocks.block_elements.InteractiveElement")
* [BlockElement](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Subclasses (4)

* [ChannelMultiSelectElement](block_elements.html#slack_sdk.models.blocks.block_elements.ChannelMultiSelectElement "slack_sdk.models.blocks.block_elements.ChannelMultiSelectElement")
* [ChannelSelectElement](block_elements.html#slack_sdk.models.blocks.block_elements.ChannelSelectElement "slack_sdk.models.blocks.block_elements.ChannelSelectElement")
* [CheckboxesElement](block_elements.html#slack_sdk.models.blocks.block_elements.CheckboxesElement "slack_sdk.models.blocks.block_elements.CheckboxesElement")
* [ConversationMultiSelectElement](block_elements.html#slack_sdk.models.blocks.block_elements.ConversationMultiSelectElement "slack_sdk.models.blocks.block_elements.ConversationMultiSelectElement")
* [ConversationSelectElement](block_elements.html#slack_sdk.models.blocks.block_elements.ConversationSelectElement "slack_sdk.models.blocks.block_elements.ConversationSelectElement")
* [DatePickerElement](block_elements.html#slack_sdk.models.blocks.block_elements.DatePickerElement "slack_sdk.models.blocks.block_elements.DatePickerElement")
* [DateTimePickerElement](block_elements.html#slack_sdk.models.blocks.block_elements.DateTimePickerElement "slack_sdk.models.blocks.block_elements.DateTimePickerElement")
* [EmailInputElement](block_elements.html#slack_sdk.models.blocks.block_elements.EmailInputElement "slack_sdk.models.blocks.block_elements.EmailInputElement")
* [ExternalDataMultiSelectElement](block_elements.html#slack_sdk.models.blocks.block_elements.ExternalDataMultiSelectElement "slack_sdk.models.blocks.block_elements.ExternalDataMultiSelectElement")
* [ExternalDataSelectElement](block_elements.html#slack_sdk.models.blocks.block_elements.ExternalDataSelectElement "slack_sdk.models.blocks.block_elements.ExternalDataSelectElement")
* [FileInputElement](block_elements.html#slack_sdk.models.blocks.block_elements.FileInputElement "slack_sdk.models.blocks.block_elements.FileInputElement")
* [NumberInputElement](block_elements.html#slack_sdk.models.blocks.block_elements.NumberInputElement "slack_sdk.models.blocks.block_elements.NumberInputElement")
* [PlainTextInputElement](block_elements.html#slack_sdk.models.blocks.block_elements.PlainTextInputElement "slack_sdk.models.blocks.block_elements.PlainTextInputElement")
* [RadioButtonsElement](block_elements.html#slack_sdk.models.blocks.block_elements.RadioButtonsElement "slack_sdk.models.blocks.block_elements.RadioButtonsElement")
* [RichTextInputElement](block_elements.html#slack_sdk.models.blocks.block_elements.RichTextInputElement "slack_sdk.models.blocks.block_elements.RichTextInputElement")
* [SelectElement](block_elements.html#slack_sdk.models.blocks.block_elements.SelectElement "slack_sdk.models.blocks.block_elements.SelectElement")
* [StaticMultiSelectElement](block_elements.html#slack_sdk.models.blocks.block_elements.StaticMultiSelectElement "slack_sdk.models.blocks.block_elements.StaticMultiSelectElement")
* [StaticSelectElement](block_elements.html#slack_sdk.models.blocks.block_elements.StaticSelectElement "slack_sdk.models.blocks.block_elements.StaticSelectElement")
* [TimePickerElement](block_elements.html#slack_sdk.models.blocks.block_elements.TimePickerElement "slack_sdk.models.blocks.block_elements.TimePickerElement")
* [UrlInputElement](block_elements.html#slack_sdk.models.blocks.block_elements.UrlInputElement "slack_sdk.models.blocks.block_elements.UrlInputElement")
* [UserMultiSelectElement](block_elements.html#slack_sdk.models.blocks.block_elements.UserMultiSelectElement "slack_sdk.models.blocks.block_elements.UserMultiSelectElement")
* [UserSelectElement](block_elements.html#slack_sdk.models.blocks.block_elements.UserSelectElement "slack_sdk.models.blocks.block_elements.UserSelectElement")

### Class variables (29)

`var attributes`

The type of the None singleton.

`var placeholder_max_length`

The type of the None singleton.

### Instance variables (22)

`prop subtype : str | None`

Expand source code

```python
@property
def subtype(self) -> Optional[str]:
    return self.type
```

### Inherited members (29)

* `**[InteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement "slack_sdk.models.blocks.block_elements.InteractiveElement")**`:
  * `[action_id_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement.action_id_max_length "slack_sdk.models.blocks.block_elements.InteractiveElement.action_id_max_length")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.block_elements.InteractiveElement.get_non_null_attributes")`
  * `[logger](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement.logger "slack_sdk.models.blocks.block_elements.InteractiveElement.logger")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.block_elements.InteractiveElement.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.block_elements.InteractiveElement.validate_json")`

`class InteractiveElement (*,   action_id: str | None = None,   type: str | None = None,   subtype: str | None = None,   **others: dict)`

Expand source code

```typescript
class InteractiveElement(BlockElement):
    action_id_max_length = 255

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union({"alt_text", "action_id"})

    def __init__(
        self,
        *,
        action_id: Optional[str] = None,
        type: Optional[str] = None,
        subtype: Optional[str] = None,
        **others: dict,
    ):
        """An interactive block element.

        We generally recommend using the concrete subclasses for better supports of available properties.
        """
        if subtype:
            self._subtype_warning()
        super().__init__(type=type or subtype)

        # Note that we don't intentionally have show_unknown_key_warning for the unknown key warnings here.
        # It's fine to pass any kwargs to the held dict here although the class does not do any validation.
        # show_unknown_key_warning(self, others)

        self.action_id = action_id

    @JsonValidator(f"action_id attribute cannot exceed {action_id_max_length} characters")
    def _validate_action_id_length(self) -> bool:
        return self.action_id is None or len(self.action_id) <= self.action_id_max_length
```

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

An interactive block element.

We generally recommend using the concrete subclasses for better supports of available properties.

### Ancestors (30)

* [BlockElement](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Subclasses (5)

* [ButtonElement](block_elements.html#slack_sdk.models.blocks.block_elements.ButtonElement "slack_sdk.models.blocks.block_elements.ButtonElement")
* [FeedbackButtonsElement](block_elements.html#slack_sdk.models.blocks.block_elements.FeedbackButtonsElement "slack_sdk.models.blocks.block_elements.FeedbackButtonsElement")
* [IconButtonElement](block_elements.html#slack_sdk.models.blocks.block_elements.IconButtonElement "slack_sdk.models.blocks.block_elements.IconButtonElement")
* [InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")
* [OverflowMenuElement](block_elements.html#slack_sdk.models.blocks.block_elements.OverflowMenuElement "slack_sdk.models.blocks.block_elements.OverflowMenuElement")
* [WorkflowButtonElement](block_elements.html#slack_sdk.models.blocks.block_elements.WorkflowButtonElement "slack_sdk.models.blocks.block_elements.WorkflowButtonElement")

### Class variables (30)

`var action_id_max_length`

The type of the None singleton.

### Instance variables (23)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union({"alt_text", "action_id"})
```

Build an unordered collection of unique elements.

### Inherited members (30)

* `**[BlockElement](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.block_elements.BlockElement.get_non_null_attributes")`
  * `[logger](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement.logger "slack_sdk.models.blocks.block_elements.BlockElement.logger")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.block_elements.BlockElement.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.block_elements.BlockElement.validate_json")`

`class LinkButtonElement (*,   text: str | dict | [PlainTextObject](basic_components.html#slack_sdk.models.blocks.basic_components.PlainTextObject "slack_sdk.models.blocks.basic_components.PlainTextObject"),   url: str,   action_id: str | None = None,   style: str | None = None,   **others: dict)`

Expand source code

```typescript
class LinkButtonElement(ButtonElement):
    def __init__(
        self,
        *,
        text: Union[str, dict, PlainTextObject],
        url: str,
        action_id: Optional[str] = None,
        style: Optional[str] = None,
        **others: dict,
    ):
        """A simple button that simply opens a given URL. You will still receive an
        interaction payload and will need to send an acknowledgement response.
        This is a helper class that makes creating links simpler.
        https://docs.slack.dev/reference/block-kit/block-elements/button-element/

        Args:
            text (required): A text object that defines the button's text.
                Can only be of type: plain_text.
                Maximum length for the text in this field is 75 characters.
            url (required): A URL to load in the user's browser when the button is clicked.
                Maximum length for this field is 3000 characters.
                If you're using url, you'll still receive an interaction payload
                and will need to send an acknowledgement response.
            action_id (required): An identifier for this action.
                You can use this when you receive an interaction payload to identify the source of the action.
                Should be unique among all other action_ids in the containing block.
                Maximum length for this field is 255 characters.
            style: Decorates buttons with alternative visual color schemes. Use this option with restraint.
                "primary" gives buttons a green outline and text, ideal for affirmation or confirmation actions.
                "primary" should only be used for one button within a set.
                "danger" gives buttons a red outline and text, and should be used when the action is destructive.
                Use "danger" even more sparingly than "primary".
                If you don't include this field, the default button style will be used.
        """
        super().__init__(
            # NOTE: value must be always absent
            text=text,
            url=url,
            action_id=action_id,
            value=None,
            style=style,
        )
        show_unknown_key_warning(self, others)
```

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

A simple button that simply opens a given URL. You will still receive an interaction payload and will need to send an acknowledgement response. This is a helper class that makes creating links simpler. [https://docs.slack.dev/reference/block-kit/block-elements/button-element/](https://docs.slack.dev/reference/block-kit/block-elements/button-element/)

## Args (25)

**`text`** : `required`

A text object that defines the button's text. Can only be of type: plain\_text. Maximum length for the text in this field is 75 characters.

**`url`** : `required`

A URL to load in the user's browser when the button is clicked. Maximum length for this field is 3000 characters. If you're using url, you'll still receive an interaction payload and will need to send an acknowledgement response.

**`action_id`** : `required`

An identifier for this action. You can use this when you receive an interaction payload to identify the source of the action. Should be unique among all other action\_ids in the containing block. Maximum length for this field is 255 characters.

**`style`**

Decorates buttons with alternative visual color schemes. Use this option with restraint. "primary" gives buttons a green outline and text, ideal for affirmation or confirmation actions. "primary" should only be used for one button within a set. "danger" gives buttons a red outline and text, and should be used when the action is destructive. Use "danger" even more sparingly than "primary". If you don't include this field, the default button style will be used.

### Ancestors (31)

* [ButtonElement](block_elements.html#slack_sdk.models.blocks.block_elements.ButtonElement "slack_sdk.models.blocks.block_elements.ButtonElement")
* [InteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement "slack_sdk.models.blocks.block_elements.InteractiveElement")
* [BlockElement](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Inherited members (31)

* `**[ButtonElement](block_elements.html#slack_sdk.models.blocks.block_elements.ButtonElement "slack_sdk.models.blocks.block_elements.ButtonElement")**`:
  * `[action_id_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement.action_id_max_length "slack_sdk.models.blocks.block_elements.ButtonElement.action_id_max_length")`
  * `[attributes](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement.attributes "slack_sdk.models.blocks.block_elements.ButtonElement.attributes")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.block_elements.ButtonElement.get_non_null_attributes")`
  * `[logger](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement.logger "slack_sdk.models.blocks.block_elements.ButtonElement.logger")`
  * `[text_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.ButtonElement.text_max_length "slack_sdk.models.blocks.block_elements.ButtonElement.text_max_length")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.block_elements.ButtonElement.to_dict")`
  * `[type](block_elements.html#slack_sdk.models.blocks.block_elements.ButtonElement.type "slack_sdk.models.blocks.block_elements.ButtonElement.type")`
  * `[url_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.ButtonElement.url_max_length "slack_sdk.models.blocks.block_elements.ButtonElement.url_max_length")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.block_elements.ButtonElement.validate_json")`
  * `[value_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.ButtonElement.value_max_length "slack_sdk.models.blocks.block_elements.ButtonElement.value_max_length")`

`class MarkdownBlock (*, text: str, block_id: str | None = None, **others: dict)`

Expand source code

```typescript
class MarkdownBlock(Block):
    type = "markdown"
    text_max_length = 12000

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union({"text"})

    def __init__(
        self,
        *,
        text: str,
        block_id: Optional[str] = None,
        **others: dict,
    ):
        """Displays formatted markdown.
        https://docs.slack.dev/reference/block-kit/blocks/markdown-block/

        Args:
            block_id: A string acting as a unique identifier for a block. If not specified, one will be generated.
                Maximum length for this field is 255 characters.
                block_id should be unique for each message and each iteration of a message.
                If a message is updated, use a new block_id.
            text (required): The standard markdown-formatted text. Limit 12,000 characters max.
        """
        super().__init__(type=self.type, block_id=block_id)
        show_unknown_key_warning(self, others)

        self.text = text

    @JsonValidator("text attribute must be specified")
    def _validate_text(self):
        return self.text != ""

    @JsonValidator(f"text attribute cannot exceed {text_max_length} characters")
    def _validate_alt_text_length(self):
        return len(self.text) <= self.text_max_length
```

Blocks are a series of components that can be combined to create visually rich and compellingly interactive messages. [https://docs.slack.dev/reference/block-kit/blocks](https://docs.slack.dev/reference/block-kit/blocks)

Displays formatted markdown. [https://docs.slack.dev/reference/block-kit/blocks/markdown-block/](https://docs.slack.dev/reference/block-kit/blocks/markdown-block/)

## Args (26)

**`block_id`**

A string acting as a unique identifier for a block. If not specified, one will be generated. Maximum length for this field is 255 characters. block\_id should be unique for each message and each iteration of a message. If a message is updated, use a new block\_id.

**`text`** : `required`

The standard markdown-formatted text. Limit 12,000 characters max.

### Ancestors (32)

* [Block](blocks.html#slack_sdk.models.blocks.blocks.Block "slack_sdk.models.blocks.blocks.Block")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (31)

`var text_max_length`

The type of the None singleton.

`var type`

The type of the None singleton.

### Instance variables (24)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union({"text"})
```

Build an unordered collection of unique elements.

### Inherited members (32)

* `**[Block](blocks.html#slack_sdk.models.blocks.blocks.Block "slack_sdk.models.blocks.blocks.Block")**`:
  * `[block_id_max_length](blocks.html#slack_sdk.models.blocks.blocks.Block.block_id_max_length "slack_sdk.models.blocks.blocks.Block.block_id_max_length")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.blocks.Block.get_non_null_attributes")`
  * `[logger](blocks.html#slack_sdk.models.blocks.blocks.Block.logger "slack_sdk.models.blocks.blocks.Block.logger")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.blocks.Block.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.blocks.Block.validate_json")`

`class MarkdownTextObject (*, text: str, verbatim: bool | None = None)`

Expand source code

```typescript
class MarkdownTextObject(TextObject):
    """mrkdwn typed text object"""

    type = "mrkdwn"

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union({"verbatim"})

    def __init__(self, *, text: str, verbatim: Optional[bool] = None):
        """A Markdown text object, meaning markdown characters will be parsed as
        formatting information.
        https://docs.slack.dev/reference/block-kit/composition-objects/text-object

        Args:
            text (required): The text for the block. This field accepts any of the standard text formatting markup
                when type is mrkdwn.
            verbatim: When set to false (as is default) URLs will be auto-converted into links,
                conversation names will be link-ified, and certain mentions will be automatically parsed.
                Using a value of true will skip any preprocessing of this nature,
                although you can still include manual parsing strings. This field is only usable when type is mrkdwn.
        """
        super().__init__(text=text, type=self.type)
        self.verbatim = verbatim

    @staticmethod
    def from_str(text: str) -> "MarkdownTextObject":
        """Transforms a string into the required object shape to act as a MarkdownTextObject"""
        return MarkdownTextObject(text=text)

    @staticmethod
    def direct_from_string(text: str) -> Dict[str, Any]:
        """Transforms a string into the required object shape to act as a MarkdownTextObject"""
        return MarkdownTextObject.from_str(text).to_dict()

    @staticmethod
    def from_link(link: Link, title: str = "") -> "MarkdownTextObject":
        """
        Transform a Link object directly into the required object shape
        to act as a MarkdownTextObject
        """
        if title:
            title = f": {title}"
        return MarkdownTextObject(text=f"{link}{title}")

    @staticmethod
    def direct_from_link(link: Link, title: str = "") -> Dict[str, Any]:
        """
        Transform a Link object directly into the required object shape
        to act as a MarkdownTextObject
        """
        return MarkdownTextObject.from_link(link, title).to_dict()
```

mrkdwn typed text object

A Markdown text object, meaning markdown characters will be parsed as formatting information. [https://docs.slack.dev/reference/block-kit/composition-objects/text-object](https://docs.slack.dev/reference/block-kit/composition-objects/text-object)

## Args (27)

**`text`** : `required`

The text for the block. This field accepts any of the standard text formatting markup when type is mrkdwn.

**`verbatim`**

When set to false (as is default) URLs will be auto-converted into links, conversation names will be link-ified, and certain mentions will be automatically parsed. Using a value of true will skip any preprocessing of this nature, although you can still include manual parsing strings. This field is only usable when type is mrkdwn.

### Ancestors (33)

* [TextObject](basic_components.html#slack_sdk.models.blocks.basic_components.TextObject "slack_sdk.models.blocks.basic_components.TextObject")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (32)

`var type`

The type of the None singleton.

### Static methods (6)

`def direct_from_link(link: [Link](../messages/index.html#slack_sdk.models.messages.Link "slack_sdk.models.messages.Link"),   title: str = '') ‑> Dict[str, Any]`

Expand source code

```python
@staticmethod
def direct_from_link(link: Link, title: str = "") -> Dict[str, Any]:
    """
    Transform a Link object directly into the required object shape
    to act as a MarkdownTextObject
    """
    return MarkdownTextObject.from_link(link, title).to_dict()
```

Transform a Link object directly into the required object shape to act as a MarkdownTextObject

`def direct_from_string(text: str) ‑> Dict[str, Any]`

Expand source code

```typescript
@staticmethod
def direct_from_string(text: str) -> Dict[str, Any]:
    """Transforms a string into the required object shape to act as a MarkdownTextObject"""
    return MarkdownTextObject.from_str(text).to_dict()
```

Transforms a string into the required object shape to act as a MarkdownTextObject

`def from_link(link: [Link](../messages/index.html#slack_sdk.models.messages.Link "slack_sdk.models.messages.Link"),   title: str = '') ‑> [MarkdownTextObject](basic_components.html#slack_sdk.models.blocks.basic_components.MarkdownTextObject "slack_sdk.models.blocks.basic_components.MarkdownTextObject")`

Expand source code

```python
@staticmethod
def from_link(link: Link, title: str = "") -> "MarkdownTextObject":
    """
    Transform a Link object directly into the required object shape
    to act as a MarkdownTextObject
    """
    if title:
        title = f": {title}"
    return MarkdownTextObject(text=f"{link}{title}")
```

Transform a Link object directly into the required object shape to act as a MarkdownTextObject

`def from_str(text: str) ‑> [MarkdownTextObject](basic_components.html#slack_sdk.models.blocks.basic_components.MarkdownTextObject "slack_sdk.models.blocks.basic_components.MarkdownTextObject")`

Expand source code

```typescript
@staticmethod
def from_str(text: str) -> "MarkdownTextObject":
    """Transforms a string into the required object shape to act as a MarkdownTextObject"""
    return MarkdownTextObject(text=text)
```

Transforms a string into the required object shape to act as a MarkdownTextObject

### Instance variables (25)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union({"verbatim"})
```

Build an unordered collection of unique elements.

### Inherited members (33)

* `**[TextObject](basic_components.html#slack_sdk.models.blocks.basic_components.TextObject "slack_sdk.models.blocks.basic_components.TextObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.basic_components.TextObject.get_non_null_attributes")`
  * `[logger](basic_components.html#slack_sdk.models.blocks.basic_components.TextObject.logger "slack_sdk.models.blocks.basic_components.TextObject.logger")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.basic_components.TextObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.basic_components.TextObject.validate_json")`

`class NumberInputElement (*,   action_id: str | None = None,   is_decimal_allowed: bool | None = False,   initial_value: int | float | str | None = None,   min_value: int | float | str | None = None,   max_value: int | float | str | None = None,   dispatch_action_config: dict | [DispatchActionConfig](basic_components.html#slack_sdk.models.blocks.basic_components.DispatchActionConfig "slack_sdk.models.blocks.basic_components.DispatchActionConfig") | None = None,   focus_on_load: bool | None = None,   placeholder: str | dict | [TextObject](basic_components.html#slack_sdk.models.blocks.basic_components.TextObject "slack_sdk.models.blocks.basic_components.TextObject") | None = None,   **others: dict)`

Expand source code

```typescript
class NumberInputElement(InputInteractiveElement):
    type = "number_input"

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union(
            {
                "initial_value",
                "is_decimal_allowed",
                "min_value",
                "max_value",
                "dispatch_action_config",
            }
        )

    def __init__(
        self,
        *,
        action_id: Optional[str] = None,
        is_decimal_allowed: Optional[bool] = False,
        initial_value: Optional[Union[int, float, str]] = None,
        min_value: Optional[Union[int, float, str]] = None,
        max_value: Optional[Union[int, float, str]] = None,
        dispatch_action_config: Optional[Union[dict, DispatchActionConfig]] = None,
        focus_on_load: Optional[bool] = None,
        placeholder: Optional[Union[str, dict, TextObject]] = None,
        **others: dict,
    ):
        """
        https://docs.slack.dev/reference/block-kit/block-elements/number-input-element/

        Args:
            action_id (required): An identifier for the input value when the parent modal is submitted.
                You can use this when you receive a view_submission payload to identify the value of the input element.
                Should be unique among all other action_ids in the containing block.
                Maximum length for this field is 255 characters.
            is_decimal_allowed (required): Decimal numbers are allowed if is_decimal_allowed= true, set the value to
                false otherwise.
            initial_value: The initial value in the number input when it is loaded.
            min_value: The minimum value, cannot be greater than max_value.
            max_value: The maximum value, cannot be less than min_value.
            dispatch_action_config: A dispatch configuration object that determines when
                during text input the element returns a block_actions payload.
            focus_on_load: Indicates whether the element will be set to auto focus within the view object.
                Only one element can be set to true. Defaults to false.
            placeholder: A plain_text only text object that defines the placeholder text shown
                in the plain-text input. Maximum length for the text in this field is 150 characters.
        """
        super().__init__(
            type=self.type,
            action_id=action_id,
            placeholder=TextObject.parse(placeholder, PlainTextObject.type),  # type: ignore[arg-type]
            focus_on_load=focus_on_load,
        )
        show_unknown_key_warning(self, others)

        self.initial_value = str(initial_value) if initial_value is not None else None
        self.is_decimal_allowed = is_decimal_allowed
        self.min_value = str(min_value) if min_value is not None else None
        self.max_value = str(max_value) if max_value is not None else None
        self.dispatch_action_config = dispatch_action_config
```

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

[https://docs.slack.dev/reference/block-kit/block-elements/number-input-element/](https://docs.slack.dev/reference/block-kit/block-elements/number-input-element/)

## Args (28)

**`action_id`** : `required`

An identifier for the input value when the parent modal is submitted. You can use this when you receive a view\_submission payload to identify the value of the input element. Should be unique among all other action\_ids in the containing block. Maximum length for this field is 255 characters.

**`is_decimal_allowed`** : `required`

Decimal numbers are allowed if is\_decimal\_allowed= true, set the value to false otherwise.

**`initial_value`**

The initial value in the number input when it is loaded.

**`min_value`**

The minimum value, cannot be greater than max\_value.

**`max_value`**

The maximum value, cannot be less than min\_value.

**`dispatch_action_config`**

A dispatch configuration object that determines when during text input the element returns a block\_actions payload.

**`focus_on_load`**

Indicates whether the element will be set to auto focus within the view object. Only one element can be set to true. Defaults to false.

**`placeholder`**

A plain\_text only text object that defines the placeholder text shown in the plain-text input. Maximum length for the text in this field is 150 characters.

### Ancestors (34)

* [InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")
* [InteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement "slack_sdk.models.blocks.block_elements.InteractiveElement")
* [BlockElement](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (33)

`var type`

The type of the None singleton.

### Instance variables (26)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union(
        {
            "initial_value",
            "is_decimal_allowed",
            "min_value",
            "max_value",
            "dispatch_action_config",
        }
    )
```

Build an unordered collection of unique elements.

### Inherited members (34)

* `**[InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")**`:
  * `[action_id_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement.action_id_max_length "slack_sdk.models.blocks.block_elements.InputInteractiveElement.action_id_max_length")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.block_elements.InputInteractiveElement.get_non_null_attributes")`
  * `[logger](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement.logger "slack_sdk.models.blocks.block_elements.InputInteractiveElement.logger")`
  * `[placeholder_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement.placeholder_max_length "slack_sdk.models.blocks.block_elements.InputInteractiveElement.placeholder_max_length")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.block_elements.InputInteractiveElement.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.block_elements.InputInteractiveElement.validate_json")`

`class Option (*,   value: str,   label: str | None = None,   text: str | Dict[str, Any] | [TextObject](basic_components.html#slack_sdk.models.blocks.basic_components.TextObject "slack_sdk.models.blocks.basic_components.TextObject") | None = None,   description: str | Dict[str, Any] | [TextObject](basic_components.html#slack_sdk.models.blocks.basic_components.TextObject "slack_sdk.models.blocks.basic_components.TextObject") | None = None,   url: str | None = None,   **others: Dict[str, Any])`

Expand source code

```typescript
class Option(JsonObject):
    """Option object used in dialogs, legacy message actions (interactivity in attachments),
    and blocks. JSON must be retrieved with an explicit option_type - the Slack API has
    different required formats in different situations
    """

    attributes: Set[str] = set()
    logger = logging.getLogger(__name__)

    label_max_length = 75
    value_max_length = 150

    def __init__(
        self,
        *,
        value: str,
        label: Optional[str] = None,
        text: Optional[Union[str, Dict[str, Any], TextObject]] = None,  # Block Kit
        description: Optional[Union[str, Dict[str, Any], TextObject]] = None,
        url: Optional[str] = None,
        **others: Dict[str, Any],
    ):
        """
        An object that represents a single selectable item in a block element (
        SelectElement, OverflowMenuElement) or dialog element
        (StaticDialogSelectElement)

        Blocks:
        https://docs.slack.dev/reference/block-kit/composition-objects/option-object

        Dialogs:
        https://docs.slack.dev/legacy/legacy-dialogs/#select_elements

        Legacy interactive attachments:
        https://docs.slack.dev/legacy/legacy-messaging/legacy-interactive-message-field-guide/#option_fields

        Args:
            label: A short, user-facing string to label this option to users.
                Cannot exceed 75 characters.
            value: A short string that identifies this particular option to your
                application. It will be part of the payload when this option is selected
                . Cannot exceed 150 characters.
            description: A user-facing string that provides more details about
                this option. Only supported in legacy message actions, not in blocks or
                dialogs.
        """
        if text:
            # For better compatibility with Block Kit ("mrkdwn" does not work for it),
            # we've changed the default text object type to plain_text since version 3.10.0
            self._text: Optional[TextObject] = TextObject.parse(
                text=text,  # "text" here can be either a str or a TextObject
                default_type=PlainTextObject.type,
            )
            self._label: Optional[str] = None
        else:
            self._text = None
            self._label = label

        # for backward-compatibility with version 2.0-2.5, the following fields return str values
        self.text: Optional[str] = self._text.text if self._text else None
        self.label: Optional[str] = self._label

        self.value: str = value

        # for backward-compatibility with version 2.0-2.5, the following fields return str values
        if isinstance(description, str):
            self.description = description
            self._block_description = PlainTextObject.from_str(description)
        elif isinstance(description, dict):
            self.description = description["text"]
            self._block_description = TextObject.parse(description)  # type: ignore[assignment]
        elif isinstance(description, TextObject):
            self.description = description.text
            self._block_description = description  # type: ignore[assignment]
        else:
            self.description = None  # type: ignore[assignment]
            self._block_description = None  # type: ignore[assignment]

        # A URL to load in the user's browser when the option is clicked.
        # The url attribute is only available in overflow menus.
        # Maximum length for this field is 3000 characters.
        # If you're using url, you'll still receive an interaction payload
        # and will need to send an acknowledgement response.
        self.url: Optional[str] = url
        show_unknown_key_warning(self, others)

    @JsonValidator(f"label attribute cannot exceed {label_max_length} characters")
    def _validate_label_length(self) -> bool:
        return self._label is None or len(self._label) <= self.label_max_length

    @JsonValidator(f"text attribute cannot exceed {label_max_length} characters")
    def _validate_text_length(self) -> bool:
        return self._text is None or self._text.text is None or len(self._text.text) <= self.label_max_length

    @JsonValidator(f"value attribute cannot exceed {value_max_length} characters")
    def _validate_value_length(self) -> bool:
        return len(self.value) <= self.value_max_length

    @classmethod
    def parse_all(cls, options: Optional[Sequence[Union[Dict[str, Any], "Option"]]]) -> Optional[List["Option"]]:
        if options is None:
            return None
        option_objects: List[Option] = []
        for o in options:
            if isinstance(o, dict):
                d = copy.copy(o)
                option_objects.append(Option(**d))
            elif isinstance(o, Option):
                option_objects.append(o)
            else:
                cls.logger.warning(f"Unknown option object detected and skipped ({o})")
        return option_objects

    def to_dict(self, option_type: str = "block") -> Dict[str, Any]:
        """
        Different parent classes must call this with a valid value from OptionTypes -
        either "dialog", "action", or "block", so that JSON is returned in the
        correct shape.
        """
        self.validate_json()
        if option_type == "dialog":
            return {"label": self.label, "value": self.value}
        elif option_type == "action" or option_type == "attachment":
            # "action" can be confusing but it means a legacy message action in attachments
            # we don't remove the type name for backward compatibility though
            json: Dict[str, Any] = {"text": self.label, "value": self.value}
            if self.description is not None:
                json["description"] = self.description
            return json
        else:  # if option_type == "block"; this should be the most common case
            text: TextObject = self._text or PlainTextObject.from_str(self.label)  # type: ignore[arg-type]
            json = {
                "text": text.to_dict(),
                "value": self.value,
            }
            if self._block_description:
                json["description"] = self._block_description.to_dict()
            if self.url:
                json["url"] = self.url
            return json

    @staticmethod
    def from_single_value(value_and_label: str):
        """Creates a simple Option instance with the same value and label"""
        return Option(value=value_and_label, label=value_and_label)
```

Option object used in dialogs, legacy message actions (interactivity in attachments), and blocks. JSON must be retrieved with an explicit option\_type - the Slack API has different required formats in different situations

An object that represents a single selectable item in a block element ( SelectElement, OverflowMenuElement) or dialog element (StaticDialogSelectElement)

Blocks: [https://docs.slack.dev/reference/block-kit/composition-objects/option-object](https://docs.slack.dev/reference/block-kit/composition-objects/option-object)

Dialogs: [https://docs.slack.dev/legacy/legacy-dialogs/#select\_elements](https://docs.slack.dev/legacy/legacy-dialogs/#select_elements)

Legacy interactive attachments: [https://docs.slack.dev/legacy/legacy-messaging/legacy-interactive-message-field-guide/#option\_fields](https://docs.slack.dev/legacy/legacy-messaging/legacy-interactive-message-field-guide/#option_fields)

## Args (29)

**`label`**

A short, user-facing string to label this option to users. Cannot exceed 75 characters.

**`value`**

A short string that identifies this particular option to your application. It will be part of the payload when this option is selected . Cannot exceed 150 characters.

**`description`**

A user-facing string that provides more details about this option. Only supported in legacy message actions, not in blocks or dialogs.

### Ancestors (35)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (34)

`var attributes : Set[str]`

The type of the None singleton.

`var label_max_length`

The type of the None singleton.

`var logger`

The type of the None singleton.

`var value_max_length`

The type of the None singleton.

### Static methods (7)

`def from_single_value(value_and_label: str)`

Expand source code

```python
@staticmethod
def from_single_value(value_and_label: str):
    """Creates a simple Option instance with the same value and label"""
    return Option(value=value_and_label, label=value_and_label)
```

Creates a simple Option instance with the same value and label

`def parse_all(options: Sequence[Dict[str, Any] | [Option](#slack_sdk.models.blocks.Option "slack_sdk.models.blocks.Option")] | None) ‑> List[[Option](basic_components.html#slack_sdk.models.blocks.basic_components.Option "slack_sdk.models.blocks.basic_components.Option")] | None`

### Methods (3)

`def to_dict(self, option_type: str = 'block') ‑> Dict[str, Any]`

Expand source code

```typescript
def to_dict(self, option_type: str = "block") -> Dict[str, Any]:
    """
    Different parent classes must call this with a valid value from OptionTypes -
    either "dialog", "action", or "block", so that JSON is returned in the
    correct shape.
    """
    self.validate_json()
    if option_type == "dialog":
        return {"label": self.label, "value": self.value}
    elif option_type == "action" or option_type == "attachment":
        # "action" can be confusing but it means a legacy message action in attachments
        # we don't remove the type name for backward compatibility though
        json: Dict[str, Any] = {"text": self.label, "value": self.value}
        if self.description is not None:
            json["description"] = self.description
        return json
    else:  # if option_type == "block"; this should be the most common case
        text: TextObject = self._text or PlainTextObject.from_str(self.label)  # type: ignore[arg-type]
        json = {
            "text": text.to_dict(),
            "value": self.value,
        }
        if self._block_description:
            json["description"] = self._block_description.to_dict()
        if self.url:
            json["url"] = self.url
        return json
```

Different parent classes must call this with a valid value from OptionTypes - either "dialog", "action", or "block", so that JSON is returned in the correct shape.

### Inherited members (35)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class OptionGroup (*,   label: str | Dict[str, Any] | [TextObject](basic_components.html#slack_sdk.models.blocks.basic_components.TextObject "slack_sdk.models.blocks.basic_components.TextObject") | None = None,   options: Sequence[Dict[str, Any] | [Option](basic_components.html#slack_sdk.models.blocks.basic_components.Option "slack_sdk.models.blocks.basic_components.Option")],   **others: Dict[str, Any])`

Expand source code

```typescript
class OptionGroup(JsonObject):
    """
    JSON must be retrieved with an explicit option_type - the Slack API has
    different required formats in different situations
    """

    attributes: Set[str] = set()
    label_max_length = 75
    options_max_length = 100
    logger = logging.getLogger(__name__)

    def __init__(
        self,
        *,
        label: Optional[Union[str, Dict[str, Any], TextObject]] = None,
        options: Sequence[Union[Dict[str, Any], Option]],
        **others: Dict[str, Any],
    ):
        """
        Create a group of Option objects - pass in a label (that will be part of the
        UI) and a list of Option objects.

        Blocks:
        https://docs.slack.dev/reference/block-kit/composition-objects/option-group-object

        Dialogs:
        https://docs.slack.dev/legacy/legacy-dialogs/#select_elements

        Legacy interactive attachments:
        https://docs.slack.dev/legacy/legacy-messaging/legacy-interactive-message-field-guide/#option_groups

        Args:
            label: Text to display at the top of this group of options.
            options: A list of no more than 100 Option objects.
        """  # noqa prevent flake8 blowing up on the long URL
        # default_type=PlainTextObject.type is for backward-compatibility
        self._label: Optional[TextObject] = TextObject.parse(label, default_type=PlainTextObject.type)  # type: ignore[arg-type] # noqa: E501
        self.label: Optional[str] = self._label.text if self._label else None
        self.options = Option.parse_all(options)  # compatible with version 2.5
        show_unknown_key_warning(self, others)

    @JsonValidator(f"label attribute cannot exceed {label_max_length} characters")
    def _validate_label_length(self):
        return self.label is None or len(self.label) <= self.label_max_length

    @JsonValidator(f"options attribute cannot exceed {options_max_length} elements")
    def _validate_options_length(self):
        return self.options is None or len(self.options) <= self.options_max_length

    @classmethod
    def parse_all(
        cls, option_groups: Optional[Sequence[Union[Dict[str, Any], "OptionGroup"]]]
    ) -> Optional[List["OptionGroup"]]:
        if option_groups is None:
            return None
        option_group_objects = []
        for o in option_groups:
            if isinstance(o, dict):
                d = copy.copy(o)
                option_group_objects.append(OptionGroup(**d))
            elif isinstance(o, OptionGroup):
                option_group_objects.append(o)
            else:
                cls.logger.warning(f"Unknown option group object detected and skipped ({o})")
        return option_group_objects

    def to_dict(self, option_type: str = "block") -> Dict[str, Any]:
        self.validate_json()
        dict_options = [o.to_dict(option_type) for o in self.options]  # type: ignore[union-attr]
        if option_type == "dialog":
            return {
                "label": self.label,
                "options": dict_options,
            }
        elif option_type == "action":
            return {
                "text": self.label,
                "options": dict_options,
            }
        else:  # if option_type == "block"; this should be the most common case
            dict_label: Dict[str, Any] = self._label.to_dict()  # type: ignore[union-attr]
            return {
                "label": dict_label,
                "options": dict_options,
            }
```

JSON must be retrieved with an explicit option\_type - the Slack API has different required formats in different situations

Create a group of Option objects - pass in a label (that will be part of the UI) and a list of Option objects.

Blocks: [https://docs.slack.dev/reference/block-kit/composition-objects/option-group-object](https://docs.slack.dev/reference/block-kit/composition-objects/option-group-object)

Dialogs: [https://docs.slack.dev/legacy/legacy-dialogs/#select\_elements](https://docs.slack.dev/legacy/legacy-dialogs/#select_elements)

Legacy interactive attachments: [https://docs.slack.dev/legacy/legacy-messaging/legacy-interactive-message-field-guide/#option\_groups](https://docs.slack.dev/legacy/legacy-messaging/legacy-interactive-message-field-guide/#option_groups)

## Args (30)

**`label`**

Text to display at the top of this group of options.

**`options`**

A list of no more than 100 Option objects.

### Ancestors (36)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (35)

`var attributes : Set[str]`

The type of the None singleton.

`var label_max_length`

The type of the None singleton.

`var logger`

The type of the None singleton.

`var options_max_length`

The type of the None singleton.

### Static methods (8)

`def parse_all(option_groups: Sequence[Dict[str, Any] | [OptionGroup](#slack_sdk.models.blocks.OptionGroup "slack_sdk.models.blocks.OptionGroup")] | None) ‑> List[[OptionGroup](basic_components.html#slack_sdk.models.blocks.basic_components.OptionGroup "slack_sdk.models.blocks.basic_components.OptionGroup")] | None`

### Inherited members (36)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class OverflowMenuElement (*,   action_id: str | None = None,   options: Sequence[[Option](basic_components.html#slack_sdk.models.blocks.basic_components.Option "slack_sdk.models.blocks.basic_components.Option")],   confirm: dict | [ConfirmObject](basic_components.html#slack_sdk.models.blocks.basic_components.ConfirmObject "slack_sdk.models.blocks.basic_components.ConfirmObject") | None = None,   **others: dict)`

Expand source code

```typescript
class OverflowMenuElement(InteractiveElement):
    type = "overflow"
    options_min_length = 1
    options_max_length = 5

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union({"confirm", "options"})

    def __init__(
        self,
        *,
        action_id: Optional[str] = None,
        options: Sequence[Option],
        confirm: Optional[Union[dict, ConfirmObject]] = None,
        **others: dict,
    ):
        """
        This is like a cross between a button and a select menu - when a user clicks
        on this overflow button, they will be presented with a list of options to
        choose from. Unlike the select menu, there is no typeahead field, and the
        button always appears with an ellipsis ("…") rather than customisable text.

        As such, it is usually used if you want a more compact layout than a select
        menu, or to supply a list of less visually important actions after a row of
        buttons. You can also specify simple URL links as overflow menu options,
        instead of actions.

        https://docs.slack.dev/reference/block-kit/block-elements/overflow-menu-element

        Args:
            action_id (required): An identifier for the action triggered when a menu option is selected.
                You can use this when you receive an interaction payload to identify the source of the action.
                Should be unique among all other action_ids in the containing block.
                Maximum length for this field is 255 characters.
            options (required): An array of option objects to display in the menu.
                Maximum number of options is 5, minimum is 1.
            confirm: A confirm object that defines an optional confirmation dialog that appears
                after a menu item is selected.
        """
        super().__init__(action_id=action_id, type=self.type)
        show_unknown_key_warning(self, others)

        self.options = options
        self.confirm = ConfirmObject.parse(confirm)  # type: ignore[arg-type]

    @JsonValidator(f"options attribute must have between {options_min_length} " f"and {options_max_length} items")
    def _validate_options_length(self) -> bool:
        return self.options_min_length <= len(self.options) <= self.options_max_length
```

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

This is like a cross between a button and a select menu - when a user clicks on this overflow button, they will be presented with a list of options to choose from. Unlike the select menu, there is no typeahead field, and the button always appears with an ellipsis ("…") rather than customisable text.

As such, it is usually used if you want a more compact layout than a select menu, or to supply a list of less visually important actions after a row of buttons. You can also specify simple URL links as overflow menu options, instead of actions.

[https://docs.slack.dev/reference/block-kit/block-elements/overflow-menu-element](https://docs.slack.dev/reference/block-kit/block-elements/overflow-menu-element)

## Args (31)

**`action_id`** : `required`

An identifier for the action triggered when a menu option is selected. You can use this when you receive an interaction payload to identify the source of the action. Should be unique among all other action\_ids in the containing block. Maximum length for this field is 255 characters.

**`options`** : `required`

An array of option objects to display in the menu. Maximum number of options is 5, minimum is 1.

**`confirm`**

A confirm object that defines an optional confirmation dialog that appears after a menu item is selected.

### Ancestors (37)

* [InteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement "slack_sdk.models.blocks.block_elements.InteractiveElement")
* [BlockElement](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (36)

`var options_max_length`

The type of the None singleton.

`var options_min_length`

The type of the None singleton.

`var type`

The type of the None singleton.

### Inherited members (37)

* `**[InteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement "slack_sdk.models.blocks.block_elements.InteractiveElement")**`:
  * `[action_id_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement.action_id_max_length "slack_sdk.models.blocks.block_elements.InteractiveElement.action_id_max_length")`
  * `[attributes](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement.attributes "slack_sdk.models.blocks.block_elements.InteractiveElement.attributes")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.block_elements.InteractiveElement.get_non_null_attributes")`
  * `[logger](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement.logger "slack_sdk.models.blocks.block_elements.InteractiveElement.logger")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.block_elements.InteractiveElement.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.block_elements.InteractiveElement.validate_json")`

`class PlainTextInputElement (*,   action_id: str | None = None,   placeholder: str | dict | [TextObject](basic_components.html#slack_sdk.models.blocks.basic_components.TextObject "slack_sdk.models.blocks.basic_components.TextObject") | None = None,   initial_value: str | None = None,   multiline: bool | None = None,   min_length: int | None = None,   max_length: int | None = None,   dispatch_action_config: dict | [DispatchActionConfig](basic_components.html#slack_sdk.models.blocks.basic_components.DispatchActionConfig "slack_sdk.models.blocks.basic_components.DispatchActionConfig") | None = None,   focus_on_load: bool | None = None,   **others: dict)`

Expand source code

```typescript
class PlainTextInputElement(InputInteractiveElement):
    type = "plain_text_input"

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union(
            {
                "initial_value",
                "multiline",
                "min_length",
                "max_length",
                "dispatch_action_config",
            }
        )

    def __init__(
        self,
        *,
        action_id: Optional[str] = None,
        placeholder: Optional[Union[str, dict, TextObject]] = None,
        initial_value: Optional[str] = None,
        multiline: Optional[bool] = None,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
        dispatch_action_config: Optional[Union[dict, DispatchActionConfig]] = None,
        focus_on_load: Optional[bool] = None,
        **others: dict,
    ):
        """
        A plain-text input, similar to the HTML <input> tag, creates a field
        where a user can enter freeform data. It can appear as a single-line
        field or a larger textarea using the multiline flag. Plain-text input
        elements can be used inside of SectionBlocks and ActionsBlocks.
        https://docs.slack.dev/reference/block-kit/block-elements/plain-text-input-element

        Args:
            action_id (required): An identifier for the input value when the parent modal is submitted.
                You can use this when you receive a view_submission payload to identify the value of the input element.
                Should be unique among all other action_ids in the containing block.
                Maximum length for this field is 255 characters.
            placeholder: A plain_text only text object that defines the placeholder text shown
                in the plain-text input. Maximum length for the text in this field is 150 characters.
            initial_value: The initial value in the plain-text input when it is loaded.
            multiline: Indicates whether the input will be a single line (false) or a larger textarea (true).
                Defaults to false.
            min_length: The minimum length of input that the user must provide. If the user provides less,
                they will receive an error. Maximum value is 3000.
            max_length: The maximum length of input that the user can provide. If the user provides more,
                they will receive an error.
            dispatch_action_config: A dispatch configuration object that determines when
                during text input the element returns a block_actions payload.
            focus_on_load: Indicates whether the element will be set to auto focus within the view object.
                Only one element can be set to true. Defaults to false.
        """
        super().__init__(
            type=self.type,
            action_id=action_id,
            placeholder=TextObject.parse(placeholder, PlainTextObject.type),  # type: ignore[arg-type]
            focus_on_load=focus_on_load,
        )
        show_unknown_key_warning(self, others)

        self.initial_value = initial_value
        self.multiline = multiline
        self.min_length = min_length
        self.max_length = max_length
        self.dispatch_action_config = dispatch_action_config
```

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

A plain-text input, similar to the HTML  tag, creates a field where a user can enter freeform data. It can appear as a single-line field or a larger textarea using the multiline flag. Plain-text input elements can be used inside of SectionBlocks and ActionsBlocks. [https://docs.slack.dev/reference/block-kit/block-elements/plain-text-input-element](https://docs.slack.dev/reference/block-kit/block-elements/plain-text-input-element)

## Args (32)

**`action_id`** : `required`

An identifier for the input value when the parent modal is submitted. You can use this when you receive a view\_submission payload to identify the value of the input element. Should be unique among all other action\_ids in the containing block. Maximum length for this field is 255 characters.

**`placeholder`**

A plain\_text only text object that defines the placeholder text shown in the plain-text input. Maximum length for the text in this field is 150 characters.

**`initial_value`**

The initial value in the plain-text input when it is loaded.

**`multiline`**

Indicates whether the input will be a single line (false) or a larger textarea (true). Defaults to false.

**`min_length`**

The minimum length of input that the user must provide. If the user provides less, they will receive an error. Maximum value is 3000.

**`max_length`**

The maximum length of input that the user can provide. If the user provides more, they will receive an error.

**`dispatch_action_config`**

A dispatch configuration object that determines when during text input the element returns a block\_actions payload.

**`focus_on_load`**

Indicates whether the element will be set to auto focus within the view object. Only one element can be set to true. Defaults to false.

### Ancestors (38)

* [InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")
* [InteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement "slack_sdk.models.blocks.block_elements.InteractiveElement")
* [BlockElement](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (37)

`var type`

The type of the None singleton.

### Instance variables (27)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union(
        {
            "initial_value",
            "multiline",
            "min_length",
            "max_length",
            "dispatch_action_config",
        }
    )
```

Build an unordered collection of unique elements.

### Inherited members (38)

* `**[InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")**`:
  * `[action_id_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement.action_id_max_length "slack_sdk.models.blocks.block_elements.InputInteractiveElement.action_id_max_length")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.block_elements.InputInteractiveElement.get_non_null_attributes")`
  * `[logger](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement.logger "slack_sdk.models.blocks.block_elements.InputInteractiveElement.logger")`
  * `[placeholder_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement.placeholder_max_length "slack_sdk.models.blocks.block_elements.InputInteractiveElement.placeholder_max_length")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.block_elements.InputInteractiveElement.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.block_elements.InputInteractiveElement.validate_json")`

`class PlainTextObject (*, text: str, emoji: bool | None = None)`

Expand source code

```typescript
class PlainTextObject(TextObject):
    """plain_text typed text object"""

    type = "plain_text"

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union({"emoji"})

    def __init__(self, *, text: str, emoji: Optional[bool] = None):
        """A plain text object, meaning markdown characters will not be parsed as
        formatting information.
        https://docs.slack.dev/reference/block-kit/composition-objects/text-object

        Args:
            text (required): The text for the block. This field accepts any of the standard text formatting markup
                when type is mrkdwn.
            emoji: Indicates whether emojis in a text field should be escaped into the colon emoji format.
                This field is only usable when type is plain_text.
        """
        super().__init__(text=text, type=self.type)
        self.emoji = emoji

    @staticmethod
    def from_str(text: str) -> "PlainTextObject":
        return PlainTextObject(text=text, emoji=True)

    @staticmethod
    def direct_from_string(text: str) -> Dict[str, Any]:
        """Transforms a string into the required object shape to act as a PlainTextObject"""
        return PlainTextObject.from_str(text).to_dict()
```

plain\_text typed text object

A plain text object, meaning markdown characters will not be parsed as formatting information. [https://docs.slack.dev/reference/block-kit/composition-objects/text-object](https://docs.slack.dev/reference/block-kit/composition-objects/text-object)

## Args (33)

**`text`** : `required`

The text for the block. This field accepts any of the standard text formatting markup when type is mrkdwn.

**`emoji`**

Indicates whether emojis in a text field should be escaped into the colon emoji format. This field is only usable when type is plain\_text.

### Ancestors (39)

* [TextObject](basic_components.html#slack_sdk.models.blocks.basic_components.TextObject "slack_sdk.models.blocks.basic_components.TextObject")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (38)

`var type`

The type of the None singleton.

### Static methods (9)

`def direct_from_string(text: str) ‑> Dict[str, Any]`

Expand source code

```typescript
@staticmethod
def direct_from_string(text: str) -> Dict[str, Any]:
    """Transforms a string into the required object shape to act as a PlainTextObject"""
    return PlainTextObject.from_str(text).to_dict()
```

Transforms a string into the required object shape to act as a PlainTextObject

`def from_str(text: str) ‑> [PlainTextObject](basic_components.html#slack_sdk.models.blocks.basic_components.PlainTextObject "slack_sdk.models.blocks.basic_components.PlainTextObject")`

Expand source code

```python
@staticmethod
def from_str(text: str) -> "PlainTextObject":
    return PlainTextObject(text=text, emoji=True)
```

### Instance variables (28)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union({"emoji"})
```

Build an unordered collection of unique elements.

### Inherited members (39)

* `**[TextObject](basic_components.html#slack_sdk.models.blocks.basic_components.TextObject "slack_sdk.models.blocks.basic_components.TextObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.basic_components.TextObject.get_non_null_attributes")`
  * `[logger](basic_components.html#slack_sdk.models.blocks.basic_components.TextObject.logger "slack_sdk.models.blocks.basic_components.TextObject.logger")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.basic_components.TextObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.basic_components.TextObject.validate_json")`

`class PlanBlock (*,   title: str,   tasks: Sequence[Dict | [TaskCardBlock](blocks.html#slack_sdk.models.blocks.blocks.TaskCardBlock "slack_sdk.models.blocks.blocks.TaskCardBlock")] | None = None,   block_id: str | None = None,   **others: dict)`

Expand source code

```typescript
class PlanBlock(Block):
    type = "plan"

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union(
            {
                "title",
                "tasks",
            }
        )

    def __init__(
        self,
        *,
        title: str,
        tasks: Optional[Sequence[Union[Dict, TaskCardBlock]]] = None,
        block_id: Optional[str] = None,
        **others: dict,
    ):
        """Displays a collection of related tasks.
        https://docs.slack.dev/reference/block-kit/blocks/plan-block/

        Args:
            block_id: A string acting as a unique identifier for a block. If not specified, one will be generated.
                Maximum length for this field is 255 characters.
                block_id should be unique for each message and each iteration of a message.
                If a message is updated, use a new block_id.
            title (required): Title of the plan in plain text
            tasks: A sequence of task card blocks. Each task represents a single action within the plan.
        """
        super().__init__(type=self.type, block_id=block_id)
        show_unknown_key_warning(self, others)

        self.title = title
        self.tasks = tasks
```

Blocks are a series of components that can be combined to create visually rich and compellingly interactive messages. [https://docs.slack.dev/reference/block-kit/blocks](https://docs.slack.dev/reference/block-kit/blocks)

Displays a collection of related tasks. [https://docs.slack.dev/reference/block-kit/blocks/plan-block/](https://docs.slack.dev/reference/block-kit/blocks/plan-block/)

## Args (34)

**`block_id`**

A string acting as a unique identifier for a block. If not specified, one will be generated. Maximum length for this field is 255 characters. block\_id should be unique for each message and each iteration of a message. If a message is updated, use a new block\_id.

**`title`** : `required`

Title of the plan in plain text

**`tasks`**

A sequence of task card blocks. Each task represents a single action within the plan.

### Ancestors (40)

* [Block](blocks.html#slack_sdk.models.blocks.blocks.Block "slack_sdk.models.blocks.blocks.Block")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (39)

`var type`

The type of the None singleton.

### Instance variables (29)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union(
        {
            "title",
            "tasks",
        }
    )
```

Build an unordered collection of unique elements.

### Inherited members (40)

* `**[Block](blocks.html#slack_sdk.models.blocks.blocks.Block "slack_sdk.models.blocks.blocks.Block")**`:
  * `[block_id_max_length](blocks.html#slack_sdk.models.blocks.blocks.Block.block_id_max_length "slack_sdk.models.blocks.blocks.Block.block_id_max_length")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.blocks.Block.get_non_null_attributes")`
  * `[logger](blocks.html#slack_sdk.models.blocks.blocks.Block.logger "slack_sdk.models.blocks.blocks.Block.logger")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.blocks.Block.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.blocks.Block.validate_json")`

`class RadioButtonsElement (*,   action_id: str | None = None,   options: Sequence[dict | [Option](basic_components.html#slack_sdk.models.blocks.basic_components.Option "slack_sdk.models.blocks.basic_components.Option")] | None = None,   initial_option: dict | [Option](basic_components.html#slack_sdk.models.blocks.basic_components.Option "slack_sdk.models.blocks.basic_components.Option") | None = None,   confirm: dict | [ConfirmObject](basic_components.html#slack_sdk.models.blocks.basic_components.ConfirmObject "slack_sdk.models.blocks.basic_components.ConfirmObject") | None = None,   focus_on_load: bool | None = None,   **others: dict)`

Expand source code

```typescript
class RadioButtonsElement(InputInteractiveElement):
    type = "radio_buttons"

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union({"options", "initial_option"})

    def __init__(
        self,
        *,
        action_id: Optional[str] = None,
        options: Optional[Sequence[Union[dict, Option]]] = None,
        initial_option: Optional[Union[dict, Option]] = None,
        confirm: Optional[Union[dict, ConfirmObject]] = None,
        focus_on_load: Optional[bool] = None,
        **others: dict,
    ):
        """A radio button group that allows a user to choose one item from a list of possible options.
        https://docs.slack.dev/reference/block-kit/block-elements/radio-button-group-element

        Args:
            action_id (required): An identifier for the action triggered when the radio button group is changed.
                You can use this when you receive an interaction payload to identify the source of the action.
                Should be unique among all other action_ids in the containing block.
                Maximum length for this field is 255 characters.
            options (required): An array of option objects. A maximum of 10 options are allowed.
            initial_option: An option object that exactly matches one of the options.
                This option will be selected when the radio button group initially loads.
            confirm: A confirm object that defines an optional confirmation dialog that appears
                after clicking one of the radio buttons in this element.
            focus_on_load: Indicates whether the element will be set to auto focus within the view object.
                Only one element can be set to true. Defaults to false.
        """
        super().__init__(
            type=self.type,
            action_id=action_id,
            confirm=ConfirmObject.parse(confirm),  # type: ignore[arg-type]
            focus_on_load=focus_on_load,
        )
        show_unknown_key_warning(self, others)

        self.options = options
        self.initial_option = initial_option
```

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

A radio button group that allows a user to choose one item from a list of possible options. [https://docs.slack.dev/reference/block-kit/block-elements/radio-button-group-element](https://docs.slack.dev/reference/block-kit/block-elements/radio-button-group-element)

## Args (35)

**`action_id`** : `required`

An identifier for the action triggered when the radio button group is changed. You can use this when you receive an interaction payload to identify the source of the action. Should be unique among all other action\_ids in the containing block. Maximum length for this field is 255 characters.

**`options`** : `required`

An array of option objects. A maximum of 10 options are allowed.

**`initial_option`**

An option object that exactly matches one of the options. This option will be selected when the radio button group initially loads.

**`confirm`**

A confirm object that defines an optional confirmation dialog that appears after clicking one of the radio buttons in this element.

**`focus_on_load`**

Indicates whether the element will be set to auto focus within the view object. Only one element can be set to true. Defaults to false.

### Ancestors (41)

* [InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")
* [InteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement "slack_sdk.models.blocks.block_elements.InteractiveElement")
* [BlockElement](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (40)

`var type`

The type of the None singleton.

### Instance variables (30)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union({"options", "initial_option"})
```

Build an unordered collection of unique elements.

### Inherited members (41)

* `**[InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")**`:
  * `[action_id_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement.action_id_max_length "slack_sdk.models.blocks.block_elements.InputInteractiveElement.action_id_max_length")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.block_elements.InputInteractiveElement.get_non_null_attributes")`
  * `[logger](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement.logger "slack_sdk.models.blocks.block_elements.InputInteractiveElement.logger")`
  * `[placeholder_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement.placeholder_max_length "slack_sdk.models.blocks.block_elements.InputInteractiveElement.placeholder_max_length")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.block_elements.InputInteractiveElement.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.block_elements.InputInteractiveElement.validate_json")`

`class RawTextObject (*, text: str)`

Expand source code

```typescript
class RawTextObject(TextObject):
    """raw_text typed text object"""

    type = "raw_text"

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return {"text", "type"}

    def __init__(self, *, text: str):
        """A raw text object used in table block cells.
        https://docs.slack.dev/reference/block-kit/composition-objects/text-object/
        https://docs.slack.dev/reference/block-kit/blocks/table-block

        Args:
            text (required): The text content for the table block cell.
        """
        super().__init__(text=text, type=self.type)

    @staticmethod
    def from_str(text: str) -> "RawTextObject":
        """Transforms a string into a RawTextObject"""
        return RawTextObject(text=text)

    @staticmethod
    def direct_from_string(text: str) -> Dict[str, Any]:
        """Transforms a string into the required object shape to act as a RawTextObject"""
        return RawTextObject.from_str(text).to_dict()

    @JsonValidator("text attribute must have at least 1 character")
    def _validate_text_min_length(self):
        return len(self.text) >= 1
```

raw\_text typed text object

A raw text object used in table block cells. [https://docs.slack.dev/reference/block-kit/composition-objects/text-object/](https://docs.slack.dev/reference/block-kit/composition-objects/text-object/) [https://docs.slack.dev/reference/block-kit/blocks/table-block](https://docs.slack.dev/reference/block-kit/blocks/table-block)

## Args (36)

**`text`** : `required`

The text content for the table block cell.

### Ancestors (42)

* [TextObject](basic_components.html#slack_sdk.models.blocks.basic_components.TextObject "slack_sdk.models.blocks.basic_components.TextObject")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (41)

`var type`

The type of the None singleton.

### Static methods (10)

`def direct_from_string(text: str) ‑> Dict[str, Any]`

Expand source code

```typescript
@staticmethod
def direct_from_string(text: str) -> Dict[str, Any]:
    """Transforms a string into the required object shape to act as a RawTextObject"""
    return RawTextObject.from_str(text).to_dict()
```

Transforms a string into the required object shape to act as a RawTextObject

`def from_str(text: str) ‑> [RawTextObject](basic_components.html#slack_sdk.models.blocks.basic_components.RawTextObject "slack_sdk.models.blocks.basic_components.RawTextObject")`

Expand source code

```typescript
@staticmethod
def from_str(text: str) -> "RawTextObject":
    """Transforms a string into a RawTextObject"""
    return RawTextObject(text=text)
```

Transforms a string into a RawTextObject

### Instance variables (31)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return {"text", "type"}
```

Build an unordered collection of unique elements.

### Inherited members (42)

* `**[TextObject](basic_components.html#slack_sdk.models.blocks.basic_components.TextObject "slack_sdk.models.blocks.basic_components.TextObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.basic_components.TextObject.get_non_null_attributes")`
  * `[logger](basic_components.html#slack_sdk.models.blocks.basic_components.TextObject.logger "slack_sdk.models.blocks.basic_components.TextObject.logger")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.basic_components.TextObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.basic_components.TextObject.validate_json")`

`class RichTextBlock (*,   elements: Sequence[dict | [RichTextElement](block_elements.html#slack_sdk.models.blocks.block_elements.RichTextElement "slack_sdk.models.blocks.block_elements.RichTextElement")],   block_id: str | None = None,   **others: dict)`

Expand source code

```typescript
class RichTextBlock(Block):
    type = "rich_text"

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union({"elements"})

    def __init__(
        self,
        *,
        elements: Sequence[Union[dict, RichTextElement]],
        block_id: Optional[str] = None,
        **others: dict,
    ):
        """A block that is used to hold interactive elements.
        https://docs.slack.dev/reference/block-kit/blocks/rich-text-block

        Args:
            elements (required): An array of rich text objects -
                rich_text_section, rich_text_list, rich_text_quote, rich_text_preformatted
            block_id: A unique identifier for a block. If not specified, one will be generated.
                Maximum length for this field is 255 characters.
                block_id should be unique for each message or view and each iteration of a message or view.
                If a message or view is updated, use a new block_id.
        """
        super().__init__(type=self.type, block_id=block_id)
        show_unknown_key_warning(self, others)

        self.elements = BlockElement.parse_all(elements)
```

Blocks are a series of components that can be combined to create visually rich and compellingly interactive messages. [https://docs.slack.dev/reference/block-kit/blocks](https://docs.slack.dev/reference/block-kit/blocks)

A block that is used to hold interactive elements. [https://docs.slack.dev/reference/block-kit/blocks/rich-text-block](https://docs.slack.dev/reference/block-kit/blocks/rich-text-block)

## Args (37)

**`elements`** : `required`

An array of rich text objects - rich\_text\_section, rich\_text\_list, rich\_text\_quote, rich\_text\_preformatted

**`block_id`**

A unique identifier for a block. If not specified, one will be generated. Maximum length for this field is 255 characters. block\_id should be unique for each message or view and each iteration of a message or view. If a message or view is updated, use a new block\_id.

### Ancestors (43)

* [Block](blocks.html#slack_sdk.models.blocks.blocks.Block "slack_sdk.models.blocks.blocks.Block")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (42)

`var type`

The type of the None singleton.

### Instance variables (32)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union({"elements"})
```

Build an unordered collection of unique elements.

### Inherited members (43)

* `**[Block](blocks.html#slack_sdk.models.blocks.blocks.Block "slack_sdk.models.blocks.blocks.Block")**`:
  * `[block_id_max_length](blocks.html#slack_sdk.models.blocks.blocks.Block.block_id_max_length "slack_sdk.models.blocks.blocks.Block.block_id_max_length")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.blocks.Block.get_non_null_attributes")`
  * `[logger](blocks.html#slack_sdk.models.blocks.blocks.Block.logger "slack_sdk.models.blocks.blocks.Block.logger")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.blocks.Block.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.blocks.Block.validate_json")`

`class RichTextElement (*, type: str | None = None, subtype: str | None = None, **others: dict)`

Expand source code

```text
class RichTextElement(BlockElement):
    pass
```

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

### Ancestors (44)

* [BlockElement](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Subclasses (6)

* [RichTextElementParts.Broadcast](block_elements.html#slack_sdk.models.blocks.block_elements.RichTextElementParts.Broadcast "slack_sdk.models.blocks.block_elements.RichTextElementParts.Broadcast")
* [RichTextElementParts.Channel](block_elements.html#slack_sdk.models.blocks.block_elements.RichTextElementParts.Channel "slack_sdk.models.blocks.block_elements.RichTextElementParts.Channel")
* [RichTextElementParts.Color](block_elements.html#slack_sdk.models.blocks.block_elements.RichTextElementParts.Color "slack_sdk.models.blocks.block_elements.RichTextElementParts.Color")
* [RichTextElementParts.Date](block_elements.html#slack_sdk.models.blocks.block_elements.RichTextElementParts.Date "slack_sdk.models.blocks.block_elements.RichTextElementParts.Date")
* [RichTextElementParts.Emoji](block_elements.html#slack_sdk.models.blocks.block_elements.RichTextElementParts.Emoji "slack_sdk.models.blocks.block_elements.RichTextElementParts.Emoji")
* [RichTextElementParts.Link](block_elements.html#slack_sdk.models.blocks.block_elements.RichTextElementParts.Link "slack_sdk.models.blocks.block_elements.RichTextElementParts.Link")
* [RichTextElementParts.Team](block_elements.html#slack_sdk.models.blocks.block_elements.RichTextElementParts.Team "slack_sdk.models.blocks.block_elements.RichTextElementParts.Team")
* [RichTextElementParts.Text](block_elements.html#slack_sdk.models.blocks.block_elements.RichTextElementParts.Text "slack_sdk.models.blocks.block_elements.RichTextElementParts.Text")
* [RichTextElementParts.User](block_elements.html#slack_sdk.models.blocks.block_elements.RichTextElementParts.User "slack_sdk.models.blocks.block_elements.RichTextElementParts.User")
* [RichTextElementParts.UserGroup](block_elements.html#slack_sdk.models.blocks.block_elements.RichTextElementParts.UserGroup "slack_sdk.models.blocks.block_elements.RichTextElementParts.UserGroup")
* [RichTextListElement](block_elements.html#slack_sdk.models.blocks.block_elements.RichTextListElement "slack_sdk.models.blocks.block_elements.RichTextListElement")
* [RichTextPreformattedElement](block_elements.html#slack_sdk.models.blocks.block_elements.RichTextPreformattedElement "slack_sdk.models.blocks.block_elements.RichTextPreformattedElement")
* [RichTextQuoteElement](block_elements.html#slack_sdk.models.blocks.block_elements.RichTextQuoteElement "slack_sdk.models.blocks.block_elements.RichTextQuoteElement")
* [RichTextSectionElement](block_elements.html#slack_sdk.models.blocks.block_elements.RichTextSectionElement "slack_sdk.models.blocks.block_elements.RichTextSectionElement")

### Inherited members (44)

* `**[BlockElement](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement")**`:
  * `[attributes](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement.attributes "slack_sdk.models.blocks.block_elements.BlockElement.attributes")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.block_elements.BlockElement.get_non_null_attributes")`
  * `[logger](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement.logger "slack_sdk.models.blocks.block_elements.BlockElement.logger")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.block_elements.BlockElement.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.block_elements.BlockElement.validate_json")`

`class RichTextElementParts`

Expand source code

```typescript
class RichTextElementParts:
    class TextStyle:
        def __init__(
            self,
            *,
            bold: Optional[bool] = None,
            italic: Optional[bool] = None,
            strike: Optional[bool] = None,
            code: Optional[bool] = None,
            underline: Optional[bool] = None,
        ):
            self.bold = bold
            self.italic = italic
            self.strike = strike
            self.code = code
            self.underline = underline

        def to_dict(self, *args) -> dict:
            result = {
                "bold": self.bold,
                "italic": self.italic,
                "strike": self.strike,
                "code": self.code,
                "underline": self.underline,
            }
            return {k: v for k, v in result.items() if v is not None}

    class Text(RichTextElement):
        type = "text"

        @property
        def attributes(self) -> Set[str]:  # type: ignore[override]
            return super().attributes.union({"text", "style"})

        def __init__(
            self,
            *,
            text: str,
            style: Optional[Union[dict, "RichTextElementParts.TextStyle"]] = None,
            **others: dict,
        ):
            super().__init__(type=self.type)
            show_unknown_key_warning(self, others)
            self.text = text
            self.style = style

    class Channel(RichTextElement):
        type = "channel"

        @property
        def attributes(self) -> Set[str]:  # type: ignore[override]
            return super().attributes.union({"channel_id", "style"})

        def __init__(
            self,
            *,
            channel_id: str,
            style: Optional[Union[dict, "RichTextElementParts.TextStyle"]] = None,
            **others: dict,
        ):
            super().__init__(type=self.type)
            show_unknown_key_warning(self, others)
            self.channel_id = channel_id
            self.style = style

    class User(RichTextElement):
        type = "user"

        @property
        def attributes(self) -> Set[str]:  # type: ignore[override]
            return super().attributes.union({"user_id", "style"})

        def __init__(
            self,
            *,
            user_id: str,
            style: Optional[Union[dict, "RichTextElementParts.TextStyle"]] = None,
            **others: dict,
        ):
            super().__init__(type=self.type)
            show_unknown_key_warning(self, others)
            self.user_id = user_id
            self.style = style

    class Emoji(RichTextElement):
        type = "emoji"

        @property
        def attributes(self) -> Set[str]:  # type: ignore[override]
            return super().attributes.union({"name", "skin_tone", "unicode", "style"})

        def __init__(
            self,
            *,
            name: str,
            skin_tone: Optional[int] = None,
            unicode: Optional[str] = None,
            style: Optional[Union[dict, "RichTextElementParts.TextStyle"]] = None,
            **others: dict,
        ):
            super().__init__(type=self.type)
            show_unknown_key_warning(self, others)
            self.name = name
            self.skin_tone = skin_tone
            self.unicode = unicode
            self.style = style

    class Link(RichTextElement):
        type = "link"

        @property
        def attributes(self) -> Set[str]:  # type: ignore[override]
            return super().attributes.union({"url", "text", "style"})

        def __init__(
            self,
            *,
            url: str,
            text: Optional[str] = None,
            style: Optional[Union[dict, "RichTextElementParts.TextStyle"]] = None,
            **others: dict,
        ):
            super().__init__(type=self.type)
            show_unknown_key_warning(self, others)
            self.url = url
            self.text = text
            self.style = style

    class Team(RichTextElement):
        type = "team"

        @property
        def attributes(self) -> Set[str]:  # type: ignore[override]
            return super().attributes.union({"team_id", "style"})

        def __init__(
            self,
            *,
            team_id: str,
            style: Optional[Union[dict, "RichTextElementParts.TextStyle"]] = None,
            **others: dict,
        ):
            super().__init__(type=self.type)
            show_unknown_key_warning(self, others)
            self.team_id = team_id
            self.style = style

    class UserGroup(RichTextElement):
        type = "usergroup"

        @property
        def attributes(self) -> Set[str]:  # type: ignore[override]
            return super().attributes.union({"usergroup_id", "style"})

        def __init__(
            self,
            *,
            usergroup_id: str,
            style: Optional[Union[dict, "RichTextElementParts.TextStyle"]] = None,
            **others: dict,
        ):
            super().__init__(type=self.type)
            show_unknown_key_warning(self, others)
            self.usergroup_id = usergroup_id
            self.style = style

    class Date(RichTextElement):
        type = "date"

        @property
        def attributes(self) -> Set[str]:  # type: ignore[override]
            return super().attributes.union({"timestamp", "format", "url", "fallback"})

        def __init__(
            self,
            *,
            timestamp: int,
            format: str,
            url: Optional[str] = None,
            fallback: Optional[str] = None,
            **others: dict,
        ):
            super().__init__(type=self.type)
            show_unknown_key_warning(self, others)
            self.timestamp = timestamp
            self.format = format
            self.url = url
            self.fallback = fallback

    class Broadcast(RichTextElement):
        type = "broadcast"

        @property
        def attributes(self) -> Set[str]:  # type: ignore[override]
            return super().attributes.union({"range"})

        def __init__(
            self,
            *,
            range: str,  # channel, here, ..
            **others: dict,
        ):
            super().__init__(type=self.type)
            show_unknown_key_warning(self, others)
            self.range = range

    class Color(RichTextElement):
        type = "color"

        @property
        def attributes(self) -> Set[str]:  # type: ignore[override]
            return super().attributes.union({"value"})

        def __init__(
            self,
            *,
            value: str,
            **others: dict,
        ):
            super().__init__(type=self.type)
            show_unknown_key_warning(self, others)
            self.value = value
```

### Class variables (43)

`var Broadcast`

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

`var Channel`

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

`var Color`

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

`var Date`

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

`var Emoji`

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

`var Link`

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

`var Team`

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

`var Text`

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

`var TextStyle`

The type of the None singleton.

`var User`

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

`var UserGroup`

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

`class RichTextInputElement (*,   action_id: str | None = None,   placeholder: str | dict | [TextObject](basic_components.html#slack_sdk.models.blocks.basic_components.TextObject "slack_sdk.models.blocks.basic_components.TextObject") | None = None,   initial_value: Dict[str, Any] | [RichTextBlock](#slack_sdk.models.blocks.RichTextBlock "slack_sdk.models.blocks.RichTextBlock") | None = None,   dispatch_action_config: dict | [DispatchActionConfig](basic_components.html#slack_sdk.models.blocks.basic_components.DispatchActionConfig "slack_sdk.models.blocks.basic_components.DispatchActionConfig") | None = None,   focus_on_load: bool | None = None,   **others: dict)`

Expand source code

```typescript
class RichTextInputElement(InputInteractiveElement):
    type = "rich_text_input"

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union(
            {
                "initial_value",
                "dispatch_action_config",
            }
        )

    def __init__(
        self,
        *,
        action_id: Optional[str] = None,
        placeholder: Optional[Union[str, dict, TextObject]] = None,
        # To avoid circular imports, the RichTextBlock type here is intentionally a string
        initial_value: Optional[Union[Dict[str, Any], "RichTextBlock"]] = None,  # type: ignore[name-defined] # noqa: F821
        dispatch_action_config: Optional[Union[dict, DispatchActionConfig]] = None,
        focus_on_load: Optional[bool] = None,
        **others: dict,
    ):
        super().__init__(
            type=self.type,
            action_id=action_id,
            placeholder=TextObject.parse(placeholder, PlainTextObject.type),  # type: ignore[arg-type]
            focus_on_load=focus_on_load,
        )
        show_unknown_key_warning(self, others)

        self.initial_value = initial_value
        self.dispatch_action_config = dispatch_action_config
```

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

InteractiveElement that is usable in input blocks

We generally recommend using the concrete subclasses for better supports of available properties.

### Ancestors (45)

* [InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")
* [InteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement "slack_sdk.models.blocks.block_elements.InteractiveElement")
* [BlockElement](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (44)

`var type`

The type of the None singleton.

### Instance variables (33)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union(
        {
            "initial_value",
            "dispatch_action_config",
        }
    )
```

Build an unordered collection of unique elements.

### Inherited members (45)

* `**[InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")**`:
  * `[action_id_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement.action_id_max_length "slack_sdk.models.blocks.block_elements.InputInteractiveElement.action_id_max_length")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.block_elements.InputInteractiveElement.get_non_null_attributes")`
  * `[logger](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement.logger "slack_sdk.models.blocks.block_elements.InputInteractiveElement.logger")`
  * `[placeholder_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement.placeholder_max_length "slack_sdk.models.blocks.block_elements.InputInteractiveElement.placeholder_max_length")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.block_elements.InputInteractiveElement.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.block_elements.InputInteractiveElement.validate_json")`

`class RichTextListElement (*,   elements: Sequence[dict | [RichTextElement](block_elements.html#slack_sdk.models.blocks.block_elements.RichTextElement "slack_sdk.models.blocks.block_elements.RichTextElement")],   style: str | None = None,   indent: int | None = None,   offset: int | None = None,   border: int | None = None,   **others: dict)`

Expand source code

```typescript
class RichTextListElement(RichTextElement):
    type = "rich_text_list"

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union({"elements", "style", "indent", "offset", "border"})

    def __init__(
        self,
        *,
        elements: Sequence[Union[dict, RichTextElement]],
        style: Optional[str] = None,  # bullet, ordered
        indent: Optional[int] = None,
        offset: Optional[int] = None,
        border: Optional[int] = None,
        **others: dict,
    ):
        super().__init__(type=self.type)
        show_unknown_key_warning(self, others)
        self.elements = BlockElement.parse_all(elements)
        self.style = style
        self.indent = indent
        self.offset = offset
        self.border = border
```

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

### Ancestors (46)

* [RichTextElement](block_elements.html#slack_sdk.models.blocks.block_elements.RichTextElement "slack_sdk.models.blocks.block_elements.RichTextElement")
* [BlockElement](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (45)

`var type`

The type of the None singleton.

### Instance variables (34)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union({"elements", "style", "indent", "offset", "border"})
```

Build an unordered collection of unique elements.

### Inherited members (46)

* `**[RichTextElement](block_elements.html#slack_sdk.models.blocks.block_elements.RichTextElement "slack_sdk.models.blocks.block_elements.RichTextElement")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.block_elements.RichTextElement.get_non_null_attributes")`
  * `[logger](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement.logger "slack_sdk.models.blocks.block_elements.RichTextElement.logger")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.block_elements.RichTextElement.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.block_elements.RichTextElement.validate_json")`

`class RichTextPreformattedElement (*,   elements: Sequence[dict | [RichTextElement](block_elements.html#slack_sdk.models.blocks.block_elements.RichTextElement "slack_sdk.models.blocks.block_elements.RichTextElement")],   border: int | None = None,   **others: dict)`

Expand source code

```typescript
class RichTextPreformattedElement(RichTextElement):
    type = "rich_text_preformatted"

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union({"elements", "border"})

    def __init__(
        self,
        *,
        elements: Sequence[Union[dict, RichTextElement]],
        border: Optional[int] = None,
        **others: dict,
    ):
        super().__init__(type=self.type)
        show_unknown_key_warning(self, others)
        self.elements = BlockElement.parse_all(elements)
        self.border = border
```

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

### Ancestors (47)

* [RichTextElement](block_elements.html#slack_sdk.models.blocks.block_elements.RichTextElement "slack_sdk.models.blocks.block_elements.RichTextElement")
* [BlockElement](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (46)

`var type`

The type of the None singleton.

### Instance variables (35)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union({"elements", "border"})
```

Build an unordered collection of unique elements.

### Inherited members (47)

* `**[RichTextElement](block_elements.html#slack_sdk.models.blocks.block_elements.RichTextElement "slack_sdk.models.blocks.block_elements.RichTextElement")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.block_elements.RichTextElement.get_non_null_attributes")`
  * `[logger](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement.logger "slack_sdk.models.blocks.block_elements.RichTextElement.logger")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.block_elements.RichTextElement.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.block_elements.RichTextElement.validate_json")`

`class RichTextQuoteElement (*,   elements: Sequence[dict | [RichTextElement](block_elements.html#slack_sdk.models.blocks.block_elements.RichTextElement "slack_sdk.models.blocks.block_elements.RichTextElement")],   **others: dict)`

Expand source code

```typescript
class RichTextQuoteElement(RichTextElement):
    type = "rich_text_quote"

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union({"elements"})

    def __init__(
        self,
        *,
        elements: Sequence[Union[dict, RichTextElement]],
        **others: dict,
    ):
        super().__init__(type=self.type)
        show_unknown_key_warning(self, others)
        self.elements = BlockElement.parse_all(elements)
```

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

### Ancestors (48)

* [RichTextElement](block_elements.html#slack_sdk.models.blocks.block_elements.RichTextElement "slack_sdk.models.blocks.block_elements.RichTextElement")
* [BlockElement](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (47)

`var type`

The type of the None singleton.

### Instance variables (36)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union({"elements"})
```

Build an unordered collection of unique elements.

### Inherited members (48)

* `**[RichTextElement](block_elements.html#slack_sdk.models.blocks.block_elements.RichTextElement "slack_sdk.models.blocks.block_elements.RichTextElement")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.block_elements.RichTextElement.get_non_null_attributes")`
  * `[logger](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement.logger "slack_sdk.models.blocks.block_elements.RichTextElement.logger")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.block_elements.RichTextElement.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.block_elements.RichTextElement.validate_json")`

`class RichTextSectionElement (*,   elements: Sequence[dict | [RichTextElement](block_elements.html#slack_sdk.models.blocks.block_elements.RichTextElement "slack_sdk.models.blocks.block_elements.RichTextElement")],   **others: dict)`

Expand source code

```typescript
class RichTextSectionElement(RichTextElement):
    type = "rich_text_section"

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union({"elements"})

    def __init__(
        self,
        *,
        elements: Sequence[Union[dict, RichTextElement]],
        **others: dict,
    ):
        super().__init__(type=self.type)
        show_unknown_key_warning(self, others)
        self.elements = BlockElement.parse_all(elements)
```

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

### Ancestors (49)

* [RichTextElement](block_elements.html#slack_sdk.models.blocks.block_elements.RichTextElement "slack_sdk.models.blocks.block_elements.RichTextElement")
* [BlockElement](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (48)

`var type`

The type of the None singleton.

### Instance variables (37)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union({"elements"})
```

Build an unordered collection of unique elements.

### Inherited members (49)

* `**[RichTextElement](block_elements.html#slack_sdk.models.blocks.block_elements.RichTextElement "slack_sdk.models.blocks.block_elements.RichTextElement")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.block_elements.RichTextElement.get_non_null_attributes")`
  * `[logger](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement.logger "slack_sdk.models.blocks.block_elements.RichTextElement.logger")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.block_elements.RichTextElement.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.block_elements.RichTextElement.validate_json")`

`class SectionBlock (*,   block_id: str | None = None,   text: str | dict | [TextObject](basic_components.html#slack_sdk.models.blocks.basic_components.TextObject "slack_sdk.models.blocks.basic_components.TextObject") | None = None,   fields: Sequence[str | dict | [TextObject](basic_components.html#slack_sdk.models.blocks.basic_components.TextObject "slack_sdk.models.blocks.basic_components.TextObject")] | None = None,   accessory: dict | [BlockElement](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement") | None = None,   expand: bool | None = None,   **others: dict)`

Expand source code

```typescript
class SectionBlock(Block):
    type = "section"
    fields_max_length = 10
    text_max_length = 3000

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union({"text", "fields", "accessory", "expand"})

    def __init__(
        self,
        *,
        block_id: Optional[str] = None,
        text: Optional[Union[str, dict, TextObject]] = None,
        fields: Optional[Sequence[Union[str, dict, TextObject]]] = None,
        accessory: Optional[Union[dict, BlockElement]] = None,
        expand: Optional[bool] = None,
        **others: dict,
    ):
        """A section is one of the most flexible blocks available.
        https://docs.slack.dev/reference/block-kit/blocks/section-block

        Args:
            block_id (required): A string acting as a unique identifier for a block.
                If not specified, one will be generated.
                You can use this block_id when you receive an interaction payload to identify the source of the action.
                Maximum length for this field is 255 characters.
                block_id should be unique for each message and each iteration of a message.
                If a message is updated, use a new block_id.
            text (preferred): The text for the block, in the form of a text object.
                Maximum length for the text in this field is 3000 characters.
                This field is not required if a valid array of fields objects is provided instead.
            fields (required if no text is provided): Required if no text is provided.
                An array of text objects. Any text objects included with fields will be rendered
                in a compact format that allows for 2 columns of side-by-side text.
                Maximum number of items is 10. Maximum length for the text in each item is 2000 characters.
            accessory: One of the available element objects.
            expand: Whether or not this section block's text should always expand when rendered.
                If false or not provided, it may be rendered with a 'see more' option to expand and show the full text.
                For AI Assistant apps, this allows the app to post long messages without users needing
                to click 'see more' to expand the message.
        """
        super().__init__(type=self.type, block_id=block_id)
        show_unknown_key_warning(self, others)

        self.text = TextObject.parse(text)  # type: ignore[arg-type]
        field_objects = []
        for f in fields or []:
            if isinstance(f, str):
                field_objects.append(MarkdownTextObject.from_str(f))
            elif isinstance(f, TextObject):
                field_objects.append(f)  # type: ignore[arg-type]
            elif isinstance(f, dict) and "type" in f:
                d = copy.copy(f)
                t = d.pop("type")
                if t == MarkdownTextObject.type:
                    field_objects.append(MarkdownTextObject(**d))
                else:
                    field_objects.append(PlainTextObject(**d))  # type: ignore[arg-type]
            else:
                self.logger.warning(f"Unsupported filed detected and skipped {f}")
        self.fields = field_objects
        self.accessory = BlockElement.parse(accessory)  # type: ignore[arg-type]
        self.expand = expand

    @JsonValidator("text or fields attribute must be specified")
    def _validate_text_or_fields_populated(self):
        return self.text is not None or self.fields

    @JsonValidator(f"fields attribute cannot exceed {fields_max_length} items")
    def _validate_fields_length(self):
        return self.fields is None or len(self.fields) <= self.fields_max_length

    @JsonValidator(f"text attribute cannot exceed {text_max_length} characters")
    def _validate_alt_text_length(self):
        return self.text is None or len(self.text.text) <= self.text_max_length
```

Blocks are a series of components that can be combined to create visually rich and compellingly interactive messages. [https://docs.slack.dev/reference/block-kit/blocks](https://docs.slack.dev/reference/block-kit/blocks)

A section is one of the most flexible blocks available. [https://docs.slack.dev/reference/block-kit/blocks/section-block](https://docs.slack.dev/reference/block-kit/blocks/section-block)

## Args (38)

**`block_id`** : `required`

A string acting as a unique identifier for a block. If not specified, one will be generated. You can use this block\_id when you receive an interaction payload to identify the source of the action. Maximum length for this field is 255 characters. block\_id should be unique for each message and each iteration of a message. If a message is updated, use a new block\_id.

**`text`** : `preferred`

The text for the block, in the form of a text object. Maximum length for the text in this field is 3000 characters. This field is not required if a valid array of fields objects is provided instead.

**`fields`** : `required if no text is provided`

Required if no text is provided. An array of text objects. Any text objects included with fields will be rendered in a compact format that allows for 2 columns of side-by-side text. Maximum number of items is 10. Maximum length for the text in each item is 2000 characters.

**`accessory`**

One of the available element objects.

**`expand`**

Whether or not this section block's text should always expand when rendered. If false or not provided, it may be rendered with a 'see more' option to expand and show the full text. For AI Assistant apps, this allows the app to post long messages without users needing to click 'see more' to expand the message.

### Ancestors (50)

* [Block](blocks.html#slack_sdk.models.blocks.blocks.Block "slack_sdk.models.blocks.blocks.Block")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (49)

`var fields_max_length`

The type of the None singleton.

`var text_max_length`

The type of the None singleton.

`var type`

The type of the None singleton.

### Instance variables (38)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union({"text", "fields", "accessory", "expand"})
```

Build an unordered collection of unique elements.

### Inherited members (50)

* `**[Block](blocks.html#slack_sdk.models.blocks.blocks.Block "slack_sdk.models.blocks.blocks.Block")**`:
  * `[block_id_max_length](blocks.html#slack_sdk.models.blocks.blocks.Block.block_id_max_length "slack_sdk.models.blocks.blocks.Block.block_id_max_length")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.blocks.Block.get_non_null_attributes")`
  * `[logger](blocks.html#slack_sdk.models.blocks.blocks.Block.logger "slack_sdk.models.blocks.blocks.Block.logger")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.blocks.Block.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.blocks.Block.validate_json")`

`class SelectElement (*,   action_id: str | None = None,   placeholder: str | None = None,   options: Sequence[[Option](basic_components.html#slack_sdk.models.blocks.basic_components.Option "slack_sdk.models.blocks.basic_components.Option")] | None = None,   option_groups: Sequence[[OptionGroup](basic_components.html#slack_sdk.models.blocks.basic_components.OptionGroup "slack_sdk.models.blocks.basic_components.OptionGroup")] | None = None,   initial_option: [Option](basic_components.html#slack_sdk.models.blocks.basic_components.Option "slack_sdk.models.blocks.basic_components.Option") | None = None,   confirm: dict | [ConfirmObject](basic_components.html#slack_sdk.models.blocks.basic_components.ConfirmObject "slack_sdk.models.blocks.basic_components.ConfirmObject") | None = None,   focus_on_load: bool | None = None,   **others: dict)`

Expand source code

```typescript
class SelectElement(InputInteractiveElement):
    type = "static_select"
    options_max_length = 100
    option_groups_max_length = 100

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union({"options", "option_groups", "initial_option"})

    def __init__(
        self,
        *,
        action_id: Optional[str] = None,
        placeholder: Optional[str] = None,
        options: Optional[Sequence[Option]] = None,
        option_groups: Optional[Sequence[OptionGroup]] = None,
        initial_option: Optional[Option] = None,
        confirm: Optional[Union[dict, ConfirmObject]] = None,
        focus_on_load: Optional[bool] = None,
        **others: dict,
    ):
        """This is the simplest form of select menu, with a static list of options passed in when defining the element.
        https://docs.slack.dev/reference/block-kit/block-elements/select-menu-element#static_select

        Args:
            action_id (required): An identifier for the action triggered when a menu option is selected.
                You can use this when you receive an interaction payload to identify the source of the action.
                Should be unique among all other action_ids in the containing block.
                Maximum length for this field is 255 characters.
            placeholder (required): A plain_text only text object that defines the placeholder text shown on the menu.
                Maximum length for the text in this field is 150 characters.
            options (either options or option_groups is required): An array of option objects.
                Maximum number of options is 100.
                If option_groups is specified, this field should not be.
            option_groups (either options or option_groups is required): An array of option group objects.
                Maximum number of option groups is 100.
                If options is specified, this field should not be.
            initial_option: A single option that exactly matches one of the options or option_groups.
                This option will be selected when the menu initially loads.
            confirm: A confirm object that defines an optional confirmation dialog
                that appears after a menu item is selected.
            focus_on_load: Indicates whether the element will be set to auto focus within the view object.
                Only one element can be set to true. Defaults to false.
        """
        super().__init__(
            type=self.type,
            action_id=action_id,
            placeholder=TextObject.parse(placeholder, PlainTextObject.type),  # type: ignore[arg-type]
            confirm=ConfirmObject.parse(confirm),  # type: ignore[arg-type]
            focus_on_load=focus_on_load,
        )
        show_unknown_key_warning(self, others)

        self.options = options
        self.option_groups = option_groups
        self.initial_option = initial_option

    @JsonValidator(f"options attribute cannot exceed {options_max_length} elements")
    def _validate_options_length(self) -> bool:
        return self.options is None or len(self.options) <= self.options_max_length

    @JsonValidator(f"option_groups attribute cannot exceed {option_groups_max_length} elements")
    def _validate_option_groups_length(self) -> bool:
        return self.option_groups is None or len(self.option_groups) <= self.option_groups_max_length

    @JsonValidator("options and option_groups cannot both be specified")
    def _validate_options_and_option_groups_both_specified(self) -> bool:
        return not (self.options is not None and self.option_groups is not None)

    @JsonValidator("options or option_groups must be specified")
    def _validate_neither_options_or_option_groups_is_specified(self) -> bool:
        return self.options is not None or self.option_groups is not None
```

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

This is the simplest form of select menu, with a static list of options passed in when defining the element. [https://docs.slack.dev/reference/block-kit/block-elements/select-menu-element#static\_select](https://docs.slack.dev/reference/block-kit/block-elements/select-menu-element#static_select)

## Args (39)

**`action_id`** : `required`

An identifier for the action triggered when a menu option is selected. You can use this when you receive an interaction payload to identify the source of the action. Should be unique among all other action\_ids in the containing block. Maximum length for this field is 255 characters.

**`placeholder`** : `required`

A plain\_text only text object that defines the placeholder text shown on the menu. Maximum length for the text in this field is 150 characters.

**`options`** : `either options` or `option_groups is required`

An array of option objects. Maximum number of options is 100. If option\_groups is specified, this field should not be.

**`option_groups`** : `either options` or `option_groups is required`

An array of option group objects. Maximum number of option groups is 100. If options is specified, this field should not be.

**`initial_option`**

A single option that exactly matches one of the options or option\_groups. This option will be selected when the menu initially loads.

**`confirm`**

A confirm object that defines an optional confirmation dialog that appears after a menu item is selected.

**`focus_on_load`**

Indicates whether the element will be set to auto focus within the view object. Only one element can be set to true. Defaults to false.

### Ancestors (51)

* [InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")
* [InteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement "slack_sdk.models.blocks.block_elements.InteractiveElement")
* [BlockElement](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (50)

`var option_groups_max_length`

The type of the None singleton.

`var options_max_length`

The type of the None singleton.

`var type`

The type of the None singleton.

### Instance variables (39)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union({"options", "option_groups", "initial_option"})
```

Build an unordered collection of unique elements.

### Inherited members (51)

* `**[InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")**`:
  * `[action_id_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement.action_id_max_length "slack_sdk.models.blocks.block_elements.InputInteractiveElement.action_id_max_length")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.block_elements.InputInteractiveElement.get_non_null_attributes")`
  * `[logger](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement.logger "slack_sdk.models.blocks.block_elements.InputInteractiveElement.logger")`
  * `[placeholder_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement.placeholder_max_length "slack_sdk.models.blocks.block_elements.InputInteractiveElement.placeholder_max_length")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.block_elements.InputInteractiveElement.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.block_elements.InputInteractiveElement.validate_json")`

`class StaticMultiSelectElement (*,   placeholder: str | dict | [TextObject](basic_components.html#slack_sdk.models.blocks.basic_components.TextObject "slack_sdk.models.blocks.basic_components.TextObject") | None = None,   action_id: str | None = None,   options: Sequence[[Option](basic_components.html#slack_sdk.models.blocks.basic_components.Option "slack_sdk.models.blocks.basic_components.Option")] | None = None,   option_groups: Sequence[[OptionGroup](basic_components.html#slack_sdk.models.blocks.basic_components.OptionGroup "slack_sdk.models.blocks.basic_components.OptionGroup")] | None = None,   initial_options: Sequence[[Option](basic_components.html#slack_sdk.models.blocks.basic_components.Option "slack_sdk.models.blocks.basic_components.Option")] | None = None,   confirm: dict | [ConfirmObject](basic_components.html#slack_sdk.models.blocks.basic_components.ConfirmObject "slack_sdk.models.blocks.basic_components.ConfirmObject") | None = None,   max_selected_items: int | None = None,   focus_on_load: bool | None = None,   **others: dict)`

Expand source code

```typescript
class StaticMultiSelectElement(InputInteractiveElement):
    type = "multi_static_select"
    options_max_length = 100
    option_groups_max_length = 100

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union({"options", "option_groups", "initial_options", "max_selected_items"})

    def __init__(
        self,
        *,
        placeholder: Optional[Union[str, dict, TextObject]] = None,
        action_id: Optional[str] = None,
        options: Optional[Sequence[Option]] = None,
        option_groups: Optional[Sequence[OptionGroup]] = None,
        initial_options: Optional[Sequence[Option]] = None,
        confirm: Optional[Union[dict, ConfirmObject]] = None,
        max_selected_items: Optional[int] = None,
        focus_on_load: Optional[bool] = None,
        **others: dict,
    ):
        """
        This is the simplest form of select menu, with a static list of options passed in when defining the element.
        https://docs.slack.dev/reference/block-kit/block-elements/multi-select-menu-element#static_multi_select

        Args:
            placeholder (required): A plain_text only text object that defines the placeholder text shown on the menu.
                Maximum length for the text in this field is 150 characters.
            action_id (required): An identifier for the action triggered when a menu option is selected.
                You can use this when you receive an interaction payload to identify the source of the action.
                Should be unique among all other action_ids in the containing block.
                Maximum length for this field is 255 characters.
            options (either options or option_groups is required): An array of option objects.
                Maximum number of options is 100.
                If option_groups is specified, this field should not be.
            option_groups (either options or option_groups is required): An array of option group objects.
                Maximum number of option groups is 100.
                If options is specified, this field should not be.
            initial_options: An array of option objects that exactly match one or more of the options
                within options or option_groups. These options will be selected when the menu initially loads.
            confirm: A confirm object that defines an optional confirmation dialog
                that appears before the multi-select choices are submitted.
            max_selected_items: Specifies the maximum number of items that can be selected in the menu.
                Minimum number is 1.
            focus_on_load: Indicates whether the element will be set to auto focus within the view object.
                Only one element can be set to true. Defaults to false.
        """
        super().__init__(
            type=self.type,
            action_id=action_id,
            placeholder=TextObject.parse(placeholder, PlainTextObject.type),  # type: ignore[arg-type]
            confirm=ConfirmObject.parse(confirm),  # type: ignore[arg-type]
            focus_on_load=focus_on_load,
        )
        show_unknown_key_warning(self, others)

        self.options = Option.parse_all(options)
        self.option_groups = OptionGroup.parse_all(option_groups)
        self.initial_options = Option.parse_all(initial_options)
        self.max_selected_items = max_selected_items

    @JsonValidator(f"options attribute cannot exceed {options_max_length} elements")
    def _validate_options_length(self) -> bool:
        return self.options is None or len(self.options) <= self.options_max_length

    @JsonValidator(f"option_groups attribute cannot exceed {option_groups_max_length} elements")
    def _validate_option_groups_length(self) -> bool:
        return self.option_groups is None or len(self.option_groups) <= self.option_groups_max_length

    @JsonValidator("options and option_groups cannot both be specified")
    def _validate_options_and_option_groups_both_specified(self) -> bool:
        return self.options is None or self.option_groups is None

    @JsonValidator("options or option_groups must be specified")
    def _validate_neither_options_or_option_groups_is_specified(self) -> bool:
        return self.options is not None or self.option_groups is not None
```

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

This is the simplest form of select menu, with a static list of options passed in when defining the element. [https://docs.slack.dev/reference/block-kit/block-elements/multi-select-menu-element#static\_multi\_select](https://docs.slack.dev/reference/block-kit/block-elements/multi-select-menu-element#static_multi_select)

## Args (40)

**`placeholder`** : `required`

A plain\_text only text object that defines the placeholder text shown on the menu. Maximum length for the text in this field is 150 characters.

**`action_id`** : `required`

An identifier for the action triggered when a menu option is selected. You can use this when you receive an interaction payload to identify the source of the action. Should be unique among all other action\_ids in the containing block. Maximum length for this field is 255 characters.

**`options`** : `either options` or `option_groups is required`

An array of option objects. Maximum number of options is 100. If option\_groups is specified, this field should not be.

**`option_groups`** : `either options` or `option_groups is required`

An array of option group objects. Maximum number of option groups is 100. If options is specified, this field should not be.

**`initial_options`**

An array of option objects that exactly match one or more of the options within options or option\_groups. These options will be selected when the menu initially loads.

**`confirm`**

A confirm object that defines an optional confirmation dialog that appears before the multi-select choices are submitted.

**`max_selected_items`**

Specifies the maximum number of items that can be selected in the menu. Minimum number is 1.

**`focus_on_load`**

Indicates whether the element will be set to auto focus within the view object. Only one element can be set to true. Defaults to false.

### Ancestors (52)

* [InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")
* [InteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement "slack_sdk.models.blocks.block_elements.InteractiveElement")
* [BlockElement](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (51)

`var option_groups_max_length`

The type of the None singleton.

`var options_max_length`

The type of the None singleton.

`var type`

The type of the None singleton.

### Instance variables (40)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union({"options", "option_groups", "initial_options", "max_selected_items"})
```

Build an unordered collection of unique elements.

### Inherited members (52)

* `**[InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")**`:
  * `[action_id_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement.action_id_max_length "slack_sdk.models.blocks.block_elements.InputInteractiveElement.action_id_max_length")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.block_elements.InputInteractiveElement.get_non_null_attributes")`
  * `[logger](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement.logger "slack_sdk.models.blocks.block_elements.InputInteractiveElement.logger")`
  * `[placeholder_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement.placeholder_max_length "slack_sdk.models.blocks.block_elements.InputInteractiveElement.placeholder_max_length")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.block_elements.InputInteractiveElement.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.block_elements.InputInteractiveElement.validate_json")`

`class StaticSelectElement (*,   placeholder: str | dict | [TextObject](basic_components.html#slack_sdk.models.blocks.basic_components.TextObject "slack_sdk.models.blocks.basic_components.TextObject") | None = None,   action_id: str | None = None,   options: Sequence[dict | [Option](basic_components.html#slack_sdk.models.blocks.basic_components.Option "slack_sdk.models.blocks.basic_components.Option")] | None = None,   option_groups: Sequence[dict | [OptionGroup](basic_components.html#slack_sdk.models.blocks.basic_components.OptionGroup "slack_sdk.models.blocks.basic_components.OptionGroup")] | None = None,   initial_option: dict | [Option](basic_components.html#slack_sdk.models.blocks.basic_components.Option "slack_sdk.models.blocks.basic_components.Option") | None = None,   confirm: dict | [ConfirmObject](basic_components.html#slack_sdk.models.blocks.basic_components.ConfirmObject "slack_sdk.models.blocks.basic_components.ConfirmObject") | None = None,   focus_on_load: bool | None = None,   **others: dict)`

Expand source code

```typescript
class StaticSelectElement(InputInteractiveElement):
    type = "static_select"
    options_max_length = 100
    option_groups_max_length = 100

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union({"options", "option_groups", "initial_option"})

    def __init__(
        self,
        *,
        placeholder: Optional[Union[str, dict, TextObject]] = None,
        action_id: Optional[str] = None,
        options: Optional[Sequence[Union[dict, Option]]] = None,
        option_groups: Optional[Sequence[Union[dict, OptionGroup]]] = None,
        initial_option: Optional[Union[dict, Option]] = None,
        confirm: Optional[Union[dict, ConfirmObject]] = None,
        focus_on_load: Optional[bool] = None,
        **others: dict,
    ):
        """This is the simplest form of select menu, with a static list of options passed in when defining the element.
        https://docs.slack.dev/reference/block-kit/block-elements/select-menu-element#static_select

        Args:
            placeholder (required): A plain_text only text object that defines the placeholder text shown on the menu.
                Maximum length for the text in this field is 150 characters.
            action_id (required): An identifier for the action triggered when a menu option is selected.
                You can use this when you receive an interaction payload to identify the source of the action.
                Should be unique among all other action_ids in the containing block.
                Maximum length for this field is 255 characters.
            options (either options or option_groups is required): An array of option objects.
                Maximum number of options is 100.
                If option_groups is specified, this field should not be.
            option_groups (either options or option_groups is required): An array of option group objects.
                Maximum number of option groups is 100.
                If options is specified, this field should not be.
            initial_option: A single option that exactly matches one of the options or option_groups.
                This option will be selected when the menu initially loads.
            confirm: A confirm object that defines an optional confirmation dialog
                that appears after a menu item is selected.
            focus_on_load: Indicates whether the element will be set to auto focus within the view object.
                Only one element can be set to true. Defaults to false.
        """
        super().__init__(
            type=self.type,
            action_id=action_id,
            placeholder=TextObject.parse(placeholder, PlainTextObject.type),  # type: ignore[arg-type]
            confirm=ConfirmObject.parse(confirm),  # type: ignore[arg-type]
            focus_on_load=focus_on_load,
        )
        show_unknown_key_warning(self, others)

        self.options = options
        self.option_groups = option_groups
        self.initial_option = initial_option

    @JsonValidator(f"options attribute cannot exceed {options_max_length} elements")
    def _validate_options_length(self) -> bool:
        return self.options is None or len(self.options) <= self.options_max_length

    @JsonValidator(f"option_groups attribute cannot exceed {option_groups_max_length} elements")
    def _validate_option_groups_length(self) -> bool:
        return self.option_groups is None or len(self.option_groups) <= self.option_groups_max_length

    @JsonValidator("options and option_groups cannot both be specified")
    def _validate_options_and_option_groups_both_specified(self) -> bool:
        return not (self.options is not None and self.option_groups is not None)

    @JsonValidator("options or option_groups must be specified")
    def _validate_neither_options_or_option_groups_is_specified(self) -> bool:
        return self.options is not None or self.option_groups is not None
```

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

This is the simplest form of select menu, with a static list of options passed in when defining the element. [https://docs.slack.dev/reference/block-kit/block-elements/select-menu-element#static\_select](https://docs.slack.dev/reference/block-kit/block-elements/select-menu-element#static_select)

## Args (41)

**`placeholder`** : `required`

A plain\_text only text object that defines the placeholder text shown on the menu. Maximum length for the text in this field is 150 characters.

**`action_id`** : `required`

An identifier for the action triggered when a menu option is selected. You can use this when you receive an interaction payload to identify the source of the action. Should be unique among all other action\_ids in the containing block. Maximum length for this field is 255 characters.

**`options`** : `either options` or `option_groups is required`

An array of option objects. Maximum number of options is 100. If option\_groups is specified, this field should not be.

**`option_groups`** : `either options` or `option_groups is required`

An array of option group objects. Maximum number of option groups is 100. If options is specified, this field should not be.

**`initial_option`**

A single option that exactly matches one of the options or option\_groups. This option will be selected when the menu initially loads.

**`confirm`**

A confirm object that defines an optional confirmation dialog that appears after a menu item is selected.

**`focus_on_load`**

Indicates whether the element will be set to auto focus within the view object. Only one element can be set to true. Defaults to false.

### Ancestors (53)

* [InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")
* [InteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement "slack_sdk.models.blocks.block_elements.InteractiveElement")
* [BlockElement](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (52)

`var option_groups_max_length`

The type of the None singleton.

`var options_max_length`

The type of the None singleton.

`var type`

The type of the None singleton.

### Instance variables (41)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union({"options", "option_groups", "initial_option"})
```

Build an unordered collection of unique elements.

### Inherited members (53)

* `**[InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")**`:
  * `[action_id_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement.action_id_max_length "slack_sdk.models.blocks.block_elements.InputInteractiveElement.action_id_max_length")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.block_elements.InputInteractiveElement.get_non_null_attributes")`
  * `[logger](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement.logger "slack_sdk.models.blocks.block_elements.InputInteractiveElement.logger")`
  * `[placeholder_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement.placeholder_max_length "slack_sdk.models.blocks.block_elements.InputInteractiveElement.placeholder_max_length")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.block_elements.InputInteractiveElement.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.block_elements.InputInteractiveElement.validate_json")`

`class TableBlock (*,   rows: Sequence[Sequence[Dict[str, Any]]],   column_settings: Sequence[Dict[str, Any] | None] | None = None,   block_id: str | None = None,   **others: dict)`

Expand source code

```typescript
class TableBlock(Block):
    type = "table"

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union({"rows", "column_settings"})

    def __init__(
        self,
        *,
        rows: Sequence[Sequence[Dict[str, Any]]],
        column_settings: Optional[Sequence[Optional[Dict[str, Any]]]] = None,
        block_id: Optional[str] = None,
        **others: dict,
    ):
        """Displays structured information in a table.
        https://docs.slack.dev/reference/block-kit/blocks/table-block

        Args:
            rows (required): An array consisting of table rows. Maximum 100 rows.
                Each row object is an array with a max of 20 table cells.
                Table cells can have a type of raw_text or rich_text.
            column_settings: An array describing column behavior. If there are fewer items in the column_settings array
                than there are columns in the table, then the items in the the column_settings array will describe
                the same number of columns in the table as there are in the array itself.
                Any additional columns will have the default behavior. Maximum 20 items.
                See below for column settings schema.
            block_id: A unique identifier for a block. If not specified, a block_id will be generated.
                You can use this block_id when you receive an interaction payload to identify the source of the action.
                Maximum length for this field is 255 characters.
                block_id should be unique for each message and each iteration of a message.
                If a message is updated, use a new block_id.
        """
        super().__init__(type=self.type, block_id=block_id)
        show_unknown_key_warning(self, others)

        self.rows = rows
        self.column_settings = column_settings

    @JsonValidator("rows attribute must be specified")
    def _validate_rows(self):
        return self.rows is not None and len(self.rows) > 0
```

Blocks are a series of components that can be combined to create visually rich and compellingly interactive messages. [https://docs.slack.dev/reference/block-kit/blocks](https://docs.slack.dev/reference/block-kit/blocks)

Displays structured information in a table. [https://docs.slack.dev/reference/block-kit/blocks/table-block](https://docs.slack.dev/reference/block-kit/blocks/table-block)

## Args (42)

**`rows`** : `required`

An array consisting of table rows. Maximum 100 rows. Each row object is an array with a max of 20 table cells. Table cells can have a type of raw\_text or rich\_text.

**`column_settings`**

An array describing column behavior. If there are fewer items in the column\_settings array than there are columns in the table, then the items in the the column\_settings array will describe the same number of columns in the table as there are in the array itself. Any additional columns will have the default behavior. Maximum 20 items. See below for column settings schema.

**`block_id`**

A unique identifier for a block. If not specified, a block\_id will be generated. You can use this block\_id when you receive an interaction payload to identify the source of the action. Maximum length for this field is 255 characters. block\_id should be unique for each message and each iteration of a message. If a message is updated, use a new block\_id.

### Ancestors (54)

* [Block](blocks.html#slack_sdk.models.blocks.blocks.Block "slack_sdk.models.blocks.blocks.Block")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (53)

`var type`

The type of the None singleton.

### Instance variables (42)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union({"rows", "column_settings"})
```

Build an unordered collection of unique elements.

### Inherited members (54)

* `**[Block](blocks.html#slack_sdk.models.blocks.blocks.Block "slack_sdk.models.blocks.blocks.Block")**`:
  * `[block_id_max_length](blocks.html#slack_sdk.models.blocks.blocks.Block.block_id_max_length "slack_sdk.models.blocks.blocks.Block.block_id_max_length")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.blocks.Block.get_non_null_attributes")`
  * `[logger](blocks.html#slack_sdk.models.blocks.blocks.Block.logger "slack_sdk.models.blocks.blocks.Block.logger")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.blocks.Block.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.blocks.Block.validate_json")`

`class TaskCardBlock (*,   task_id: str,   title: str,   details: [RichTextBlock](blocks.html#slack_sdk.models.blocks.blocks.RichTextBlock "slack_sdk.models.blocks.blocks.RichTextBlock") | dict | None = None,   output: [RichTextBlock](blocks.html#slack_sdk.models.blocks.blocks.RichTextBlock "slack_sdk.models.blocks.blocks.RichTextBlock") | dict | None = None,   sources: Sequence[[UrlSourceElement](block_elements.html#slack_sdk.models.blocks.block_elements.UrlSourceElement "slack_sdk.models.blocks.block_elements.UrlSourceElement") | dict] | None = None,   status: str,   block_id: str | None = None,   **others: dict)`

Expand source code

```typescript
class TaskCardBlock(Block):
    type = "task_card"

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union(
            {
                "task_id",
                "title",
                "details",
                "output",
                "sources",
                "status",
            }
        )

    def __init__(
        self,
        *,
        task_id: str,
        title: str,
        details: Optional[Union[RichTextBlock, dict]] = None,
        output: Optional[Union[RichTextBlock, dict]] = None,
        sources: Optional[Sequence[Union[UrlSourceElement, dict]]] = None,
        status: str,  # pending, in_progress, complete, error
        block_id: Optional[str] = None,
        **others: dict,
    ):
        """Displays a single task, representing a single action.
        https://docs.slack.dev/reference/block-kit/blocks/task-card-block/

        Args:
            block_id: A string acting as a unique identifier for a block. If not specified, one will be generated.
                Maximum length for this field is 255 characters.
                block_id should be unique for each message and each iteration of a message.
                If a message is updated, use a new block_id.
            task_id (required): ID for the task
            title (required): Title of the task in plain text
            details: Details of the task in the form of a single "rich_text" entity.
            output: Output of the task in the form of a single "rich_text" entity.
            sources: Array of URL source elements used to generate a response.
            status: The state of a task. Either "pending", "in_progress", "complete", or "error".
        """
        super().__init__(type=self.type, block_id=block_id)
        show_unknown_key_warning(self, others)

        self.task_id = task_id
        self.title = title
        self.details = details
        self.output = output
        self.sources = sources
        self.status = status

    @JsonValidator("status must be an expected value (pending, in_progress, complete, or error)")
    def _validate_rows(self):
        return self.status in ["pending", "in_progress", "complete", "error"]
```

Blocks are a series of components that can be combined to create visually rich and compellingly interactive messages. [https://docs.slack.dev/reference/block-kit/blocks](https://docs.slack.dev/reference/block-kit/blocks)

Displays a single task, representing a single action. [https://docs.slack.dev/reference/block-kit/blocks/task-card-block/](https://docs.slack.dev/reference/block-kit/blocks/task-card-block/)

## Args (43)

**`block_id`**

A string acting as a unique identifier for a block. If not specified, one will be generated. Maximum length for this field is 255 characters. block\_id should be unique for each message and each iteration of a message. If a message is updated, use a new block\_id.

**`task_id`** : `required`

ID for the task

**`title`** : `required`

Title of the task in plain text

**`details`**

Details of the task in the form of a single "rich\_text" entity.

**`output`**

Output of the task in the form of a single "rich\_text" entity.

**`sources`**

Array of URL source elements used to generate a response.

**`status`**

The state of a task. Either "pending", "in\_progress", "complete", or "error".

### Ancestors (55)

* [Block](blocks.html#slack_sdk.models.blocks.blocks.Block "slack_sdk.models.blocks.blocks.Block")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (54)

`var type`

The type of the None singleton.

### Instance variables (43)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union(
        {
            "task_id",
            "title",
            "details",
            "output",
            "sources",
            "status",
        }
    )
```

Build an unordered collection of unique elements.

### Inherited members (55)

* `**[Block](blocks.html#slack_sdk.models.blocks.blocks.Block "slack_sdk.models.blocks.blocks.Block")**`:
  * `[block_id_max_length](blocks.html#slack_sdk.models.blocks.blocks.Block.block_id_max_length "slack_sdk.models.blocks.blocks.Block.block_id_max_length")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.blocks.Block.get_non_null_attributes")`
  * `[logger](blocks.html#slack_sdk.models.blocks.blocks.Block.logger "slack_sdk.models.blocks.blocks.Block.logger")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.blocks.Block.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.blocks.Block.validate_json")`

`class TextObject (text: str,   type: str | None = None,   subtype: str | None = None,   emoji: bool | None = None,   **kwargs)`

Expand source code

```typescript
class TextObject(JsonObject):
    """The interface for text objects (types: plain_text, mrkdwn)"""

    attributes = {"text", "type", "emoji"}
    logger = logging.getLogger(__name__)

    def _subtype_warning(self):
        warnings.warn(
            "subtype is deprecated since slackclient 2.6.0, use type instead",
            DeprecationWarning,
        )

    @property
    def subtype(self) -> Optional[str]:
        return self.type

    @classmethod
    def parse(
        cls,
        text: Union[str, Dict[str, Any], "TextObject"],
        default_type: str = "mrkdwn",
    ) -> Optional["TextObject"]:
        if not text:
            return None
        elif isinstance(text, str):
            if default_type == PlainTextObject.type:
                return PlainTextObject.from_str(text)
            else:
                return MarkdownTextObject.from_str(text)
        elif isinstance(text, dict):
            d = copy.copy(text)
            t = d.pop("type")
            if t == PlainTextObject.type:
                return PlainTextObject(**d)
            else:
                return MarkdownTextObject(**d)
        elif isinstance(text, TextObject):
            return text
        else:
            cls.logger.warning(f"Unknown type ({type(text)}) detected when parsing a TextObject")
            return None

    def __init__(
        self,
        text: str,
        type: Optional[str] = None,
        subtype: Optional[str] = None,
        emoji: Optional[bool] = None,
        **kwargs,
    ):
        """Super class for new text "objects" used in Block kit"""
        if subtype:
            self._subtype_warning()

        self.text = text
        self.type = type if type else subtype
        self.emoji = emoji
```

The interface for text objects (types: plain\_text, mrkdwn)

Super class for new text "objects" used in Block kit

### Ancestors (56)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Subclasses (7)

* [MarkdownTextObject](basic_components.html#slack_sdk.models.blocks.basic_components.MarkdownTextObject "slack_sdk.models.blocks.basic_components.MarkdownTextObject")
* [PlainTextObject](basic_components.html#slack_sdk.models.blocks.basic_components.PlainTextObject "slack_sdk.models.blocks.basic_components.PlainTextObject")
* [RawTextObject](basic_components.html#slack_sdk.models.blocks.basic_components.RawTextObject "slack_sdk.models.blocks.basic_components.RawTextObject")

### Class variables (55)

`var attributes`

The type of the None singleton.

`var logger`

The type of the None singleton.

### Static methods (11)

`def parse(text: str | Dict[str, Any] | [TextObject](#slack_sdk.models.blocks.TextObject "slack_sdk.models.blocks.TextObject"),   default_type: str = 'mrkdwn') ‑> [TextObject](basic_components.html#slack_sdk.models.blocks.basic_components.TextObject "slack_sdk.models.blocks.basic_components.TextObject") | None`

### Instance variables (44)

`prop subtype : str | None`

Expand source code

```python
@property
def subtype(self) -> Optional[str]:
    return self.type
```

### Inherited members (56)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class TimePickerElement (*,   action_id: str | None = None,   placeholder: str | dict | [TextObject](basic_components.html#slack_sdk.models.blocks.basic_components.TextObject "slack_sdk.models.blocks.basic_components.TextObject") | None = None,   initial_time: str | None = None,   confirm: dict | [ConfirmObject](basic_components.html#slack_sdk.models.blocks.basic_components.ConfirmObject "slack_sdk.models.blocks.basic_components.ConfirmObject") | None = None,   focus_on_load: bool | None = None,   timezone: str | None = None,   **others: dict)`

Expand source code

```typescript
class TimePickerElement(InputInteractiveElement):
    type = "timepicker"

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union({"initial_time", "timezone"})

    def __init__(
        self,
        *,
        action_id: Optional[str] = None,
        placeholder: Optional[Union[str, dict, TextObject]] = None,
        initial_time: Optional[str] = None,
        confirm: Optional[Union[dict, ConfirmObject]] = None,
        focus_on_load: Optional[bool] = None,
        timezone: Optional[str] = None,
        **others: dict,
    ):
        """
        An element which allows selection of a time of day.
        On desktop clients, this time picker will take the form of a dropdown list
        with free-text entry for precise choices.
        On mobile clients, the time picker will use native time picker UIs.
        https://docs.slack.dev/reference/block-kit/block-elements/time-picker-element

        Args:
            action_id (required): An identifier for the action triggered when a time is selected.
                You can use this when you receive an interaction payload to identify the source of the action.
                Should be unique among all other action_ids in the containing block.
                Maximum length for this field is 255 characters.
            placeholder: A plain_text only text object that defines the placeholder text shown on the timepicker.
                Maximum length for the text in this field is 150 characters.
            initial_time: The initial time that is selected when the element is loaded.
                This should be in the format HH:mm, where HH is the 24-hour format of an hour (00 to 23)
                and mm is minutes with leading zeros (00 to 59), for example 22:25 for 10:25pm.
            confirm: A confirm object that defines an optional confirmation dialog
                that appears after a time is selected.
            focus_on_load: Indicates whether the element will be set to auto focus within the view object.
                Only one element can be set to true. Defaults to false.
            timezone: The timezone to consider for this input value.
        """
        super().__init__(
            type=self.type,
            action_id=action_id,
            placeholder=TextObject.parse(placeholder, PlainTextObject.type),  # type: ignore[arg-type]
            confirm=ConfirmObject.parse(confirm),  # type: ignore[arg-type]
            focus_on_load=focus_on_load,
        )
        show_unknown_key_warning(self, others)

        self.initial_time = initial_time
        self.timezone = timezone

    @JsonValidator("initial_time attribute must be in format 'HH:mm'")
    def _validate_initial_time_valid(self) -> bool:
        return self.initial_time is None or re.match(r"([0-1][0-9]|2[0-3]):([0-5][0-9])", self.initial_time) is not None
```

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

An element which allows selection of a time of day. On desktop clients, this time picker will take the form of a dropdown list with free-text entry for precise choices. On mobile clients, the time picker will use native time picker UIs. [https://docs.slack.dev/reference/block-kit/block-elements/time-picker-element](https://docs.slack.dev/reference/block-kit/block-elements/time-picker-element)

## Args (44)

**`action_id`** : `required`

An identifier for the action triggered when a time is selected. You can use this when you receive an interaction payload to identify the source of the action. Should be unique among all other action\_ids in the containing block. Maximum length for this field is 255 characters.

**`placeholder`**

A plain\_text only text object that defines the placeholder text shown on the timepicker. Maximum length for the text in this field is 150 characters.

**`initial_time`**

The initial time that is selected when the element is loaded. This should be in the format HH:mm, where HH is the 24-hour format of an hour (00 to 23) and mm is minutes with leading zeros (00 to 59), for example 22:25 for 10:25pm.

**`confirm`**

A confirm object that defines an optional confirmation dialog that appears after a time is selected.

**`focus_on_load`**

Indicates whether the element will be set to auto focus within the view object. Only one element can be set to true. Defaults to false.

**`timezone`**

The timezone to consider for this input value.

### Ancestors (57)

* [InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")
* [InteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement "slack_sdk.models.blocks.block_elements.InteractiveElement")
* [BlockElement](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (56)

`var type`

The type of the None singleton.

### Instance variables (45)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union({"initial_time", "timezone"})
```

Build an unordered collection of unique elements.

### Inherited members (57)

* `**[InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")**`:
  * `[action_id_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement.action_id_max_length "slack_sdk.models.blocks.block_elements.InputInteractiveElement.action_id_max_length")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.block_elements.InputInteractiveElement.get_non_null_attributes")`
  * `[logger](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement.logger "slack_sdk.models.blocks.block_elements.InputInteractiveElement.logger")`
  * `[placeholder_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement.placeholder_max_length "slack_sdk.models.blocks.block_elements.InputInteractiveElement.placeholder_max_length")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.block_elements.InputInteractiveElement.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.block_elements.InputInteractiveElement.validate_json")`

`class UrlInputElement (*,   action_id: str | None = None,   initial_value: str | None = None,   dispatch_action_config: dict | [DispatchActionConfig](basic_components.html#slack_sdk.models.blocks.basic_components.DispatchActionConfig "slack_sdk.models.blocks.basic_components.DispatchActionConfig") | None = None,   focus_on_load: bool | None = None,   placeholder: str | dict | [TextObject](basic_components.html#slack_sdk.models.blocks.basic_components.TextObject "slack_sdk.models.blocks.basic_components.TextObject") | None = None,   **others: dict)`

Expand source code

```typescript
class UrlInputElement(InputInteractiveElement):
    type = "url_text_input"

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union(
            {
                "initial_value",
                "dispatch_action_config",
            }
        )

    def __init__(
        self,
        *,
        action_id: Optional[str] = None,
        initial_value: Optional[str] = None,
        dispatch_action_config: Optional[Union[dict, DispatchActionConfig]] = None,
        focus_on_load: Optional[bool] = None,
        placeholder: Optional[Union[str, dict, TextObject]] = None,
        **others: dict,
    ):
        """
        A URL input element, similar to the Plain-text input element,
        creates a single line field where a user can enter URL-encoded data.
        https://docs.slack.dev/reference/block-kit/block-elements/url-input-element

        Args:
            action_id (required): An identifier for the input value when the parent modal is submitted.
                You can use this when you receive a view_submission payload to identify the value of the input element.
                Should be unique among all other action_ids in the containing block.
                Maximum length for this field is 255 characters.
            initial_value: The initial value in the URL input when it is loaded.
            dispatch_action_config: A dispatch configuration object that determines when during text input
                the element returns a block_actions payload.
            focus_on_load: Indicates whether the element will be set to auto focus within the view object.
                Only one element can be set to true. Defaults to false.
            placeholder: A plain_text only text object that defines the placeholder text shown in the URL input.
                Maximum length for the text in this field is 150 characters.
        """
        super().__init__(
            type=self.type,
            action_id=action_id,
            placeholder=TextObject.parse(placeholder, PlainTextObject.type),  # type: ignore[arg-type]
            focus_on_load=focus_on_load,
        )
        show_unknown_key_warning(self, others)

        self.initial_value = initial_value
        self.dispatch_action_config = dispatch_action_config
```

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

A URL input element, similar to the Plain-text input element, creates a single line field where a user can enter URL-encoded data. [https://docs.slack.dev/reference/block-kit/block-elements/url-input-element](https://docs.slack.dev/reference/block-kit/block-elements/url-input-element)

## Args (45)

**`action_id`** : `required`

An identifier for the input value when the parent modal is submitted. You can use this when you receive a view\_submission payload to identify the value of the input element. Should be unique among all other action\_ids in the containing block. Maximum length for this field is 255 characters.

**`initial_value`**

The initial value in the URL input when it is loaded.

**`dispatch_action_config`**

A dispatch configuration object that determines when during text input the element returns a block\_actions payload.

**`focus_on_load`**

Indicates whether the element will be set to auto focus within the view object. Only one element can be set to true. Defaults to false.

**`placeholder`**

A plain\_text only text object that defines the placeholder text shown in the URL input. Maximum length for the text in this field is 150 characters.

### Ancestors (58)

* [InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")
* [InteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement "slack_sdk.models.blocks.block_elements.InteractiveElement")
* [BlockElement](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (57)

`var type`

The type of the None singleton.

### Instance variables (46)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union(
        {
            "initial_value",
            "dispatch_action_config",
        }
    )
```

Build an unordered collection of unique elements.

### Inherited members (58)

* `**[InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")**`:
  * `[action_id_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement.action_id_max_length "slack_sdk.models.blocks.block_elements.InputInteractiveElement.action_id_max_length")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.block_elements.InputInteractiveElement.get_non_null_attributes")`
  * `[logger](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement.logger "slack_sdk.models.blocks.block_elements.InputInteractiveElement.logger")`
  * `[placeholder_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement.placeholder_max_length "slack_sdk.models.blocks.block_elements.InputInteractiveElement.placeholder_max_length")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.block_elements.InputInteractiveElement.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.block_elements.InputInteractiveElement.validate_json")`

`class UrlSourceElement (*, url: str, text: str, **others: Dict)`

Expand source code

```typescript
class UrlSourceElement(BlockElement):
    type = "url"

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union(
            {
                "url",
                "text",
            }
        )

    def __init__(
        self,
        *,
        url: str,
        text: str,
        **others: Dict,
    ):
        """
        A URL source element that displays a URL source for referencing within a task card block.
        https://docs.slack.dev/reference/block-kit/block-elements/url-source-element

        Args:
            url (required): The URL type source.
            text (required): Display text for the URL.
        """
        super().__init__(type=self.type)
        show_unknown_key_warning(self, others)
        self.url = url
        self.text = text
```

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

A URL source element that displays a URL source for referencing within a task card block. [https://docs.slack.dev/reference/block-kit/block-elements/url-source-element](https://docs.slack.dev/reference/block-kit/block-elements/url-source-element)

## Args (46)

**`url`** : `required`

The URL type source.

**`text`** : `required`

Display text for the URL.

### Ancestors (59)

* [BlockElement](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (58)

`var type`

The type of the None singleton.

### Instance variables (47)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union(
        {
            "url",
            "text",
        }
    )
```

Build an unordered collection of unique elements.

### Inherited members (59)

* `**[BlockElement](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.block_elements.BlockElement.get_non_null_attributes")`
  * `[logger](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement.logger "slack_sdk.models.blocks.block_elements.BlockElement.logger")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.block_elements.BlockElement.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.block_elements.BlockElement.validate_json")`

`class UserMultiSelectElement (*,   action_id: str | None = None,   placeholder: str | dict | [TextObject](basic_components.html#slack_sdk.models.blocks.basic_components.TextObject "slack_sdk.models.blocks.basic_components.TextObject") | None = None,   initial_users: Sequence[str] | None = None,   confirm: dict | [ConfirmObject](basic_components.html#slack_sdk.models.blocks.basic_components.ConfirmObject "slack_sdk.models.blocks.basic_components.ConfirmObject") | None = None,   max_selected_items: int | None = None,   focus_on_load: bool | None = None,   **others: dict)`

Expand source code

```typescript
class UserMultiSelectElement(InputInteractiveElement):
    type = "multi_users_select"

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union({"initial_users", "max_selected_items"})

    def __init__(
        self,
        *,
        action_id: Optional[str] = None,
        placeholder: Optional[Union[str, dict, TextObject]] = None,
        initial_users: Optional[Sequence[str]] = None,
        confirm: Optional[Union[dict, ConfirmObject]] = None,
        max_selected_items: Optional[int] = None,
        focus_on_load: Optional[bool] = None,
        **others: dict,
    ):
        """
        This select menu will populate its options with a list of Slack users visible to
        the current user in the active workspace.
        https://docs.slack.dev/reference/block-kit/block-elements/multi-select-menu-element#users_multi_select

        Args:
            action_id (required): An identifier for the action triggered when a menu option is selected.
                You can use this when you receive an interaction payload to identify the source of the action.
                Should be unique among all other action_ids in the containing block.
                Maximum length for this field is 255 characters.
            placeholder (required): A plain_text only text object that defines the placeholder text shown on the menu.
                Maximum length for the text in this field is 150 characters.
            initial_users: An array of user IDs of any valid users to be pre-selected when the menu loads.
            confirm: A confirm object that defines an optional confirmation dialog that appears
                before the multi-select choices are submitted.
            max_selected_items: Specifies the maximum number of items that can be selected in the menu.
                Minimum number is 1.
            focus_on_load: Indicates whether the element will be set to auto focus within the view object.
                Only one element can be set to true. Defaults to false.
        """
        super().__init__(
            type=self.type,
            action_id=action_id,
            placeholder=TextObject.parse(placeholder, PlainTextObject.type),  # type: ignore[arg-type]
            confirm=ConfirmObject.parse(confirm),  # type: ignore[arg-type]
            focus_on_load=focus_on_load,
        )
        show_unknown_key_warning(self, others)

        self.initial_users = initial_users
        self.max_selected_items = max_selected_items
```

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

This select menu will populate its options with a list of Slack users visible to the current user in the active workspace. [https://docs.slack.dev/reference/block-kit/block-elements/multi-select-menu-element#users\_multi\_select](https://docs.slack.dev/reference/block-kit/block-elements/multi-select-menu-element#users_multi_select)

## Args (47)

**`action_id`** : `required`

An identifier for the action triggered when a menu option is selected. You can use this when you receive an interaction payload to identify the source of the action. Should be unique among all other action\_ids in the containing block. Maximum length for this field is 255 characters.

**`placeholder`** : `required`

A plain\_text only text object that defines the placeholder text shown on the menu. Maximum length for the text in this field is 150 characters.

**`initial_users`**

An array of user IDs of any valid users to be pre-selected when the menu loads.

**`confirm`**

A confirm object that defines an optional confirmation dialog that appears before the multi-select choices are submitted.

**`max_selected_items`**

Specifies the maximum number of items that can be selected in the menu. Minimum number is 1.

**`focus_on_load`**

Indicates whether the element will be set to auto focus within the view object. Only one element can be set to true. Defaults to false.

### Ancestors (60)

* [InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")
* [InteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement "slack_sdk.models.blocks.block_elements.InteractiveElement")
* [BlockElement](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (59)

`var type`

The type of the None singleton.

### Instance variables (48)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union({"initial_users", "max_selected_items"})
```

Build an unordered collection of unique elements.

### Inherited members (60)

* `**[InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")**`:
  * `[action_id_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement.action_id_max_length "slack_sdk.models.blocks.block_elements.InputInteractiveElement.action_id_max_length")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.block_elements.InputInteractiveElement.get_non_null_attributes")`
  * `[logger](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement.logger "slack_sdk.models.blocks.block_elements.InputInteractiveElement.logger")`
  * `[placeholder_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement.placeholder_max_length "slack_sdk.models.blocks.block_elements.InputInteractiveElement.placeholder_max_length")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.block_elements.InputInteractiveElement.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.block_elements.InputInteractiveElement.validate_json")`

`class UserSelectElement (*,   placeholder: str | dict | [TextObject](basic_components.html#slack_sdk.models.blocks.basic_components.TextObject "slack_sdk.models.blocks.basic_components.TextObject") | None = None,   action_id: str | None = None,   initial_user: str | None = None,   confirm: dict | [ConfirmObject](basic_components.html#slack_sdk.models.blocks.basic_components.ConfirmObject "slack_sdk.models.blocks.basic_components.ConfirmObject") | None = None,   focus_on_load: bool | None = None,   **others: dict)`

Expand source code

```typescript
class UserSelectElement(InputInteractiveElement):
    type = "users_select"

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union({"initial_user"})

    def __init__(
        self,
        *,
        placeholder: Optional[Union[str, dict, TextObject]] = None,
        action_id: Optional[str] = None,
        initial_user: Optional[str] = None,
        confirm: Optional[Union[dict, ConfirmObject]] = None,
        focus_on_load: Optional[bool] = None,
        **others: dict,
    ):
        """
        This select menu will populate its options with a list of Slack users visible to
        the current user in the active workspace.
        https://docs.slack.dev/reference/block-kit/block-elements/select-menu-element#users_select

        Args:
            placeholder (required): A plain_text only text object that defines the placeholder text shown on the menu.
                Maximum length for the text in this field is 150 characters.
            action_id (required): An identifier for the action triggered when a menu option is selected.
                You can use this when you receive an interaction payload to identify the source of the action.
                Should be unique among all other action_ids in the containing block.
                Maximum length for this field is 255 characters.
            initial_user: The user ID of any valid user to be pre-selected when the menu loads.
            confirm: A confirm object that defines an optional confirmation dialog
                that appears after a menu item is selected.
            focus_on_load: Indicates whether the element will be set to auto focus within the view object.
                Only one element can be set to true. Defaults to false.
        """
        super().__init__(
            type=self.type,
            action_id=action_id,
            placeholder=TextObject.parse(placeholder, PlainTextObject.type),  # type: ignore[arg-type]
            confirm=ConfirmObject.parse(confirm),  # type: ignore[arg-type]
            focus_on_load=focus_on_load,
        )
        show_unknown_key_warning(self, others)

        self.initial_user = initial_user
```

Block Elements are things that exists inside of your Blocks. [https://docs.slack.dev/reference/block-kit/block-elements/](https://docs.slack.dev/reference/block-kit/block-elements/)

This select menu will populate its options with a list of Slack users visible to the current user in the active workspace. [https://docs.slack.dev/reference/block-kit/block-elements/select-menu-element#users\_select](https://docs.slack.dev/reference/block-kit/block-elements/select-menu-element#users_select)

## Args (48)

**`placeholder`** : `required`

A plain\_text only text object that defines the placeholder text shown on the menu. Maximum length for the text in this field is 150 characters.

**`action_id`** : `required`

An identifier for the action triggered when a menu option is selected. You can use this when you receive an interaction payload to identify the source of the action. Should be unique among all other action\_ids in the containing block. Maximum length for this field is 255 characters.

**`initial_user`**

The user ID of any valid user to be pre-selected when the menu loads.

**`confirm`**

A confirm object that defines an optional confirmation dialog that appears after a menu item is selected.

**`focus_on_load`**

Indicates whether the element will be set to auto focus within the view object. Only one element can be set to true. Defaults to false.

### Ancestors (61)

* [InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")
* [InteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement "slack_sdk.models.blocks.block_elements.InteractiveElement")
* [BlockElement](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement "slack_sdk.models.blocks.block_elements.BlockElement")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (60)

`var type`

The type of the None singleton.

### Instance variables (49)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union({"initial_user"})
```

Build an unordered collection of unique elements.

### Inherited members (61)

* `**[InputInteractiveElement](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement "slack_sdk.models.blocks.block_elements.InputInteractiveElement")**`:
  * `[action_id_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InteractiveElement.action_id_max_length "slack_sdk.models.blocks.block_elements.InputInteractiveElement.action_id_max_length")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.block_elements.InputInteractiveElement.get_non_null_attributes")`
  * `[logger](block_elements.html#slack_sdk.models.blocks.block_elements.BlockElement.logger "slack_sdk.models.blocks.block_elements.InputInteractiveElement.logger")`
  * `[placeholder_max_length](block_elements.html#slack_sdk.models.blocks.block_elements.InputInteractiveElement.placeholder_max_length "slack_sdk.models.blocks.block_elements.InputInteractiveElement.placeholder_max_length")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.block_elements.InputInteractiveElement.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.block_elements.InputInteractiveElement.validate_json")`

`class VideoBlock (*,   block_id: str | None = None,   alt_text: str | None = None,   video_url: str | None = None,   thumbnail_url: str | None = None,   title: str | dict | [PlainTextObject](basic_components.html#slack_sdk.models.blocks.basic_components.PlainTextObject "slack_sdk.models.blocks.basic_components.PlainTextObject") | None = None,   title_url: str | None = None,   description: str | dict | [PlainTextObject](basic_components.html#slack_sdk.models.blocks.basic_components.PlainTextObject "slack_sdk.models.blocks.basic_components.PlainTextObject") | None = None,   provider_icon_url: str | None = None,   provider_name: str | None = None,   author_name: str | None = None,   **others: dict)`

Expand source code

```typescript
class VideoBlock(Block):
    type = "video"
    title_max_length = 200
    author_name_max_length = 50

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union(
            {
                "alt_text",
                "video_url",
                "thumbnail_url",
                "title",
                "title_url",
                "description",
                "provider_icon_url",
                "provider_name",
                "author_name",
            }
        )

    def __init__(
        self,
        *,
        block_id: Optional[str] = None,
        alt_text: Optional[str] = None,
        video_url: Optional[str] = None,
        thumbnail_url: Optional[str] = None,
        title: Optional[Union[str, dict, PlainTextObject]] = None,
        title_url: Optional[str] = None,
        description: Optional[Union[str, dict, PlainTextObject]] = None,
        provider_icon_url: Optional[str] = None,
        provider_name: Optional[str] = None,
        author_name: Optional[str] = None,
        **others: dict,
    ):
        """A video block is designed to embed videos in all app surfaces
        (e.g. link unfurls, messages, modals, App Home) —
        anywhere you can put blocks! To use the video block within your app,
        you must have the links.embed:write scope.
        https://docs.slack.dev/reference/block-kit/blocks/video-block

        Args:
            block_id: A string acting as a unique identifier for a block. If not specified, one will be generated.
                Maximum length for this field is 255 characters.
                block_id should be unique for each message and each iteration of a message.
                If a message is updated, use a new block_id.
            alt_text (required): A tooltip for the video. Required for accessibility
            video_url (required): The URL to be embedded. Must match any existing unfurl domains within the app
                and point to a HTTPS URL.
            thumbnail_url (required): The thumbnail image URL
            title (required): Video title in plain text format. Must be less than 200 characters.
            title_url: Hyperlink for the title text. Must correspond to the non-embeddable URL for the video.
                Must go to an HTTPS URL.
            description: Description for video in plain text format.
            provider_icon_url: Icon for the video provider - ex. Youtube icon
            provider_name: The originating application or domain of the video ex. Youtube
            author_name: Author name to be displayed. Must be less than 50 characters.
        """
        super().__init__(type=self.type, block_id=block_id)
        show_unknown_key_warning(self, others)

        self.alt_text = alt_text
        self.video_url = video_url
        self.thumbnail_url = thumbnail_url
        self.title = TextObject.parse(title, default_type=PlainTextObject.type)  # type: ignore[arg-type]
        self.title_url = title_url
        self.description = TextObject.parse(description, default_type=PlainTextObject.type)  # type: ignore[arg-type]
        self.provider_icon_url = provider_icon_url
        self.provider_name = provider_name
        self.author_name = author_name

    @JsonValidator("alt_text attribute must be specified")
    def _validate_alt_text(self):
        return self.alt_text is not None

    @JsonValidator("video_url attribute must be specified")
    def _validate_video_url(self):
        return self.video_url is not None

    @JsonValidator("thumbnail_url attribute must be specified")
    def _validate_thumbnail_url(self):
        return self.thumbnail_url is not None

    @JsonValidator("title attribute must be specified")
    def _validate_title(self):
        return self.title is not None

    @JsonValidator(f"title attribute cannot exceed {title_max_length} characters")
    def _validate_title_length(self):
        return self.title is None or len(self.title.text) < self.title_max_length

    @JsonValidator(f"author_name attribute cannot exceed {author_name_max_length} characters")
    def _validate_author_name_length(self):
        return self.author_name is None or len(self.author_name) < self.author_name_max_length
```

Blocks are a series of components that can be combined to create visually rich and compellingly interactive messages. [https://docs.slack.dev/reference/block-kit/blocks](https://docs.slack.dev/reference/block-kit/blocks)

A video block is designed to embed videos in all app surfaces (e.g. link unfurls, messages, modals, App Home) — anywhere you can put blocks! To use the video block within your app, you must have the links.embed:write scope. [https://docs.slack.dev/reference/block-kit/blocks/video-block](https://docs.slack.dev/reference/block-kit/blocks/video-block)

## Args (49)

**`block_id`**

A string acting as a unique identifier for a block. If not specified, one will be generated. Maximum length for this field is 255 characters. block\_id should be unique for each message and each iteration of a message. If a message is updated, use a new block\_id.

**`alt_text`** : `required`

A tooltip for the video. Required for accessibility

**`video_url`** : `required`

The URL to be embedded. Must match any existing unfurl domains within the app and point to a HTTPS URL.

**`thumbnail_url`** : `required`

The thumbnail image URL

**`title`** : `required`

Video title in plain text format. Must be less than 200 characters.

**`title_url`**

Hyperlink for the title text. Must correspond to the non-embeddable URL for the video. Must go to an HTTPS URL.

**`description`**

Description for video in plain text format.

**`provider_icon_url`**

Icon for the video provider - ex. Youtube icon

**`provider_name`**

The originating application or domain of the video ex. Youtube

**`author_name`**

Author name to be displayed. Must be less than 50 characters.

### Ancestors (62)

* [Block](blocks.html#slack_sdk.models.blocks.blocks.Block "slack_sdk.models.blocks.blocks.Block")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (61)

`var author_name_max_length`

The type of the None singleton.

`var title_max_length`

The type of the None singleton.

`var type`

The type of the None singleton.

### Instance variables (50)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union(
        {
            "alt_text",
            "video_url",
            "thumbnail_url",
            "title",
            "title_url",
            "description",
            "provider_icon_url",
            "provider_name",
            "author_name",
        }
    )
```

Build an unordered collection of unique elements.

### Inherited members (62)

* `**[Block](blocks.html#slack_sdk.models.blocks.blocks.Block "slack_sdk.models.blocks.blocks.Block")**`:
  * `[block_id_max_length](blocks.html#slack_sdk.models.blocks.blocks.Block.block_id_max_length "slack_sdk.models.blocks.blocks.Block.block_id_max_length")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.blocks.blocks.Block.get_non_null_attributes")`
  * `[logger](blocks.html#slack_sdk.models.blocks.blocks.Block.logger "slack_sdk.models.blocks.blocks.Block.logger")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.blocks.blocks.Block.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.blocks.blocks.Block.validate_json")`
