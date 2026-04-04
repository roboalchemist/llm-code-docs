Source: https://docs.slack.dev/tools/python-slack-sdk/reference/models/messages

# Module slack_sdk.models.messages

## Sub-modules

`[slack_sdk.models.messages.chunk](chunk.html "slack_sdk.models.messages.chunk")`

`[slack_sdk.models.messages.message](message.html "slack_sdk.models.messages.message")`

## Classes

`class ChannelLink`

Expand source code

```typescript
class ChannelLink(Link):
    def __init__(self):
        """Represents an @channel link, which notifies everyone present in this channel.
        https://docs.slack.dev/messaging/formatting-message-text/
        """
        super().__init__(url="!channel", text="channel")
```

The base class for all model objects in this module

Represents an @channel link, which notifies everyone present in this channel. [https://docs.slack.dev/messaging/formatting-message-text/](https://docs.slack.dev/messaging/formatting-message-text/)

### Ancestors

* [Link](#slack_sdk.models.messages.Link "slack_sdk.models.messages.Link")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

`class DateLink (*,   date: datetime.datetime | int,   date_format: str,   fallback: str,   link: str | None = None)`

Expand source code

```typescript
class DateLink(Link):
    def __init__(
        self,
        *,
        date: Union[datetime, int],
        date_format: str,
        fallback: str,
        link: Optional[str] = None,
    ):
        """Text containing a date or time should display that date in the local timezone of the person seeing the text.
        https://docs.slack.dev/messaging/formatting-message-text/#date-formatting
        """
        if isinstance(date, datetime):
            epoch = int(date.timestamp())
        else:
            epoch = date
        if link is not None:
            link = f"^{link}"
        else:
            link = ""
        super().__init__(url=f"!date^{epoch}^{date_format}{link}", text=fallback)
```

The base class for all model objects in this module

Text containing a date or time should display that date in the local timezone of the person seeing the text. [https://docs.slack.dev/messaging/formatting-message-text/#date-formatting](https://docs.slack.dev/messaging/formatting-message-text/#date-formatting)

### Ancestors (2)

* [Link](#slack_sdk.models.messages.Link "slack_sdk.models.messages.Link")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

`class EveryoneLink`

Expand source code

```typescript
class EveryoneLink(Link):
    def __init__(self):
        """Represents an @everyone link, which notifies all users of this workspace.
        https://docs.slack.dev/messaging/formatting-message-text/
        """
        super().__init__(url="!everyone", text="everyone")
```

The base class for all model objects in this module

Represents an @everyone link, which notifies all users of this workspace. [https://docs.slack.dev/messaging/formatting-message-text/](https://docs.slack.dev/messaging/formatting-message-text/)

### Ancestors (3)

* [Link](#slack_sdk.models.messages.Link "slack_sdk.models.messages.Link")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

`class HereLink`

Expand source code

```typescript
class HereLink(Link):
    def __init__(self):
        """Represents an @here link, which notifies all online users of this channel.
        https://docs.slack.dev/messaging/formatting-message-text/
        """
        super().__init__(url="!here", text="here")
```

The base class for all model objects in this module

Represents an @here link, which notifies all online users of this channel. [https://docs.slack.dev/messaging/formatting-message-text/](https://docs.slack.dev/messaging/formatting-message-text/)

### Ancestors (4)

* [Link](#slack_sdk.models.messages.Link "slack_sdk.models.messages.Link")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

`class Link (*, url: str, text: str)`

Expand source code

```typescript
class Link(BaseObject):
    def __init__(self, *, url: str, text: str):
        """Base class used to generate links in Slack's not-quite Markdown, not quite HTML syntax
        https://docs.slack.dev/messaging/formatting-message-text/#linking_to_urls
        """
        self.url = url
        self.text = text

    def __str__(self):
        if self.text:
            separator = "|"
        else:
            separator = ""
        return f"<{self.url}{separator}{self.text}>"
```

The base class for all model objects in this module

Base class used to generate links in Slack's not-quite Markdown, not quite HTML syntax [https://docs.slack.dev/messaging/formatting-message-text/#linking\_to\_urls](https://docs.slack.dev/messaging/formatting-message-text/#linking_to_urls)

### Ancestors (5)

* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Subclasses

* [ChannelLink](#slack_sdk.models.messages.ChannelLink "slack_sdk.models.messages.ChannelLink")
* [DateLink](#slack_sdk.models.messages.DateLink "slack_sdk.models.messages.DateLink")
* [EveryoneLink](#slack_sdk.models.messages.EveryoneLink "slack_sdk.models.messages.EveryoneLink")
* [HereLink](#slack_sdk.models.messages.HereLink "slack_sdk.models.messages.HereLink")
* [ObjectLink](#slack_sdk.models.messages.ObjectLink "slack_sdk.models.messages.ObjectLink")

`class ObjectLink (*, object_id: str, text: str = '')`

Expand source code

```typescript
class ObjectLink(Link):
    prefix_mapping = {
        "C": "#",  # channel
        "G": "#",  # group message
        "U": "@",  # user
        "W": "@",  # workspace user (enterprise)
        "B": "@",  # bot user
        "S": "!subteam^",  # user groups, originally known as subteams
    }

    def __init__(self, *, object_id: str, text: str = ""):
        """Convenience class to create links to specific object types
        https://docs.slack.dev/messaging/formatting-message-text/#linking-channels
        """
        prefix = self.prefix_mapping.get(object_id[0].upper(), "@")
        super().__init__(url=f"{prefix}{object_id}", text=text)
```

The base class for all model objects in this module

Convenience class to create links to specific object types [https://docs.slack.dev/messaging/formatting-message-text/#linking-channels](https://docs.slack.dev/messaging/formatting-message-text/#linking-channels)

### Ancestors (6)

* [Link](#slack_sdk.models.messages.Link "slack_sdk.models.messages.Link")
* [BaseObject](../basic_objects.html#slack_sdk.models.basic_objects.BaseObject "slack_sdk.models.basic_objects.BaseObject")

### Class variables

`var prefix_mapping`

The type of the None singleton.
