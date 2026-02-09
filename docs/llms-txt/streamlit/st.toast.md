# Source: https://docs.streamlit.io/develop/api-reference/status/st.toast

# st.toast

Display a short message, known as a notification "toast".

The toast appears in the app's top-right corner and disappears after four seconds.

## Warning

`st.toast` is not compatible with Streamlit's [caching](https://docs.streamlit.io/develop/concepts/architecture/caching) and cannot be called within a cached function.

## Examples

### Example 1: Show a toast message

```python
import streamlit as st

st.toast("Your edited image was saved!", icon="😍")
```

### Example 2: Show multiple toasts

When multiple toasts are generated, they will stack. Hovering over a toast will stop it from disappearing. When hovering ends, the toast will disappear after time specified in `duration`.

```python
import time
import streamlit as st

if st.button("Three cheers"):
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hooray!", icon="🎉")
```

### Example 3: Update a toast message

Toast messages can also be updated. Assign `st.toast(my_message)` to a variable and use the `.toast()` method to update it. If a toast has already disappeared or been dismissed, the update will not be seen.

```python
import time
import streamlit as st

def cook_breakfast():
    msg = st.toast("Gathering ingredients...")
    time.sleep(1)
    msg.toast("Cooking...")
    time.sleep(1)
    msg.toast("Ready!", icon="🥞")

if st.button("Cook breakfast"):
    cook_breakfast()
```

## Streamlit Version

Version 1.52.0

## Notes

Streamlit Version

## Version From Slug

## Platform From Slug

## Menu

### Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

### Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Status elements](/develop/api-reference/status)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

### Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/develop/tutorials)

### Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## st.toast

Display a short message, known as a notification "toast".

The toast appears in the app's top-right corner and disappears after four seconds.

### Example 1: Show a toast message

```python
import streamlit as st

st.toast("Your edited image was saved!", icon="😍")
```

### Example 2: Show multiple toasts

When multiple toasts are generated, they will stack. Hovering over a toast will stop it from disappearing. When hovering ends, the toast will disappear after time specified in `duration`.

```python
import time
import streamlit as st

if st.button("Three cheers"):
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hooray!", icon="🎉")
```

### Example 3: Update a toast message

Toast messages can also be updated. Assign `st.toast(my_message)` to a variable and use the `.toast()` method to update it. If a toast has already disappeared or been dismissed, the update will not be seen.

```python
import time
import streamlit as st

def cook_breakfast():
    msg = st.toast("Gathering ingredients...")
    time.sleep(1)
    msg.toast("Cooking...")
    time.sleep(1)
    msg.toast("Ready!", icon="🥞")

if st.button("Cook breakfast"):
    cook_breakfast()
```

## st.toast

Display a short message, known as a notification "toast".

The toast appears in the app's top-right corner and disappears after four seconds.

### Example 1: Show a toast message

```python
import streamlit as st

st.toast("Your edited image was saved!", icon="😍")
```

### Example 2: Show multiple toasts

When multiple toasts are generated, they will stack. Hovering over a toast will stop it from disappearing. When hovering ends, the toast will disappear after time specified in `duration`.

```python
import time
import streamlit as st

if st.button("Three cheers"):
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hooray!", icon="🎉")
```

### Example 3: Update a toast message

Toast messages can also be updated. Assign `st.toast(my_message)` to a variable and use the `.toast()` method to update it. If a toast has already disappeared or been dismissed, the update will not be seen.

```python
import time
import streamlit as st

def cook_breakfast():
    msg = st.toast("Gathering ingredients...")
    time.sleep(1)
    msg.toast("Cooking...")
    time.sleep(1)
    msg.toast("Ready!", icon="🥞")

if st.button("Cook breakfast"):
    cook_breakfast()
```

## st.toast

Display a short message, known as a notification "toast".

The toast appears in the app's top-right corner and disappears after four seconds.

### Example 1: Show a toast message

```python
import streamlit as st

st.toast("Your edited image was saved!", icon="😍")
```

### Example 2: Show multiple toasts

When multiple toasts are generated, they will stack. Hovering over a toast will stop it from disappearing. When hovering ends, the toast will disappear after time specified in `duration`.

```python
import time
import streamlit as st

if st.button("Three cheers"):
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hooray!", icon="🎉")
```

### Example 3: Update a toast message

Toast messages can also be updated. Assign `st.toast(my_message)` to a variable and use the `.toast()` method to update it. If a toast has already disappeared or been dismissed, the update will not be seen.

```python
import time
import streamlit as st

def cook_breakfast():
    msg = st.toast("Gathering ingredients...")
    time.sleep(1)
    msg.toast("Cooking...")
    time.sleep(1)
    msg.toast("Ready!", icon="🥞")

if st.button("Cook breakfast"):
    cook_breakfast()
```

## st.toast

Display a short message, known as a notification "toast".

The toast appears in the app's top-right corner and disappears after four seconds.

### Example 1: Show a toast message

```python
import streamlit as st

st.toast("Your edited image was saved!", icon="😍")
```

### Example 2: Show multiple toasts

When multiple toasts are generated, they will stack. Hovering over a toast will stop it from disappearing. When hovering ends, the toast will disappear after time specified in `duration`.

```python
import time
import streamlit as st

if st.button("Three cheers"):
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hooray!", icon="🎉")
```

### Example 3: Update a toast message

Toast messages can also be updated. Assign `st.toast(my_message)` to a variable and use the `.toast()` method to update it. If a toast has already disappeared or been dismissed, the update will not be seen.

```python
import time
import streamlit as st

def cook_breakfast():
    msg = st.toast("Gathering ingredients...")
    time.sleep(1)
    msg.toast("Cooking...")
    time.sleep(1)
    msg.toast("Ready!", icon="🥞")

if st.button("Cook breakfast"):
    cook_breakfast()
```

## st.toast

Display a short message, known as a notification "toast".

The toast appears in the app's top-right corner and disappears after four seconds.

### Example 1: Show a toast message

```python
import streamlit as st

st.toast("Your edited image was saved!", icon="😍")
```

### Example 2: Show multiple toasts

When multiple toasts are generated, they will stack. Hovering over a toast will stop it from disappearing. When hovering ends, the toast will disappear after time specified in `duration`.

```python
import time
import streamlit as st

if st.button("Three cheers"):
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hooray!", icon="🎉")
```

### Example 3: Update a toast message

Toast messages can also be updated. Assign `st.toast(my_message)` to a variable and use the `.toast()` method to update it. If a toast has already disappeared or been dismissed, the update will not be seen.

```python
import time
import streamlit as st

def cook_breakfast():
    msg = st.toast("Gathering ingredients...")
    time.sleep(1)
    msg.toast("Cooking...")
    time.sleep(1)
    msg.toast("Ready!", icon="🥞")

if st.button("Cook breakfast"):
    cook_breakfast()
```

## st.toast

Display a short message, known as a notification "toast".

The toast appears in the app's top-right corner and disappears after four seconds.

### Example 1: Show a toast message

```python
import streamlit as st

st.toast("Your edited image was saved!", icon="😍")
```

### Example 2: Show multiple toasts

When multiple toasts are generated, they will stack. Hovering over a toast will stop it from disappearing. When hovering ends, the toast will disappear after time specified in `duration`.

```python
import time
import streamlit as st

if st.button("Three cheers"):
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hooray!", icon="🎉")
```

### Example 3: Update a toast message

Toast messages can also be updated. Assign `st.toast(my_message)` to a variable and use the `.toast()` method to update it. If a toast has already disappeared or been dismissed, the update will not be seen.

```python
import time
import streamlit as st

def cook_breakfast():
    msg = st.toast("Gathering ingredients...")
    time.sleep(1)
    msg.toast("Cooking...")
    time.sleep(1)
    msg.toast("Ready!", icon="🥞")

if st.button("Cook breakfast"):
    cook_breakfast()
```

## st.toast

Display a short message, known as a notification "toast".

The toast appears in the app's top-right corner and disappears after four seconds.

### Example 1: Show a toast message

```python
import streamlit as st

st.toast("Your edited image was saved!", icon="😍")
```

### Example 2: Show multiple toasts

When multiple toasts are generated, they will stack. Hovering over a toast will stop it from disappearing. When hovering ends, the toast will disappear after time specified in `duration`.

```python
import time
import streamlit as st

if st.button("Three cheers"):
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hooray!", icon="🎉")
```

### Example 3: Update a toast message

Toast messages can also be updated. Assign `st.toast(my_message)` to a variable and use the `.toast()` method to update it. If a toast has already disappeared or been dismissed, the update will not be seen.

```python
import time
import streamlit as st

def cook_breakfast():
    msg = st.toast("Gathering ingredients...")
    time.sleep(1)
    msg.toast("Cooking...")
    time.sleep(1)
    msg.toast("Ready!", icon="🥞")

if st.button("Cook breakfast"):
    cook_breakfast()
```

## st.toast

Display a short message, known as a notification "toast".

The toast appears in the app's top-right corner and disappears after four seconds.

### Example 1: Show a toast message

```python
import streamlit as st

st.toast("Your edited image was saved!", icon="😍")
```

### Example 2: Show multiple toasts

When multiple toasts are generated, they will stack. Hovering over a toast will stop it from disappearing. When hovering ends, the toast will disappear after time specified in `duration`.

```python
import time
import streamlit as st

if st.button("Three cheers"):
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hooray!", icon="🎉")
```

### Example 3: Update a toast message

Toast messages can also be updated. Assign `st.toast(my_message)` to a variable and use the `.toast()` method to update it. If a toast has already disappeared or been dismissed, the update will not be seen.

```python
import time
import streamlit as st

def cook_breakfast():
    msg = st.toast("Gathering ingredients...")
    time.sleep(1)
    msg.toast("Cooking...")
    time.sleep(1)
    msg.toast("Ready!", icon="🥞")

if st.button("Cook breakfast"):
    cook_breakfast()
```

## st.toast

Display a short message, known as a notification "toast".

The toast appears in the app's top-right corner and disappears after four seconds.

### Example 1: Show a toast message

```python
import streamlit as st

st.toast("Your edited image was saved!", icon="😍")
```

### Example 2: Show multiple toasts

When multiple toasts are generated, they will stack. Hovering over a toast will stop it from disappearing. When hovering ends, the toast will disappear after time specified in `duration`.

```python
import time
import streamlit as st

if st.button("Three cheers"):
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hooray!", icon="🎉")
```

### Example 3: Update a toast message

Toast messages can also be updated. Assign `st.toast(my_message)` to a variable and use the `.toast()` method to update it. If a toast has already disappeared or been dismissed, the update will not be seen.

```python
import time
import streamlit as st

def cook_breakfast():
    msg = st.toast("Gathering ingredients...")
    time.sleep(1)
    msg.toast("Cooking...")
    time.sleep(1)
    msg.toast("Ready!", icon="🥞")

if st.button("Cook breakfast"):
    cook_breakfast()
```

## st.toast

Display a short message, known as a notification "toast".

The toast appears in the app's top-right corner and disappears after four seconds.

### Example 1: Show a toast message

```python
import streamlit as st

st.toast("Your edited image was saved!", icon="😍")
```

### Example 2: Show multiple toasts

When multiple toasts are generated, they will stack. Hovering over a toast will stop it from disappearing. When hovering ends, the toast will disappear after time specified in `duration`.

```python
import time
import streamlit as st

if st.button("Three cheers"):
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hooray!", icon="🎉")
```

### Example 3: Update a toast message

Toast messages can also be updated. Assign `st.toast(my_message)` to a variable and use the `.toast()` method to update it. If a toast has already disappeared or been dismissed, the update will not be seen.

```python
import time
import streamlit as st

def cook_breakfast():
    msg = st.toast("Gathering ingredients...")
    time.sleep(1)
    msg.toast("Cooking...")
    time.sleep(1)
    msg.toast("Ready!", icon="🥞")

if st.button("Cook breakfast"):
    cook_breakfast()
```

## st.toast

Display a short message, known as a notification "toast".

The toast appears in the app's top-right corner and disappears after four seconds.

### Example 1: Show a toast message

```python
import streamlit as st

st.toast("Your edited image was saved!", icon="😍")
```

### Example 2: Show multiple toasts

When multiple toasts are generated, they will stack. Hovering over a toast will stop it from disappearing. When hovering ends, the toast will disappear after time specified in `duration`.

```python
import time
import streamlit as st

if st.button("Three cheers"):
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hooray!", icon="🎉")
```

### Example 3: Update a toast message

Toast messages can also be updated. Assign `st.toast(my_message)` to a variable and use the `.toast()` method to update it. If a toast has already disappeared or been dismissed, the update will not be seen.

```python
import time
import streamlit as st

def cook_breakfast():
    msg = st.toast("Gathering ingredients...")
    time.sleep(1)
    msg.toast("Cooking...")
    time.sleep(1)
    msg.toast("Ready!", icon="🥞")

if st.button("Cook breakfast"):
    cook_breakfast()
```

## st.toast

Display a short message, known as a notification "toast".

The toast appears in the app's top-right corner and disappears after four seconds.

### Example 1: Show a toast message

```python
import streamlit as st

st.toast("Your edited image was saved!", icon="😍")
```

### Example 2: Show multiple toasts

When multiple toasts are generated, they will stack. Hovering over a toast will stop it from disappearing. When hovering ends, the toast will disappear after time specified in `duration`.

```python
import time
import streamlit as st

if st.button("Three cheers"):
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hooray!", icon="🎉")
```

### Example 3: Update a toast message

Toast messages can also be updated. Assign `st.toast(my_message)` to a variable and use the `.toast()` method to update it. If a toast has already disappeared or been dismissed, the update will not be seen.

```python
import time
import streamlit as st

def cook_breakfast():
    msg = st.toast("Gathering ingredients...")
    time.sleep(1)
    msg.toast("Cooking...")
    time.sleep(1)
    msg.toast("Ready!", icon="🥞")

if st.button("Cook breakfast"):
    cook_breakfast()
```

## st.toast

Display a short message, known as a notification "toast".

The toast appears in the app's top-right corner and disappears after four seconds.

### Example 1: Show a toast message

```python
import streamlit as st

st.toast("Your edited image was saved!", icon="😍")
```

### Example 2: Show multiple toasts

When multiple toasts are generated, they will stack. Hovering over a toast will stop it from disappearing. When hovering ends, the toast will disappear after time specified in `duration`.

```python
import time
import streamlit as st

if st.button("Three cheers"):
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hooray!", icon="🎉")
```

### Example 3: Update a toast message

Toast messages can also be updated. Assign `st.toast(my_message)` to a variable and use the `.toast()` method to update it. If a toast has already disappeared or been dismissed, the update will not be seen.

```python
import time
import streamlit as st

def cook_breakfast():
    msg = st.toast("Gathering ingredients...")
    time.sleep(1)
    msg.toast("Cooking...")
    time.sleep(1)
    msg.toast("Ready!", icon="🥞")

if st.button("Cook breakfast"):
    cook_breakfast()
```

## st.toast

Display a short message, known as a notification "toast".

The toast appears in the app's top-right corner and disappears after four seconds.

### Example 1: Show a toast message

```python
import streamlit as st

st.toast("Your edited image was saved!", icon="😍")
```

### Example 2: Show multiple toasts

When multiple toasts are generated, they will stack. Hovering over a toast will stop it from disappearing. When hovering ends, the toast will disappear after time specified in `duration`.

```python
import time
import streamlit as st

if st.button("Three cheers"):
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hooray!", icon="🎉")
```

### Example 3: Update a toast message

Toast messages can also be updated. Assign `st.toast(my_message)` to a variable and use the `.toast()` method to update it. If a toast has already disappeared or been dismissed, the update will not be seen.

```python
import time
import streamlit as st

def cook_breakfast():
    msg = st.toast("Gathering ingredients...")
    time.sleep(1)
    msg.toast("Cooking...")
    time.sleep(1)
    msg.toast("Ready!", icon="🥞")

if st.button("Cook breakfast"):
    cook_breakfast()
```

## st.toast

Display a short message, known as a notification "toast".

The toast appears in the app's top-right corner and disappears after four seconds.

### Example 1: Show a toast message

```python
import streamlit as st

st.toast("Your edited image was saved!", icon="😍")
```

### Example 2: Show multiple toasts

When multiple toasts are generated, they will stack. Hovering over a toast will stop it from disappearing. When hovering ends, the toast will disappear after time specified in `duration`.

```python
import time
import streamlit as st

if st.button("Three cheers"):
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hooray!", icon="🎉")
```

### Example 3: Update a toast message

Toast messages can also be updated. Assign `st.toast(my_message)` to a variable and use the `.toast()` method to update it. If a toast has already disappeared or been dismissed, the update will not be seen.

```python
import time
import streamlit as st

def cook_breakfast():
    msg = st.toast("Gathering ingredients...")
    time.sleep(1)
    msg.toast("Cooking...")
    time.sleep(1)
    msg.toast("Ready!", icon="🥞")

if st.button("Cook breakfast"):
    cook_breakfast()
```

## st.toast

Display a short message, known as a notification "toast".

The toast appears in the app's top-right corner and disappears after four seconds.

### Example 1: Show a toast message

```python
import streamlit as st

st.toast("Your edited image was saved!", icon="😍")
```

### Example 2: Show multiple toasts

When multiple toasts are generated, they will stack. Hovering over a toast will stop it from disappearing. When hovering ends, the toast will disappear after time specified in `duration`.

```python
import time
import streamlit as st

if st.button("Three cheers"):
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hooray!", icon="🎉")
```

### Example 3: Update a toast message

Toast messages can also be updated. Assign `st.toast(my_message)` to a variable and use the `.toast()` method to update it. If a toast has already disappeared or been dismissed, the update will not be seen.

```python
import time
import streamlit as st

def cook_breakfast():
    msg = st.toast("Gathering ingredients...")
    time.sleep(1)
    msg.toast("Cooking...")
    time.sleep(1)
    msg.toast("Ready!", icon="🥞")

if st.button("Cook breakfast"):
    cook_breakfast()
```

## st.toast

Display a short message, known as a notification "toast".

The toast appears in the app's top-right corner and disappears after four seconds.

### Example 1: Show a toast message

```python
import streamlit as st

st.toast("Your edited image was saved!", icon="😍")
```

### Example 2: Show multiple toasts

When multiple toasts are generated, they will stack. Hovering over a toast will stop it from disappearing. When hovering ends, the toast will disappear after time specified in `duration`.

```python
import time
import streamlit as st

if st.button("Three cheers"):
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hooray!", icon="🎉")
```

### Example 3: Update a toast message

Toast messages can also be updated. Assign `st.toast(my_message)` to a variable and use the `.toast()` method to update it. If a toast has already disappeared or been dismissed, the update will not be seen.

```python
import time
import streamlit as st

def cook_breakfast():
    msg = st.toast("Gathering ingredients...")
    time.sleep(1)
    msg.toast("Cooking...")
    time.sleep(1)
    msg.toast("Ready!", icon="🥞")

if st.button("Cook breakfast"):
    cook_breakfast()
```

## st.toast

Display a short message, known as a notification "toast".

The toast appears in the app's top-right corner and disappears after four seconds.

### Example 1: Show a toast message

```python
import streamlit as st

st.toast("Your edited image was saved!", icon="😍")
```

### Example 2: Show multiple toasts

When multiple toasts are generated, they will stack. Hovering over a toast will stop it from disappearing. When hovering ends, the toast will disappear after time specified in `duration`.

```python
import time
import streamlit as st

if st.button("Three cheers"):
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hooray!", icon="🎉")
```

### Example 3: Update a toast message

Toast messages can also be updated. Assign `st.toast(my_message)` to a variable and use the `.toast()` method to update it. If a toast has already disappeared or been dismissed, the update will not be seen.

```python
import time
import streamlit as st

def cook_breakfast():
    msg = st.toast("Gathering ingredients...")
    time.sleep(1)
    msg.toast("Cooking...")
    time.sleep(1)
    msg.toast("Ready!", icon="🥞")

if st.button("Cook breakfast"):
    cook_breakfast()
```

## st.toast

Display a short message, known as a notification "toast".

The toast appears in the app's top-right corner and disappears after four seconds.

### Example 1: Show a toast message

```python
import streamlit as st

st.toast("Your edited image was saved!", icon="😍")
```

### Example 2: Show multiple toasts

When multiple toasts are generated, they will stack. Hovering over a toast will stop it from disappearing. When hovering ends, the toast will disappear after time specified in `duration`.

```python
import time
import streamlit as st

if st.button("Three cheers"):
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hooray!", icon="🎉")
```

### Example 3: Update a toast message

Toast messages can also be updated. Assign `st.toast(my_message)` to a variable and use the `.toast()` method to update it. If a toast has already disappeared or been dismissed, the update will not be seen.

```python
import time
import streamlit as st

def cook_breakfast():
    msg = st.toast("Gathering ingredients...")
    time.sleep(1)
    msg.toast("Cooking...")
    time.sleep(1)
    msg.toast("Ready!", icon="🥞")

if st.button("Cook breakfast"):
    cook_breakfast()
```

## st.toast

Display a short message, known as a notification "toast".

The toast appears in the app's top-right corner and disappears after four seconds.

### Example 1: Show a toast message

```python
import streamlit as st

st.toast("Your edited image was saved!", icon="😍")
```

### Example 2: Show multiple toasts

When multiple toasts are generated, they will stack. Hovering over a toast will stop it from disappearing. When hovering ends, the toast will disappear after time specified in `duration`.

```python
import time
import streamlit as st

if st.button("Three cheers"):
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hooray!", icon="🎉")
```

### Example 3: Update a toast message

Toast messages can also be updated. Assign `st.toast(my_message)` to a variable and use the `.toast()` method to update it. If a toast has already disappeared or been dismissed, the update will not be seen.

```python
import time
import streamlit as st

def cook_breakfast():
    msg = st.toast("Gathering ingredients...")
    time.sleep(1)
    msg.toast("Cooking...")
    time.sleep(1)
    msg.toast("Ready!", icon="🥞")

if st.button("Cook breakfast"):
    cook_breakfast()
```

## st.toast

Display a short message, known as a notification "toast".

The toast appears in the app's top-right corner and disappears after four seconds.

### Example 1: Show a toast message

```python
import streamlit as st

st.toast("Your edited image was saved!", icon="😍")
```

### Example 2: Show multiple toasts

When multiple toasts are generated, they will stack. Hovering over a toast will stop it from disappearing. When hovering ends, the toast will disappear after time specified in `duration`.

```python
import time
import streamlit as st

if st.button("Three cheers"):
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hooray!", icon="🎉")
```

### Example 3: Update a toast message

Toast messages can also be updated. Assign `st.toast(my_message)` to a variable and use the `.toast()` method to update it. If a toast has already disappeared or been dismissed, the update will not be seen.

```python
import time
import streamlit as st

def cook_breakfast():
    msg = st.toast("Gathering ingredients...")
    time.sleep(1)
    msg.toast("Cooking...")
    time.sleep(1)
    msg.toast("Ready!", icon="🥞")

if st.button("Cook breakfast"):
    cook_breakfast()
```

## st.toast

Display a short message, known as a notification "toast".

The toast appears in the app's top-right corner and disappears after four seconds.

### Example 1: Show a toast message

```python
import streamlit as st

st.toast("Your edited image was saved!", icon="😍")
```

### Example 2: Show multiple toasts

When multiple toasts are generated, they will stack. Hovering over a toast will stop it from disappearing. When hovering ends, the toast will disappear after time specified in `duration`.

```python
import time
import streamlit as st

if st.button("Three cheers"):
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hooray!", icon="🎉")
```

### Example 3: Update a toast message

Toast messages can also be updated. Assign `st.toast(my_message)` to a variable and use the `.toast()` method to update it. If a toast has already disappeared or been dismissed, the update will not be seen.

```python
import time
import streamlit as st

def cook_breakfast():
    msg = st.toast("Gathering ingredients...")
    time.sleep(1)
    msg.toast("Cooking...")
    time.sleep(1)
    msg.toast("Ready!", icon="🥞")

if st.button("Cook breakfast"):
    cook_breakfast()
```

## st.toast

Display a short message, known as a notification "toast".

The toast appears in the app's top-right corner and disappears after four seconds.

### Example 1: Show a toast message

```python
import streamlit as st

st.toast("Your edited image was saved!", icon="😍")
```

### Example 2: Show multiple toasts

When multiple toasts are generated, they will stack. Hovering over a toast will stop it from disappearing. When hovering ends, the toast will disappear after time specified in `duration`.

```python
import time
import streamlit as st

if st.button("Three cheers"):
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hooray!", icon="🎉")
```

### Example 3: Update a toast message

Toast messages can also be updated. Assign `st.toast(my_message)` to a variable and use the `.toast()` method to update it. If a toast has already disappeared or been dismissed, the update will not be seen.

```python
import time
import streamlit as st

def cook_breakfast():
    msg = st.toast("Gathering ingredients...")
    time.sleep(1)
    msg.toast("Cooking...")
    time.sleep(1)
    msg.toast("Ready!", icon="🥞")

if st.button("Cook breakfast"):
    cook_breakfast()
```

## st.toast

Display a short message, known as a notification "toast".

The toast appears in the app's top-right corner and disappears after four seconds.

### Example 1: Show a toast message

```python
import streamlit as st

st.toast("Your edited image was saved!", icon="😍")
```

### Example 2: Show multiple toasts

When multiple toasts are generated, they will stack. Hovering over a toast will stop it from disappearing. When hovering ends, the toast will disappear after time specified in `duration`.

```python
import time
import streamlit as st

if st.button("Three cheers"):
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hooray!", icon="🎉")
```

### Example 3: Update a toast message

Toast messages can also be updated. Assign `st.toast(my_message)` to a variable and use the `.toast()` method to update it. If a toast has already disappeared or been dismissed, the update will not be seen.

```python
import time
import streamlit as st

def cook_breakfast():
    msg = st.toast("Gathering ingredients...")
    time.sleep(1)
    msg.toast("Cooking...")
    time.sleep(1)
    msg.toast("Ready!", icon="🥞")

if st.button("Cook breakfast"):
    cook_breakfast()
```

## st.toast

Display a short message, known as a notification "toast".

The toast appears in the app's top-right corner and disappears after four seconds.

### Example 1: Show a toast message

```python
import streamlit as st

st.toast("Your edited image was saved!", icon="😍")
```

### Example 2: Show multiple toasts

When multiple toasts are generated, they will stack. Hovering over a toast will stop it from disappearing. When hovering ends, the toast will disappear after time specified in `duration`.

```python
import time
import streamlit as st

if st.button("Three cheers"):
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hooray!", icon="🎉")
```

### Example 3: Update a toast message

Toast messages can also be updated. Assign `st.toast(my_message)` to a variable and use the `.toast()` method to update it. If a toast has already disappeared or been dismissed, the update will not be seen.

```python
import time
import streamlit as st

def cook_breakfast():
    msg = st.toast("Gathering ingredients...")
    time.sleep(1)
    msg.toast("Cooking...")
    time.sleep(1)
    msg.toast("Ready!", icon="🥞")

if st.button("Cook breakfast"):
    cook_breakfast()
```

## st.toast

Display a short message, known as a notification "toast".

The toast appears in the app's top-right corner and disappears after four seconds.

### Example 1: Show a toast message

```python
import streamlit as st

st.toast("Your edited image was saved!", icon="😍")
```

### Example 2: Show multiple toasts

When multiple toasts are generated, they will stack. Hovering over a toast will stop it from disappearing. When hovering ends, the toast will disappear after time specified in `duration`.

```python
import time
import streamlit as st

if st.button("Three cheers"):
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hip!")
    time