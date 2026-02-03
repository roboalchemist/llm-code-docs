# Source: https://docs.streamlit.io/develop/api-reference/write-magic/st.write_stream

# st.write_stream

Stream a generator, iterable, or stream-like sequence to the app.

st.write_stream iterates through the given sequences and writes all chunks to the app. String chunks will be written using a typewriter effect. Other data types will be written using st.write.

## Function signature

```python
st.write_stream(stream, *, cursor=None)
```

## Parameters

- **stream**: (Callable, Generator, Iterable, OpenAI Stream, or LangChain Stream)
  - The generator or iterable to stream.
  - If you pass an async generator, Streamlit will internally convert it to a sync generator. If the generator depends on a cached object with async references, this can raise an error.
  - To use additional LLM libraries, you can create a wrapper to manually define a generator function and include custom output parsing.

- **cursor**: (str or None)
  - A string to append to text as it's being written. If this is None (default), no cursor is shown. Otherwise, the string is rendered as Markdown and appears as a cursor at the end of the streamed text. For example, you can use an emoji, emoji shortcode, or Material icon.
  - The first line of the cursor string can contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height. If you pass a multiline string, additional lines display after the text with the full Markdown rendering capabilities of st.markdown.
  - See the body parameter of st.markdown for additional, supported Markdown directives.

## Returns

- (str or list)
  - The full response. If the streamed output only contains text, this is a string. Otherwise, this is a list of all the streamed objects. The return value is fully compatible as input for st.write.

## Example

You can pass an OpenAI stream as shown in our tutorial, [Build a basic LLM chat app](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps#build-a-chatgpt-like-app). Alternatively, you can pass a generic generator function as input:

```python
import time
import numpy as np
import pandas as pd
import streamlit as st

_LOREM_IPSUM = "\\"\""
Lorem ipsum dolor sit amet, **consectetur adipiscing** elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
\\\"\\\"\\"

def stream_data():
    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.02)

    yield pd.DataFrame(
        np.random.randn(5, 10),
        columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    )

    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.02)

if st.button("Stream data"):
    st.write_stream(stream_data)
```

## Tip

If your stream object is not compatible with `st.write_stream`, define a wrapper around your stream object to create a compatible generator function.

For an example, see how we use [Replicate](https://replicate.com/docs/get-started/python) with [Snowflake Arctic](https://www.snowflake.com/en/data-cloud/arctic/) in [this code](https://github.com/streamlit/snowflake-arctic-st-demo/blob/0f0d8b49f328f72ae58ced2e9000790fb5e56e6f/simple_app.py#L58).

## Related Links

- [Previous: st.write](/develop/api-reference/write-magic/st.write)
- [Next: magic](/develop/api-reference/write-magic/magic)

## Forum

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.