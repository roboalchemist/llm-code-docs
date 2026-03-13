# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/mixin/State.md

# [State](https://bryntum.com/docs/gantt/api/Core/mixin/State)

A mixin that handles accessing, saving, and restoring an object's persistent state.

Using Stateful Components
-------------------------

Instances of classes that use this mixin (i.e., "stateful components") have a [state](https://bryntum.com/docs/gantt/api/#Core/mixin/State#property-state) property that provides read/write access to their persistable state in the form of a simple object. These state objects can be saved and restored under application control, e.g., using `localStorage`.

This approach can be streamlined using a [StateProvider](https://bryntum.com/docs/gantt/api/#Core/state/StateProvider) either by setting the [default state provider](https://bryntum.com/docs/gantt/api/#Core/state/StateProvider#property-instance-static) or by using an instance-level [stateProvider](https://bryntum.com/docs/gantt/api/#Core/mixin/State#config-stateProvider) config.

When using a state provider, stateful components with a [stateId](https://bryntum.com/docs/gantt/api/#Core/mixin/State#config-stateId) or an [id](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-id) will automatically save (see [saveState](https://bryntum.com/docs/gantt/api/#Core/mixin/State#function-saveState)) and restore (see [loadState](https://bryntum.com/docs/gantt/api/#Core/mixin/State#function-loadState)) their `state`. This use of the `id` as a `stateId` can be disabled by assigning the [stateful](https://bryntum.com/docs/gantt/api/#Core/mixin/State#config-stateful) config to `false`. When using a `stateId` and a state provider, it is not necessary to call the [loadState](https://bryntum.com/docs/gantt/api/#Core/mixin/State#function-loadState) and [saveState](https://bryntum.com/docs/gantt/api/#Core/mixin/State#function-saveState) methods directly.

### Simple vs Complex State

Some stateful components (e.g., [panels](https://bryntum.com/docs/gantt/api/#Core/widget/Panel)) have state that can be described purely by their config properties. For these components, the [stateful](https://bryntum.com/docs/gantt/api/#Core/mixin/State#config-stateful) config can be used to control which config properties to include in their persistent state. For example:

```
 const mainPanel = new Panel({
     collapsible : true,
     stateId     : 'mainPanel',
     stateful    : ['collapsed']
 });
```

Other components have a complex state (e.g., `GridState`), and do not use the `stateful` config in this way. In all other ways, however, these components behave the same as their simple state counterparts.

### Alter state information

For complex state components, the [beforeStateSave](https://bryntum.com/docs/gantt/api/#Core/mixin/State#event-beforeStateSave) event can be used to alter the state object:

```
const grid = new Grid({
   stateId   : 'grid',
   listeners : {
      beforeStateSave : ({ state }) => {
         // Removes state info for the store, like sorters and filters
         delete state.store;
      }
   }
}
```

Implementing Stateful Components
--------------------------------

Implementors of stateful components have two main design points to consider:

* Getting and setting their persistent [state](https://bryntum.com/docs/gantt/api/#Core/mixin/State#property-state) object.
* Initiating calls to [saveState](https://bryntum.com/docs/gantt/api/#Core/mixin/State#function-saveState) when the object's persistent state changes.

### Persistent State

For simple cases, the [stateful](https://bryntum.com/docs/gantt/api/#Core/mixin/State#config-stateful) config can be set to the list of config property names that should be saved:

```
 class MyStatefulComponent extends Base.mixin(State) {
     static configurable = {
         stateful : ['text', 'size']
     };
 }
```

While the `stateful` config supports an object form (where keys with truthy values are the config names), this form is typically reserved for configuring instances.

Classes can choose to implement the [getState](https://bryntum.com/docs/gantt/api/#Core/mixin/State#function-getState) and [applyState](https://bryntum.com/docs/gantt/api/#Core/mixin/State#function-applyState) methods to enhance the `state` object with data not easily mapped to config properties. These method can call their `super` methods or fully replace them.

```
 class MyStatefulComponent extends Base.mixin(State) {
     getState() {
         return {
             text : this.text,
             size : this.size
         };
     }

     applyState(state) {
         this.text = state.text;
         this.size = state.size;
     }
 }
```

### Saving Dates

A stateful property may be a `Date` property if the `changeDate` method of the class accepts an ISO 8601 formatted date. Dates are saved in state using ISO 8601 format: `YYYY-MM-DDTHH:mm:ssZ`

### Saving State

When the persistent state of a stateful component changes, it must call [saveState](https://bryntum.com/docs/gantt/api/#Core/mixin/State#function-saveState). This method schedules an update of the component's persistence [state](https://bryntum.com/docs/gantt/api/#Core/mixin/State#property-state) with the appropriate [stateProvider](https://bryntum.com/docs/gantt/api/#Core/mixin/State#config-stateProvider). When a config property named in the [stateful](https://bryntum.com/docs/gantt/api/#Core/mixin/State#config-stateful) config changes, this call will be made automatically. This means that even if a component replaces [getState](https://bryntum.com/docs/gantt/api/#Core/mixin/State#function-getState) and [applyState](https://bryntum.com/docs/gantt/api/#Core/mixin/State#function-applyState), it can still be helpful to specify a value for the `stateful` config.

```
 class MyStatefulComponent extends Base.mixin(State) {
     static configurable = {
         stateful : ['text', 'size']
     };

     getState() { ... }
     applyState(state) { ... }
 }
```

Another way to ensure [saveState](https://bryntum.com/docs/gantt/api/#Core/mixin/State#function-saveState) is called when necessary is to use [statefulEvents](https://bryntum.com/docs/gantt/api/#Core/mixin/State#config-statefulEvents).

```
 class MyStatefulComponent extends Base.mixin(State) {
     static configurable = {
         statefulEvents : ['change', 'resize']
     };
 }
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[stateful](https://bryntum.com/docs/gantt/api/Core/mixin/State#config-stateful)
This value can be one of the following:

* `false` to not use an explicitly assigned [id](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-id) as the component's [stateId](https://bryntum.com/docs/gantt/api/#Core/mixin/State#config-stateId) (this is only necessary when there is a [stateProvider](https://bryntum.com/docs/gantt/api/#Core/mixin/State#config-stateProvider)).
* An array of strings naming the config properties to save in the component's [state](https://bryntum.com/docs/gantt/api/#Core/mixin/State#property-state) object.
* An object whose truthy keys are the config properties to save in the component's [state](https://bryntum.com/docs/gantt/api/#Core/mixin/State#property-state) object.

These last two uses of the `stateful` config property do not apply to components that have a complex state, as described in the [State mixin documentation](https://bryntum.com/docs/gantt/api/#Core/mixin/State).

This config property is typically set by derived classes to a value including any config property that the user can affect via the user interface. For example, the [collapsed](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#config-collapsed) config property is listed for a [Panel](https://bryntum.com/docs/gantt/api/#Core/widget/Panel) since the user can toggle this config property using the [collapse tool](https://bryntum.com/docs/gantt/api/#Core/widget/panel/PanelCollapser#config-tool).

[statefulEvents](https://bryntum.com/docs/gantt/api/Core/mixin/State#config-statefulEvents)
The events that, when fired by this component, should trigger it to save its state by calling [saveState](https://bryntum.com/docs/gantt/api/#Core/mixin/State#function-saveState).

```
 class MyStatefulComponent extends Base.mixin(State) {
     static configurable = {
         statefulEvents : [ 'change', 'resize' ]
     };
 }
```

In the above example, [saveState](https://bryntum.com/docs/gantt/api/#Core/mixin/State#function-saveState) will be called any time an instance of this class fires the `change` or `resize` event.

This config is typically set by derived classes as a way to ensure [saveState](https://bryntum.com/docs/gantt/api/#Core/mixin/State#function-saveState) is called whenever their persistent state changes.

[stateId](https://bryntum.com/docs/gantt/api/Core/mixin/State#config-stateId)
The key to use when saving this object's state in the [stateProvider](https://bryntum.com/docs/gantt/api/#Core/mixin/State#config-stateProvider). If this config is not assigned, and [stateful](https://bryntum.com/docs/gantt/api/#Core/mixin/State#config-stateful) is not set to `false`, the [id](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-id) (if explicitly specified) will be used as the `stateId`.

If neither of these is given, the [loadState](https://bryntum.com/docs/gantt/api/#Core/mixin/State#function-loadState) and [saveState](https://bryntum.com/docs/gantt/api/#Core/mixin/State#function-saveState) methods will need to be called directly to make use of the `stateProvider`.

For single page applications (SPA's), or multi-page applications (MPA's) that have common, stateful components on multiple pages, the `stateId` should be unique across all stateful components (similar to DOM element id's). MPA's that want each page to be isolated can more easily achieve that isolation using the [prefix](https://bryntum.com/docs/gantt/api/#Core/state/StateProvider#config-prefix).

[stateProvider](https://bryntum.com/docs/gantt/api/Core/mixin/State#config-stateProvider)
The `StateProvider` to use to save and restore this object's [state](https://bryntum.com/docs/gantt/api/#Core/mixin/State#property-state). By default, `state` will be saved using the [default state provider](https://bryntum.com/docs/gantt/api/#Core/state/StateProvider#property-instance-static).

This config is useful for multi-page applications that have a set of common components that want to share state across pages, as well as other components that want their state to be isolated. One of these groups of stateful components could be assigned an explicit `stateProvider` while the other group could use the default state provider.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isState](https://bryntum.com/docs/gantt/api/Core/mixin/State#property-isState)
Identifies an object as an instance of [State](https://bryntum.com/docs/gantt/api/#Core/mixin/State) class, or subclass thereof.

[isState](https://bryntum.com/docs/gantt/api/Core/mixin/State#property-isState-static)
Identifies an object as an instance of [State](https://bryntum.com/docs/gantt/api/#Core/mixin/State) class, or subclass thereof.

[isStateful](https://bryntum.com/docs/gantt/api/Core/mixin/State#property-isStateful)
Returns `true` if this instance implements the [State](https://bryntum.com/docs/gantt/api/#Core/mixin/State) interface.

[isStatefulActive](https://bryntum.com/docs/gantt/api/Core/mixin/State#property-isStatefulActive)
Returns `true` if this instance is ready to participate in state activities.

[state](https://bryntum.com/docs/gantt/api/Core/mixin/State#property-state)
Gets or sets a component's state

[statefulId](https://bryntum.com/docs/gantt/api/Core/mixin/State#property-statefulId)
Returns the state key to use for this instance. This will be either the [stateId](https://bryntum.com/docs/gantt/api/#Core/mixin/State#config-stateId) or the [id](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-id) (if explicitly specified and [stateful](https://bryntum.com/docs/gantt/api/#Core/mixin/State#config-stateful) is not `false`).

[statefulness](https://bryntum.com/docs/gantt/api/Core/mixin/State#property-statefulness)
Returns an object whose truthy keys are the config properties to include in this object's [state](https://bryntum.com/docs/gantt/api/#Core/mixin/State#property-state).

## Functions

Functions are methods available for calling on the class

[applyState](https://bryntum.com/docs/gantt/api/Core/mixin/State#function-applyState)
Applies the given `state` to this instance.

This method is not called directly, but is called when the [state](https://bryntum.com/docs/gantt/api/#Core/mixin/State#property-state) property is assigned a value.

This method is implemented by derived classes that have complex state which exceeds the simple list of config properties provided by [stateful](https://bryntum.com/docs/gantt/api/#Core/mixin/State#config-stateful). In these cases, the `super` method can be called to handle any config properties that are part of the complex state. The default implementation of this method will only assign those config properties listed in [stateful](https://bryntum.com/docs/gantt/api/#Core/mixin/State#config-stateful) from the provided `state` object.

[getState](https://bryntum.com/docs/gantt/api/Core/mixin/State#function-getState)
Returns this object's state information.

This method is not called directly, but is called to return the value of the [state](https://bryntum.com/docs/gantt/api/#Core/mixin/State#property-state) property.

This method is implemented by derived classes that have complex state which exceeds the simple list of config properties provided by [stateful](https://bryntum.com/docs/gantt/api/#Core/mixin/State#config-stateful). In these cases, the `super` method can be called to gather the config properties that are part of the complex state. The default implementation of this method will only copy those config properties listed in [stateful](https://bryntum.com/docs/gantt/api/#Core/mixin/State#config-stateful) to the returned `state` object.

[loadState](https://bryntum.com/docs/gantt/api/Core/mixin/State#function-loadState)
Loads this object's state from its [stateProvider](https://bryntum.com/docs/gantt/api/#Core/mixin/State#config-stateProvider) and applies it to its [state](https://bryntum.com/docs/gantt/api/#Core/mixin/State#property-state).

This method only acts upon its first invocation for a given instance (unless `true` is passed for the `reload` parameter). This allows for flexibility in the timing of that call during the early stages of the instances' lifecycle. To reload the state after this time, manually assign the desired value to the [state](https://bryntum.com/docs/gantt/api/#Core/mixin/State#property-state) property or call this method and pass `reload` as `true`.

This method is called automatically during construction when a [stateId](https://bryntum.com/docs/gantt/api/#Core/mixin/State#config-stateId) or (in some cases) an explicit [id](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-id) is provided.

[saveState](https://bryntum.com/docs/gantt/api/Core/mixin/State#function-saveState)
Saves this object's state to its [stateProvider](https://bryntum.com/docs/gantt/api/#Core/mixin/State#config-stateProvider).

When a [stateId](https://bryntum.com/docs/gantt/api/#Core/mixin/State#config-stateId) or (in some cases) an explicit [id](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-id) is provided, this method will be called automatically any time a config property listed in [stateful](https://bryntum.com/docs/gantt/api/#Core/mixin/State#config-stateful) changes or when a [stateful event](https://bryntum.com/docs/gantt/api/#Core/mixin/State#config-statefulEvents) is fired.

Derived classes are responsible for calling this method whenever the persistent [state](https://bryntum.com/docs/gantt/api/#Core/mixin/State#property-state) of the object changes.

[pruneState](https://bryntum.com/docs/gantt/api/Core/mixin/State#function-pruneState)
Returns an object that copies the [stateful](https://bryntum.com/docs/gantt/api/#Core/mixin/State#config-stateful) config properties from the provided `state` object.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeStateSave](https://bryntum.com/docs/gantt/api/Core/mixin/State#event-beforeStateSave)
Fired before state is saved by the StateProvider. Allows editing the state object or preventing the operation.

[beforeStateApply](https://bryntum.com/docs/gantt/api/Core/mixin/State#event-beforeStateApply)
Fired before state is applied to the source. Allows editing the state object or preventing the operation.
