# Source: https://www.electronjs.org/docs/latest/api/touch-bar-popover

On this page

# Class: TouchBarPopover

## Class: TouchBarPopover[â€‹](#class-touchbarpopover "Direct link to Class: TouchBarPopover") 

> Create a popover in the touch bar for native macOS applications

Process: [Main](/docs/latest/glossary#main-process)\
*This class is not exported from the `'electron'` module. It is only available as a return value of other methods in the Electron API.*

### `new TouchBarPopover(options)`[â€‹](#new-touchbarpopoveroptions "Direct link to new-touchbarpopoveroptions") 

- `options` Object
  - `label` string (optional) - Popover button text.
  - `icon` [NativeImage](/docs/latest/api/native-image) (optional) - Popover button icon.
  - `items` [TouchBar](/docs/latest/api/touch-bar) - Items to display in the popover.
  - `showCloseButton` boolean (optional) - `true` to display a close button on the left of the popover, `false` to not show it. Default is `true`.

### Instance Properties[â€‹](#instance-properties "Direct link to Instance Properties") 

The following properties are available on instances of `TouchBarPopover`:

#### `touchBarPopover.label`[â€‹](#touchbarpopoverlabel "Direct link to touchbarpopoverlabel") 

A `string` representing the popover\'s current button text. Changing this value immediately updates the popover in the touch bar.

#### `touchBarPopover.icon`[â€‹](#touchbarpopovericon "Direct link to touchbarpopovericon") 

A `NativeImage` representing the popover\'s current button icon. Changing this value immediately updates the popover in the touch bar.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/touch-bar-popover.md)