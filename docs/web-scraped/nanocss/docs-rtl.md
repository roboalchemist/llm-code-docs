# nano-css Documentation
# Source: https://raw.githubusercontent.com/streamich/nano-css/master/docs/rtl.md
# Path: docs/rtl.md

# `rtl` Addon

Flips all your styles to support right-to-left styling.

Example:

```js
nano.put('.foo', {
    textAlign: 'left',
    marginLeft: '100px'
});
```

Result:

```css
.foo {
    text-align: right;
    margin-right: 100px;
}
```


## Installation

Simply install `rtl` addon.

Read more about the [Addon Installation](./Addons.md#addon-installation).
