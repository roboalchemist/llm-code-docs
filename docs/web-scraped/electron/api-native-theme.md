# Source: https://www.electronjs.org/docs/latest/api/native-theme

On this page

# nativeTheme

> Read and respond to changes in Chromium\'s native color theme.

Process: [Main](/docs/latest/glossary#main-process)

## Events[â€‹](#events "Direct link to Events") 

The `nativeTheme` module emits the following events:

### Event: \'updated\'[â€‹](#event-updated "Direct link to Event: 'updated'") 

Emitted when something in the underlying NativeTheme has changed. This normally means that either the value of `shouldUseDarkColors`, `shouldUseHighContrastColors` or `shouldUseInvertedColorScheme` has changed. You will have to check them to determine which one has changed.

## Properties[â€‹](#properties "Direct link to Properties") 

The `nativeTheme` module has the following properties:

### `nativeTheme.shouldUseDarkColors` *Readonly*[â€‹](#nativethemeshouldusedarkcolors-readonly "Direct link to nativethemeshouldusedarkcolors-readonly") 

A `boolean` for if the OS / Chromium currently has a dark mode enabled or is being instructed to show a dark-style UI. If you want to modify this value you should use `themeSource` below.

### `nativeTheme.themeSource`[â€‹](#nativethemethemesource "Direct link to nativethemethemesource") 

A `string` property that can be `system`, `light` or `dark`. It is used to override and supersede the value that Chromium has chosen to use internally.

Setting this property to `system` will remove the override and everything will be reset to the OS default. By default `themeSource` is `system`.

Settings this property to `dark` will have the following effects:

- `nativeTheme.shouldUseDarkColors` will be `true` when accessed
- Any UI Electron renders on Linux and Windows including context menus, devtools, etc. will use the dark UI.
- Any UI the OS renders on macOS including menus, window frames, etc. will use the dark UI.
- The [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) CSS query will match `dark` mode.
- The `updated` event will be emitted

Settings this property to `light` will have the following effects:

- `nativeTheme.shouldUseDarkColors` will be `false` when accessed
- Any UI Electron renders on Linux and Windows including context menus, devtools, etc. will use the light UI.
- Any UI the OS renders on macOS including menus, window frames, etc. will use the light UI.
- The [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) CSS query will match `light` mode.
- The `updated` event will be emitted

The usage of this property should align with a classic \"dark mode\" state machine in your application where the user has three options.

- `Follow OS` \--\> `themeSource = 'system'`
- `Dark Mode` \--\> `themeSource = 'dark'`
- `Light Mode` \--\> `themeSource = 'light'`

Your application should then always use `shouldUseDarkColors` to determine what CSS to apply.

### `nativeTheme.shouldUseHighContrastColors` *macOS* *Windows* *Readonly*[â€‹](#nativethemeshouldusehighcontrastcolors-macos-windows-readonly "Direct link to nativethemeshouldusehighcontrastcolors-macos-windows-readonly") 

A `boolean` for if the OS / Chromium currently has high-contrast mode enabled or is being instructed to show a high-contrast UI.

### `nativeTheme.shouldUseDarkColorsForSystemIntegratedUI` *macOS* *Windows* *Readonly*[â€‹](#nativethemeshouldusedarkcolorsforsystemintegratedui-macos-windows-readonly "Direct link to nativethemeshouldusedarkcolorsforsystemintegratedui-macos-windows-readonly") 

A `boolean` property indicating whether or not the system theme has been set to dark or light.

On Windows this property distinguishes between system and app light/dark theme, returning `true` if the system theme is set to dark theme and `false` otherwise. On macOS the return value will be the same as `nativeTheme.shouldUseDarkColors`.

### `nativeTheme.shouldUseInvertedColorScheme` *macOS* *Windows* *Readonly*[â€‹](#nativethemeshoulduseinvertedcolorscheme-macos-windows-readonly "Direct link to nativethemeshoulduseinvertedcolorscheme-macos-windows-readonly") 

A `boolean` for if the OS / Chromium currently has an inverted color scheme or is being instructed to use an inverted color scheme.

### `nativeTheme.inForcedColorsMode` *Windows* *Readonly*[â€‹](#nativethemeinforcedcolorsmode-windows-readonly "Direct link to nativethemeinforcedcolorsmode-windows-readonly") 

A `boolean` indicating whether Chromium is in forced colors mode, controlled by system accessibility settings. Currently, Windows high contrast is the only system setting that triggers forced colors mode.

### `nativeTheme.prefersReducedTransparency` *Readonly*[â€‹](#nativethemeprefersreducedtransparency-readonly "Direct link to nativethemeprefersreducedtransparency-readonly") 

A `boolean` that indicates the whether the user has chosen via system accessibility settings to reduce transparency at the OS level.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/native-theme.md)