# Use variable font files to customize your font

Streamlit comes with Source Sans as the default font, but you can configure your app to use another font. This tutorial uses variable font files and is a walkthrough of Example 1 from [Customize fonts in your Streamlit app](/develop/concepts/configuration/theming-customize-fonts#example-1-define-an-alternative-font-with-variable-font-files). For an example that uses static font files, see [Use static font files to customize your font](/develop/tutorials/configuration-and-theming/static-fonts).

## Prerequisites

1. Go to [Google fonts](https://fonts.google.com/).
2. Search for or follow the link to [Noto Sans](https://fonts.google.com/noto/specimen/Noto+Sans), and select "Get font".
3. Search for or follow the link to [Noto Sans Mono](https://fonts.google.com/noto/specimen/Noto+Sans+Mono), and select "Get font".
4. To download your font files, in the upper-right corner, select the shopping bag (shopping_bag), and then select "Download all". In your downloads directory, unzip the downloaded file.
5. From the unzipped files, copy and save the TTF font files into a `static/` directory in `your_repository/`. Copy the following files:

    ```none
    Noto_Sans,Noto_Sans_Mono/
    ├── Noto_Sans_Mono/
    │   └── NotoSansMono-VariableFont_wdth,wght.ttf
    └── Noto_Sans/
       ├── NotoSans-Italic-VariableFont_wdth,wght.ttf
       └── NotoSans-VariableFont_wdth,wght.ttf
    ```

    Save those files in your repository:

    ```none
    your_repository/
    └── static/
        ├── NotoSans-Italic-VariableFont_wdth,wght.ttf
        ├── NotoSans-VariableFont_wdth,wght.ttf
        └── NotoSansMono-VariableFont_wdth,wght.ttf
    ```

    In this example, the font files are `NotoSans-Italic-VariableFont_wdth,wght.ttf` and `NotoSansMono-VariableFont_wdth,wght.ttf` for Noto Sans italic and normal font, respectively. `NotoSansMono-VariableFont_wdth,wght.ttf` is the file for Noto Sans Mono.

## Create your app configuration

To verify that your font is loaded correctly, create a simple app.

### Initialize your app

1. In your_repository, create a `.streamlit/config.toml` file:

    ```none
    your_repository/
    ├── .streamlit/
    │   └── config.toml
    └── static/
        ├── NotoSans-Italic-VariableFont_wdth,wght.ttf
        ├── NotoSans-VariableFont_wdth,wght.ttf
        └── NotoSansMono-VariableFont_wdth,wght.ttf
    ```

2. To enable static file serving, in `.streamlit/config.toml`, add the following text:

    ```none
    [server]
    enableStaticServing = true
    ```

    This makes the files in your `static/` directory publicly available through your app's URL at the relative path `app/static/{filename}`.

3. To define your alternative fonts, in `.streamlit/config.toml`, add the following text:

    ```none
    [[theme.fontFaces]]
    family="noto-sans"
    url="app/static/NotoSans-Italic-VariableFont_wdth,wght.ttf"
    style="italic"
    [[theme.fontFaces]]
    family="noto-sans"
    url="app/static/NotoSans-VariableFont_wdth,wght.ttf"
    style="normal"
    [[theme.fontFaces]]
    family="noto-mono"
    url="app/static/NotoSansMono-VariableFont_wdth,wght.ttf"
    ```

    The `[[theme.fontFaces]]` table can be repeated to use multiple files to define a single font or to define multiple fonts. In this example, the definitions make "noto-sans" and "noto-mono" available to other font configuration options.

    For convenience, avoid spaces in your font family names. When you declare the default font, you can also declare fallback fonts. If you avoid spaces in your font family names, you don't need inner quotes.

4. To set your alternative fonts as the default font for your app, in `.streamlit/config.toml`, add the following text:

    ```none
    [theme]
    font="noto-sans"
    codeFont="noto-mono"
    ```

    This sets Noto Sans as the default for all text in your app except inline code and code blocks, which will be Noto Sans Mono instead.

## Build the example

To verify that your font is loaded correctly, create a simple app.

### Initialize your app

1. In your_repository, create a `.streamlit/config.toml` file:

    ```none
    your_repository/
    ├── .streamlit/
    │   └── config.toml
    └── static/
        ├── NotoSans-Italic-VariableFont_wdth,wght.ttf
        ├── NotoSans-VariableFont_wdth,wght.ttf
        └── NotoSansMono-VariableFont_wdth,wght.ttf
    ```

2. To enable static file serving, in `.streamlit/config.toml`, add the following text:

    ```none
    [server]
    enableStaticServing = true
    ```

    This makes the files in your `static/` directory publicly available through your app's URL at the relative path `app/static/{filename}`.

3. To define your alternative fonts, in `.streamlit/config.toml`, add the following text:

    ```none
    [[theme.fontFaces]]
    family="noto-sans"
    url="app/static/NotoSans-Italic-VariableFont_wdth,wght.ttf"
    style="italic"
    [[theme.fontFaces]]
    family="noto-sans"
    url="app/static/NotoSans-VariableFont_wdth,wght.ttf"
    style="normal"
    [[theme.fontFaces]]
    family="noto-mono"
    url="app/static/NotoSansMono-VariableFont_wdth,wght.ttf"
    ```

    The `[[theme.fontFaces]]` table can be repeated to use multiple files to define a single font or to define multiple fonts. In this example, the definitions make "noto-sans" and "noto-mono" available to other font configuration options.

    For convenience, avoid spaces in your font family names. When you declare the default font, you can also declare fallback fonts. If you avoid spaces in your font family names, you don't need inner quotes.

4. To set your alternative fonts as the default font for your app, in `.streamlit/config.toml`, add the following text:

    ```none
    [theme]
    font="noto-sans"
    codeFont="noto-mono"
    ```

    This sets Noto Sans as the default for all text in your app except inline code and code blocks, which will be Noto Sans Mono instead.

## App testing

### Get started

1. Create a `streamlit_app.py` file in your working directory.

2. In `streamlit_app.py`, add the following text:

    ```python
    import streamlit as st

    st.write("Normal efg")
    st.write("*Italic efg*")
    st.write("**Bold efg**")
    st.write("***Bold-italic efg***")
    st.write("`Code normal efg`")
    st.write("*`Code italic efg`*")
    st.write("**`Code bold efg`**")
    st.write("***`Code bold-italic efg`***")
    ```

    The example includes "efg" in each line to better show the typographical differences when you run your app. The italic "f" descends below baseline, but the normal "f" doesn't. The italic "e" has a rounded front, but the normal "e" has a sharp corner.

## Status and limitations

## Additional resources

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)
- [Knowledge base](/knowledge-base)
- [Quick reference](/develop/quick-reference)