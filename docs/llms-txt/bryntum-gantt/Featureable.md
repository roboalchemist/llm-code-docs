# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/mixin/Featureable.md

# [Featureable](https://bryntum.com/docs/gantt/api/Core/mixin/Featureable)

This mixin provides management of a set of features that can be manipulated via the `features` config.

The first step in using `Featureable` is to define the family of features using `Factoryable` to declare a base class for features to extend:

```
 class SuperWidgetFeature extends InstancePlugin.mixin(Factoryable) {
     static get factoryable() {
         //
     }
 }
```

The various feature classes extend the `SuperWidgetFeature` base class and call `initClass()` to register themselves:

```
 export default class AmazingSuperWidgetFeature extends SuperWidgetFeature {
     static get type() {
         return 'amazing';
     }
 }

 AmazingSuperWidgetFeature.initClass();
```

A class that supports these features via `Featureable` is declared like so:

```
 class SuperWidget extends Widget.mixin(Featureable) {
     static get featureable() {
         return {
             factory : SuperWidgetFeature
         };
     }

     static configurable = {
         // Declare the default features. These can be disabled by setting them to a falsy value. Using
         // configurable(), the value defined by this class is merged with values defined by derived classes
         // and ultimately the instance.
         features : {
             amazing : {
                 ...
             }
         }
     };
 }
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[features](https://bryntum.com/docs/gantt/api/Core/mixin/Featureable#config-features)
Specifies the features to create and associate with the instance. The keys of this object are the names of features. The values are config objects for those feature instances.

After construction, this property can be used to access the feature instances and even reconfigure them.

For example:

```
 instance.features.amazing = {
     // reconfigure this feature
 }
```

This can also be done in bulk:

```
 instance.features = {
     amazing : {
         // reconfigure this feature
     },
     // reconfigure other features
 }
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isFeatureable](https://bryntum.com/docs/gantt/api/Core/mixin/Featureable#property-isFeatureable)
Identifies an object as an instance of [Featureable](https://bryntum.com/docs/gantt/api/#Core/mixin/Featureable) class, or subclass thereof.

[isFeatureable](https://bryntum.com/docs/gantt/api/Core/mixin/Featureable#property-isFeatureable-static)
Identifies an object as an instance of [Featureable](https://bryntum.com/docs/gantt/api/#Core/mixin/Featureable) class, or subclass thereof.

[featureable](https://bryntum.com/docs/gantt/api/Core/mixin/Featureable#property-featureable-static)
This property getter returns options that control feature management for the derived class. This property getter must be defined by the class that mixes in `Featureable` in order to initialize the class properly.

```
 class SuperWidget extends Widget.mixin(Featureable) {
     static get featureable() {
         return {
             factory : SuperWidgetFeature
         };
     }
     ...
 }
```

## Functions

Functions are methods available for calling on the class

[hasFeature](https://bryntum.com/docs/gantt/api/Core/mixin/Featureable#function-hasFeature)
Returns `true` if the specified feature is active for this instance and `false` otherwise.
