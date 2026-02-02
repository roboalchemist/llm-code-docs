# Working with fragments

Reruns are a central part of every Streamlit app. When users interact with widgets, your script reruns from top to bottom, and your app's frontend is updated. Streamlit provides several features to help you develop your app within this execution model. Streamlit version 1.37.0 introduced fragments to allow rerunning a portion of your code instead of your full script. As your app grows larger and more complex, these fragment reruns help your app be efficient and performant. Fragments give you finer, easy-to-understand control over your app's execution flow.

Before you read about fragments, we recommend having a basic understanding of [caching](/develop/concepts/architecture/caching), [Session State](/concepts/architecture/session-state), and [forms](/develop/concepts/architecture/forms).

## Use cases for fragments

### Fragments vs forms

Here is a comparison between fragments and forms:

- **Forms**: allow users to interact with widgets without rerunning your app. Streamlit does not send user actions within a form to your app's Python backend until the form is submitted. Widgets within a form can not dynamically update other widgets (in or out of the form) in real-time.
- **Fragments**: run independently from the rest of your code. As your users interact with fragment widgets, their actions are immediately processed by your app's Python backend and your fragment code is rerun. Widgets within a fragment can dynamically update other widgets within the same fragment in real-time.

### Fragments vs custom components

Here is a comparison between fragments and custom components:

- **Components**: are custom frontend code that can interact with the Python code, native elements, and widgets in your Streamlit app. Custom components extend what’s possible with Streamlit. They follow the normal Streamlit execution flow.
- **Fragments**: are parts of your app that can rerun independently of the full app. Fragments can be composed of multiple Streamlit elements, widgets, or any Python code.

A fragment can include one or more custom components. A custom component could not easily include a fragment!

## Fragments vs caching

Here is a comparison between fragments and caching:

- **Caching**: allows you to skip over a function and return a previously computed value. When you use caching, you execute everything except the cached function (if you've already run it before).
- **Fragments**: allow you to freeze most of your app and just execute the fragment. When you use fragments, you execute only the fragment (when triggering a fragment rerun).

Caching saves you from unnecessarily running a piece of your app while the rest runs. Fragments save you from running your full app when you only want to run one piece.

## Limitations and unsupported behavior

- Fragments can't detect a change in input values. It is best to use Session State for dynamic input and output for fragment functions.
- Using caching and fragments on the same function is unsupported.
- Fragments can't render widgets in externally-created containers; widgets can only be in the main body of a fragment.