# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/Mask.md

# [Mask](https://bryntum.com/docs/gantt/api/Core/widget/Mask)

Masks a target element (`document.body` if none is specified). Call static methods for ease of use or make instance for reusability.

```
 Mask.mask('hello');
 Mask.unmask();
```

Can show progress:

```
 // Using progress by calling static method
 const mask = Mask.mask({
     text        :'The task is in progress',
     progress    : 0,
     maxProgress : 100
 });

 let timer = setInterval(() => {
     mask.progress += 5;
     if (mask.progress >= mask.maxProgress) {
         Mask.unmask();
         clearInterval(timer);
     }
 }, 100);
```

Stacking Multiple Masks
-----------------------

An element can have multiple masks attached to it (for example, to handle independent asynchronous activities). When an element has multiple masks attached, only the first mask created is visible to the user. This avoids unpleasant transparency layering that would occur if all masks were visible at the same time. When the active mask is destroyed or hidden (via [hide](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#function-hide)), the next oldest mask is made visible. That is, masks are displayed in FIFO order.

When a mask is hidden, it is not a candidate in the FIFO order and is ignored when looking for the next oldest mask. If the mask is shown (via [show](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#function-show)), the mask is again a candidate for being shown, and will be shown immediately if there is not already a currently visible mask. This eliminates flickering effects that would otherwise come from multiple masks competing for display.

When the last mask is hidden or destroyed, the target element becomes unmasked. Showing and hiding of masks is useful when the masks may be needed repeatedly over time.

Masking Bryntum Widgets
-----------------------

Shortcut to masking Bryntum components:

```
 // Using progress to mask a Bryntum component
 scheduler.mask({
     text:'Loading in progress',
     progress: 0,
     maxProgress: 100
 });

 let timer = setInterval(() => {
     scheduler.masked.progress += 5;
     if (scheduler.masked.progress >= scheduler.masked.maxProgress) {
         scheduler.unmask();
         clearInterval(timer);
     }
 },100);
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[autoClose](https://bryntum.com/docs/gantt/api/Core/widget/Mask#config-autoClose)
Set this config to trigger an automatic close after the desired delay:

```
 mask.autoClose = 2000;
```

If the mask has an `owner`, its `onMaskAutoClosing` method is called when the close starts and its `onMaskAutoClose` method is called when the close finishes.

[cover](https://bryntum.com/docs/gantt/api/Core/widget/Mask#config-cover)
The portion of the [target](https://bryntum.com/docs/gantt/api/#Core/widget/Mask#config-target) element to be covered by this mask. By default, the mask fully covers the `target`. In some cases, however, it may be desired to only cover the `'body'` (for example, in a grid).

This config is set in conjunction with `owner` which implements the method `syncMaskCover`.

[icon](https://bryntum.com/docs/gantt/api/Core/widget/Mask#config-icon)
The icon to show next to the text. Defaults to showing a spinner

[target](https://bryntum.com/docs/gantt/api/Core/widget/Mask#config-target)
The element to be masked. If this config is a string, that string is the name of the property of the [owner](https://bryntum.com/docs/gantt/api/#Core/widget/Mask#config-owner) that holds the `HTMLElement` that is the actual target of the mask.

NOTE: In prior releases, this used to be specified as the `element` config.

[text](https://bryntum.com/docs/gantt/api/Core/widget/Mask#config-text)
The text (or HTML) to show in the mask, the text is not HTML encoded. See also the [htmlEncode](https://bryntum.com/docs/gantt/api/#Core/widget/Mask#config-htmlEncode) config for displaying raw HTML. As of v8.0 the text is automatically HTML encoded.

[showDelay](https://bryntum.com/docs/gantt/api/Core/widget/Mask#config-showDelay)
The number of milliseconds to delay before making the mask visible. If set, the mask will have an initial `opacity` of 0 but will function in all other ways as a normal mask. Setting this delay can reduce flicker in cases where load operations are typically short (for example, a second or less).

[htmlEncode](https://bryntum.com/docs/gantt/api/Core/widget/Mask#config-htmlEncode)
By default in versions below 8.0, the [text](https://bryntum.com/docs/gantt/api/#Core/widget/Mask#config-text) is not HTML-encoded. Set this flag to `true` to automatically HTML-encode the text.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isMask](https://bryntum.com/docs/gantt/api/Core/widget/Mask#property-isMask)
Identifies an object as an instance of [Mask](https://bryntum.com/docs/gantt/api/#Core/widget/Mask) class, or subclass thereof.

[isMask](https://bryntum.com/docs/gantt/api/Core/widget/Mask#property-isMask-static)
Identifies an object as an instance of [Mask](https://bryntum.com/docs/gantt/api/#Core/widget/Mask) class, or subclass thereof.

[maxProgress](https://bryntum.com/docs/gantt/api/Core/widget/Mask#property-maxProgress)
The maximum value of the progress indicator

[progress](https://bryntum.com/docs/gantt/api/Core/widget/Mask#property-progress)
Number expressing the progress

[text](https://bryntum.com/docs/gantt/api/Core/widget/Mask#property-text)
The text (or HTML) to show in the mask, the text is not HTML encoded. See also the [htmlEncode](https://bryntum.com/docs/gantt/api/#Core/widget/Mask#config-htmlEncode) config for displaying raw HTML. As of v8.0 the text is automatically HTML encoded.

[htmlEncode](https://bryntum.com/docs/gantt/api/Core/widget/Mask#property-htmlEncode)
By default in versions below 8.0, the [text](https://bryntum.com/docs/gantt/api/#Core/widget/Mask#config-text) is not HTML-encoded. Set this flag to `true` to automatically HTML-encode the text.

## Functions

Functions are methods available for calling on the class

[get](https://bryntum.com/docs/gantt/api/Core/widget/Mask#function-get-static)
Returns the array of `Mask` instances for the given `element`.

[mask](https://bryntum.com/docs/gantt/api/Core/widget/Mask#function-mask-static)
Shows a mask with the specified message.

Masks stack, call [unmask](https://bryntum.com/docs/gantt/api/#Core/widget/Mask#function-unmask-static) to remove the topmost mask. Or call [close](https://bryntum.com/docs/gantt/api/#Core/widget/Mask#function-close) on the returned mask to close it specifically. Only one mask is displayed for a given `target` element at a time. For example, if two masks are added to an element, the first mask is displayed. If the first mask is closed, then the second mask will become visible.

[unmask](https://bryntum.com/docs/gantt/api/Core/widget/Mask#function-unmask-static)
Close the most recently created mask for the specified element.

[unmaskAll](https://bryntum.com/docs/gantt/api/Core/widget/Mask#function-unmaskAll-static)
Close all masks for the specified element

[close](https://bryntum.com/docs/gantt/api/Core/widget/Mask#function-close)
Close mask (removes it)
