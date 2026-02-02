# st.Page

Configure a page for `st.navigation` in a multipage app.

Call `st.Page` to initialize a `StreamlitPage` object, and pass it to `st.navigation` to declare a page in your app.

When a user navigates to a page, `st.navigation` returns the selected `StreamlitPage` object. Call `.run()` on the returned `StreamlitPage` object to execute the page. You can only run the page returned by `st.navigation`, and you can only run it once per app rerun.

A page can be defined by a Python file or `Callable`.

## st.Page

A page within a multipage Streamlit app.

Use `st.Page` to initialize a `StreamlitPage` object.

### Methods

- `st.Page.run()`

### Attributes

- `icon`: The icon of the page.
  - If no icon was declared in `st.Page`, this property returns `""`.
- `title`: The title of the page.
  - Unless declared otherwise in `st.Page`, the page title is inferred from the filename or callable name. For more information, see [Overview of multipage apps](https://docs.streamlit.io/st.page.automatic-page-labels).
- `url_path`: The page's URL pathname, which is the path relative to the app's root URL.
  - Unless declared otherwise in `st.Page`, the URL pathname is inferred from the filename or callable name. For more information, see [Overview of multipage apps](https://docs.streamlit.io/st.page.automatic-page-urls).
  - The default page will always have a `url_path` of `""` to indicate the root URL (e.g. homepage).

## st.Page.run

Execute the page.

When a page is returned by `st.navigation`, use the `run()` method within your entrypoint file to render the page. You can only call this method on the page returned by `st.navigation`. You can only call this method once per run of your entrypoint file.

### Methods

- `st.Page.run()`

### Attributes

- `icon`: The icon of the page.
  - If no icon was declared in `st.Page`, this property returns `""`.
- `title`: The title of the page.
  - Unless declared otherwise in `st.Page`, the page title is inferred from the filename or callable name. For more information, see [Overview of multipage apps](https://docs.streamlit.io/st.page.automatic-page-labels).
- `url_path`: The page's URL pathname, which is the path relative to the app's root URL.
  - Unless declared otherwise in `st.Page`, the URL pathname is inferred from the filename or callable name. For more information, see [Overview of multipage apps](https://docs.streamlit.io/st.page.automatic-page-urls).
  - The default page will always have a `url_path` of `""` to indicate the root URL (e.g. homepage).