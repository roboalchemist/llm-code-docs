# Source: https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html

Title: Migrating from Firebug — Firefox Source Docs documentation

URL Source: https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html

Markdown Content:
When migrating from Firebug to the Firefox Developer Tools, you may wonder where the features you loved in Firebug are available in the Developer Tools. The following list aims to help Firebug users to find their way into the Developer Tools.

![Image 1: ../../_images/logo-developer-quantum1.png](https://firefox-source-docs.mozilla.org/_images/logo-developer-quantum1.png)
For the latest developer tools and features, try Firefox Developer Edition.

[Download Firefox Developer Edition](https://www.mozilla.org/en-US/firefox/developer/)
General[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#general "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------

### Activation[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#activation "Link to this heading")

Firebug’s activation is URL based respecting the [same origin policy](https://en.wikipedia.org/wiki/Same_origin_policy). That means that when you open a page on the same origin in a different tab, Firebug gets opened automatically. And when you open a page of a different origin in the same tab, it closes automatically. The DevTools’ activation on the other hand is tab based. That means, that when you open the DevTools in a tab, they stay open even when you switch between different websites. When you switch to another tab, though, they’re closed.

### Open the tools[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#open-the-tools "Link to this heading")

Firebug can be opened by pressing F12. To open it to inspect an element it is possible to press Ctrl + Shift + C / Cmd + Opt + C. The DevTools share the same shortcuts, but also provide [shortcuts for the different panels](https://firefox-source-docs.mozilla.org/devtools-user/keyboard_shortcuts/index.html#keyboard-shortcuts-opening-and-closing-tools). E.g. the [Network Monitor](https://firefox-source-docs.mozilla.org/devtools-user/network_monitor/index.html) can be opened via Ctrl + Shift + Q / Cmd + Opt + Q, the [Web Console](https://firefox-source-docs.mozilla.org/devtools-user/web_console/index.html) via Ctrl + Shift + K / Cmd + Opt + K and the [Debugger](https://firefox-source-docs.mozilla.org/devtools-user/debugger/index.html) via Ctrl + Shift + S / Cmd + Opt + S.

Web Console[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#web-console "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------

The [Web Console](https://firefox-source-docs.mozilla.org/devtools-user/web_console/index.html) is the equivalent of Firebug’s Console panel. It shows log information associated with a web page and allows you to execute JavaScript expressions via its [command line](https://firefox-source-docs.mozilla.org/devtools-user/web_console/the_command_line_interpreter/index.html). The display between both is somewhat different. This may be changed in [bug 1269730](https://bugzilla.mozilla.org/show_bug.cgi?id=1269730).

### Filter log messages[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#filter-log-messages "Link to this heading")

Firebug offers two ways to filter log messages, via the options menu and via the filter buttons within the toolbar. The Developer Tools console offers similar functionality via the [filter buttons inside its toolbar](https://firefox-source-docs.mozilla.org/devtools-user/web_console/console_messages/index.html#web-console-ui-tour-filtering-by-category) — centralized at one place.

### Command Line API[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#command-line-api "Link to this heading")

The Command Line API in Firebug provides some special functions for your convenience. The Developer Tools command line has [some functions in common](https://firefox-source-docs.mozilla.org/devtools-user/web_console/the_command_line_interpreter/index.html#command-line-interpreter-helper-commands), but also has some other functions and misses others.

### Console API[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#console-api "Link to this heading")

To log things to the console from within the web page Firebug makes a Console API available within the page. The Developer Tools share the [same API](https://developer.mozilla.org/en-US/docs/Web/API/console), so your `console.*` statements will continue to work.

### Persist logs[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#persist-logs "Link to this heading")

In Firebug you can click the _Persist_ button within the toolbar to keep the logged messages between page navigations and reloads. In the DevTools this option is called [Enable persistent logs](https://firefox-source-docs.mozilla.org/devtools-user/settings/index.html#settings-common-preferences) and is available within the Toolbox Options panel.

### Server logs[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#server-logs "Link to this heading")

Firebug extensions like FirePHP allow to log server-side messages to the Firebug console. This functionality is already [integrated into the DevTools](https://firefox-source-docs.mozilla.org/devtools-user/web_console/console_messages/index.html#web-console-server) using the [ChromeLogger](https://craig.is/writing/chrome-logger) protocol and doesn’t require any extensions to be installed.

### Command history[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#command-history "Link to this heading")

The [command history](https://firefox-source-docs.mozilla.org/devtools-user/web_console/the_command_line_interpreter/index.html#command-line-interpreter-execution-history) available through a button in Firebug’s command line, is available by pressing ↑/↓ within the DevTools command line.

### Inspect object properties[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#inspect-object-properties "Link to this heading")

By clicking on an object logged within the console you can inspect the object’s properties and methods within the DOM panel. In the Firefox DevTools you can also inspect the objects. The difference is that they [show the properties and methods within a side panel inside the Web Console](https://firefox-source-docs.mozilla.org/devtools-user/web_console/rich_output/index.html#web-console-rich-output-examining-object-properties).

### Show network requests[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#show-network-requests "Link to this heading")

The Console panel in Firebug allows to log [AJAX](https://developer.mozilla.org/en-US/docs/Glossary/AJAX) requests (aka [XMLHttpRequest](https://developer.mozilla.org/en-US/docs/Glossary/XHR_(XMLHttpRequest))). This option is also available within the DevTools Web Console via the _Net_>_XHR_. Furthermore, the Web Console even allows to display all other network requests via _Net_>_Log_.

### View JSON and XML structures[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#view-json-and-xml-structures "Link to this heading")

To view JSON and XML responses of [AJAX](https://developer.mozilla.org/en-US/docs/Glossary/AJAX) requests, Firebug has special tabs when expanding the request within the Console panel. The DevTools Web Console shows those structures directly under the “Response” tab.

### Multi-line command line[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#multi-line-command-line "Link to this heading")

Firebug’s console has a multi-line command line called Command Editor. The DevTools have a [side panel](https://firefox-source-docs.mozilla.org/devtools-user/web_console/the_command_line_interpreter/index.html#command-line-interpreter-multi-line-mode) like the Command Editor.

### Response preview[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#response-preview "Link to this heading")

There is a _Preview_ tab when a network request logged to the console is expanded in Firebug. The Web Console displays a preview within the _Response_ tab. It is currently missing the preview for HTML, XML and SVG, though, which is tracked in [bug 1247392](https://bugzilla.mozilla.org/show_bug.cgi?id=1247392) and [bug 1262796](https://bugzilla.mozilla.org/show_bug.cgi?id=1262796), but when you click on the URL of the request you switch to the [Network Monitor](https://firefox-source-docs.mozilla.org/devtools-user/network_monitor/index.html), which has a _Preview_ tab.

Inspector[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#inspector "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------

Firebug has an HTML panel, which allows to edit HTML/XML/SVG and the CSS related to it. Within the DevTools this functionality is served by the [Page Inspector](https://firefox-source-docs.mozilla.org/devtools-user/page_inspector/index.html).

### Edit HTML[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#edit-html "Link to this heading")

Within the Page Inspector the tag attributes and the contents can be edited inline just like in Firebug. Beyond that it allows to edit the tag names inline.

You can also edit the HTML directly. In Firebug you do this by right-clicking a node and clicking Edit HTML… in the context menu. In the DevTools this option is also available via the context menu. There the option is called [Edit As HTML](https://firefox-source-docs.mozilla.org/devtools-user/page_inspector/how_to/examine_and_edit_html/index.html#page-inspector-how-to-examine-and-edit-html-editing-html). Only the live preview of changes is currently missing, which is tracked in [bug 1067318](https://bugzilla.mozilla.org/show_bug.cgi?id=1067318) and [bug 815464](https://bugzilla.mozilla.org/show_bug.cgi?id=815464).

### Copy HTML and related information[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#copy-html-and-related-information "Link to this heading")

Firebug’s HTML panel allows to copy the inner and outer HTML of an element as well as the CSS and XPath to it via the context menu of an element. The Page Inspector provides the same functionality except copying XPaths. This is covered by [bug 987877](https://bugzilla.mozilla.org/show_bug.cgi?id=987877).

### Edit CSS[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#edit-css "Link to this heading")

Both tools allow to view and edit the CSS rules related to the element selected within the node view in a similar way. Firebug has a Style side panel for this, the DevTools have a [Rules side panel](https://firefox-source-docs.mozilla.org/devtools-user/page_inspector/how_to/examine_and_edit_css/index.html).

In Firebug you add new rules by right-clicking and choosing _Add Rule…_ from the context menu. The DevTools also have a context menu option for that named [Add New Rule and additionally have a + button](https://firefox-source-docs.mozilla.org/devtools-user/page_inspector/how_to/examine_and_edit_css/index.html#page-inspector-how-to-examine-and-edit-css-add-rules) within the Rules panel’s toolbar to create new rules.

To edit element styles, i.e. the CSS properties of the [style](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes#attr-style) attribute of an element, in Firebug you have to right-click into the Style side panel and choose Edit Element Style… from the context menu. The DevTools display an [element {} rule](https://firefox-source-docs.mozilla.org/devtools-user/page_inspector/how_to/examine_and_edit_css/index.html#page-inspector-how-to-examine-and-edit-css-element-rule) for this purpose, which requires a single click into it to start editing the properties.

### Auto-completion of CSS[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#auto-completion-of-css "Link to this heading")

As in Firebug, the Rules view provides an auto-completion for the CSS property names and their values. A few property values are not auto-completed yet, which is tracked in [bug 1337918](https://bugzilla.mozilla.org/show_bug.cgi?id=1337918).

### Copy & paste CSS[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#copy-paste-css "Link to this heading")

Firebug’s Style side panel as well as the DevTools’ Rules side panel provide options within their context menus to copy the CSS rule or the style declarations. The DevTools additionally provide an option to copy the selector of a rule and copy disabled property declarations as commented out. They are missing the option to copy the whole style declaration, though this can be achieved by selecting them within the panel and copying the selection by pressing Ctrl + C or via the context menu.

The Rules side panel of the DevTools is smarter when it comes to pasting CSS into it. You can paste whole style declarations into an existing rule property declarations which are commented out are automatically disabled.

### Toggle pseudo-classes[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#toggle-pseudo-classes "Link to this heading")

Firebug lets you toggle the CSS [pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)[:hover](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:hover), [:active](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active) and [:focus](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus) for an element via the options menu of the Style side panel. In the DevTools there are two ways to do the same. The first one is to toggle them via the pseudo-class panel within the Rules side panel. The second one is to right-click and element within the node view and toggle the pseudo-classes via the [context menu](https://firefox-source-docs.mozilla.org/devtools-user/page_inspector/how_to/examine_and_edit_html/index.html#page-inspector-how-to-examine-and-edit-html-context-menu-reference).

### Examine CSS shorthand properties[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#examine-css-shorthand-properties "Link to this heading")

CSS [shorthand properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties) can be split into their related longhand properties by setting the option _Expand Shorthand Properties_ within the Style side panel. The DevTools’ Rules panel is a bit smarter and allows you to expand individual shorthand properties by clicking the twisty besides them.

### Only show applied styles[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#only-show-applied-styles "Link to this heading")

The Style side panel in Firebug has an option to display only the properties of a CSS rule that are applied to the selected element and hide all overwritten styles. There is no such feature in the [Rules side panel](https://firefox-source-docs.mozilla.org/devtools-user/page_inspector/how_to/examine_and_edit_css/index.html) of the DevTools, but it is requested in [bug 1335327](https://bugzilla.mozilla.org/show_bug.cgi?id=1335327).

### Inspect box model[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#inspect-box-model "Link to this heading")

In Firebug the [box model](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/The_box_model) can be inspected via the Layout side panel. In the DevTools the [box model is part of the Computed side panel](https://firefox-source-docs.mozilla.org/devtools-user/page_inspector/how_to/examine_and_edit_the_box_model/index.html). Both tools highlight the different parts of the box model within the page when hovering them in the box model view. Also, both tools allow you to edit the different values inline via a click on them.

### Inspect computed styles[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#inspect-computed-styles "Link to this heading")

The computed values of CSS properties are displayed within the DevTools’ [Computed side panel](https://firefox-source-docs.mozilla.org/devtools-user/page_inspector/how_to/examine_and_edit_css/index.html#page-inspector-how-to-examine-and-edit-css-examine-computed-css) like within Firebug’s Computed side panel. The difference is that in the DevTools the properties are always listed alphabetically and not grouped (see [bug 977128](https://bugzilla.mozilla.org/show_bug.cgi?id=977128)) and there is no option to hide the Mozilla specific styles, therefore there is an input field allowing to filter the properties.

### Inspect events[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#inspect-events "Link to this heading")

Events assigned to an element are displayed in the Events side panel in Firebug. In the DevTools they are shown when clicking the small ‘ev’ icon besides an element within the node view. Both tools allow to display wrapped event listeners (e.g. listeners wrapped in jQuery functions). To improve the UI of the DevTools, there is also a request to add an Events side panel to them like the one in Firebug (see [bug 1226640](https://bugzilla.mozilla.org/show_bug.cgi?id=1226640)).

### Stop script execution on DOM mutation[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#stop-script-execution-on-dom-mutation "Link to this heading")

In Firebug you can break on DOM mutations, that means that when an element is changed, the script execution is stopped at the related line within the JavaScript file, which caused the change. This feature can globally be enabled via the _Break On Mutate_ button, or individually for each element and for different types of changes like attribute changes, content changes or element removal. Unfortunately, the DevTools do not have this feature yet (see [bug 1004678](https://bugzilla.mozilla.org/show_bug.cgi?id=1004678)). To stop the script execution there, you need to set a breakpoint on the line with the modification within the [Debugger panel](https://firefox-source-docs.mozilla.org/devtools-user/debugger/index.html).

### Search for elements via CSS selectors or XPaths[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#search-for-elements-via-css-selectors-or-xpaths "Link to this heading")

Firebug allows to search for elements within the HTML panel via CSS selectors or XPaths. Also the [DevTools’ Inspector panel allows to search for CSS selectors](https://firefox-source-docs.mozilla.org/devtools-user/page_inspector/how_to/examine_and_edit_html/index.html#page-inspector-how-to-examine-and-edit-html-searching). It even displays a list with matching IDs or classes. Searching by XPaths is not supported though (see [bug 963933](https://bugzilla.mozilla.org/show_bug.cgi?id=963933)).

Debugger[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#debugger "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------

What’s the Script panel in Firebug, is the [Debugger panel](https://firefox-source-docs.mozilla.org/devtools-user/debugger/index.html) in the DevTools. Both allow you to debug JavaScript code executed on a website.

### Switch between sources[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#switch-between-sources "Link to this heading")

Firebug has a Script Location Menu listing all JavaScript sources related to the website. Those sources can be static, i.e. files, or they can be dynamically generated (i.e. scripts executed via event handlers, `eval()`, `new Function()`, etc.). In the DevTools’ Debugger panel the scripts are listed at the left side within the [Sources side panel](https://firefox-source-docs.mozilla.org/devtools-user/debugger/ui_tour/index.html#debugger-ui-tour-source-list-pane). Dynamically generated scripts are only listed there when they are [named via a //# sourceURL comment](https://firefox-source-docs.mozilla.org/devtools-user/debugger/how_to/debug_eval_sources/index.html).

### Managing breakpoints[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#managing-breakpoints "Link to this heading")

In Firebug you can set different types of breakpoints, which are all listed within the Breakpoints side panel. In the DevTools the breakpoints are shown below each script source within the [Sources side panel](https://firefox-source-docs.mozilla.org/devtools-user/debugger/ui_tour/index.html#debugger-ui-tour-source-list-pane). Those panels allow you to enable and disable single or all breakpoints and to remove single breakpoints or all of them at once. They do currently only allow to set script breakpoints. XHR, DOM, Cookie and Error breakpoints are not supported yet (see [bug 821610](https://bugzilla.mozilla.org/show_bug.cgi?id=821610), [bug 1004678](https://bugzilla.mozilla.org/show_bug.cgi?id=1004678), [bug 895893](https://bugzilla.mozilla.org/show_bug.cgi?id=895893) and [bug 1165010](https://bugzilla.mozilla.org/show_bug.cgi?id=1165010)). While there are no breakpoints for single JavaScript errors, there is a setting _Pause on Exceptions_ within the [Debugger panel options](https://firefox-source-docs.mozilla.org/devtools-user/settings/index.html#settings-debugger).

### Step through code[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#step-through-code "Link to this heading")

Once the script execution is stopped, you can step through the code using the Continue (F8), Step Over (F10), Step Into (F11) and Step Out (Shift + F11) options. They work the same in both tools.

### Examine call stack[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#examine-call-stack "Link to this heading")

When the script execution is paused, Firebug displays the function call stack within its Stack side panel. In there the functions are listed together with their call parameters. In the DevTools the function call stack is shown within the [Call Stack side panel](https://firefox-source-docs.mozilla.org/devtools-user/debugger/ui_tour/index.html#debugger-ui-tour-call-stack). To see the call parameters in the DevTools, you need to have a look at the [Variables side panel](https://firefox-source-docs.mozilla.org/devtools-user/debugger/how_to/set_watch_expressions/index.html).

### Examine variables[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#examine-variables "Link to this heading")

The Watch side panel in Firebug displays the [window](https://developer.mozilla.org/en-US/docs/Web/API/Window) object (the global scope) by default. With the script execution halted it shows the different variable scopes available within the current call stack frame. Furthermore, it allows you to add and manipulate watch expressions. The DevTools have a [Variables side panel](https://firefox-source-docs.mozilla.org/devtools-user/debugger/how_to/set_watch_expressions/index.html), which works basically the same. The main difference is that it is empty when the script execution is not stopped, i.e. it doesn’t display the `window` object. Though you can inspect that object either via the [DOM property viewer](https://firefox-source-docs.mozilla.org/devtools-user/dom_property_viewer/index.html) or via the [Web Console](https://firefox-source-docs.mozilla.org/devtools-user/web_console/index.html).

Style Editor[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#style-editor "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

The [Style Editor](https://firefox-source-docs.mozilla.org/devtools-user/style_editor/index.html) in the Firefox DevTools allows you to examine and edit the different CSS style sheets of a page like Firebug’s CSS panel does it. In addition to that it allows to create new style sheets and to import existing style sheets and apply them to the page. It also allows you to toggle individual style sheets.

### Switch between sources[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#id3 "Link to this heading")

The CSS panel of Firebug allows to switch between different CSS sources using the CSS Location Menu. The Style Editor has a [sidebar](https://firefox-source-docs.mozilla.org/devtools-user/style_editor/index.html#style-editor-the-style-sheet-pane) for this purpose.

### Edit a style sheet[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#edit-a-style-sheet "Link to this heading")

Firebug’s CSS panel offers three different ways for editing style sheets. The default one is to edit them inline like within the Style side panel. Furthermore it has a Source and a Live Edit mode, which allow to edit the selected style sheet like within a text editor. The Style Editor of the DevTools only has one way to edit style sheets, which corresponds to Firebug’s Live Edit mode.

### Try out CSS selectors[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#try-out-css-selectors "Link to this heading")

Firebug’s Selectors side panel provides a way to validate a CSS selector. It lists all elements matching the entered selector. The DevTools don’t have this feature yet, but it’s requested in [bug 1323746](https://bugzilla.mozilla.org/show_bug.cgi?id=1323746).

### Searching within the style sheets[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#searching-within-the-style-sheets "Link to this heading")

Firebug allows to search within the style sheets via the search field. The Style Editor in the DevTools also provides a way to search within a style sheet, though there is currently no option to search within multiple sheets (see [bug 889571](https://bugzilla.mozilla.org/show_bug.cgi?id=889571) and also not via a regular expression (see [bug 1362030](https://bugzilla.mozilla.org/show_bug.cgi?id=1362030)).

Performance Tool[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#performance-tool "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------

Firebug allows to profile JavaScript performance via the “Profile” button within the Console panel or the `console.profile()` and `console.profileEnd()` commands. The DevTools provide advanced tooling regarding performance profiling. A profile can be created via [console.profile()](https://developer.mozilla.org/en-US/docs/Web/API/console/profile) and [console.profileEnd()](https://developer.mozilla.org/en-US/docs/Web/API/console/profileEnd) like in Firebug or via the “Start Recording Performance” button in the [Performance Tool](https://firefox-source-docs.mozilla.org/devtools-user/performance/index.html). The output of the Call Tree is the one that comes nearest to the output in Firebug, but the Performance panel provides much more information than just the JavaScript performance. E.g. it also provides information about HTML parsing or layout.

This is the part where Firebug and the DevTools differ the most, because the outputs are completely different. While Firebug focuses on JavaScript performance and provides detailed information about JavaScript function calls during the profiling session, the Performance Tool in the DevTools offers a broad spectrum of information regarding a website’s performance but doesn’t go into detail regarding JavaScript function calls.

### View JavaScript call performance[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#view-javascript-call-performance "Link to this heading")

What comes nearest to Firebug’s profiler output is the [Call Tree view](https://firefox-source-docs.mozilla.org/devtools-user/performance/index.html) in the Performance panel. Like in Firebug it lists the total execution time of each function call under _Total Time_ as well as the number of calls under _Samples_, the time spent within the function under _Self Time_ and the related percentages in reference to the total execution time.

Note

The times and percentages listed in the DevTools’ Call Tree view is not equivalent to the ones shown in Firebug, because it uses different APIs sampling the execution of the JavaScript code.

### Jump to function declaration[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#jump-to-function-declaration "Link to this heading")

Like in Firebug’s profiler output the Call Tree view of the DevTools’ Performance Tool allows to jump to the line of code where the called JavaScript function is defined. In Firebug the source link to the function is located at the right side of the Console panel output while within the DevTools the link is placed on the right side within the Call Tree View.

Network Monitor[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#network-monitor "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------

To monitor network requests Firebug provides a Net panel. The Firefox DevTools allow to inspect the network traffic using the [Network Monitor](https://firefox-source-docs.mozilla.org/devtools-user/network_monitor/index.html). Both tools provide similar information including a timeline showing the request and response times of the network requests.

### Inspect request information[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#inspect-request-information "Link to this heading")

Both Firebug and the Firefox DevTools’ Network Monitor allow you to inspect the information about a request by clicking on it. The only difference is that Firebug shows the information below the request while the Network Monitor displays it within a side panel.

In both tools there are different tabs containing different kinds of information for the selected request. They contain a _Headers_, _Params_, _Response_ and _Cookies_ panel. A preview of the response is shown within specifically named panels like _HTML_. The Network Monitor has a _Preview_ panel for this purpose. It doesn’t provide information about the cached data yet (see [bug 859051](https://bugzilla.mozilla.org/show_bug.cgi?id=859051)), but provides a _Security_ tab in addition to Firebug’s information and a _Timings_ tab showing detailed information about the network timings.

### View request timings[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#view-request-timings "Link to this heading")

Firebug offers detailed information about the network timings related to a request by hovering the Timeline column within its Net panel. The Network Monitor shows this information within a [Timings side panel](https://firefox-source-docs.mozilla.org/devtools-user/network_monitor/request_details/index.html#network-monitor-request-details-timings-tab) when you select a request.

### View remote address[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#view-remote-address "Link to this heading")

The remote address of a request is shown within the Remote IP column within Firebug. In the Network Monitor the address is shown at _Remote Address_ in the _Headers_ tab when a request is selected.

### Search within requests[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#search-within-requests "Link to this heading")

The search field within Firebug allows to search within the requests. The search field in the Firefox DevTools filters the requests by the entered string.

Firebug allowed to search within the response body of the network requests by checking _Response Bodies_ within its search field options. This feature is not available yet within the Network Monitor, but it’s requested in [bug 1334408](https://bugzilla.mozilla.org/show_bug.cgi?id=1334408). While response bodies can’t be searched yet, the Network Monitor allows to [filter by different request properties](https://firefox-source-docs.mozilla.org/devtools-user/network_monitor/request_list/index.html#request-list-filtering-by-properties).

Storage Inspector[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#storage-inspector "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------

The Cookies panel in Firebug displays information related to the cookies created by a page and allows to manipulate the information they store. Within the DevTools this functionality is located within the [Storage Inspector](https://firefox-source-docs.mozilla.org/devtools-user/storage_inspector/index.html). In contrast to Firebug the Storage Inspector not only allows to inspect cookies but also other kinds of storages like the local and session storage, the cache and [IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API) databases.

### Inspect cookies[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#inspect-cookies "Link to this heading")

All cookies related to a website are listed inside the Cookies panel in Firebug. Inside the DevTools, the cookies are grouped by domain under the Cookies section within the [Storage Inspector](https://firefox-source-docs.mozilla.org/devtools-user/storage_inspector/index.html). Both show pretty much the same information per cookie, i.e. the name, value, domain, path, expiration date and whether the cookie is HTTP-only.

The DevTools don’t show by default whether a cookie is secure, but this can be enabled by right-clicking the table header and checking _Secure_ from the context menu. Additionally, the DevTools allow to display the creation date of a cookie as well as when it was last accessed and whether it is host-only.

### Edit cookies[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#edit-cookies "Link to this heading")

To edit a cookie in Firebug you have to right-click the cookie and choose _Edit_ from the context menu. Then a dialog pops up allowing you to edit the data of the cookie and save it. Inside the Storage Inspector you just have to double-click the data you want to edit. Then an inline editor allows you to edit the value.

### Delete cookies[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#delete-cookies "Link to this heading")

Firebug’s Cookies panel allows you to delete all cookies of a website via the menu option _Cookies_>_Remove Cookies_ or by pressing Ctrl + Shift + O. It also allows you to only remove session cookies via _Cookies_>_Remove Session Cookies_ and to remove single cookies by right-clicking them and choosing _Delete_. The DevTools Storage Inspector allows to remove all cookies and a single one by right-clicking on a cookie and choosing _Delete All_ resp. _Delete “<cookie name>”_. Additionally, it allows to delete all cookies from a specific domain via the context menu option _Delete All From “<domain name>”_. It currently does not allow to only delete session cookies (see [bug 1336934](https://bugzilla.mozilla.org/show_bug.cgi?id=1336934)).

Feedback[](https://firefox-source-docs.mozilla.org/devtools-user/migrating_from_firebug/index.html#feedback "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------

We are always happy to respond to feedback and questions. If you have any queries or points of view, feel free to share them on our [DevTools Discourse Forum](https://discourse.mozilla.org/c/devtools).
