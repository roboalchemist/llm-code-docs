# Source: https://docs.streamlit.io/develop/api-reference/widgets/st.datetime_input

# st.datetime_input

Display a date and time input widget.

## Function signature

```jsx
st.datetime_input(
  label: string,
  value: datetime.datetime | datetime.date | datetime.time | string | null,
  min_value: datetime.datetime | datetime.date | datetime.time | string | null,
  max_value: datetime.datetime | datetime.date | datetime.time | string | null,
  key: string | number,
  help: string | null,
  on_change: callable,
  args: list | tuple,
  kwargs: dict,
  format: string,
  step: int | timedelta,
  disabled: bool,
  label_visibility: "visible" | "hidden" | "collapsed",
  width: "stretch" | number,
)
```

## Parameters

- **label**: (str) A short label explaining to the user what this datetime input is for. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height.

  Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list".

  See the `body` parameter of [st.markdown](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives.

  For accessibility reasons, you should never set an empty label, but you can hide it with `label_visibility` if needed. In the future, we may disallow empty labels by raising an exception.

- **value**: (datetime.datetime | datetime.date | datetime.time | string | null) The value of this widget when it first renders. This can be one of the following:

  - "now" (default): The widget initializes with the current date and time.
  - A datetime.datetime object: The widget initializes with the given datetime, stripping any timezone information.
  - A datetime.date object: The widget initializes with the given date at 00:00.
  - A datetime.time object: The widget initializes with today's date and the provided time.
  - An ISO-formatted datetime (YYYY-MM-DD hh:mm[:ss]) or date/time string: The widget initializes with the parsed value.
  - None: The widget initializes with no value and returns None until the user selects a datetime.

- **min_value**: (datetime.datetime | datetime.date | datetime.time | string | null) The minimum selectable datetime. This can be any of the datetime types accepted by `value`.

  If this is None (default), the minimum selectable datetime is ten years before the initial value. If no initial value is set, the minimum selectable datetime is ten years before today at 00:00.

- **max_value**: (datetime.datetime | datetime.date | datetime.time | string | null) The maximum selectable datetime. This can be any of the datetime types accepted by `value`.

  If this is None (default), the maximum selectable datetime is ten years after the initial value. If no initial value is set, the maximum selectable datetime is ten years after today at 23:59.

- **key**: (str or int) An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key.

- **help**: (str or null) A tooltip that gets displayed next to the widget label. Streamlit only displays the tooltip when `label_visibility="visible"`. If this is None (default), no tooltip is displayed.

  The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the `body` parameter of `st.markdown`.

- **on_change**: (callable) An optional callback invoked when this datetime_input's value changes.

- **args**: (list or tuple) An optional list or tuple of args to pass to the callback.

- **kwargs**: (dict) An optional dict of kwargs to pass to the callback.

- **format**: (str) A format string controlling how the interface displays dates. Supports "YYYY/MM/DD" (default), "DD/MM/YYYY", or "MM/DD/YYYY". You may also use a period (.) or hyphen (-) as separators. This doesn't affect the time format.

- **step**: (int or timedelta) The stepping interval in seconds. This defaults to 900 (15 minutes). You can also pass a datetime.timedelta object. The value must be between 60 seconds and 23 hours.

- **disabled**: (bool) An optional boolean that disables the widget if set to True. The default is False.

- **label_visibility**: ("visible" | "hidden" | "collapsed") The visibility of the label. The default is "visible". If this is "hidden", Streamlit displays an empty spacer instead of the label, which can help keep the widget aligned with other widgets. If this is "collapsed", Streamlit displays no label or spacer.

- **width**: ("stretch" or number) The width of the widget. This can be one of the following:

  - "stretch" (default): The width of the widget matches the width of the parent container.
  - An integer specifying the width in pixels: The widget has a fixed width. If the specified width is greater than the width of the parent container, the widget matches the container width.

## Returns

- (datetime.datetime or None) The current value of the datetime input widget (without timezone) or None if no value has been selected.

## Examples

### Example 1: Basic usage

```jsx
import datetime
import streamlit as st

event_time = st.datetime_input(
    "Schedule your event",
    datetime.datetime(2025, 11, 19, 16, 45),
)
st.write("Event scheduled for", event_time)
```

### Example 2: Empty initial value

To initialize an empty datetime input, use None as the value:

```jsx
import datetime
import streamlit as st

event_time = st.datetime_input("Schedule your event", value=None)
st.write("Event scheduled for", event_time)
```

## Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

## Footer

© 2025 Snowflake Inc.