# Source: https://docs.pentaho.com/pba-ctools/pentaho-cdf-api/components/unmanagedcomponent.md

# UnmanagedComponent

## cdf.components. UnmanagedComponent

The `UnmanagedComponent` is an advanced version of the `BaseComponent` which allows control over the core CDF lifecycle for implementing components.

It should be used as the base class for all components which desire to implement an asynchronous lifecycle, as CDF cannot otherwise ensure that the `postExecution` callback is correctly handled.

## CDF Async Developer's Guide

CDF now supports proper, asynchronous, AJAX calls for all its querying. The following is a guide to converting old components and dashboards to the new async style, and developing new ones based on asynchronous querying.

## Rationale

The first step to understanding the changes in the async patch is understanding the CDF component lifecycle. When a component is updated, the basic update lifecycle looks like this:

`preExecution -> update -> postExecution`

Usually, though, there will be a call to a data source, with a subsequent call to `postFetch`, and only then is the component rendered:

`preExecution -> update -> query -> postFetch -> redraw -> postExecution`

This is a more typical lifecycle, and one that has some important limitations. First, `preExecution` and `postExecution` are entirely the responsibility of CDF itself, rather than the component. Because CDF has no control over the contents of the update method, it has no way of ensuring that, should the component execute an asynchronous query, `postExecution` only runs after redraw. In this case, you are likely to see this instead:

`preExecution -> update -> postExecution -> query -> postFetch -> redraw`

This breaks the contract for `postExecution` running after the component is done updating. The solution here is that the component itself must take control of `postExecution`, while keeping the burden of implementing the lifecycle in CDF rather than passing it to the component developer. On a related topic, `postFetch` has become a de facto standard part of the lifecycle, yet its implementation was left to the component implementers, which leads to a fairly large amount of boilerplate code.

Our objective here was to retool the base component to deal with both of these issues, thus allowing queries to be performed asynchronously while reducing the developer effort involved in creating a component.

## Component Execution Order and Priority

There are no major changes in the way components behave. There is, however an important caveat: since all components that have been converted will be executed simultaneously, we can no longer rely on the order of execution.

There's now an additional property named `priority`. This is the `priority` of component execution, defaulting to 5. The lower the number, the higher `priority` the component has. Components with the same `priority` with be executed simultaneously. This property is useful in places where we need to give higher `priority` to filters or other components that need to be executed before other components.

This way there's no longer the need to use dummy parameters and postChange tricks to do, for instance, cascade prompts.

## Backward Compatibility and Changes

Maintaining backwards compatibility requires some care. If components have no `priority`, we give them a sequential value, trying to emulate the old behavior. It's recommended that proper priorities are set in order to take advantage of the new improvements.

If using Community Dashboard Editor (CDE), note that if you edit a dashboard and save it, *all components will have a default priority of 5*. This may break the old behavior. If you need to change a dashboard, make sure you tweak the priorities, if needed.

## Developing Components

Components desiring to use asynchronous queries should inherit from the new `UnmanagedComponent`, instead of `BaseComponent`. The `UnmanagedComponent` base class provides pre-composed methods which implement the core lifecycle for a variety of different scenarios:

* `synchronous`: implements a synchronous lifecycle identical to the core CDF lifecycle.
* `triggerQuery`: implements a simple interface to a lifecycle built around Query objects.
* `triggerAjax`: implements a simple interface to a lifecycle built around AJAX calls.

Since all these lifecycle methods expect a callback which handles the actual component rendering, it's a conventional style to have that callback as a method of the component, called `redraw`. It's also considered standard practice to use Function#bind or \_.bind to ensure that, inside the `redraw` callback, `this` points to the component itself.

## Use `synchronous` If Your Component Does Not Use External Data

Components that do not use any external data at all can continue subclassing `BaseComponent` without any change of functionality. However, for the sake of consistency (or because you want querying to be optional), you can use subclass `UnmanagedComponent` and use the `synchronous` lifecycle method to emulate `BaseComponent`'s behavior:

```
update: function() {
 this.synchronous(this.redraw);
 }
 
```

If you want to pass parameters to `redraw`, you can pass them as an array to `synchronous`:

```
update: function() {
 // Will call this.redraw(1, 2, 3)
 this.synchronous(this.redraw, [1, 2, 3]);
 }
 
```

## Use `triggerQuery` When You Want Your Component To Use CDA/Query Objects

If you're using a CDA data source, you probably want to use `triggerQuery` to handle the component lifecycle for you. `triggerQuery` expects at a minimum a query definition and a `redraw` callback to process the query results. The query definition is an object of the form:

```
{
 dataAccessId: 'myQuery',
 file: '/path/to/my/datasourceDefinition.cda'
 }
 
```

Typically, if you are using CDE, these properties will be added to one of either this.queryDefinition, this.chartDefinition or this.trafficDefinition so you can just use this pattern:

```
update: function() {
 var redraw = _.bind(this.redraw, this);
 this.triggerQuery(this.queryDefinition, redraw);
 }
 
```

## Alternating Between Static And Query-Based Data

As the lifecycle methods are completely self-contained, you can switch between them at will, deciding on an appropriate lifecycle at runtime. A common pattern (used for example in SelectComponent and the CccComponent family) is exposing a valuesArray property, and using static data if valuesArray is provided, or a query if it is not. Using UnmanagedComponent, this convention would look like this:

```
update: function() {
 var redraw = _.bind(this.redraw, this);
 if(this.valuesArray && this.valuesArray.length > 0) {
 this.synchronous(redraw, this.valuesArray);
 } else {
 this.triggerQuery(this.queryDefinition, redraw);
 }
 }
 
```

**AMD Module**

```
require(["cdf/components/UnmanagedComponent"], function(UnmanagedComponent) { /* code goes here */ });

```

## Extends

cdf.components.BaseComponent

## Constructor

| Name                               | Description                                                                               |
| ---------------------------------- | ----------------------------------------------------------------------------------------- |
| new UnmanagedComponent(properties) | Advanced version of the `BaseComponent` which allows control over the core CDF lifecycle. |

## Members

| Name                                        | Description                                                                     |
| ------------------------------------------- | ------------------------------------------------------------------------------- |
| chartDefinition : \`\`object\`              | \`function\`\`                                                                  |
| elapsedSinceSplit : `number`Protected       | Number of milliseconds since the timer split.                                   |
| elapsedSinceStart : `number`Protected       | Number of milliseconds since the timer start.                                   |
| htmlObject : `string`Protected              | HTML element identifier where the component is rendered.                        |
| initInstance : `Number`Deprecated Protected | The Dashboard instance to which the component belongs.                          |
| isDataPush : `boolean`                      | Indicates if the component lifecycle is being run because of a data push event. |
| isDisposed : `boolean`Protected             | The component is in a disposed state.                                           |
| isManaged : `boolean`                       | Flag that defines if the component is managed or not.                           |
| isRunning : `boolean`                       | Flag that defines if the component is running or not.                           |
| logColor : `string`Protected                | Color to use while logging messages.                                            |
| name : `string`Protected                    | Name of the component.                                                          |
| postChange : `function`                     | Function to be executed after the components parameter value changes.           |
| preChange : `function`                      | Function to be executed before the components parameter value changes.          |
| priority : `number`                         | Priority of a component in the cdf execution cycle.                             |
| queryDefinition : \`\`object\`              | \`function\`\`                                                                  |
| timerSplit : `number`Protected              | Start date for the timer split.                                                 |
| timerStart : `number`Protected              | Start date for the timer start.                                                 |
| trafficDefinition : \`\`object\`            | \`function\`\`                                                                  |
| type : `string`Protected                    | Type of the component.                                                          |
| visible : `boolean`Protected                | Visibility flag.                                                                |

## Methods

| Name                                                                              | Description                                                                                                         |
| --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| \_disposeCore()Protected                                                          | Override this to (irreversibly) dispose of any resources which are not disposed of when simply removed.             |
| \_setQuery(queryDef, queryOptions) : `cdf.queries.BaseQuery`Protected             | Creates and sets the component's current query given its definition, and optionally, query options.                 |
| \_throwIfDisposed()Protected                                                      | Throws an error if the Dashboard is already disposed.                                                               |
| \_unlink()Protected                                                               | Un-links the component without releasing the resources.                                                             |
| beginAjax(ajaxParameters, callback)                                               | The beginAjax lifecycle handler implements the beginning phase of a lifecycle based on generic AJAX calls.          |
| beginExec(isDataPush) : `boolean`                                                 | Begins execution of the component.                                                                                  |
| beginQuery(queryDef, callback, queryOptions)                                      | The beginQuery lifecycle handler implements the beginning phase of a lifecycle around Query objects.                |
| block()                                                                           | Trigger UI blocking while the component is updating.                                                                |
| callCounter() : `number`                                                          | Increment the call counter, so we can keep track of the order in which requests were made.                          |
| clear()                                                                           | Clears the component HTML element.                                                                                  |
| clone(parameterRemap, componentRemap, htmlRemap) : `cdf.components.BaseComponent` | Clones a component.                                                                                                 |
| copyEvents(target, events)                                                        | General copy events methods.                                                                                        |
| dispose()                                                                         | Disposes this component, if it wasn't already disposed.                                                             |
| drawTooltip()                                                                     | Draws a tooltip, if one is defined in the component options.                                                        |
| endExec()                                                                         | Ends a successful execution of the component.                                                                       |
| error(msg, cause)                                                                 | Triggers an error event on the component.                                                                           |
| errorNotification(err, ph)                                                        | Creates an error notification `popup`.                                                                              |
| execute(callback)                                                                 | Generic execute method that handles `preExecution` and `postExecution` lifecycle tasks.                             |
| failExec(arg)                                                                     | Fails execution of the component, given a string, an error object or the arguments of a jQuery.ajax error callback. |
| focus()                                                                           | Focus the first placeholder DOM element on the component.                                                           |
| getAddIn(slot, addIn) : `cdf.AddIn`                                               | Gets an add-in for this component.                                                                                  |
| getAddInOptions(slot, addIn) : `object`                                           | Gets an add-in option.                                                                                              |
| getErrorHandler() : `cdf.components.UnmanagedComponent`                           | Gets an error handler suitable for use as a jQuery.ajax error callback or a try/catch handler.                      |
| getQueryDefinition() : `Object` \| `undefined`                                    | Gets the query definition `object`.                                                                                 |
| getSuccessHandler(counter, success, always, canceled) : `function`                | Builds a generic response handler which runs the success callback.                                                  |
| getValuesArray() : `Array.<`object`>`Deprecated                                   | Gets the values array property.                                                                                     |
| hasAddIn(slot, addIn) : `boolean`                                                 | Returns `true` if the add-in with the provided subtype and name exists.                                             |
| isSilent() : `boolean`                                                            | Returns `true` if the component's lifecycle is marked as silent.                                                    |
| onWillRemove()                                                                    | Prepares the component for removal.                                                                                 |
| parseArray(jData, includeHeader) : `Array.<`object`>`Deprecated                   | Builds an array with the data received from the server in another format.                                           |
| parseArrayCda(jData, includeHeader) : `Array.<`object`>`Deprecated                | Builds an array with the data received.                                                                             |
| placeholder(selector) : `jQuery`                                                  | Getter for the component's DOM element.                                                                             |
| postExec()                                                                        | Handles calling `postExecution` when it exists.                                                                     |
| postFetchData(data) : `object`                                                    | Handles calling `postFetch`, when it exists, and triggering the `postFetch` event.                                  |
| preExec() : `boolean`                                                             | Handles calling `preExecution` when it exists.                                                                      |
| setAddInOptions(slot, addIn, options)                                             | Sets the options for an add-in.                                                                                     |
| showTooltip()                                                                     | Shows a tooltip attached to the component, if one is defined in the `_tooltip` option.                              |
| synchronous(callback, arg)                                                        | The synchronous lifecycle handler closely resembles the core CDF lifecycle.                                         |
| triggerAjax(url, params, callback, ajaxParameters)                                | The triggerAjax lifecycle handler builds a lifecycle around generic AJAX calls.                                     |
| triggerQuery(queryDef, callback, queryOptions)                                    | The triggerQuery lifecycle handler builds a lifecycle around Query objects.                                         |
| unblock()                                                                         | Trigger UI unblock when the component finishes updating.                                                            |

## Events

| Name                | Description                                           |
| ------------------- | ----------------------------------------------------- |
| cdf:error           | Event triggered on error.                             |
| cdf:postExecution   | Event triggered after execution.                      |
| cdf:postFetch(data) | Event triggered after fetching data.                  |
| cdf:preExecution    | Event triggered before execution.                     |
| cdf:render          | Event triggered after the `render` callback executes. |
| all                 | Event triggered by any other event.                   |

## Constructor Details

| **new UnmanagedComponent**(properties)                                                                           |               |                                                                          |
| ---------------------------------------------------------------------------------------------------------------- | ------------- | ------------------------------------------------------------------------ |
| <p>The constructor of an unmanaged component.</p><p>\*\*Source:\*\*components/UnmanagedComponent.js, line 21</p> |               |                                                                          |
| Name                                                                                                             | Default Value | Summary                                                                  |
| properties : `object`                                                                                            |               | An object with the properties to extend the UnmanagedComponent instance. |

\## Members Details

| chartDefinition: ``object` \| `function``                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <p>The chart definition <code>object</code> used to hold the parameters for the query.</p><p>\*\*Source:\*\*components/UnmanagedComponent.js, line 237</p><p><strong>See also:</strong><code>queryDefinition</code>.</p> |

| elapsedSinceSplit: `number`Protected                                                                                                                                                                                                         |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>Number of milliseconds since the timer split.</p><p>\*\*Source:\*\*components/BaseComponent.js, line 98</p><p><strong>Inherited From:</strong> cdf.components.BaseComponent#elapsedSinceSplit</p><p><strong>Default Value:</strong>-1</p> |

| elapsedSinceStart: `number`Protected                                                                                                                                                                                                          |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>Number of milliseconds since the timer start.</p><p>\*\*Source:\*\*components/BaseComponent.js, line 108</p><p><strong>Inherited From:</strong> cdf.components.BaseComponent#elapsedSinceStart</p><p><strong>Default Value:</strong>-1</p> |

| htmlObject: `string`Protected                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>The HTML element identifier, unique in the HTML page, where the component is rendered.</p><p>\*\*Source:\*\*components/BaseComponent.js, line 46</p><p><strong>Inherited From:</strong> cdf.components.BaseComponent#htmlObject</p> |

| initInstance: `Number`Deprecated Protected                                                                                                                                                                |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>The Dashboard instance to which the component belongs.</p><p>\*\*Source:\*\*components/BaseComponent.js, line 130</p><p><strong>Inherited From:</strong> cdf.components.BaseComponent#initInstance</p> |

| isDataPush: `boolean`                                                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>Indicates if the component lifecycle is being run because of a data push event..</p><p>\*\*Source:\*\*components/UnmanagedComponent.js, line 216</p><p>\*\*Default Value:\*\*false</p> |

| isDisposed: `boolean`Protected                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <p>The component is in a disposed state.</p><p>\*\*Source:\*\*components/BaseComponent.js, line 128</p><p><strong>Inherited From:</strong> cdf.components.BaseComponent#isDisposed</p><p>\*\*Default Value:\*\*false</p> |

| isManaged: `boolean`                                                                                                                                                                                                          |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>Flag that defines if the component is managed or not.</p><p>\*\*Source:\*\*components/UnmanagedComponent.js, line 198</p><p>\*\*Default Value:\*\*false</p><p>\*\*Overrides:\*\*cdf.components.BaseComponent#isManaged</p> |

| isRunning: `boolean`                                                                                                                                           |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>Flag that defines if the component is running or not.</p><p>\*\*Source:\*\*components/UnmanagedComponent.js, line 207</p><p>\*\*Default Value:\*\*false</p> |

| logColor: `string`Protected                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>Color to use while logging messages.</p><p>\*\*Source:\*\*components/BaseComponent.js, line 118</p><p><strong>Inherited From:</strong> cdf.components.BaseComponent#logColor</p><p>\*\*Default Value:\*\*undefined</p> |

| name: `string`Protected                                                                                                                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>The name of the component. Its name needs to be unique in the dashboard to which they belong.</p><p>\*\*Source:\*\*components/BaseComponent.js, line 30</p><p><strong>Inherited From:</strong> cdf.components.BaseComponent#name</p> |

| postChange: `function`                                                                                                                                                                                                 |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>Function to be executed after the components parameter value changes.</p><p>\*\*Source:\*\*components/BaseComponent.js, line 150</p><p><strong>Inherited From:</strong> cdf.components.BaseComponent#postChange</p> |

| preChange: `function`                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>Function to be executed before the components parameter value changes.</p><p>\*\*Source:\*\*components/BaseComponent.js, line 141</p><p><strong>Inherited From:</strong> cdf.components.BaseComponent#preChange</p> |

| priority: `number`                                                                                                                                       |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>Priority of a component in the cdf execution cycle.</p><p>\*\*Source:\*\*components/UnmanagedComponent.js, line 218</p><p>\*\*Default Value:\*\*5</p> |

| queryDefinition: ``object` \| `function``                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>The query definition <code>object</code> used to hold the parameters for the query.</p><p>\*\*Source:\*\*components/UnmanagedComponent.js, line 228</p> |

| timerSplit: `number`Protected                                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>Start date for the timer split.</p><p>\*\*Source:\*\*components/BaseComponent.js, line 88</p><p><strong>Inherited From:</strong> cdf.components.BaseComponent#timerSplit</p><p>\*\*Default Value:\*\*0</p> |

| timerStart: `number`Protected                                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>Start date for the timer start.</p><p>\*\*Source:\*\*components/BaseComponent.js, line 78</p><p><strong>Inherited From:</strong> cdf.components.BaseComponent#timerStart</p><p>\*\*Default Value:\*\*0</p> |

| trafficDefinition: ``object` \| `function``                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>The traffic definition <code>object</code> used to hold the parameters for the query.</p><p>\*\*Source:\*\*components/UnmanagedComponent.js, line 247</p><p><strong>See also:</strong><code>queryDefinition</code>.</p> |

| type: `string`Protected                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>The type of the component, usually the class name of the component.</p><p>\*\*Source:\*\*components/BaseComponent.js, line 38</p><p><strong>Inherited From:</strong> cdf.components.BaseComponent#type</p> |

| visible: `boolean`Protected                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>Visibility flag.</p><p>\*\*Source:\*\*components/BaseComponent.js, line 56</p><p><strong>Inherited From:</strong> cdf.components.BaseComponent#visible</p><p>\*\*Default Value:\*\*true</p> |

\## Method Details

| **\_disposeCore**()Protected                                                                                                                                                                                                                                |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>Override this to (irreversibly) dispose of any resources which are not disposed of when simply removed.</p><p>\*\*Source:\*\*components/BaseComponent.js, line 574</p><p><strong>Inherited From:</strong> cdf.components.BaseComponent#\_disposeCore</p> |

| **\_setQuery**(queryDef, queryOptions) : `cdf.queries.BaseQuery`Protected                                                                                                     |               |                                                                                                           |   |      |             |   |                         |                     |      |   |   |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | --------------------------------------------------------------------------------------------------------- | - | ---- | ----------- | - | ----------------------- | ------------------- | ---- | - | - |
| <p>Creates and sets the component's current query given its definition, and optionally, query options.</p><p>\*\*Source:\*\*components/UnmanagedComponent.js, line 669</p><p> | Name          | Description                                                                                               |   | ---- | ----------- |   | `cdf.queries.BaseQuery` | The query `object`. | </p> |   |   |
| Name                                                                                                                                                                          | Default Value | Summary                                                                                                   |   |      |             |   |                         |                     |      |   |   |
| queryDef : `object`                                                                                                                                                           |               | The query definition `object`.                                                                            |   |      |             |   |                         |                     |      |   |   |
| queryOptions : `object`Optional                                                                                                                                               |               | Query options `object`.                                                                                   |   |      |             |   |                         |                     |      |   |   |
| Name                                                                                                                                                                          | Default Value | Summary                                                                                                   |   |      |             |   |                         |                     |      |   |   |
| ajax : `object`Optional                                                                                                                                                       |               | Options passed to jQuery.ajax. The jQuery.ajax options `data`, `url`, `error` and `success` are reserved. |   |      |             |   |                         |                     |      |   |   |
| pageSize : `number`Optional                                                                                                                                                   |               | The page size of paginated results.                                                                       |   |      |             |   |                         |                     |      |   |   |

| **\_throwIfDisposed**()Protected                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>Throws an error if the Dashboard is already disposed.</p><p>\*\*Source:\*\*components/BaseComponent.js, line 582</p><p><strong>Inherited From:</strong> cdf.components.BaseComponent#\_throwIfDisposed</p> |

| **\_unlink**()Protected                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <p>Un-links the component without releasing the resources.</p><p>\*\*Source:\*\*components/BaseComponent.js, line 561</p><p><strong>Inherited From:</strong> cdf.components.BaseComponent#\_unlink</p> |

<table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><strong>beginAjax</strong>(ajaxParameters, callback)</td></tr><tr><td><p>The beginAjax lifecycle handler implements the beginning phase of a lifecycle based on generic AJAX calls. It implements the lifecycle:</p><pre><code>``preExecution` -> `block` (optional) -> `fetchData` -> `postFetch` -> `callback``
</code></pre><p>Ending the execution is the responsibility of the specified callback, by calling <code>endExec</code>, resulting in:``` <code>postExec` -> `unblock` (optional) or `failExec</code></p><pre><code>
**Source:**components/UnmanagedComponent.js, line 640

\<table id="TABLE\_QBQ\_BNY\_M1C">\<thead>\<tr>\<th>

Name

\</th>\<th>

Default Value

\</th>\<th>

Summary

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

ajaxParameters : `object`

\</td>\<td>

 

\</td>\<td>

Parameters for jQuery.ajax, including, at a minimum, the `url` option. `beginAjax` will take control over the `success` and `error` callbacks and default `async` to `true`.

| Name           | Default Value | Summary      |
| -------------- | ------------- | ------------ |
| url : `string` |               | URL to call. |

\</td>\</tr>\<tr>\<td>

callback : `function`

\</td>\<td>

 

\</td>\<td>

Render callback, called with the response data.

\</td>\</tr>\</tbody>
\</table>

\</td>\</tr>\</tbody>
\</table>\<table id="BEGINEXEC">\<thead>\<tr>\<th>

**beginExec**(isDataPush) : `boolean`

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

Begins execution of the component. This method handles calling `preExecution` and blocking the UI, if necessary.

A component that actually begins execution, by returning `true` from this method, should later complete the lifecycle by calling either `endExec` or `failExec`.

\*\*Source:\*\*components/UnmanagedComponent.js, line 378

| Name                   | Default Value | Summary                                                         |
| ---------------------- | ------------- | --------------------------------------------------------------- |
| isDataPush : `boolean` |               | If the lifecycle event is being triggered by a push data event. |

| Name      | Description                                                          |
| --------- | -------------------------------------------------------------------- |
| `boolean` | `false` if component execution should be canceled, `true` otherwise. |

\</td>\</tr>\</tbody>
\</table>\<table id="BEGINQUERY">\<thead>\<tr>\<th>

**beginQuery**(queryDef, callback, queryOptions)

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

The beginQuery lifecycle handler implements the beginning phase of a lifecycle around Query objects. It implements the lifecycle:

</code></pre><p>\`\`preExecution<code>-></code>block<code>(optional) -></code>fetchData<code>-></code>postFetch <code>-> callback</code></p><pre><code>
Ending the execution, is the responsibility of the specified callback by calling `endExec`, resulting in:

</code></pre><p><code>postExecution`->`unblock`(optional) or`failExec</code></p><pre><code>
\*\*Source:\*\*components/UnmanagedComponent.js, line 538

| Name                    | Default Value | Summary                              |
| ----------------------- | ------------- | ------------------------------------ |
| queryDef : `object`     |               | The query definition object.         |
| callback : `function`   |               | Callback to run after query has ran. |
| queryOptions : `object` |               | User options for the query.          |

\</td>\</tr>\</tbody>
\</table>\<table id="BLOCK">\<thead>\<tr>\<th>

**block**()

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

Trigger UI blocking while the component is updating. Default implementation uses the global CDF blockUI, but implementers are encouraged to override with per-component blocking where appropriate (or no blocking at all in components that support it).

\*\*Source:\*\*components/UnmanagedComponent.js, line 838

\</td>\</tr>\</tbody>
\</table>\<table id="CALLCOUNTER">\<thead>\<tr>\<th>

**callCounter**() : `number`

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

Increment the call counter, so we can keep track of the order in which requests were made.

\*\*Source:\*\*components/UnmanagedComponent.js, line 696

| Name     | Description              |
| -------- | ------------------------ |
| `number` | The incremented counter. |

\</td>\</tr>\</tbody>
\</table>\<table id="CLEAR">\<thead>\<tr>\<th>

**clear**()

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

Clears the component HTML element.

\*\*Source:\*\*components/BaseComponent.js, line 214

**Inherited From:** cdf.components.BaseComponent#clear

\</td>\</tr>\</tbody>
\</table>\<table id="CLONE">\<thead>\<tr>\<th>

**clone**(parameterRemap, componentRemap, htmlRemap) : `cdf.components.BaseComponent`

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

Clones a component.

\*\*Source:\*\*components/BaseComponent.js, line 245

**Inherited From:** cdf.components.BaseComponent#clone

| Name                      | Default Value | Summary                               |
| ------------------------- | ------------- | ------------------------------------- |
| parameterRemap : `Object` |               | Map containing parameter remapping.   |
| componentRemap : `Object` |               | Map containing component remapping.   |
| htmlRemap : `Object`      |               | Map containing DOM element remapping. |

| Name                           | Description           |
| ------------------------------ | --------------------- |
| `cdf.components.BaseComponent` | The cloned component. |

\</td>\</tr>\</tbody>
\</table>\<table id="COPYEVENTS">\<thead>\<tr>\<th>

**copyEvents**(target, events)

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

General copy events methods. Given a target component and an event list, adds the component as a listener for all events in the list.

\*\*Source:\*\*components/BaseComponent.js, line 226

**Inherited From:** cdf.components.BaseComponent#copyEvents

| Name                                      | Default Value | Summary                       |
| ----------------------------------------- | ------------- | ----------------------------- |
| target : `cdf.components.BaseComponent`   |               | The target component object.  |
| events : `Array.&#x3C;`Backbone.Events`>` |               | Backbone.Events list to copy. |

\</td>\</tr>\</tbody>
\</table>\<table id="DISPOSE">\<thead>\<tr>\<th>

**dispose**()

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

Disposes this component, if it wasn't already disposed.

\*\*Source:\*\*components/BaseComponent.js, line 531

**Inherited From:** cdf.components.BaseComponent#dispose

\</td>\</tr>\</tbody>
\</table>\<table id="DRAWTOOLTIP">\<thead>\<tr>\<th>

**drawTooltip**()

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

Draws a tooltip, if one is defined in the component options.

\*\*Source:\*\*components/UnmanagedComponent.js, line 344

\</td>\</tr>\</tbody>
\</table>\<table id="ENDEXEC">\<thead>\<tr>\<th>

**endExec**()

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

Ends a successful execution of the component. This method handles drawing and showing the component's tooltip, if any, calling `postExec` and unblocking the UI, if necessary.

\*\*Source:\*\*components/UnmanagedComponent.js, line 422

\</td>\</tr>\</tbody>
\</table>\<table id="ERROR">\<thead>\<tr>\<th>

**error**(msg, cause)

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

Triggers an error event on the component. Takes as arguments the error message and optionally, a `cause` object. It also calls `errorNotification` showing the notification to the user.

\*\*Source:\*\*components/UnmanagedComponent.js, line 796

| Name                     | Default Value | Summary              |
| ------------------------ | ------------- | -------------------- |
| msg : `string`           |               | Error message.       |
| cause : `string`Optional | null          | Cause for the error. |

**Fires:** cdf.event:cdf , cdf.components.UnmanagedComponent#event:cdf:error

\</td>\</tr>\</tbody>
\</table>\<table id="ERRORNOTIFICATION">\<thead>\<tr>\<th>

**errorNotification**(err, ph)

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

Creates an error notification `popup` with the given messages and error.

\*\*Source:\*\*components/UnmanagedComponent.js, line 822

\<table id="TABLE\_ACQ\_BNY\_M1C">\<thead>\<tr>\<th>

Name

\</th>\<th>

Default Value

\</th>\<th>

Summary

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

err : `object`

\</td>\<td>

 

\</td>\<td>

A CDF error object containing `msg` and `error` properties.

| Name             | Default Value | Summary              |
| ---------------- | ------------- | -------------------- |
| msg : `string`   |               | Error message.       |
| error : `string` |               | Cause for the error. |

\</td>\</tr>\<tr>\<td>

ph : `jQuery`Optional

\</td>\<td>

 

\</td>\<td>

DOM element where to display the error notification.

\</td>\</tr>\</tbody>
\</table> **See also:**`errorNotification`

\</td>\</tr>\</tbody>
\</table>\<table id="EXECUTE">\<thead>\<tr>\<th>

**execute**(callback)

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

Generic execute method that handles `preExecution` and `postExecution` lifecycle tasks.

The specified `callback` function handles the component's core execution. If execution is not canceled by the `preExecution` handler, it is called synchronously, from within a call to this method. If it throws an error, it is like if `failExec` had been called with that error. This function is called with this component as the `this` context.

This method is sugar for the following common pattern:

</code></pre><p>if(this.beginExec()) { try { callback.call(this); } catch(ex) { this.failExec(ex); } }</p><pre><code>
\*\*Source:\*\*components/UnmanagedComponent.js, line 465

\<table id="TABLE\_CCQ\_BNY\_M1C">\<thead>\<tr>\<th>

Name

\</th>\<th>

Default Value

\</th>\<th>

Summary

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

callback : `function`

\</td>\<td>

 

\</td>\<td>

The function to execute. This function receives two arguments:

1. resolve - call this function to signal that core execution has ended.
2. reject - called, optionally with a cause value (an `Error` object), to signal that an error occurred during core execution.

\</td>\</tr>\</tbody>
\</table>

\</td>\</tr>\</tbody>
\</table>\<table id="FAILEXEC">\<thead>\<tr>\<th>

**failExec**(arg)

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

Fails execution of the component, given a String an error object or the arguments of a jQuery.ajax error callback. This method handles parsing, signaling and logging of the error and unblocking the UI, if necessary.

\*\*Source:\*\*components/UnmanagedComponent.js, line 400

| Name           | Default Value | Summary                                                                    |
| -------------- | ------------- | -------------------------------------------------------------------------- |
| arg : `object` |               | A string an error object or the arguments of a jQuery.ajax error callback. |

\</td>\</tr>\</tbody>
\</table>\<table id="FOCUS">\<thead>\<tr>\<th>

**focus**()

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

Focus the first placeholder DOM element on the component.

\*\*Source:\*\*components/BaseComponent.js, line 190

**Inherited From:** cdf.components.BaseComponent#focus

\</td>\</tr>\</tbody>
\</table>\<table id="GETADDIN">\<thead>\<tr>\<th>

**getAddIn**(slot, addIn) : `cdf.AddIn`

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

Gets an add-in for this component.

\*\*Source:\*\*components/BaseComponent.js, line 306

**Inherited From:** cdf.components.BaseComponent#getAddIn

| Name             | Default Value | Summary         |
| ---------------- | ------------- | --------------- |
| slot : `string`  |               | Add-in subtype. |
| addIn : `string` |               | Add-in name.    |

| Name        | Description                                            |
| ----------- | ------------------------------------------------------ |
| `cdf.AddIn` | Add-in registered with the specified name and subtype. |

\</td>\</tr>\</tbody>
\</table>\<table id="GETADDINOPTIONS">\<thead>\<tr>\<th>

**getAddInOptions**(slot, addIn) : `object`

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

Gets an add-in option.

\*\*Source:\*\*components/BaseComponent.js, line 516

**Inherited From:** cdf.components.BaseComponent#getAddInOptions

| Name             | Default Value | Summary             |
| ---------------- | ------------- | ------------------- |
| slot : `string`  |               | The add-in subtype. |
| addIn : `string` |               | The add-in name.    |

| Name     | Description                                       |
| -------- | ------------------------------------------------- |
| `object` | The options associated with the specified add-in. |

\</td>\</tr>\</tbody>
\</table>\<table id="GETERRORHANDLER">\<thead>\<tr>\<th>

**getErrorHandler**() : `cdf.components.UnmanagedComponent`

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

Gets an error handler suitable for use as a jQuery.ajax error callback or a try/catch handler.

This method returns a `this` free version of the `failExec` method.

\*\*Source:\*\*components/UnmanagedComponent.js, line 770

| Name                                | Description    |
| ----------------------------------- | -------------- |
| `cdf.components.UnmanagedComponent` | Error handler. |

\</td>\</tr>\</tbody>
\</table>\<table id="GETQUERYDEFINITION">\<thead>\<tr>\<th>

**getQueryDefinition**() : `Object` | `undefined`

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

Gets the query definition `object`.

The properties used for retrieving the query definition are based on the known component implementations.

\*\*Source:\*\*components/UnmanagedComponent.js, line 577

| Name                    | Description                                   |
| ----------------------- | --------------------------------------------- |
| `Object` \| `undefined` | The query definition `object` or `undefined`. |

\</td>\</tr>\</tbody>
\</table>\<table id="GETSUCCESSHANDLER">\<thead>\<tr>\<th>

**getSuccessHandler**(counter, success, always, canceled) : `function`

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

Builds a generic response handler which runs the success callback when being called in response to the most recent AJAX request that was triggered for this component (as determined by comparing counter and this.runCounter), and always calls the always callback. If the counter is not provided, it will be generated automatically.

Accepts the following calling conventions:

* `getSuccessHandler`(counter, success, always)
* `getSuccessHandler`(counter, success)
* `getSuccessHandler`(success, always)
* `getSuccessHandler`(success)

\*\*Source:\*\*components/UnmanagedComponent.js, line 721

| Name                          | Default Value | Summary                                                                                                          |
| ----------------------------- | ------------- | ---------------------------------------------------------------------------------------------------------------- |
| counter : `number`Optional    | `callCounter` | Identifier for the ajax call being made.                                                                         |
| success : `function`          |               | Success callback.                                                                                                |
| always : `function`Optional   |               | Callback that is run independently of call status.                                                               |
| canceled : `function`Optional |               | Callback that is run when the call has been superseeded by a more recent one. It receives the raw received data. |

| Name       | Description               |
| ---------- | ------------------------- |
| `function` | Success handler function. |

\</td>\</tr>\</tbody>
\</table>\<table id="GETVALUESARRAY">\<thead>\<tr>\<th>

**getValuesArray**() : `Array.&#x3C;`object`>`Deprecated

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

Gets the values array property, if one is defined. Otherwise, issues a call to the server to get data.

\*\*Source:\*\*components/BaseComponent.js, line 340

**Inherited From:** cdf.components.BaseComponent#getValuesArray

| Name                    | Description                                                                                |
| ----------------------- | ------------------------------------------------------------------------------------------ |
| `Array.&#x3C;`object`>` | An array with values from the values array property or the data retrieved from the server. |

\</td>\</tr>\</tbody>
\</table>\<table id="HASADDIN">\<thead>\<tr>\<th>

**hasAddIn**(slot, addIn) : `boolean`

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

Returns `true` if the add-in with the provided subtype and name exists.

\*\*Source:\*\*components/BaseComponent.js, line 323

**Inherited From:** cdf.components.BaseComponent#hasAddIn

| Name             | Default Value | Summary         |
| ---------------- | ------------- | --------------- |
| slot : `string`  |               | Add-in subtype. |
| addIn : `string` |               | Add-in name.    |

| Name      | Description                                     |
| --------- | ----------------------------------------------- |
| `boolean` | `true` if the add-in exists, `false` otherwise. |

\</td>\</tr>\</tbody>
\</table>\<table id="ISSILENT">\<thead>\<tr>\<th>

**isSilent**() : `boolean`

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

Returns `true` if the component's lifecycle is marked as silent. This means that any step in the lifecycle of the component will not try to block the UI.

\*\*Source:\*\*components/UnmanagedComponent.js, line 865

| Name      | Description                                                           |
| --------- | --------------------------------------------------------------------- |
| `boolean` | `true` if the component should not trigger an UI block when updating. |

\</td>\</tr>\</tbody>
\</table>\<table id="ONWILLREMOVE">\<thead>\<tr>\<th>

**onWillRemove**()

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

Prepares the component for removal.

\*\*Source:\*\*components/BaseComponent.js, line 552

**Inherited From:** cdf.components.BaseComponent#onWillRemove

\</td>\</tr>\</tbody>
\</table>\<table id="PARSEARRAY">\<thead>\<tr>\<th>

**parseArray**(jData, includeHeader) : `Array.&#x3C;`object`>`Deprecated

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

Builds an array with the data received from the server in another format.

\*\*Source:\*\*components/BaseComponent.js, line 414

**Inherited From:** cdf.components.BaseComponent#parseArray

| Name                      | Default Value | Summary                                                                      |
| ------------------------- | ------------- | ---------------------------------------------------------------------------- |
| jData : `object`          |               | Data object (Xaction or CDA) resulting from a call to the server.            |
| includeHeader : `boolean` |               | A boolean indicating whether the resulting array should include the headers. |

| Name                    | Description |
| ----------------------- | ----------- |
| `Array.&#x3C;`object`>` | /p          |

\</td>\</tr>\</tbody>
\</table>\<table id="PARSEARRAYCDA">\<thead>\<tr>\<th>

**parseArrayCda**(jData, includeHeader) : `Array.&#x3C;`object`>`Deprecated

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

Builds an array with the data received from the server in CDA format.

\*\*Source:\*\*components/BaseComponent.js, line 457

**Inherited From:** cdf.components.BaseComponent#parseArrayCda

| Name                      | Default Value | Summary                                                                      |
| ------------------------- | ------------- | ---------------------------------------------------------------------------- |
| jData : `object`          |               | Data object (CDA format) resulting from a call to the server.                |
| includeHeader : `boolean` |               | A boolean indicating whether the resulting array should include the headers. |

| Name                    | Description                             |
| ----------------------- | --------------------------------------- |
| `Array.&#x3C;`object`>` | The built data array in the CDA format. |

\</td>\</tr>\</tbody>
\</table>\<table id="PLACEHOLDER">\<thead>\<tr>\<th>

**placeholder**(selector) : `jQuery`

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

Getter for the component's DOM element. Returns the jQuery `object` that represents it.

\*\*Source:\*\*components/BaseComponent.js, line 181

**Inherited From:** cdf.components.BaseComponent#placeholder

| Name                | Default Value | Summary                                             |
| ------------------- | ------------- | --------------------------------------------------- |
| selector : `string` |               | Optional `string` to append to the jQuery selector. |

| Name     | Description                                                    |
| -------- | -------------------------------------------------------------- |
| `jQuery` | The matched DOM element or a new element if no match is found. |

\</td>\</tr>\</tbody>
\</table>\<table id="POSTEXEC">\<thead>\<tr>\<th>

**postExec**()

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

Handles calling `postExecution` when it exists.

All components extending UnmanagedComponent should either use one of the three lifecycles declared in this class (`synchronous`, `triggerQuery` or `triggerAjax`), or explicitly call this method immediately before yielding control back to CDF.

\*\*Source:\*\*components/UnmanagedComponent.js, line 308

**Fires:** cdf.event:cdf , cdf.components.UnmanagedComponent#event:cdf:postExecution

\</td>\</tr>\</tbody>
\</table>\<table id="POSTFETCHDATA">\<thead>\<tr>\<th>

**postFetchData**(data) : `object`

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

Handles calling `postFetch`, when it exists, and triggering the `postFetch` event.

\*\*Source:\*\*components/UnmanagedComponent.js, line 327

| Name            | Default Value | Summary           |
| --------------- | ------------- | ----------------- |
| data : `object` |               | The fetched data. |

**Fires:** cdf.event:cdf , cdf.components.UnmanagedComponent#event:cdf:postFetch

| Name     | Description         |
| -------- | ------------------- |
| `object` | The resulting data. |

\</td>\</tr>\</tbody>
\</table>\<table id="PREEXEC">\<thead>\<tr>\<th>

**preExec**() : `boolean`

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

Handles calling `preExecution` when it exists.

All components extending UnmanagedComponent should either use one of the three lifecycles declared in this class (`synchronous`, `triggerQuery` or `triggerAjax`), or explicitly call this method at the very earliest opportunity. If `preExecution` returns a falsy value, component execution should be canceled as immediately as possible.

\*\*Source:\*\*components/UnmanagedComponent.js, line 273

**Fires:** cdf.event:cdf , cdf.components.UnmanagedComponent#event:cdf:preExecution

| Name      | Description                                                          |
| --------- | -------------------------------------------------------------------- |
| `boolean` | `false` if component execution should be canceled, `true` otherwise. |

\</td>\</tr>\</tbody>
\</table>\<table id="SETADDINOPTIONS">\<thead>\<tr>\<th>

**setAddInOptions**(slot, addIn, options)

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

Sets the options for an add-in.

\*\*Source:\*\*components/BaseComponent.js, line 497

**Inherited From:** cdf.components.BaseComponent#setAddInOptions

| Name               | Default Value | Summary                            |
| ------------------ | ------------- | ---------------------------------- |
| slot : `string`    |               | The add-in subtype.                |
| addIn : `string`   |               | The add-in name.                   |
| options : `object` |               | An object with the options to use. |

\</td>\</tr>\</tbody>
\</table>\<table id="SHOWTOOLTIP">\<thead>\<tr>\<th>

**showTooltip**()

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

Shows a tooltip attached to the component, if one is defined in the `_tooltip` option.

\*\*Source:\*\*components/UnmanagedComponent.js, line 354

\</td>\</tr>\</tbody>
\</table>\<table id="SYNCHRONOUS">\<thead>\<tr>\<th>

**synchronous**(callback, arg)

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

The synchronous lifecycle handler closely resembles the core CDF lifecycle, and is provided as an alternative for components that desire the option to alternate between a synchronous and asynchronous style lifecycles depending on external configuration (e.g., if it can take values from either a static array or a query). It takes the component drawing method as a callback.

\*\*Source:\*\*components/UnmanagedComponent.js, line 486

| Name                                  | Default Value | Summary                    |
| ------------------------------------- | ------------- | -------------------------- |
| callback : `function`                 |               | Component drawing method.  |
| arg : `Array.&#x3C;`Object`>`Optional | \[]           | Argument for the callback. |

\</td>\</tr>\</tbody>
\</table>\<table id="TRIGGERAJAX">\<thead>\<tr>\<th>

**triggerAjax**(url, params, callback, ajaxParameters)

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

The triggerAjax lifecycle handler builds a lifecycle around generic AJAX calls. It implements the lifecycle:

</code></pre><p>\`\`preExecution<code>-></code>block<code>(optional) -></code>fetchData<code>-></code>postFetch<code>-> render -></code>postExecution<code>-></code>unblock <code>(optional)</code></p><pre><code>
After the call to the `render` callback, the event `cdf:render` is fired, and then the execution ends.

triggerAjax can be used with either of the following call conventions:-   `triggerAjax`(url, params, callback);

* `triggerAjax`({url: url, data: params, ...}, callback);
* `triggerAjax`({url: url, data: params, ...}, callback, ajaxParameters);

In the second case, you can add any other jQuery.ajax parameters you desire to the object, but `callback` will take control over the success and error callbacks. If passed, the supplied `ajaxParameters` will be passed to the default Ajax call.

\*\*Source:\*\*components/UnmanagedComponent.js, line 606

\<table id="TABLE\_EDQ\_BNY\_M1C">\<thead>\<tr>\<th>

Name

\</th>\<th>

Default Value

\</th>\<th>

Summary

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

url : `string` | `Object`

\</td>\<td>

 

\</td>\<td>

URL to call.

| Name              | Default Value | Summary                  |
| ----------------- | ------------- | ------------------------ |
| url : `string`    |               | URL to call.             |
| params : `object` |               | Parameters for the call. |

\</td>\</tr>\<tr>\<td>

params : `object`Optional

\</td>\<td>

 

\</td>\<td>

Parameters for the call.

\</td>\</tr>\<tr>\<td>

callback : `function`

\</td>\<td>

 

\</td>\<td>

Render callback, called with the response data.

\</td>\</tr>\<tr>\<td>

ajaxParameters : `object`Optional

\</td>\<td>

{}

\</td>\<td>

Parameters specific to the Ajax call definition.

\</td>\</tr>\</tbody>
\</table>**Fires:** cdf.event:cdf , cdf.components.UnmanagedComponent#event:cdf:render

\</td>\</tr>\</tbody>
\</table>\<table id="TRIGGERQUERY">\<thead>\<tr>\<th>

**triggerQuery**(queryDef, callback, queryOptions)

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

The triggerQuery lifecycle handler builds a lifecycle around Query objects. Execution ends immediately after the call to the specified callback.

It takes a query definition object which is passed directly into the Query constructor, and the component rendering callback, and implements the lifecycle:

</code></pre><p>\`\`preExecution<code>-></code>block<code>(optional) -></code>fetchData<code>-></code>postFetch<code>-> callback -></code>postExecution<code>-></code>unblock <code>(optional)</code></p><pre><code>
This method detects concurrent updates to the component and ensures that only the redraw of the most recent update is performed. `endExec` is called after the `callback` execution.

\*\*Source:\*\*components/UnmanagedComponent.js, line 518

| Name                    | Default Value | Summary                                                                           |
| ----------------------- | ------------- | --------------------------------------------------------------------------------- |
| queryDef : `object`     |               | The query definition object.                                                      |
| callback : `function`   |               | Callback to run after query has ran. It receives the fetched data as an argument. |
| queryOptions : `object` |               | User options for the query.                                                       |

\</td>\</tr>\</tbody>
\</table>\<table id="UNBLOCK">\<thead>\<tr>\<th>

**unblock**()

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

Trigger UI unblock when the component finishes updating. Functionality is defined as undoing whatever was done in the block method. Should also be overridden in components that override `block`.

\*\*Source:\*\*components/UnmanagedComponent.js, line 851

\</td>\</tr>\</tbody>
\</table>## Events Details

\<table>\<thead>\<tr>\<th>

**cdf:error**

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

Event triggered when an error occurs.

\*\*Source:\*\*components/\_doc/events.jsdoc, line 46

\</td>\</tr>\</tbody>
\</table>\<table>\<thead>\<tr>\<th>

**cdf:postExecution**

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

Event triggered after a component finishes executing.

\*\*Source:\*\*components/\_doc/events.jsdoc, line 38

\</td>\</tr>\</tbody>
\</table>\<table>\<thead>\<tr>\<th>

**cdf:postFetch**(data)

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

Event triggered after an `UnmanagedComponent` fetches data.

\*\*Source:\*\*components/\_doc/events.jsdoc, line 54

| Name            | Default Value | Summary                                      |
| --------------- | ------------- | -------------------------------------------- |
| data : `object` |               | The data returned from the jQuery.ajax call. |

\</td>\</tr>\</tbody>
\</table>\<table>\<thead>\<tr>\<th>

**cdf:preExecution**

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

Event triggered before a component starts executing.

\*\*Source:\*\*components/\_doc/events.jsdoc, line 30

\</td>\</tr>\</tbody>
\</table>\<table>\<thead>\<tr>\<th>

**cdf:render**

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

Event triggered after the `render` callback executes and before `endExec` executes.

\*\*Source:\*\*components/\_doc/events.jsdoc, line 64

\</td>\</tr>\</tbody>
\</table>\<table id="EVENT:EVENT:ALL">\<thead>\<tr>\<th>

**all**

\</th>\</tr>\</thead>\<tbody>\<tr>\<td>

The `all` event is a special event which will trigger the bound callbacks when any event occurs. This event is mainly used for logging purposes.

\*\*Source:\*\*components/\_doc/events.jsdoc, line 19

**Inherited From:** cdf.components.BaseComponent#event:all

\*\*See also:\*\*Backbone Events catalog.

\</td>\</tr>\</tbody>
\</table> </code></pre></td></tr></tbody></table>
