# Colors and borders

## Color values

For all configuration options that accept a color, you can specify the value with one of the following strings:

- A CSS `<named-color>` like `&quot;darkBlue&quot;` or `&quot;maroon&quot;`.
- A HEX string like `&quot;#483d8b&quot;` or `&quot;#6A5ACD&quot;`.
- An RGB string like `&quot;rgb(106, 90, 205)&quot;` or `&quot;RGB(70, 130, 180)&quot;`.
- An HSL string like `&quot;hsl(248, 53%, 58%)&quot;` or `&quot;HSL(147, 50%, 47%)&quot;`.

### `primaryColor`

`primaryColor` defines the accent color most often used throughout your Streamlit app. The following features and effects use your primary color:

- Button hover effects
- Elements in focus
- Selected elements

When your primary color is used as a background, Streamlit changes the text color to white. For example, this happens for `type="primary"` buttons and for selected items in `st.multiselect` and the navigation menu.

### `backgroundColor`, `secondaryBackgroundColor`, `codeBackgroundColor`, and `dataframeHeaderBackgroundColor`

Streamlit does not display borders for unfocused widgets by default (except for buttons). When a user focuses on a widget, Streamlit displays a border around the input area in your `primaryColor`. When the user removes focus, Streamlit hides the border.

If you set `showWidgetBorder=true`, Streamlit will display widget borders when the widget is not in focus. For those widgets, the border color is set by `borderColor`. If `borderColor` is not set, Streamlit infers a color by adding transparency to your `textColor`.

The following elements have borders that you can modify:

- Containers with borders, including expanders, forms, dialogs, popovers, and toasts
- The sidebar, including the right edge and the boundary below the navigation menu
- Dataframes and tables
- `st.tabs` (bottom border)

`dataframeBorderColor` overrides `borderColor` for dataframes and tables.

### `textColor`, `codeTextColor`, `linkColor`, and `linkUnderline`

You can configure the color of body, code, and link text.

`textColor` sets the default text color for all text in the app except language-highlighting in code blocks, inline code, and links. `codeTextColor` sets the default text color for inline code, but doesn't affect code blocks. `linkColor` sets the default font color for all Markdown links in the app. If `linkUnderline` is set to true (default), the link underline color matches `linkColor`.

The following elements are impacted by `textColor`:

- Markdown text, except links
- Text in code blocks that's not colored otherwise from language highlighting
- App-chrome and sidebar menu icons
- Widget labels, icons, option text, and placeholder text
- Dataframe and table text
- Non-Markdown links, like `st.page_link`, `st.link_button`, and the navigation menu

As noted previously, Streamlit changes the text color to white when text is displayed against your primary color.

### `backgroundColor`, `secondaryBackgroundColor`, `codeBackgroundColor`, and `dataframeHeaderBackgroundColor`

The following configuration options can be set separately for the sidebar by using the `[theme.sidebar]` table instead of the `[theme]` table in `config.toml`:

- `backgroundColor` defines the background color of your app.
- `secondaryBackgroundColor` is used for contrast in the following places:
  - The background of input or selection regions for widgets
  - Headers within elements like `st.help` and `st.dataframe` (if `dataframeHeaderBackgroundColor` isn't set)
  - Code blocks and inline code (if `codeBackgroundColor` isn't set)
- `codeBackgroundColor` sets the background for code blocks and line code. If `codeBackgroundColor` is not set, Streamlit uses `secondaryBackgroundColor` instead.
- `dataframeHeaderBackgroundColor` sets the background for dataframe headers (including the cells used for row selection and addition, if present).

### `borderColor`, `dataframeBorderColor`, and `showWidgetBorder`

Streamlit does not display borders for unfocused widgets by default (except for buttons). When a user focuses on a widget, Streamlit displays a border around the input area in your `primaryColor`. When the user removes focus, Streamlit hides the border.

If you set `showWidgetBorder=true`, Streamlit will display widget borders when the widget is not in focus. For those widgets, the border color is set by `borderColor`. If `borderColor` is not set, Streamlit infers a color by adding transparency to your `textColor`.

The following elements have borders that you can modify:

- Containers with borders, including expanders, forms, dialogs, popovers, and toasts
- The sidebar, including the right edge and the boundary below the navigation menu
- Dataframes and tables
- `st.tabs` (bottom border)

`dataframeBorderColor` overrides `borderColor` for dataframes and tables.

### `textColor`, `codeTextColor`, `linkColor`, and `linkUnderline`

You can configure the color of body, code, and link text.

`textColor` sets the default text color for all text in the app except language-highlighting in code blocks, inline code, and links. `codeTextColor` sets the default text color for inline code, but doesn't affect code blocks. `linkColor` sets the default font color for all Markdown links in the app. If `linkUnderline` is set to true (default), the link underline color matches `linkColor`.

The following elements are impacted by `textColor`:

- Markdown text, except links
- Text in code blocks that's not colored otherwise from language highlighting
- App-chrome and sidebar menu icons
- Widget labels, icons, option text, and placeholder text
- Dataframe and table text
- Non-Markdown links, like `st.page_link`, `st.link_button`, and the navigation menu

As noted previously, Streamlit changes the text color to white when text is displayed against your primary color.

### `backgroundColor`, `secondaryBackgroundColor`, `codeBackgroundColor`, and `dataframeHeaderBackgroundColor`

The following configuration options can be set separately for the sidebar by using the `[theme.sidebar]` table instead of the `[theme]` table in `config.toml`:

- `backgroundColor` defines the background color of your app.
- `secondaryBackgroundColor` is used for contrast in the following places:
  - The background of input or selection regions for widgets
  - Headers within elements like `st.help` and `st.dataframe` (if `dataframeHeaderBackgroundColor` isn't set)
  - Code blocks and inline code (if `codeBackgroundColor` isn't set)
- `codeBackgroundColor` sets the background for code blocks and line code. If `codeBackgroundColor` is not set, Streamlit uses `secondaryBackgroundColor` instead.
- `dataframeHeaderBackgroundColor` sets the background for dataframe headers (including the cells used for row selection and addition, if present).

### `borderColor`, `dataframeBorderColor`, and `showWidgetBorder`

Streamlit does not display borders for unfocused widgets by default (except for buttons). When a user focuses on a widget, Streamlit displays a border around the input area in your `primaryColor`. When the user removes focus, Streamlit hides the border.

If you set `showWidgetBorder=true`, Streamlit will display widget borders when the widget is not in focus. For those widgets, the border color is set by `borderColor`. If `borderColor` is not set, Streamlit infers a color by adding transparency to your `textColor`.

The following elements have borders that you can modify:

- Containers with borders, including expanders, forms, dialogs, popovers, and toasts
- The sidebar, including the right edge and the boundary below the navigation menu
- Dataframes and tables
- `st.tabs` (bottom border)

`dataframeBorderColor` overrides `borderColor` for dataframes and tables.

### `textColor`, `codeTextColor`, `linkColor`, and `linkUnderline`

You can configure the color of body, code, and link text.

`textColor` sets the default text color for all text in the app except language-highlighting in code blocks, inline code, and links. `codeTextColor` sets the default text color for inline code, but doesn't affect code blocks. `linkColor` sets the default font color for all Markdown links in the app. If `linkUnderline` is set to true (default), the link underline color matches `linkColor`.

The following elements are impacted by `textColor`:

- Markdown text, except links
- Text in code blocks that's not colored otherwise from language highlighting
- App-chrome and sidebar menu icons
- Widget labels, icons, option text, and placeholder text
- Dataframe and table text
- Non-Markdown links, like `st.page_link`, `st.link_button`, and the navigation menu

As noted previously, Streamlit changes the text color to white when text is displayed against your primary color.

### `backgroundColor`, `secondaryBackgroundColor`, `codeBackgroundColor`, and `dataframeHeaderBackgroundColor`

The following configuration options can be set separately for the sidebar by using the `[theme.sidebar]` table instead of the `[theme]` table in `config.toml`:

- `backgroundColor` defines the background color of your app.
- `secondaryBackgroundColor` is used for contrast in the following places:
  - The background of input or selection regions for widgets
  - Headers within elements like `st.help` and `st.dataframe` (if `dataframeHeaderBackgroundColor` isn't set)
  - Code blocks and inline code (if `codeBackgroundColor` isn't set)
- `codeBackgroundColor` sets the background for code blocks and line code. If `codeBackgroundColor` is not set, Streamlit uses `secondaryBackgroundColor` instead.
- `dataframeHeaderBackgroundColor` sets the background for dataframe headers (including the cells used for row selection and addition, if present).

### `borderColor`, `dataframeBorderColor`, and `showWidgetBorder`

Streamlit does not display borders for unfocused widgets by default (except for buttons). When a user focuses on a widget, Streamlit displays a border around the input area in your `primaryColor`. When the user removes focus, Streamlit hides the border.

If you set `showWidgetBorder=true`, Streamlit will display widget borders when the widget is not in focus. For those widgets, the border color is set by `borderColor`. If `borderColor` is not set, Streamlit infers a color by adding transparency to your `textColor`.

The following elements have borders that you can modify:

- Containers with borders, including expanders, forms, dialogs, popovers, and toasts
- The sidebar, including the right edge and the boundary below the navigation menu
- Dataframes and tables
- `st.tabs` (bottom border)

`dataframeBorderColor` overrides `borderColor` for dataframes and tables.

### `textColor`, `codeTextColor`, `linkColor`, and `linkUnderline`

You can configure the color of body, code, and link text.

`textColor` sets the default text color for all text in the app except language-highlighting in code blocks, inline code, and links. `codeTextColor` sets the default text color for inline code, but doesn't affect code blocks. `linkColor` sets the default font color for all Markdown links in the app. If `linkUnderline` is set to true (default), the link underline color matches `linkColor`.

The following elements are impacted by `textColor`:

- Markdown text, except links
- Text in code blocks that's not colored otherwise from language highlighting
- App-chrome and sidebar menu icons
- Widget labels, icons, option text, and placeholder text
- Dataframe and table text
- Non-Markdown links, like `st.page_link`, `st.link_button`, and the navigation menu

As noted previously, Streamlit changes the text color to white when text is displayed against your primary color.

### `backgroundColor`, `secondaryBackgroundColor`, `codeBackgroundColor`, and `dataframeHeaderBackgroundColor`

The following configuration options can be set separately for the sidebar by using the `[theme.sidebar]` table instead of the `[theme]` table in `config.toml`:

- `backgroundColor` defines the background color of your app.
- `secondaryBackgroundColor` is used for contrast in the following places:
  - The background of input or selection regions for widgets
  - Headers within elements like `st.help` and `st.dataframe` (if `dataframeHeaderBackgroundColor` isn't set)
  - Code blocks and inline code (if `codeBackgroundColor` isn't set)
- `codeBackgroundColor` sets the background for code blocks and line code. If `codeBackgroundColor` is not set, Streamlit uses `secondaryBackgroundColor` instead.
- `dataframeHeaderBackgroundColor` sets the background for dataframe headers (including the cells used for row selection and addition, if present).

### `borderColor`, `dataframeBorderColor`, and `showWidgetBorder`

Streamlit does not display borders for unfocused widgets by default (except for buttons). When a user focuses on a widget, Streamlit displays a border around the input area in your `primaryColor`. When the user removes focus, Streamlit hides the border.

If you set `showWidgetBorder=true`, Streamlit will display widget borders when the widget is not in focus. For those widgets, the border color is set by `borderColor`. If `borderColor` is not set, Streamlit infers a color by adding transparency to your `textColor`.

The following elements have borders that you can modify:

- Containers with borders, including expanders, forms, dialogs, popovers, and toasts
- The sidebar, including the right edge and the boundary below the navigation menu
- Dataframes and tables
- `st.tabs` (bottom border)

`dataframeBorderColor` overrides `borderColor` for dataframes and tables.

### `textColor`, `codeTextColor`, `linkColor`, and `linkUnderline`

You can configure the color of body, code, and link text.

`textColor` sets the default text color for all text in the app except language-highlighting in code blocks, inline code, and links. `codeTextColor` sets the default text color for inline code, but doesn't affect code blocks. `linkColor` sets the default font color for all Markdown links in the app. If `linkUnderline` is set to true (default), the link underline color matches `linkColor`.

The following elements are impacted by `textColor`:

- Markdown text, except links
- Text in code blocks that's not colored otherwise from language highlighting
- App-chrome and sidebar menu icons
- Widget labels, icons, option text, and placeholder text
- Dataframe and table text
- Non-Markdown links, like `st.page_link`, `st.link_button`, and the navigation menu

As noted previously, Streamlit changes the text color to white when text is displayed against your primary color.

### `backgroundColor`, `secondaryBackgroundColor`, `codeBackgroundColor`, and `dataframeHeaderBackgroundColor`

The following configuration options can be set separately for the sidebar by using the `[theme.sidebar]` table instead of the `[theme]` table in `config.toml`:

- `backgroundColor` defines the background color of your app.
- `secondaryBackgroundColor` is used for contrast in the following places:
  - The background of input or selection regions for widgets
  - Headers within elements like `st.help` and `st.dataframe` (if `dataframeHeaderBackgroundColor` isn't set)
  - Code blocks and inline code (if `codeBackgroundColor` isn't set)
- `codeBackgroundColor` sets the background for code blocks and line code. If `codeBackgroundColor` is not set, Streamlit uses `secondaryBackgroundColor` instead.
- `dataframeHeaderBackgroundColor` sets the background for dataframe headers (including the cells used for row selection and addition, if present).

### `borderColor`, `dataframeBorderColor`, and `showWidgetBorder`

Streamlit does not display borders for unfocused widgets by default (except for buttons). When a user focuses on a widget, Streamlit displays a border around the input area in your `primaryColor`. When the user removes focus, Streamlit hides the border.

If you set `showWidgetBorder=true`, Streamlit will display widget borders when the widget is not in focus. For those widgets, the border color is set by `borderColor`. If `borderColor` is not set, Streamlit infers a color by adding transparency to your `textColor`.

The following elements have borders that you can modify:

- Containers with borders, including expanders, forms, dialogs, popovers, and toasts
- The sidebar, including the right edge and the boundary below the navigation menu
- Dataframes and tables
- `st.tabs` (bottom border)

`dataframeBorderColor` overrides `borderColor` for dataframes and tables.

### `textColor`, `codeTextColor`, `linkColor`, and `linkUnderline`

You can configure the color of body, code, and link text.

`textColor` sets the default text color for all text in the app except language-highlighting in code blocks, inline code, and links. `codeTextColor` sets the default text color for inline code, but doesn't affect code blocks. `linkColor` sets the default font color for all Markdown links in the app. If `linkUnderline` is set to true (default), the link underline color matches `linkColor`.

The following elements are impacted by `textColor`:

- Markdown text, except links
- Text in code blocks that's not colored otherwise from language highlighting
- App-chrome and sidebar menu icons
- Widget labels, icons, option text, and placeholder text
- Dataframe and table text
- Non-Markdown links, like `st.page_link`, `st.link_button`, and the navigation menu

As noted previously, Streamlit changes the text color to white when text is displayed against your primary color.

### `backgroundColor`, `secondaryBackgroundColor`, `codeBackgroundColor`, and `dataframeHeaderBackgroundColor`

The following configuration options can be set separately for the sidebar by using the `[theme.sidebar]` table instead of the `[theme]` table in `config.toml`:

- `backgroundColor` defines the background color of your app.
- `secondaryBackgroundColor` is used for contrast in the following places:
  - The background of input or selection regions for widgets
  - Headers within elements like `st.help` and `st.dataframe` (if `dataframeHeaderBackgroundColor` isn't set)
  - Code blocks and inline code (if `codeBackgroundColor` isn't set)
- `codeBackgroundColor` sets the background for code blocks and line code. If `codeBackgroundColor` is not set, Streamlit uses `secondaryBackgroundColor` instead.
- `dataframeHeaderBackgroundColor` sets the background for dataframe headers (including the cells used for row selection and addition, if present).

### `borderColor`, `dataframeBorderColor`, and `showWidgetBorder`

Streamlit does not display borders for unfocused widgets by default (except for buttons). When a user focuses on a widget, Streamlit displays a border around the input area in your `primaryColor`. When the user removes focus, Streamlit hides the border.

If you set `showWidgetBorder=true`, Streamlit will display widget borders when the widget is not in focus. For those widgets, the border color is set by `borderColor`. If `borderColor` is not set, Streamlit infers a color by adding transparency to your `textColor`.

The following elements have borders that you can modify:

- Containers with borders, including expanders, forms, dialogs, popovers, and toasts
- The sidebar, including the right edge and the boundary below the navigation menu
- Dataframes and tables
- `st.tabs` (bottom border)

`dataframeBorderColor` overrides `borderColor` for dataframes and tables.

### `textColor`, `codeTextColor`, `linkColor`, and `linkUnderline`

You can configure the color of body, code, and link text.

`textColor` sets the default text color for all text in the app except language-highlighting in code blocks, inline code, and links. `codeTextColor` sets the default text color for inline code, but doesn't affect code blocks. `linkColor` sets the default font color for all Markdown links in the app. If `linkUnderline` is set to true (default), the link underline color matches `linkColor`.

The following elements are impacted by `textColor`:

- Markdown text, except links
- Text in code blocks that's not colored otherwise from language highlighting
- App-chrome and sidebar menu icons
- Widget labels, icons, option text, and placeholder text
- Dataframe and table text
- Non-Markdown links, like `st.page_link`, `st.link_button`, and the navigation menu

As noted previously, Streamlit changes the text color to white when text is displayed against your primary color.

### `backgroundColor`, `secondaryBackgroundColor`, `codeBackgroundColor`, and `dataframeHeaderBackgroundColor`

The following configuration options can be set separately for the sidebar by using the `[theme.sidebar]` table instead of the `[theme]` table in `config.toml`:

- `backgroundColor` defines the background color of your app.
- `secondaryBackgroundColor` is used for contrast in the following places:
  - The background of input or selection regions for widgets
  - Headers within elements like `st.help` and `st.dataframe` (if `dataframeHeaderBackgroundColor` isn't set)
  - Code blocks and inline code (if `codeBackgroundColor` isn't set)
- `codeBackgroundColor` sets the background for code blocks and line code. If `codeBackgroundColor` is not set, Streamlit uses `secondaryBackgroundColor` instead.
- `dataframeHeaderBackgroundColor` sets the background for dataframe headers (including the cells used for row selection and addition, if present).

### `borderColor`, `dataframeBorderColor`, and `showWidgetBorder`

Streamlit does not display borders for unfocused widgets by default (except for buttons). When a user focuses on a widget, Streamlit displays a border around the input area in your `primaryColor`. When the user removes focus, Streamlit hides the border.

If you set `showWidgetBorder=true`, Streamlit will display widget borders when the widget is not in focus. For those widgets, the border color is set by `borderColor`. If `borderColor` is not set, Streamlit infers a color by adding transparency to your `textColor`.

The following elements have borders that you can modify:

- Containers with borders, including expanders, forms, dialogs, popovers, and toasts
- The sidebar, including the right edge and the boundary below the navigation menu
- Dataframes and tables
- `st.tabs` (bottom border)

`dataframeBorderColor` overrides `borderColor` for dataframes and tables.

### `textColor`, `codeTextColor`, `linkColor`, and `linkUnderline`

You can configure the color of body, code, and link text.

`textColor` sets the default text color for all text in the app except language-highlighting in code blocks, inline code, and links. `codeTextColor` sets the default text color for inline code, but doesn't affect code blocks. `linkColor` sets the default font color for all Markdown links in the app. If `linkUnderline` is set to true (default), the link underline color matches `linkColor`.

The following elements are impacted by `textColor`:

- Markdown text, except links
- Text in code blocks that's not colored otherwise from language highlighting
- App-chrome and sidebar menu icons
- Widget labels, icons, option text, and placeholder text
- Dataframe and table text
- Non-Markdown links, like `st.page_link`, `st.link_button`, and the navigation menu

As noted previously, Streamlit changes the text color to white when text is displayed against your primary color.

### `backgroundColor`, `secondaryBackgroundColor`, `codeBackgroundColor`, and `dataframeHeaderBackgroundColor`

The following configuration options can be set separately for the sidebar by using the `[theme.sidebar]` table instead of the `[theme]` table in `config.toml`:

- `backgroundColor` defines the background color of your app.
- `secondaryBackgroundColor` is used for contrast in the following places:
  - The background of input or selection regions for widgets
  - Headers within elements like `st.help` and `st.dataframe` (if `dataframeHeaderBackgroundColor` isn't set)
  - Code blocks and inline code (if `codeBackgroundColor` isn't set)
- `codeBackgroundColor` sets the background for code blocks and line code. If `codeBackgroundColor` is not set, Streamlit uses `secondaryBackgroundColor` instead.
- `dataframeHeaderBackgroundColor` sets the background for dataframe headers (including the cells used for row selection and addition, if present).

### `borderColor`, `dataframeBorderColor`, and `showWidgetBorder`

Streamlit does not display borders for unfocused widgets by default (except for buttons). When a user focuses on a widget, Streamlit displays a border around the input area in your `primaryColor`. When the user removes focus, Streamlit hides the border.

If you set `showWidgetBorder=true`, Streamlit will display widget borders when the widget is not in focus. For those widgets, the border color is set by `borderColor`. If `borderColor` is not set, Streamlit infers a color by adding transparency to your `textColor`.

The following elements have borders that you can modify:

- Containers with borders, including expanders, forms, dialogs, popovers, and toasts
- The sidebar, including the right edge and the boundary below the navigation menu
- Dataframes and tables
- `st.tabs` (bottom border)

`dataframeBorderColor` overrides `borderColor` for dataframes and tables.

### `textColor`, `codeTextColor`, `linkColor`, and `linkUnderline`

You can configure the color of body, code, and link text.

`textColor` sets the default text color for all text in the app except language-highlighting in code blocks, inline code, and links. `codeTextColor` sets the default text color for inline code, but doesn't affect code blocks. `linkColor` sets the default font color for all Markdown links in the app. If `linkUnderline` is set to true (default), the link underline color matches `linkColor`.

The following elements are impacted by `textColor`:

- Markdown text, except links
- Text in code blocks that's not colored otherwise from language highlighting
- App-chrome and sidebar menu icons
- Widget labels, icons, option text, and placeholder text
- Dataframe and table text
- Non-Markdown links, like `st.page_link`, `st.link_button`, and the navigation menu

As noted previously, Streamlit changes the text color to white when text is displayed against your primary color.

### `backgroundColor`, `secondaryBackgroundColor`, `codeBackgroundColor`, and `dataframeHeaderBackgroundColor`

The following configuration options can be set separately for the sidebar by using the `[theme.sidebar]` table instead of the `[theme]` table in `config.toml`:

- `backgroundColor` defines the background color of your app.
- `secondaryBackgroundColor` is used for contrast in the following places:
  - The background of input or selection regions for widgets
  - Headers within elements like `st.help` and `st.dataframe` (if `dataframeHeaderBackgroundColor` isn't set)
  - Code blocks and inline code (if `codeBackgroundColor` isn't set)
- `codeBackgroundColor` sets the background for code blocks and line code. If `codeBackgroundColor` is not set, Streamlit uses `secondaryBackgroundColor` instead.
- `dataframeHeaderBackgroundColor` sets the background for dataframe headers (including the cells used for row selection and addition, if present).

### `borderColor`, `dataframeBorderColor`, and `showWidgetBorder`

Streamlit does not display borders for unfocused widgets by default (except for buttons). When a user focuses on a widget, Streamlit displays a border around the input area in your `primaryColor`. When the user removes focus, Streamlit hides the border.

If you set `showWidgetBorder=true`, Streamlit will display widget borders when the widget is not in focus. For those widgets, the border color is set by `borderColor`. If `borderColor` is not set, Streamlit infers a color by adding transparency to your `textColor`.

The following elements have borders that you can modify:

- Containers with borders, including expanders, forms, dialogs, popovers, and toasts
- The sidebar, including the right edge and the boundary below the navigation menu
- Dataframes and tables
- `st.tabs` (bottom border)

`dataframeBorderColor` overrides `borderColor` for dataframes and tables.

### `textColor`, `codeTextColor`, `linkColor`, and `linkUnderline`

You can configure the color of body, code, and link text.

`textColor` sets the default text color for all text in the app except language-highlighting in code blocks, inline code, and links. `codeTextColor` sets the default text color for inline code, but doesn't affect code blocks. `linkColor` sets the default font color for all Markdown links in the app. If `linkUnderline` is set to true (default), the link underline color matches `linkColor`.

The following elements are impacted by `textColor`:

- Markdown text, except links
- Text in code blocks that's not colored otherwise from language highlighting
- App-chrome and sidebar menu icons
- Widget labels, icons, option text, and placeholder text
- Dataframe and table text
- Non-Markdown links, like `st.page_link`, `st.link_button`, and the navigation menu

As noted previously, Streamlit changes the text color to white when text is displayed against your primary color.

### `backgroundColor`, `secondaryBackgroundColor`, `codeBackgroundColor`, and `dataframeHeaderBackgroundColor`

The following configuration options can be set separately for the sidebar by using the `[theme.sidebar]` table instead of the `[theme]` table in `config.toml`:

- `backgroundColor` defines the background color of your app.
- `secondaryBackgroundColor` is used for contrast in the following places:
  - The background of input or selection regions for widgets
  - Headers within elements like `st.help` and `st.dataframe` (if `dataframeHeaderBackgroundColor` isn't set)
  - Code blocks and inline code (if `codeBackgroundColor` isn't set)
- `codeBackgroundColor` sets the background for code blocks and line code. If `codeBackgroundColor` is not set, Streamlit uses `secondaryBackgroundColor` instead.
- `dataframeHeaderBackgroundColor` sets the background for dataframe headers (including the cells used for row selection and addition, if present).

### `borderColor`, `dataframeBorderColor`, and `showWidgetBorder`

Streamlit does not display borders for unfocused widgets by default (except for buttons). When a user focuses on a widget, Streamlit displays a border around the input area in your `primaryColor`. When the user removes focus, Streamlit hides the border.

If you set `showWidgetBorder=true`, Streamlit will display widget borders when the widget is not in focus. For those widgets, the border color is set by `borderColor`. If `borderColor` is not set, Streamlit infers a color by adding transparency to your `textColor`.

The following elements have borders that you can modify:

- Containers with borders, including expanders, forms, dialogs, popovers, and toasts
- The sidebar, including the right edge and the boundary below the navigation menu
- Dataframes and tables
- `st.tabs` (bottom border)

`dataframeBorderColor` overrides `borderColor` for dataframes and tables.

### `textColor`, `codeTextColor`, `linkColor`, and `linkUnderline`

You can configure the color of body, code, and link text.

`textColor` sets the default text color for all text in the app except language-highlighting in code blocks, inline code, and links. `codeTextColor` sets the default text color for inline code, but doesn't affect code blocks. `linkColor` sets the default font color for all Markdown links in the app. If `linkUnderline` is set to true (default), the link underline color matches `linkColor`.

The following elements are impacted by `textColor`:

- Markdown text, except links
- Text in code blocks that's not colored otherwise from language highlighting
- App-chrome and sidebar menu icons
- Widget labels, icons, option text, and placeholder text
- Dataframe and table text
- Non-Markdown links, like `st.page_link`, `st.link_button`, and the navigation menu

As noted previously, Streamlit changes the text color to white when text is displayed against your primary color.

### `backgroundColor`, `secondaryBackgroundColor`, `codeBackgroundColor`, and `dataframeHeaderBackgroundColor`

The following configuration options can be set separately for the sidebar by using the `[theme.sidebar]` table instead of the `[theme]` table in `config.toml`:

- `backgroundColor` defines the background color of your app.
- `secondaryBackgroundColor` is used for contrast in the following places:
  - The background of input or selection regions for widgets
  - Headers within elements like `st.help` and `st.dataframe` (if `dataframeHeaderBackgroundColor` isn't set)
  - Code blocks and inline code (if `codeBackgroundColor` isn't set)
- `codeBackgroundColor` sets the background for code blocks and line code. If `codeBackgroundColor` is not set, Streamlit uses `secondaryBackgroundColor` instead.
- `dataframeHeaderBackgroundColor` sets the background for dataframe headers (including the cells used for row selection and addition, if present).

### `borderColor`, `dataframeBorderColor`, and `showWidgetBorder`

Streamlit does not display borders for unfocused widgets by default (except for buttons). When a user focuses on a widget, Streamlit displays a border around the input area in your `primaryColor`. When the user removes focus, Streamlit hides the border.

If you set `showWidgetBorder=true`, Streamlit will display widget borders when the widget is not in focus. For those widgets, the border color is set by `borderColor`. If `borderColor` is not set, Streamlit infers a color by adding transparency to your `textColor`.

The following elements have borders that you can modify:

- Containers with borders, including expanders, forms, dialogs, popovers, and toasts
- The sidebar, including the right edge and the boundary below the navigation menu
- Dataframes and tables
- `st.tabs` (bottom border)

`dataframeBorderColor` overrides `borderColor` for dataframes and tables.

### `textColor`, `codeTextColor`, `linkColor`, and `linkUnderline`

You can configure the color of body, code, and link text.

`textColor` sets the default text color for all text in the app except language-highlighting in code blocks, inline code, and links. `codeTextColor` sets the default text color for inline code, but doesn't affect code blocks. `linkColor` sets the default font color for all Markdown links in the app. If `linkUnderline` is set to true (default), the link underline color matches `linkColor`.

The following elements are impacted by `textColor`:

- Markdown text, except links
- Text in code blocks that's not colored otherwise from language highlighting
- App-chrome and sidebar menu icons
- Widget labels, icons, option text, and placeholder text
- Dataframe and table text
- Non-Markdown links, like `st.page_link`, `st.link_button`, and the navigation menu

As noted previously, Streamlit changes the text color to white when text is displayed against your primary color.

### `backgroundColor`, `secondaryBackgroundColor`, `codeBackgroundColor`, and `dataframeHeaderBackgroundColor`

The following configuration options can be set separately for the sidebar by using the `[theme.sidebar]` table instead of the `[theme]` table in `config.toml`:

- `backgroundColor` defines the background color of your app.
- `secondaryBackgroundColor` is used for contrast in the following places:
  - The background of input or selection regions for widgets
  - Headers within elements like `st.help` and `st.dataframe` (if `dataframeHeaderBackgroundColor` isn't set)
  - Code blocks and inline code (if `codeBackgroundColor` isn't set)
- `codeBackgroundColor` sets the background for code blocks and line code. If `codeBackgroundColor` is not set, Streamlit uses `secondaryBackgroundColor` instead.
- `dataframeHeaderBackgroundColor` sets the background for dataframe headers (including the cells used for row selection and addition, if present).

### `borderColor`, `dataframeBorderColor`, and `showWidgetBorder`

Streamlit does not display borders for unfocused widgets by default (except for buttons). When a user focuses on a widget, Streamlit displays a border around the input area in your `primaryColor`. When the user removes focus, Streamlit hides the border.

If you set `showWidgetBorder=true`, Streamlit will display widget borders when the widget is not in focus. For those widgets, the border color is set by `borderColor`. If `borderColor` is not set, Streamlit infers a color by adding transparency to your `textColor`.

The following elements have borders that you can modify:

- Containers with borders, including expanders, forms, dialogs, popovers, and toasts
- The sidebar, including the right edge and the boundary below the navigation menu
- Dataframes and tables
- `st.tabs` (bottom border)

`dataframeBorderColor` overrides `borderColor` for dataframes and tables.

### `textColor`, `codeTextColor`, `linkColor`, and `linkUnderline`

You can configure the color of body, code, and link text.

`textColor` sets the default text color for all text in the app except language-highlighting in code blocks, inline code, and links. `codeTextColor` sets the default text color for inline code, but doesn't affect code blocks. `linkColor` sets the default font color for all Markdown links in the app. If `linkUnderline` is set to true (default), the link underline color matches `linkColor`.

The following elements are impacted by `textColor`:

- Markdown text