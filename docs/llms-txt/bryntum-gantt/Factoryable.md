# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/mixin/Factoryable.md

# [Factoryable](https://bryntum.com/docs/gantt/api/Core/mixin/Factoryable)

This mixin is applied to base classes of a type that will be dynamically created by type name aliases.

```
 class Layout extends Base.mixin(Factoryable) {
     static get factoryable() {
         return {
             defaultType : 'default'
         };
     }

     static get type() {
         return 'default';
     }
 }

 class Fit extends Layout {
     static get type() {
         return 'fit';
     }
 }
```

Once a family of classes has been defined, instances are created using the `create()` method:

```
 const layout = Layout.create(config);
```

In the above example, `config` can be a type name (such as "fit") or a config object with a `type` property that holds the type name.

Factories can also extend other factories. For example, one factory creates objects that are useful across a wide range of consumers, and a second factory creates objects for a more specialized consumer. If that specialized consumer can also consume objects from the first factory, then the second factory can specify this relationship:

```
 class General extends Base.mixin(Factoryable) {
     ...
 }

 class Specialized extends Base.mixin(Factoryable) {
     static get factoryable() {
         return {
             extends : General,
             ...
         };
     }
 }
```

The `extends` factoryable option can be either a class that mixes in `Factoryable` or an array of such classes.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isFactoryable](https://bryntum.com/docs/gantt/api/Core/mixin/Factoryable#property-isFactoryable)
Identifies an object as an instance of [Factoryable](https://bryntum.com/docs/gantt/api/#Core/mixin/Factoryable) class, or subclass thereof.

[isFactoryable](https://bryntum.com/docs/gantt/api/Core/mixin/Factoryable#property-isFactoryable-static)
Identifies an object as an instance of [Factoryable](https://bryntum.com/docs/gantt/api/#Core/mixin/Factoryable) class, or subclass thereof.

[factoryable](https://bryntum.com/docs/gantt/api/Core/mixin/Factoryable#property-factoryable-static)
This property getter returns options that control the factory process. This property getter must be defined by the class that mixes in `Factoryable` in order to initialize the factory properly.

```
 static get factoryable() {
     return {
         defaultType : 'default'
     };
 }
```

If there are no special options to provide, this method can return nothing (`undefined`):

```
 static get factoryable() {
     // initialize the factory with all default options
 }
```

[alias](https://bryntum.com/docs/gantt/api/Core/mixin/Factoryable#property-alias-static)
One or more additional type name aliases for this class. This can be useful for renaming and maintaining a previous type name.

```
 class Fit extends Layout {
     static type = 'fit';

     static alias = 'fill';
 }
```

[type](https://bryntum.com/docs/gantt/api/Core/mixin/Factoryable#property-type-static)
The (canonical) type name for this class by which instances can be created using the static [create()](https://bryntum.com/docs/gantt/api/#Core/mixin/Factoryable#function-create-static) method.

## Functions

Functions are methods available for calling on the class

[register](https://bryntum.com/docs/gantt/api/Core/mixin/Factoryable#function-register-static)
Registers a class (`cls`) associated with the given `type`.

[isA](https://bryntum.com/docs/gantt/api/Core/mixin/Factoryable#function-isA-static)
Returns `true` if the passed instance is of the passed type or of a derived class.

[isType](https://bryntum.com/docs/gantt/api/Core/mixin/Factoryable#function-isType-static)
Returns `true` if the passed instance is of the passed type.

[create](https://bryntum.com/docs/gantt/api/Core/mixin/Factoryable#function-create-static)
Creates an instance from this factory, given the type name or a config object.

[reconfigure](https://bryntum.com/docs/gantt/api/Core/mixin/Factoryable#function-reconfigure-static)
Reconfigures an optional existing instance based on the provided config and returns the correctly configured instance. This will be the `existingInstance` if the `config` does not specify a different type.

If `config` is `null` (or simply falsy), this method will destroy the `existingInstance` (if any) and return `null`.

If there is no `existingInstance`, the config must specify a type. That is, it must be a string (the type name) or an object containing a `type` property, the `defaultType` must be provided or the factory itself must have a `defaultType` specified (see [factoryable](https://bryntum.com/docs/gantt/api/#Core/mixin/Factoryable#property-factoryable-static)).

When an `existingInstance` is provided and a type is specified, the instance will be reconfigured via `setConfig` if it is of that type. Otherwise, the `existingInstance` is destroyed (if it is owned by the `options.owner`) and a new instance of the correct type is created.

[resolveType](https://bryntum.com/docs/gantt/api/Core/mixin/Factoryable#function-resolveType-static)
This method returns the constructor of the class registered for the given type name.
