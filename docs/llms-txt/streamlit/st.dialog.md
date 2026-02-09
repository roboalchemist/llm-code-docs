# Source: https://docs.streamlit.io/develop/api-reference/execution-flow/st.dialog

# st.dialog

Function decorator to create a modal dialog.

A function decorated with `st.dialog` becomes a dialog function. When you call a dialog function, Streamlit inserts a modal dialog into your app. Streamlit element commands called within the dialog function render inside the modal dialog.

The dialog function can accept arguments that can be passed when it is called. Any values from the dialog that need to be accessed from the wider app should generally be stored in Session State.

If a dialog is dismissible, a user can dismiss it by clicking outside of it, clicking the "X" in its upper-right corner, or pressing ESC on their keyboard. You can configure whether this triggers a rerun of the app by setting the `on_dismiss` parameter.

If a dialog is not dismissible, it must be closed programmatically by calling `st.rerun()` inside the dialog function. This is useful when you want to ensure that the dialog is always closed programmatically, such as when the dialog contains a form that must be submitted before closing.

`st.dialog` inherits behavior from [st.fragment](https://docs.streamlit.io/develop/api-reference/execution-flow/st.fragment). When a user interacts with an input widget created inside a dialog function, Streamlit only reruns the dialog function instead of the full script.

Calling `st.sidebar` in a dialog function is not supported.

Dialog code can interact with Session State, imported modules, and other Streamlit elements created outside the dialog. Note that these interactions are additive across multiple dialog reruns. You are responsible for handling any side effects of that behavior.

## Warning

Only one dialog function may be called in a script run, which means that only one dialog can be open at any given time.

## Examples

The following example demonstrates the basic usage of `st.dialog`. In this app, clicking "A" or "B" will open a modal dialog and prompt you to enter a reason for your vote. In the modal dialog, click "Submit" to record your vote into Session State and rerun the app. This will close the modal dialog since the dialog function is not called during the full-script rerun.

```python
import streamlit as st

# st.dialog("Cast your vote")
def vote(item):
    st.write(f"Why is {item} your favorite?")
    reason = st.text_input("Because...")
    if st.button("Submit"):
        st.session_state.vote = { "item": item, "reason": reason }
        st.rerun()

if "vote" not in st.session_state:
    st.write("Vote for your favorite")
    if st.button("A"):
        vote("A")
    if st.button("B"):
        vote("B")
else:
    f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"
```

## Caching and state

## Connections and secrets

## Custom components

## Configuration

## Tools

## App testing

## Command line

## Tutorials

## Quick reference

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## API reference

- [PAGE ELEMENTS](/develop/concepts/architecture/run-your-app)
- [Write and magic](/develop/api-reference/write-magic)
- [Text elements](/develop/api-reference/text)
- [Data elements](/develop/api-reference/data)
- [Chart elements](/develop/api-reference/charts)
- [Input widgets](/develop/api-reference/widgets)
- [Media elements](/develop/api-reference/media)
- [Layouts and containers](/develop/api-reference/layout)
- [Chat elements](/develop/api-reference/chat)
- [Status elements](/develop/api-reference/status)
- [Third-party components](https://streamlit.io/components)
- [Application logic](/develop/concepts/architecture/run-your-app)
- [Authentication and user info](/develop/api-reference/user)
- [Navigation and pages](/develop/api-reference/navigation)
- [Execution flow](/develop/api-reference/execution-flow)
- [Caching and state](/develop/api-reference/caching-and-state)
- [Connections and secrets](/develop/api-reference/connections)
- [Custom components](/develop/api-reference/custom-components)
- [Configuration](/develop/api-reference/configuration)
- [App testing](/develop/api-reference/app-testing)
- [Command line](/develop/api-reference/cli)
- [Knowledge base](/knowledge-base)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## API reference

- [PAGE ELEMENTS](/develop/concepts/architecture/run-your-app)
- [Write and magic](/develop/api-reference/write-magic)
- [Text elements](/develop/api-reference/text)
- [Data elements](/develop/api-reference/data)
- [Chart elements](/develop/api-reference/charts)
- [Input widgets](/develop/api-reference/widgets)
- [Media elements](/develop/api-reference/media)
- [Layouts and containers](/develop/api-reference/layout)
- [Chat elements](/develop/api-reference/chat)
- [Status elements](/develop/api-reference/status)
- [Third-party components](https://streamlit.io/components)
- [Application logic](/develop/concepts/architecture/run-your-app)
- [Authentication and user info](/develop/api-reference/user)
- [Navigation and pages](/develop/api-reference/navigation)
- [Execution flow](/develop/api-reference/execution-flow)
- [Caching and state](/develop/api-reference/caching-and-state)
- [Connections and secrets](/develop/api-reference/connections)
- [Custom components](/develop/api-reference/custom-components)
- [Configuration](/develop/api-reference/configuration)
- [App testing](/develop/api-reference/app-testing)
- [Command line](/develop/api-reference/cli)
- [Knowledge base](/knowledge-base)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## API reference

- [PAGE ELEMENTS](/develop/concepts/architecture/run-your-app)
- [Write and magic](/develop/api-reference/write-magic)
- [Text elements](/develop/api-reference/text)
- [Data elements](/develop/api-reference/data)
- [Chart elements](/develop/api-reference/charts)
- [Input widgets](/develop/api-reference/widgets)
- [Media elements](/develop/api-reference/media)
- [Layouts and containers](/develop/api-reference/layout)
- [Chat elements](/develop/api-reference/chat)
- [Status elements](/develop/api-reference/status)
- [Third-party components](https://streamlit.io/components)
- [Application logic](/develop/concepts/architecture/run-your-app)
- [Authentication and user info](/develop/api-reference/user)
- [Navigation and pages](/develop/api-reference/navigation)
- [Execution flow](/develop/api-reference/execution-flow)
- [Caching and state](/develop/api-reference/caching-and-state)
- [Connections and secrets](/develop/api-reference/connections)
- [Custom components](/develop/api-reference/custom-components)
- [Configuration](/develop/api-reference/configuration)
- [App testing](/develop/api-reference/app-testing)
- [Command line](/develop/api-reference/cli)
- [Knowledge base](/knowledge-base)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## API reference

- [PAGE ELEMENTS](/develop/concepts/architecture/run-your-app)
- [Write and magic](/develop/api-reference/write-magic)
- [Text elements](/develop/api-reference/text)
- [Data elements](/develop/api-reference/data)
- [Chart elements](/develop/api-reference/charts)
- [Input widgets](/develop/api-reference/widgets)
- [Media elements](/develop/api-reference/media)
- [Layouts and containers](/develop/api-reference/layout)
- [Chat elements](/develop/api-reference/chat)
- [Status elements](/develop/api-reference/status)
- [Third-party components](https://streamlit.io/components)
- [Application logic](/develop/concepts/architecture/run-your-app)
- [Authentication and user info](/develop/api-reference/user)
- [Navigation and pages](/develop/api-reference/navigation)
- [Execution flow](/develop/api-reference/execution-flow)
- [Caching and state](/develop/api-reference/caching-and-state)
- [Connections and secrets](/develop/api-reference/connections)
- [Custom components](/develop/api-reference/custom-components)
- [Configuration](/develop/api-reference/configuration)
- [App testing](/develop/api-reference/app-testing)
- [Command line](/develop/api-reference/cli)
- [Knowledge base](/knowledge-base)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## API reference

- [PAGE ELEMENTS](/develop/concepts/architecture/run-your-app)
- [Write and magic](/develop/api-reference/write-magic)
- [Text elements](/develop/api-reference/text)
- [Data elements](/develop/api-reference/data)
- [Chart elements](/develop/api-reference/charts)
- [Input widgets](/develop/api-reference/widgets)
- [Media elements](/develop/api-reference/media)
- [Layouts and containers](/develop/api-reference/layout)
- [Chat elements](/develop/api-reference/chat)
- [Status elements](/develop/api-reference/status)
- [Third-party components](https://streamlit.io/components)
- [Application logic](/develop/concepts/architecture/run-your-app)
- [Authentication and user info](/develop/api-reference/user)
- [Navigation and pages](/develop/api-reference/navigation)
- [Execution flow](/develop/api-reference/execution-flow)
- [Caching and state](/develop/api-reference/caching-and-state)
- [Connections and secrets](/develop/api-reference/connections)
- [Custom components](/develop/api-reference/custom-components)
- [Configuration](/develop/api-reference/configuration)
- [App testing](/develop/api-reference/app-testing)
- [Command line](/develop/api-reference/cli)
- [Knowledge base](/knowledge-base)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## API reference

- [PAGE ELEMENTS](/develop/concepts/architecture/run-your-app)
- [Write and magic](/develop/api-reference/write-magic)
- [Text elements](/develop/api-reference/text)
- [Data elements](/develop/api-reference/data)
- [Chart elements](/develop/api-reference/charts)
- [Input widgets](/develop/api-reference/widgets)
- [Media elements](/develop/api-reference/media)
- [Layouts and containers](/develop/api-reference/layout)
- [Chat elements](/develop/api-reference/chat)
- [Status elements](/develop/api-reference/status)
- [Third-party components](https://streamlit.io/components)
- [Application logic](/develop/concepts/architecture/run-your-app)
- [Authentication and user info](/develop/api-reference/user)
- [Navigation and pages](/develop/api-reference/navigation)
- [Execution flow](/develop/api-reference/execution-flow)
- [Caching and state](/develop/api-reference/caching-and-state)
- [Connections and secrets](/develop/api-reference/connections)
- [Custom components](/develop/api-reference/custom-components)
- [Configuration](/develop/api-reference/configuration)
- [App testing](/develop/api-reference/app-testing)
- [Command line](/develop/api-reference/cli)
- [Knowledge base](/knowledge-base)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## API reference

- [PAGE ELEMENTS](/develop/concepts/architecture/run-your-app)
- [Write and magic](/develop/api-reference/write-magic)
- [Text elements](/develop/api-reference/text)
- [Data elements](/develop/api-reference/data)
- [Chart elements](/develop/api-reference/charts)
- [Input widgets](/develop/api-reference/widgets)
- [Media elements](/develop/api-reference/media)
- [Layouts and containers](/develop/api-reference/layout)
- [Chat elements](/develop/api-reference/chat)
- [Status elements](/develop/api-reference/status)
- [Third-party components](https://streamlit.io/components)
- [Application logic](/develop/concepts/architecture/run-your-app)
- [Authentication and user info](/develop/api-reference/user)
- [Navigation and pages](/develop/api-reference/navigation)
- [Execution flow](/develop/api-reference/execution-flow)
- [Caching and state](/develop/api-reference/caching-and-state)
- [Connections and secrets](/develop/api-reference/connections)
- [Custom components](/develop/api-reference/custom-components)
- [Configuration](/develop/api-reference/configuration)
- [App testing](/develop/api-reference/app-testing)
- [Command line](/develop/api-reference/cli)
- [Knowledge base](/knowledge-base)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## API reference

- [PAGE ELEMENTS](/develop/concepts/architecture/run-your-app)
- [Write and magic](/develop/api-reference/write-magic)
- [Text elements](/develop/api-reference/text)
- [Data elements](/develop/api-reference/data)
- [Chart elements](/develop/api-reference/charts)
- [Input widgets](/develop/api-reference/widgets)
- [Media elements](/develop/api-reference/media)
- [Layouts and containers](/develop/api-reference/layout)
- [Chat elements](/develop/api-reference/chat)
- [Status elements](/develop/api-reference/status)
- [Third-party components](https://streamlit.io/components)
- [Application logic](/develop/concepts/architecture/run-your-app)
- [Authentication and user info](/develop/api-reference/user)
- [Navigation and pages](/develop/api-reference/navigation)
- [Execution flow](/develop/api-reference/execution-flow)
- [Caching and state](/develop/api-reference/caching-and-state)
- [Connections and secrets](/develop/api-reference/connections)
- [Custom components](/develop/api-reference/custom-components)
- [Configuration](/develop/api-reference/configuration)
- [App testing](/develop/api-reference/app-testing)
- [Command line](/develop/api-reference/cli)
- [Knowledge base](/knowledge-base)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## API reference

- [PAGE ELEMENTS](/develop/concepts/architecture/run-your-app)
- [Write and magic](/develop/api-reference/write-magic)
- [Text elements](/develop/api-reference/text)
- [Data elements](/develop/api-reference/data)
- [Chart elements](/develop/api-reference/charts)
- [Input widgets](/develop/api-reference/widgets)
- [Media elements](/develop/api-reference/media)
- [Layouts and containers](/develop/api-reference/layout)
- [Chat elements](/develop/api-reference/chat)
- [Status elements](/develop/api-reference/status)
- [Third-party components](https://streamlit.io/components)
- [Application logic](/develop/concepts/architecture/run-your-app)
- [Authentication and user info](/develop/api-reference/user)
- [Navigation and pages](/develop/api-reference/navigation)
- [Execution flow](/develop/api-reference/execution-flow)
- [Caching and state](/develop/api-reference/caching-and-state)
- [Connections and secrets](/develop/api-reference/connections)
- [Custom components](/develop/api-reference/custom-components)
- [Configuration](/develop/api-reference/configuration)
- [App testing](/develop/api-reference/app-testing)
- [Command line](/develop/api-reference/cli)
- [Knowledge base](/knowledge-base)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## API reference

- [PAGE ELEMENTS](/develop/concepts/architecture/run-your-app)
- [Write and magic](/develop/api-reference/write-magic)
- [Text elements](/develop/api-reference/text)
- [Data elements](/develop/api-reference/data)
- [Chart elements](/develop/api-reference/charts)
- [Input widgets](/develop/api-reference/widgets)
- [Media elements](/develop/api-reference/media)
- [Layouts and containers](/develop/api-reference/layout)
- [Chat elements](/develop/api-reference/chat)
- [Status elements](/develop/api-reference/status)
- [Third-party components](https://streamlit.io/components)
- [Application logic](/develop/concepts/architecture/run-your-app)
- [Authentication and user info](/develop/api-reference/user)
- [Navigation and pages](/develop/api-reference/navigation)
- [Execution flow](/develop/api-reference/execution-flow)
- [Caching and state](/develop/api-reference/caching-and-state)
- [Connections and secrets](/develop/api-reference/connections)
- [Custom components](/develop/api-reference/custom-components)
- [Configuration](/develop/api-reference/configuration)
- [App testing](/develop/api-reference/app-testing)
- [Command line](/develop/api-reference/cli)
- [Knowledge base](/knowledge-base)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## API reference

- [PAGE ELEMENTS](/develop/concepts/architecture/run-your-app)
- [Write and magic](/develop/api-reference/write-magic)
- [Text elements](/develop/api-reference/text)
- [Data elements](/develop/api-reference/data)
- [Chart elements](/develop/api-reference/charts)
- [Input widgets](/develop/api-reference/widgets)
- [Media elements](/develop/api-reference/media)
- [Layouts and containers](/develop/api-reference/layout)
- [Chat elements](/develop/api-reference/chat)
- [Status elements](/develop/api-reference/status)
- [Third-party components](https://streamlit.io/components)
- [Application logic](/develop/concepts/architecture/run-your-app)
- [Authentication and user info](/develop/api-reference/user)
- [Navigation and pages](/develop/api-reference/navigation)
- [Execution flow](/develop/api-reference/execution-flow)
- [Caching and state](/develop/api-reference/caching-and-state)
- [Connections and secrets](/develop/api-reference/connections)
- [Custom components](/develop/api-reference/custom-components)
- [Configuration](/develop/api-reference/configuration)
- [App testing](/develop/api-reference/app-testing)
- [Command line](/develop/api-reference/cli)
- [Knowledge base](/knowledge-base)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## API reference

- [PAGE ELEMENTS](/develop/concepts/architecture/run-your-app)
- [Write and magic](/develop/api-reference/write-magic)
- [Text elements](/develop/api-reference/text)
- [Data elements](/develop/api-reference/data)
- [Chart elements](/develop/api-reference/charts)
- [Input widgets](/develop/api-reference/widgets)
- [Media elements](/develop/api-reference/media)
- [Layouts and containers](/develop/api-reference/layout)
- [Chat elements](/develop/api-reference/chat)
- [Status elements](/develop/api-reference/status)
- [Third-party components](https://streamlit.io/components)
- [Application logic](/develop/concepts/architecture/run-your-app)
- [Authentication and user info](/develop/api-reference/user)
- [Navigation and pages](/develop/api-reference/navigation)
- [Execution flow](/develop/api-reference/execution-flow)
- [Caching and state](/develop/api-reference/caching-and-state)
- [Connections and secrets](/develop/api-reference/connections)
- [Custom components](/develop/api-reference/custom-components)
- [Configuration](/develop/api-reference/configuration)
- [App testing](/develop/api-reference/app-testing)
- [Command line](/develop/api-reference/cli)
- [Knowledge base](/knowledge-base)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## API reference

- [PAGE ELEMENTS](/develop/concepts/architecture/run-your-app)
- [Write and magic](/develop/api-reference/write-magic)
- [Text elements](/develop/api-reference/text)
- [Data elements](/develop/api-reference/data)
- [Chart elements](/develop/api-reference/charts)
- [Input widgets](/develop/api-reference/widgets)
- [Media elements](/develop/api-reference/media)
- [Layouts and containers](/develop/api-reference/layout)
- [Chat elements](/develop/api-reference/chat)
- [Status elements](/develop/api-reference/status)
- [Third-party components](https://streamlit.io/components)
- [Application logic](/develop/concepts/architecture/run-your-app)
- [Authentication and user info](/develop/api-reference/user)
- [Navigation and pages](/develop/api-reference/navigation)
- [Execution flow](/develop/api-reference/execution-flow)
- [Caching and state](/develop/api-reference/caching-and-state)
- [Connections and secrets](/develop/api-reference/connections)
- [Custom components](/develop/api-reference/custom-components)
- [Configuration](/develop/api-reference/configuration)
- [App testing](/develop/api-reference/app-testing)
- [Command line](/develop/api-reference/cli)
- [Knowledge base](/knowledge-base)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## API reference

- [PAGE ELEMENTS](/develop/concepts/architecture/run-your-app)
- [Write and magic](/develop/api-reference/write-magic)
- [Text elements](/develop/api-reference/text)
- [Data elements](/develop/api-reference/data)
- [Chart elements](/develop/api-reference/charts)
- [Input widgets](/develop/api-reference/widgets)
- [Media elements](/develop/api-reference/media)
- [Layouts and containers](/develop/api-reference/layout)
- [Chat elements](/develop/api-reference/chat)
- [Status elements](/develop/api-reference/status)
- [Third-party components](https://streamlit.io/components)
- [Application logic](/develop/concepts/architecture/run-your-app)
- [Authentication and user info](/develop/api-reference/user)
- [Navigation and pages](/develop/api-reference/navigation)
- [Execution flow](/develop/api-reference/execution-flow)
- [Caching and state](/develop/api-reference/caching-and-state)
- [Connections and secrets](/develop/api-reference/connections)
- [Custom components](/develop/api-reference/custom-components)
- [Configuration](/develop/api-reference/configuration)
- [App testing](/develop/api-reference/app-testing)
- [Command line](/develop/api-reference/cli)
- [Knowledge base](/knowledge-base)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## API reference

- [PAGE ELEMENTS](/develop/concepts/architecture/run-your-app)
- [Write and magic](/develop/api-reference/write-magic)
- [Text elements](/develop/api-reference/text)
- [Data elements](/develop/api-reference/data)
- [Chart elements](/develop/api-reference/charts)
- [Input widgets](/develop/api-reference/widgets)
- [Media elements](/develop/api-reference/media)
- [Layouts and containers](/develop/api-reference/layout)
- [Chat elements](/develop/api-reference/chat)
- [Status elements](/develop/api-reference/status)
- [Third-party components](https://streamlit.io/components)
- [Application logic](/develop/concepts/architecture/run-your-app)
- [Authentication and user info](/develop/api-reference/user)
- [Navigation and pages](/develop/api-reference/navigation)
- [Execution flow](/develop/api-reference/execution-flow)
- [Caching and state](/develop/api-reference/caching-and-state)
- [Connections and secrets](/develop/api-reference/connections)
- [Custom components](/develop/api-reference/custom-components)
- [Configuration](/develop/api-reference/configuration)
- [App testing](/develop/api-reference/app-testing)
- [Command line](/develop/api-reference/cli)
- [Knowledge base](/knowledge-base)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## API reference

- [PAGE ELEMENTS](/develop/concepts/architecture/run-your-app)
- [Write and magic](/develop/api-reference/write-magic)
- [Text elements](/develop/api-reference/text)
- [Data elements](/develop/api-reference/data)
- [Chart elements](/develop/api-reference/charts)
- [Input widgets](/develop/api-reference/widgets)
- [Media elements](/develop/api-reference/media)
- [Layouts and containers](/develop/api-reference/layout)
- [Chat elements](/develop/api-reference/chat)
- [Status elements](/develop/api-reference/status)
- [Third-party components](https://streamlit.io/components)
- [Application logic](/develop/concepts/architecture/run-your-app)
- [Authentication and user info](/develop/api-reference/user)
- [Navigation and pages](/develop/api-reference/navigation)
- [Execution flow](/develop/api-reference/execution-flow)
- [Caching and state](/develop/api-reference/caching-and-state)
- [Connections and secrets](/develop/api-reference/connections)
- [Custom components](/develop/api-reference/custom-components)
- [Configuration](/develop/api-reference/configuration)
- [App testing](/develop/api-reference/app-testing)
- [Command line](/develop/api-reference/cli)
- [Knowledge base](/knowledge-base)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## API reference

- [PAGE ELEMENTS](/develop/concepts/architecture/run-your-app)
- [Write and magic](/develop/api-reference/write-magic)
- [Text elements](/develop/api-reference/text)
- [Data elements](/develop/api-reference/data)
- [Chart elements](/develop/api-reference/charts)
- [Input widgets](/develop/api-reference/widgets)
- [Media elements](/develop/api-reference/media)
- [Layouts and containers](/develop/api-reference/layout)
- [Chat elements](/develop/api-reference/chat)
- [Status elements](/develop/api-reference/status)
- [Third-party components](https://streamlit.io/components)
- [Application logic](/develop/concepts/architecture/run-your-app)
- [Authentication and user info](/develop/api-reference/user)
- [Navigation and pages](/develop/api-reference/navigation)
- [Execution flow](/develop/api-reference/execution-flow)
- [Caching and state](/develop/api-reference/caching-and-state)
- [Connections and secrets](/develop/api-reference/connections)
- [Custom components](/develop/api-reference/custom-components)
- [Configuration](/develop/api-reference/configuration)
- [App testing](/develop/api-reference/app-testing)
- [Command line](/develop/api-reference/cli)
- [Knowledge base](/knowledge-base)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## API reference

- [PAGE ELEMENTS](/develop/concepts/architecture/run-your-app)
- [Write and magic](/develop/api-reference/write-magic)
- [Text elements](/develop/api-reference/text)
- [Data elements](/develop/api-reference/data)
- [Chart elements](/develop/api-reference/charts)
- [Input widgets](/develop/api-reference/widgets)
- [Media elements](/develop/api-reference/media)
- [Layouts and containers](/develop/api-reference/layout)
- [Chat elements](/develop/api-reference/chat)
- [Status elements](/develop/api-reference/status)
- [Third-party components](https://streamlit.io/components)
- [Application logic](/develop/concepts/architecture/run-your-app)
- [Authentication and user info](/develop/api-reference/user)
- [Navigation and pages](/develop/api-reference/navigation)
- [Execution flow](/develop/api-reference/execution-flow)
- [Caching and state](/develop/api-reference/caching-and-state)
- [Connections and secrets](/develop/api-reference/connections)
- [Custom components](/develop/api-reference/custom-components)
- [Configuration](/develop/api-reference/configuration)
- [App testing](/develop/api-reference/app-testing)
- [Command line](/develop/api-reference/cli)
- [Knowledge base](/knowledge-base)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## API reference

- [PAGE ELEMENTS](/develop/concepts/architecture/run-your-app)
- [Write and magic](/develop/api-reference/write-magic)
- [Text elements](/develop/api-reference/text)
- [Data elements](/develop/api-reference/data)
- [Chart elements](/develop/api-reference/charts)
- [Input widgets](/develop/api-reference/widgets)
- [Media elements](/develop/api-reference/media)
- [Layouts and containers](/develop/api-reference/layout)
- [Chat elements](/develop/api-reference/chat)
- [Status elements](/develop/api-reference/status)
- [Third-party components](https://streamlit.io/components)
- [Application logic](/develop/concepts/architecture/run-your-app)
- [Authentication and user info](/develop/api-reference/user)
- [Navigation and pages](/develop/api-reference/navigation)
- [Execution flow](/develop/api-reference/execution-flow)
- [Caching and state](/develop/api-reference/caching-and-state)
- [Connections and secrets](/develop/api-reference/connections)
- [Custom components](/develop/api-reference/custom-components)
- [Configuration](/develop/api-reference/configuration)
- [App testing](/develop/api-reference/app-testing)
- [Command line](/develop/api-reference/cli)
- [Knowledge base](/knowledge-base)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## API reference

- [PAGE ELEMENTS](/develop/concepts/architecture/run-your-app)
- [Write and magic](/develop/api-reference/write-magic)
- [Text elements](/develop/api-reference/text)
- [Data elements](/develop/api-reference/data)
- [Chart elements](/develop/api-reference/charts)
- [Input widgets](/develop/api-reference/widgets)
- [Media elements](/develop/api-reference/media)
- [Layouts and containers](/develop/api-reference/layout)
- [Chat elements](/develop/api-reference/chat)
- [Status elements](/develop/api-reference/status)
- [Third-party components](https://streamlit.io/components)
- [Application logic](/develop/concepts/architecture/run-your-app)
- [Authentication and user info](/develop/api-reference/user)
- [Navigation and pages](/develop/api-reference/navigation)
- [Execution flow](/develop/api-reference/execution-flow)
- [Caching and state](/develop/api-reference/caching-and-state)
- [Connections and secrets](/develop/api-reference/connections)
- [Custom components](/develop/api-reference/custom-components)
- [Configuration](/develop/api-reference/configuration)
- [App testing](/develop/api-reference/app-testing)
- [Command line](/develop/api-reference/cli)
- [Knowledge base](/knowledge-base)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## API reference

- [PAGE ELEMENTS](/develop/concepts/architecture/run-your-app)
- [Write and magic](/develop/api-reference/write-magic)
- [Text elements](/develop/api-reference/text)
- [Data elements](/develop/api-reference/data)
- [Chart elements](/develop/api-reference/charts)
- [Input widgets](/develop/api-reference/widgets)
- [Media elements](/develop/api-reference/media)
- [Layouts and containers](/develop/api-reference/layout)
- [Chat elements](/develop/api-reference/chat)
- [Status elements](/develop/api-reference/status)
- [Third-party components](https://streamlit.io/components)
- [Application logic](/develop/concepts/architecture/run-your-app)
- [Authentication and user info](/develop/api-reference/user)
- [Navigation and pages](/develop/api-reference/navigation)
- [Execution flow](/develop/api-reference/execution-flow)
- [Caching and state](/develop/api-reference/caching-and-state)
- [Connections and secrets](/develop/api-reference/connections)
- [Custom components](/develop/api-reference/custom-components)
- [Configuration](/develop/api-reference/configuration)
- [App testing](/develop/api-reference/app-testing)
- [Command line](/develop/api-reference/cli)
- [Knowledge base](/knowledge-base)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## API reference

- [PAGE ELEMENTS](/develop/concepts/architecture/run-your-app)
- [Write and magic](/develop/api-reference/write-magic)