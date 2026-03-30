# Interface: CESDKConfiguration

Represents the configuration settings for the Creative Editor SDK. This interface defines various settings such as locale, theme, development mode, user interface, internationalization, accessibility, callbacks, feature flags, and logger.

## Properties[#](#properties)

| Property | Type | Description |
| --- | --- | --- |
| ~`locale`~ | `string` | **Deprecated** The `locale` property is deprecated. Please use the `setLocale()` property to configure localization. |
| ~`theme`~ | [`ThemeConfig`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/documentation/namespaces/configtypes/type-aliases/themeconfig/) | **Deprecated** The `theme` property is deprecated. Please use `ui.setTheme()` to configure theming. |
| `devMode` | `boolean` | \- |
| `ui` | [`UserInterface`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/userinterface/) | \- |
| ~`i18n`~ | [`I18n`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/documentation/namespaces/configtypes/type-aliases/i18n/) | **Deprecated** The `i18n` property is deprecated. Please use the `setTranslations()` method to configure internationalization. |
| `a11y` | [`A11y`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/documentation/namespaces/configtypes/type-aliases/a11y/) | \- |
| ~`callbacks`~ | [`Callbacks`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/documentation/namespaces/configtypes/type-aliases/callbacks/) | **Deprecated** The `callbacks` property is deprecated in favor of the `cesdk.actions` API and navigation bar order APIs. |
| `featureFlags?` | `object` | \- |
| `logger` | [`Logger`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/logger/) | \- |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/canvasmenuoptionscomponent)