# Source: https://docs.streamlit.io/develop/concepts/configuration/theming-customize-fonts

# Customize fonts

Streamlit lets you change and customize the fonts in your app. You can load font files from a public URL or host them with your app using [static file serving](/develop/concepts/configuration/serving-static-files).

## Default Streamlit fonts

Streamlit comes with [Source Sans](https://fonts.adobe.com/fonts/source-sans), [Source Serif](https://fonts.adobe.com/fonts/source-serif), and [Source Code](https://fonts.adobe.com/fonts/source-code-pro) fonts. These font files are included with the Streamlit library so clients don't download them from a third party. By default, Streamlit uses Source Sans for all text except inline code and code blocks, which use Source Code instead.

To use these default faults, you can set each of the following configuration options to `"sans-serif"` (Source Sans), `"serif"` (Source Serif), or `"monospace"` (Source Code) in `config.toml`:

```toml
[theme]
font = "sans-serif"
headingFont = "sans-serif"
codeFont = "monospace"
[theme.sidebar]
font = "sans-serif"
headingFont = "sans-serif"
codeFont = "monospace"
```

Directory structure:

```none
project_directory/
├── .streamlit/
│   └── config.toml
├── static/
│   ├── NotoSans-Italic-VariableFont_wdth,wght.ttf
│   ├── NotoSans-VariableFont_wdth,wght.ttf
│   └── NotoSansMono-VariableFont_wdth,wght.ttf
└── streamlit_app.py
```

## Font size

You can set the base font size for your app in pixels. You must specify the base font size as an integer. The following configuration is equivalent to the default base font size of 16 pixels:

```toml
[theme]
baseFontSize = 16
```

Additionally, you can set the font size for code blocks. The font size can be declared in pixels or rem. The following configuration is equivalent to the default code font size of 0.875rem:

```toml
[theme]
codeFontSize = "0.875rem"
```

## Font colors

Font color options are described in [Customize colors and borders in your Streamlit app](/develop/concepts/configuration/theming-customize-colors-and-borders#textcolor-and-linkcolor).

## Design tips

When using alternative fonts in your Streamlit app, keep good design practices in mind. The legibility of a font is strongly influenced by its size, contrast with its background, and shape. Streamlit lets you declare a different font for your headers from the rest of your text. If you introduce a more elaborate font, limit it to your headers. Because `theme.font` and `theme.sidebar.font` are used to set the font in widget labels, tooltips, column headers, and dataframe cells, they should always be a highly readable font.

For inspiration, see [Fonts in Use](https://fontsinuse.com/).