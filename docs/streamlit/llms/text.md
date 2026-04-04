# Source: https://docs.streamlit.io/develop/api-reference/text

# Text elements

Streamlit apps usually start with a call to `st.title` to set the app's title. After that, there are 2 heading levels you can use: `st.header` and `st.subheader`.

Pure text is entered with `st.text`, and Markdown with `st.markdown`.

We also offer a "swiss-army knife" command called `st.write`, which accepts multiple arguments, and multiple data types. And as described above, you can also use [magic commands](/develop/api-reference/write-magic/magic) in place of `st.write`.

## Headings and body text

### Markdown

Display string formatted as Markdown.

```python
st.markdown("Hello **world**!")
```

### Title

Display text in title formatting.

```python
st.title("The app title")
```

### Header

Display text in header formatting.

```python
st.header("This is a header")
```

### Subheader

Display text in subheader formatting.

```python
st.subheader("This is a subheader")
```

### Badges

Display a small, colored badge.

```python
st.badge("New")
```

### Captions

Display text in small font.

```python
st.caption("This is written small caption text")
```

### Code blocks

Display a code block with optional syntax highlighting.

```python
st.code("a = 1234")
```

### Echo

Display some code on the app, then execute it. Useful for tutorials.

```python
with st.echo():
  st.write('This code will be printed')
```

### Preformatted text

Write fixed-width and preformatted text.

```python
st.text("Hello world")
```

### LaTeX

Display mathematical expressions formatted as LaTeX.

```python
st.latex("\\int a x^2 \\,dx")
```

### Divider

Display a horizontal rule.

```python
st.divider()
```

## Utilities

### Get help

Display object’s doc string, nicely formatted.

```python
st.help(st.write)
st.help(pd.DataFrame)
```

### Render HTML

Renders HTML strings to your app.

```python
st.html("Foo bar.")
```

## Third-party components

These are featured components created by our lovely community. For more examples and inspiration, check out our [Components Gallery](https://streamlit.io/components) and [Streamlit Extras](https://extras.streamlit.app/)!

### Tags

Add tags to your Streamlit apps. Created by [@gagan3012](https://github.com/gagan3012).

```python
st_tags(label="# Enter Keywords:", text="Press enter to add more", value=['Zero', 'One', 'Two'], suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'], maxtags = 4, key='1')
```

### NLU

Apply text mining on a dataframe. Created by [@JohnSnowLabs](https://github.com/JohnSnowLabs/).

```python
nlu.load('sentiment').predict('I love NLU! <3')
```

### Streamlit Extras

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
mention(label="An awesome Streamlit App", icon="streamlit", url="https://extras.streamlit.app/")
```

## App testing

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.