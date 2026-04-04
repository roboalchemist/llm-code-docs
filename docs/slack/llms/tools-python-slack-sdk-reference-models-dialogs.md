Source: https://docs.slack.dev/tools/python-slack-sdk/reference/models/dialogs

# Module slack_sdk.models.dialogs

## Classes

`class AbstractDialogSelector (*,   name: str,   label: str,   optional: bool = False,   value: [Option](../blocks/basic_components.html#slack_sdk.models.blocks.basic_components.Option "slack_sdk.models.blocks.basic_components.Option") | str | None = None,   placeholder: str | None = None)`

Expand source code

```typescript
class AbstractDialogSelector(JsonObject, metaclass=ABCMeta):
    DataSourceTypes = DynamicSelectElementTypes.union({"external", "static"})

    attributes = {"data_source", "label", "name", "optional", "placeholder", "type"}

    name_max_length = 300
    label_max_length = 48
    placeholder_max_length = 150

    @property
    @abstractmethod
    def data_source(self) -> str:
        pass

    def __init__(
        self,
        *,
        name: str,
        label: str,
        optional: bool = False,
        value: Optional[Union[Option, str]] = None,
        placeholder: Optional[str] = None,
    ):
        self.name = name
        self.label = label
        self.optional = optional
        self.value = value
        self.placeholder = placeholder
        self.type = "select"

    @JsonValidator(f"name attribute cannot exceed {name_max_length} characters")
    def name_length(self) -> bool:
        return len(self.name) < self.name_max_length

    @JsonValidator(f"label attribute cannot exceed {label_max_length} characters")
    def label_length(self) -> bool:
        return len(self.label) < self.label_max_length

    @JsonValidator(f"placeholder attribute cannot exceed {placeholder_max_length} characters")
    def placeholder_length(self) -> bool:
        return self.placeholder is None or len(self.placeholder) < self.placeholder_max_length

    @EnumValidator("data_source", DataSourceTypes)
    def data_source_valid(self) -> bool:
        return self.data_source in self.DataSourceTypes

    def to_dict(self) -> dict:
        json = super().to_dict()
        if self.data_source == "external":
            if isinstance(self.value, Option):
                json["selected_options"] = extract_json([self.value], "dialog")
            elif self.value is not None:
                json["selected_options"] = Option.from_single_value(self.value)
        else:
            if isinstance(self.value, Option):
                json["value"] = self.value.value
            elif self.value is not None:
                json["value"] = self.value
        return json
```

The base class for JSON serializable class objects

### Ancestors

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Subclasses

* [DialogChannelSelector](#slack_sdk.models.dialogs.DialogChannelSelector "slack_sdk.models.dialogs.DialogChannelSelector")
* [DialogConversationSelector](#slack_sdk.models.dialogs.DialogConversationSelector "slack_sdk.models.dialogs.DialogConversationSelector")
* [DialogExternalSelector](#slack_sdk.models.dialogs.DialogExternalSelector "slack_sdk.models.dialogs.DialogExternalSelector")
* [DialogStaticSelector](#slack_sdk.models.dialogs.DialogStaticSelector "slack_sdk.models.dialogs.DialogStaticSelector")
* [DialogUserSelector](#slack_sdk.models.dialogs.DialogUserSelector "slack_sdk.models.dialogs.DialogUserSelector")

### Class variables

`var DataSourceTypes`

The type of the None singleton.

`var attributes`

The type of the None singleton.

`var label_max_length`

The type of the None singleton.

`var name_max_length`

The type of the None singleton.

`var placeholder_max_length`

The type of the None singleton.

### Instance variables

`prop data_source : str`

Expand source code

```python
@property
@abstractmethod
def data_source(self) -> str:
    pass
```

### Methods

`def data_source_valid(self) ‑> bool`

Expand source code

```python
@EnumValidator("data_source", DataSourceTypes)
def data_source_valid(self) -> bool:
    return self.data_source in self.DataSourceTypes
```

`def label_length(self) ‑> bool`

Expand source code

```python
@JsonValidator(f"label attribute cannot exceed {label_max_length} characters")
def label_length(self) -> bool:
    return len(self.label) < self.label_max_length
```

`def name_length(self) ‑> bool`

Expand source code

```python
@JsonValidator(f"name attribute cannot exceed {name_max_length} characters")
def name_length(self) -> bool:
    return len(self.name) < self.name_max_length
```

`def placeholder_length(self) ‑> bool`

Expand source code

```python
@JsonValidator(f"placeholder attribute cannot exceed {placeholder_max_length} characters")
def placeholder_length(self) -> bool:
    return self.placeholder is None or len(self.placeholder) < self.placeholder_max_length
```

### Inherited members

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class DialogBuilder`

Expand source code

```typescript
class DialogBuilder(JsonObject):
    attributes: Set[str] = set()

    _callback_id: Optional[str]
    _elements: List[Union[DialogTextComponent, AbstractDialogSelector]]
    _submit_label: Optional[str]
    _notify_on_cancel: bool
    _state: Optional[str]

    title_max_length = 24
    submit_label_max_length = 24
    elements_max_length = 10
    state_max_length = 3000

    def __init__(self):
        """
        Create a DialogBuilder to more easily construct the JSON required to submit a
        dialog to Slack
        """
        self._title = None
        self._callback_id = None
        self._elements = []
        self._submit_label = None
        self._notify_on_cancel = False
        self._state = None

    def title(self, title: str) -> "DialogBuilder":
        """
        Specify a title for this dialog

        Args:
          title: must not exceed 24 characters
        """
        self._title = title
        return self

    def state(self, state: Union[dict, str]) -> "DialogBuilder":
        """
        Pass state into this dialog - dictionaries will be automatically formatted to
        JSON

        Args:
            state: Extra state information that you need to pass from this dialog
                back to your application on submission
        """
        if isinstance(state, dict):
            self._state = dumps(state)
        else:
            self._state = state
        return self

    def callback_id(self, callback_id: str) -> "DialogBuilder":
        """
        Specify a callback ID for this dialog, which your application will then
        receive upon dialog submission

        Args:
          callback_id: a string identifying this particular dialog
        """
        self._callback_id = callback_id
        return self

    def submit_label(self, label: str) -> "DialogBuilder":
        """
        The label to use on the 'Submit' button on the dialog. Defaults to 'Submit'
        if not specified.

        Args:
            label: must not exceed 24 characters, and must be a single word (no
                spaces)
        """
        self._submit_label = label
        return self

    def notify_on_cancel(self, notify: bool) -> "DialogBuilder":
        """
        Whether this dialog should send a request to your application even if the
        user cancels their interaction. Defaults to False.

        Args:
            notify: Set to True to indicate that your application should receive a
                request even if the user cancels interaction with the dialog.
        """
        self._notify_on_cancel = notify
        return self

    def text_field(
        self,
        *,
        name: str,
        label: str,
        optional: bool = False,
        placeholder: Optional[str] = None,
        hint: Optional[str] = None,
        value: Optional[str] = None,
        min_length: int = 0,
        max_length: int = 150,
        subtype: Optional[str] = None,
    ) -> "DialogBuilder":
        """
        Text elements are single-line plain text fields.

        https://docs.slack.dev/legacy/legacy-dialogs/#attributes_text_elements

        Args:
            name: Name of form element. Required. No more than 300 characters.
            label: Label displayed to user. Required. 48 character maximum.
            optional: Provide true when the form element is not required. By
                default, form elements are required.
            placeholder: A string displayed as needed to help guide users in
                completing the element. 150 character maximum.
            hint: Helpful text provided to assist users in answering a question.
                Up to 150 characters.
            value: A default value for this field. Up to 150 characters.
            min_length: Minimum input length allowed for element. Up to 150
                characters. Defaults to 0.
            max_length: Maximum input length allowed for element. Up to 150
                characters. Defaults to 150.
            subtype: A subtype for this text input. Accepts email, number, tel,
                    or url. In some form factors, optimized input is provided for this
                    subtype.
        """
        self._elements.append(
            DialogTextField(
                name=name,
                label=label,
                optional=optional,
                placeholder=placeholder,
                hint=hint,
                value=value,
                min_length=min_length,
                max_length=max_length,
                subtype=subtype,
            )
        )
        return self

    def text_area(
        self,
        *,
        name: str,
        label: str,
        optional: bool = False,
        placeholder: Optional[str] = None,
        hint: Optional[str] = None,
        value: Optional[str] = None,
        min_length: int = 0,
        max_length: int = 3000,
        subtype: Optional[str] = None,
    ) -> "DialogBuilder":
        """
        A textarea is a multi-line plain text editing control. You've likely
        encountered these on the world wide web. Use this element if you want a
        relatively long answer from users. The element UI provides a remaining
        character count to the max_length you have set or the default,
        3000.

        https://docs.slack.dev/legacy/legacy-dialogs/#attributes_textarea_elements

        Args:
            name: Name of form element. Required. No more than 300 characters.
            label: Label displayed to user. Required. 48 character maximum.
            optional: Provide true when the form element is not required. By
                default, form elements are required.
            placeholder: A string displayed as needed to help guide users in
                completing the element. 150 character maximum.
            hint: Helpful text provided to assist users in answering a question.
                Up to 150 characters.
            value: A default value for this field. Up to 3000 characters.
            min_length: Minimum input length allowed for element. 1-3000
                characters. Defaults to 0.
            max_length: Maximum input length allowed for element. 0-3000
                characters. Defaults to 3000.
            subtype: A subtype for this text input. Accepts email, number, tel,
                or url. In some form factors, optimized input is provided for this
                subtype.
        """
        self._elements.append(
            DialogTextArea(
                name=name,
                label=label,
                optional=optional,
                placeholder=placeholder,
                hint=hint,
                value=value,
                min_length=min_length,
                max_length=max_length,
                subtype=subtype,
            )
        )
        return self

    def static_selector(
        self,
        *,
        name: str,
        label: str,
        options: Union[Sequence[Option], Sequence[OptionGroup]],
        optional: bool = False,
        value: Optional[str] = None,
        placeholder: Optional[str] = None,
    ) -> "DialogBuilder":
        """
        Use the select element for multiple choice selections allowing users to pick
        a single item from a list. True to web roots, this selection is displayed as
        a dropdown menu.

        A select element may contain up to 100 selections, provided as a list of
        Option or OptionGroup objects

        https://docs.slack.dev/legacy/legacy-dialogs/#attributes_select_elements

        Args:
            name: Name of form element. Required. No more than 300 characters.
            label: Label displayed to user. Required. No more than 48 characters.
            options: A list of up to 100 Option or OptionGroup objects. Object
                types cannot be mixed.
            optional: Provide true when the form element is not required. By
                default, form elements are required.
            value: Provide a default selected value.
            placeholder: A string displayed as needed to help guide users in
                completing the element. 150 character maximum.
        """
        self._elements.append(
            DialogStaticSelector(
                name=name,
                label=label,
                options=options,
                optional=optional,
                value=value,
                placeholder=placeholder,
            )
        )
        return self

    def external_selector(
        self,
        *,
        name: str,
        label: str,
        optional: bool = False,
        value: Optional[Option] = None,
        placeholder: Optional[str] = None,
        min_query_length: Optional[int] = None,
    ) -> "DialogBuilder":
        """
        Use the select element for multiple choice selections allowing users to pick
        a single item from a list. True to web roots, this selection is displayed as
        a dropdown menu.

        A list of options can be loaded from an external URL and used in your dialog
        menus.

        https://docs.slack.dev/legacy/legacy-dialogs/#dynamic_select_elements_external

        Args:
            name: Name of form element. Required. No more than 300 characters.
            label: Label displayed to user. Required. No more than 48 characters.
            min_query_length: Specify the number of characters that must be
                typed by a user into a dynamic select menu before dispatching to your
                application.
            optional: Provide true when the form element is not required. By
                default, form elements are required.
            value: Provide a default selected value. This should be a single
                Option or OptionGroup that exactly matches one that will be returned
                from your external endpoint.
            placeholder: A string displayed as needed to help guide users in
                completing the element. 150 character maximum.
        """
        self._elements.append(
            DialogExternalSelector(
                name=name,
                label=label,
                optional=optional,
                value=value,
                placeholder=placeholder,
                min_query_length=min_query_length,
            )
        )
        return self

    def user_selector(
        self,
        *,
        name: str,
        label: str,
        optional: bool = False,
        value: Optional[str] = None,
        placeholder: Optional[str] = None,
    ) -> "DialogBuilder":
        """
        Now you can easily populate a select menu with a list of users. For example,
        when you are creating a bug tracking app, you want to include a field for an
        assignee. Slack pre-populates the user list in client-side, so your app
        doesn't need access to a related OAuth scope.

        https://docs.slack.dev/legacy/legacy-dialogs/#dynamic_select_elements_users

        Args:
            name: Name of form element. Required. No more than 300 characters.
            label: Label displayed to user. Required. No more than 48 characters.
            optional: Provide true when the form element is not required. By
                default, form elements are required.
            value: Provide a default selected value.
            placeholder: A string displayed as needed to help guide users in
                completing the element. 150 character maximum.
        """
        self._elements.append(
            DialogUserSelector(
                name=name,
                label=label,
                optional=optional,
                value=value,
                placeholder=placeholder,
            )
        )
        return self

    def channel_selector(
        self,
        *,
        name: str,
        label: str,
        optional: bool = False,
        value: Optional[str] = None,
        placeholder: Optional[str] = None,
    ) -> "DialogBuilder":
        """
        You can also provide a select menu with a list of channels. Specify your
        data_source as channels to limit only to public channels

        https://docs.slack.dev/legacy/legacy-dialogs/#dynamic_select_elements_channels_conversations

        Args:
            name: Name of form element. Required. No more than 300 characters.
            label: Label displayed to user. Required. No more than 48 characters.
            optional: Provide true when the form element is not required. By
                default, form elements are required.
            value: Provide a default selected value.
            placeholder: A string displayed as needed to help guide users in
                completing the element. 150 character maximum.
        """
        self._elements.append(
            DialogChannelSelector(
                name=name,
                label=label,
                optional=optional,
                value=value,
                placeholder=placeholder,
            )
        )
        return self

    def conversation_selector(
        self,
        *,
        name: str,
        label: str,
        optional: bool = False,
        value: Optional[str] = None,
        placeholder: Optional[str] = None,
    ) -> "DialogBuilder":
        """
        You can also provide a select menu with a list of conversations - including
        private channels, direct messages, MPIMs, and whatever else we consider a
        conversation-like thing.

        https://docs.slack.dev/legacy/legacy-dialogs/#dynamic_select_elements_channels_conversations

        Args:
            name: Name of form element. Required. No more than 300 characters.
            label: Label displayed to user. Required. No more than 48 characters.
            optional: Provide true when the form element is not required. By
                default, form elements are required.
            value: Provide a default selected value.
            placeholder: A string displayed as needed to help guide users in
                completing the element. 150 character maximum.
        """
        self._elements.append(
            DialogConversationSelector(
                name=name,
                label=label,
                optional=optional,
                value=value,
                placeholder=placeholder,
            )
        )
        return self

    @JsonValidator("title attribute is required")
    def title_present(self) -> bool:
        return self._title is not None

    @JsonValidator(f"title attribute cannot exceed {title_max_length} characters")
    def title_length(self) -> bool:
        return self._title is not None and len(self._title) <= self.title_max_length

    @JsonValidator("callback_id attribute is required")
    def callback_id_present(self) -> bool:
        return self._callback_id is not None

    @JsonValidator(f"dialogs must contain between 1 and {elements_max_length} elements")
    def elements_length(self) -> bool:
        return 0 < len(self._elements) <= self.elements_max_length

    @JsonValidator(f"submit_label cannot exceed {submit_label_max_length} characters")
    def submit_label_length(self) -> bool:
        return self._submit_label is None or len(self._submit_label) <= self.submit_label_max_length

    @JsonValidator("submit_label can only be one word")
    def submit_label_valid(self) -> bool:
        return self._submit_label is None or " " not in self._submit_label

    @JsonValidator(f"state cannot exceed {state_max_length} characters")
    def state_length(self) -> bool:
        return not self._state or len(self._state) <= self.state_max_length

    def to_dict(self) -> dict:
        self.validate_json()
        json = {
            "title": self._title,
            "callback_id": self._callback_id,
            "elements": extract_json(self._elements),
            "notify_on_cancel": self._notify_on_cancel,
        }
        if self._submit_label is not None:
            json["submit_label"] = self._submit_label
        if self._state is not None:
            json["state"] = self._state
        return json
```

The base class for JSON serializable class objects

Create a DialogBuilder to more easily construct the JSON required to submit a dialog to Slack

### Ancestors (2)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (2)

`var attributes : Set[str]`

The type of the None singleton.

`var elements_max_length`

The type of the None singleton.

`var state_max_length`

The type of the None singleton.

`var submit_label_max_length`

The type of the None singleton.

`var title_max_length`

The type of the None singleton.

### Methods (2)

`def callback_id(self, callback_id: str) ‑> [DialogBuilder](#slack_sdk.models.dialogs.DialogBuilder "slack_sdk.models.dialogs.DialogBuilder")`

Expand source code

```typescript
def callback_id(self, callback_id: str) -> "DialogBuilder":
    """
    Specify a callback ID for this dialog, which your application will then
    receive upon dialog submission

    Args:
      callback_id: a string identifying this particular dialog
    """
    self._callback_id = callback_id
    return self
```

Specify a callback ID for this dialog, which your application will then receive upon dialog submission

## Args

**`callback_id`**

a string identifying this particular dialog

`def callback_id_present(self) ‑> bool`

Expand source code

```python
@JsonValidator("callback_id attribute is required")
def callback_id_present(self) -> bool:
    return self._callback_id is not None
```

`def channel_selector(self,   *,   name: str,   label: str,   optional: bool = False,   value: str | None = None,   placeholder: str | None = None) ‑> [DialogBuilder](#slack_sdk.models.dialogs.DialogBuilder "slack_sdk.models.dialogs.DialogBuilder")`

Expand source code

```typescript
def channel_selector(
    self,
    *,
    name: str,
    label: str,
    optional: bool = False,
    value: Optional[str] = None,
    placeholder: Optional[str] = None,
) -> "DialogBuilder":
    """
    You can also provide a select menu with a list of channels. Specify your
    data_source as channels to limit only to public channels

    https://docs.slack.dev/legacy/legacy-dialogs/#dynamic_select_elements_channels_conversations

    Args:
        name: Name of form element. Required. No more than 300 characters.
        label: Label displayed to user. Required. No more than 48 characters.
        optional: Provide true when the form element is not required. By
            default, form elements are required.
        value: Provide a default selected value.
        placeholder: A string displayed as needed to help guide users in
            completing the element. 150 character maximum.
    """
    self._elements.append(
        DialogChannelSelector(
            name=name,
            label=label,
            optional=optional,
            value=value,
            placeholder=placeholder,
        )
    )
    return self
```

You can also provide a select menu with a list of channels. Specify your data\_source as channels to limit only to public channels

[https://docs.slack.dev/legacy/legacy-dialogs/#dynamic\_select\_elements\_channels\_conversations](https://docs.slack.dev/legacy/legacy-dialogs/#dynamic_select_elements_channels_conversations)

## Args (2)

**`name`**

Name of form element. Required. No more than 300 characters.

**`label`**

Label displayed to user. Required. No more than 48 characters.

**`optional`**

Provide true when the form element is not required. By default, form elements are required.

**`value`**

Provide a default selected value.

**`placeholder`**

A string displayed as needed to help guide users in completing the element. 150 character maximum.

`def conversation_selector(self,   *,   name: str,   label: str,   optional: bool = False,   value: str | None = None,   placeholder: str | None = None) ‑> [DialogBuilder](#slack_sdk.models.dialogs.DialogBuilder "slack_sdk.models.dialogs.DialogBuilder")`

Expand source code

```typescript
def conversation_selector(
    self,
    *,
    name: str,
    label: str,
    optional: bool = False,
    value: Optional[str] = None,
    placeholder: Optional[str] = None,
) -> "DialogBuilder":
    """
    You can also provide a select menu with a list of conversations - including
    private channels, direct messages, MPIMs, and whatever else we consider a
    conversation-like thing.

    https://docs.slack.dev/legacy/legacy-dialogs/#dynamic_select_elements_channels_conversations

    Args:
        name: Name of form element. Required. No more than 300 characters.
        label: Label displayed to user. Required. No more than 48 characters.
        optional: Provide true when the form element is not required. By
            default, form elements are required.
        value: Provide a default selected value.
        placeholder: A string displayed as needed to help guide users in
            completing the element. 150 character maximum.
    """
    self._elements.append(
        DialogConversationSelector(
            name=name,
            label=label,
            optional=optional,
            value=value,
            placeholder=placeholder,
        )
    )
    return self
```

You can also provide a select menu with a list of conversations - including private channels, direct messages, MPIMs, and whatever else we consider a conversation-like thing.

[https://docs.slack.dev/legacy/legacy-dialogs/#dynamic\_select\_elements\_channels\_conversations](https://docs.slack.dev/legacy/legacy-dialogs/#dynamic_select_elements_channels_conversations)

## Args (3)

**`name`**

Name of form element. Required. No more than 300 characters.

**`label`**

Label displayed to user. Required. No more than 48 characters.

**`optional`**

Provide true when the form element is not required. By default, form elements are required.

**`value`**

Provide a default selected value.

**`placeholder`**

A string displayed as needed to help guide users in completing the element. 150 character maximum.

`def elements_length(self) ‑> bool`

Expand source code

```python
@JsonValidator(f"dialogs must contain between 1 and {elements_max_length} elements")
def elements_length(self) -> bool:
    return 0 < len(self._elements) <= self.elements_max_length
```

`def external_selector(self,   *,   name: str,   label: str,   optional: bool = False,   value: [Option](../blocks/basic_components.html#slack_sdk.models.blocks.basic_components.Option "slack_sdk.models.blocks.basic_components.Option") | None = None,   placeholder: str | None = None,   min_query_length: int | None = None) ‑> [DialogBuilder](#slack_sdk.models.dialogs.DialogBuilder "slack_sdk.models.dialogs.DialogBuilder")`

Expand source code

```typescript
def external_selector(
    self,
    *,
    name: str,
    label: str,
    optional: bool = False,
    value: Optional[Option] = None,
    placeholder: Optional[str] = None,
    min_query_length: Optional[int] = None,
) -> "DialogBuilder":
    """
    Use the select element for multiple choice selections allowing users to pick
    a single item from a list. True to web roots, this selection is displayed as
    a dropdown menu.

    A list of options can be loaded from an external URL and used in your dialog
    menus.

    https://docs.slack.dev/legacy/legacy-dialogs/#dynamic_select_elements_external

    Args:
        name: Name of form element. Required. No more than 300 characters.
        label: Label displayed to user. Required. No more than 48 characters.
        min_query_length: Specify the number of characters that must be
            typed by a user into a dynamic select menu before dispatching to your
            application.
        optional: Provide true when the form element is not required. By
            default, form elements are required.
        value: Provide a default selected value. This should be a single
            Option or OptionGroup that exactly matches one that will be returned
            from your external endpoint.
        placeholder: A string displayed as needed to help guide users in
            completing the element. 150 character maximum.
    """
    self._elements.append(
        DialogExternalSelector(
            name=name,
            label=label,
            optional=optional,
            value=value,
            placeholder=placeholder,
            min_query_length=min_query_length,
        )
    )
    return self
```

Use the select element for multiple choice selections allowing users to pick a single item from a list. True to web roots, this selection is displayed as a dropdown menu.

A list of options can be loaded from an external URL and used in your dialog menus.

[https://docs.slack.dev/legacy/legacy-dialogs/#dynamic\_select\_elements\_external](https://docs.slack.dev/legacy/legacy-dialogs/#dynamic_select_elements_external)

## Args (4)

**`name`**

Name of form element. Required. No more than 300 characters.

**`label`**

Label displayed to user. Required. No more than 48 characters.

**`min_query_length`**

Specify the number of characters that must be typed by a user into a dynamic select menu before dispatching to your application.

**`optional`**

Provide true when the form element is not required. By default, form elements are required.

**`value`**

Provide a default selected value. This should be a single Option or OptionGroup that exactly matches one that will be returned from your external endpoint.

**`placeholder`**

A string displayed as needed to help guide users in completing the element. 150 character maximum.

`def notify_on_cancel(self, notify: bool) ‑> [DialogBuilder](#slack_sdk.models.dialogs.DialogBuilder "slack_sdk.models.dialogs.DialogBuilder")`

Expand source code

```python
def notify_on_cancel(self, notify: bool) -> "DialogBuilder":
    """
    Whether this dialog should send a request to your application even if the
    user cancels their interaction. Defaults to False.

    Args:
        notify: Set to True to indicate that your application should receive a
            request even if the user cancels interaction with the dialog.
    """
    self._notify_on_cancel = notify
    return self
```

Whether this dialog should send a request to your application even if the user cancels their interaction. Defaults to False.

## Args (5)

**`notify`**

Set to True to indicate that your application should receive a request even if the user cancels interaction with the dialog.

`def state(self, state: dict | str) ‑> [DialogBuilder](#slack_sdk.models.dialogs.DialogBuilder "slack_sdk.models.dialogs.DialogBuilder")`

Expand source code

```python
def state(self, state: Union[dict, str]) -> "DialogBuilder":
    """
    Pass state into this dialog - dictionaries will be automatically formatted to
    JSON

    Args:
        state: Extra state information that you need to pass from this dialog
            back to your application on submission
    """
    if isinstance(state, dict):
        self._state = dumps(state)
    else:
        self._state = state
    return self
```

Pass state into this dialog - dictionaries will be automatically formatted to JSON

## Args (6)

**`state`**

Extra state information that you need to pass from this dialog back to your application on submission

`def state_length(self) ‑> bool`

Expand source code

```python
@JsonValidator(f"state cannot exceed {state_max_length} characters")
def state_length(self) -> bool:
    return not self._state or len(self._state) <= self.state_max_length
```

`def static_selector(self,   *,   name: str,   label: str,   options: Sequence[[Option](../blocks/basic_components.html#slack_sdk.models.blocks.basic_components.Option "slack_sdk.models.blocks.basic_components.Option")] | Sequence[[OptionGroup](../blocks/basic_components.html#slack_sdk.models.blocks.basic_components.OptionGroup "slack_sdk.models.blocks.basic_components.OptionGroup")],   optional: bool = False,   value: str | None = None,   placeholder: str | None = None) ‑> [DialogBuilder](#slack_sdk.models.dialogs.DialogBuilder "slack_sdk.models.dialogs.DialogBuilder")`

Expand source code

```typescript
def static_selector(
    self,
    *,
    name: str,
    label: str,
    options: Union[Sequence[Option], Sequence[OptionGroup]],
    optional: bool = False,
    value: Optional[str] = None,
    placeholder: Optional[str] = None,
) -> "DialogBuilder":
    """
    Use the select element for multiple choice selections allowing users to pick
    a single item from a list. True to web roots, this selection is displayed as
    a dropdown menu.

    A select element may contain up to 100 selections, provided as a list of
    Option or OptionGroup objects

    https://docs.slack.dev/legacy/legacy-dialogs/#attributes_select_elements

    Args:
        name: Name of form element. Required. No more than 300 characters.
        label: Label displayed to user. Required. No more than 48 characters.
        options: A list of up to 100 Option or OptionGroup objects. Object
            types cannot be mixed.
        optional: Provide true when the form element is not required. By
            default, form elements are required.
        value: Provide a default selected value.
        placeholder: A string displayed as needed to help guide users in
            completing the element. 150 character maximum.
    """
    self._elements.append(
        DialogStaticSelector(
            name=name,
            label=label,
            options=options,
            optional=optional,
            value=value,
            placeholder=placeholder,
        )
    )
    return self
```

Use the select element for multiple choice selections allowing users to pick a single item from a list. True to web roots, this selection is displayed as a dropdown menu.

A select element may contain up to 100 selections, provided as a list of Option or OptionGroup objects

[https://docs.slack.dev/legacy/legacy-dialogs/#attributes\_select\_elements](https://docs.slack.dev/legacy/legacy-dialogs/#attributes_select_elements)

## Args (7)

**`name`**

Name of form element. Required. No more than 300 characters.

**`label`**

Label displayed to user. Required. No more than 48 characters.

**`options`**

A list of up to 100 Option or OptionGroup objects. Object types cannot be mixed.

**`optional`**

Provide true when the form element is not required. By default, form elements are required.

**`value`**

Provide a default selected value.

**`placeholder`**

A string displayed as needed to help guide users in completing the element. 150 character maximum.

`def submit_label(self, label: str) ‑> [DialogBuilder](#slack_sdk.models.dialogs.DialogBuilder "slack_sdk.models.dialogs.DialogBuilder")`

Expand source code

```python
def submit_label(self, label: str) -> "DialogBuilder":
    """
    The label to use on the 'Submit' button on the dialog. Defaults to 'Submit'
    if not specified.

    Args:
        label: must not exceed 24 characters, and must be a single word (no
            spaces)
    """
    self._submit_label = label
    return self
```

The label to use on the 'Submit' button on the dialog. Defaults to 'Submit' if not specified.

## Args (8)

**`label`**

must not exceed 24 characters, and must be a single word (no spaces)

`def submit_label_length(self) ‑> bool`

Expand source code

```python
@JsonValidator(f"submit_label cannot exceed {submit_label_max_length} characters")
def submit_label_length(self) -> bool:
    return self._submit_label is None or len(self._submit_label) <= self.submit_label_max_length
```

`def submit_label_valid(self) ‑> bool`

Expand source code

```python
@JsonValidator("submit_label can only be one word")
def submit_label_valid(self) -> bool:
    return self._submit_label is None or " " not in self._submit_label
```

`def text_area(self,   *,   name: str,   label: str,   optional: bool = False,   placeholder: str | None = None,   hint: str | None = None,   value: str | None = None,   min_length: int = 0,   max_length: int = 3000,   subtype: str | None = None) ‑> [DialogBuilder](#slack_sdk.models.dialogs.DialogBuilder "slack_sdk.models.dialogs.DialogBuilder")`

Expand source code

```typescript
def text_area(
    self,
    *,
    name: str,
    label: str,
    optional: bool = False,
    placeholder: Optional[str] = None,
    hint: Optional[str] = None,
    value: Optional[str] = None,
    min_length: int = 0,
    max_length: int = 3000,
    subtype: Optional[str] = None,
) -> "DialogBuilder":
    """
    A textarea is a multi-line plain text editing control. You've likely
    encountered these on the world wide web. Use this element if you want a
    relatively long answer from users. The element UI provides a remaining
    character count to the max_length you have set or the default,
    3000.

    https://docs.slack.dev/legacy/legacy-dialogs/#attributes_textarea_elements

    Args:
        name: Name of form element. Required. No more than 300 characters.
        label: Label displayed to user. Required. 48 character maximum.
        optional: Provide true when the form element is not required. By
            default, form elements are required.
        placeholder: A string displayed as needed to help guide users in
            completing the element. 150 character maximum.
        hint: Helpful text provided to assist users in answering a question.
            Up to 150 characters.
        value: A default value for this field. Up to 3000 characters.
        min_length: Minimum input length allowed for element. 1-3000
            characters. Defaults to 0.
        max_length: Maximum input length allowed for element. 0-3000
            characters. Defaults to 3000.
        subtype: A subtype for this text input. Accepts email, number, tel,
            or url. In some form factors, optimized input is provided for this
            subtype.
    """
    self._elements.append(
        DialogTextArea(
            name=name,
            label=label,
            optional=optional,
            placeholder=placeholder,
            hint=hint,
            value=value,
            min_length=min_length,
            max_length=max_length,
            subtype=subtype,
        )
    )
    return self
```

A textarea is a multi-line plain text editing control. You've likely encountered these on the world wide web. Use this element if you want a relatively long answer from users. The element UI provides a remaining character count to the max\_length you have set or the default, 3000.

[https://docs.slack.dev/legacy/legacy-dialogs/#attributes\_textarea\_elements](https://docs.slack.dev/legacy/legacy-dialogs/#attributes_textarea_elements)

## Args (9)

**`name`**

Name of form element. Required. No more than 300 characters.

**`label`**

Label displayed to user. Required. 48 character maximum.

**`optional`**

Provide true when the form element is not required. By default, form elements are required.

**`placeholder`**

A string displayed as needed to help guide users in completing the element. 150 character maximum.

**`hint`**

Helpful text provided to assist users in answering a question. Up to 150 characters.

**`value`**

A default value for this field. Up to 3000 characters.

**`min_length`**

Minimum input length allowed for element. 1-3000 characters. Defaults to 0.

**`max_length`**

Maximum input length allowed for element. 0-3000 characters. Defaults to 3000.

**`subtype`**

A subtype for this text input. Accepts email, number, tel, or url. In some form factors, optimized input is provided for this subtype.

`def text_field(self,   *,   name: str,   label: str,   optional: bool = False,   placeholder: str | None = None,   hint: str | None = None,   value: str | None = None,   min_length: int = 0,   max_length: int = 150,   subtype: str | None = None) ‑> [DialogBuilder](#slack_sdk.models.dialogs.DialogBuilder "slack_sdk.models.dialogs.DialogBuilder")`

Expand source code

```typescript
def text_field(
    self,
    *,
    name: str,
    label: str,
    optional: bool = False,
    placeholder: Optional[str] = None,
    hint: Optional[str] = None,
    value: Optional[str] = None,
    min_length: int = 0,
    max_length: int = 150,
    subtype: Optional[str] = None,
) -> "DialogBuilder":
    """
    Text elements are single-line plain text fields.

    https://docs.slack.dev/legacy/legacy-dialogs/#attributes_text_elements

    Args:
        name: Name of form element. Required. No more than 300 characters.
        label: Label displayed to user. Required. 48 character maximum.
        optional: Provide true when the form element is not required. By
            default, form elements are required.
        placeholder: A string displayed as needed to help guide users in
            completing the element. 150 character maximum.
        hint: Helpful text provided to assist users in answering a question.
            Up to 150 characters.
        value: A default value for this field. Up to 150 characters.
        min_length: Minimum input length allowed for element. Up to 150
            characters. Defaults to 0.
        max_length: Maximum input length allowed for element. Up to 150
            characters. Defaults to 150.
        subtype: A subtype for this text input. Accepts email, number, tel,
                or url. In some form factors, optimized input is provided for this
                subtype.
    """
    self._elements.append(
        DialogTextField(
            name=name,
            label=label,
            optional=optional,
            placeholder=placeholder,
            hint=hint,
            value=value,
            min_length=min_length,
            max_length=max_length,
            subtype=subtype,
        )
    )
    return self
```

Text elements are single-line plain text fields.

[https://docs.slack.dev/legacy/legacy-dialogs/#attributes\_text\_elements](https://docs.slack.dev/legacy/legacy-dialogs/#attributes_text_elements)

## Args (10)

**`name`**

Name of form element. Required. No more than 300 characters.

**`label`**

Label displayed to user. Required. 48 character maximum.

**`optional`**

Provide true when the form element is not required. By default, form elements are required.

**`placeholder`**

A string displayed as needed to help guide users in completing the element. 150 character maximum.

**`hint`**

Helpful text provided to assist users in answering a question. Up to 150 characters.

**`value`**

A default value for this field. Up to 150 characters.

**`min_length`**

Minimum input length allowed for element. Up to 150 characters. Defaults to 0.

**`max_length`**

Maximum input length allowed for element. Up to 150 characters. Defaults to 150.

**`subtype`**

A subtype for this text input. Accepts email, number, tel, or url. In some form factors, optimized input is provided for this subtype.

`def title(self, title: str) ‑> [DialogBuilder](#slack_sdk.models.dialogs.DialogBuilder "slack_sdk.models.dialogs.DialogBuilder")`

Expand source code

```python
def title(self, title: str) -> "DialogBuilder":
    """
    Specify a title for this dialog

    Args:
      title: must not exceed 24 characters
    """
    self._title = title
    return self
```

Specify a title for this dialog

## Args (11)

**`title`**

must not exceed 24 characters

`def title_length(self) ‑> bool`

Expand source code

```python
@JsonValidator(f"title attribute cannot exceed {title_max_length} characters")
def title_length(self) -> bool:
    return self._title is not None and len(self._title) <= self.title_max_length
```

`def title_present(self) ‑> bool`

Expand source code

```python
@JsonValidator("title attribute is required")
def title_present(self) -> bool:
    return self._title is not None
```

`def user_selector(self,   *,   name: str,   label: str,   optional: bool = False,   value: str | None = None,   placeholder: str | None = None) ‑> [DialogBuilder](#slack_sdk.models.dialogs.DialogBuilder "slack_sdk.models.dialogs.DialogBuilder")`

Expand source code

```typescript
def user_selector(
    self,
    *,
    name: str,
    label: str,
    optional: bool = False,
    value: Optional[str] = None,
    placeholder: Optional[str] = None,
) -> "DialogBuilder":
    """
    Now you can easily populate a select menu with a list of users. For example,
    when you are creating a bug tracking app, you want to include a field for an
    assignee. Slack pre-populates the user list in client-side, so your app
    doesn't need access to a related OAuth scope.

    https://docs.slack.dev/legacy/legacy-dialogs/#dynamic_select_elements_users

    Args:
        name: Name of form element. Required. No more than 300 characters.
        label: Label displayed to user. Required. No more than 48 characters.
        optional: Provide true when the form element is not required. By
            default, form elements are required.
        value: Provide a default selected value.
        placeholder: A string displayed as needed to help guide users in
            completing the element. 150 character maximum.
    """
    self._elements.append(
        DialogUserSelector(
            name=name,
            label=label,
            optional=optional,
            value=value,
            placeholder=placeholder,
        )
    )
    return self
```

Now you can easily populate a select menu with a list of users. For example, when you are creating a bug tracking app, you want to include a field for an assignee. Slack pre-populates the user list in client-side, so your app doesn't need access to a related OAuth scope.

[https://docs.slack.dev/legacy/legacy-dialogs/#dynamic\_select\_elements\_users](https://docs.slack.dev/legacy/legacy-dialogs/#dynamic_select_elements_users)

## Args (12)

**`name`**

Name of form element. Required. No more than 300 characters.

**`label`**

Label displayed to user. Required. No more than 48 characters.

**`optional`**

Provide true when the form element is not required. By default, form elements are required.

**`value`**

Provide a default selected value.

**`placeholder`**

A string displayed as needed to help guide users in completing the element. 150 character maximum.

### Inherited members (2)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class DialogChannelSelector (*,   name: str,   label: str,   optional: bool = False,   value: str | None = None,   placeholder: str | None = None)`

Expand source code

```typescript
class DialogChannelSelector(AbstractDialogSelector):
    data_source = "channels"

    def __init__(
        self,
        *,
        name: str,
        label: str,
        optional: bool = False,
        value: Optional[str] = None,
        placeholder: Optional[str] = None,
    ):
        """
        You can also provide a select menu with a list of channels. Specify your
        data_source as channels to limit only to public channels

        https://docs.slack.dev/legacy/legacy-dialogs/#dynamic_select_elements_channels_conversations

        Args:
            name: Name of form element. Required. No more than 300 characters.
            label: Label displayed to user. Required. No more than 48 characters.
            optional: Provide true when the form element is not required. By
                default, form elements are required.
            value: Provide a default selected value.
            placeholder: A string displayed as needed to help guide users in
                completing the element. 150 character maximum.
        """
        super().__init__(
            name=name,
            label=label,
            optional=optional,
            value=value,
            placeholder=placeholder,
        )
```

The base class for JSON serializable class objects

You can also provide a select menu with a list of channels. Specify your data\_source as channels to limit only to public channels

[https://docs.slack.dev/legacy/legacy-dialogs/#dynamic\_select\_elements\_channels\_conversations](https://docs.slack.dev/legacy/legacy-dialogs/#dynamic_select_elements_channels_conversations)

## Args (13)

**`name`**

Name of form element. Required. No more than 300 characters.

**`label`**

Label displayed to user. Required. No more than 48 characters.

**`optional`**

Provide true when the form element is not required. By default, form elements are required.

**`value`**

Provide a default selected value.

**`placeholder`**

A string displayed as needed to help guide users in completing the element. 150 character maximum.

### Ancestors (3)

* [AbstractDialogSelector](#slack_sdk.models.dialogs.AbstractDialogSelector "slack_sdk.models.dialogs.AbstractDialogSelector")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (3)

`var data_source`

The type of the None singleton.

### Inherited members (3)

* `**[AbstractDialogSelector](#slack_sdk.models.dialogs.AbstractDialogSelector "slack_sdk.models.dialogs.AbstractDialogSelector")**`:
  * `[DataSourceTypes](#slack_sdk.models.dialogs.AbstractDialogSelector.DataSourceTypes "slack_sdk.models.dialogs.AbstractDialogSelector.DataSourceTypes")`
  * `[attributes](#slack_sdk.models.dialogs.AbstractDialogSelector.attributes "slack_sdk.models.dialogs.AbstractDialogSelector.attributes")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.dialogs.AbstractDialogSelector.get_non_null_attributes")`
  * `[label_max_length](#slack_sdk.models.dialogs.AbstractDialogSelector.label_max_length "slack_sdk.models.dialogs.AbstractDialogSelector.label_max_length")`
  * `[name_max_length](#slack_sdk.models.dialogs.AbstractDialogSelector.name_max_length "slack_sdk.models.dialogs.AbstractDialogSelector.name_max_length")`
  * `[placeholder_max_length](#slack_sdk.models.dialogs.AbstractDialogSelector.placeholder_max_length "slack_sdk.models.dialogs.AbstractDialogSelector.placeholder_max_length")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.dialogs.AbstractDialogSelector.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.dialogs.AbstractDialogSelector.validate_json")`

`class DialogConversationSelector (*,   name: str,   label: str,   optional: bool = False,   value: str | None = None,   placeholder: str | None = None)`

Expand source code

```typescript
class DialogConversationSelector(AbstractDialogSelector):
    data_source = "conversations"

    def __init__(
        self,
        *,
        name: str,
        label: str,
        optional: bool = False,
        value: Optional[str] = None,
        placeholder: Optional[str] = None,
    ):
        """
        You can also provide a select menu with a list of conversations - including
        private channels, direct messages, MPIMs, and whatever else we consider a
        conversation-like thing.

        https://docs.slack.dev/legacy/legacy-dialogs/#dynamic_select_elements_channels_conversations

        Args:
            name: Name of form element. Required. No more than 300 characters.
            label: Label displayed to user. Required. No more than 48 characters.
            optional: Provide true when the form element is not required. By
                default, form elements are required.
            value: Provide a default selected value.
            placeholder: A string displayed as needed to help guide users in
                completing the element. 150 character maximum.
        """
        super().__init__(
            name=name,
            label=label,
            optional=optional,
            value=value,
            placeholder=placeholder,
        )
```

The base class for JSON serializable class objects

You can also provide a select menu with a list of conversations - including private channels, direct messages, MPIMs, and whatever else we consider a conversation-like thing.

[https://docs.slack.dev/legacy/legacy-dialogs/#dynamic\_select\_elements\_channels\_conversations](https://docs.slack.dev/legacy/legacy-dialogs/#dynamic_select_elements_channels_conversations)

## Args (14)

**`name`**

Name of form element. Required. No more than 300 characters.

**`label`**

Label displayed to user. Required. No more than 48 characters.

**`optional`**

Provide true when the form element is not required. By default, form elements are required.

**`value`**

Provide a default selected value.

**`placeholder`**

A string displayed as needed to help guide users in completing the element. 150 character maximum.

### Ancestors (4)

* [AbstractDialogSelector](#slack_sdk.models.dialogs.AbstractDialogSelector "slack_sdk.models.dialogs.AbstractDialogSelector")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (4)

`var data_source`

The type of the None singleton.

### Inherited members (4)

* `**[AbstractDialogSelector](#slack_sdk.models.dialogs.AbstractDialogSelector "slack_sdk.models.dialogs.AbstractDialogSelector")**`:
  * `[DataSourceTypes](#slack_sdk.models.dialogs.AbstractDialogSelector.DataSourceTypes "slack_sdk.models.dialogs.AbstractDialogSelector.DataSourceTypes")`
  * `[attributes](#slack_sdk.models.dialogs.AbstractDialogSelector.attributes "slack_sdk.models.dialogs.AbstractDialogSelector.attributes")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.dialogs.AbstractDialogSelector.get_non_null_attributes")`
  * `[label_max_length](#slack_sdk.models.dialogs.AbstractDialogSelector.label_max_length "slack_sdk.models.dialogs.AbstractDialogSelector.label_max_length")`
  * `[name_max_length](#slack_sdk.models.dialogs.AbstractDialogSelector.name_max_length "slack_sdk.models.dialogs.AbstractDialogSelector.name_max_length")`
  * `[placeholder_max_length](#slack_sdk.models.dialogs.AbstractDialogSelector.placeholder_max_length "slack_sdk.models.dialogs.AbstractDialogSelector.placeholder_max_length")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.dialogs.AbstractDialogSelector.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.dialogs.AbstractDialogSelector.validate_json")`

`class DialogExternalSelector (*,   name: str,   label: str,   value: [Option](../blocks/basic_components.html#slack_sdk.models.blocks.basic_components.Option "slack_sdk.models.blocks.basic_components.Option") | None = None,   min_query_length: int | None = None,   optional: bool | None = False,   placeholder: str | None = None)`

Expand source code

```typescript
class DialogExternalSelector(AbstractDialogSelector):
    data_source = "external"

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union({"min_query_length"})

    def __init__(
        self,
        *,
        name: str,
        label: str,
        value: Optional[Option] = None,
        min_query_length: Optional[int] = None,
        optional: Optional[bool] = False,
        placeholder: Optional[str] = None,
    ):
        """
        Use the select element for multiple choice selections allowing users to pick
        a single item from a list. True to web roots, this selection is displayed as
        a dropdown menu.

        A list of options can be loaded from an external URL and used in your dialog
        menus.

        https://docs.slack.dev/legacy/legacy-dialogs/#dynamic_select_elements_external

        Args:
            name: Name of form element. Required. No more than 300 characters.
            label: Label displayed to user. Required. No more than 48 characters.
            min_query_length: Specify the number of characters that must be typed
                by a user into a dynamic select menu before dispatching to the app.
            optional: Provide true when the form element is not required. By
                default, form elements are required.
            value: Provide a default selected value. This should be a single
                Option or OptionGroup that exactly matches one that will be returned
                from your external endpoint.
            placeholder: A string displayed as needed to help guide users in
                completing the element. 150 character maximum.
        """
        super().__init__(
            name=name,
            label=label,
            value=value,
            optional=optional,  # type: ignore[arg-type]
            placeholder=placeholder,
        )
        self.min_query_length = min_query_length
```

The base class for JSON serializable class objects

Use the select element for multiple choice selections allowing users to pick a single item from a list. True to web roots, this selection is displayed as a dropdown menu.

A list of options can be loaded from an external URL and used in your dialog menus.

[https://docs.slack.dev/legacy/legacy-dialogs/#dynamic\_select\_elements\_external](https://docs.slack.dev/legacy/legacy-dialogs/#dynamic_select_elements_external)

## Args (15)

**`name`**

Name of form element. Required. No more than 300 characters.

**`label`**

Label displayed to user. Required. No more than 48 characters.

**`min_query_length`**

Specify the number of characters that must be typed by a user into a dynamic select menu before dispatching to the app.

**`optional`**

Provide true when the form element is not required. By default, form elements are required.

**`value`**

Provide a default selected value. This should be a single Option or OptionGroup that exactly matches one that will be returned from your external endpoint.

**`placeholder`**

A string displayed as needed to help guide users in completing the element. 150 character maximum.

### Ancestors (5)

* [AbstractDialogSelector](#slack_sdk.models.dialogs.AbstractDialogSelector "slack_sdk.models.dialogs.AbstractDialogSelector")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (5)

`var data_source`

The type of the None singleton.

### Instance variables (2)

`prop attributes : Set[str]`

Expand source code

```python
@property
def attributes(self) -> Set[str]:  # type: ignore[override]
    return super().attributes.union({"min_query_length"})
```

Build an unordered collection of unique elements.

### Inherited members (5)

* `**[AbstractDialogSelector](#slack_sdk.models.dialogs.AbstractDialogSelector "slack_sdk.models.dialogs.AbstractDialogSelector")**`:
  * `[DataSourceTypes](#slack_sdk.models.dialogs.AbstractDialogSelector.DataSourceTypes "slack_sdk.models.dialogs.AbstractDialogSelector.DataSourceTypes")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.dialogs.AbstractDialogSelector.get_non_null_attributes")`
  * `[label_max_length](#slack_sdk.models.dialogs.AbstractDialogSelector.label_max_length "slack_sdk.models.dialogs.AbstractDialogSelector.label_max_length")`
  * `[name_max_length](#slack_sdk.models.dialogs.AbstractDialogSelector.name_max_length "slack_sdk.models.dialogs.AbstractDialogSelector.name_max_length")`
  * `[placeholder_max_length](#slack_sdk.models.dialogs.AbstractDialogSelector.placeholder_max_length "slack_sdk.models.dialogs.AbstractDialogSelector.placeholder_max_length")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.dialogs.AbstractDialogSelector.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.dialogs.AbstractDialogSelector.validate_json")`

`class DialogStaticSelector (*,   name: str,   label: str,   options: Sequence[[Option](../blocks/basic_components.html#slack_sdk.models.blocks.basic_components.Option "slack_sdk.models.blocks.basic_components.Option")] | Sequence[[OptionGroup](../blocks/basic_components.html#slack_sdk.models.blocks.basic_components.OptionGroup "slack_sdk.models.blocks.basic_components.OptionGroup")],   optional: bool = False,   value: [Option](../blocks/basic_components.html#slack_sdk.models.blocks.basic_components.Option "slack_sdk.models.blocks.basic_components.Option") | str | None = None,   placeholder: str | None = None)`

Expand source code

```typescript
class DialogStaticSelector(AbstractDialogSelector):
    """
    Use the select element for multiple choice selections allowing users to pick a
    single item from a list. True to web roots, this selection is displayed as a
    dropdown menu.

    https://docs.slack.dev/legacy/legacy-dialogs/#select_elements
    """

    data_source = "static"

    options_max_length = 100

    def __init__(
        self,
        *,
        name: str,
        label: str,
        options: Union[Sequence[Option], Sequence[OptionGroup]],
        optional: bool = False,
        value: Optional[Union[Option, str]] = None,
        placeholder: Optional[str] = None,
    ):
        """
        Use the select element for multiple choice selections allowing users to pick
        a single item from a list. True to web roots, this selection is displayed as
        a dropdown menu.

        A select element may contain up to 100 selections, provided as a list of
        Option or OptionGroup objects

        https://docs.slack.dev/legacy/legacy-dialogs/#attributes_select_elements

        Args:
            name: Name of form element. Required. No more than 300 characters.
            label: Label displayed to user. Required. No more than 48 characters.
            options: A list of up to 100 Option or OptionGroup objects. Object
                types cannot be mixed.
            optional: Provide true when the form element is not required. By
                default, form elements are required.
            value: Provide a default selected value.
            placeholder: A string displayed as needed to help guide users in
                completing the element. 150 character maximum.
        """
        super().__init__(
            name=name,
            label=label,
            optional=optional,
            value=value,
            placeholder=placeholder,
        )
        self.options = options

    @JsonValidator(f"options attribute cannot exceed {options_max_length} items")
    def options_length(self) -> bool:
        return len(self.options) < self.options_max_length

    def to_dict(self) -> dict:
        json = super().to_dict()
        if isinstance(self.options[0], OptionGroup):
            json["option_groups"] = extract_json(self.options, "dialog")
        else:
            json["options"] = extract_json(self.options, "dialog")
        return json
```

Use the select element for multiple choice selections allowing users to pick a single item from a list. True to web roots, this selection is displayed as a dropdown menu.

[https://docs.slack.dev/legacy/legacy-dialogs/#select\_elements](https://docs.slack.dev/legacy/legacy-dialogs/#select_elements)

Use the select element for multiple choice selections allowing users to pick a single item from a list. True to web roots, this selection is displayed as a dropdown menu.

A select element may contain up to 100 selections, provided as a list of Option or OptionGroup objects

[https://docs.slack.dev/legacy/legacy-dialogs/#attributes\_select\_elements](https://docs.slack.dev/legacy/legacy-dialogs/#attributes_select_elements)

## Args (16)

**`name`**

Name of form element. Required. No more than 300 characters.

**`label`**

Label displayed to user. Required. No more than 48 characters.

**`options`**

A list of up to 100 Option or OptionGroup objects. Object types cannot be mixed.

**`optional`**

Provide true when the form element is not required. By default, form elements are required.

**`value`**

Provide a default selected value.

**`placeholder`**

A string displayed as needed to help guide users in completing the element. 150 character maximum.

### Ancestors (6)

* [AbstractDialogSelector](#slack_sdk.models.dialogs.AbstractDialogSelector "slack_sdk.models.dialogs.AbstractDialogSelector")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (6)

`var data_source`

The type of the None singleton.

`var options_max_length`

The type of the None singleton.

### Methods (3)

`def options_length(self) ‑> bool`

Expand source code

```python
@JsonValidator(f"options attribute cannot exceed {options_max_length} items")
def options_length(self) -> bool:
    return len(self.options) < self.options_max_length
```

### Inherited members (6)

* `**[AbstractDialogSelector](#slack_sdk.models.dialogs.AbstractDialogSelector "slack_sdk.models.dialogs.AbstractDialogSelector")**`:
  * `[DataSourceTypes](#slack_sdk.models.dialogs.AbstractDialogSelector.DataSourceTypes "slack_sdk.models.dialogs.AbstractDialogSelector.DataSourceTypes")`
  * `[attributes](#slack_sdk.models.dialogs.AbstractDialogSelector.attributes "slack_sdk.models.dialogs.AbstractDialogSelector.attributes")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.dialogs.AbstractDialogSelector.get_non_null_attributes")`
  * `[label_max_length](#slack_sdk.models.dialogs.AbstractDialogSelector.label_max_length "slack_sdk.models.dialogs.AbstractDialogSelector.label_max_length")`
  * `[name_max_length](#slack_sdk.models.dialogs.AbstractDialogSelector.name_max_length "slack_sdk.models.dialogs.AbstractDialogSelector.name_max_length")`
  * `[placeholder_max_length](#slack_sdk.models.dialogs.AbstractDialogSelector.placeholder_max_length "slack_sdk.models.dialogs.AbstractDialogSelector.placeholder_max_length")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.dialogs.AbstractDialogSelector.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.dialogs.AbstractDialogSelector.validate_json")`

`class DialogTextArea (*,   name: str,   label: str,   optional: bool = False,   placeholder: str | None = None,   hint: str | None = None,   value: str | None = None,   min_length: int = 0,   max_length: int | None = None,   subtype: str | None = None)`

Expand source code

```typescript
class DialogTextArea(DialogTextComponent):
    """
    A textarea is a multi-line plain text editing control. You've likely encountered
    these on the world wide web. Use this element if you want a relatively long
    answer from users. The element UI provides a remaining character count to the
    max_length you have set or the default, 3000.

    https://docs.slack.dev/legacy/legacy-dialogs/#textarea_elements
    """

    type = "textarea"
    max_value_length = 3000
```

A textarea is a multi-line plain text editing control. You've likely encountered these on the world wide web. Use this element if you want a relatively long answer from users. The element UI provides a remaining character count to the max\_length you have set or the default, 3000.

[https://docs.slack.dev/legacy/legacy-dialogs/#textarea\_elements](https://docs.slack.dev/legacy/legacy-dialogs/#textarea_elements)

### Ancestors (7)

* [DialogTextComponent](#slack_sdk.models.dialogs.DialogTextComponent "slack_sdk.models.dialogs.DialogTextComponent")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (7)

`var max_value_length`

The type of the None singleton.

`var type`

The type of the None singleton.

### Inherited members (7)

* `**[DialogTextComponent](#slack_sdk.models.dialogs.DialogTextComponent "slack_sdk.models.dialogs.DialogTextComponent")**`:
  * `[attributes](#slack_sdk.models.dialogs.DialogTextComponent.attributes "slack_sdk.models.dialogs.DialogTextComponent.attributes")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.dialogs.DialogTextComponent.get_non_null_attributes")`
  * `[hint_max_length](#slack_sdk.models.dialogs.DialogTextComponent.hint_max_length "slack_sdk.models.dialogs.DialogTextComponent.hint_max_length")`
  * `[label_max_length](#slack_sdk.models.dialogs.DialogTextComponent.label_max_length "slack_sdk.models.dialogs.DialogTextComponent.label_max_length")`
  * `[name_max_length](#slack_sdk.models.dialogs.DialogTextComponent.name_max_length "slack_sdk.models.dialogs.DialogTextComponent.name_max_length")`
  * `[placeholder_max_length](#slack_sdk.models.dialogs.DialogTextComponent.placeholder_max_length "slack_sdk.models.dialogs.DialogTextComponent.placeholder_max_length")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.dialogs.DialogTextComponent.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.dialogs.DialogTextComponent.validate_json")`

`class DialogTextComponent (*,   name: str,   label: str,   optional: bool = False,   placeholder: str | None = None,   hint: str | None = None,   value: str | None = None,   min_length: int = 0,   max_length: int | None = None,   subtype: str | None = None)`

Expand source code

```typescript
class DialogTextComponent(JsonObject, metaclass=ABCMeta):
    attributes = {
        "hint",
        "label",
        "max_length",
        "min_length",
        "name",
        "optional",
        "placeholder",
        "subtype",
        "type",
        "value",
    }

    name_max_length = 300
    label_max_length = 48
    placeholder_max_length = 150
    hint_max_length = 150

    @property
    @abstractmethod
    def type(self):
        pass

    @property
    @abstractmethod
    def max_value_length(self):
        pass

    def __init__(
        self,
        *,
        name: str,
        label: str,
        optional: bool = False,
        placeholder: Optional[str] = None,
        hint: Optional[str] = None,
        value: Optional[str] = None,
        min_length: int = 0,
        max_length: Optional[int] = None,
        subtype: Optional[str] = None,
    ):
        self.name = name
        self.label = label
        self.optional = optional
        self.placeholder = placeholder
        self.hint = hint
        self.value = value
        self.min_length = min_length
        self.max_length = max_length or self.max_value_length
        self.subtype = subtype

    @JsonValidator(f"name attribute cannot exceed {name_max_length} characters")
    def name_length(self) -> bool:
        return len(self.name) < self.name_max_length

    @JsonValidator(f"label attribute cannot exceed {label_max_length} characters")
    def label_length(self) -> bool:
        return len(self.label) < self.label_max_length

    @JsonValidator(f"placeholder attribute cannot exceed {placeholder_max_length} characters")
    def placeholder_length(self) -> bool:
        return self.placeholder is None or len(self.placeholder) < self.placeholder_max_length

    @JsonValidator(f"hint attribute cannot exceed {hint_max_length} characters")
    def hint_length(self) -> bool:
        return self.hint is None or len(self.hint) < self.hint_max_length

    @JsonValidator("value attribute exceeded bounds")
    def value_length(self) -> bool:
        return self.value is None or len(self.value) < self.max_value_length

    @JsonValidator("min_length attribute must be greater than or equal to 0")
    def min_length_above_zero(self) -> bool:
        return self.min_length is None or self.min_length >= 0

    @JsonValidator("min_length attribute exceed bounds")
    def min_length_length(self) -> bool:
        return self.min_length is None or self.min_length <= self.max_value_length

    @JsonValidator("min_length attribute must be less than max value attribute")
    def min_length_below_max_length(self) -> bool:
        return self.min_length is None or self.min_length < self.max_length

    @JsonValidator("max_length attribute must be greater than or equal to 0")
    def max_length_above_zero(self) -> bool:
        return self.max_length is None or self.max_length > 0

    @JsonValidator("max_length attribute exceeded bounds")
    def max_length_length(self) -> bool:
        return self.max_length is None or self.max_length <= self.max_value_length

    @EnumValidator("subtype", TextElementSubtypes)
    def subtype_valid(self) -> bool:
        return self.subtype is None or self.subtype in TextElementSubtypes
```

The base class for JSON serializable class objects

### Ancestors (8)

* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Subclasses (2)

* [DialogTextArea](#slack_sdk.models.dialogs.DialogTextArea "slack_sdk.models.dialogs.DialogTextArea")
* [DialogTextField](#slack_sdk.models.dialogs.DialogTextField "slack_sdk.models.dialogs.DialogTextField")

### Class variables (8)

`var attributes`

The type of the None singleton.

`var hint_max_length`

The type of the None singleton.

`var label_max_length`

The type of the None singleton.

`var name_max_length`

The type of the None singleton.

`var placeholder_max_length`

The type of the None singleton.

### Instance variables (3)

`prop max_value_length`

Expand source code

```python
@property
@abstractmethod
def max_value_length(self):
    pass
```

`prop type`

Expand source code

```python
@property
@abstractmethod
def type(self):
    pass
```

### Methods (4)

`def hint_length(self) ‑> bool`

Expand source code

```python
@JsonValidator(f"hint attribute cannot exceed {hint_max_length} characters")
def hint_length(self) -> bool:
    return self.hint is None or len(self.hint) < self.hint_max_length
```

`def label_length(self) ‑> bool`

Expand source code

```python
@JsonValidator(f"label attribute cannot exceed {label_max_length} characters")
def label_length(self) -> bool:
    return len(self.label) < self.label_max_length
```

`def max_length_above_zero(self) ‑> bool`

Expand source code

```python
@JsonValidator("max_length attribute must be greater than or equal to 0")
def max_length_above_zero(self) -> bool:
    return self.max_length is None or self.max_length > 0
```

`def max_length_length(self) ‑> bool`

Expand source code

```python
@JsonValidator("max_length attribute exceeded bounds")
def max_length_length(self) -> bool:
    return self.max_length is None or self.max_length <= self.max_value_length
```

`def min_length_above_zero(self) ‑> bool`

Expand source code

```python
@JsonValidator("min_length attribute must be greater than or equal to 0")
def min_length_above_zero(self) -> bool:
    return self.min_length is None or self.min_length >= 0
```

`def min_length_below_max_length(self) ‑> bool`

Expand source code

```python
@JsonValidator("min_length attribute must be less than max value attribute")
def min_length_below_max_length(self) -> bool:
    return self.min_length is None or self.min_length < self.max_length
```

`def min_length_length(self) ‑> bool`

Expand source code

```python
@JsonValidator("min_length attribute exceed bounds")
def min_length_length(self) -> bool:
    return self.min_length is None or self.min_length <= self.max_value_length
```

`def name_length(self) ‑> bool`

Expand source code

```python
@JsonValidator(f"name attribute cannot exceed {name_max_length} characters")
def name_length(self) -> bool:
    return len(self.name) < self.name_max_length
```

`def placeholder_length(self) ‑> bool`

Expand source code

```python
@JsonValidator(f"placeholder attribute cannot exceed {placeholder_max_length} characters")
def placeholder_length(self) -> bool:
    return self.placeholder is None or len(self.placeholder) < self.placeholder_max_length
```

`def subtype_valid(self) ‑> bool`

Expand source code

```typescript
@EnumValidator("subtype", TextElementSubtypes)
def subtype_valid(self) -> bool:
    return self.subtype is None or self.subtype in TextElementSubtypes
```

`def value_length(self) ‑> bool`

Expand source code

```python
@JsonValidator("value attribute exceeded bounds")
def value_length(self) -> bool:
    return self.value is None or len(self.value) < self.max_value_length
```

### Inherited members (8)

* `**[JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")**`:
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.basic_objects.JsonObject.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.basic_objects.JsonObject.validate_json")`

`class DialogTextField (*,   name: str,   label: str,   optional: bool = False,   placeholder: str | None = None,   hint: str | None = None,   value: str | None = None,   min_length: int = 0,   max_length: int | None = None,   subtype: str | None = None)`

Expand source code

```typescript
class DialogTextField(DialogTextComponent):
    """
    Text elements are single-line plain text fields.

    https://docs.slack.dev/legacy/legacy-dialogs/#text_elements
    """

    type = "text"
    max_value_length = 150
```

Text elements are single-line plain text fields.

[https://docs.slack.dev/legacy/legacy-dialogs/#text\_elements](https://docs.slack.dev/legacy/legacy-dialogs/#text_elements)

### Ancestors (9)

* [DialogTextComponent](#slack_sdk.models.dialogs.DialogTextComponent "slack_sdk.models.dialogs.DialogTextComponent")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (9)

`var max_value_length`

The type of the None singleton.

`var type`

The type of the None singleton.

### Inherited members (9)

* `**[DialogTextComponent](#slack_sdk.models.dialogs.DialogTextComponent "slack_sdk.models.dialogs.DialogTextComponent")**`:
  * `[attributes](#slack_sdk.models.dialogs.DialogTextComponent.attributes "slack_sdk.models.dialogs.DialogTextComponent.attributes")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.dialogs.DialogTextComponent.get_non_null_attributes")`
  * `[hint_max_length](#slack_sdk.models.dialogs.DialogTextComponent.hint_max_length "slack_sdk.models.dialogs.DialogTextComponent.hint_max_length")`
  * `[label_max_length](#slack_sdk.models.dialogs.DialogTextComponent.label_max_length "slack_sdk.models.dialogs.DialogTextComponent.label_max_length")`
  * `[name_max_length](#slack_sdk.models.dialogs.DialogTextComponent.name_max_length "slack_sdk.models.dialogs.DialogTextComponent.name_max_length")`
  * `[placeholder_max_length](#slack_sdk.models.dialogs.DialogTextComponent.placeholder_max_length "slack_sdk.models.dialogs.DialogTextComponent.placeholder_max_length")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.dialogs.DialogTextComponent.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.dialogs.DialogTextComponent.validate_json")`

`class DialogUserSelector (*,   name: str,   label: str,   optional: bool = False,   value: str | None = None,   placeholder: str | None = None)`

Expand source code

```typescript
class DialogUserSelector(AbstractDialogSelector):
    data_source = "users"

    def __init__(
        self,
        *,
        name: str,
        label: str,
        optional: bool = False,
        value: Optional[str] = None,
        placeholder: Optional[str] = None,
    ):
        """
        Now you can easily populate a select menu with a list of users. For example,
        when you are creating a bug tracking app, you want to include a field for an
        assignee. Slack pre-populates the user list in client-side, so your app
        doesn't need access to a related OAuth scope.

        https://docs.slack.dev/legacy/legacy-dialogs/#dynamic_select_elements_users

        Args:
            name: Name of form element. Required. No more than 300 characters.
            label: Label displayed to user. Required. No more than 48 characters.
            optional: Provide true when the form element is not required. By
                default, form elements are required.
            value: Provide a default selected value.
            placeholder: A string displayed as needed to help guide users in
                completing the element. 150 character maximum.
        """
        super().__init__(
            name=name,
            label=label,
            optional=optional,
            value=value,
            placeholder=placeholder,
        )
```

The base class for JSON serializable class objects

Now you can easily populate a select menu with a list of users. For example, when you are creating a bug tracking app, you want to include a field for an assignee. Slack pre-populates the user list in client-side, so your app doesn't need access to a related OAuth scope.

[https://docs.slack.dev/legacy/legacy-dialogs/#dynamic\_select\_elements\_users](https://docs.slack.dev/legacy/legacy-dialogs/#dynamic_select_elements_users)

## Args (17)

**`name`**

Name of form element. Required. No more than 300 characters.

**`label`**

Label displayed to user. Required. No more than 48 characters.

**`optional`**

Provide true when the form element is not required. By default, form elements are required.

**`value`**

Provide a default selected value.

**`placeholder`**

A string displayed as needed to help guide users in completing the element. 150 character maximum.

### Ancestors (10)

* [AbstractDialogSelector](#slack_sdk.models.dialogs.AbstractDialogSelector "slack_sdk.models.dialogs.AbstractDialogSelector")
* [JsonObject](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject "slack_sdk.models.basic_objects.JsonObject")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables (10)

`var data_source`

The type of the None singleton.

### Inherited members (10)

* `**[AbstractDialogSelector](#slack_sdk.models.dialogs.AbstractDialogSelector "slack_sdk.models.dialogs.AbstractDialogSelector")**`:
  * `[DataSourceTypes](#slack_sdk.models.dialogs.AbstractDialogSelector.DataSourceTypes "slack_sdk.models.dialogs.AbstractDialogSelector.DataSourceTypes")`
  * `[attributes](#slack_sdk.models.dialogs.AbstractDialogSelector.attributes "slack_sdk.models.dialogs.AbstractDialogSelector.attributes")`
  * `[get_non_null_attributes](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.get_non_null_attributes "slack_sdk.models.dialogs.AbstractDialogSelector.get_non_null_attributes")`
  * `[label_max_length](#slack_sdk.models.dialogs.AbstractDialogSelector.label_max_length "slack_sdk.models.dialogs.AbstractDialogSelector.label_max_length")`
  * `[name_max_length](#slack_sdk.models.dialogs.AbstractDialogSelector.name_max_length "slack_sdk.models.dialogs.AbstractDialogSelector.name_max_length")`
  * `[placeholder_max_length](#slack_sdk.models.dialogs.AbstractDialogSelector.placeholder_max_length "slack_sdk.models.dialogs.AbstractDialogSelector.placeholder_max_length")`
  * `[to_dict](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.to_dict "slack_sdk.models.dialogs.AbstractDialogSelector.to_dict")`
  * `[validate_json](../basic_objects.html#slack_sdk.models.basic_objects.JsonObject.validate_json "slack_sdk.models.dialogs.AbstractDialogSelector.validate_json")`
