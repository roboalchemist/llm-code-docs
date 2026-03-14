# Source: https://firefox-source-docs.mozilla.org/devtools-user/

Title: Firefox DevTools User Docs — Firefox Source Docs documentation

URL Source: https://firefox-source-docs.mozilla.org/devtools-user/

Markdown Content:
Firefox Developer Tools is a set of web developer tools built into Firefox. You can use them to examine, edit, and debug HTML, CSS, and JavaScript.

This section contains detailed guides to all of the tools as well as information on how to debug Firefox for Android, how to extend DevTools, and how to debug the browser as a whole.

If you have any feedback on DevTools or want to contribute to the project, you can [join the DevTools community](https://firefox-dev.tools/).

The Core Tools[](https://firefox-source-docs.mozilla.org/devtools-user/#the-core-tools "Link to this heading")
---------------------------------------------------------------------------------------------------------------

You can open the Firefox Developer Tools from the menu by selecting **Tools > Web Developer > Web Developer Tools** or use the keyboard shortcut Ctrl + Shift + I or F12 on Windows and Linux, or Cmd + Opt + I on macOS.

The ellipsis menu on the right-hand side of Developer Tools contains several commands that let you perform actions or change tool settings.

![Image 1: ../_images/devtools_layoutmenu.png](https://firefox-source-docs.mozilla.org/_images/devtools_layoutmenu.png)

![Image 2: image1](https://firefox-source-docs.mozilla.org/_images/iframe_button.png)This button only appears when there are multiple iframes on a page. Click it to display a list of the iframes on the current page and select the one with which you want to work.
![Image 3: image2](https://firefox-source-docs.mozilla.org/_images/camera_button.png)Click this button to take a screenshot of the current page. (_Note:_ This feature is not turned on by default and must be enabled in settings before the icon will appear.)
![Image 4: image3](https://firefox-source-docs.mozilla.org/_images/responsive_button.png)Toggles Responsive Design Mode
![Image 5: image4](https://firefox-source-docs.mozilla.org/_images/menu_button.png)Opens the menu that includes docking options, the ability to show or hide the split console, and Developer Tools settings. The menu also includes links to the documentation for Firefox Web Tools and the Mozilla Community.
![Image 6: image5](https://firefox-source-docs.mozilla.org/_images/close_button.png)Closes the Developer Tools

### [Page Inspector](https://firefox-source-docs.mozilla.org/devtools-user/page_inspector)[](https://firefox-source-docs.mozilla.org/devtools-user/#page-inspector "Link to this heading")

[![Image 7: The all-new Inspector panel in Firefox 57.](https://firefox-source-docs.mozilla.org/_images/landingpage_pageinspector.png)](https://firefox-source-docs.mozilla.org/devtools-user/page_inspector)
View and edit page content and layout. Visualize many aspects of the page including the box model, animations, and grid layouts

### [Web Console](https://firefox-source-docs.mozilla.org/devtools-user/web_console)[](https://firefox-source-docs.mozilla.org/devtools-user/#web-console "Link to this heading")

[![Image 8: The all-new Console panel in Firefox 57.](https://firefox-source-docs.mozilla.org/_images/landingpage_console.png)](https://firefox-source-docs.mozilla.org/devtools-user/web_console)
See messages logged by a web page and interact with the page using JavaScript.

### [JavaScript Debugger](https://firefox-source-docs.mozilla.org/devtools-user/debugger)[](https://firefox-source-docs.mozilla.org/devtools-user/#javascript-debugger "Link to this heading")

[![Image 9: The all-new Debugger panel in Firefox 57.](https://firefox-source-docs.mozilla.org/_images/landingpage_debugger.png)](https://firefox-source-docs.mozilla.org/devtools-user/debugger)
Stop, step through, and examine the JavaScript running on a page.

### [Network Monitor](https://firefox-source-docs.mozilla.org/devtools-user/network_monitor)[](https://firefox-source-docs.mozilla.org/devtools-user/#network-monitor "Link to this heading")

[![Image 10: The Network panel in Firefox 57 DevTools.](https://firefox-source-docs.mozilla.org/_images/landingpage_network.png)](https://firefox-source-docs.mozilla.org/devtools-user/network_monitor)
See the network requests made when a page is loaded.

### [Performance Panel](https://profiler.firefox.com/docs/)[](https://firefox-source-docs.mozilla.org/devtools-user/#performance-panel "Link to this heading")

[![Image 11: Performance Panel in Firefox 103 Developer Tools.](https://firefox-source-docs.mozilla.org/_images/landingpage_performance_2022.png)](https://profiler.firefox.com/docs/)
Analyze your site’s general responsiveness, JavaScript, and layout performance.

### [Responsive Design Mode](https://firefox-source-docs.mozilla.org/devtools-user/responsive_design_mode)[](https://firefox-source-docs.mozilla.org/devtools-user/#responsive-design-mode "Link to this heading")

[![Image 12: Responsive Design mode in Firefox 57 Developer Tools.](https://firefox-source-docs.mozilla.org/_images/landingpage_responsivedesign.png)](https://firefox-source-docs.mozilla.org/devtools-user/responsive_design_mode)
See how your website or app will look and behave on different devices and network types.

### [Accessibility inspector](https://firefox-source-docs.mozilla.org/devtools-user/accessibility_inspector)[](https://firefox-source-docs.mozilla.org/devtools-user/#accessibility-inspector "Link to this heading")

[![Image 13: Performance Tools in Firefox 57 Developer Tools.](https://firefox-source-docs.mozilla.org/_images/landingpage_accessibility.png)](https://firefox-source-docs.mozilla.org/devtools-user/accessibility_inspector)
Provides a means to access the page’s accessibility tree, allowing you to check what’s missing or otherwise needs attention.

### [Application panel](https://firefox-source-docs.mozilla.org/devtools-user/application)[](https://firefox-source-docs.mozilla.org/devtools-user/#application-panel "Link to this heading")

[![Image 14: Performance Tools in Firefox 57 Developer Tools.](https://firefox-source-docs.mozilla.org/_images/just-application-panel.png)](https://firefox-source-docs.mozilla.org/devtools-user/application)
Provides tools for inspecting and debugging modern web apps (also known as [Progressive Web Apps](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps)). This includes inspection of [service workers](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API) and [web app manifests](https://developer.mozilla.org/en-US/docs/Web/Manifest)

Note

The collective term for the UI inside which the DevTools all live is the [Toolbox](https://firefox-source-docs.mozilla.org/devtools-user/tools_toolbox/index.html)

More Tools[](https://firefox-source-docs.mozilla.org/devtools-user/#more-tools "Link to this heading")
-------------------------------------------------------------------------------------------------------

These developer tools are also built into Firefox. Unlike the “Core Tools” above, you might not use them every day.

[Memory](https://firefox-source-docs.mozilla.org/devtools-user/memory/index.html)Figure out which objects are keeping memory in use.
[Storage Inspector](https://firefox-source-docs.mozilla.org/devtools-user/storage_inspector/index.html)Inspect cookies, local storage, indexedDB, and session storage present in a page.
[DOM Property Viewer](https://firefox-source-docs.mozilla.org/devtools-user/dom_property_viewer/index.html)Inspect the page’s DOM properties, functions, etc.
[Eyedropper](https://firefox-source-docs.mozilla.org/devtools-user/eyedropper/index.html)Select a color from the page.
[Style Editor](https://firefox-source-docs.mozilla.org/devtools-user/style_editor/index.html)View and edit CSS styles for the current page.
[Taking screenshot](https://firefox-source-docs.mozilla.org/devtools-user/taking_screenshots/index.html)Take a screenshot of the entire page or of a single element.
[Measure a portion of the page](https://firefox-source-docs.mozilla.org/devtools-user/measure_a_portion_of_the_page/index.html)Measure a specific area of a web page.
[Rulers](https://firefox-source-docs.mozilla.org/devtools-user/rulers/index.html)Overlay horizontal and vertical rulers on a web page
[Custom formatters](https://firefox-source-docs.mozilla.org/devtools-user/custom_formatters/index.html)Customize the way objects are displayed within the DevTools.
[JavaScript tracer](https://firefox-source-docs.mozilla.org/devtools-user/javascript_tracer/index.html)Live display all JavaScript function calls.

![Image 15: ../_images/logo-developer-quantum.png](https://firefox-source-docs.mozilla.org/_images/logo-developer-quantum.png)
For the latest developer tools and features, try Firefox Developer Edition.

[Download Firefox Developer Edition](https://www.mozilla.org/en-US/firefox/developer/)

Connecting the Developer Tools[](https://firefox-source-docs.mozilla.org/devtools-user/#connecting-the-developer-tools "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------

If you open the developer tools using [keyboard shortcuts](https://firefox-source-docs.mozilla.org/devtools-user/keyboard_shortcuts/index.html#keyboard-shortcuts-opening-and-closing-tools) or the equivalent menu items, they’ll target the document hosted by the currently active tab. But you can attach the tools to a variety of other targets, too, both within the current browser and in different browsers or even different devices.

[about:debugging](https://firefox-source-docs.mozilla.org/devtools-user/about_colon_debugging/index.html)Debug add-ons, content tabs, and workers running in the browser.
[Connecting to Firefox for Android](https://firefox-source-docs.mozilla.org/devtools-user/about_colon_debugging/index.html#about-colon-debugging-connecting-to-a-remote-device)Connect the developer tools to an instance of Firefox running on an Android device.
[Connecting to iframes](https://firefox-source-docs.mozilla.org/devtools-user/working_with_iframes/index.html)Connect the developer tools to a specific iframe in the current page.

Debugging the browser[](https://firefox-source-docs.mozilla.org/devtools-user/#debugging-the-browser "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------

By default, the developer tools are attached to a web page or web app. But you can also connect them to the browser as a whole. This is useful for browser and add-on development.

[Browser Console](https://firefox-source-docs.mozilla.org/devtools-user/browser_console/index.html)See messages logged by the browser itself and by add-ons, and run JavaScript code in the browser’s scope.
[Browser Toolbox](https://firefox-source-docs.mozilla.org/devtools-user/browser_toolbox/index.html)Attach the Developer Tools to the browser itself.

Extending DevTools[](https://firefox-source-docs.mozilla.org/devtools-user/#extending-devtools "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------

For information on extending the Firefox DevTools, see [Extending the developer tools](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Extending_the_developer_tools) over in the [Browser Extensions](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions) section of MDN.

Migrating from Firebug[](https://firefox-source-docs.mozilla.org/devtools-user/#migrating-from-firebug "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------

Firebug has come to the end of its lifespan (see [Firebug lives on in Firefox DevTools](https://hacks.mozilla.org/2016/12/firebug-lives-on-in-firefox-devtools/) for details of why), and we appreciate that some people will find migrating to another less familiar set of DevTools to be challenging. To ease a transition from Firebug to the Firefox developer tools, we have written a handy guide — [Migrating from Firebug](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html)

Contribute[](https://firefox-source-docs.mozilla.org/devtools-user/#contribute "Link to this heading")
-------------------------------------------------------------------------------------------------------

If you want to help improve the developer tools, these resources will get you started.

[Get Involved](https://firefox-dev.tools/)Our community website explains how to get involved.
[codetribute.mozilla.org](https://codetribute.mozilla.org/projects/devtools/)A tool helping to find bugs to work on.
[Read source docs](https://firefox-source-docs.mozilla.org/devtools/index.html#devtools-contributor-doc)Firefox DevTools source code documentation.
