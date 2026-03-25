# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/Config.md

# [Config](https://bryntum.com/docs/gantt/api/Core/Config)

This class holds the description of a config property. Only one instance of this class is needed for each config name (e.g., "text"). If config options are supplied, however, they also contribute to the cached instance.

Instances should always be retrieved by calling `Config.get()`.

The **Configs** of this class correspond to `options` that can be supplied to the `get()` method. These affect the behavior of the config property in some way, as descried by their respective documentation.

This class is not used directly.

The Setter
----------

The primary functionality provided by `Config` is its standard setter. This setter function ensures consistent behavior when modifying config properties.

The standard setter algorithm is as follows (using the `'text'` config for illustration):

* If the class defines a `changeText()` method, call it passing the new value and the current value: `changeText(newText, oldText)`.  
    Then:
  * If `changeText()` exits without returning a value (i.e., `undefined`), exit and do nothing further. The assumption is that the changer method has done all that is required.
  * Otherwise, the return value of `changeText()` replaces the incoming value passed to the setter.
* If the new value (or the value returned by `changeText()`) is `!==` to the current value:
  * Update the stored config value in `this._text`.
  * If the class defines an `updateText()` method, call it passing the new value and the previous value. `updateText(newText, oldText)`
  * Any return value from `updateText()` is stored in `this.textUpdated`.
  * If the class defines an `onConfigChange()` method, call it passing an object with the following properties:
    * `name` - The config's name
    * `value` - The new value
    * `was` - The previous value
    * `config` - The `Config` instance.

NOTE: unlike `changeText()` and `updateText()`, the name of the `onConfigChange()` method is unaffected by the config's name.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[equal](https://bryntum.com/docs/gantt/api/Core/Config#config-equal)
A function that compares values for equality. This test is used to determine if the `update` method should be called when the setter is invoked.

To handle `Date` values:

```
 class Foo extends Base {
     static configurable = {
         date : {
             $config : {
                 equal : 'date'
             },

             value : null
         }
     };

     updateDate(date) {
         // date has changed
     }
 }
```

Also useful for some configs, a custom equal function can be specified. The function is called using the owning instance as the `thisObj`

```
 class Foo extends Base {
     static configurable = {
         bar : {
             $config : {
                 equal : ObjectHelper.isEqual
             },

             value : null
         }
     };

     updateBar(value) {
         // value has changed
     }
 }
```

[date](https://bryntum.com/docs/gantt/api/Core/Config#config-date)
Indicates that values are Date objects.

[lazy](https://bryntum.com/docs/gantt/api/Core/Config#config-lazy)
Indicates that this config property should not automatically initialize during construction. When this property is set to `true`, initialization is triggered by the first use of the config property's getter.

This property can alternatively be set to a string, in which case it can be initialized as a group using the [triggerConfigs](https://bryntum.com/docs/gantt/api/#Core/Base#function-triggerConfigs) method which will initialize all lazy configs with the same value for this property. Note: the config will still initialize on first use if that occurs prior to the call to `triggerConfigs`.

[nullify](https://bryntum.com/docs/gantt/api/Core/Config#config-nullify)
Indicates that this config property should automatically be set to `null` on destroy.

[render](https://bryntum.com/docs/gantt/api/Core/Config#config-render)
Indicates that this config participates in rendering. This has does not affect the behavior of the property directly, but allows classes that perform rendering to detect which config changes will affect the rendered result.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[descriptor](https://bryntum.com/docs/gantt/api/Core/Config#property-descriptor)
The descriptor to use with `Reflect.defineProperty()` for defining this config's getter and setter.

[initDescriptor](https://bryntum.com/docs/gantt/api/Core/Config#property-initDescriptor)
The descriptor to use with `Reflect.defineProperty()` for defining this config's initter.

[cache](https://bryntum.com/docs/gantt/api/Core/Config#property-cache-static)
This object holds `Config` instances keyed by their name. For example:

```
 Config.cache = {
     disabled : Config.get('disabled'),
     text     : Config.get('text'),
     title    : Config.get('title')
 };
```

[convertMethods](https://bryntum.com/docs/gantt/api/Core/Config#property-convertMethods-static)
This object holds config value converter methods.

All methods in this object have the same signature as the [convert()](https://bryntum.com/docs/gantt/api/#Core/Config#function-convert) method.

This object has the following convert methods:

* `array` : Converts non-null values into arrays.
* `date` : Converts values to `Date` type.
* `day` : Converts values to `Date` type and clears the time to midnight.

[equalityMethods](https://bryntum.com/docs/gantt/api/Core/Config#property-equalityMethods-static)
This object holds config value equality methods. By default, the `===` operator is used to compare config values for semantic equality. When an `equal` option is specified as a string, that string is used as a key into this object.

All equality methods in this object have the same signature as the [equal()](https://bryntum.com/docs/gantt/api/#Core/Config#function-equal) method.

This object has the following equality methods:

* `array` : Compares arrays of values using `===` on each element.
* `date` : Compares values of `Date` type.
* `day` : Compares values of `Date` type.
* `strict` : The default equal algorithm based on `===` operator.

[mergeMethods](https://bryntum.com/docs/gantt/api/Core/Config#property-mergeMethods-static)
This object holds config value merge methods. By default, [merge](https://bryntum.com/docs/gantt/api/#Core/helper/ObjectHelper#function-merge-static) is used to merge object's by their properties. Config merge methods are used to combine config values from derived classes with config values from super classes, as well as instance config values with those of the class.

All merge methods in this object have the same signature as the [merge()](https://bryntum.com/docs/gantt/api/#Core/Config#function-merge) method.

This object has the following merge methods:

* `distinct` : Combines arrays of values ensuring that no value is duplicated. When given an object, its truthy keys are included, while its falsy keys are removed from the result.
* `merge` : The default merge algorithm for `configurable()` properties, based on [merge](https://bryntum.com/docs/gantt/api/#Core/helper/ObjectHelper#function-merge-static).
* `items` : Similar to `merge`, but allows reordering (see `ObjectHelper.mergeItems`).
* `objects` : The same as to `merge` except this method promotes `true` to an empty object.
* 'classList' : Incoming strings are converted to an object where the string is a property name with a truthy value.
* `replace` : Always returns `newValue` to replace the super class value with the derived class value, or the class value with the instance value.

## Functions

Functions are methods available for calling on the class

[get](https://bryntum.com/docs/gantt/api/Core/Config#function-get-static)
Returns the `Config` instance for the given `name` and `options`.

[convert](https://bryntum.com/docs/gantt/api/Core/Config#function-convert)
This method converts a value presented to the setter to the value that will be processed by config hook methods (e.g., `changeFoo` and `updateFoo`).

[equal](https://bryntum.com/docs/gantt/api/Core/Config#function-equal)
This method compares two values for semantic equality. By default, this is based on the `===` operator. This is often overridden for configs that accept `Date` or array values.

[extend](https://bryntum.com/docs/gantt/api/Core/Config#function-extend)
Extends this config with a given additional set of options. These objects are just prototype extensions of this instance.

[define](https://bryntum.com/docs/gantt/api/Core/Config#function-define)
Defines the property on a given target object via `Reflect.defineProperty()`. If the object has its own getter, it will be preserved. It is invalid to define a setter.

[defineInitter](https://bryntum.com/docs/gantt/api/Core/Config#function-defineInitter)
Defines the property initter on the `target`. This is a property getter/setter that propagates the configured value when the property is read.

[makeArrayEquals](https://bryntum.com/docs/gantt/api/Core/Config#function-makeArrayEquals-static)
Returns an equality function for arrays of a base type, for example `'date'`.

[makeCacheKey](https://bryntum.com/docs/gantt/api/Core/Config#function-makeCacheKey-static)
Returns the key to use in the Config `cache`.

[makeDescriptor](https://bryntum.com/docs/gantt/api/Core/Config#function-makeDescriptor)
Creates and returns a property descriptor for this config suitable to be passed to `Reflect.defineProperty()`.

[makeInitter](https://bryntum.com/docs/gantt/api/Core/Config#function-makeInitter)
Creates and returns a property descriptor for this config's initter suitable to pass to `Reflect.defineProperty()`.

[removeInitter](https://bryntum.com/docs/gantt/api/Core/Config#function-removeInitter)
Removes the property initter and restores the instance to its original form.

[merge](https://bryntum.com/docs/gantt/api/Core/Config#function-merge)
This method combines (merges) two config values. This is called in two cases:

* When a derived class specifies the value of a config defined in a super class.
* When a value is specified in the instance config object.
