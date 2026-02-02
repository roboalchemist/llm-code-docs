# Intro to custom components

The first step in developing a Streamlit Component is deciding whether to create a static component (i.e. rendered once, controlled by Python) or to create a bi-directional component that can communicate from Python to JavaScript and back.

## Create a static component

If your goal in creating a Streamlit Component is solely to display HTML code or render a chart from a Python visualization library, Streamlit provides two methods that greatly simplify the process: `components.html()` and `components.iframe()`.

If you are unsure whether you need bi-directional communication, **start here first**!

### Render an HTML string

While `st.text`, `st.markdown`, and `st.write` make it easy to write text to a Streamlit app, sometimes you'd rather implement a custom piece of HTML. Similarly, while Streamlit natively supports many charting libraries, you may want to implement a specific HTML/JavaScript template for a new charting library. `components.html` works by giving you the ability to embed an iframe inside of a Streamlit app that contains your desired output.

**Example**

```python
import streamlit as st
import streamlit.components.v1 as components

# bootstrap 4 collapse example
components.html(
    "<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css' integrity='sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm'>"
    "<script src='https://code.jquery.com/jquery-3.2.1.slim.min.js' integrity='sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN'>"
    "<script src='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js' integrity='sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl'>"
    "<div id='accordion'>"
      "<div class='card'>"
        "<div class='card-header' id='headingOne'>"
          <h5 class='mb-0'>
            <button class='btn btn-link' data-toggle='collapse' data-target='#collapseOne' aria-expanded='true' aria-controls='collapseOne'>
            Collapsible Group Item #1
            </button>
          </h5>
        </div>
        <div id='collapseOne' class='collapse show' aria-labelledby='headingOne' data-parent='#accordion'>
          <div class='card-body'>
            Collapsible Group Item #1 content
          </div>
        </div>
      </div>
      "<div class='card'>"
        "<div class='card-header' id='headingTwo'>"
          <h5 class='mb-0'>
            <button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseTwo' aria-expanded='false' aria-controls='collapseTwo'>
            Collapsible Group Item #2
            </button>
          </h5>
        </div>
        <div id='collapseTwo' class='collapse' aria-labelledby='headingTwo' data-parent='#accordion'>
          <div class='card-body'>
            Collapsible Group Item #2 content
          </div>
        </div>
      </div>"
    "</div>"
    "<script>\\n    Streamlit.setComponentValue(3.14);\\n</script>"
)
```

### Frontend

Because each Streamlit Component is its own webpage that gets rendered into an `iframe`, you can use just about any web tech you'd like to create that web page. We provide two templates to get started with in the Streamlit [Components-template GitHub repo](https://github.com/streamlit/component-template/); one of those templates uses [React](https://reactjs.org/) and the other does not.

```javascript
import streamlit.components.v1 as components
my_component = components.declare_component(
    "my_component",
    url="http://localhost:3001"
)
```

You can then use the returned `my_component` function to send and receive data with your frontend code:

```javascript
# Send data to the frontend using named arguments.
return_value = my_component(name="Blackbeard", ship="Queen Anne's Revenge")

# `my_component`'s return value is the data returned from the frontend.
st.write("Value = ", return_value)
```

While the above is all you need to define from the Python side to have a working Component, we recommend creating a "wrapper" function with named arguments and default values, input validation and so on. This will make it easier for end-users to understand what data values your function accepts and allows for defining helpful docstrings.

Please see [this example](https://github.com/streamlit/component-template/blob/master/template/my_component/__init__.py#L41-L77) from the Components-template for an example of creating a wrapper function.

## Python API

`components.declare_component()` is all that's required to create your Component's Python API:

```python
import streamlit.components.v1 as components
my_component = components.declare_component(
    "my_component",
    url="http://localhost:3001"
)
```

You can then use the returned `my_component` function to send and receive data with your frontend code:

```python
# Send data to the frontend using named arguments.
return_value = my_component(name="Blackbeard", ship="Queen Anne's Revenge")

# `my_component`'s return value is the data returned from the frontend.
st.write("Value = ", return_value)
```

While the above is all you need to define from the Python side to have a working Component, we recommend creating a "wrapper" function with named arguments and default values, input validation and so on. This will make it easier for end-users to understand what data values your function accepts and allows for defining helpful docstrings.

Please see [this example](https://github.com/streamlit/component-template/blob/master/template/my_component/__init__.py#L41-L77) from the Components-template for an example of creating a wrapper function.

## Data serialization

### Python → Frontend

You send data from Python to the frontend by passing keyword args to your Component's invoke function (that is, the function returned from `declare_component`). You can send the following types of data from Python to the frontend:

- Any JSON-serializable data
- `numpy.array`
- `pandas.DataFrame`

Any JSON-serializable data gets serialized to a JSON string, and deserialized to its JavaScript equivalent. `numpy.array` and `pandas.DataFrame` get serialized using [Apache Arrow](https://arrow.apache.org/) and are deserialized as instances of `ArrowTable`, which is a custom type that wraps Arrow structures and provides a convenient API on top of them.

Check out the [CustomDataframe](https://github.com/streamlit/component-template/tree/master/examples/CustomDataframe) and [SelectableDataTable](https://github.com/streamlit/component-template/tree/master/examples/SelectableDataTable) Component example code for more context on how to use `ArrowTable`.

### Frontend → Python

You send data from the frontend to Python via the `Streamlit.setComponentValue()` API (which is part of the template code). Unlike arg-passing from Python → frontend, **this API takes a single value**. If you want to return multiple values, you'll need to wrap them in an `Array` or `Object`.

Custom Components can send JSON-serializable data from the frontend to Python, as well as [Apache Arrow](http://arrow.apache.org/) `ArrowTable`s to represent dataframes.

## Other frontend details

- Because you're hosting your component from a dev server (via `npm run start`), any changes you make should be automatically reflected in the Streamlit app when you save.
- If you want to add more packages to your component, run `npm add` to add them from within your component's `frontend/` directory.

```bash
npm add baseui
```

- To build a static version of your component, run `npm run export`. See [Prepare your Component](https://docs.streamlit.io/publish#prepare-your-component) for more information.