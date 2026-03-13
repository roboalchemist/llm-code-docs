# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/util/DynamicObject.md

# [DynamicObject](https://bryntum.com/docs/gantt/api/Core/util/DynamicObject)

This class is used to manage dynamic creation and configuration of individual properties of an object. This pattern is used to allow the names of an object to each represent a dynamically instantiated object. For example, the `features` config of Calendar is defined like so:

```
 class Calendar extends ... {
     static configurable = {
         features : {
             drag : {
                 // configs for Drag feature
             }
         }
     };
 }
```

This class is used to manage the `features` objects in the above case. The `drag` property value is promoted from the config object defined by the class and user instance on first request. Like config properties themselves, these features may access other features during their initialization. These accesses are trapped by this class to ensure the config object is promoted to an instantiated instance.

A [factory](https://bryntum.com/docs/gantt/api/#Core/util/DynamicObject#config-factory) is provided to this object to allow it to create instances from names like `'drag'`.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[cleanup](https://bryntum.com/docs/gantt/api/Core/util/DynamicObject#config-cleanup)
Optional function that will be passed an instance prior to destroying it.

[configName](https://bryntum.com/docs/gantt/api/Core/util/DynamicObject#config-configName)
Optional name of the config property managed by this instance. If changes are made directly, this property is used to run the `onConfigChange` method of the `owner`.

[created](https://bryntum.com/docs/gantt/api/Core/util/DynamicObject#config-created)
Optional function to call as instances are created. Each new instance is passed to this function.

[factory](https://bryntum.com/docs/gantt/api/Core/util/DynamicObject#config-factory)
The [factory](https://bryntum.com/docs/gantt/api/#Core/mixin/Factoryable) to use to create instances.

[inferType](https://bryntum.com/docs/gantt/api/Core/util/DynamicObject#config-inferType)
By default, the name of the member is used for the type. Set this config to `true` to also allow the config object for a property to contain a `type` property. Set this to `false` to ignore the name of the member and rely on the [factory](https://bryntum.com/docs/gantt/api/#Core/util/DynamicObject#config-factory) to process the config object.

[owner](https://bryntum.com/docs/gantt/api/Core/util/DynamicObject#config-owner)
The owning object to pass along to the instances as the `ownerName` property.

[ownerName](https://bryntum.com/docs/gantt/api/Core/util/DynamicObject#config-ownerName)
The property name by which to store the `owner` on each instance.

[proxyable](https://bryntum.com/docs/gantt/api/Core/util/DynamicObject#config-proxyable)
Set to `false` to prevent using a `Proxy` even if that JavaScript platform feature is available. Using a `Proxy` is ideal because it allows for all forms of access to the dynamic properties to be handled instead of only those that have predefined configuration values.

[setup](https://bryntum.com/docs/gantt/api/Core/util/DynamicObject#config-setup)
Optional function that will be passed a config object prior to instantiating an object. This function can either modify the passed object or return a new object.

[transform](https://bryntum.com/docs/gantt/api/Core/util/DynamicObject#config-transform)
Optional function that will be passed a raw config object prior to processing and the value it returns replaces the raw value. This function is used to transform strings or arrays (for example) into proper config objects.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[defaults](https://bryntum.com/docs/gantt/api/Core/util/DynamicObject#property-defaults)
Holds config objects for each defined object. These are used to hold class and instance config values and use them to create instances on first request, or when `flush()` is called. Further, if the instance is initially assigned instead of retrieved, these values act as the defaults for the instance and are combined with those provided in the assignment.

[instances](https://bryntum.com/docs/gantt/api/Core/util/DynamicObject#property-instances)
This object holds the actual instances that are retrieved by the dynamic accessor or `Proxy`.

[object](https://bryntum.com/docs/gantt/api/Core/util/DynamicObject#property-object)
The object that contains the dynamic accessors for each instance. This object is not used when using a `Proxy`.

[proxy](https://bryntum.com/docs/gantt/api/Core/util/DynamicObject#property-proxy)
Returns the `Proxy` instance used to manage dynamic assignments. If the JavaScript platform does not support the `Proxy` class, this will be `null`.

[target](https://bryntum.com/docs/gantt/api/Core/util/DynamicObject#property-target)
Returns the object that contains the dynamic properties. This may be a `Proxy` instance or an object with getter and setter accessors.

## Functions

Functions are methods available for calling on the class

[define](https://bryntum.com/docs/gantt/api/Core/util/DynamicObject#function-define)
This method establishes the initial definition of a dynamic property. When using a `Proxy`, this method simply needs to cache away the initial config for use by the getter. When `Proxy` is unavailable, this method will also defined a getter/setter to intercept access to the dynamic property.

[defineProp](https://bryntum.com/docs/gantt/api/Core/util/DynamicObject#function-defineProp)
Define the get/set accessors for `name` on our `object` or its prototype.

[flush](https://bryntum.com/docs/gantt/api/Core/util/DynamicObject#function-flush)
Ensures that all defined members are touched to trigger their creation.

[get](https://bryntum.com/docs/gantt/api/Core/util/DynamicObject#function-get)
Returns (lazily creating as necessary) the value of a dynamic property given its name.

[set](https://bryntum.com/docs/gantt/api/Core/util/DynamicObject#function-set)
Sets the value of a dynamic property given its name and value.

[setDefaults](https://bryntum.com/docs/gantt/api/Core/util/DynamicObject#function-setDefaults)
Stores the default config values for use in the factory reconfiguration process.

[update](https://bryntum.com/docs/gantt/api/Core/util/DynamicObject#function-update)
Updates the members of `object` based on the provided configuration.
