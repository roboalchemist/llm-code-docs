# Source: https://configcat.com/docs/api/reference/feature-flag-setting-values-v-2.md

# Feature Flag & Setting values V2

*These endpoints are exclusive for [**Config V2**](https://configcat.com/docs/docs/advanced/config-v2/.md) Feature Flags.*<br />*They can only be used on a Config that has `evaluationVersion` set to `v2`.*<br /><br />With these endpoints you can control how your existing Feature Flags and Settings should serve their values. You can turn Feature Flags on or off, update Setting values and change Targeting Rules.

To determine which Feature Flag or Setting you want to work with you have to pass its `settingId`. It can be obtained from the [Feature Flag & Setting](https://configcat.com/docs/docs/api/reference/feature-flags-settings/.md) endpoints.

You also have to specify in which Environment you want to change the served value configuration by its `environmentId` which can be obtained from the [List Environments](https://configcat.com/docs/docs/api/reference/get-environments/.md) endpoint.

<!-- -->

## [üìÑÔ∏è<!-- --> <!-- -->Get value](https://configcat.com/docs/docs/api/reference/get-setting-value-v-2/.md)

[This endpoint returns the value of a Feature Flag or Setting](https://configcat.com/docs/docs/api/reference/get-setting-value-v-2/.md)

## [üìÑÔ∏è<!-- --> <!-- -->Replace value](https://configcat.com/docs/docs/api/reference/replace-setting-value-v-2/.md)

[This endpoint replaces the value and the Targeting Rules of a Feature Flag or Setting](https://configcat.com/docs/docs/api/reference/replace-setting-value-v-2/.md)

## [üìÑÔ∏è<!-- --> <!-- -->Update value](https://configcat.com/docs/docs/api/reference/update-setting-value-v-2/.md)

[This endpoint updates the value of a Feature Flag or Setting](https://configcat.com/docs/docs/api/reference/update-setting-value-v-2/.md)

## [üìÑÔ∏è<!-- --> <!-- -->Get values](https://configcat.com/docs/docs/api/reference/get-setting-values-v-2/.md)

[This endpoint returns all Feature Flag and Setting values of a Config identified by the \`configId\` parameter](https://configcat.com/docs/docs/api/reference/get-setting-values-v-2/.md)

## [üìÑÔ∏è<!-- --> <!-- -->Post values](https://configcat.com/docs/docs/api/reference/post-setting-values-v-2/.md)

[This endpoint batch updates the Feature Flags and Settings of a Config identified by the \`configId\` parameter](https://configcat.com/docs/docs/api/reference/post-setting-values-v-2/.md)
