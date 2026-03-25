# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/helper/DomHelper.md

# [DomHelper](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper)

Helps with dom querying and manipulation.

```
DomHelper.createElement({
  tag       : 'div',
  className : 'parent',
  style     : 'background: red',
  children  : [
     { tag: 'div', className: 'child' },
     { tag: 'div', className: 'child' }
  ]
});
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[enableKeyboardCssModifiers](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#property-enableKeyboardCssModifiers)
Set to `false` to not show focus renditions when using keyboard

[activeElement](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#property-activeElement-static)
Returns active element checking shadow dom too

[scrollBarWidth](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#property-scrollBarWidth-static)
Measures the scrollbar width using a hidden div. Caches result

[scrollLimit](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#property-scrollLimit-static)
Returns the maximum scroll range the browser can correctly manage. This value is browser-specific and typically in the millions of pixels. This answer is not intended to be a precise value but a safe and reliable value to avoid encountering browser limitations.

[themeInfo](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#property-themeInfo-static)
A theme information object about the current theme. Note, when using Bryntum widgets inside a shadowRoot context, you need to use [getThemeInfo](https://bryntum.com/docs/gantt/api/#Core/helper/DomHelper#function-getThemeInfo-static) and pass a context element.

[primaryColor](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#property-primaryColor-static)
Get the current themes primary color (by reading it from `document.body`)

[isDarkTheme](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#property-isDarkTheme-static)
Check if the currently used theme is a dark theme, by checking the `color-scheme` property of `.b-widget`.

## Functions

Functions are methods available for calling on the class

[slideIn](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-slideIn-static)
Animates the specified element to slide it into view within the visible viewport of its parentElement from the direction of movement.

So in a left-to-right Widget, `direction` 1 means it slides in from the right and `direction` -1 means it slides in from the left. RTL reverses the movement.

See the forward/backward navigations in [DatePicker](https://bryntum.com/docs/gantt/api/#Core/widget/DatePicker) for an example of this in action.

If "next" should arrive from below and "previous" should arrive from above, add the class `b-slide-vertical` to the element.

[getExpando](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-getExpando-static)
Returns a dynamic property from a DOM element given a dot-path name. All of these properties are stored on a `$bryntum` object property lazily added to the `element`.

For example:

```
const v = DomHelper.getExpando(el, 'foo');
```

Is equivalent to:

```
const v = el.$bryntum?.foo;
```

Also:

```
const v = DomHelper.getExpando(el, 'foo', 42);
```

Is equivalent to:

```
const v = (el.$bryntum && 'foo' in el.$bryntum) ? el.$bryntum.foo : 42;
```

The `key` parameter can also be a dot-path, like so:

```
const v = DomHelper.getExpando(el, 'foo.bar', 42);
```

Is equivalent to:

```
const v = (el.$bryntum?.foo && 'bar' in el.$bryntum.foo) ? el.$bryntum.foo.bar : 42;
```

[getExpandos](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-getExpandos-static)
Returns a lazily created object attached to `element` given its `key`. The `key` parameter can be a simple name or a dot-path.

For example:

```
const obj = DomHelper.getExpandos(el, 'foo');
```

Is equivalent to:

```
const obj = (el.$bryntum || (el.$bryntum = Object.create(null))).foo ||
            (el.$bryntum.foo = Object.creat(null));
```

[removeExpando](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-removeExpando-static)
Removes a dynamic property from a DOM element given a dot-path name.

[setExpando](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-setExpando-static)
Stores a dynamic property on a DOM element given a dot-path name. All of these properties are stored on a `$bryntum` object property lazily added to the `element`.

For example:

```
DomHelper.setExpando(el, 'foo', 42);
```

Is equivalent to:

```
(el.$bryntum || (el.$bryntum = Object.create(null))).foo = 42;
```

[getFocusability](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-getFocusability-static)
Returns an object describing the focus and keyboard navigation aspects of a given element.

By default, it returns the general abilities of the element to be focused, _not_ taking into account whether the element is currently visible.

To check whether the element is currently focusable in the UI, pass `true` as the second parameter.

[isClipping](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-isClipping-static)
Checks if an element clips its content.

[isFocusable](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-isFocusable-static)
Returns `true` if the passed element is focusable either programmatically or through pointer gestures.

[isEditable](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-isEditable-static)
Returns `true` if the passed element accepts keystrokes to edit its contents.

[isInView](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-isInView-static)
Returns the rectangle of the element or event which is currently visible in the browser viewport, i.e. user can find it on screen, or `false` if it is scrolled out of view.

[getViewportIntersection](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-getViewportIntersection-static)
This method checks that the passed target is visible in all viewports

[isVisible](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-isVisible-static)
Returns `true` if the passed element is deeply visible. Meaning it is not hidden using `display` or `visibility` and no ancestor node is hidden.

[isDOMEvent](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-isDOMEvent-static)
Returns true if DOM Event instance is passed. It is handy to override to support Locker Service.

[merge](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-merge-static)
Merges specified source DOM config objects into a `dest` object.

[normalizeChildren](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-normalizeChildren-static)
Updates in-place a DOM config object whose `children` property may be an object instead of the typical array. The keys of such objects become the `reference` property upon conversion.

[isCustomElement](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-isCustomElement-static)
Returns true if element has opened shadow root

[elementFromPoint](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-elementFromPoint-static)
Resolves element from point, checking shadow DOM if required

[childFromPoint](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-childFromPoint-static)
Resolves child element from point **in the passed element's coordinate space**.

[unitize](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-unitize-static)
Converts a name/value pair of a style name and its value into the canonical (hyphenated) name of the style property and a value with the `defaultUnit` suffix appended if no unit is already present in the `value`.

For example:

```
 const [property, value] = DomHelper.unitize('marginInlineStart', 50);
 console.log(property, value);
```

```
 > margin-inline-start 50px
```

[getId](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-getId-static)
Returns the `id` of the passed element. Generates a unique `id` if the element does not have one.

[getCommonAncestor](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-getCommonAncestor-static)
Returns common widget/node ancestor for from/to arguments

[waitForSelector](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-waitForSelector-static)
Waits for the specified target element to be visible and in view, and not within an animation.

If the specified selector is not immediately visible and outside of any animations, this method will return a Promise which, if the element becomes available in the specified `maxWait`, resolves to the target `HTMLElement`.

If the element does not become available after the `maxWait`, the Promise will reject.

If the selector ends with `?`, or the `maxWait` is negative, the target element is optional and if not found, `undefined` is returned.

[getElement](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-getElement-static)
Internal convenience fn to allow specifying either an element or a CSS selector to retrieve one

[setAttributes](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-setAttributes-static)
Sets attributes passed as object to given element

[addAttributeValue](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-addAttributeValue-static)
Adds the passed string as a space-separated value to the passed attribute in the passed element.

[removeAttributeValue](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-removeAttributeValue-static)
Removed the passed string as a space-separated value from the passed attribute in the passed element.

[setLength](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-setLength-static)
Sets a CSS [length](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/CSS/length) style value.

[percentify](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-percentify-static)
Returns string percentified and rounded value for setting element's height, width etc.

[getChild](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-getChild-static)
Gets the first direct child of `element` that matches `selector`.

[hasChild](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-hasChild-static)
Checks if `element` has any child that matches `selector`.

[children](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-children-static)
Returns all child elements (not necessarily direct children) that matches `selector`.

If `selector` starts with `'>'` or `'# '`, then all components of the `selector` must match inside of `element`. The scope selector, `:scope` is prepended to the selector (and if `#` was used, it is removed).

These are equivalent:

```
 DomHelper.children(el, '# .foo .bar');

 el.querySelectorAll(':scope .foo .bar');
```

These are also equivalent:

```
 DomHelper.children(el, '> .foo .bar');

 el.querySelectorAll(':scope > .foo .bar');
```

[down](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-down-static)
Looks at the specified `element` and all of its children for the one that first matches `selector`.

[isDescendant](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-isDescendant-static)
Checks if childElement is a descendant of parentElement (contained in it or a sub element)

[getEventElement](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-getEventElement-static)
Returns the specified element of the given `event`. If the `event` is an `Element`, it is returned. Otherwise, the `eventName` argument is used to retrieve the desired element property from `event` (this defaults to the `'target'` property).

[isElement](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-isElement-static)
Returns `true` if the provided value is _likely_ a DOM element. If the element can be assured to be from the same document, `instanceof Element` is more reliable.

[isReactElement](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-isReactElement-static)
Returns `true` if the provided element is an instance of React Element.

[handleReactElement](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-handleReactElement-static)
Handles the content provided by a React component for the widget.

[handleReactHeaderElement](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-handleReactHeaderElement-static)
Handles the React header element by processing JSX content within the widget.

[isVueConfig](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-isVueConfig-static)
Returns `true` if the provided configuration object is valid for Vue processing.

[handleVueContent](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-handleVueContent-static)
Handles the content provided by a Vue component for the widget.

[isNode](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-isNode-static)
Returns `true` if the provided value is _likely_ a DOM node. If the node can be assured to be from the same document, `instanceof Node` is more reliable.

[forEachSelector](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-forEachSelector-static)
Iterates over each result returned from `element.querySelectorAll(selector)`. Can also be called with only two arguments, in which case the first argument is used as selector and document is used as the element.

[forEachChild](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-forEachChild-static)
Iterates over the direct child elements of the specified element.

[removeEachSelector](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-removeEachSelector-static)
Removes each element returned from `element.querySelectorAll(selector)`.

[removeClsGlobally](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-removeClsGlobally-static)
Removes the passed CSS classes from all descendants of the passed element.

[getParents](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-getParents-static)
Retrieves all parents to the specified element.

[makeValidId](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-makeValidId-static)
Converts the passed id to an id valid for usage as id on a DOM element.

[createElement](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-createElement-static)
Creates an Element, accepts a [DomConfig](https://bryntum.com/docs/gantt/api/#Core/helper/DomHelper#typedef-DomConfig) object. Example usage:

```
DomHelper.createElement({
  tag         : 'table', // defaults to 'div'
  className   : 'nacho',
  html        : 'I am a nacho',
  children    : [ { tag: 'tr', ... }, myDomElement ],
  parent      : myExistingElement // Or its id
  style       : 'font-weight: bold;color: red',
  dataset     : { index: 0, size: 10 },
  tooltip     : 'Yay!',
  ns          : 'http://www.w3.org/1999/xhtml'
});
```

[createElementFromTemplate](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-createElementFromTemplate-static)
Create element(s) from a template (html string). Note that `textNode`s are discarded unless the `raw` option is passed as `true`.

If the template has a single root element, then the single element will be returned unless the `array` option is passed as `true`.

If there are multiple elements, then an Array will be returned.

[triggerMouseEvent](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-triggerMouseEvent-static)
Dispatches a MouseEvent of the passed type to the element at the visible centre of the passed element. If the element is not in view, the event is not dispatched.

[insertFirst](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-insertFirst-static)
Inserts an `element` at first position in `into`.

[insertBefore](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-insertBefore-static)
Inserts an `element` before `beforeElement` in `into`.

[append](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-append-static)
Appends element to parentElement.

[getTranslateX](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-getTranslateX-static)
Returns the `x` from the element's `translate: x y` value in pixels.

[getTranslateY](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-getTranslateY-static)
Returns the `y` from the element's `translate: x y` value in pixels.

[getTranslateXY](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-getTranslateXY-static)
Gets both X and Y coordinates as an array \[x, y\]

[getOffsetX](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-getOffsetX-static)
Get elements X offset within a containing element

[getOffsetY](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-getOffsetY-static)
Get elements Y offset within a containing element

[getOffsetXY](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-getOffsetXY-static)
Gets elements X and Y offset within containing element as an array \[x, y\]

[getPageX](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-getPageX-static)
Get elements X position on page

[getPageY](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-getPageY-static)
Get elements Y position on page

[getExtremalSizePX](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-getExtremalSizePX-static)
Returns extremal (min/max) size (height/width) of the element in pixels

[setScale](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-setScale-static)
Set element's `scale`.

[setTranslateX](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-setTranslateX-static)
Set element's `X` translation in pixels (keepin `Y` translation as is).

[setTranslateY](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-setTranslateY-static)
Set element's `Y` translation in pixels (keeping `X` translation as is).

[setTop](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-setTop-static)
Set element's style `top`.

[setLeft](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-setLeft-static)
Set element's style `left`.

[setTranslateXY](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-setTranslateXY-static)
Set elements `X` and `Y` translation in pixels.

[addTranslateX](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-addTranslateX-static)
Increase `X` translation

[addTranslateY](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-addTranslateY-static)
Increase `Y` position

[addLeft](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-addLeft-static)
Increase X position

[addTop](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-addTop-static)
Increase Y position

[alignTo](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-alignTo-static)
Align the passed element with the passed target according to the align spec.

[getStyleValue](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-getStyleValue-static)
Returns a style value or values for the passed element.

[getEdgeSize](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-getEdgeSize-static)
Returns an object with the parse style values for the top, right, bottom, and left components of the given edge style.

The return value is an object with `top`, `right`, `bottom`, and `left` properties for the respective components of the edge style, as well as `width` (the sum of `left` and `right`) and `height` (the sum of `top` and `bottom`).

[parseStyle](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-parseStyle-static)
Splits a style string up into object form. For example `'font-weight:bold;font-size:150%'` would convert to

```
{
    font-weight : 'bold',
    font-size : '150%'
}
```

[applyStyle](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-applyStyle-static)
Applies specified style to the passed element. Style can be an object or a string.

[assignClasses](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-assignClasses-static)
Adds or removes the `classes` contained in the specified object based on the truthy or falsy value of that key.

For example:

```
 DomHelper.assignClasses(element, {
     'b-class-one' : 1   // class will be added
     'b-class-two' : 0   // class will be removed
 });
```

[toggleClasses](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-toggleClasses-static)
Toggle multiple classes in elements classList. Helper for toggling multiple classes at once.

[addTemporaryClass](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-addTemporaryClass-static)
Adds a CSS class to an element during the specified duration

[getPropertyTransitionDuration](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-getPropertyTransitionDuration-static)
Reads computed style from the element and returns transition duration for a given property in milliseconds

[getAnimationDuration](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-getAnimationDuration-static)
Reads computed style from the element and returns the animation duration for any attached animation in milliseconds

[getAnimations](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-getAnimations-static)
Returns element animations

[highlight](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-highlight-static)
Highlights the passed element or Rectangle according to the theme's highlighting rules. Usually an animated framing effect.

The framing effect is achieved by adding the CSS class `b-fx-highlight` which references a `keyframes` animation named `b-fx-highlight-animation`. You may override the animation name referenced, or the animation itself in your own CSS.

[resetScrollBarWidth](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-resetScrollBarWidth-static)
Resets DomHelper.scrollBarWidth cache, triggering a new measurement next time it is read

[measureText](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-measureText-static)
Measures the text width using a hidden div

[measureSize](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-measureSize-static)
Measures a relative size, such as a size specified in `em` units for the passed element.

[stripTags](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-stripTags-static)
Strips the tags from a html string, returning text content.

```
DomHelper.stripTags('<div class="custom"><b>Bold</b><i>Italic</i></div>'); // -> BoldItalic
```

[sync](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-sync-static)
Sync one source element attributes, children etc. to a target element. Source element can be specified as a html string or an actual HTMLElement.

NOTE: This function is superseded by [DomSync.sync()](https://bryntum.com/docs/gantt/api/#Core/helper/DomSync#function-sync-static), which works with DOM configs. For most usecases, use it instead.

[syncAttributes](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-syncAttributes-static)
Syncs attributes from sourceElement to targetElement.

[syncContent](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-syncContent-static)
Sync content (innerText) from sourceElement to targetElement

[syncChildren](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-syncChildren-static)
Sync traversing children

[syncClassList](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-syncClassList-static)
Replaces the passed element's `className` with the class names passed in either Array or String format or Object.

This method compares the existing class set with the incoming class set and avoids mutating the element's class name set if possible.

This can avoid browser style invalidations.

[updateClassList](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-updateClassList-static)
Applies the key state of the passed object or DomClassList to the passed element.

Properties with a falsy value mean that property name is _removed_ as a class name.

Properties with a truthy value mean that property name is _added_ as a class name.

This is different from [syncClassList](https://bryntum.com/docs/gantt/api/#Core/helper/DomHelper#function-syncClassList-static). That sets the `className` of the element to the sum of all its truthy keys, regardless of what the pre-existing value of the `className` was, and ignoring falsy keys.

This _selectively_ updates the classes in the `className`. If there is a truthy key, the name is added. If there is a falsy key, the name is removed.

[setTheme](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-setTheme-static)
Changes the theme to the passed theme name if possible.

Theme names are case-insensitive. The `href` used is all lower case.

To use this method, the `<link rel="stylesheet">` _must_ use the default, Bryntum-supplied CSS files where the `href` end with `<themeName>.css`, so that it can be found in the document, and switched out for a new link with the modified `href`. The new `href` will use the same path, just with the `themeName` portion substituted for the new name.

If no `<link>` with that name pattern can be found, an error will be thrown.

If you use this method, you must ensure that the theme files are all accessible on your server.

Because this is an asynchronous operation, a `Promise` is returned. The theme change event is passed to the success function. If the theme was not changed, because the theme name passed is the current theme, nothing is passed to the success function.

The theme change event contains two properties:

* `prev` The previous Theme name.
* `theme` The new Theme name.

[toggleLightDarkTheme](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-toggleLightDarkTheme-static)
Toggles between light and dark themes. Does not check if the theme is actually available, only does a string replace on the current themes filename for light/dark.

[getThemeInfo](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#function-getThemeInfo-static)
Gets theme information about the currently active theme by reading CSS custom properties from the `.b-theme-info` class.

The method creates a temporary DOM element with the `b-theme-info` class, reads all CSS custom properties that start with `--b-theme-`, converts them to camelCase property names, and returns them as an object.

Example theme CSS:

```
.b-theme-info {
    --b-theme-name             : "SvalbardDark";
    --b-theme-filename         : "svalbard-dark";
    --b-theme-button-rendition : "text";
    --b-theme-label-position   : "align-before";
    --b-theme-overlap-label    : "false";
}
```

This would result in:

```
{
    name            : "SvalbardDark",
    filename        : "svalbard-dark",
    buttonRendition : "text",
    labelPosition   : "align-before",
    overlapLabel    : false  // String "true"/"false" values are converted to boolean
}
```

## Typedefs

Typedefs are type definitions for the class

[Focusability](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#typedef-Focusability)
An immutable object that describes the various aspects of an element's focus and keyboard navigation.

[ThemeInfo](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#typedef-ThemeInfo)
A theme information object about the current theme.

Theme information object containing metadata about the active theme. The theme information is read from CSS custom properties defined in the `.b-theme-info` class.

Example CSS:

```
.b-theme-info {
    --b-theme-name             : "SvalbardDark";
    --b-theme-filename         : "svalbard-dark";
    --b-theme-button-rendition : "text";
    --b-theme-label-position   : "align-before";
    --b-theme-overlap-label    : "false";
}
```

[DomConfig](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#typedef-DomConfig)
An object that describes a DOM element. Used for example by [createElement()](https://bryntum.com/docs/gantt/api/#Core/helper/DomHelper#function-createElement-static) and by [DomSync.sync()](https://bryntum.com/docs/gantt/api/#Core/helper/DomSync#function-sync-static).

```
DomHelper.createElement({
   class : {
       big   : true,
       small : false
   },
   children : [
       { tag : 'img', src : 'img.png' },
       { html : '<b style="color: red">Red text</b>' }
   ]
});
```

[VueConfig](https://bryntum.com/docs/gantt/api/Core/helper/DomHelper#typedef-VueConfig)
An object that describes a vue component configuration.

```
{
    vue  : true
    is   : 'VueWidget'
    bind : { prop1: 'value1', prop2: 'value2' }
    on   : { myclick: handleMyClick }
}
```
