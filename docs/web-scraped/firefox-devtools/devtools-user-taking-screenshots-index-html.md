# Source: https://firefox-source-docs.mozilla.org/devtools-user/taking_screenshots/index.html

Title: Taking screenshots — Firefox Source Docs documentation

URL Source: https://firefox-source-docs.mozilla.org/devtools-user/taking_screenshots/index.html

Markdown Content:
You can use the Developer Tools to take a screenshot of the entire page, or of a single element in the page.

Taking a screenshot of the page[](https://firefox-source-docs.mozilla.org/devtools-user/taking_screenshots/index.html#taking-a-screenshot-of-the-page "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Use the screenshot icon: [![Image 1: image1](https://firefox-source-docs.mozilla.org/_images/camera-icon.png)](https://firefox-source-docs.mozilla.org/_images/camera-icon.png) to take a full-page screenshot of the current page.

By default, the screenshot icon is not enabled. To enable it:

*   visit the [Settings](https://firefox-source-docs.mozilla.org/devtools-user/settings/index.html) page

*   find the section labeled “Available Toolbox Buttons”

*   check the box labeled “Take a screenshot of the entire page”.

You’ll now see the icon in the toolbar:

Click the icon to take a screenshot of the current page. The screenshot is saved to your browser’s “Downloads” directory:

Taking a screenshot of an element[](https://firefox-source-docs.mozilla.org/devtools-user/taking_screenshots/index.html#taking-a-screenshot-of-an-element "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To take a screenshot of a single element in the page, activate the context menu on that element in the [Inspector’s HTML pane](https://firefox-source-docs.mozilla.org/devtools-user/page_inspector/ui_tour/index.html#page-inspector-ui-tour-html-pane), and select “Screenshot Node”. The screenshot is saved to the browser’s “Downloads” directory:

Copying screenshots to the clipboard[](https://firefox-source-docs.mozilla.org/devtools-user/taking_screenshots/index.html#copying-screenshots-to-the-clipboard "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can also copy the screenshot to the clipboard. Just check the box in Settings labeled “Screenshot to clipboard”:

Now, whenever you take a screenshot, the screenshot is also copied to the clipboard.

Taking screenshots with the web console[](https://firefox-source-docs.mozilla.org/devtools-user/taking_screenshots/index.html#taking-screenshots-with-the-web-console "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you need to specify a different device-pixel-ratio, set a delay before taking the screenshot, or specify your own file name, you can use the `:screenshot` helper function in the [Web Console](https://firefox-source-docs.mozilla.org/devtools-user/web_console/index.html).

Type `:screenshot` in the Web Console to create a screenshot of the current page. By default, the image file will be named `Screen Shot yyy-mm-dd at hh.mm.ss.png`.

Note

**Tip**: You could type `:s` and then hit Tab to autocomplete `:screenshot`.

The command has the following optional parameters:

| Command | Type | Description |
| --- | --- | --- |
| `--clipboard` | boolean | When present, this parameter will cause the screenshot to be copied to the clipboard. Prevents saving to a file unless you use the `--file` option to force file writing. |
| `--delay` | number | The number of seconds to delay before taking the screenshot; you can use an integer or floating point number. This is useful if you want to pop open a menu or invoke a hover state for the screenshot. |
| `--dpr` | number | The device pixel ratio to use when taking the screenshot. Values above 1 yield “zoomed-in” images, whereas values below 1 create “zoomed-out” images. |
| `--file` | boolean | When present, the screenshot will be saved to a file, even if other options (e.g. `--clipboard`) are included. |
| `--filename` | string | The name to use in saving the file. The file should have a “.png” extension. |
| `--fullpage` | boolean | If included, the full webpage will be saved. With this parameter, even the parts of the webpage which are outside the current bounds of the window will be included in the screenshot. When used, “<span style=”white-space: nowrap;”>-fullpage</span>” will be appended to the file name. |
| `--selector` | string | A CSS selector that selects a single element on the page. When supplied, only this element and its descendants will be included in the screenshot. |

Note

If you capture an image to a filename like `test.png`, and then you capture to that same filename, the new image will overwrite the old image. So if you’re using the up-arrow history scroll to capture images in quick succession, be careful — you need to remember to change the filename for each new capture.

Note

Thanks to Eric Meyer for his enthusiasm for our screenshot feature, and help! Small portions of this section have been borrowed from his [Firefox’s :screenshot command](https://meyerweb.com/eric/thoughts/2018/08/24/firefoxs-screenshot-command-2018/) article.
