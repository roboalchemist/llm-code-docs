# Source: https://docs.streamlit.io/develop/concepts/architecture/session-state

# Add statefulness to apps

## What is State?

We define access to a Streamlit app in a browser tab as a **session**. For each browser tab that connects to the Streamlit server, a new session is created. Streamlit reruns your script from top to bottom every time you interact with your app. Each rerun takes place in a blank slate: no variables are shared between runs.

Session State is a way to share variables between reruns, for each user session. In addition to the ability to store and persist state, Streamlit also exposes the ability to manipulate state using Callbacks. Session state also persists across pages inside a [multipage app](/develop/concepts/multipage-apps).

In this guide, we will illustrate the usage of **Session State** and **Callbacks** as we build a stateful Counter app.

## Example 1: Add Session State

Now that we've got a hang of the Session State API, let's update our Counter app to use Session State:

```python
import streamlit as st

if 'count' not in st.session_state:
    # set the initial default value of the slider widget
    st.session_state.celsius = 50.0

st.slider(
    "Temperature in Celsius",
    min_value=-100.0,
    max_value=100.0,
    key="celsius"
)

# This will get the value of the slider widget
st.write(st.session_state.celsius)
```

There is a limitation to setting widget values using the Session State API.

Streamlit does not allow setting widget values via the Session State API for `st.button` and `st.file_uploader`.

The following example will raise a `StreamlitAPIException` on trying to set the state of `st.button` via the Session State API:

```python
import streamlit as st

if 'my_button' not in st.session_state:
    st.session_state.my_button = True
    # Streamlit will raise an Exception on trying to set the state of button
    st.button('Submit', key='my_button')
```

## Serializable Session State

Serialization refers to the process of converting an object or data structure into a format that can be persisted and shared, and allowing you to recover the data’s original structure. Python’s built-in [pickle](https://docs.python.org/3/library/pickle.html) module serializes Python objects to a byte stream ("pickling") and deserializes the stream into an object ("unpickling").

By default, Streamlit’s [Session State](/develop/concepts/architecture/session-state) allows you to persist any Python object for the duration of the session, irrespective of the object’s pickle-serializability. This property lets you store Python primitives such as integers, floating-point numbers, complex numbers and booleans, dataframes, and even [lambdas](https://docs.python.org/3/reference/expressions.html#lambda) returned by functions. However, some execution environments may require serializing all data in Session State, so it may be useful to detect incompatibility during development, or when the execution environment will stop supporting it in the future.

To that end, Streamlit provides a `runner.enforceSerializableSessionState` [configuration option](/develop/concepts/configuration) that, when set to `true`, only allows pickle-serializable objects in Session State. To enable the option, either create a global or project config file with the following or use it as a command-line flag:

```toml
# .streamlit/config.toml
[runner]
enforceSerializableSessionState = true
```

By "pickle-serializable", we mean calling `pickle.dumps(obj)` should not raise a [PicklingError](https://docs.python.org/3/library/pickle.html#pickle.PicklingError) exception. When the config option is enabled, adding unserializable data to session state should result in an exception. E.g.,

```python
import streamlit as st

def unserializable_data():
    return lambda x: x

# 👇 results in an exception when enforceSerializableSessionState is on
st.session_state.unserializable = unserializable_data()
```

When `runner.enforceSerializableSessionState` is set to `true`, Session State implicitly uses the `pickle` module, which is known to be insecure. Ensure all data saved and retrieved from Session State is trusted because it is possible to construct malicious pickle data that will execute arbitrary code during unpickling. Never load data that could have come from an untrusted source in an unsafe mode or that could have been tampered with. **Only load data you trust**.

## Caveats and limitations

Here are some limitations to keep in mind when using Session State:

- Session State exists for as long as the tab is open and connected to the Streamlit server. As soon as you close the tab, everything stored in Session State is lost.
- Session State is not persisted. If the Streamlit server crashes, then everything stored in Session State gets wiped.
- For caveats and limitations with the Session State API, please see the [API limitations](/develop/api-reference/caching-and-state/st.session_state#caveats-and-limitations).

## Previous and Next Links

- [Previous: Caching](/develop/concepts/architecture/caching)
- [Next: Forms](/develop/concepts/architecture/forms)