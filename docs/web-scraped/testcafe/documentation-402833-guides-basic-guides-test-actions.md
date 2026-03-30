# Source: https://testcafe.io/documentation/402833/guides/basic-guides/test-actions

Title: Test Actions | Basic Guides | Guides

URL Source: https://testcafe.io/documentation/402833/guides/basic-guides/test-actions

Markdown Content:
[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#article-summary)Article Summary[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#article-summary)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

TestCafe includes a comprehensive set of test action methods.

Test actions look like this:

```
await t.click('#button');
```

Test actions interact with [the page](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#page-actions) and [the browser](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#browser-actions). The [t.request](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#api-testing) action allows you to send HTTP requests and perform API tests.

Test actions are methods of the [TestController](https://testcafe.io/documentation/402665/reference/test-api/testcontroller) object. You can invoke test actions in any function that has access to the [TestController](https://testcafe.io/documentation/402665/reference/test-api/testcontroller), such as the [test body](https://testcafe.io/documentation/403366/reference/test-api/test), [test hooks](https://testcafe.io/documentation/403435/guides/intermediate-guides/hooks), and [Role definitions](https://testcafe.io/documentation/402845/guides/intermediate-guides/authentication).

[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#table-of-contents)Table of contents[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#table-of-contents)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   [List of actions](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#list-of-actions)
*   [How test actions work](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#how-test-actions-work)
*   [Page actions](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#page-actions)
*   [Browser actions](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#browser-actions)
*   [API Testing](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#api-testing)
*   [Role activation](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#role-activation)
*   [Cookie management](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#cookie-management)
*   [Test interruption](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#test-interruption)
*   [Pass data to the reporter](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#pass-data-to-the-reporter)
*   [Scroll elements into view](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#scroll-elements-into-view)
*   [Debug test actions](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#debug-test-actions)

[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#list-of-actions)List of actions[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#list-of-actions)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The following test actions [interact with the page](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#page-actions):

*   [Click](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#click)
*   [Press Key](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#press-key)
*   [Type Text](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#type-text)
*   [Select Text](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#select-text)
*   [Hover](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#hover)
*   [Scroll](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#scroll)
*   [Drag Elements](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#drag-elements)
*   [Upload Files](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#upload-files)
*   [Work with iframes](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#work-with-iframes)

The following test actions [interact with the browser](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#browser-actions):

*   [Navigate to a URL](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#navigate-to-a-url)
*   [Take Screenshots](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#take-screenshots)
*   [Handle Native Dialogs](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#handle-native-dialogs)
*   [Resize Windows](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#resize-windows)
*   [Manage Multiple Browser Windows](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#manage-multiple-browser-windows)

The following test action issues HTTP requests:

*   [Request](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#request)

The following test action pauses the test:

*   [Wait](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#wait)

The following test action interrupts the test and opens the TestCafe debugger panel:

*   [Debug](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#debug)

The following test action passes data to the reporter plugin:

*   [Report](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#report)

TestCafe users can define custom test action methods. Read the [Custom actions guide](https://testcafe.io/documentation/404150/guides/advanced-guides/custom-test-actions) for more information.

[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#how-test-actions-work)How Test Actions Work[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#how-test-actions-work)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Test actions are methods of the [test controller](https://testcafe.io/documentation/402665/reference/test-api/testcontroller) object. Test actions are [infinitely chainable](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#action-chaining). Action targets are subject to [interaction requirements](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#interaction-requirements).

### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#action-chaining)Action Chaining[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#action-chaining)

You can invoke the test controller object for every action or assertion, like so:

```
await t.click('#id1') //actions
await t.typeText('.input-field-1')
await t.click('#submit')

await t.expect(Selector('#result').textContent).eql('expected text');//assertion
```

Some people find this syntax more intuitive when they both write and debug tests. Other people prefer to chain method calls and minimize code:

```
await t
    .click('#id1') //actions
    .typeText('.input-field-1')
    .click('#submit')

    .expect(Selector('#result').textContent).eql('expected text');//assertion
```

You can chain all [test controller methods](https://testcafe.io/documentation/402665/reference/test-api/testcontroller) that don’t return a value, including [custom test actions](https://testcafe.io/documentation/404150/guides/advanced-guides/custom-test-actions). Add blank lines between logical parts of the action chain to improve readability.

You cannot chain the following methods (TestCafe v1.20.0):

*   [t.eval](https://testcafe.io/documentation/402703/reference/test-api/testcontroller/eval)
*   [t.getBrowserConsoleMessages](https://testcafe.io/documentation/402700/reference/test-api/testcontroller/getbrowserconsolemessages)
*   [t.getNativeDialogHistory](https://testcafe.io/documentation/402698/reference/test-api/testcontroller/getnativedialoghistory)
*   [t.request](https://testcafe.io/documentation/403981/reference/test-api/testcontroller/request)

### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#interaction-requirements)Interaction Requirements[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#interaction-requirements)

TestCafe imposes a number of requirements on page action targets to keep action simulation realistic.

The action target must meet the following requirements:

*   The target is the [root page element](https://developer.mozilla.org/en-US/docs/Web/API/Document/documentElement) or its descendant.
*   The target is located in the [active browser window](https://developer.mozilla.org/en-US/docs/Web/API/Window/top) or the active [`<iframe>`](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#work-with-iframes).
*   The target meets the [visibility criteria](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#visibility-criteria).
*   Another element does not overlap the target as to prevent user interaction (See [Treatment of Overlapping DOM Elements](https://testcafe.io/documentation/402827/guides/advanced-guides/built-in-wait-mechanisms#treatment-of-overlapping-dom-elements)).

Important

If the target resides outside the viewport, TestCafe scrolls it into view.

#### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#visibility-criteria)Visibility Criteria[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#visibility-criteria)

The element is `visible` if:

*   The value of the element’s `display` property is not `none`
*   The value of the element’s `visibility` property is not `hidden`
*   The element has a non-zero `width` and `height`

Elements that meet the visibility criteria above may still be invisible to the user. The following factors **do not** influence the element’s visibility status:

*   The element’s `z-index`
*   The element’s `opacity`
*   The element’s position on the page

#### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#additional-requirement-for-ttypetext)Additional requirement for t.typeText[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#additional-requirement-for-ttypetext)

The [`t.typeText`](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#type-text) action can only interact with **focused** elements. If the target element doesn’t have focus, TestCafe **automatically**[clicks](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#click) it. If the element doesn’t gain `:focus` after the click, the action fails.

### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#touch-devices)Touch Devices[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#touch-devices)

On touch devices, TestCafe emulates touch events instead of mouse events.

| Mouse event | Corresponding touch event |
| --- | --- |
| `mousemove` (when you hover or drag) | `touchmove` (when you drag) |
| `mousedown` | `touchstart` |
| `mouseup` | `touchend` |

[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#page-actions)Page Actions[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#page-actions)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#click)Click[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#click)

The following three methods click page elements:

*   [Click](https://testcafe.io/documentation/402710/reference/test-api/testcontroller/click)
*   [Double-Click](https://testcafe.io/documentation/402706/reference/test-api/testcontroller/doubleclick)
*   [Right-Click](https://testcafe.io/documentation/402689/reference/test-api/testcontroller/rightclick)

#### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#example)Example[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#example)

```
import { Selector } from 'testcafe';

fixture`Interact With the Page`
    .page`https://devexpress.github.io/testcafe/example/`;

test('Click test', async t => {
    const selectBasedOnText = Selector('label').withText('I have tried TestCafe');

    await t
        .click(selectBasedOnText);
});
```

### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#press-key)Press Key[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#press-key)

The [Press Key](https://testcafe.io/documentation/402693/reference/test-api/testcontroller/presskey) action presses a key or key combination.

#### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#example-1)Example[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#example-1)

```
fixture`Interact With the Page`
    .page`https://devexpress.github.io/testcafe/example/`;

test('Press Key test', async t => {
    await t
        .click('#tried-test-cafe')
        // pressing 'Space' imitates clicking the checkbox again
        .pressKey('space');
});
```

### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#type-text)Type Text[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#type-text)

The [Type Text](https://testcafe.io/documentation/402674/reference/test-api/testcontroller/typetext) action types a string into an element. The action can target `input` fields, `textarea` elements, and elements with the [`contenteditable`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable) attribute. The action target is subject to additional [interaction requirements](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#additional-requirement-for-ttypetext).

#### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#example-2)Example[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#example-2)

```
fixture`Interact With the Page`
    .page`https://devexpress.github.io/testcafe/example/`;

test('Type Text test', async t => {
    await t
        .typeText('#developer-name', 'John Doe');
});
```

### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#select-text)Select Text[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#select-text)

The [Select Text](https://testcafe.io/documentation/402687/reference/test-api/testcontroller/selecttext) action selects text box content. The action can **only** target `input` fields, `textarea` elements, and elements with the [`contenteditable`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable) attribute.

*   [Select Text in Input Elements](https://testcafe.io/documentation/402687/reference/test-api/testcontroller/selecttext)
*   [Select <textarea> Content](https://testcafe.io/documentation/402686/reference/test-api/testcontroller/selecttextareacontent)
*   [Perform Selection within Editable Content](https://testcafe.io/documentation/402688/reference/test-api/testcontroller/selecteditablecontent)

#### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#example-3)Example[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#example-3)

```
fixture`Interact With the Page`
    .page`https://devexpress.github.io/testcafe/example/`;

test('Select Text test', async t => {
    await t
        .typeText('#developer-name', 'John Doe')
        .selectText('#developer-name')
        .pressKey('delete');
});
```

### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#hover)Hover[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#hover)

The [Hover](https://testcafe.io/documentation/402697/reference/test-api/testcontroller/hover) action hovers the mouse pointer over page elements.

#### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#example-4)Example[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#example-4)

```
fixture`Interact With the Page`
    .page`https://js.devexpress.com`;

test('Hover test', async t => {
    await t
        .hover('.map-container');
});
```

### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#scroll)Scroll[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#scroll)

Important

TestCafe automatically scrolls [valid](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#interaction-requirements) off-screen action targets into view. There is usually no need to use the `scroll` action.

The [Scroll](https://testcafe.io/documentation/403065/reference/test-api/testcontroller/scroll) method scrolls the target element (or the document body) to the specified position.

### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#drag-elements)Drag Elements[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#drag-elements)

The following two methods drag elements around the page:

*   [Drag an Element by an Offset](https://testcafe.io/documentation/402705/reference/test-api/testcontroller/drag)
*   [Drag an Element onto Another](https://testcafe.io/documentation/402704/reference/test-api/testcontroller/dragtoelement)

These methods emulate user interaction with draggable elements. Do not use them to [select text](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#select-text) and perform other complex browser actions.

#### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#example-5)Example[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#example-5)

```
import { Selector } from 'testcafe';

fixture`Interact With the Page`
    .page`https://devexpress.github.io/testcafe/example/`;

test('Drag test', async t => {
    const triedCheckbox = Selector('label').withText('I have tried TestCafe');

    await t
        .click(triedCheckbox)
        .drag('#slider', 360, 0, { offsetX: 10, offsetY: 10 });
});
```

### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#upload-files)Upload Files[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#upload-files)

The following two methods interact with file upload input elements:

*   [t.setFilesToUpload](https://testcafe.io/documentation/402685/reference/test-api/testcontroller/setfilestoupload)
*   [t.clearUpload](https://testcafe.io/documentation/402711/reference/test-api/testcontroller/clearupload)

### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#file-upload-guide)File Upload Guide[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#file-upload-guide)

1.   Use the [t.setFilesToUpload](https://testcafe.io/documentation/402685/reference/test-api/testcontroller/setfilestoupload) action to populate a `file` type input.
2.   If your application uploads files as soon as you populate the field, you don’t need to take any further action. Otherwise, start the upload manually (for example, [click](https://testcafe.io/documentation/402710/reference/test-api/testcontroller/click) the submit button).
3.   Use the [t.clearUpload](https://testcafe.io/documentation/402711/reference/test-api/testcontroller/clearupload) action to clear the list of files to upload.

Read the [Test File Upload](https://testcafe.io/documentation/402808/recipes/basics/test-file-upload) article for more details.

#### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#example-6)Example[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#example-6)

```
fixture`Interact With the Page`
    .page`https://js.devexpress.com/Demos/WidgetsGallery/Demo/FileUploader/FileSelection/jQuery/Light/`;

test('Upload Files test', async t => {
    await t
        .switchToIframe('.demo-frame')
        .setFilesToUpload('.dx-fileuploader-input', [
            // substitute the following string with the path to a local file or multiple files you want to upload
            'src/file.txt',
        ]);
});
```

### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#work-with-iframes)Work With Iframes[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#work-with-iframes)

TestCafe intentionally limits its [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context). When you first load the page, you only gain access to the main window.

Use the `switchToIframe` method to access an `<iframe>`. Use the `switchToMainWindow` method to switch back to the main window.

*   [Switch To <iframe>](https://testcafe.io/documentation/402681/reference/test-api/testcontroller/switchtoiframe)
*   [Switch To Main Window](https://testcafe.io/documentation/402680/reference/test-api/testcontroller/switchtomainwindow)

#### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#example-7)Example[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#example-7)

```
fixture`Interact With the Page`
    .page`https://js.devexpress.com/Demos/WidgetsGallery/Demo/DataGrid/Overview/jQuery/Light/`;

test('Working With iframe test', async t => {
    await t
        .switchToIframe('.demo-frame')
        .click('.dx-datagrid-group-panel')
        .switchToMainWindow();
});
```

[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#browser-actions)Browser Actions[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#browser-actions)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#navigate-to-a-url)Navigate to a URL[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#navigate-to-a-url)

The [Navigate](https://testcafe.io/documentation/402695/reference/test-api/testcontroller/navigateto) action opens a new URL in the current window.

#### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#example-8)Example[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#example-8)

```
fixture`Interact With the Page`
    .page`https://devexpress.github.io/testcafe/example/`;

test('Navigate To URL test', async t => {
    await t
        .navigateTo('https://github.com/DevExpress/testcafe');
});
```

### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#take-screenshots)Take Screenshots[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#take-screenshots)

The following two actions take screenshots:

*   [Take Screenshot](https://testcafe.io/documentation/402675/reference/test-api/testcontroller/takescreenshot)
*   [Take Element Screenshot](https://testcafe.io/documentation/402676/reference/test-api/testcontroller/takeelementscreenshot)

#### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#example-9)Example[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#example-9)

```
fixture`Interact With the Page`
    .page`https://js.devexpress.com`;

test('Take Screenshot test', async t => {
    await t
        .takeScreenshot()
        .takeElementScreenshot('.map-container');
});
```

### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#handle-native-dialogs)Handle Native Dialogs[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#handle-native-dialogs)

Important

Read the [authentication](https://testcafe.io/documentation/402845/guides/intermediate-guides/authentication) guide for information on how to handle native authentication prompts.

Use the `t.setNativeDialogHandler` method to dismiss or interact with native browser dialogs **from that point forward**. If a native dialog appears **before** you call this method, the test fails with an error.

TestCafe can interact with the following native dialog types:

*   [alert](https://developer.mozilla.org/en-US/docs/Web/API/Window/alert)
*   [beforeunload](https://developer.mozilla.org/en-US/docs/Web/API/Window/beforeunload_event)
*   [print](https://developer.mozilla.org/en-US/docs/Web/API/Window/print)
*   [confirm](https://developer.mozilla.org/en-US/docs/Web/API/Window/confirm)
*   [prompt](https://developer.mozilla.org/en-US/docs/Web/API/Window/prompt)
*   [geolocation](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/getCurrentPosition)

Use the `t.getNativeDialogHistory` method to retrieve native dialog data (type, content, and URL).

*   [Set Native Dialog Handler](https://testcafe.io/documentation/402684/reference/test-api/testcontroller/setnativedialoghandler)
*   [Get Native Dialog History](https://testcafe.io/documentation/402698/reference/test-api/testcontroller/getnativedialoghistory)

### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#resize-windows)Resize Windows[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#resize-windows)

Three TestController methods resize browser windows. Before you add these methods to your test suite, make sure that your testing environment meets [the necessary requirements](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#requirements).

*   [t.resizeWindow](https://testcafe.io/documentation/402691/reference/test-api/testcontroller/resizewindow) resizes the window to match the `height` and `width` parameters.
*   [t.resizeWindowToFitDevice](https://testcafe.io/documentation/402690/reference/test-api/testcontroller/resizewindowtofitdevice) resizes the window to match the resolution of a mobile device.
*   [t.maximizeWindow](https://testcafe.io/documentation/402696/reference/test-api/testcontroller/maximizewindow) maximizes the browser window. To enter full-screen mode, use the `--start-fullscreen`[CLI flag](https://testcafe.io/documentation/402639/reference/command-line-interface#browser-options).

Browser windows _retain_ their size in between tests and fixtures. You can use [hooks](https://testcafe.io/documentation/403435/guides/intermediate-guides/hooks) to reset window size before or after test entities.

#### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#requirements)Requirements[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#requirements)

You cannot resize the windows of [remote browsers](https://testcafe.io/documentation/403584/guides/intermediate-guides/mobile-devices-cloud-browsers-and-emulation#remote-and-mobile-devices).

*   **Mac** testing environments are compatible with window resizing actions out of the box.
*   **Windows** testing environments require .NET 4.0 or newer.
*   **Linux** testing environments require an [ICCCM/EWMH-compliant window manager](https://en.wikipedia.org/wiki/Comparison_of_X_window_managers).

#### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#example-10)Example[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#example-10)

```
fixture`Interact With the Page`
    .page`https://devexpress.github.io/testcafe/example/`;

test('Resize Window test', async t => {
    await t
        .resizeWindowToFitDevice('iphonexr')
        .maximizeWindow();
});
```

### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#manage-multiple-browser-windows)Manage Multiple Browser Windows[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#manage-multiple-browser-windows)

TestCafe v1.10.1 introduced the ability to run multi-window tests in select browsers. Read the [Multiple Windows Guide](https://testcafe.io/documentation/402841/guides/intermediate-guides/multiple-browser-windows) for more information.

[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#api-testing)API testing[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#api-testing)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#request)Request[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#request)

The [Request](https://testcafe.io/documentation/403981/reference/test-api/testcontroller/request) action executes an HTTP request and returns the server’s response.

```
const responseBody = await t.request(`http://localhost:3000/helloworld`).body;
t.expect(responseBody).contains('Hello World') // true
```

Read the [API Testing Guide](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing) for a full overview of the framework’s API testing capabilities.

[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#role-activation)Role activation[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#role-activation)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Roles allow you to authenticate users with a single line of code. Read the [Authentication and Roles](https://testcafe.io/documentation/402845/guides/intermediate-guides/authentication) guide for more information.

### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#userole)useRole[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#userole)

The [t.useRole](https://testcafe.io/documentation/402673/reference/test-api/testcontroller/userole) action activates a Role.

#### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#example-11)Example[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#example-11)

```
import * as path from 'path';

const loginUrl = path.join(__dirname, './pages/login-page.html');

import { Role, Selector } from 'testcafe';

const registeredUser = Role(loginUrl, async t => {
    await t
        .typeText('#login', 'User1')
        .typeText('#password', 'pa$$w0rd')
        .click('#sign-in');
});

fixture`TestController.useRole`
    .page`./pages/index.html`;

test('Check avatar after login', async t => {
    await t
        .useRole(registeredUser)
        .expect(Selector('#avatar').visible).ok();
});
```

[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#cookie-management)Cookie management[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#cookie-management)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The following three methods manage page cookies:

### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#deletecookies)deleteCookies[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#deletecookies)

The [t.deleteCookies](https://testcafe.io/documentation/403874/reference/test-api/testcontroller/deletecookies) method deletes cookies.

#### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#example-12)Example[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#example-12)

```
fixture`[API] Delete Cookies`
    .page('https://devexpress.github.io/testcafe/example/');

test('Should delete the cookie with the specified name', async t => {
    await t.setCookies({ name: 'apiCookie1', value: 'value1' });
    await t.expect((await t.getCookies()).length).eql(1);

    await t.deleteCookies('apiCookie1');
    await t.expect((await t.getCookies()).length).eql(0);
});
```

### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#getcookies)getCookies[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#getcookies)

The [t.getCookies](https://testcafe.io/documentation/403873/reference/test-api/testcontroller/getcookies) method retrieves page cookies.

Note

The order of cookies in the array depends on circumstances beyond the framework’s control. Do not expect cookie order to persist between test runs. Reference cookies by name, and not by their array index.

#### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#example-13)Example[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#example-13)

```
fixture`[API] Get Cookies`
    .page('https://devexpress.github.io/testcafe/example/');

test('Should retrieve a cookie by name', async t => {
    //set a cookie for the Example page
    await t.setCookies({ name: 'apiCookie1', value: 'value1' });

    //retrieve the named cookie from any of the tested pages
    const cookies = await t.getCookies('apiCookie1');
    const { name, value } = cookies[0];

    await t
        .expect(name).eql('apiCookie1')
        .expect(value).eql('value1');
});
```

### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#setcookies)setCookies[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#setcookies)

The [t.setCookies](https://testcafe.io/documentation/403872/reference/test-api/testcontroller/setcookies) method sets page cookies.

#### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#example-14)Example[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#example-14)

```
fixture`[API] Set Cookies`
    .page('https://devexpress.github.io/testcafe/example/');

test('Should set cookies by name and value', async t => {
    await t.setCookies({ apiCookie1: 'value1' }, 'http://localhost');

    const cookies = await t.getCookies();

    const { name, value, domain, path } = cookies[0];

    await t
        .expect(name).eql('apiCookie1')
        .expect(value).eql('value1')
        .expect(domain).eql('localhost')
        .expect(path).eql('/');
});
```

[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#test-interruption)Test interruption[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#test-interruption)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#debug)Debug[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#debug)

The [t.debug](https://testcafe.io/documentation/402707/reference/test-api/testcontroller/debug) method indefinitely pauses the test to allow the use of browser developer tools. To continue the test, press the appropriate button on the TestCafe debugger panel.

#### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#example-15)Example[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#example-15)

```
fixture`Interact With the Page`
    .page`https://devexpress.github.io/testcafe/example/`;

test('Test with debug action', async t => {
    await t
        .navigateTo('https://js.devexpress.com')
        .debug()
        .hover('.map-container');
});
```

### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#wait)Wait[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#wait)

The [Wait](https://testcafe.io/documentation/402672/reference/test-api/testcontroller/wait) action pauses the test.

#### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#example-16)Example[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#example-16)

```
fixture`Interact With the Page`
    .page`https://js.devexpress.com`;

test('Wait test', async t => {
    await t
        .hover('.map-container')
        .wait(1000);
});
```

[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#pass-data-to-the-reporter)Pass Data to the Reporter[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#pass-data-to-the-reporter)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#report)Report[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#report)

The [Report](https://testcafe.io/documentation/404350/reference/test-api/testcontroller/report) action passes data to the reporter plugin.

TestCafe scrolls to reach items that are on the page but outside the user’s viewport.

You can use any action (for example, [hover](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#hover)) to scroll towards the desired part of the page.

If you specifically need to scroll the page without any action, use the [scroll action](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#scroll).

```
import { ClientFunction } from 'testcafe';

const scrollBy = ClientFunction(() => {
    window.scrollBy(0, 1000);
});

fixture`Interact With the Page`
    .page`https://devexpress.github.io/testcafe/example/`;

test('Scroll an Element into View', async () => {
    await scrollBy();
});
```

[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#debug-test-actions)Debug test actions[](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#debug-test-actions)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A badly written [Element Selector query](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors) may lead to test action failure. Read the [Debug Tests guide](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests) for more information.
