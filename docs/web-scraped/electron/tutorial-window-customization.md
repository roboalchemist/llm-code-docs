# Source: https://www.electronjs.org/docs/latest/tutorial/window-customization

# Window Customization

TheÂ [`BrowserWindow`](/docs/latest/api/browser-window)Â module is the foundation of your Electron application, and it exposes many APIs that let you customize the look and behavior of your appâ€™s windows. This section covers how to implement various use cases for window customization on macOS, Windows, and Linux.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

`BrowserWindow` is a subclass of the [`BaseWindow`](/docs/latest/api/base-window) module. Both modules allow you to create and manage application windows in Electron, with the main difference being that `BrowserWindow` supports a single, full size web view while `BaseWindow` supports composing many web views. `BaseWindow` can be used interchangeably with `BrowserWindow` in the examples of the documents in this section.

[](/docs/latest/tutorial/custom-title-bar)

## ðŸ"„ï¸? Custom Title Bar 

Application windows have a default chrome applied by the OS. Not to be confused with the Google Chrome browser, windowÂ \_chrome_Â refers to the parts of the window (e.g. title bar, toolbars, controls) that are not a part of the main web content. While the default title bar provided by the OS chrome is sufficient for simple use cases, many applications opt to remove it. Implementing a custom title bar can help your application feel more modern and consistent across platforms.