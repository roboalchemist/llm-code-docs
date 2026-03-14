# Source: https://testcafe.io/documentation/402710/reference/test-api/testcontroller/click

Title: .click() | TestController | Test API | API

URL Source: https://testcafe.io/documentation/402710/reference/test-api/testcontroller/click

Markdown Content:
t.click Method
--------------

Clicks a page element. [Chainable](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#action-chaining).

```
t.click(selector [, options]) → this | Promise<any>
```

| Parameter | Type | Description |
| --- | --- | --- |
| `selector` | Function | String | Selector | Snapshot | Promise | The target page element (See [Select Target Elements](https://testcafe.io/documentation/402710/reference/test-api/testcontroller/click#select-target-elements)). |
| `options`_(optional)_ | Object | Additional action options (see [Options](https://testcafe.io/documentation/402710/reference/test-api/testcontroller/click#options)). |

The following example shows how to use the `t.click` action to check a checkbox element:

```
import { Selector } from 'testcafe';

const checkbox = Selector('#tried-test-cafe');

fixture`TestController.click`
    .page`https://devexpress.github.io/testcafe/example/`;

test('Click a check box and check its state', async t => {
    await t
        .click(checkbox)
        .expect(checkbox.checked).ok();
});
```

[](https://testcafe.io/documentation/402710/reference/test-api/testcontroller/click#select-target-elements)Select Target Elements[](https://testcafe.io/documentation/402710/reference/test-api/testcontroller/click#select-target-elements)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Use the `selector` parameter to identify the target of a DOM event.

You can pass any of the following objects as a `selector`:

*   A CSS selector string.

```
test('Click submit', async t => {

    // Click will be performed on the first element
    // that matches the CSS selector.
    await t.click('#submit-button');
});
```
*   A [selector](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors).

```
import { Selector } from 'testcafe';

fixture`Parameter as Selector`
    .page`https://devexpress.github.io/testcafe/example/`;

const lastCheckbox = Selector('fieldset p:last-child [type="checkbox"]');

test('Click last checkbox', async t => {

    // Click will be performed on the element selected by
    // the 'getLastItem' selector.
    await t.click(lastCheckbox);
});
```
*   A client-side function that returns a DOM element.

```
test('Click first child of the body', async t => {

    // Click will be performed on the element returned by the function,
    // which is the third child of the document's body.
    await t.click(() => document.body.children[0]);
});
```
*   A [DOM node snapshot](https://testcafe.io/documentation/402670/reference/test-api/domnodestate).

```
import { Selector } from 'testcafe';

fixture`Parameter as DOM node snapshot`
    .page`https://devexpress.github.io/testcafe/example/`;

test('Click preferred interface', async t => {
    const preferredInterface = await Selector('#preferred-interface');

    // Click will be performed on the element whose snapshot
    // is specified. This is an element with the '#preferred-interface' ID.
    await t.click(preferredInterface);
});
```
*   A Promise returned by a [selector](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors).

```
import { Selector } from 'testcafe';

const submitButton = Selector('#submit-button');

fixture`Parameter as Promise by Selector`
    .page`https://devexpress.github.io/testcafe/example/`;

test('Click submit', async t => {
    // Click will be performed on the element specified by the selector
    // as soon as the promise is resolved.
    await t.click(submitButton());
});
```

TestCafe waits for the target element to become visible before it executes an action. If this does not happen within the [selector timeout](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#timeout), the test fails.

TestCafe cannot interact with background elements. If a different element overlaps the action target, TestCafe waits for this element to disappear. If this does not happen within the [selector timeout](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#timeout), TestCafe performs the action with the element on top of the original target. Learn more about _stacking_ and [z-index](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/z-index) on MDN.

Note

The [upload action](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#upload-files) is an exception to this rule — it does not check the visibility of the target `input`.

[](https://testcafe.io/documentation/402710/reference/test-api/testcontroller/click#options)Options[](https://testcafe.io/documentation/402710/reference/test-api/testcontroller/click#options)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Click action options provide additional parameters for `t.click`, `t.doubleClick` and `t.rightClick` actions.

```
export interface ClickOptions {
    modifiers: {
        ctrl: boolean;
        alt: boolean;
        shift: boolean;
        meta: boolean;
    };

    offsetX: number;
    offsetY: number;
    caretPos: number;
    speed: number;
}
```

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| `ctrl`, `alt`, `shift`, `meta` | Boolean | Indicate which modifier keys are to be pressed during the mouse action. | `false` |
| `offsetX`, `offsetY` | Number | Mouse pointer coordinates that define a point where the action is performed or started. If an offset is a positive integer, coordinates are calculated relative to the top-left corner of the target element. If an offset is a negative integer, they are calculated relative to the bottom-right corner. | The center of the target element. |
| `caretPos` | Number | The initial caret position if the action is performed on a text input field. A zero-based integer. | The length of the input field content. |
| `speed` | Number | The speed of action emulation. Defines how fast TestCafe performs the action when running tests. A number between `1` (the maximum speed) and `0.01` (the minimum speed). If test speed is also specified in the [CLI](https://testcafe.io/documentation/402639/reference/command-line-interface#--speed-factor), [API](https://testcafe.io/documentation/402655/reference/testcafe-api/runner/run) or in [test code](https://testcafe.io/documentation/402682/reference/test-api/testcontroller/settestspeed), the action speed setting overrides test speed. | `1` |

**Example**

```
import { Selector } from 'testcafe';

const nameInput = Selector('#developer-name');

fixture`Click options`
    .page`https://devexpress.github.io/testcafe/example/`;

test('Fix name', async t => {
    await t
        .typeText(nameInput, 'Pete Parker')
        .click(nameInput, { caretPos: 4 })
        .pressKey('r');
});
```
