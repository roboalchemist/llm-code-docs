# Source: https://www.electronjs.org/docs/latest/api/touch-bar-label

On this page

# Class: TouchBarLabel

## Class: TouchBarLabel[â€‹](#class-touchbarlabel "Direct link to Class: TouchBarLabel") 

> Create a label in the touch bar for native macOS applications

Process: [Main](/docs/latest/glossary#main-process)\
*This class is not exported from the `'electron'` module. It is only available as a return value of other methods in the Electron API.*

### `new TouchBarLabel(options)`[â€‹](#new-touchbarlabeloptions "Direct link to new-touchbarlabeloptions") 

- `options` Object
  - `label` string (optional) - Text to display.
  - `accessibilityLabel` string (optional) - A short description of the button for use by screenreaders like VoiceOver.
  - `textColor` string (optional) - Hex color of text, i.e `#ABCDEF`.

When defining `accessibilityLabel`, ensure you have considered macOS [best practices](https://developer.apple.com/documentation/appkit/nsaccessibilitybutton/1524910-accessibilitylabel?language=objc).

### Instance Properties[â€‹](#instance-properties "Direct link to Instance Properties") 

The following properties are available on instances of `TouchBarLabel`:

#### `touchBarLabel.label`[â€‹](#touchbarlabellabel "Direct link to touchbarlabellabel") 

A `string` representing the label\'s current text. Changing this value immediately updates the label in the touch bar.

#### `touchBarLabel.accessibilityLabel`[â€‹](#touchbarlabelaccessibilitylabel "Direct link to touchbarlabelaccessibilitylabel") 

A `string` representing the description of the label to be read by a screen reader.

#### `touchBarLabel.textColor`[â€‹](#touchbarlabeltextcolor "Direct link to touchbarlabeltextcolor") 

A `string` hex code representing the label\'s current text color. Changing this value immediately updates the label in the touch bar.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/touch-bar-label.md)