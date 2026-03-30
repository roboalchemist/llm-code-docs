# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/helper/util/Rectangle.md

# [Rectangle](https://bryntum.com/docs/gantt/api/Core/helper/util/Rectangle)

Constructs a Rectangle

## Properties

Properties are getters/setters or publicly accessible variables on this class

[center](https://bryntum.com/docs/gantt/api/Core/helper/util/Rectangle#property-center)
The center point of this rectangle.

[x](https://bryntum.com/docs/gantt/api/Core/helper/util/Rectangle#property-x)
Get/sets the X coordinate of the Rectangle. Note that this does _not_ translate the Rectangle. The requested [width](https://bryntum.com/docs/gantt/api/#Core/helper/util/Rectangle#property-width) will change.

[left](https://bryntum.com/docs/gantt/api/Core/helper/util/Rectangle#property-left)
Alias for x. To match DOMRect.

[top](https://bryntum.com/docs/gantt/api/Core/helper/util/Rectangle#property-top)
Alias for y. To match DOMRect.

[y](https://bryntum.com/docs/gantt/api/Core/helper/util/Rectangle#property-y)
Get/sets the Y coordinate of the Rectangle. Note that this does _not_ translate the Rectangle. The requested [height](https://bryntum.com/docs/gantt/api/#Core/helper/util/Rectangle#property-height) will change.

[width](https://bryntum.com/docs/gantt/api/Core/helper/util/Rectangle#property-width)
Get/sets the width of the Rectangle. Note that the requested [right](https://bryntum.com/docs/gantt/api/#Core/helper/util/Rectangle#property-right) will change.

[height](https://bryntum.com/docs/gantt/api/Core/helper/util/Rectangle#property-height)
Get/sets the height of the Rectangle. Note that the requested [bottom](https://bryntum.com/docs/gantt/api/#Core/helper/util/Rectangle#property-bottom) will change.

[right](https://bryntum.com/docs/gantt/api/Core/helper/util/Rectangle#property-right)
Get/sets the right edge of the Rectangle. Note that the requested [width](https://bryntum.com/docs/gantt/api/#Core/helper/util/Rectangle#property-width) will change.

The right edge value is exclusive of the calculated rectangle width. So x=0 and right=10 means a width of 10.

[bottom](https://bryntum.com/docs/gantt/api/Core/helper/util/Rectangle#property-bottom)
Get/sets the bottom edge of the Rectangle. Note that the requested [height](https://bryntum.com/docs/gantt/api/#Core/helper/util/Rectangle#property-height) will change.

The bottom edge value is exclusive of the calculated rectangle height. So y=0 and bottom=10 means a height of 10.

## Functions

Functions are methods available for calling on the class

[from](https://bryntum.com/docs/gantt/api/Core/helper/util/Rectangle#function-from-static)
Returns the Rectangle in document based coordinates of the passed element.

_Note:_ If the element passed is the `document` or `window` the `window`'s rectangle is returned which is always at `[0, 0]` and encompasses the browser's entire document viewport.

[fromScreen](https://bryntum.com/docs/gantt/api/Core/helper/util/Rectangle#function-fromScreen-static)
Returns the Rectangle in viewport coordinates of the passed element.

_Note:_ If the element passed is the `document` or `window` the `window`'s rectangle is returned which is always at `[0, 0]` and encompasses the browser's entire document viewport.

[inner](https://bryntum.com/docs/gantt/api/Core/helper/util/Rectangle#function-inner-static)
Returns the inner Rectangle (within border) in document based coordinates of the passed element.

[content](https://bryntum.com/docs/gantt/api/Core/helper/util/Rectangle#function-content-static)
Returns the content Rectangle (within border and padding) in document based coordinates of the passed element.

[client](https://bryntum.com/docs/gantt/api/Core/helper/util/Rectangle#function-client-static)
Returns the client Rectangle (within border and padding and scrollbars) in document based coordinates of the passed element.

[outer](https://bryntum.com/docs/gantt/api/Core/helper/util/Rectangle#function-outer-static)
Returns the outer Rectangle (including margin) in document based coordinates of the passed element.

[union](https://bryntum.com/docs/gantt/api/Core/helper/util/Rectangle#function-union-static)
Returns a new rectangle created as the union of all supplied rectangles.

[roundPx](https://bryntum.com/docs/gantt/api/Core/helper/util/Rectangle#function-roundPx)
Rounds this Rectangle to the pixel resolution of the current display or to the nearest passed unit which defaults to the current display's [`devicePixelRatio`](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/API/Window/devicePixelRatio).

[clone](https://bryntum.com/docs/gantt/api/Core/helper/util/Rectangle#function-clone)
Creates a copy of this Rectangle.

[contains](https://bryntum.com/docs/gantt/api/Core/helper/util/Rectangle#function-contains)
Returns `true` if this Rectangle wholly contains the passed rectangle.

Note that a [Point](https://bryntum.com/docs/gantt/api/#Core/helper/util/Rectangle/Point) may be passed.

[exclude](https://bryntum.com/docs/gantt/api/Core/helper/util/Rectangle#function-exclude)
Clips off the area of the "other" Rectangle(s) from this Rectangle if any of the the other rectangles occlude a whole edge of this Rectangle.

In the example below, the `other` Rectangle obscures the whole of the left edge of `this` Rectangle.

The result from this call would be a Rectangle with the left edge moved to the right edge of the `other` Rectangle.

This is useful for clipping off sticky elements which are docked to the edges of an element.

```
  other                   this
┌───────┐─────────────────────────────────────────┐
│   │   │                                         │
│   │   │                                         │
│   │   │                                         │
│   │   │                                         │
│   │   │                                         │
│   │   │                                         │
└───────┘─────────────────────────────────────────┘
```

[intersect](https://bryntum.com/docs/gantt/api/Core/helper/util/Rectangle#function-intersect)
Checks if this Rectangle intersects the passed Rectangle

[translate](https://bryntum.com/docs/gantt/api/Core/helper/util/Rectangle#function-translate)
Translates this Rectangle by the passed vector. Size is maintained.

[moveTo](https://bryntum.com/docs/gantt/api/Core/helper/util/Rectangle#function-moveTo)
Moves this Rectangle to the passed `x`, `y` position. Size is maintained.

[getDelta](https://bryntum.com/docs/gantt/api/Core/helper/util/Rectangle#function-getDelta)
Returns the vector which would translate this Rectangle (or Point) to the same position as the other Rectangle (or point)

[adjust](https://bryntum.com/docs/gantt/api/Core/helper/util/Rectangle#function-adjust)
Modifies the bounds of this Rectangle by the specified deltas.

[inflate](https://bryntum.com/docs/gantt/api/Core/helper/util/Rectangle#function-inflate)
Modifies the bounds of this rectangle by expanding them by the specified amount in all directions. The parameters are read the same way as CSS margin values.

Number of values passed:

* One: all edges are inflated by that value.
* Two: values are top/bottom deflation and left/right inflation.
* Three: values are top, left/right, and bottom.
* Four: the values are top, right, bottom, and left.

[deflate](https://bryntum.com/docs/gantt/api/Core/helper/util/Rectangle#function-deflate)
Modifies the bounds of this rectangle by reducing them by the specified amount in all directions. The parameters are read the same way as CSS margin values.

Number of values passed:

* One: all edges are deflated by that value.
* Two: values are top/bottom deflation and left/right deflation.
* Three: values are top, left/right, and bottom.
* Four: the values are top, right, bottom, and left.

[constrainTo](https://bryntum.com/docs/gantt/api/Core/helper/util/Rectangle#function-constrainTo)
Attempts to constrain this Rectangle into the passed Rectangle. If the `strict` parameter is `true` then this method will return `false` if constraint could not be achieved.

If this Rectangle has a `minHeight` or `minWidth` property, size will be adjusted while attempting to constrain.

Right and bottom are adjusted first leaving the top and bottom sides to "win" in the case that this Rectangle overflows the constrainTo Rectangle.

[alignTo](https://bryntum.com/docs/gantt/api/Core/helper/util/Rectangle#function-alignTo)
Returns a cloned version of this Rectangle aligned to a target Rectangle, or element or [Widget](https://bryntum.com/docs/gantt/api/#Core/widget/Widget).

[getAlignmentPoint](https://bryntum.com/docs/gantt/api/Core/helper/util/Rectangle#function-getAlignmentPoint)
Returns the `[x, y]` position of the specified anchor point of this Rectangle in format. for example passing "t50" will return the centre point of the top edge, passing "r0" will return the start position of the right edge (the top right corner).

Note that the offset defaults to 50, so "t" means the centre of the top edge.

[highlight](https://bryntum.com/docs/gantt/api/Core/helper/util/Rectangle#function-highlight)
Highlights this Rectangle using the highlighting effect of [DomHelper](https://bryntum.com/docs/gantt/api/#Core/helper/DomHelper) on a transient element which encapsulates the region's area.

[visualize](https://bryntum.com/docs/gantt/api/Core/helper/util/Rectangle#function-visualize)
Visualizes this Rectangle by adding a DOM element which encapsulates the region's area into the provided parent element.

## Typedefs

Typedefs are type definitions for the class

[AlignResult](https://bryntum.com/docs/gantt/api/Core/helper/util/Rectangle#typedef-AlignResult)
