# Source: https://www.electronjs.org/docs/latest/api/touch-bar-spacer

On this page

# Class: TouchBarSpacer

## Class: TouchBarSpacer[â€‹](#class-touchbarspacer "Direct link to Class: TouchBarSpacer") 

> Create a spacer between two items in the touch bar for native macOS applications

Process: [Main](/docs/latest/glossary#main-process)\
*This class is not exported from the `'electron'` module. It is only available as a return value of other methods in the Electron API.*

### `new TouchBarSpacer(options)`[â€‹](#new-touchbarspaceroptions "Direct link to new-touchbarspaceroptions") 

- `options` Object
  - `size` string (optional) - Size of spacer, possible values are:
    - `small` - Small space between items. Maps to `NSTouchBarItemIdentifierFixedSpaceSmall`. This is the default.
    - `large` - Large space between items. Maps to `NSTouchBarItemIdentifierFixedSpaceLarge`.
    - `flexible` - Take up all available space. Maps to `NSTouchBarItemIdentifierFlexibleSpace`.

### Instance Properties[â€‹](#instance-properties "Direct link to Instance Properties") 

The following properties are available on instances of `TouchBarSpacer`:

#### `touchBarSpacer.size`[â€‹](#touchbarspacersize "Direct link to touchbarspacersize") 

A `string` representing the size of the spacer. Can be `small`, `large` or `flexible`.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/touch-bar-spacer.md)