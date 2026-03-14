# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/Toast.md

# [Toast](https://bryntum.com/docs/gantt/api/Core/widget/Toast)

Basic toast. Toasts are stacked on top of each other

```
// simplest possible
Toast.show('Just toasting');

// with config
Toast.show({
  html         : 'Well toasted',
  showProgress : false
});

// as instance (instance is also returned from Toast.show()
const toast = new Toast({
  html    : 'Not going away',
  timeout : 0
});

toast.show();
```

To show toasts from the top and have them stack downwards, specify `side` as `'top'`:

```
Toast.show({
  html : 'Well toasted',
  side : 'top'
});
```

By default, Toasts show at the `inline-end` side of the screen, so on the right in LTR environments and on the left in RTL environments.

Append `-start` to the side to display at the required edge, or just use `side : 'start'` to show at the bottom but at the `inline-start` side of the screen.

```
Toast.show({
  html : 'Well toasted on the left',
  side : 'start'
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[timeout](https://bryntum.com/docs/gantt/api/Core/widget/Toast#config-timeout)
Timeout (in ms) until the toast is automatically dismissed. Set to 0 to never hide.

[showProgress](https://bryntum.com/docs/gantt/api/Core/widget/Toast#config-showProgress)
Show a progress bar indicating the time remaining until the toast is dismissed.

[side](https://bryntum.com/docs/gantt/api/Core/widget/Toast#config-side)
Which side to show the toast at, `'top'` or `'bottom'`. Defaults to `'bottom'`.

May also define the inline edge to show at, by using `'top-start'`, or `'top-end'` etc.

By default, toasts are shown at the bottom at the inline-end edge.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isToast](https://bryntum.com/docs/gantt/api/Core/widget/Toast#property-isToast)
Identifies an object as an instance of [Toast](https://bryntum.com/docs/gantt/api/#Core/widget/Toast) class, or subclass thereof.

[isToast](https://bryntum.com/docs/gantt/api/Core/widget/Toast#property-isToast-static)
Identifies an object as an instance of [Toast](https://bryntum.com/docs/gantt/api/#Core/widget/Toast) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[show](https://bryntum.com/docs/gantt/api/Core/widget/Toast#function-show)
Show the toast

[hide](https://bryntum.com/docs/gantt/api/Core/widget/Toast#function-hide)
Hide the toast

[hideAll](https://bryntum.com/docs/gantt/api/Core/widget/Toast#function-hideAll-static)
Hide all visible toasts

[show](https://bryntum.com/docs/gantt/api/Core/widget/Toast#function-show-static)
Easiest way to show a toast

```
Toast.show('Hi');

Toast.show({
  html   : 'Read quickly, please',
  timeout: 1000
});
```
