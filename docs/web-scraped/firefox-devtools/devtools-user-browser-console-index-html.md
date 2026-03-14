# Source: https://firefox-source-docs.mozilla.org/devtools-user/browser_console/index.html

Title: Browser Console — Firefox Source Docs documentation

URL Source: https://firefox-source-docs.mozilla.org/devtools-user/browser_console/index.html

Markdown Content:
The Browser Console is like the [Web Console](https://firefox-source-docs.mozilla.org/devtools-user/web_console/index.html), but applied to the whole browser rather than a single content tab.

So it logs the same sorts of information as the Web Console - network requests, JavaScript, CSS, and security errors and warnings, and messages explicitly logged by JavaScript code. However, rather than logging this information for a single content tab, it logs information for all content tabs, for add-ons, and for the browser’s own code.

If you also want to use the other web developer tools in the regular Web [Toolbox](https://firefox-source-docs.mozilla.org/devtools-user/tools_toolbox/index.html) with add-on or browser code, consider using the [Browser Toolbox](https://firefox-source-docs.mozilla.org/devtools-user/browser_toolbox/index.html).

Similarly, you can execute JavaScript expressions using the Browser Console. But while the Web Console executes code in the page window scope, the Browser Console executes them in the scope of the browser’s chrome window. This means you can interact with all the browser’s tabs using the `gBrowser` global, and even with the XUL used to specify the browser’s user interface.

NB: The Browser Console command line (to execute JavaScript expressions) is disabled by default. To enable it set the `devtools.chrome.enabled` preference to `true` in [about:config](about:config), or set the “Enable browser [chrome](https://developer.mozilla.org/en-US/docs/Glossary/Chrome) and add-on debugging toolboxes” option in the [developer tool settings](https://firefox-source-docs.mozilla.org/devtools-user/settings/index.html).

Opening the Browser Console[](https://firefox-source-docs.mozilla.org/devtools-user/browser_console/index.html#opening-the-browser-console "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can open the Browser Console in one of two ways:

1.   from the menu: select “Browser Console” from the Browser Tools submenu in the Firefox Menu (or Tools menu if you display the menu bar or are on macOS).

2.   from the keyboard: press Ctrl + Shift + J (or Cmd + Shift + J on a Mac).

You can also start the Browser Console by launching Firefox from the command line and passing the `-jsconsole` argument:

/Applications/FirefoxAurora.app/Contents/MacOS/firefox -jsconsole

The Browser Console looks like this:

![Image 1: ../../_images/browser_console_68.png](https://firefox-source-docs.mozilla.org/_images/browser_console_68.png)
You can see that the Browser Console looks and behaves very much like the [Web Console](https://firefox-source-docs.mozilla.org/devtools-user/web_console/index.html):

*   most of the window is occupied by a [pane that display messages](https://firefox-source-docs.mozilla.org/devtools-user/web_console/console_messages/index.html)

*   at the top, a [toolbar](https://firefox-source-docs.mozilla.org/devtools-user/web_console/ui_tour/index.html#web-console-ui-tour-toolbar) enables you to filter the messages that appear.

*   at the bottom, a [command line interpreter](https://firefox-source-docs.mozilla.org/devtools-user/web_console/the_command_line_interpreter/index.html) enables you to evaluate JavaScript expressions.

The Browser Console allows you to show or hide messages from the content process (i.e. the messages from scripts in all the opened pages) by setting or clearing the checkbox labeled **Show Content Messages**. The following image shows the browser console focused on the same page as above after clicking on the **Show Content Messages** checkbox.

![Image 2: ../../_images/browser_console_68_02.png](https://firefox-source-docs.mozilla.org/_images/browser_console_68_02.png)
Browser Console logging[](https://firefox-source-docs.mozilla.org/devtools-user/browser_console/index.html#browser-console-logging "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------

The Browser console logs the same sorts of messages as the Web Console:

*   [HTTP requests](https://firefox-source-docs.mozilla.org/devtools-user/web_console/console_messages/index.html#web-console-console-messages)

*   [Warnings and errors](https://firefox-source-docs.mozilla.org/devtools-user/web_console/console_messages/index.html) (including JavaScript, CSS, security warnings and errors, and messages explicitly logged by JavaScript code using the [Console API](https://developer.mozilla.org/en-US/docs/Web/API/console)

*   [Input/output messages](https://firefox-source-docs.mozilla.org/devtools-user/web_console/console_messages/index.html#web-console-console-messages-interpreter-io) commands send to the browser via the command line, and the result of executing them

However, it displays such messages from:

*   web content hosted by all browser tabs

*   the browser’s own code

*   add-ons

### Messages from add-ons[](https://firefox-source-docs.mozilla.org/devtools-user/browser_console/index.html#messages-from-add-ons "Link to this heading")

The Browser Console displays messages logged by all Firefox add-ons.

#### Console.sys.mjs[](https://firefox-source-docs.mozilla.org/devtools-user/browser_console/index.html#console-sys-mjs "Link to this heading")

To use the console API from a traditional or bootstrapped add-on, get it from the Console module.

One exported symbol from `Console.sys.mjs` is `console`. Below is an example of how to access it, which adds a message to the Browser Console.

const { console } = ChromeUtils.importESModule("resource://gre/modules/Console.sys.mjs");
console.log("Hello from Firefox code"); //output messages to the console

Learn more:

*   [Console API reference](https://developer.mozilla.org/en-US/docs/Web/API/console)

*   [Console.sys.mjs source code](https://searchfox.org/firefox-main/source/toolkit/modules/Console.sys.mjs)

Browser Console command line[](https://firefox-source-docs.mozilla.org/devtools-user/browser_console/index.html#browser-console-command-line "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

The Browser Console command line is disabled by default. To enable it set the `devtools.chrome.enabled` preference to `true` in `about:config`, or set the “Enable chrome debugging” option in the [developer tool settings](https://firefox-source-docs.mozilla.org/devtools-user/settings/index.html).

Like the Web Console, the command line interpreter enables you to evaluate JavaScript expressions in real time:

![Image 3: ../../_images/browser-console-commandline.png](https://firefox-source-docs.mozilla.org/_images/browser-console-commandline.png)
Also like the Web Console’s command line interpreter, this command line supports autocomplete, history, and various [keyboard shortcuts](https://firefox-source-docs.mozilla.org/devtools-user/keyboard_shortcuts/index.html#keyboard-shortcuts-web-console) and [helper commands](https://firefox-source-docs.mozilla.org/devtools-user/web_console/helpers/index.html). If the result of a command is an object, you can click on the object to see its details.

But while the Web Console executes code in the scope of the content window it’s attached to, the browser console executes code in the scope of the chrome window of the browser. You can confirm this by evaluating `window`:

![Image 4: ../../_images/browser-console-chromewindow.png](https://firefox-source-docs.mozilla.org/_images/browser-console-chromewindow.png)
This means you can control the browser: opening, closing tabs and windows and changing the content that they host, and modify the browser’s UI by creating, changing and removing XUL elements.

### Controlling the browser[](https://firefox-source-docs.mozilla.org/devtools-user/browser_console/index.html#controlling-the-browser "Link to this heading")

The command line interpreter gets access to the `tabbrowser` object, through the `gBrowser` global, and that enables you to control the browser through the command line. Try running this code in the Browser Console’s command line (remember that to send multiple lines to the Browser Console, use Shift + Enter):

var newTabBrowser = gBrowser.getBrowserForTab(gBrowser.selectedTab);
newTabBrowser.addEventListener("load", function() {
 newTabBrowser.contentDocument.body.innerHTML = "<h1>this page has been eaten</h1>";
}, true);
newTabBrowser.contentDocument.location.href = "https://mozilla.org/";

It adds a listener to the currently selected tab’s `load` event that will eat the new page, then loads a new page.

Note

You can restart the browser with the command Ctrl + Alt + R (Windows, Linux) or Cmd + Alt + R (Mac) This command restarts the browser with the same tabs open as before the restart.

### Modifying the browser UI[](https://firefox-source-docs.mozilla.org/devtools-user/browser_console/index.html#modifying-the-browser-ui "Link to this heading")

Since the global `window` object is the browser’s chrome window, you can also modify the browser’s user interface. On Windows, the following code will add a new item to the browser’s main menu:

var parent = window.document.getElementById("appmenuPrimaryPane");
var makeTheTea = gBrowser.ownerDocument.defaultView.document.createElementNS("http://www.mozilla.org/keymaster/gatekeeper/there.is.only.xul", "menuitem");
makeTheTea.setAttribute("label", "A nice cup of tea?");
parent.appendChild(makeTheTea);

![Image 5: ../../_images/browser-console-modify-ui-windows.png](https://firefox-source-docs.mozilla.org/_images/browser-console-modify-ui-windows.png)
On macOS, this similar code will add a new item to the **Tools** menu:

var parent = window.document.getElementById("menu_ToolsPopup");
var makeTheTea = gBrowser.ownerDocument.defaultView.document.createElementNS("http://www.mozilla.org/keymaster/gatekeeper/there.is.only.xul", "menuitem");
makeTheTea.setAttribute("label", "A nice cup of tea?");
parent.appendChild(makeTheTea);

![Image 6: ../../_images/browser-console-modify-ui-osx.png](https://firefox-source-docs.mozilla.org/_images/browser-console-modify-ui-osx.png)
