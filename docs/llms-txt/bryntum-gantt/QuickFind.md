# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/QuickFind.md

# [QuickFind](https://bryntum.com/docs/gantt/api/Grid/feature/QuickFind)

Feature that allows the user to search in a column by focusing a cell and typing. Navigate between hits using the keyboard, \[f3\] or \[ctrl\]/\[cmd\] + \[g\] moves to next, also pressing \[shift\] moves to previous.

This feature is **disabled** by default.

Keyboard shortcuts
------------------

This feature has the following default keyboard shortcuts:

Keys

Action

Action description

`F3`

_goToNextHit_

Move focus to next search hit

`Shift`+F3\`

_goToPrevHit_

Move focus to previous search hit

`Ctrl`+`G`

_goToNextHit_

Move focus to next search hit

`Ctrl`+`Shift`+`G`

_goToPrevHit_

Move focus to previous search hit

`Ctrl`+`Shift`+`F3`

_showFilterEditor_

Shows the filter editor

`Escape`

_clearSearch_

Removes the search completely

Please note that `Ctrl` is the equivalent to `Command` and `Alt` is the equivalent to `Option` for Mac users

For more information on how to customize keyboard shortcuts, please see [our guide](https://bryntum.com/docs/gantt/api/#Grid/guides/customization/keymap.md)

```
// enable QuickFind
let grid = new Grid({
  features: {
    quickFind: true
  }
});

// navigate to next hit programmatically
grid.features.quickFind.gotoNextHit();
```

When Store has [lazyLoad](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-lazyLoad), this feature will only work on locally available data

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[keyMap](https://bryntum.com/docs/gantt/api/Grid/feature/QuickFind#config-keyMap)
See [Keyboard shortcuts](https://bryntum.com/docs/gantt/api/#Grid/feature/QuickFind#keyboard-shortcuts) for details

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isQuickFind](https://bryntum.com/docs/gantt/api/Grid/feature/QuickFind#property-isQuickFind)
Identifies an object as an instance of [QuickFind](https://bryntum.com/docs/gantt/api/#Grid/feature/QuickFind) class, or subclass thereof.

[isQuickFind](https://bryntum.com/docs/gantt/api/Grid/feature/QuickFind#property-isQuickFind-static)
Identifies an object as an instance of [QuickFind](https://bryntum.com/docs/gantt/api/#Grid/feature/QuickFind) class, or subclass thereof.

[foundCount](https://bryntum.com/docs/gantt/api/Grid/feature/QuickFind#property-foundCount)
Number of results found

[found](https://bryntum.com/docs/gantt/api/Grid/feature/QuickFind#property-found)
Found results (as returned by Store#findByField), an array in format { index: x, data: record }

## Functions

Functions are methods available for calling on the class

[showQuickFind](https://bryntum.com/docs/gantt/api/Grid/feature/QuickFind#function-showQuickFind)
Shows a "searchfield" in the header. Triggered automatically when you have a cell focused and start typing.

[hideQuickFind](https://bryntum.com/docs/gantt/api/Grid/feature/QuickFind#function-hideQuickFind)
Hide the "searchfield" and remove highlighted hits. Called automatically when pressing \[esc\] or backspacing away the keywords.

[search](https://bryntum.com/docs/gantt/api/Grid/feature/QuickFind#function-search)
Performs a search and highlights hits. If find is empty, QuickFind is closed.

[clear](https://bryntum.com/docs/gantt/api/Grid/feature/QuickFind#function-clear)
Clears and closes QuickFind.

[gotoHit](https://bryntum.com/docs/gantt/api/Grid/feature/QuickFind#function-gotoHit)
Go to specified hit.

[gotoFirstHit](https://bryntum.com/docs/gantt/api/Grid/feature/QuickFind#function-gotoFirstHit)
Go to the first hit.

[gotoLastHit](https://bryntum.com/docs/gantt/api/Grid/feature/QuickFind#function-gotoLastHit)
Go to the last hit.

[gotoNextHit](https://bryntum.com/docs/gantt/api/Grid/feature/QuickFind#function-gotoNextHit)
Select the next hit, scrolling it into view. Triggered with \[f3\] or \[ctrl\]/\[cmd\] + \[g\].

[gotoPrevHit](https://bryntum.com/docs/gantt/api/Grid/feature/QuickFind#function-gotoPrevHit)
Select the previous hit, scrolling it into view. Triggered with \[shift\] + \[f3\] or \[shift\] + \[ctrl\]/\[cmd\] + \[g\].

[renderCell](https://bryntum.com/docs/gantt/api/Grid/feature/QuickFind#function-renderCell)
Called from SubGrid when a cell is rendered.

[onElementKeyPress](https://bryntum.com/docs/gantt/api/Grid/feature/QuickFind#function-onElementKeyPress)
Chained function called on grids keypress event. Handles input for "searchfield".
