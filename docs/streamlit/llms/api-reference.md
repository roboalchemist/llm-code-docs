# Source: https://docs.streamlit.io/develop/api-reference

# API Reference - Streamlit Docs

API Reference
-------------

Visually explore a gallery of Streamlit's API.

Streamlit makes it easy for you to visualize, mutate, and share data. The API reference is organized by activity type, like displaying data or optimizing performance. Each section includes methods associated with the activity type, including examples.

Browse our API below and click to learn more about any of our available commands! 🎈

### Display almost anything

#### Markdown

Display string formatted as Markdown.

```python
st.markdown("Hello **world**!")
```

### Dataframes

Display a dataframe as an interactive table.

```python
st.dataframe(my_data_frame)
```

### Data editor

Display a data editor widget.

```python
edited = st.data_editor(df, num_rows=5)
```

### Column configuration

Configure the display and editing behavior of dataframes and data editors.

```python
st.column_config.NumberColumn('Price (in USD)', min_value=0, format='$%d')
```

### Static tables

Display a static table.

```python
st.table(my_data_frame)
```

### Line chart

Display a line chart.

```python
st.line_chart(my_data_frame)
```

### Scatterplot on maps

Display a map with points on it.

```python
st.map(my_data_frame)
```

### Plotly

Display a plotly chart.

```python
st.plotly_chart(my_plotly_chart)
```

### PyDeck

Display a chart using the PyDeck library.

```python
st.pydeck_chart(my_pydeck_chart)
```

### Image

Display an image or list of images.

```python
st.image(numpy_array)
st.image(image_bytes)
st.image(file)
st.image("https://example.com/myimage.jpg")
```

### Logo

Display a logo in the upper-left corner of your app and its sidebar.

```python
st.logo("logo.jpg")
```

### PDF

Display a PDF file.

```python
st.pdf(my_document.pdf)
```

### Audio

Display an audio player.

```python
st.audio(numpy_array)
st.audio(audio_bytes)
st.audio(file)
st.audio("https://example.com/myaudio.mp3", format="audio/mp3")
```

### Video

Display a video player.

```python
st.video(numpy_array)
st.video(video_bytes)
st.video(file)
st.video("https://example.com/myvideo.mp4", format="video/mp4")
```

### Chat input

Display a chat input widget.

```python
prompt = st.chat_input("Say something")
if prompt:
    st.write(f"The user has sent: {prompt}")
```

### Text input

Display a single-line text input widget.

```python
name = st.text_input("First name")
```

### Audio input

Display a widget that allows users to record with their microphone.

```python
speech = st.audio_input("Record a voice message")
```

### Data editor

Display a data editor widget.

```python
content = st.data_editor(df, num_rows=5)
```

### Page

Define a page in a multipage app.

```python
home = st.Page(
    "home.py",
    title="Home",
    icon="🏠",
)
```

### Page link

Display a link to another page in a multipage app.

```python
st.page_link("app.py", label="Home", icon="🏠")
st.page_link("pages/profile.py", label="My profile")
```

### Modal dialog

Insert a modal dialog that can rerun independently from the rest of the script.

```python
@st.dialog("Sign up")
def email_form():
    name = st.text_input("Name")
    email = st.text_input("Email")
```

### Status container

Display output of long-running tasks in a container.

```python
with st.status('Running'):
    do_something_slow()
```

### Progress bar

Display a progress bar.

```python
for i in range(101):
  st.progress(i)
  do_something_slow()
```

### Spinner

Temporarily displays a message while executing a block of code.

```python
with st.spinner("Please wait..."):
  do_something_slow()
```

### Status container

Display output of long-running tasks in a container.

```python
with st.status('Running'):
  do_something_slow()
```

### Toast

Briefly displays a toast message in the bottom-right corner.

```python
st.toast('Butter!', icon='🧈')
```

### Snowflakes

Display celebratory snowflakes!

```python
do_something()
# Celebrate when all done! st.snow()
```

### Success box

Display a success message.

```python
st.success("Match found!")
```

### Info box

Display an informational message.

```python
st.info("Dataset is updated every day at midnight.")
```

### Warning box

Display warning message.

```python
st.warning("Unable to fetch image. Skipping...")
```

### Error box

Display error message.

```python
st.error("We encountered an error")
```

### Autorefresh

Force a refresh without tying up a script. Created by @kmcgrady.

```python
from streamlit_autorefresh import st_autorefresh
st_autorefresh(interval=2000, limit=100, key="fizzbuzzcounter")
```

### Pydantic

Auto-generate Streamlit UI from Pydantic Models and Dataclasses. Created by @lukasmasuch.

```python
import streamlit_pydantic as sp
sp.pydantic_form(key="my_form", model=ExampleModel)
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by @blackary.

```python
from st_pages import Page, show_pages, add_page_title
show_pages([Page("streamlit_app.py", "Home", "🏠"), Page("other_pages/page2.py", "Page 2", ":books:")]
```

### Streamlit Pages

An experimental version of Streamlit Multi-Page