# Namespace: ConfigTypes

## Type Aliases[#](#type-aliases)

| Type Alias | Description |
| --- | --- |
| [A11y](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/configtypes/type-aliases/a11y/) | Represents the accessibility settings for the Creative Editor SDK. This type defines the heading hierarchy start level, which can be a number between 1 and 6. |
| [~Callbacks~](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/configtypes/type-aliases/callbacks/) | Represents the callback functions for various events in the Creative Editor SDK. This interface defines functions for handling back, close, share, save, load, load archive, download, export, upload, and unsupported browser events. |
| [CombinedConfiguration](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/configtypes/type-aliases/combinedconfiguration/) | Represents the combined configuration for the Creative Editor SDK. This type combines the `CESDKConfiguration` with the `EngineConfiguration` while omitting the `presets` key. It also includes deprecated keys from the `CESDKConfiguration`. |
| [I18n](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/configtypes/type-aliases/i18n/) | Represents the internationalization settings for the Creative Editor SDK. This type defines a record of locale strings to translation objects. Note: this will append keys and not override keys. |
| [OnUploadCallback](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/configtypes/type-aliases/onuploadcallback/) | Represents the upload callback function for the Creative Editor SDK. This type defines a function that handles file uploads, including progress updates and context. |
| [OnUploadOptions](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/configtypes/type-aliases/onuploadoptions/) | Represents the options for the upload callback in the Creative Editor SDK. This type defines the supported MIME types for uploads. |
| [Scale](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/configtypes/type-aliases/scale/) | Represents the base scale values for the Creative Editor SDK. This type defines the concrete scales that can be rendered. |
| [ScaleConfig](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/configtypes/type-aliases/scaleconfig/) | Represents the scale configuration for the Creative Editor SDK. This can be a concrete scale or a function that returns a scale based on viewport properties. |
| [ScaleFn](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/configtypes/type-aliases/scalefn/) | A function that returns a scale value based on viewport properties. This allows for dynamic scale selection based on runtime conditions. |
| [Theme](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/configtypes/type-aliases/theme/) | Represents the base theme values for the Creative Editor SDK. This type defines the concrete themes that can be rendered. |
| [ThemeConfig](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/configtypes/type-aliases/themeconfig/) | Represents the theme configuration for the Creative Editor SDK. This can be a concrete theme, a function that returns a theme, or ‘system’ to use OS preference. |
| [ThemeFn](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/configtypes/type-aliases/themefn/) | A function that returns a theme value. This allows for dynamic theme selection based on runtime conditions. The function is evaluated lazily whenever the theme is accessed. |

## Interfaces[#](#interfaces)

| Interface | Description |
| --- | --- |
| [BleedMarginOptions](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/configtypes/interfaces/bleedmarginoptions/) | Represents the bleed margin configuration options for a single design unit type in the Creative Editor SDK. This interface defines the dropdown options and the default bleed margin value. |
| [FontSizeOptions](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/configtypes/interfaces/fontsizeoptions/) | Represents the font size configuration options in the Creative Editor SDK. This interface defines the dropdown options for font sizes. |
| [UIOptionsForSingleDesignUnit](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/configtypes/interfaces/uioptionsforsingledesignunit/) | Represents the UI options for a single design unit type in the Creative Editor SDK. This interface defines the bleed margin options for a single design unit. |
| [UIOptionsPerDesignUnit](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/configtypes/interfaces/uioptionsperdesignunit/) | Represents the UI options for different design units in the Creative Editor SDK. This interface defines the UI options for millimeters, pixels, and inches. |
| [UploadCallbackContext](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/configtypes/interfaces/uploadcallbackcontext/) | Represents the context for the upload callback in the Creative Editor SDK. This interface defines the source ID and an optional group for the upload context. |

---



[Source](https:/img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/experimentaluserinterfaceapi)