# Use externally hosted fonts and fallbacks to customize your font

Streamlit comes with Source Sans as the default font, but you can configure your app to use another font. This tutorial uses variable font files and is a walkthrough of Example 3 from [Customize fonts in your Streamlit app](/develop/concepts/configuration/theming-customize-fonts#example-1-define-an-alternative-font-with-variable-font-files). For an example that uses self-hosted variable font files, see [Use variable font files to customize your font](/develop/tutorials/configuration-and-theming/variable-fonts). For an example that uses self-hosted static font files, see [Use static font files to customize your font](/develop/tutorials/configuration-and-theming/static-fonts).

This tutorial uses inline font definitions, which were introduced in Streamlit version 1.50.0. For an older workaround, see [Use externally hosted fonts and fallbacks to customize your font (streamlit<1.50.0)](/develop/tutorials/configuration-and-theming/external-fonts-old).

## Collect your font CSS URLs

1. To collect your URLs to use in later steps, open a text editor.
2. Remember to label the values as you paste them so you don't mix them up.
3. Go to [Google fonts](https://fonts.google.com/).
4. Search for or follow the link to [Nunito](https://fonts.google.com/specimen/Nunito), and select "Get font".
5. To get a link to a style sheet for your font files, in the upper-right corner, select the shopping bag (shopping_bag), and then select "Get embed code".
6. On the right, in the first code block, copy the `href` URL from the third link, and paste it into your text editor.
7. By default, the "Embed Code" page loads with the "Web" tab and `<link>` radio option selected. The first code block is titled, "Embed code in the <head> of your html". The URL is a link to a style sheet and should look like the following text:
8. To remove Nunito from your list and get a clean URL for Space Mono, select the trash can (delete). Then, repeat the previous three steps for [Space Mono](https://fonts.google.com/specimen/Space+Mono).
9. The URL should look like the following text:
10. In your text editor, modify each URL by prepending its font family and a colon separator:
11. Because Space Mono has a space in its name, use single quotes around the font family. These will be inner quotes when the string is later copied into your configuration file.

## Create your app configuration

1. In `your_repository/`, create a `.streamlit/config.toml` file:
2. To set your alternative fonts as the default font for your app, in `.streamlit/config.toml`, add the following text:
3. This sets Nunito as the default for all text in your app except inline code and code blocks, which will be Space Mono instead. If Google's font service is unavailable, the app will fall back to the indicated built-in fonts.

## Build the example

To verify that your font is loaded correctly, create a simple app.

### Initialize your app

1. In your_repository, create a file named `streamlit_app.py`.
2. In a terminal, change directories to your_repository, and start your app:
3. Your app will be blank because you still need to add code.
4. In `streamlit_app.py`, write the following:
5. Save your `streamlit_app.py` file, and view your running app.

### Display some text in your app

1. Create a `streamlit_app.py` file in your working directory.
2. In `streamlit_app.py`, add the following text:
3. The example includes "efg" in each line to better show the typographical differences when you run your app. In Space Mono, the italic "f" descends below baseline, but the normal "f" doesn't. Space Mono also has different serifs on its normal and italic "l".