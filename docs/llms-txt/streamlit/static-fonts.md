# Use static font files to customize your font

Streamlit comes with Source Sans as the default font, but you can configure your app to use another font. This tutorial uses static font files and is a walkthrough of Example 2 from [Customize fonts in your Streamlit app](/develop/concepts/configuration/theming-customize-fonts#example-2-define-an-alternative-font-with-static-font-files). For an example that uses variable font files, see [Use variable font files](/develop/tutorials/configuration-and-theming/variable-fonts).

## Prerequisites

1. In your_repository, create a `.streamlit/config.toml` file:
   
   ```toml
   your_repository/
   ├── .streamlit/
   │   └── config.toml
   └── static/
       ├── Tuffy-Bold.ttf
       ├── Tuffy-BoldItalic.ttf
       ├── Tuffy-Italic.ttf
       └── Tuffy-Regular.ttf
   ```
   
2. To enable static file serving, in `.streamlit/config.toml`, add the following text:
   
   ```toml
   [server]
   enableStaticServing = true
   ```
   
   This makes the files in your `static/` directory publicly available through your app's URL at the relative path `app/static/{filename}`.

3. To define your alternative fonts, in `.streamlit/config.toml`, add the following text:
   
   ```toml
   [[theme.fontFaces]]
   family="tuffy"
   url="app/static/Tuffy-Regular.ttf"
   style="normal"
   weight=400
   [[theme.fontFaces]]
   family="tuffy"
   url="app/static/Tuffy-Bold.ttf"
   style="normal"
   weight=700
   [[theme.fontFaces]]
   family="tuffy"
   url="app/static/Tuffy-Italic.ttf"
   style="italic"
   weight=400
   [[theme.fontFaces]]
   family="tuffy"
   url="app/static/Tuffy-BoldItalic.ttf"
   style="italic"
   weight=700
   ```
   
   The `[[theme.fontFaces]]` table can be repeated to use multiple files to define a single font or to define multiple fonts. In this example, the definitions make `tuffy` available to other font configuration options.

4. To set your alternative fonts as the default font for your app, in `.streamlit/config.toml`, add the following text:
   
   ```toml
   [theme]
   font="tuffy"
   ```
   
   This sets Tuffy as the default for all text in your app except inline code and code blocks.

## Build the example

To verify that your font is loaded correctly, create a simple app.

### Initialize your app

1. In your_repository, create a file named `streamlit_app.py`.

2. In a terminal, change directories to your_repository, and start your app:
   
   ```bash
   streamlit run streamlit_app.py
   ```
   
   Your app will be blank because you still need to add code.

3. In `streamlit_app.py`, write the following:
   
   ```python
   import streamlit as st
   st.write("Normal ABCabc123")
   st.write("*Italic ABCabc123*")
   st.write("**Bold ABCabc123**")
   st.write("***Bold-italic ABCabc123***")
   st.write("`Code ABCabc123`")
   ```

## Display some text in your app

1. Create a `streamlit_app.py` file in your working directory.

2. In `streamlit_app.py`, add the following text:
   
   ```python
   import streamlit as st
   st.write("Normal ABCabc123")
   st.write("*Italic ABCabc123*")
   st.write("**Bold ABCabc123**")
   st.write("***Bold-italic ABCabc123***")
   st.write("`Code ABCabc123`")
   ```

## Status and limitations

- [App analytics](/deploy/streamlit-community-cloud/manage-your-app/app-analytics)
- [App settings](/deploy/streamlit-community-cloud/manage-your-app/app-settings)
- [Delete your app](/deploy/streamlit-community-cloud/manage-your-app/delete-your-app)
- [Edit your app](/deploy/streamlit-community-cloud/manage-your-app/edit-your-app)
- [Favorite your app](/deploy/streamlit-community-cloud/manage-your-app/favorite-your-app)
- [Reboot your app](/deploy/streamlit-community-cloud/manage-your-app/reboot-your-app)
- [Rename your app in GitHub](/deploy/streamlit-community-cloud/manage-your-app/rename-your-app)
- [Upgrade Python](/deploy/streamlit-community-cloud/manage-your-app/upgrade-python)
- [Upgrade Streamlit](/deploy/streamlit-community-cloud/manage-your-app/upgrade-streamlit)