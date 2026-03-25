# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/Search.md

# [Search](https://bryntum.com/docs/gantt/api/Grid/feature/Search)

Feature that allows the user to search the entire grid. Navigate between hits using the keyboard, \[F3\] or \[Ctrl/CMD + G\] moves to next, also pressing \[Shift\] moves to previous.

Note that this feature does not include a UI, please build your own and call appropriate methods in the feature. For a demo implementation, see [Search example](https://bryntum.com/docs/gantt/api/../examples/search/).

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

`Shift`+`F3`

_goToPrevHit_

Move focus to previous search hit

`Ctrl`+`G`

_goToNextHit_

Move focus to next search hit

`Ctrl`+`Shift`+`G`

_goToPrevHit_

Move focus to previous search hit

Please note that `Ctrl` is the equivalent to `Command` and `Alt` is the equivalent to `Option` for Mac users

For more information on how to customize keyboard shortcuts, please see [our guide](https://bryntum.com/docs/gantt/api/#Grid/guides/customization/keymap.md)

```
// enable Search
let grid = new Grid({
  features : {
    search : true
  }
});

// perform search
grid.features.search.search('steve');
```

When Store has [lazyLoad](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-lazyLoad), this feature will only work on locally available data

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[limit](https://bryntum.com/docs/gantt/api/Grid/feature/Search#config-limit)
The maximum amount of search hits

[showHitIndex](https://bryntum.com/docs/gantt/api/Grid/feature/Search#config-showHitIndex)
Set to `false` to not show the search hit index numbers

[keyMap](https://bryntum.com/docs/gantt/api/Grid/feature/Search#config-keyMap)
See [Keyboard shortcuts](https://bryntum.com/docs/gantt/api/#Grid/feature/Search#keyboard-shortcuts) for details

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isSearch](https://bryntum.com/docs/gantt/api/Grid/feature/Search#property-isSearch)
Identifies an object as an instance of [Search](https://bryntum.com/docs/gantt/api/#Grid/feature/Search) class, or subclass thereof.

[isSearch](https://bryntum.com/docs/gantt/api/Grid/feature/Search#property-isSearch-static)
Identifies an object as an instance of [Search](https://bryntum.com/docs/gantt/api/#Grid/feature/Search) class, or subclass thereof.

[foundCount](https://bryntum.com/docs/gantt/api/Grid/feature/Search#property-foundCount)
Number of results found

[isHitFocused](https://bryntum.com/docs/gantt/api/Grid/feature/Search#property-isHitFocused)
Returns true if focused row is a hit

## Functions

Functions are methods available for calling on the class

[search](https://bryntum.com/docs/gantt/api/Grid/feature/Search#function-search)
Performs a search and highlights hits.

[clear](https://bryntum.com/docs/gantt/api/Grid/feature/Search#function-clear)
Clears search results.

[gotoNextHit](https://bryntum.com/docs/gantt/api/Grid/feature/Search#function-gotoNextHit)
Select the next hit, scrolling it into view. Triggered with \[f3\] or \[ctrl\]/\[cmd\] + \[g\].

[gotoPrevHit](https://bryntum.com/docs/gantt/api/Grid/feature/Search#function-gotoPrevHit)
Select the previous hit, scrolling it into view. Triggered with \[shift\] + \[f3\] or \[shift\] + \[ctrl\]/\[cmd\] + \[g\].

[gotoHit](https://bryntum.com/docs/gantt/api/Grid/feature/Search#function-gotoHit)
Go to specified hit.

[gotoFirstHit](https://bryntum.com/docs/gantt/api/Grid/feature/Search#function-gotoFirstHit)
Go to the first hit.

[gotoLastHit](https://bryntum.com/docs/gantt/api/Grid/feature/Search#function-gotoLastHit)
Go to the last hit.

[renderCell](https://bryntum.com/docs/gantt/api/Grid/feature/Search#function-renderCell)
Called from SubGrid when a cell is rendered. Highlights search hits.

[populateCellMenu](https://bryntum.com/docs/gantt/api/Grid/feature/Search#function-populateCellMenu)
Add search menu item to cell context menu.
