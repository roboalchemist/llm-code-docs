# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/Base.md

# [Base](https://bryntum.com/docs/gantt/api/Core/Base)

Base class for all configurable classes.

Subclasses do not have to implement a constructor with its restriction of having to call super() before there is a `this` reference. Subclasses instead implement a `construct` method which is called by the `Base` constructor. This may call its `super` implementation at any time.

The `Base` constructor applies all configs to properties of the new instance. The instance will have been configured after the `super.construct(config)` is called.

See the Class System documentation in the guides for more information.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[declarable](https://bryntum.com/docs/gantt/api/Core/Base#property-declarable-static)
A class property getter to add additional, special class properties.

For example, a class adds a `declarable` class property like so:

```
 class Something extends Base {
     static get declarable() {
         return ['extra'];
     }

     static setupExtra(cls, meta) {
         // use cls.extra
     }
 }
```

A derived class can then specify this property like so:

```
 class Derived extends Something {
     static get extra() {
         // return extra information
     }
 }
```

When the `Derived` class is initialized, the `setupExtra()` method is called and `Derived` is passed as the argument. It is also the `this` pointer, but the parameter is minifiable. The second argument passed is the `$meta` object for the class.

Classes are initialized at the first occurrence of the following:

* An instance is created
* The class `$meta` property is accessed

[configurable](https://bryntum.com/docs/gantt/api/Core/Base#property-configurable-static)
A class property getter for the configuration properties of the class, which can be overridden by configurations passed at construction time.

Unlike a normal `static` property, this property is only ever used for the class that defines it (as in, `hasOwnProperty`). It is retrieved for all classes in a class hierarchy, to gather their configs individually and then combine them with those of derived classes.

For example, a `Label` might declare a `text` config like so:

```
 class Label extends Base {
     static configurable = {
         text : null
     };
 }
```

The `text` config is automatically inherited by classes derived from Label. By implementing `get configurable()`, derived classes can change the default value of inherited configs, or define new configs, or both.

When a config property is declared in this way, the class author can also implement either of two special methods that will be called when the config property is assigned a new value:

* `changeText()`
* `updateText()`

In the example above, the `Label` class could implement a `changeText()` method, an `updateText()` method, or both. The generated property setter ensures these methods will be called when the `text` property is assigned.

The generated setter (for `text` in this example) performs the following steps:

* If the class defines a `changeText()` method, call it passing the new value and the current value: `changeText(newText, oldText)`.  
    Then:
  * If `changeText()` exits without returning a value (i.e., `undefined`), exit and do nothing further. The assumption is that the changer method has done all that is required.
  * Otherwise, the return value of `changeText()` replaces the incoming value passed to the setter.
* If the new value (or the value returned by `changeText()`) is `!==` to the current value:
  * Update the stored config value in `this._text`.
  * If the class defines an `updateText()` method, call it passing the new value and the previous value. `updateText(newText, oldText)`

#### Resolving a value from an owner

By specifying a value starting with `'up.'` for a config, the config system will resolve that value by examining the ownership hierarchy. It will walk up the hierarchy looking for a property matching the name (or dot separated path) after 'up.'. If one is found, the value will be read and used as the initial value.

```
class Parent extends Base {
    static get configurable() {
        return [
          'importantValue'
        ]
    }
}

class Child extends Base {
    static get configurable() {
        return [
          'value'
        ]
    }
}

const parent = new Parent({
    importantValue : 123
});

const child = new Child({
    owner : parent,
    // Will be resolved from the owner
    value : 'up.importantValue'
});

console.log(child.value); // logs 123
```

Please note that this is for now a one way one time binding, the value will only be read initially and not kept up to date on later changes.

#### Value Merging

When a config property value is an object, the value declared by the base class is merged with values declared by derived classes and the value passed to the constructor.

```
 class Example extends Base {
     static configurable = {
         config : {
             foo : 1,
             bar : 2
         }
     };
 }

 class Example2 extends Example {
     static configurable = {
         config : {
             bar : 42,
             zip : 'abc'
         }
     };
 }

 let ex = new Example2({
     config : {
         zip : 'xyz'
     }
 });
```

The result of the merge would set `config` to:

```
 ex.foo = {
     foo : 1,    // from Example
     bar : 42,   // from Example2
     zip : 'xyz' // from constructor
 }
```

#### Config Options

Some config properties require additional options such as declarative information about the config that may be useful to automate some operation. Consider a `Button`. It could declare that its `text` config affects the rendered HTML by applying a `render` property to the config definition. Its base class could then examine the config definition to find this property.

To support this, config options ca be declared like so:

```
 class Button extends Widget {
     static configurable = {
         text : {
             value   : null,
             $config : {
                 render : true
             }
         }
     };
 }
```

The `$config` property can alternatively be just the names of the options that should be enabled (set to `true`).

For example, the following is equivalent to the above:

```
 class Button extends Widget {
     static configurable = {
         text : {
             value   : null,
             $config : 'render'
         }
     };
```

#### Default Value

It is common to set a config to a `null` value to take advantage of internal optimizations for `null` values. In most cases the fact that this produces `undefined` as the actual initial value of the config is acceptable. When this is not acceptable, a config can be declared like so:

```
 class Widget {
     static configurable = {
         disabled : {
             $config : null,
             value   : null,
             default : false
         }
     };
```

The `default` property above determines the value of the config while still gaining the benefits of minimal processing due to the `null` value of the `value` property.

[defaultConfig](https://bryntum.com/docs/gantt/api/Core/Base#property-defaultConfig-static)
A legacy class property getter for the default configuration of the class, which can be overridden by configurations passed at construction time. We recommend using `configurable` instead.

Unlike a normal `static` property, this property is only ever used for the class that defines it (as in, `hasOwnProperty`). It is retrieved for all classes in a class hierarchy, to gather their configs individually and then combine them with those of derived classes.

For example, a `Store` might declare its `url` config like so:

```
 class Store extends Base {
     static get defaultConfig() {
         return {
             url : null
         };
     }
 }
```

The `url` config is automatically inherited by classes derived from Store. By implementing `get defaultConfig()`, derived classes can change the default value of inherited configs, or define new configs, or both. When defining new configs, however, `configurable` is preferred.

Config properties introduced to a class by this declaration do not participate in value merging and do not get a generated setter. Config properties introduced by a base class using `configurable` can be set to a different value using `defaultConfig` and in doing so, the values will be merged as appropriate for `configurable`.

[properties](https://bryntum.com/docs/gantt/api/Core/Base#property-properties-static)
A class property getter for the default values of internal properties for this class.

[emptyObject](https://bryntum.com/docs/gantt/api/Core/Base#property-emptyObject)
An empty object that can be used as a default value.

[emptyArray](https://bryntum.com/docs/gantt/api/Core/Base#property-emptyArray)
An empty array that can be used as a default value.

[config](https://bryntum.com/docs/gantt/api/Core/Base#property-config)
Returns a _copy_ of the full configuration which was used to configure this object.

[$meta](https://bryntum.com/docs/gantt/api/Core/Base#property-$meta)
The class's [meta](https://bryntum.com/docs/gantt/api/#Core/Base#property-$meta-static) object.

[$meta](https://bryntum.com/docs/gantt/api/Core/Base#property-$meta-static)
An object owned by this class that does not share properties with its super class.

This object may contain other properties which are added as needed and are not documented here.

[isConstructing](https://bryntum.com/docs/gantt/api/Core/Base#property-isConstructing)
This property is set to `true` before the `constructor` returns.

[isDestroyed](https://bryntum.com/docs/gantt/api/Core/Base#property-isDestroyed)
This property is set to `true` by [destroy](https://bryntum.com/docs/gantt/api/#Core/Base#function-destroy) after destruction.

It is also one of the few properties that remains on the object after returning from `destroy()`. This property is often checked in code paths that may encounter a destroyed object (like some event handlers) or in the destruction path during cleanup.

[isDestroying](https://bryntum.com/docs/gantt/api/Core/Base#property-isDestroying)
This property is set to `true` on entry to the [destroy](https://bryntum.com/docs/gantt/api/#Core/Base#function-destroy) method. It remains on the objects after returning from `destroy()`. If [isDestroyed](https://bryntum.com/docs/gantt/api/#Core/Base#property-isDestroyed) is `true`, this property will also be `true`, so there is no need to test for both (for example, `comp.isDestroying || comp.isDestroyed`).

## Functions

Functions are methods available for calling on the class

[constructor](https://bryntum.com/docs/gantt/api/Core/Base#function-constructor)
Base constructor, passes arguments to [construct](https://bryntum.com/docs/gantt/api/#Core/Base#function-construct).

[new](https://bryntum.com/docs/gantt/api/Core/Base#function-new-static)
Factory version of the Base constructor. Merges all arguments to create a config object that is passed along to the constructor.

[construct](https://bryntum.com/docs/gantt/api/Core/Base#function-construct)
Base implementation applies configuration.

Subclasses need only implement this if they have to initialize instance specific properties required by the class. Often a `construct` method is unnecessary. All initialization of incoming configuration properties can be done in a `set propName` implementation.

[destroy](https://bryntum.com/docs/gantt/api/Core/Base#function-destroy-static)
Destroys the provided objects by calling their [destroy](https://bryntum.com/docs/gantt/api/#Core/Base#function-destroy) method. Skips empty values or objects that are already destroyed.

```
Base.destroy(myButton, toolbar1, helloWorldMessageBox);
```

[destroy](https://bryntum.com/docs/gantt/api/Core/Base#function-destroy)
Destroys this object.

This is primarily accomplished by calling [doDestroy](https://bryntum.com/docs/gantt/api/#Core/Base#function-doDestroy), however, prior to calling `doDestroy`, [isDestroying](https://bryntum.com/docs/gantt/api/#Core/Base#property-isDestroying) is set to `true`. After [doDestroy](https://bryntum.com/docs/gantt/api/#Core/Base#function-doDestroy) returns, [isDestroyed](https://bryntum.com/docs/gantt/api/#Core/Base#property-isDestroyed) is set to `true`.

Do not override this method in subclasses. To provide class-specific cleanup, implement [doDestroy](https://bryntum.com/docs/gantt/api/#Core/Base#function-doDestroy) instead.

[_thisIsAUsedExpression](https://bryntum.com/docs/gantt/api/Core/Base#function-_thisIsAUsedExpression)
This method is required to help `unused` getters to survive production build process. Some tools, like angular, will remove `unused` code in production build, making our side-effected getters behind, breaking code heavily.

[startConfigure](https://bryntum.com/docs/gantt/api/Core/Base#function-startConfigure)
Base implementation so that all subclasses and mixins may safely call super.startConfigure.

This is called by the Base class before setting configuration properties, but after the active initial getters have been set, so all configurations are available.

This method allows all classes in the hierarchy to force some configs to be evaluated before others.

[finishConfigure](https://bryntum.com/docs/gantt/api/Core/Base#function-finishConfigure)
Base implementation so that all subclasses and mixins may safely call super.finishConfigure.

This is called by the Base class before exiting the [configure](https://bryntum.com/docs/gantt/api/#Core/Base#function-configure) method.

At this point, all configs have been applied, but the `isConfiguring` property is still set.

This method allows all classes in the hierarchy to inject functionality into the config phase.

[afterConfigure](https://bryntum.com/docs/gantt/api/Core/Base#function-afterConfigure)
Base implementation so that all subclasses and mixins may safely call `super.afterConfigure`. This is called by the Base class after the [configure](https://bryntum.com/docs/gantt/api/#Core/Base#function-configure) method has been called. At this point, all configs have been applied.

This method allows all classes in the hierarchy to inject functionality either before or after the super.afterConstruct();

[afterConstruct](https://bryntum.com/docs/gantt/api/Core/Base#function-afterConstruct)
Base implementation so that all subclasses and mixins may safely call super.afterConstruct.

This is called by the Base class after the [construct](https://bryntum.com/docs/gantt/api/#Core/Base#function-construct) method has been called.

At this point, all configs have been applied.

This method allows all classes in the hierarchy to inject functionality either before or after the super.afterConstruct();

[animateProperty](https://bryntum.com/docs/gantt/api/Core/Base#function-animateProperty)
Changes the value of a numeric property of this object smoothly over the specified duration.

[callback](https://bryntum.com/docs/gantt/api/Core/Base#function-callback)
Provides a way of calling callbacks which may have been specified as the _name_ of a function and optionally adds scope resolution.

For example, if the callback is specified as a string, then if it is prefixed with `'this.'` then the function is resolved in this object. This is useful when configuring listeners at the class level.

If the callback name is prefixed with `'up.'` then the ownership hierarchy is queried using the `owner` property until an object with the named function is present, then the named function is called upon that object.

If a named function is not found, an error is thrown. If the function should be only called when present, and may not be present, add a `?` as a suffix.

[resolveCallback](https://bryntum.com/docs/gantt/api/Core/Base#function-resolveCallback)
Provides a way of locating callbacks which may have been specified as the _name_ of a function and optionally adds scope resolution.

For example, if the callback is specified as a string, then if it is prefixed with `'this.'` then the function is resolved in this object. This is useful when configuring listeners at the class level.

If the callback name is prefixed with `'up.'` then the ownership hierarchy is queried using the `owner` property until an object with the named function is present, then the named function is called upon that object.

[delay](https://bryntum.com/docs/gantt/api/Core/Base#function-delay)
Delays the execution of the passed function by the passed time quantum, or if the time is omitted or not a number, delays until the next animation frame. Note that this will use [setTimeout](https://bryntum.com/docs/gantt/api/#Core/mixin/Delayable#function-setTimeout) || [requestAnimationFrame](https://bryntum.com/docs/gantt/api/#Core/mixin/Delayable#function-requestAnimationFrame) if this class mixes in `Delayable`, otherwise it uses the global methods. The function will be called using `this` object as its execution scope.

[doDestroy](https://bryntum.com/docs/gantt/api/Core/Base#function-doDestroy)
Classes implement this method to provide custom cleanup logic before calling `super.doDestroy()`. The general pattern is as follows:

```
 class Foo extends Base {
     doDestroy() {
         // perform custom cleanup

         super.doDestroy();
     }
 }
```

This method is called by [destroy](https://bryntum.com/docs/gantt/api/#Core/Base#function-destroy) which also prevents multiple calls from reaching `doDestroy`. Prior to calling `doDestroy`, [isDestroying](https://bryntum.com/docs/gantt/api/#Core/Base#property-isDestroying) is set to `true`. Upon return, the object is fully destructed and [isDestroyed](https://bryntum.com/docs/gantt/api/#Core/Base#property-isDestroyed) is set to `true`.

Do not call this method directly. Instead call [destroy](https://bryntum.com/docs/gantt/api/#Core/Base#function-destroy).

[destroyProperties](https://bryntum.com/docs/gantt/api/Core/Base#function-destroyProperties)
Destroys the named properties if they have been initialized, and if they have a `destroy` method. Deletes the property from this object. For example:

```
 this.destroyProperties('store', 'resourceStore', 'eventStore', 'dependencyStore', 'assignmentStore');
```

[configure](https://bryntum.com/docs/gantt/api/Core/Base#function-configure)
Called by the Base constructor to apply configs to this instance. This must not be called.

[bindConfigs](https://bryntum.com/docs/gantt/api/Core/Base#function-bindConfigs)
Creates a binding between the specified config properties of this object and the specified `target` object. Changes to these config properties of this object will be reflected to the `target` object as they occur, and (optionally), vise-versa.

Returns a function to call to remove the binding.

[getConfig](https://bryntum.com/docs/gantt/api/Core/Base#function-getConfig)
Returns the value of the specified config property. This is a method to allow property getters to be explicitly called in a way that does not get optimized out.

The following triggers the getter call, but optimizers will remove it:

```
 inst.foo;   // also raises "expression has no side-effects" warning
```

Instead, do the following to trigger a getter:

```
 inst.getConfig('foo');
```

[updateConfiguration](https://bryntum.com/docs/gantt/api/Core/Base#function-updateConfiguration)
This is intended to set a block of configs _during_ configuration. It is not intended to be used outside of the configuration phase.

If any of the properties are not yet ingested from the configuration object, they will be set and ingested in the normal order.

Properties which are already ingested are set immediately.

[setConfig](https://bryntum.com/docs/gantt/api/Core/Base#function-setConfig)
Sets configuration options this object with all the properties passed in the parameter object. Timing is taken care of. If the setter of one config is called first, and references the value of another config which has not yet been set, that config will be set just in time, and the _new_ value will be used.

[hasConfig](https://bryntum.com/docs/gantt/api/Core/Base#function-hasConfig)
Returns `true` if this instance has a non-null value for the specified config. This will not activate a lazy config.

[hasConfigPath](https://bryntum.com/docs/gantt/api/Core/Base#function-hasConfigPath-static)
Determines if the specified config property exists in an instance of [Base](https://bryntum.com/docs/gantt/api/#Core/Base)

[peekConfig](https://bryntum.com/docs/gantt/api/Core/Base#function-peekConfig)
Returns the value of an uningested config _without_ ingesting the config or transforming it from its raw value using its `changeXxxxx` method.

[triggerConfig](https://bryntum.com/docs/gantt/api/Core/Base#function-triggerConfig)
Ensures that the specified config is initialized if it is needed. If there is a config value specified, and it was initialized by this call, this method returns `true`. If there was a config value specified, and it was already initialized, this method returns `false`. If there was no value specified for the given config, this method returns `null`.

This is not the same as just reading the property, because some property getters exist that do not actually just read the config value back, but instead produce some result. Reading such properties to incidentally trigger a possible config initializer can lead to incorrect results. For example, the Combo items config.

[triggerConfigs](https://bryntum.com/docs/gantt/api/Core/Base#function-triggerConfigs)
This call will activate any pending [lazy](https://bryntum.com/docs/gantt/api/#Core/Config#config-lazy) configs that were assigned a string value equal to the `group` parameter.

[onConfigChange](https://bryntum.com/docs/gantt/api/Core/Base#function-onConfigChange)
This method is called when any config changes.

[downloadTestCase](https://bryntum.com/docs/gantt/api/Core/Base#function-downloadTestCase)
Experimental helper function, extracts the currently used configs and wraps them as an app, downloading the resulting JS file.

This function is intended to simplify creating test cases for issue reporting on Bryntum's support forum.

[initClass](https://bryntum.com/docs/gantt/api/Core/Base#function-initClass-static)
Registers this class type with its Factory

[onClassMixedIn](https://bryntum.com/docs/gantt/api/Core/Base#function-onClassMixedIn-static)
This optional class method is called when a class is mixed in using the [mixin()](https://bryntum.com/docs/gantt/api/#Core/Base#function-mixin-static) method.

[mergeConfigs](https://bryntum.com/docs/gantt/api/Core/Base#function-mergeConfigs-static)
Returns the merge of the `baseConfig` and `config` config objects based on the configs defined by this class.

[mixin](https://bryntum.com/docs/gantt/api/Core/Base#function-mixin-static)
Applies one or more `mixins` to this class and returns the produced class constructor.

For example, instead of writing this:

```
 class A extends Delayable(Events(Localizable(Base))) {
     // ...
 }
```

Using this method, one would write this:

```
 class A extends Base.mixin(Localizable, Events, Delayable) {
     // ...
 }
```

If one of the mixins specified has already been mixed into the class, it will be ignored and not mixed in a second time.

[setupClass](https://bryntum.com/docs/gantt/api/Core/Base#function-setupClass-static)
This method is called only once for any class. This can occur when the first instance is created or when the `$meta` object is first requested.

[setupConfigs](https://bryntum.com/docs/gantt/api/Core/Base#function-setupConfigs-static)
This method is called as part of `setupClass()`. It will process the `configurable()` return object and the `defaultConfig` return object.

[getDefaultConfiguration](https://bryntum.com/docs/gantt/api/Core/Base#function-getDefaultConfiguration-static)
Gets the full [defaultConfig](https://bryntum.com/docs/gantt/api/#Core/Base#property-defaultConfig-static) block for this object's entire inheritance chain all the way up to but not including [Base](https://bryntum.com/docs/gantt/api/#Core/Base)

[getDefaultConfiguration](https://bryntum.com/docs/gantt/api/Core/Base#function-getDefaultConfiguration)
Gets the full [defaultConfig](https://bryntum.com/docs/gantt/api/#Core/Base#property-defaultConfig-static) block for the entire inheritance chain for this class all the way up to but not including [Base](https://bryntum.com/docs/gantt/api/#Core/Base)

[getProperties](https://bryntum.com/docs/gantt/api/Core/Base#function-getProperties)
Gets the full [properties](https://bryntum.com/docs/gantt/api/#Core/Base#property-properties-static) block for this class's entire inheritance chain all the way up to but not including [Base](https://bryntum.com/docs/gantt/api/#Core/Base)

[applyDefaults](https://bryntum.com/docs/gantt/api/Core/Base#function-applyDefaults-static)
Merges the provided default configuration values with the existing defaults for this class (and its subclasses).

This method allows you to define additional or override existing default property values that apply to all instances of the class.

```
// All my input fields should be clearable
 Field.applyDefaults({
     clearable : true
});
```

[classHierarchy](https://bryntum.com/docs/gantt/api/Core/Base#function-classHierarchy)
Used by the Widget and GridFeatureManager class internally. Returns the class hierarchy of this object starting from the `topClass` class (which defaults to `Base`).

For example `classHierarchy(Widget)` on a Combo would yield `[Widget, Field, TextField, PickerField, Combo]`

[isOfTypeName](https://bryntum.com/docs/gantt/api/Core/Base#function-isOfTypeName-static)
Checks if an obj is of type using object's $$name property and doing string comparison of the property with the type parameter.

[detachListeners](https://bryntum.com/docs/gantt/api/Core/Base#function-detachListeners)
Removes all event listeners that were registered with the passed names.

[trackDetacher](https://bryntum.com/docs/gantt/api/Core/Base#function-trackDetacher)
Tracks a detacher function for the specified listener name.

[untrackDetachers](https://bryntum.com/docs/gantt/api/Core/Base#function-untrackDetachers)
Removes all detacher functions for the specified `Events` object. This is called by the `removeAllListeners` method on that object which is typically called by its `destroy` invocation.
