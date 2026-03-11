# Source: https://redocly.com/docs/realm/config/breadcrumbs.md

# `breadcrumbs`

Use the `breadcrumbs` option to control the links displayed at the top of the page to indicate a page's location in the navigation structure.

The breadcrumbs option also supports page-level configuration using front matter.

Screenshot of page in project with breadcrumbs
Breadcrumbs are enabled by default, but can be disabled to remove them from your published project.
You can also add links that you want to always appear on every page at the start of the breadcrumbs links.

## Options

| Option | Type | Description |
|  --- | --- | --- |
| hide | boolean | Disables breadcrumb links in the project when set to `true`.
Default value: `false` |
| prefixItems | [[Breadcrumb object](#breadcrumb-object)] | A list of breadcrumb links to always be displayed first. |


### Breadcrumb object

| Option | Type | Description |
|  --- | --- | --- |
| page | string | **REQUIRED.** Path to the file which represents the page to link to.
If you do not include the `label` property, the text for the link will match the level 1 heading of the page. |
| label | string | Link text displayed for the item. |
| labelTranslationKey | string | Translation key used for [localization](/docs/realm/config/l10n). |
| icon | string | A [Font Awesome](https://fontawesome.com/icons) or relative path to icon image file.
Font Awesome icons can be prefixed with type: `duotone`, `solid`, `regular` or `brands`.
Example: `book`, `duotone book`, `./images/config-icon.svg`. |


## Example


```yaml
breadcrumbs:
  hide: false
  prefixItems:
    - page: index.page.tsx
      label: Home
      labelTranslationKey: home.title
      icon: home
```

## Resources

- **[Navigation concepts](/docs/realm/navigation/navigation)** - Understand different navigation elements in your project including breadcrumbs and their role in user experience
- **[Configure navigation elements](/docs/realm/navigation)** - Customize navigation elements including sidebar, navbar, footer, and breadcrumbs for optimal site organization
- **[Front matter configuration](/docs/realm/config/front-matter-config)** - Configure breadcrumb behavior and appearance on individual pages using front matter for granular control
- **[Configuration options](/docs/realm/config)** - Explore other project configuration options for comprehensive documentation and platform customization
- **[Markdown configuration options](/docs/realm/config/markdown)** - Customize default items on Markdown pages including time stamps and table of contents for enhanced breadcrumb integration
- **[Navigation configuration options](/docs/realm/config/navigation)** - Configure previous and next navigation buttons and label text for seamless breadcrumb navigation flow