# Source: https://www.electronjs.org/docs/latest/api/touch-bar

On this page

# TouchBar

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)]warning

Electron\'s built-in classes cannot be subclassed in user code. For more information, see [the FAQ](/docs/latest/faq#class-inheritance-does-not-work-with-electron-built-in-modules).

## Class: TouchBar[â€‹](#class-touchbar "Direct link to Class: TouchBar") 

> Create TouchBar layouts for native macOS applications

Process: [Main](/docs/latest/glossary#main-process)

### `new TouchBar(options)`[â€‹](#new-touchbaroptions "Direct link to new-touchbaroptions") 

- `options` Object
  - `items` ([TouchBarButton](/docs/latest/api/touch-bar-button) \| [TouchBarColorPicker](/docs/latest/api/touch-bar-color-picker) \| [TouchBarGroup](/docs/latest/api/touch-bar-group) \| [TouchBarLabel](/docs/latest/api/touch-bar-label) \| [TouchBarPopover](/docs/latest/api/touch-bar-popover) \| [TouchBarScrubber](/docs/latest/api/touch-bar-scrubber) \| [TouchBarSegmentedControl](/docs/latest/api/touch-bar-segmented-control) \| [TouchBarSlider](/docs/latest/api/touch-bar-slider) \| [TouchBarSpacer](/docs/latest/api/touch-bar-spacer))\[\] (optional)
  - `escapeItem` ([TouchBarButton](/docs/latest/api/touch-bar-button) \| [TouchBarColorPicker](/docs/latest/api/touch-bar-color-picker) \| [TouchBarGroup](/docs/latest/api/touch-bar-group) \| [TouchBarLabel](/docs/latest/api/touch-bar-label) \| [TouchBarPopover](/docs/latest/api/touch-bar-popover) \| [TouchBarScrubber](/docs/latest/api/touch-bar-scrubber) \| [TouchBarSegmentedControl](/docs/latest/api/touch-bar-segmented-control) \| [TouchBarSlider](/docs/latest/api/touch-bar-slider) \| [TouchBarSpacer](/docs/latest/api/touch-bar-spacer) \| null) (optional)

Creates a new touch bar with the specified items. Use `BrowserWindow.setTouchBar` to add the `TouchBar` to a window.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

The TouchBar API is currently experimental and may change or be removed in future Electron releases.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6IiAvPjwvc3ZnPg==)]tip

If you don\'t have a MacBook with Touch Bar, you can use [Touch Bar Simulator](https://github.com/sindresorhus/touch-bar-simulator) to test Touch Bar usage in your app.

### Static Properties[â€‹](#static-properties "Direct link to Static Properties") 

#### `TouchBarButton`[â€‹](#touchbarbutton "Direct link to touchbarbutton") 

A [`typeof TouchBarButton`](/docs/latest/api/touch-bar-button) reference to the `TouchBarButton` class.

#### `TouchBarColorPicker`[â€‹](#touchbarcolorpicker "Direct link to touchbarcolorpicker") 

A [`typeof TouchBarColorPicker`](/docs/latest/api/touch-bar-color-picker) reference to the `TouchBarColorPicker` class.

#### `TouchBarGroup`[â€‹](#touchbargroup "Direct link to touchbargroup") 

A [`typeof TouchBarGroup`](/docs/latest/api/touch-bar-group) reference to the `TouchBarGroup` class.

#### `TouchBarLabel`[â€‹](#touchbarlabel "Direct link to touchbarlabel") 

A [`typeof TouchBarLabel`](/docs/latest/api/touch-bar-label) reference to the `TouchBarLabel` class.

#### `TouchBarPopover`[â€‹](#touchbarpopover "Direct link to touchbarpopover") 

A [`typeof TouchBarPopover`](/docs/latest/api/touch-bar-popover) reference to the `TouchBarPopover` class.

#### `TouchBarScrubber`[â€‹](#touchbarscrubber "Direct link to touchbarscrubber") 

A [`typeof TouchBarScrubber`](/docs/latest/api/touch-bar-scrubber) reference to the `TouchBarScrubber` class.

#### `TouchBarSegmentedControl`[â€‹](#touchbarsegmentedcontrol "Direct link to touchbarsegmentedcontrol") 

A [`typeof TouchBarSegmentedControl`](/docs/latest/api/touch-bar-segmented-control) reference to the `TouchBarSegmentedControl` class.

#### `TouchBarSlider`[â€‹](#touchbarslider "Direct link to touchbarslider") 

A [`typeof TouchBarSlider`](/docs/latest/api/touch-bar-slider) reference to the `TouchBarSlider` class.

#### `TouchBarSpacer`[â€‹](#touchbarspacer "Direct link to touchbarspacer") 

A [`typeof TouchBarSpacer`](/docs/latest/api/touch-bar-spacer) reference to the `TouchBarSpacer` class.

#### `TouchBarOtherItemsProxy`[â€‹](#touchbarotheritemsproxy "Direct link to touchbarotheritemsproxy") 

A [`typeof TouchBarOtherItemsProxy`](/docs/latest/api/touch-bar-other-items-proxy) reference to the `TouchBarOtherItemsProxy` class.

### Instance Properties[â€‹](#instance-properties "Direct link to Instance Properties") 

The following properties are available on instances of `TouchBar`:

#### `touchBar.escapeItem`[â€‹](#touchbarescapeitem "Direct link to touchbarescapeitem") 

A `TouchBarItem` that will replace the \"esc\" button on the touch bar when set. Setting to `null` restores the default \"esc\" button. Changing this value immediately updates the escape item in the touch bar.

## Examples[â€‹](#examples "Direct link to Examples") 

Below is an example of a simple slot machine touch bar game with a button and some labels.

``` 
const  = require('electron')

const  = TouchBar

let spinning = false

// Reel labels
const reel1 = new TouchBarLabel()
const reel2 = new TouchBarLabel()
const reel3 = new TouchBarLabel()

// Spin result label
const result = new TouchBarLabel()

// Spin button
const spin = new TouchBarButton(

    spinning = true
    result.label = ''

    let timeout = 10
    const spinLength = 4 * 1000 // 4 seconds
    const startTime = Date.now()

    const spinReels = () =>  else 
    }

    spinReels()
  }
})

const getRandomValue = () => 

const updateReels = () => 

const finishSpin = () =>  else if (uniqueValues === 2)  else 
  spinning = false
}

const touchBar = new TouchBar(),
    reel1,
    new TouchBarSpacer(),
    reel2,
    new TouchBarSpacer(),
    reel3,
    new TouchBarSpacer(),
    result
  ]
})

let window

app.whenReady().then(() => )
  window.loadURL('about:blank')
  window.setTouchBar(touchBar)
})
```

### Running the above example[â€‹](#running-the-above-example "Direct link to Running the above example") 

To run the example above, you\'ll need to (assuming you\'ve got a terminal open in the directory you want to run the example):

1.  Save the above file to your computer as `touchbar.js`
2.  Install Electron via `npm install electron`
3.  Run the example inside Electron: `./node_modules/.bin/electron touchbar.js`

You should then see a new Electron window and the app running in your touch bar (or touch bar emulator).

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/touch-bar.md)