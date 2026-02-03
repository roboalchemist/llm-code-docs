# Source: https://docs.streamlit.io/develop/api-reference/write-magic/magic

# Magic

Magic commands are a feature in Streamlit that allows you to write almost anything (markdown, data, charts) without having to type an explicit command at all. Just put the thing you want to show on its own line of code, and it will appear in your app. Here's an example:

```python
# Draw a title and some text to the app:
'''
# This is the document title

This is some _markdown_.
'''
import pandas as pd
df = pd.DataFrame({'col1': [1,2,3]})
df  # 👈 Draw the dataframe

x = 10
'x', x  # 👈 Draw the string 'x' and then the value of x

# Also works with most supported chart types
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

fig  # 👈 Draw a Matplotlib chart
```

## How Magic works

Any time Streamlit sees either a variable or literal value on its own line, it automatically writes that to your app using `st.write` (which you'll learn about later).

Also, magic is smart enough to ignore docstrings. That is, it ignores the strings at the top of files and functions.

If you prefer to call Streamlit commands more explicitly, you can always turn magic off in your `~/.streamlit/config.toml` with the following setting:

```toml
[runner]
magicEnabled = false
```

## Featured video

Learn what the `st.write` and `magic` commands are and how to use them.

<iframe src="https://www.youtube-nocookie.com/embed/wpDuY9I2fDg?playlist=wpDuY9I2fDg&amp;rel=0&amp;start=undefined&amp;end=undefined&amp;autoplay=false&amp;loop=false&amp;mute=0" width="100%" height="100%" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

[Previous: st.write_stream](/develop/api-reference/write-magic/st.write_stream) [Next: Text elements](/develop/api-reference/text)