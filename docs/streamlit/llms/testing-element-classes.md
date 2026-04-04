# Source: https://docs.streamlit.io/develop/api-reference/app-testing/testing-element-classes

# Testing element classes - Streamlit Docs

Testing element classes
-----------------------

Testing element classes include Block, Element, ChatMessage, Column, and Tab for accessing and inspecting Streamlit app components in tests.

The `Element` class has the same methods and attributes as `AppTest`. A `Block` instance represents a container of elements just as `AppTest` represents the entire app. For example, `Block.button` will produce a `WidgetList` of `Button` in the same manner as [AppTest.button](https://docs.streamlit.io/develop/api-reference/app-testing/st.testing.v1.apptest#apptestbutton).

`ChatMessage`, `Column`, and `Tab` all inherit from `Block`. For all container classes, parameters of the original element can be obtained as properties. For example, `Button.label`, `Caption.help`, and `Toast.icon`.

`st.testing.v1.element_tree.Element`:

```python
class Element(proto, root):
    def run(self, *, timeout=None):
        """Run the AppTest script which contains the element."""
        return self._run_script(timeout)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._set_value(v)

    def set_value(self, v):
        """Set the value of the widget."""
        return self._