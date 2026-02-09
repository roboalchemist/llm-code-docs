# Source: https://configcat.com/docs/api/reference/feature-flag-setting-values.md

# Feature Flag & Setting values

Copy page

With these endpoints you can control how your existing Feature Flags and Settings should serve their values. You can turn Feature Flags on or off, update Setting values and also add, remove or reorder Percentage and Targeting Rules.

To determine which Feature Flag or Setting you want to work with you have to pass its `settingId`. It can be obtained from the [Feature Flag & Setting](https://configcat.com/docs/api/reference/feature-flags-settings.md) endpoints.

You also have to specify in which Environment you want to change the served value configuration by its `environmentId` which can be obtained from the [List Environments](https://configcat.com/docs/api/reference/get-environments.md) endpoint.

<!-- -->

## [📄️<!-- --> <!-- -->Get value](https://configcat.com/docs/api/reference/get-setting-value.md)

[This endpoint returns the value of a Feature Flag or Setting](https://configcat.com/docs/api/reference/get-setting-value.md)

## [📄️<!-- --> <!-- -->Replace value](https://configcat.com/docs/api/reference/replace-setting-value.md)

[This endpoint replaces the whole value of a Feature Flag or Setting in a specified Environment.](https://configcat.com/docs/api/reference/replace-setting-value.md)

## [📄️<!-- --> <!-- -->Update value](https://configcat.com/docs/api/reference/update-setting-value.md)

[This endpoint updates the value of a Feature Flag or Setting](https://configcat.com/docs/api/reference/update-setting-value.md)

## [📄️<!-- --> <!-- -->Get values](https://configcat.com/docs/api/reference/get-setting-values.md)

[This endpoint returns the value of a specified Config's Feature Flags or Settings identified by the \`configId\` parameter](https://configcat.com/docs/api/reference/get-setting-values.md)

## [📄️<!-- --> <!-- -->Post values](https://configcat.com/docs/api/reference/post-setting-values.md)

[This endpoint replaces the values of a specified Config's Feature Flags or Settings identified by the \`configId\` parameter](https://configcat.com/docs/api/reference/post-setting-values.md)
