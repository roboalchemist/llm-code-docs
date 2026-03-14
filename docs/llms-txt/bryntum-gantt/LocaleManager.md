# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/localization/LocaleManager.md

# [LocaleManager](https://bryntum.com/docs/gantt/api/Core/localization/LocaleManager)

Singleton that handles switching locale. Locales can be included on page with `<script>` tags or loaded using ajax. When using script tags the first locale loaded is used per default, if another should be used as default specify it on any `<script>` tag with `data-default-locale="En"`.

Example for Grid (to use for other products replace grid with product name):

index.html:

```
// Using Ecma 6 modules and source
<script type="module" src="lib/Core/localization/SvSE.js">

// Specify default locale when using bundled locales
<script data-default-locale="En" src="build/locales/grid.locale.En.js">
<script src="build/locales/grid.locale.SvSE.js">
```

app.js:

```
// Import using sources
import LocaleManager from 'lib/Core/localization/LocaleManager.js';
// Or using module bundle
import { LocaleManager } from 'build/grid.module.js';

// Set locale using method
LocaleManager.applyLocale('SvSE');

// Or set locale using string property
LocaleManager.locale = 'SvSE';

// Or set locale using locale object property
LocaleManager.locale = LocaleManager.locales.SvSE;
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[throwOnMissingLocale](https://bryntum.com/docs/gantt/api/Core/localization/LocaleManager#config-throwOnMissingLocale)
Specifies if [Localizable.L()](https://bryntum.com/docs/gantt/api/#Core/localization/Localizable#function-L-static) function should throw error if no localization is found at runtime.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[throwOnMissingLocale](https://bryntum.com/docs/gantt/api/Core/localization/LocaleManager#property-throwOnMissingLocale)
Specifies if [Localizable.L()](https://bryntum.com/docs/gantt/api/#Core/localization/Localizable#function-L-static) function should throw error if no localization is found at runtime.

[locales](https://bryntum.com/docs/gantt/api/Core/localization/LocaleManager#property-locales)
Get/set currently registered locales. Alias for [LocaleHelper.locales](https://bryntum.com/docs/gantt/api/#Core/localization/LocaleHelper#property-locales-static).

[locale](https://bryntum.com/docs/gantt/api/Core/localization/LocaleManager#property-locale)
Get/set currently used locale. Setter calls [applyLocale](https://bryntum.com/docs/gantt/api/#Core/localization/LocaleManager#function-applyLocale).

## Functions

Functions are methods available for calling on the class

[applyLocale](https://bryntum.com/docs/gantt/api/Core/localization/LocaleManager#function-applyLocale)
Applies a locale by string name or publishes new locale configuration with [publishLocale](https://bryntum.com/docs/gantt/api/#Core/localization/LocaleHelper#function-publishLocale-static) and applies it. If locale is specified by string name, like 'En', it must be published before applying it.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[locale](https://bryntum.com/docs/gantt/api/Core/localization/LocaleManager#event-locale)
Fires when a locale is applied
