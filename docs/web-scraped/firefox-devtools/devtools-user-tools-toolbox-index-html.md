# Source: https://firefox-source-docs.mozilla.org/devtools-user/tools_toolbox/index.html

Title: Toolbox — Firefox Source Docs documentation

URL Source: https://firefox-source-docs.mozilla.org/devtools-user/tools_toolbox/index.html

Markdown Content:
The Toolbox provides a single home for most of the developer tools that are built into Firefox.

There are three main ways to open the Toolbox:

*   Right-click a mouse on any element in the page, and select **Inspect** from the popup menu.

*   Open the Hamburger menu [![Image 1: image1](https://firefox-source-docs.mozilla.org/_images/hamburger2.png)](https://firefox-source-docs.mozilla.org/_images/hamburger2.png) and select **More tools > Web Developer Tools**.

*   Press Ctrl + Shift + I on Windows and Linux, or Cmd + Opt + I on OS X. See also [keyboard shortcuts](https://firefox-source-docs.mozilla.org/devtools-user/keyboard_shortcuts/index.html).

By default, the window appears docked to the bottom side of the Firefox window, but you can detach it if you like. This is what it looks like when it’s docked:

![Image 2: ../../_images/toolbox.png](https://firefox-source-docs.mozilla.org/_images/toolbox.png)
The window itself is split into two parts: a toolbar along the top, and a main pane underneath:

![Image 3: ../../_images/toolbox-labelled.png](https://firefox-source-docs.mozilla.org/_images/toolbox-labelled.png)

Note

You can drag and drop tabs in the main toolbar of the toolbox to reorder your tools as you wish.

Docking mode[](https://firefox-source-docs.mozilla.org/devtools-user/tools_toolbox/index.html#docking-mode "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------

By default, the Toolbox appears docked to the bottom of the browser window, but you can also dock it to the right-hand side of the window, or make it a standalone window, using [buttons in toolbar](https://firefox-source-docs.mozilla.org/devtools-user/tools_toolbox/index.html#tools-toolbox-toolbox-controls).

![Image 4: ../../_images/docking-mode.png](https://firefox-source-docs.mozilla.org/_images/docking-mode.png)
Toolbar[](https://firefox-source-docs.mozilla.org/devtools-user/tools_toolbox/index.html#toolbar "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------

The toolbar contains controls to activate a particular tool, to dock/float the window, and to close the window.

![Image 5: ../../_images/toolbox-toolbar-labelled.png](https://firefox-source-docs.mozilla.org/_images/toolbox-toolbar-labelled.png)
Node picker[](https://firefox-source-docs.mozilla.org/devtools-user/tools_toolbox/index.html#node-picker "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------

On the far left there’s a button to activate the node picker. This lets you select a page element for inspection. See Selecting elements

Toolbox-hosted tools[](https://firefox-source-docs.mozilla.org/devtools-user/tools_toolbox/index.html#toolbox-hosted-tools "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------

Then there is an array of labeled buttons which enables you to switch between the different tools hosted by the Toolbox. The array may include the following tools:

*   [Page Inspector](https://firefox-source-docs.mozilla.org/devtools-user/page_inspector/index.html)

*   [Web Console](https://firefox-source-docs.mozilla.org/devtools-user/web_console/index.html)

*   [JavaScript Debugger](https://firefox-source-docs.mozilla.org/devtools-user/debugger/index.html)

*   [Network Monitor](https://firefox-source-docs.mozilla.org/devtools-user/network_monitor/index.html)

*   [Style Editor](https://firefox-source-docs.mozilla.org/devtools-user/style_editor/index.html)

*   [Performance](https://firefox-source-docs.mozilla.org/devtools-user/performance/index.html)

*   [Memory Tool](https://firefox-source-docs.mozilla.org/devtools-user/memory/index.html)

*   [Storage Inspector](https://firefox-source-docs.mozilla.org/devtools-user/storage_inspector/index.html)

*   [Accessibility Inspector](https://firefox-source-docs.mozilla.org/devtools-user/accessibility_inspector/index.html)

*   [Application Tool](https://firefox-source-docs.mozilla.org/devtools-user/application/index.html)

*   [DOM Property Viewer](https://firefox-source-docs.mozilla.org/devtools-user/dom_property_viewer/index.html)

Note that not all the hosted tools are always listed here: only the tools actually available in this context are shown (for example, not all tools support remote debugging yet, so if the debugging target is not the Firefox instance that launched the window, not all the hosted tools will be shown).

Toolbox controls[](https://firefox-source-docs.mozilla.org/devtools-user/tools_toolbox/index.html#toolbox-controls "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------

Finally there’s a row of buttons to:

*   close the window

*   [Responsive Design Mode](https://firefox-source-docs.mozilla.org/devtools-user/responsive_design_mode/index.html)

There’s also a meatball menu button that consists of following options:

*   A group of options to toggle the toolbox to be docked bottom, right, left or even be a separate window by itself.

*   access [developer tool settings](https://firefox-source-docs.mozilla.org/devtools-user/settings/index.html)

*   [Toggle split console](https://firefox-source-docs.mozilla.org/devtools-user/web_console/split_console/index.html)

*   two buttons leading to documentation and community

Settings[](https://firefox-source-docs.mozilla.org/devtools-user/tools_toolbox/index.html#settings "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------

[See the separate page on the Developer Tools Settings](https://firefox-source-docs.mozilla.org/devtools-user/settings/index.html)

Main Pane[](https://firefox-source-docs.mozilla.org/devtools-user/tools_toolbox/index.html#main-pane "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------

The content of the main pane in the window is entirely controlled by, and specific to, the hosted tool currently selected.

[Toolbox shortcuts](https://firefox-source-docs.mozilla.org/devtools-user/keyboard_shortcuts/index.html#keyboard-shortcuts-toolbox) lists the shortcuts that work whenever the toolbox is open, no matter which tool is active. This same page also lists tool-specific keyboard shortcuts.
