# Overview of multipage apps

Streamlit provides two built-in mechanisms for creating multipage apps. The simplest method is to use a `pages/` directory. However, the preferred and more customizable method is to use `st.navigation`.

## `st.Page` and `st.navigation`

If you want maximum flexibility in defining your multipage app, we recommend using `st.Page` and `st.navigation`. With `st.Page` you can declare any Python file or `Callable` as a page in your app. Furthermore, you can define common elements for your pages in your entrypoint file (the file you pass to `streamlit run`). With these methods, your entrypoint file becomes like a picture frame shared by all your pages.

You must include `st.navigation` in your entrypoint file to configure your app's navigation menu. This is also how your entrypoint file serves as the router between your pages.

### `pages/` directory

If you use `st.Page` without declaring the page title or URL pathname, Streamlit falls back on automatically determining the page label, title, and URL pathname in the same manner as when you use a `pages/` directory with the default navigation menu. This section describes this naming convention which is shared between the two approaches to multipage apps.

#### Parts of filenames and callables

Filenames are composed of four different parts as follows (in order):

1. `number`: A non-negative integer.
2. `separator`: Any combination of underscore (`"_"`), dash (`"-"`), and space (`" "`).
3. `identifier`: Everything up to, but not including, `.py`.
4. `.py`

For callables, the function name is the `identifier`, including any leading or trailing underscores.

#### How Streamlit converts filenames into labels and URLs

Within the navigation menu, Streamlit displays page labels and titles as follows:

1. If your page has an `identifier` that came from a filename, Streamlit uses the `identifier` with one modification. Streamlit condenses each consecutive grouping of spaces (`" "`) and underscores (`"_"`) to a single underscore.
2. Otherwise, if your page has an `identifier` that came from the name of a callable, Streamlit uses the `identifier` unmodified.
3. Otherwise, if your page has a `number` but does not have an `identifier`, Streamlit uses the `number`. Leading zeros are included, if present.

For each filename in the list above, the URL pathname would be `Awesome_page` relative to the root URL of the app. For example, if your app was running on `localhost` port `8501`, the full URL would be `localhost:8501/awesome_page`. For the last two callables, however, the pathname would include the leading and trailing underscores to match the callable name exactly.

### Important

Navigating between pages by URL creates a new browser session. In particular, clicking markdown links to other pages resets `st.session_state`. In order to retain values in `st.session_state`, handle page switching through Streamlit navigation commands and widgets, like `st.navigation`, `st.switch_page`, `st.page_link`, and the built-in navigation menu.

If a user tries to access a URL for a page that does not exist, they will see a modal like the one below, saying "Page not found."

![Page not found](/images/mpa-page-not-found.png)