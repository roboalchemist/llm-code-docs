# Widget behavior

Widgets (like `st.button`, `st.selectbox`, and `st.text_input`) are at the heart of Streamlit apps. They are the interactive elements of Streamlit that pass information from your users into your Python code. Widgets are magical and often work how you want, but they can have surprising behavior in some situations. Understanding the different parts of a widget and the precise order in which events occur helps you achieve your desired results.

This guide covers advanced concepts about widgets. Generally, it begins with simpler concepts and increases in complexity. For most beginning users, these details won't be important to know right away. When you want to dynamically change widgets or preserve widget information between pages, these concepts will be important to understand. We recommend having a basic understanding of [Session State](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state) before reading this guide.

## 🎈 TL;DR

1. The actions of one user do not affect the widgets of any other user.
2. A widget command returns the widget's current value, which is a simple Python type. For example, `st.button` returns a boolean value.
3. Widgets return their default values on their first call before a user interacts with them.
4. A widget's identity depends on the arguments passed to the widget command. **If a key is provided, only the key determines the widget's identity, with some limitations as this is still being implemented.** If no key is provided, changing a widget's label, min or max value, default value, placeholder text, or help text will cause it to reset.
5. If you don't call a widget command in a script run, Streamlit will delete the widget's information—_including its key-value pair in Session State_. If you call the same widget command later, Streamlit treats it as a new widget.
6. Widgets are not stateful between pages. If you have two widgets with the same key on different pages, they will be treated as two different widgets.

The last three points are the most relevant when dynamically changing widgets or working with multi-page applications. This is covered in detail later in this guide: [Statefulness of widgets](#statefulness-of-widgets) and [Widget life cycle](#widget-life-cycle).

## 📢 For multipage apps

**Primary recommendation:** Use common widgets in the entrypoint file with [st.navigation](https://docs.streamlit.io/develop/api-reference/navigation/st.navigation) to bypass page identity issues entirely:

```python
# streamlit_app.py (entrypoint)
import streamlit as st

# Common widgets that persist across all pages
user_name = st.sidebar.text_input("Name", key="global_name")
user_role = st.sidebar.selectbox("Role", ["User", "Admin"], key="global_role")

# Navigation
page = st.navigation([
    st.Page("page1.py", title="Dashboard"),
    st.Page("page2.py", title="Settings"),
])
page.run()
```

**Secondary recommendation:** For widgets that must be on individual pages, use the placeholder key pattern. See [Save widget values in Session State to preserve them between pages](#save-widget-values-in-session-state-to-preserve-them-between-pages) for more information.

## 📢 For parameter changes

- Use keys when you need widgets to maintain state despite parameter changes.
- If you need to change a parameter that affects a widget's identity, use placeholder keys like you would for multipage apps, or use a callback to directly maintain a widget's state. For more information, see [Retain statefulness when changing a widget's identity](#retain-statefulness-when-changing-a-widgets-identity).
- To force a widget to reset, update its key, or update a parameter without using a key.

## 📢 Best practices and recommendations

### For multipage apps

**Primary recommendation:** Use common widgets in the entrypoint file with [st.navigation](https://docs.streamlit.io/develop/api-reference/navigation/st.navigation) to bypass page identity issues entirely:

```python
# streamlit_app.py (entrypoint)
import streamlit as st

# Common widgets that persist across all pages
user_name = st.sidebar.text_input("Name", key="global_name")
user_role = st.sidebar.selectbox("Role", ["User", "Admin"], key="global_role")

# Navigation
page = st.navigation([
    st.Page("page1.py", title="Dashboard"),
    st.Page("page2.py", title="Settings"),
])
page.run()
```

**Secondary recommendation:** For widgets that must be on individual pages, use the placeholder key pattern. See [Save widget values in Session State to preserve them between pages](#save-widget-values-in-session-state-to-preserve-them-between-pages) for more information.

### For parameter changes

- Use keys when you need widgets to maintain state despite parameter changes.
- If you need to change a parameter that affects a widget's identity, use placeholder keys like you would for multipage apps, or use a callback to directly maintain a widget's state. For more information, see [Retain statefulness when changing a widget's identity](#retain-statefulness-when-changing-a-widgets-identity).
- To force a widget to reset, update its key, or update a parameter without using a key.

## 📢 Statefulness of widgets

As long as the widget identity remains the same and that widget is continuously rendered on the frontend, then it will be stateful and remember user input.

- **Primary recommendation:** Use common widgets in the entrypoint file with [st.navigation](https://docs.streamlit.io/develop/api-reference/navigation/st.navigation) to bypass page identity issues entirely:

```python
# streamlit_app.py (entrypoint)
import streamlit as st

# Common widgets that persist across all pages
user_name = st.sidebar.text_input("Name", key="global_name")
user_role = st.sidebar.selectbox("Role", ["User", "Admin"], key="global_role")

# Navigation
page = st.navigation([
    st.Page("page1.py", title="Dashboard"),
    st.Page("page2.py", title="Settings"),
])
page.run()
```

- **Secondary recommendation:** For widgets that must be on individual pages, use the placeholder key pattern. See [Save widget values in Session State to preserve them between pages](#save-widget-values-in-session-state-to-preserve-them-between-pages) for more information.

## 📢 Widget life cycle

When a widget command is called, Streamlit will check if it already has a widget with the same identity. Streamlit will reconnect if it thinks the widget already exists. Otherwise, it will make a new one.

- **Primary recommendation:** Use common widgets in the entrypoint file with [st.navigation](https://docs.streamlit.io/develop/api-reference/navigation/st.navigation) to bypass page identity issues entirely:

```python
# streamlit_app.py (entrypoint)
import streamlit as st

# Common widgets that persist across all pages
user_name = st.sidebar.text_input("Name", key="global_name")
user_role = st.sidebar.selectbox("Role", ["User", "Admin"], key="global_role")

# Navigation
page = st.navigation([
    st.Page("page1.py", title="Dashboard"),
    st.Page("page2.py", title="Settings"),
])
page.run()
```

- **Secondary recommendation:** For widgets that must be on individual pages, use the placeholder key pattern. See [Save widget values in Session State to preserve them between pages](#save-widget-values-in-session-state-to-preserve-them-between-pages) for more information.

## 📢 For multipage apps

**Primary recommendation:** Use common widgets in the entrypoint file with [st.navigation](https://docs.streamlit.io/develop/api-reference/navigation/st.navigation) to bypass page identity issues entirely:

```python
# streamlit_app.py (entrypoint)
import streamlit as st

# Common widgets that persist across all pages
user_name = st.sidebar.text_input("Name", key="global_name")
user_role = st.sidebar.selectbox("Role", ["User", "Admin"], key="global_role")

# Navigation
page = st.navigation([
    st.Page("page1.py", title="Dashboard"),
    st.Page("page2.py", title="Settings"),
])
page.run()
```

**Secondary recommendation:** For widgets that must be on individual pages, use the placeholder key pattern. See [Save widget values in Session State to preserve them between pages](#save-widget-values-in-session-state-to-preserve-them-between-pages) for more information.

## 📢 For parameter changes

- Use keys when you need widgets to maintain state despite parameter changes.
- If you need to change a parameter that affects a widget's identity, use placeholder keys like you would for multipage apps, or use a callback to directly maintain a widget's state. For more information, see [Retain statefulness when changing a widget's identity](#retain-statefulness-when-changing-a-widgets-identity).
- To force a widget to reset, update its key, or update a parameter without using a key.

## 📢 Best practices and recommendations

### For multipage apps

**Primary recommendation:** Use common widgets in the entrypoint file with [st.navigation](https://docs.streamlit.io/develop/api-reference/navigation/st.navigation) to bypass page identity issues entirely:

```python
# streamlit_app.py (entrypoint)
import streamlit as st

# Common widgets that persist across all pages
user_name = st.sidebar.text_input("Name", key="global_name")
user_role = st.sidebar.selectbox("Role", ["User", "Admin"], key="global_role")

# Navigation
page = st.navigation([
    st.Page("page1.py", title="Dashboard"),
    st.Page("page2.py", title="Settings"),
])
page.run()
```

**Secondary recommendation:** For widgets that must be on individual pages, use the placeholder key pattern. See [Save widget values in Session State to preserve them between pages](#save-widget-values-in-session-state-to-preserve-them-between-pages) for more information.

### For parameter changes

- Use keys when you need widgets to maintain state despite parameter changes.
- If you need to change a parameter that affects a widget's identity, use placeholder keys like you would for multipage apps, or use a callback to directly maintain a widget's state. For more information, see [Retain statefulness when changing a widget's identity](#retain-statefulness-when-changing-a-widgets-identity).
- To force a widget to reset, update its key, or update a parameter without using a key.

## 📢 Statefulness of widgets

As long as the widget identity remains the same and that widget is continuously rendered on the frontend, then it will be stateful and remember user input.

- **Primary recommendation:** Use common widgets in the entrypoint file with [st.navigation](https://docs.streamlit.io/develop/api-reference/navigation/st.navigation) to bypass page identity issues entirely:

```python
# streamlit_app.py (entrypoint)
import streamlit as st

# Common widgets that persist across all pages
user_name = st.sidebar.text_input("Name", key="global_name")
user_role = st.sidebar.selectbox("Role", ["User", "Admin"], key="global_role")

# Navigation
page = st.navigation([
    st.Page("page1.py", title="Dashboard"),
    st.Page("page2.py", title="Settings"),
])
page.run()
```

- **Secondary recommendation:** For widgets that must be on individual pages, use the placeholder key pattern. See [Save widget values in Session State to preserve them between pages](#save-widget-values-in-session-state-to-preserve-them-between-pages) for more information.

## 📢 Widget life cycle

When a widget command is called, Streamlit will check if it already has a widget with the same identity. Streamlit will reconnect if it thinks the widget already exists. Otherwise, it will make a new one.

- **Primary recommendation:** Use common widgets in the entrypoint file with [st.navigation](https://docs.streamlit.io/develop/api-reference/navigation/st.navigation) to bypass page identity issues entirely:

```python
# streamlit_app.py (entrypoint)
import streamlit as st

# Common widgets that persist across all pages
user_name = st.sidebar.text_input("Name", key="global_name")
user_role = st.sidebar.selectbox("Role", ["User", "Admin"], key="global_role")

# Navigation
page = st.navigation([
    st.Page("page1.py", title="Dashboard"),
    st.Page("page2.py", title="Settings"),
])
page.run()
```

- **Secondary recommendation:** For widgets that must be on individual pages, use the placeholder key pattern. See [Save widget values in Session State to preserve them between pages](#save-widget-values-in-session-state-to-preserve-them-between-pages) for more information.

## 📢 For multipage apps

**Primary recommendation:** Use common widgets in the entrypoint file with [st.navigation](https://docs.streamlit.io/develop/api-reference/navigation/st.navigation) to bypass page identity issues entirely:

```python
# streamlit_app.py (entrypoint)
import streamlit as st

# Common widgets that persist across all pages
user_name = st.sidebar.text_input("Name", key="global_name")
user_role = st.sidebar.selectbox("Role", ["User", "Admin"], key="global_role")

# Navigation
page = st.navigation([
    st.Page("page1.py", title="Dashboard"),
    st.Page("page2.py", title="Settings"),
])
page.run()
```

**Secondary recommendation:** For widgets that must be on individual pages, use the placeholder key pattern. See [Save widget values in Session State to preserve them between pages](#save-widget-values-in-session-state-to-preserve-them-between-pages) for more information.

## 📢 For parameter changes

- Use keys when you need widgets to maintain state despite parameter changes.
- If you need to change a parameter that affects a widget's identity, use placeholder keys like you would for multipage apps, or use a callback to directly maintain a widget's state. For more information, see [Retain statefulness when changing a widget's identity](#retain-statefulness-when-changing-a-widgets-identity).
- To force a widget to reset, update its key, or update a parameter without using a key.

## 📢 Best practices and recommendations

### For multipage apps

**Primary recommendation:** Use common widgets in the entrypoint file with [st.navigation](https://docs.streamlit.io/develop/api-reference/navigation/st.navigation) to bypass page identity issues entirely:

```python
# streamlit_app.py (entrypoint)
import streamlit as st

# Common widgets that persist across all pages
user_name = st.sidebar.text_input("Name", key="global_name")
user_role = st.sidebar.selectbox("Role", ["User", "Admin"], key="global_role")

# Navigation
page = st.navigation([
    st.Page("page1.py", title="Dashboard"),
    st.Page("page2.py", title="Settings"),
])
page.run()
```

**Secondary recommendation:** For widgets that must be on individual pages, use the placeholder key pattern. See [Save widget values in Session State to preserve them between pages](#save-widget-values-in-session-state-to-preserve-them-between-pages) for more information.

### For parameter changes

- Use keys when you need widgets to maintain state despite parameter changes.
- If you need to change a parameter that affects a widget's identity, use placeholder keys like you would for multipage apps, or use a callback to directly maintain a widget's state. For more information, see [Retain statefulness when changing a widget's identity](#retain-statefulness-when-changing-a-widgets-identity).
- To force a widget to reset, update its key, or update a parameter without using a key.

## 📢 Statefulness of widgets

As long as the widget identity remains the same and that widget is continuously rendered on the frontend, then it will be stateful and remember user input.

- **Primary recommendation:** Use common widgets in the entrypoint file with [st.navigation](https://docs.streamlit.io/develop/api-reference/navigation/st.navigation) to bypass page identity issues entirely:

```python
# streamlit_app.py (entrypoint)
import streamlit as st

# Common widgets that persist across all pages
user_name = st.sidebar.text_input("Name", key="global_name")
user_role = st.sidebar.selectbox("Role", ["User", "Admin"], key="global_role")

# Navigation
page = st.navigation([
    st.Page("page1.py", title="Dashboard"),
    st.Page("page2.py", title="Settings"),
])
page.run()
```

- **Secondary recommendation:** For widgets that must be on individual pages, use the placeholder key pattern. See [Save widget values in Session State to preserve them between pages](#save-widget-values-in-session-state-to-preserve-them-between-pages) for more information.

## 📢 Widget life cycle

When a widget command is called, Streamlit will check if it already has a widget with the same identity. Streamlit will reconnect if it thinks the widget already exists. Otherwise, it will make a new one.

- **Primary recommendation:** Use common widgets in the entrypoint file with [st.navigation](https://docs.streamlit.io/develop/api-reference/navigation/st.navigation) to bypass page identity issues entirely:

```python
# streamlit_app.py (entrypoint)
import streamlit as st

# Common widgets that persist across all pages
user_name = st.sidebar.text_input("Name", key="global_name")
user_role = st.sidebar.selectbox("Role", ["User", "Admin"], key="global_role")

# Navigation
page = st.navigation([
    st.Page("page1.py", title="Dashboard"),
    st.Page("page2.py", title="Settings"),
])
page.run()
```

- **Secondary recommendation:** For widgets that must be on individual pages, use the placeholder key pattern. See [Save widget values in Session State to preserve them between pages](#save-widget-values-in-session-state-to-preserve-them-between-pages) for more information.

## 📢 For multipage apps

**Primary recommendation:** Use common widgets in the entrypoint file with [st.navigation](https://docs.streamlit.io/develop/api-reference/navigation/st.navigation) to bypass page identity issues entirely:

```python
# streamlit_app.py (entrypoint)
import streamlit as st

# Common widgets that persist across all pages
user_name = st.sidebar.text_input("Name", key="global_name")
user_role = st.sidebar.selectbox("Role", ["User", "Admin"], key="global_role")

# Navigation
page = st.navigation([
    st.Page("page1.py", title="Dashboard"),
    st.Page("page2.py", title="Settings"),
])
page.run()
```

**Secondary recommendation:** For widgets that must be on individual pages, use the placeholder key pattern. See [Save widget values in Session State to preserve them between pages](#save-widget-values-in-session-state-to-preserve-them-between-pages) for more information.

## 📢 For parameter changes

- Use keys when you need widgets to maintain state despite parameter changes.
- If you need to change a parameter that affects a widget's identity, use placeholder keys like you would for multipage apps, or use a callback to directly maintain a widget's state. For more information, see [Retain statefulness when changing a widget's identity](#retain-statefulness-when-changing-a-widgets-identity).
- To force a widget to reset, update its key, or update a parameter without using a key.

## 📢 Best practices and recommendations

### For multipage apps

**Primary recommendation:** Use common widgets in the entrypoint file with [st.navigation](https://docs.streamlit.io/develop/api-reference/navigation/st.navigation) to bypass page identity issues entirely:

```python
# streamlit_app.py (entrypoint)
import streamlit as st

# Common widgets that persist across all pages
user_name = st.sidebar.text_input("Name", key="global_name")
user_role = st.sidebar.selectbox("Role", ["User", "Admin"], key="global_role")

# Navigation
page = st.navigation([
    st.Page("page1.py", title="Dashboard"),
    st.Page("page2.py", title="Settings"),
])
page.run()
```

**Secondary recommendation:** For widgets that must be on individual pages, use the placeholder key pattern. See [Save widget values in Session State to preserve them between pages](#save-widget-values-in-session-state-to-preserve-them-between-pages) for more information.

### For parameter changes

- Use keys when you need widgets to maintain state despite parameter changes.
- If you need to change a parameter that affects a widget's identity, use placeholder keys like you would for multipage apps, or use a callback to directly maintain a widget's state. For more information, see [Retain statefulness when changing a widget's identity](#retain-statefulness-when-changing-a-widgets-identity).
- To force a widget to reset, update its key, or update a parameter without using a key.

## 📢 Statefulness of widgets

As long as the widget identity remains the same and that widget is continuously rendered on the frontend, then it will be stateful and remember user input.

- **Primary recommendation:** Use common widgets in the entrypoint file with [st.navigation](https://docs.streamlit.io/develop/api-reference/navigation/st.navigation) to bypass page identity issues entirely:

```python
# streamlit_app.py (entrypoint)
import streamlit as st

# Common widgets that persist across all pages
user_name = st.sidebar.text_input("Name", key="global_name")
user_role = st.sidebar.selectbox("Role", ["User", "Admin"], key="global_role")

# Navigation
page = st.navigation([
    st.Page("page1.py", title="Dashboard"),
    st.Page("page2.py", title="Settings"),
])
page.run()
```

- **Secondary recommendation:** For widgets that must be on individual pages, use the placeholder key pattern. See [Save widget values in Session State to preserve them between pages](#save-widget-values-in-session-state-to-preserve-them-between-pages) for more information.

## 📢 Widget life cycle

When a widget command is called, Streamlit will check if it already has a widget with the same identity. Streamlit will reconnect if it thinks the widget already exists. Otherwise, it will make a new one.

- **Primary recommendation:** Use common widgets in the entrypoint file with [st.navigation](https://docs.streamlit.io/develop/api-reference/navigation/st.navigation) to bypass page identity issues entirely:

```python
# streamlit_app.py (entrypoint)
import streamlit as st

# Common widgets that persist across all pages
user_name = st.sidebar.text_input("Name", key="global_name")
user_role = st.sidebar.selectbox("Role", ["User", "Admin"], key="global_role")

# Navigation
page = st.navigation([
    st.Page("page1.py", title="Dashboard"),
    st.Page("page2.py", title="Settings"),
])
page.run()
```

- **Secondary recommendation:** For widgets that must be on individual pages, use the placeholder key pattern. See [Save widget values in Session State to preserve them between pages](#save-widget-values-in-session-state-to-preserve-them-between-pages) for more information.

## 📢 For multipage apps

**Primary recommendation:** Use common widgets in the entrypoint file with [st.navigation](https://docs.streamlit.io/develop/api-reference/navigation/st.navigation) to bypass page identity issues entirely:

```python
# streamlit_app.py (entrypoint)
import streamlit as st

# Common widgets that persist across all pages
user_name = st.sidebar.text_input("Name", key="global_name")
user_role = st.sidebar.selectbox("Role", ["User", "Admin"], key="global_role")

# Navigation
page = st.navigation([
    st.Page("page1.py", title="Dashboard"),
    st.Page("page2.py", title="Settings"),
])
page.run()
```

**Secondary recommendation:** For widgets that must be on individual pages, use the placeholder key pattern. See [Save widget values in Session State to preserve them between pages](#save-widget-values-in-session-state-to-preserve-them-between-pages) for more information.

## 📢 For parameter changes

- Use keys when you need widgets to maintain state despite parameter changes.
- If you need to change a parameter that affects a widget's identity, use placeholder keys like you would for multipage apps, or use a callback to directly maintain a widget's state. For more information, see [Retain statefulness when changing a widget's identity](#retain-statefulness-when-changing-a-widgets-identity).
- To force a widget to reset, update its key, or update a parameter without using a key.

## 📢 Best practices and recommendations

### For multipage apps

**Primary recommendation:** Use common widgets in the entrypoint file with [st.navigation](https://docs.streamlit.io/develop/api-reference/navigation/st.navigation) to bypass page identity issues entirely:

```python
# streamlit_app.py (entrypoint)
import streamlit as st

# Common widgets that persist across all pages
user_name = st.sidebar.text_input("Name", key="global_name")
user_role = st.sidebar.selectbox("Role", ["User", "Admin"], key="global_role")

# Navigation
page = st.navigation([
    st.Page("page1.py", title="Dashboard"),
    st.Page("page2.py", title="Settings"),
])
page.run()
```

**Secondary recommendation:** For widgets that must be on individual pages, use the placeholder key pattern. See [Save widget values in Session State to preserve them between pages](#save-widget-values-in-session-state-to-preserve-them-between-pages) for more information.

### For parameter changes

- Use keys when you need widgets to maintain state despite parameter changes.
- If you need to change a parameter that affects a widget's identity, use placeholder keys like you would for multipage apps, or use a callback to directly maintain a widget's state. For more information, see [Retain statefulness when changing a widget's identity](#retain-statefulness-when-changing-a-widgets-identity).
- To force a widget to reset, update its key, or update a parameter without using a key.

## 📢 Statefulness of widgets

As long as the widget identity remains the same and that widget is continuously rendered on the frontend, then it will be stateful and remember user input.

- **Primary recommendation:** Use common widgets in the entrypoint file with [st.navigation](https://docs.streamlit.io/develop/api-reference/navigation/st.navigation) to bypass page identity issues entirely:

```python
# streamlit_app.py (entrypoint)
import streamlit as st

# Common widgets that persist across all pages
user_name = st.sidebar.text_input("Name", key="global_name")
user_role = st.sidebar.selectbox("Role", ["User", "Admin"], key="global_role")

# Navigation
page = st.navigation([
    st.Page("page1.py", title="Dashboard"),
    st.Page("page2.py", title="Settings"),
])
page.run()
```

- **Secondary recommendation:** For widgets that must be on individual pages, use the placeholder key pattern. See [Save widget values in Session State to preserve them between pages](#save-widget-values-in-session-state-to-preserve-them-between-pages) for more information.

## 📢 Widget life cycle

When a widget command is called, Streamlit will check if it already has a widget with the same identity. Streamlit will reconnect if it thinks the widget already exists. Otherwise, it will make a new one.

- **Primary recommendation:** Use common widgets in the entrypoint file with [st.navigation](https://docs.streamlit.io/develop/api-reference/navigation/st.navigation) to bypass page identity issues entirely:

```python
# streamlit_app.py (entrypoint)
import streamlit as st

# Common widgets that persist across all pages
user_name = st.sidebar.text_input("Name", key="global_name")
user_role = st.sidebar.selectbox("Role", ["User", "Admin"], key="global_role")

# Navigation
page = st.navigation([
    st.Page("page1.py", title="Dashboard"),
    st.Page("page2.py", title="Settings"),
])
page.run()
```

- **Secondary recommendation:** For widgets that must be on individual pages, use the placeholder key pattern. See [Save widget values in Session State to preserve them between pages](#save-widget-values-in-session-state-to-preserve-them-between-pages) for more information.

## 📢 For multipage apps

**Primary recommendation:** Use common widgets in the entrypoint file with [st.navigation](https://docs.streamlit.io/develop/api-reference/navigation/st.navigation) to bypass page identity issues entirely:

```python
# streamlit_app.py (entrypoint)
import streamlit as st

# Common widgets that persist across all pages
user_name = st.sidebar.text_input("Name", key="global_name")
user_role = st.sidebar.selectbox("Role", ["User", "Admin"], key="global_role")

# Navigation
page = st.navigation([
    st.Page("page1.py", title="Dashboard"),
    st.Page("page2.py", title="Settings"),
])
page.run()
```

**Secondary recommendation:** For widgets that must be on individual pages, use the placeholder key pattern. See [Save widget values in Session State to preserve them between pages](#save-widget-values-in-session-state-to-preserve-them-between-pages) for more information.

## 📢 For parameter changes

- Use keys when you need widgets to maintain state despite parameter changes.
- If you need to change a parameter that affects a widget's identity, use placeholder keys like you would for multipage apps, or use a callback to directly maintain a widget's state. For more information, see [Retain statefulness when changing a widget's identity](#retain-statefulness-when-changing-a-widgets-identity).
- To force a widget to reset, update its key, or update a parameter without using a key.

## 📢 Best practices and recommendations

### For multipage apps

**Primary recommendation:** Use common widgets in the entrypoint file with [st.navigation](https://docs.streamlit.io/develop/api-reference/navigation/st.navigation) to bypass page identity issues entirely:

```python
# streamlit_app.py (entrypoint)
import streamlit as st

# Common widgets that persist across all pages
user_name = st.sidebar.text_input("Name", key="global_name")
user_role = st.sidebar.selectbox("Role", ["User", "Admin"], key="global_role")

# Navigation
page = st.navigation([
    st.Page("page1.py", title="Dashboard"),
    st.Page("page2.py", title="Settings"),
])
page.run()
```

**Secondary recommendation:** For widgets that must be on individual pages, use the placeholder key pattern. See [Save widget values in Session State to preserve them between pages](#save-widget-values-in-session-state-to-preserve-them-between-pages) for more information.

### For parameter changes

- Use keys when you need widgets to maintain state despite parameter changes.
- If you need to change a parameter that affects a widget's identity, use placeholder keys like you would for multipage apps, or use a callback to directly maintain a widget's state. For more information, see [Retain statefulness when changing a widget's identity](#retain-statefulness-when-changing-a-widgets-identity).
- To force a widget to reset, update its key, or update a parameter without using a key.

## 📢 Statefulness of widgets

As long as the widget identity remains the same and that widget is continuously rendered on the frontend, then it will be stateful and remember user input.

- **Primary recommendation:** Use common widgets in the entrypoint file with [st.navigation](https://docs.streamlit.io/develop/api-reference/navigation/st.navigation) to bypass page identity issues entirely:

```python
# streamlit_app.py (entrypoint)
import streamlit as st

# Common widgets that persist across all pages
user_name = st.sidebar.text_input("Name", key="global_name")
user_role = st.sidebar.selectbox("Role", ["User", "Admin"], key="global_role")

# Navigation
page = st.navigation([
    st.Page("page1.py", title="Dashboard"),
    st.Page("page2.py", title="Settings"),
])
page.run()
```

- **Secondary recommendation:** For widgets that must be on individual pages, use the placeholder key pattern. See [Save widget values in Session State to preserve them between pages](#save-widget-values-in-session-state-to-preserve-them-between-pages) for more information.

## 📢 Widget life cycle

When a widget command is called, Streamlit will check if it already has a widget with the same identity. Streamlit will reconnect if it thinks the widget already exists. Otherwise, it will make a new one.

- **Primary recommendation:** Use common widgets in the entrypoint file with [st.navigation](https://docs.streamlit.io/develop/api-reference/navigation/st.navigation) to bypass page identity issues entirely:

```python
# streamlit_app.py (entrypoint)
import streamlit as st

# Common widgets that persist across all pages
user_name = st.sidebar.text_input("Name", key="global_name")
user_role = st.sidebar.selectbox("Role", ["User", "Admin"], key="global_role")

# Navigation
page = st.navigation([
    st.Page("page1.py", title="Dashboard"),
    st.Page("page2.py", title="Settings"),
])
page.run()
```

- **Secondary recommendation:** For widgets that must be on individual pages, use the placeholder key pattern. See [Save widget values in Session State to preserve them between pages](#save-widget-values-in-session-state-to-preserve-them-between-pages) for more information.

## 📢 For multipage apps

**Primary recommendation:** Use common widgets in the entrypoint file with [st.navigation](https://docs.streamlit.io/develop/api-reference/navigation/st.navigation) to bypass page identity issues entirely:

```python
# streamlit_app.py (entrypoint)
import streamlit as st

# Common widgets that persist across all pages
user_name = st.sidebar.text_input("Name", key="global_name")
user_role = st.sidebar.selectbox("Role", ["User", "Admin"], key="global_role")

# Navigation
page = st.navigation([
    st.Page("page1.py", title="Dashboard"),
    st.Page("page2.py", title="Settings"),
])
page.run()
```

**Secondary recommendation:** For widgets that must be on individual pages, use the placeholder key pattern. See [Save widget values in Session State to preserve them between pages](#save-widget-values-in-session-state-to-preserve-them-between-pages) for more information.

## 📢 For parameter changes

- Use keys when you need widgets to maintain state despite parameter changes.
- If you need to change a parameter that affects a widget's identity, use placeholder keys like you would for multipage apps, or use a callback to directly maintain a widget's state. For more information, see [Retain statefulness when changing a widget's identity](#retain-statefulness-when-changing-a-widgets-identity).
- To force a widget to reset, update its key, or update a parameter without using a key.

## 📢 Best practices and recommendations

### For multipage apps

**Primary recommendation:** Use common widgets in the entrypoint file with [st.navigation](https://docs.streamlit.io/develop/api-reference/navigation/st.navigation) to bypass page identity issues entirely:

```python
# streamlit_app.py (entrypoint)
import streamlit as st

# Common widgets that persist across all pages
user_name = st.sidebar.text_input("Name", key="global_name")
user_role = st.sidebar.selectbox("Role", ["User", "Admin"], key="global_role")

# Navigation
page = st.navigation([
    st.Page("page1.py", title="Dashboard"),
    st.Page("page2.py", title="Settings"),
])
page.run()
```

**Secondary recommendation:** For widgets that must be on individual pages, use the placeholder key pattern. See [Save widget values in Session State to preserve them between pages](#save-widget-values-in-session-state-to-preserve-them-between-pages) for more information.

### For parameter changes

- Use keys when you need widgets to maintain state despite parameter changes.
- If you need to change a parameter that affects a widget's identity, use placeholder keys like you would for multipage apps, or use a callback to directly maintain a widget's state. For more information, see [Retain statefulness when changing a widget's identity](#retain-statefulness-when-changing-a-widgets-identity).
- To force a widget to reset, update its key, or update a parameter without using a key.

## 📢 Statefulness of widgets

As long as the widget identity remains the same and that widget is continuously rendered on the frontend, then it will be stateful and remember user input.

- **Primary recommendation:** Use common widgets in the entrypoint file with [st.navigation](https://docs.streamlit.io/develop/api-reference/navigation/st.navigation) to bypass page identity issues entirely:

```python
# streamlit_app.py (entrypoint)
import streamlit as st

# Common widgets that persist across all pages
user_name = st.sidebar.text_input("Name", key="global_name")
user_role = st.sidebar.selectbox("Role", ["User", "Admin"], key="global_role")

# Navigation
page = st.navigation([
    st.Page("page1.py", title="Dashboard"),
    st.Page("page2.py", title="Settings"),
])
page.run()
```

- **Secondary recommendation:** For widgets that must be on individual pages, use the placeholder key pattern. See [Save widget values in Session State to preserve them between pages](#save-widget-values-in-session-state-to-preserve-them-between-pages) for more information.

## 📢 Widget life cycle

When a widget command is called, Streamlit will check if it already has a widget with the same identity. Streamlit will reconnect if it thinks the widget already exists. Otherwise, it will make a new one.

- **Primary recommendation:** Use common widgets in the entrypoint file with [st.navigation](https://docs.streamlit.io/develop/api-reference/navigation/st.navigation) to bypass page identity issues entirely:

```python
# streamlit_app.py (entrypoint)
import streamlit as st

# Common widgets that persist across all pages
user_name = st.sidebar.text_input("Name", key="global_name")
user_role = st.sidebar.selectbox("Role", ["User", "Admin"], key="global_role")

# Navigation
page = st.navigation([
    st.Page("page1.py", title="Dashboard"),
    st.Page("page2.py", title="Settings"),
])
page.run()
```

- **Secondary recommendation:** For widgets that must be on individual pages, use the placeholder key pattern. See [Save widget values in Session State to preserve them between pages](#save-widget-values-in-session-state-to-preserve-them-between-pages) for more information.

## 📢 For multipage apps

**Primary recommendation:** Use common widgets in the entrypoint file with [st.navigation](https