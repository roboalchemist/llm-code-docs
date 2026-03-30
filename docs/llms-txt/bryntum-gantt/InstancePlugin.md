# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/mixin/InstancePlugin.md

# [InstancePlugin](https://bryntum.com/docs/gantt/api/Core/mixin/InstancePlugin)

Base class for plugins. Published functions will be available from the other class. `this` in published functions is referenced to the plugin, access the other class using `this.client`.

Observe that plugin doesn't apply itself on class level but instead on instance level. Plugin is its own instance that can have own functions and data that is not exposed to target class.

Functions can be published in four ways:

* `assign` (when function is not already available on target)
* `before` (when function is already available on target, will be called before original function)
* `after` (when function is already available on target, will be called after original function)
* `override` (replaces function on target, but old function can be reached)

To configure which functions get published and in what way, specify `pluginConfig` getter on plugin:

```
class Sort extends InstancePlugin {
  static get pluginConfig {
     return {
         before   : ['init'],
         after    : ['destroy', 'onElementClick'],
         override : ['render']
     };
  }
}
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[disabled](https://bryntum.com/docs/gantt/api/Core/mixin/InstancePlugin#config-disabled)
The plugin/feature `disabled` state.

For a feature that is **off** by default that you want to enable later during runtime, configure it with `disabled : true`.

```
const grid = new Grid({
     features : {
         featureName : {
             disabled : true // on and disabled, can be enabled later
         }
     }
});

// enable the feature
grid.features.featureName.disabled = false;
```

If the feature is **disabled** by default, and you want to include and enable the feature, configure it as `true`:

```
const grid = new Grid({
     features : {
         featureName : true // on and enabled, can be disabled later
     }
});

// disable the feature
grid.features.featureName.disabled = true;
```

If the feature is **on** by default, but you want to turn it **off**, configure it as `false`:

```
const grid = new Grid({
     features : {
         featureName : false // turned off, not included at all
     }
});
```

If the feature is **enabled** by default and you have no need of reconfiguring it, you can omit the feature configuration.

[client](https://bryntum.com/docs/gantt/api/Core/mixin/InstancePlugin#config-client)
The widget which this plugin is to attach to.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isInstancePlugin](https://bryntum.com/docs/gantt/api/Core/mixin/InstancePlugin#property-isInstancePlugin)
Identifies an object as an instance of [InstancePlugin](https://bryntum.com/docs/gantt/api/#Core/mixin/InstancePlugin) class, or subclass thereof.

[isInstancePlugin](https://bryntum.com/docs/gantt/api/Core/mixin/InstancePlugin#property-isInstancePlugin-static)
Identifies an object as an instance of [InstancePlugin](https://bryntum.com/docs/gantt/api/#Core/mixin/InstancePlugin) class, or subclass thereof.

[disabled](https://bryntum.com/docs/gantt/api/Core/mixin/InstancePlugin#property-disabled)
The plugin/feature `disabled` state.

For a feature that is **off** by default that you want to enable later during runtime, configure it with `disabled : true`.

```
const grid = new Grid({
     features : {
         featureName : {
             disabled : true // on and disabled, can be enabled later
         }
     }
});

// enable the feature
grid.features.featureName.disabled = false;
```

If the feature is **disabled** by default, and you want to include and enable the feature, configure it as `true`:

```
const grid = new Grid({
     features : {
         featureName : true // on and enabled, can be disabled later
     }
});

// disable the feature
grid.features.featureName.disabled = true;
```

If the feature is **on** by default, but you want to turn it **off**, configure it as `false`:

```
const grid = new Grid({
     features : {
         featureName : false // turned off, not included at all
     }
});
```

If the feature is **enabled** by default and you have no need of reconfiguring it, you can omit the feature configuration.

[client](https://bryntum.com/docs/gantt/api/Core/mixin/InstancePlugin#property-client)
The Widget which was passed into the constructor, which is the Widget we are providing extra services for.

[enabled](https://bryntum.com/docs/gantt/api/Core/mixin/InstancePlugin#property-enabled)
Simple wrapper for [disabled](https://bryntum.com/docs/gantt/api/#Core/mixin/InstancePlugin#property-disabled) to make optional chaining simple:

```
grid.features.myFeature?.enabled // returns true when feature exists and is enabled
```

## Functions

Functions are methods available for calling on the class

[updateKeyMap](https://bryntum.com/docs/gantt/api/Core/mixin/InstancePlugin#function-updateKeyMap)
This will merge a feature's (subclass of InstancePlugin) keyMap with it's client's keyMap.

[initPlugins](https://bryntum.com/docs/gantt/api/Core/mixin/InstancePlugin#function-initPlugins-static)
Call from another instance to add plugins to it.

```
InstancePlugin.initPlugins(this, Search, Stripe);
```

[initPlugin](https://bryntum.com/docs/gantt/api/Core/mixin/InstancePlugin#function-initPlugin-static)
Call from another instance to add a plugin to it

[applyPluginConfig](https://bryntum.com/docs/gantt/api/Core/mixin/InstancePlugin#function-applyPluginConfig)
Applies config as found in plugInto.pluginConfig, or published all if no config found.

[applyAssign](https://bryntum.com/docs/gantt/api/Core/mixin/InstancePlugin#function-applyAssign)
Applies assigning for specified functions.

[applyAfter](https://bryntum.com/docs/gantt/api/Core/mixin/InstancePlugin#function-applyAfter)
Applies after/before hooks for specified functions.

[applyOverride](https://bryntum.com/docs/gantt/api/Core/mixin/InstancePlugin#function-applyOverride)
Applies override for specified functions.

[assign](https://bryntum.com/docs/gantt/api/Core/mixin/InstancePlugin#function-assign)
Assigns specified functions.

[doAfterHook](https://bryntum.com/docs/gantt/api/Core/mixin/InstancePlugin#function-doAfterHook)
Hooks functions. When the function is called on the target class all functions in the hook chain will be called in the order they were added.

[functionChainRunner](https://bryntum.com/docs/gantt/api/Core/mixin/InstancePlugin#function-functionChainRunner)
Used to run multiple plugged in functions with the same name, see after() above. Returning false from a function will abort the hook chain.

[doDisable](https://bryntum.com/docs/gantt/api/Core/mixin/InstancePlugin#function-doDisable)
Called when disabling/enabling the plugin/feature, not intended to be called directly. To enable or disable a plugin/feature, see [disabled](https://bryntum.com/docs/gantt/api/#Core/mixin/InstancePlugin#property-disabled).

By default removes the cls of the plugin from its client. Override in subclasses to take any other actions necessary.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[disable](https://bryntum.com/docs/gantt/api/Core/mixin/InstancePlugin#event-disable)
Fired when the plugin/feature is disabled.

[enable](https://bryntum.com/docs/gantt/api/Core/mixin/InstancePlugin#event-enable)
Fired when the plugin/feature is enabled.
