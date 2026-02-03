# Source: https://configcat.com/docs/api/reference/feature-flags-settings.md

# Feature Flags & Settings

Copy page

With these endpoints you can manage your Feature Flags or Settings within a Config. However you can't use them for manipulating the values of your Feature Flags and Settings, to do that please visit the [Feature Flag & Setting values using SDK Key](https://configcat.com/docs/api/reference/feature-flag-setting-values-using-sdk-key.md) and [Feature Flag & Setting values](https://configcat.com/docs/api/reference/feature-flag-setting-values.md) sections of the API.

For using these endpoints, first you have to select which Config you want to work with by its `configId` which can be obtained from the [List Configs](https://configcat.com/docs/api/reference/get-configs.md) endpoint. Then you can use it to create new Feature Flags or to get information about existing ones.

Then you can obtain the `settingId` or `key` of your desired Feature Flag or Setting to use them for further operations in this API.

[Here](https://configcat.com/docs/main-concepts.md#setting) you can read more about the concept of Settings.

<!-- -->

## [📄️<!-- --> <!-- -->List Flags](https://configcat.com/docs/api/reference/get-settings.md)

[This endpoint returns the list of the Feature Flags and Settings defined in a](https://configcat.com/docs/api/reference/get-settings.md)

## [📄️<!-- --> <!-- -->Create Flag](https://configcat.com/docs/api/reference/create-setting.md)

[This endpoint creates a new Feature Flag or Setting in a specified Config](https://configcat.com/docs/api/reference/create-setting.md)

## [📄️<!-- --> <!-- -->Get predefined variations (Beta)](https://configcat.com/docs/api/reference/get-predefined-variations.md)

[This endpoint returns the predefined variations along with their usages in the Environments for a Feature Flag or Setting identified by the \`settingId\` parameter.](https://configcat.com/docs/api/reference/get-predefined-variations.md)

## [📄️<!-- --> <!-- -->Update predefined variations (Beta)](https://configcat.com/docs/api/reference/update-predefined-variations.md)

[This endpoint updates the predefined variations for a Feature Flag or Setting identified by the \`settingId\` parameter.](https://configcat.com/docs/api/reference/update-predefined-variations.md)

## [📄️<!-- --> <!-- -->Get Flag](https://configcat.com/docs/api/reference/get-setting.md)

[This endpoint returns the metadata attributes of a Feature Flag or Setting](https://configcat.com/docs/api/reference/get-setting.md)

## [📄️<!-- --> <!-- -->Replace Flag](https://configcat.com/docs/api/reference/replace-setting.md)

[This endpoint replaces the whole value of a Feature Flag or Setting](https://configcat.com/docs/api/reference/replace-setting.md)

## [📄️<!-- --> <!-- -->Update Flag](https://configcat.com/docs/api/reference/update-setting.md)

[This endpoint updates the metadata of a Feature Flag or Setting](https://configcat.com/docs/api/reference/update-setting.md)

## [📄️<!-- --> <!-- -->Delete Flag](https://configcat.com/docs/api/reference/delete-setting.md)

[This endpoint removes a Feature Flag or Setting from a specified Config,](https://configcat.com/docs/api/reference/delete-setting.md)
