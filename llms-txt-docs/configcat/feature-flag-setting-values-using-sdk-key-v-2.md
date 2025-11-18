# Source: https://configcat.com/docs/api/reference/feature-flag-setting-values-using-sdk-key-v-2.md

# Feature Flag & Setting values using SDK Key V2

*These endpoints are exclusive for [**Config V2**](https://configcat.com/docs/docs/advanced/config-v2/.md) Feature Flags.*<br />*They can only be used on a Config that has `evaluationVersion` set to `v2`.*<br /><br />With these endpoints you can control how your existing Feature Flags and Settings should serve their values. You can turn Feature Flags on or off, update Setting values and change Targeting Rules.

These endpoints are determining the Environment and Config by the [SDK key](https://app.configcat.com/sdkkey) passed in the `X-CONFIGCAT-SDKKEY` request header. To identify the desired Feature Flag or Setting to change, you can use either its `settingId` or `key` attribute. You can get those attributes from the [Feature Flag & Setting](https://configcat.com/docs/docs/api/reference/feature-flags-settings/.md) endpoints.

<!-- -->

## [üìÑÔ∏è<!-- --> <!-- -->Get value](https://configcat.com/docs/docs/api/reference/get-setting-value-by-sdkkey-v-2/.md)

[This endpoint returns the value of a Feature Flag or Setting](https://configcat.com/docs/docs/api/reference/get-setting-value-by-sdkkey-v-2/.md)

## [üìÑÔ∏è<!-- --> <!-- -->Replace value](https://configcat.com/docs/docs/api/reference/replace-setting-value-by-sdkkey-v-2/.md)

[This endpoint replaces the value and the Targeting Rules of a Feature Flag or Setting](https://configcat.com/docs/docs/api/reference/replace-setting-value-by-sdkkey-v-2/.md)

## [üìÑÔ∏è<!-- --> <!-- -->Update value](https://configcat.com/docs/docs/api/reference/update-setting-value-by-sdkkey-v-2/.md)

[This endpoint updates the value of a Feature Flag or Setting](https://configcat.com/docs/docs/api/reference/update-setting-value-by-sdkkey-v-2/.md)
