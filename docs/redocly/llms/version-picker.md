# Source: https://redocly.com/docs/realm/config/version-picker.md

# `versionPicker`


If you have multiple versions of content, you can organize that content into versioned folders.
Versioned folders' names must start with `@`.
Their content is displayed with a version picker UI element that enables users to switch between versions.
You can also add a `versions.yaml` file to set the default version and specify which versions should display.

The `versionPicker` configuration option allows you to hide the version picker or include the version picker even on content that does not have multiple versions.

## Options

| Option | Type | Description |
|  --- | --- | --- |
| hide | boolean | Specifies if the version picker should be hidden.
Default: `false`. |
| showForUnversioned | boolean | Specifies if the version picker should be shown even for content that does not have multiple versions.
Default: `false`. |


## Examples

The following configuration hides the version picker:


```yaml
versionPicker:
  hide: true
```

The following configuration shows the version picker even for unversioned content.


```yaml
versionPicker:
  showForUnversioned: true
```

## Resources

- **[Add multiple versions](/docs/realm/content/versions)** - Configure your versions.yaml file to specify the default version and manage multiple documentation versions
- **[Products configuration](/docs/realm/config/products)** - Organize your project with multiple products and version management for complex documentation structures
- **[Configure localization](/docs/realm/config/l10n)** - Add a language picker for content translated into multiple languages alongside version management
- **[Front matter configuration](/docs/realm/config/front-matter-config)** - Toggle version picker visibility on individual pages using front matter for custom layouts
- **[Configuration options](/docs/realm/config)** - Explore other project configuration options for comprehensive documentation and platform customization