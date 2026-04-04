# Source: https://configcat.com/docs/api/reference/feature-flag-setting-values-using-sdk-key.md

# Feature Flag & Setting values using SDK Key

Copy page

With these endpoints you can control how your existing Feature Flags and Settings should serve their values. You can turn Feature Flags on or off, update Setting values and also add, remove or change the order of Percentage and Targeting Rules.

These endpoints are determining the Environment and Config by the [SDK key](https://app.configcat.com/sdkkey) passed in the `X-CONFIGCAT-SDKKEY` request header. To identify the desired Feature Flag or Setting to change, you can use either its `settingId` or `key` attribute. You can get those attributes from the [Feature Flag & Setting](https://configcat.com/docs/api/reference/feature-flags-settings.md) endpoints.

<!-- -->

## [📄️<!-- --> <!-- -->Get value](https://configcat.com/docs/api/reference/get-setting-value-by-sdkkey.md)

[This endpoint returns the value of a Feature Flag or Setting](https://configcat.com/docs/api/reference/get-setting-value-by-sdkkey.md)

## [📄️<!-- --> <!-- -->Replace value](https://configcat.com/docs/api/reference/replace-setting-value-by-sdkkey.md)

[This endpoint replaces the value of a Feature Flag or Setting](https://configcat.com/docs/api/reference/replace-setting-value-by-sdkkey.md)

## [📄️<!-- --> <!-- -->Update value](https://configcat.com/docs/api/reference/update-setting-value-by-sdkkey.md)

[This endpoint updates the value of a Feature Flag or Setting](https://configcat.com/docs/api/reference/update-setting-value-by-sdkkey.md)
