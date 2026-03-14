# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/mixin/Pluggable.md

# [Pluggable](https://bryntum.com/docs/gantt/api/Core/mixin/Pluggable)

Enables using plugins for a class by specifying property plugins as an array of plugin classes. If only a single plugin is used, just give the plugin class instead of an array. This class isn't required for using plugins, just makes it easier. Without mixin you can otherwise use `InstancePlugin.initPlugins(this, PluginClass)`.

```
new Store({
  plugins: [PluginClass, ...]
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[plugins](https://bryntum.com/docs/gantt/api/Core/mixin/Pluggable#config-plugins)
Specify plugins (an array of classes) in config

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isPluggable](https://bryntum.com/docs/gantt/api/Core/mixin/Pluggable#property-isPluggable)
Identifies an object as an instance of [Pluggable](https://bryntum.com/docs/gantt/api/#Core/mixin/Pluggable) class, or subclass thereof.

[isPluggable](https://bryntum.com/docs/gantt/api/Core/mixin/Pluggable#property-isPluggable-static)
Identifies an object as an instance of [Pluggable](https://bryntum.com/docs/gantt/api/#Core/mixin/Pluggable) class, or subclass thereof.

[plugins](https://bryntum.com/docs/gantt/api/Core/mixin/Pluggable#property-plugins)
Map of applied plugins

## Functions

Functions are methods available for calling on the class

[initPlugins](https://bryntum.com/docs/gantt/api/Core/mixin/Pluggable#function-initPlugins)
Template method which may be implemented in subclasses to initialize any plugins. This method is empty in the `Pluggable` base class.

[addPlugins](https://bryntum.com/docs/gantt/api/Core/mixin/Pluggable#function-addPlugins)
Adds plugins to an instance.

[addPlugin](https://bryntum.com/docs/gantt/api/Core/mixin/Pluggable#function-addPlugin)
Adds a plugin to an instance, with a configuration object passed to the plugin constructor

[hasPlugin](https://bryntum.com/docs/gantt/api/Core/mixin/Pluggable#function-hasPlugin)
Checks if instance has plugin.

[getPlugin](https://bryntum.com/docs/gantt/api/Core/mixin/Pluggable#function-getPlugin)
Get a plugin instance.
