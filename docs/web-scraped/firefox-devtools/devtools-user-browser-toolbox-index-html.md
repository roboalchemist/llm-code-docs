# Source: https://firefox-source-docs.mozilla.org/devtools-user/browser_toolbox/index.html

Title: Browser Toolbox — Firefox Source Docs documentation

URL Source: https://firefox-source-docs.mozilla.org/devtools-user/browser_toolbox/index.html

Markdown Content:
The Browser Toolbox enables you to debug add-ons and the browser’s own JavaScript code rather than just web pages like the normal [Toolbox](https://firefox-source-docs.mozilla.org/devtools-user/tools_toolbox/index.html). The Browser Toolbox’s context is the whole browser rather than justsingle page on a single tab.

Enabling the Browser Toolbox[](https://firefox-source-docs.mozilla.org/devtools-user/browser_toolbox/index.html#enabling-the-browser-toolbox "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

The Browser Toolbox is not enabled by default. To enable it you need to check the settings “Enable chrome and addon debugging” and “Enable remote debugging”.

To do this, open the Developer Tools [Settings](https://firefox-source-docs.mozilla.org/devtools-user/settings/index.html), go to the section [Advanced Settings](https://firefox-source-docs.mozilla.org/devtools-user/settings/index.html#settings-advanced-settings), and check the settings “Enable browser chrome and add-on debugging toolboxes” and “Enable remote debugging”.

![Image 1: Developer Tools Settings](https://firefox-source-docs.mozilla.org/_images/settings_for_browser_debugger.png)
Opening the Browser Toolbox[](https://firefox-source-docs.mozilla.org/devtools-user/browser_toolbox/index.html#opening-the-browser-toolbox "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Open the Browser Toolbox through the menu button ![Image 2: new fx menu](https://firefox-source-docs.mozilla.org/_images/2014-01-10-13-08-08-f52b8c.png) and the menu items “Developer” then “Browser Toolbox”.

You can also open it with the Ctrl + Alt + Shift + I key combination (Cmd + Opt + Shift + I on a Mac).

You will be presented with a dialog like this (it can be removed by setting the `devtools.debugger.prompt-connection` property to false):

![Image 3: ../../_images/browser-toolbox-warning.png](https://firefox-source-docs.mozilla.org/_images/browser-toolbox-warning.png)
Click OK, and the Browser Toolbox will open in its own window:

![Image 4: ../../_images/browser-toolbox.png](https://firefox-source-docs.mozilla.org/_images/browser-toolbox.png)
You’ll be able to inspect the browser’s chrome windows and see, and be able to debug, all the JavaScript files loaded by the browser itself and by any add-ons that are running. Altogether you will have access to the following developer tools:

*   [Debugger](https://firefox-source-docs.mozilla.org/devtools-user/debugger/index.html)

*   [Console](https://firefox-source-docs.mozilla.org/devtools-user/browser_console/index.html)

*   [Style Editor](https://firefox-source-docs.mozilla.org/devtools-user/style_editor/index.html)

*   [Performance](https://firefox-source-docs.mozilla.org/devtools-user/performance/index.html)

*   [Network Monitor](https://firefox-source-docs.mozilla.org/devtools-user/network_monitor/index.html)

*   [Page Inspector](https://firefox-source-docs.mozilla.org/devtools-user/page_inspector/index.html)

*   [Accessibility Inspector](https://firefox-source-docs.mozilla.org/devtools-user/accessibility_inspector/index.html)

You can debug chrome: and about: pages using the normal [Debugger](https://firefox-source-docs.mozilla.org/devtools-user/debugger/index.html), just as if they were ordinary content pages.

Targeting a document[](https://firefox-source-docs.mozilla.org/devtools-user/browser_toolbox/index.html#targeting-a-document "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------

In the normal toolbox, there’s a [button in the toolbar enabling you to target specific iframes in the document](https://firefox-source-docs.mozilla.org/devtools-user/working_with_iframes/index.html). The same button appears in the browser toolbox where it lists all the top-level chrome and content windows as well as any iframes they contain. This enables you to inspect documents in individual chrome windows and popups, as well as in content tabs.

For example, here’s what the frame selection popup lists when there are two browser windows open, one with one content tab, and one with two:

![Image 5: ../../_images/browser-toolbox-iframes.png](https://firefox-source-docs.mozilla.org/_images/browser-toolbox-iframes.png)
