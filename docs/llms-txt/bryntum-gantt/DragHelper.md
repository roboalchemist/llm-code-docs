# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/helper/DragHelper.md

# [DragHelper](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper)

Intro
-----

A drag drop helper class which lets you move elements in page. It supports:

* Dragging the actual element
* Dragging a cloned version of the element
* Dragging extra `relatedElements` along with the main element
* Firing useful events [beforeDragStart](https://bryntum.com/docs/gantt/api/#Core/helper/DragHelper#event-beforeDragStart), [dragStart](https://bryntum.com/docs/gantt/api/#Core/helper/DragHelper#event-dragStart), [drag](https://bryntum.com/docs/gantt/api/#Core/helper/DragHelper#event-drag), [drop](https://bryntum.com/docs/gantt/api/#Core/helper/DragHelper#event-drop), [abort](https://bryntum.com/docs/gantt/api/#Core/helper/DragHelper#event-abort)
* Validation by setting a `valid` Boolean on the drag context object provided to event listeners
* Aborting drag with ESCAPE key
* Constraining drag to be only horizontal or vertical using [lockX](https://bryntum.com/docs/gantt/api/#Core/helper/DragHelper#config-lockX) and [lockY](https://bryntum.com/docs/gantt/api/#Core/helper/DragHelper#config-lockY)
* Defining X / Y boundaries using [minX](https://bryntum.com/docs/gantt/api/#Core/helper/DragHelper#config-minX), [maxX](https://bryntum.com/docs/gantt/api/#Core/helper/DragHelper#config-maxX) and [minY](https://bryntum.com/docs/gantt/api/#Core/helper/DragHelper#config-minY), [maxY](https://bryntum.com/docs/gantt/api/#Core/helper/DragHelper#config-maxY)
* Async finalization (e.g. to show confirmation prompts)
* Animated final transition after mouse up of a valid drop (see [animateProxyTo](https://bryntum.com/docs/gantt/api/#Core/helper/DragHelper#function-animateProxyTo))
* Animated abort transition after an invalid or aborted drop

Two modes
---------

DragHelper supports two [modes](https://bryntum.com/docs/gantt/api/#Core/helper/DragHelper#config-mode):

* `container` - moving / rearranging elements within and between specified containers
* `translateXY` - freely repositioning an element, either using the element or a cloned version of it - a "drag proxy" (default mode)

Container drag mode
-------------------

Container drag should be used when moving or rearranging child elements within and between specified containers

Example:

```
// dragging element between containers
let dragHelper = new DragHelper({
  mode       : 'container',
  containers : [ container1, container2 ]
});
```

Translate drag mode
-------------------

Use translate drag to reposition an element within its container using translate CSS.

Example:

```
// dragging element within container
let dragHelper = new DragHelper({
  mode           : 'translateXY',
  targetSelector : 'div.movable'
});
```

Observable events
-----------------

In the various events fired by the DragHelper, you will have access to the raw DOM event and some useful `context` about the drag operation:

```
 myDrag.on({
     drag : ({event , context}) {
           // The element which we're moving, could be a cloned version of grabbed, or the grabbed element itself
          const element = context.element;

          // The original mousedown element upon which triggered the drag operation
          const grabbed = context.grabbed;

          // The target under the current mouse / pointer / touch position
          const target = context.target;
      }
 });
```

Simple drag helper subclass with a drop target specified
---------------------------------------------------------

```
export default class MyDrag extends DragHelper {
     static configurable = {
         // Don't drag the actual cell element, clone it
         cloneTarget        : true,
         mode               : 'translateXY',
         // Only allow drops on DOM elements with 'yourDropTarget' CSS class specified
         dropTargetSelector : '.yourDropTarget',

         // Only allow dragging elements with the 'draggable' CSS class
         targetSelector : '.draggable'
     }

     construct(config) {
         const me = this;

         super.construct(config);

         me.on({
             dragstart : me.onDragStart
         });
     }

     onDragStart({ event, context }) {
         const target = context.target;

         // Here you identify what you are dragging (an image of a user, grid row in an order table etc) and map it to something in your
         // data model. You can store your data on the context object which is available to you in all drag-related events
         context.userId = target.dataset.userId;
     }

     onEquipmentDrop({ context, event }) {
         const me = this;

         if (context.valid) {
             const userId   = context.userId,
                   droppedOnTarget = context.target;

             console.log(`You dropped user ${userStore.getById(userId).name} on ${droppedOnTarget}`, droppedOnTarget);

             // Dropped on a scheduled event, display toast
             Toast.show(`You dropped user ${userStore.getById(userId).name} on ${droppedOnTarget}`);
         }
     }
 };
```

Dragging multiple elements
--------------------------

You can tell the DragHelper to also move additional `relatedElements` when a drag operation is starting. Simply provide an array of elements on the context object:

```
new DragHelper ({
    callOnFunctions : true,

    onDragStart({ context }) {
         // Let drag helper know about extra elements to drag
         context.relatedElements = Array.from(element.querySelectorAll('.b-resource-avatar'));
    }
});
```

Creating a custom drag proxy
----------------------------

Using the [createProxy](https://bryntum.com/docs/gantt/api/#Core/helper/DragHelper#function-createProxy) you can create any markup structure to use when dragging cloned targets.

```
new DragHelper ({
   callOnFunctions      : true,
   // Don't drag the actual cell element, clone it
   cloneTarget          : true,
   // We size the cloned element using CSS
   autoSizeClonedTarget : false,

   mode               : 'translateXY',
   // Only allow drops on certain DOM nodes
   dropTargetSelector : '.myDropTarget',
   // Only allow dragging cell elements in a Bryntum Grid
   targetSelector     : '.b-grid-row:not(.b-group-row) .b-grid-cell'

   // Here we receive the element where the drag originated and we can choose to return just a child element of it
   // to use for the drag proxy (such as an icon)
   createProxy(element) {
       return element.querySelector('i').cloneNode();
   }
});
```

Animating a cloned drag proxy to a point before finalizing
----------------------------------------------------------

To provide users with the optimal user experience, you can set a `transitionTo` object (with `target` element and `align` spec) on the DragHelper´s `context` object inside a [drop](https://bryntum.com/docs/gantt/api/#Core/helper/DragHelper#event-drop) listener (only applies to translate [mode](https://bryntum.com/docs/gantt/api/#Core/helper/DragHelper#config-mode) operations). This will trigger a final animation of the drag proxy which should represent the change of data state that will be triggered by the drop.

You can see this in action in Gantt´s `drag-resource-from-grid` demo.

```
new DragHelper ({
   callOnFunctions      : true,
   // Don't drag the actual cell element, clone it
   cloneTarget          : true,
   // We size the cloned element using CSS
   autoSizeClonedTarget : false,

   mode               : 'translateXY',
   // Only allow drops on certain DOM nodes
   dropTargetSelector : '.myDropTarget',
   // Only allow dragging cell elements in a Bryntum Grid
   targetSelector     : '.b-grid-row:not(.b-group-row) .b-grid-cell'

   // Here we receive the element where the drag originated and we can choose to return just a child element of it
   // to use for the drag proxy (such as an icon)
   createProxy(element) {
       return element.querySelector('i').cloneNode();
   },

   async onDrop({ context, event }) {
      // If it's a valid drop, provide a point to animate the proxy to before finishing the operation
     if (context.valid) {
         await this.animateProxyTo(someElement, {
              // align left side of drag proxy to right side of the someElement
              align  : 'l0-r0'
         });
     }
     else {
         Toast.show(`You cannot drop here`);
     }
  }
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[dragProxyCls](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#config-dragProxyCls)
Drag proxy CSS class

[invalidCls](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#config-invalidCls)
CSS class added when drag is invalid

[draggingCls](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#config-draggingCls)
CSS class added to the source element in Container drag

[dropPlaceholderCls](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#config-dropPlaceholderCls)
CSS class added to the source element in Container drag

[dragThreshold](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#config-dragThreshold)
The amount of pixels to move mouse before it counts as a drag operation

[outerElement](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#config-outerElement)
The outer element where the drag helper will operate (attach events to it and use as outer limit when looking for ancestors)

[dragWithin](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#config-dragWithin)
Outer element that limits where element can be dragged

[unifiedProxy](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#config-unifiedProxy)
Set to `true` to stack any related dragged elements below the main drag proxy element. Only applicable when using translate [mode](https://bryntum.com/docs/gantt/api/#Core/helper/DragHelper#config-mode) with [cloneTarget](https://bryntum.com/docs/gantt/api/#Core/helper/DragHelper#config-cloneTarget)

[constrain](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#config-constrain)
Constrain translate drag to dragWithin elements bounds (set to `false` to allow it to "overlap" edges)

[minX](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#config-minX)
Smallest allowed x when dragging horizontally.

[maxX](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#config-maxX)
Largest allowed x when dragging horizontally.

[minY](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#config-minY)
Smallest allowed y when dragging horizontally.

[maxY](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#config-maxY)
Largest allowed y when dragging horizontally.

[mode](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#config-mode)
Enabled dragging, specify mode:

container

Allows reordering elements within one and/or between multiple containers

translateXY

Allows dragging within a parent container

[isElementDraggable](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#config-isElementDraggable)
A function that determines if dragging an element is allowed. Gets called with the element as argument, return `true` to allow dragging or `false` to prevent.

[targetSelector](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#config-targetSelector)
A CSS selector used to target draggable elements. See also [target](https://bryntum.com/docs/gantt/api/#Core/helper/DragHelper#config-target).

[target](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#config-target)
A Widget or HTML element to drag. See also [targetSelector](https://bryntum.com/docs/gantt/api/#Core/helper/DragHelper#config-targetSelector).

[dropTargetSelector](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#config-dropTargetSelector)
A CSS selector used to determine if a drop is allowed at the current position.

[dropTargetCls](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#config-dropTargetCls)
A CSS selector added to each drop target element while dragging.

[proxySelector](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#config-proxySelector)
A CSS selector used to target a child element of the mouse down element, to use as the drag proxy element. Applies to translate [mode](https://bryntum.com/docs/gantt/api/#Core/helper/DragHelper#config-mode) when using [cloneTarget](https://bryntum.com/docs/gantt/api/#Core/helper/DragHelper#config-cloneTarget).

[cloneTarget](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#config-cloneTarget)
Set to `true` to clone the dragged target, and not move the actual target DOM node.

[autoSizeClonedTarget](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#config-autoSizeClonedTarget)
Set to `false` to not apply width/height of cloned drag proxy elements.

[hideOriginalElement](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#config-hideOriginalElement)
Set to `true` to hide the original element while dragging (applicable when `cloneTarget` is true).

[containers](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#config-containers)
Containers whose elements can be rearranged (and moved between the containers). Used when mode is set to "container".

[ignoreSelector](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#config-ignoreSelector)
A CSS selector used to exclude elements when using container mode

[lockX](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#config-lockX)
Configure as `true` to disallow dragging in the `X` axis. The dragged element will only move vertically.

[lockY](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#config-lockY)
Configure as `true` to disallow dragging in the `Y` axis. The dragged element will only move horizontally.

[touchStartDelay](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#config-touchStartDelay)
The amount of milliseconds to wait after a touchstart, before a drag gesture will be allowed to start.

[scrollManager](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#config-scrollManager)
Scroll manager of the target. If specified, scrolling while dragging is supported.

[snapCoordinates](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#config-snapCoordinates)
A method provided to snap coordinates to fixed points as you drag

[unifiedOffset](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#config-unifiedOffset)
When using [unifiedProxy](https://bryntum.com/docs/gantt/api/#Core/helper/DragHelper#config-unifiedProxy), use this amount of pixels to offset each extra element when dragging multiple items

[removeProxyAfterDrop](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#config-removeProxyAfterDrop)
Configure as `false` to take ownership of the proxy element after a valid drop (advanced usage).

[createProxy](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#config-createProxy)
Creates the proxy element to be dragged, when using [cloneTarget](https://bryntum.com/docs/gantt/api/#Core/helper/DragHelper#config-cloneTarget). Clones the original element by default. Provide your custom [createProxy](https://bryntum.com/docs/gantt/api/#Core/helper/DragHelper#function-createProxy) function to be used for creating drag proxy.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isDragHelper](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#property-isDragHelper)
Identifies an object as an instance of [DragHelper](https://bryntum.com/docs/gantt/api/#Core/helper/DragHelper) class, or subclass thereof.

[isDragHelper](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#property-isDragHelper-static)
Identifies an object as an instance of [DragHelper](https://bryntum.com/docs/gantt/api/#Core/helper/DragHelper) class, or subclass thereof.

[isDragging](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#property-isDragging)
Returns true if a drag operation is active

## Functions

Functions are methods available for calling on the class

[constructor](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#function-constructor)
Initializes a new DragHelper.

[initListeners](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#function-initListeners)
Initialize listener

[onMouseMove](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#function-onMouseMove)
Move drag element with mouse.

[update](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#function-update)
Updates drag, called when an element is grabbed and mouse moves

[abort](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#function-abort)
Abort dragging

[onDocumentClick](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#function-onDocumentClick)
This is a capture listener, only added during drag, which prevents a click gesture propagating from the terminating mouseup gesture

[onMouseUp](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#function-onMouseUp)
Drop on mouse up (if dropped on valid target).

[onKeyDown](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#function-onKeyDown)
Cancel on ESC key

[createProxy](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#function-createProxy)
Creates the proxy element to be dragged, when using [cloneTarget](https://bryntum.com/docs/gantt/api/#Core/helper/DragHelper#config-cloneTarget). Clones the original element by default. Override it to provide your own custom HTML element structure to be used as the drag proxy.

[animateProxyTo](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#function-animateProxyTo)
Animated the proxy element to be aligned with the passed element. Returns a Promise which resolves after the DOM transition completes. Only applies to 'translateXY' mode.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeDragStart](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#event-beforeDragStart)
Fired before dragging starts, return `false` to prevent the drag operation.

[dragStart](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#event-dragStart)
Fired when dragging starts. The event includes a `context` object. If you want to drag additional elements you can provide these as an array of elements assigned to the `relatedElements` property of the context object.

[drag](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#event-drag)
Fired while dragging, you can signal that the drop is valid or invalid by setting `context.valid = false;`

[abort](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#event-abort)
Fired after a drop at an invalid position

[abortFinalized](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#event-abortFinalized)
Fires after [abort](https://bryntum.com/docs/gantt/api/#Core/helper/DragHelper#event-abort) and after drag proxy has animated back to its original position

[drop](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#event-drop)
Fires after drop. For valid drops, it exposes `context.async` which you can set to `true` to signal that additional processing is needed before finalizing the drop (such as showing some dialog). When that operation is done, call `context.finalize(true/false)` with a boolean that determines the outcome of the drop.

You can signal that the drop is valid or invalid by setting `context.valid = false;`

For translate type drags with [cloneTarget](https://bryntum.com/docs/gantt/api/#Core/helper/DragHelper#config-cloneTarget), you can also set `transitionTo` if you want to animate the dragged proxy to a position before finalizing the operation. See class intro text for example usage.

[dropFinalized](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#event-dropFinalized)
Fires after [drop](https://bryntum.com/docs/gantt/api/#Core/helper/DragHelper#event-drop) and after drag proxy has animated to its final position (if setting `transitionTo` on the drag context object).

[reset](https://bryntum.com/docs/gantt/api/Core/helper/DragHelper#event-reset)
Fired after a drag operation is completed or aborted
