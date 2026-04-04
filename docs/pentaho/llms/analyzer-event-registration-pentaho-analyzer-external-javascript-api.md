# Source: https://docs.pentaho.com/analyzer-external-javascript-api/using-pentaho-analyzer-external-javascript-api-cp/analyzer-event-registration-pentaho-analyzer-external-javascript-api.md

# Analyzer Event Registration

Analyzer events are API hooks which allow you to register custom listeners into the inner workings of Analyzer. These locations can range from when Analyzer is initialized to when a cell is clicked. For a list of the Event APIs, [click here](https://help.hitachivantara.com/Documentation/Pentaho/Data_Integration_and_Analytics/10.0/Developer_center/Pentaho_Analyzer_External_JavaScript_API_Reference/Event).

## Event Registration

Event registration occurs before Analyzer is initialized. Events are registered using the Analyzer API, which has to be required using [RequireJS](http://requirejs.org/). When triggered, event listeners will execute in the order in which they were registered.

All registered event listeners receive at least three function parameters: e (the event object), and api or cv (global analyzer namespace), as shown is the following example:

```javascript
require(["analyzer/cv_api"], function(api) {
  api.event.registerInitListener(function(e, cv){
    // Perform Action
  });
}

```

## Stop Immediate Propagation

There may be a time when, under special circumstances, a prior event listener will not want any further listeners to be executed. This can be performed by stopping the immediate propagation on the event chain. The function is attached to the event object (e), which is passed into the listeners, as shown in the following example:

```javascript
api.event.registerInitListener(function(e, cv) {
  // Perform Action 1
  e.stopImmediatePropagation();
});
  
api.event.registerInitListener(function(e, cv) {
  // Perform Action 2
});

```

In the above code sample, even though two event listeners have been registered, since the first listener stopped the immediate propagation, the 2nd (and any subsequent) event listener will not be fired.

## Prevent Default

All events have a default behavior associated with them and, in some cases, this behavior can be completely prevented. As with`stopImmediatePropagation`, this is also attached the to the event object (e) and needs to be called within the listener's code block, as shown is the following example:

```javascript
api.event.registerInitListener(function(e, cv) {
  // Perform Action
  e.preventDefault();
});

```

## Removing Listeners

It is possible to remove listeners once they have been registered. A register event listener function returns a handler for that event listener which has a remove function attached to it. Calling this function removes the listener from the event chain, as shown is the following example:

```javascript
var initListenerHandler = api.event.registerInitListener(function(e, cv) {
  // Perform Action
  e.preventDefault();
});
  
initListenerHandler.remove();

```

## Attaching Event Listener Code

To insert your own custom javascript file, you must modify plugin.xml inside of your plugin folder. Currently, there is a commented line which is pointed at an example file inside of the analyzer's plugin script folder. If you would like to see this file working, uncomment that line by deleting the `<!--` and `-->` surrounding the `<file>` tag, as shown is the following example:

```javascript
<!-- <file context="analyzer">content/analyzer/scripts/api_examples/EventRegistration.js</file> -->

```

**Note:** You must restart your server to see these changes.

## Events

The following are events in Analyzer:

<table data-header-hidden><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>Event</td><td>Description</td></tr><tr><td>Example</td><td></td></tr><tr><td><code>init</code></td><td>The <code>init</code> event occurs after Analyzer's UI has initialized and the report definition (if opening a saved report) has been loaded into the editor. Once all init handlers have been called, the report will automatically refresh its data so you do not need to call <code>refreshReport</code> in the init handler.</td></tr><tr><td><pre class="language-javascript"><code class="lang-javascript">cv.api.event.registerInitListener(function(e, cv) {2
  // Perform Action
  // e.stopImmediatePropagation();
});
</code></pre></td><td></td></tr><tr><td><code>onTableClick</code></td><td>The <code>onTableClick</code> event works only for the pivot table view. The event occurs after a user clicks on a table cell. The registered <code>onTableClick</code> handlers are executed first, followed by the default on click event handlers. This event supports the <code>stopImmediatePropagation</code> and <code>preventDefault</code> functions.This method signature contains a <code>td</code> parameter. This parameter contains the <code>&#x3C;td></code> dom element that was clicked by the user.</td></tr><tr><td><pre class="language-javascript"><code class="lang-javascript">cv.api.event.registerTableClickListener(function(e, api, td, ctx, filterCtx) {
  // Perform action
  // e.preventDefault();
  // e.stopImmediatePropagation();
});

</code></pre></td><td></td></tr><tr><td><code>onTableContextMenu</code></td><td>The <code>onTableContextMenu</code> event works only for the pivot table view. The event occurs after a user opens the context menu on a table cell, via the right-click menu. The registered <code>onTableContextMenu</code> handlers are executed first, followed by the default on click event handlers. This event supports the <code>stopImmediatePropagation</code> and <code>preventDefault</code> functions.This method signature contains a <code>td</code> parameter. This parameter contains the <code>\<td></code> dom element that was clicked by the user.</td></tr><tr><td><pre class="language-javascript"><code class="lang-javascript">cv.api.event.registerTableContextMenuListener(function(e, api, td, ctx, filterCtx) {
// Perform action
// e.preventDefault();
// e.stopImmediatePropagation();
}); </code></pre></td><td></td></tr><tr><td><code>render</code></td><td>The <code>render</code> event occurs after the UI has finished drawing the visualization. This event happens after the init event is completed. This event can be used to highlight cells or change the styling of visualization elements. This event type supports <code>stopImmediatePropagation</code>, but does not support <code>preventDefault</code>.This method signature contains a <code>div</code> parameter. This parameter contains the <code>\<div></code> dom element which contains the pivot table or visualization's view.</td></tr><tr><td><pre class="language-javascript"><code class="lang-javascript">cv.api.event.registerRenderListener(function(e, api, reportArea) {
// Perform action
// e.stopImmediatePropagation();
});

</code></pre></td><td></td></tr><tr><td><code>actionEvent</code></td><td>There are multiple action events which are triggered either through UI controls (by the user) or through API calls. Depending on the action, a specific <code>actionCode</code> is passed into the bound listener (Action Codes). Additionally, an <code>actionCtx</code> (action context) is provided to indicate upon which object(s) the action is being performed. This event type supports both <code>preventDefault</code> and <code>stopImmediatePropagation</code>.</td></tr><tr><td><pre class="language-javascript"><code class="lang-javascript">cv.api.event.registerActionEventListener(function(e, api, actionCode, actionCtx) {
//Perform Action
e.preventDefault();
e.stopImmediatePropagation();
});

</code></pre></td><td></td></tr><tr><td><code>buildMenu</code></td><td>The <code>buildMenu</code> event is fired when Analyzer attempts to build a menu within the application. Normally, these menus are built when right-clicking on a table cell or a gem. Also, you may want to hook into this event to override the default behavior and prevent the menu from building such that you can replace the default menu with one of your own.</td></tr><tr><td><pre class="language-javascript"><code class="lang-javascript">cv.api.event.registerBuildMenuListener(function(e, api, menuId, menu, x, y){
//Perform Action on api.\*
e.preventDefault();
e.stopImmediatePropagation();
});

</code></pre></td><td></td></tr><tr><td><code>chartSelectItems</code></td><td>This event is fired when a user selects a chart data point or lassos a collection of data points within an Analyzer visualization. This can be useful to perform an additional action when a user selects an item in a chart.</td></tr><tr><td><pre class="language-javascript"><code class="lang-javascript">cv.api.event.registerChartSelectItemsListener(function(e, api, ctx\[]){
//Perform Action on api.\*
e.stopImmediatePropagation();
});

</code></pre></td><td></td></tr><tr><td><code>chartDoubleClick</code></td><td>This event is fired when the user double-clicks on a chart item. Normally, this would perform a drill-down action, providing a filtered result set.</td></tr><tr><td><pre class="language-javascript"><code class="lang-javascript">cv.api.event.registerChartDoubleClickListener(function(e, api, ctx){
//Perform Action on api.\*
e.preventDefault();
e.stopImmediatePropagation();
});

</code></pre></td><td></td></tr><tr><td><code>dragEvent</code></td><td>Drag events are fired when beginning to drag any draggable item within Analyzer.</td></tr><tr><td><pre class="language-javascript"><code class="lang-javascript">cv.api.event.registerDragEventListener(function(e, api, formula){
//Perform Action on api.\*
e.stopImmediatePropagation();
});

</code></pre></td><td></td></tr><tr><td><code>dropEvent</code></td><td>Drop events are fired when a draggable element has been dropped onto a drop target within the layout panel, report area, trash can, or filter panel. This event is also fired when completing a drop programmatically using <code>cv.api.operation.completeDrop</code> after retrieving a valid drop target from <code>cv.api.operation.getDropTarget</code>.</td></tr><tr><td><pre class="language-javascript"><code class="lang-javascript">cv.api.event.registerDropEventListener(function(e, api, formula, dropClass){
//Perform Action on api.\*
e.stopImmediatePropagation();
});

</code></pre></td><td></td></tr><tr><td><code>tableDoubleClick</code></td><td>This event occurs when double-clicking on a cell within Analyzer's <code>PIVOT</code> table.</td></tr><tr><td><pre class="language-javascript"><code class="lang-javascript">cv.api.event.registerTableDoubleClickListener(function(e, api, td, ctx, filterCtx){
//Perform Action on api.\*
e.preventDefault();
e.stopImmediatePropagation();
});

</code></pre></td><td></td></tr><tr><td><code>tableMouseMove</code></td><td>This event is fired when moving the mouse over a cell within Analyzer's <code>PIVOT</code> table. The listener is executed many times within a small mouse movement. Most often, the (x, y) coordinates of the mouse are recorded using this event.</td></tr><tr><td><pre class="language-javascript"><code class="lang-javascript">cv.api.event.registerTableMouseMoveListener(function(e, api, td, ctx, filterCtx){
//Perform Action on api.\*
e.preventDefault();
e.stopImmediatePropagation();
});

</code></pre></td><td></td></tr><tr><td><code>tableMouseOver</code></td><td>This event is fired when moving the mouse over a cell within Analyzer's <code>PIVOT</code> table. This event is only fired once when the mouse moves over a cell.</td></tr><tr><td><pre class="language-javascript"><code class="lang-javascript">cv.api.event.registerTableMouseOverListener(function(e, api, td, ctx, filterCtx){
//Perform Action on api.\*
e.preventDefault();
e.stopImmediatePropagation();
});

</code></pre></td><td></td></tr></tbody></table>
