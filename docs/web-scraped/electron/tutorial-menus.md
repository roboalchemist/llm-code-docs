# Source: https://www.electronjs.org/docs/latest/tutorial/menus

On this page

# Menus

Electron\'s [Menu](/docs/latest/api/menu) class provides a standardized way to create cross-platform native menus throughout your application.

## Available menus in Electron[â€‹](#available-menus-in-electron "Direct link to Available menus in Electron") 

The same menu API is used for multiple use cases:

- The **application menu** is the top-level menu for your application. Each app only has a single application menu at a time.
- **Context menus** are triggered by the user when right-clicking on a portion of your app\'s interface.
- The **tray menu** is a special context menu triggered when right-clicking on your app\'s [Tray](/docs/latest/api/tray) instance.
- On macOS, the **dock menu** is a special context menu triggered when right-clicking on your app\'s icon in the system [Dock](https://support.apple.com/en-ca/guide/mac-help/mh35859/mac).

To learn more about the various kinds of native menus you can create and how to specify keyboard shortcuts, see the individual guides in this section:

[](/docs/latest/tutorial/application-menu)

## ðŸ"„ï¸? Application Menu 

Customize the main application menu for your Electron app