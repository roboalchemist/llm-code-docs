# st.echo

Use in a `with` block to draw some code on the app, then execute it.

## Function signature

```python
st.echo(code_location="above")
```

### Parameters

- `code_location` (`"above" or "below"`): Whether to show the echoed code before or after the results of the executed code block.

## Example

```python
import streamlit as st

def get_user_name():
    return 'John'

# ------------------------------------------------
# Want people to see this part of the code...

def get_punctuation():
    return '!!!'

greeting = "Hi there, "
user_name = get_user_name()
punctuation = get_punctuation()

st.write(greeting, user_name, punctuation)

# ...up to here
# ------------------------------------------------

foo = 'bar'
st.write('Done!')
```

The file above creates a Streamlit app containing the words "Hi there, " and then "Done!".

Now let's use `st.echo()` to make that middle section of the code visible in the app:

```python
import streamlit as st

def get_user_name():
    return 'John'

with st.echo():
    # Everything inside this block will be both printed to the screen
    # and executed.

    def get_punctuation():
        return '!!!'

    greeting = "Hi there, "
    value = get_user_name()
    punctuation = get_punctuation()

    st.write(greeting, value, punctuation)

# And now we're back to not printing to the screen
foo = 'bar'
st.write('Done!')
```

It's that simple!

## Notes

You can have multiple `st.echo()` blocks in the same file. Use it as often as you wish!

## Forum

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

## Related Links

- [Previous: st.divider](/develop/api-reference/text/st.divider)
- [Next: st.latex](/develop/api-reference/text/st.latex)

## Copyright

© 2025 Snowflake Inc.