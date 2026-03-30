# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/localization/Localizable.md

# [Localizable](https://bryntum.com/docs/gantt/api/Core/localization/Localizable)

Mixin that provides localization functionality to a class.

```
// Get localized string
grid.L('foo');
grid.L('L{foo}');
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[localeClass](https://bryntum.com/docs/gantt/api/Core/localization/Localizable#config-localeClass)
A class translations of which are used for translating this entity. This is often used when translations of an item are defined on its container class. For example:

```
// Toolbar class that has some predefined items
class MyToolbar extends Toolbar {

    static $name = 'MyToolbar';

    static configurable = {
        // this specifies default configs for the items
        defaults : {
            // will tell items to use the toolbar locale
            localeClass : this
        },

        items : {
            // The toolbar has 2 buttons and translation for their texts will be searched in
            // the toolbar locales
            agree :{ text : 'Agree' },
            disagree :{ text : 'Disagree' }
        }
    };

   ...
}
```

So if one makes a locale for the `MyToolbar` class that will include `Agree` and `Disagree` string translations:

```
    ...
    MyToolbar : {
        Agree    : 'Yes, I agree',
        Disagree : 'No, I do not agree'
    }
```

They will be used for the toolbar buttons and the button captions will say `Yes, I agree` and `No, I do not agree`.

[localizable](https://bryntum.com/docs/gantt/api/Core/localization/Localizable#config-localizable)
Set to `false` to disable localization of this object.

[localizableProperties](https://bryntum.com/docs/gantt/api/Core/localization/Localizable#config-localizableProperties)
List of properties which values should be translated automatically upon a locale applying. In case there is a need to localize not typical value (not a String value or a field with re-defined setter/getter), you could use 'localeKey' meta configuration. Example:

```
 static configurable = {
      localizableProperties : ['width'],

      width : {
          value   : '54em', // default value here
          $config : {
              localeKey : 'L{editorWidth}' // name of the property that will be used in localization file
          }
      }
  };
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isLocalizable](https://bryntum.com/docs/gantt/api/Core/localization/Localizable#property-isLocalizable)
Identifies an object as an instance of [Localizable](https://bryntum.com/docs/gantt/api/#Core/localization/Localizable) class, or subclass thereof.

[isLocalizable](https://bryntum.com/docs/gantt/api/Core/localization/Localizable#property-isLocalizable-static)
Identifies an object as an instance of [Localizable](https://bryntum.com/docs/gantt/api/#Core/localization/Localizable) class, or subclass thereof.

[localeManager](https://bryntum.com/docs/gantt/api/Core/localization/Localizable#property-localeManager)
Get the global LocaleManager

[localeHelper](https://bryntum.com/docs/gantt/api/Core/localization/Localizable#property-localeHelper)
Get the global LocaleHelper

## Functions

Functions are methods available for calling on the class

[updateLocalization](https://bryntum.com/docs/gantt/api/Core/localization/Localizable#function-updateLocalization)
Method that is triggered when applying a locale to the instance (happens on the instance construction steps and when switching to another locale).

The method can be overridden to dynamically translate the instance when locale is switched. When overriding the method please make sure you call `super.updateLocalization()`.

[localize](https://bryntum.com/docs/gantt/api/Core/localization/Localizable#function-localize-static)
Get localized string, returns `null` if no localized string found.

```
// Simple localization
const someText = SomeClass.localize('L{text}');

// With template data
const someText = SomeClass.localize('L{template}', { count : 5 }); // Number in object
const someText = SomeClass.localize('L{template}', { name : 'John' }); // String in object
const someText = SomeClass.localize('L{template}', 'John'); // Strings parameter
```

[L](https://bryntum.com/docs/gantt/api/Core/localization/Localizable#function-L-static)
Get localized string, returns value of `text` if no localized string found.

If [throwOnMissingLocale](https://bryntum.com/docs/gantt/api/#Core/localization/LocaleManager#property-throwOnMissingLocale) is `true` then calls to `L()` will throw `Localization is not found for 'text' in 'ClassName'` exception when no localization is found.

```
// Simple localization
const someText = SomeClass.L('L{text}');

// With template data
const someText = SomeClass.L('L{template}', { count : 5 }); // Number in object
const someText = SomeClass.L('L{template}', { name : 'John' }); // String in object
const someText = SomeClass.L('L{template}', 'John'); // Strings parameter
```

[L](https://bryntum.com/docs/gantt/api/Core/localization/Localizable#function-L)
Localization function on the class instance that mixes [Localizable](https://bryntum.com/docs/gantt/api/#Core/localization/Localizable).

```
// Simple localization
const someText = someClass.L('L{text}');

// With template data
const someText = someClass.L('L{template}', { count : 5 }); // Number in object
const someText = someClass.L('L{template}', { name : 'John' }); // String in object
const someText = someClass.L('L{template}', 'John'); // Strings parameter
```

[optionalL](https://bryntum.com/docs/gantt/api/Core/localization/Localizable#function-optionalL-static)
Localization function to get an optional translation. The difference compared to `L()` is that it won't throw an error when the translation is missing even if configured with [throwOnMissingLocale](https://bryntum.com/docs/gantt/api/#Core/localization/LocaleManager#property-throwOnMissingLocale)

```
// Simple localization
const someText = someClass.optionalL('L{text}');

// With template data
const someText = SomeClass.optionalL('L{template}', { count : 5 }); // Number in object
const someText = SomeClass.optionalL('L{template}', { name : 'John' }); // String in object
const someText = SomeClass.optionalL('L{template}', 'John'); // Strings parameter
```

[optionalL](https://bryntum.com/docs/gantt/api/Core/localization/Localizable#function-optionalL)
Localization function to get an optional translation. The difference compared to `L()` is that it won't throw an error when the translation is missing even if configured with [throwOnMissingLocale](https://bryntum.com/docs/gantt/api/#Core/localization/LocaleManager#property-throwOnMissingLocale).

```
button.text = grid.optionalL('L{text}');

// With template data
const someText = someClass.optionalL('L{template}', { count : 5 }); // Number in object
const someText = someClass.optionalL('L{template}', { name : 'John' }); // String in object
const someText = someClass.optionalL('L{template}', 'John'); // Strings parameter
```
