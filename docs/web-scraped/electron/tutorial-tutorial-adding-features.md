# Source: https://www.electronjs.org/docs/latest/tutorial/tutorial-adding-features

On this page

# Adding Features

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiIgLz48L3N2Zz4=)]Follow along the tutorial

This is **part 4** of the Electron tutorial.

1.  [Prerequisites](/docs/latest/tutorial/tutorial-prerequisites)
2.  [Building your First App](/docs/latest/tutorial/tutorial-first-app)
3.  [Using Preload Scripts](/docs/latest/tutorial/tutorial-preload)
4.  **[Adding Features](/docs/latest/tutorial/tutorial-adding-features)**
5.  [Packaging Your Application](/docs/latest/tutorial/tutorial-packaging)
6.  [Publishing and Updating](/docs/latest/tutorial/tutorial-publishing-updating)

## Adding application complexity[â€‹](#adding-application-complexity "Direct link to Adding application complexity") 

If you have been following along, you should have a functional Electron application with a static user interface. From this starting point, you can generally progress in developing your app in two broad directions:

1.  Adding complexity to your renderer process\' web app code
2.  Deeper integrations with the operating system and Node.js

It is important to understand the distinction between these two broad concepts. For the first point, Electron-specific resources are not necessary. Building a pretty to-do list in Electron is just pointing your Electron BrowserWindow to a pretty to-do list web app. Ultimately, you are building your renderer\'s UI using the same tools (HTML, CSS, JavaScript) that you would on the web. Therefore, Electron\'s docs will not go in-depth on how to use standard web tools.

On the other hand, Electron also provides a rich set of tools that allow you to integrate with the desktop environment, from creating tray icons to adding global shortcuts to displaying native menus. It also gives you all the power of a Node.js environment in the main process. This set of capabilities separates Electron applications from running a website in a browser tab, and are the focus of Electron\'s documentation.

## How-to examples[â€‹](#how-to-examples "Direct link to How-to examples") 

Electron\'s documentation has many tutorials to help you with more advanced topics and deeper operating system integrations. To get started, check out the [How-To Examples](/docs/latest/tutorial/examples) doc.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]Let us know if something is missing!

If you can\'t find what you are looking for, please let us know on [GitHub](https://github.com/electron/website/issues/new) or in our [Discord server](https://discord.gg/electronjs)!

## What\'s next?[â€‹](#whats-next "Direct link to What's next?") 

For the rest of the tutorial, we will be shifting away from application code and giving you a look at how you can get your app from your developer machine into end users\' hands.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/tutorial/tutorial-4-adding-features.md)