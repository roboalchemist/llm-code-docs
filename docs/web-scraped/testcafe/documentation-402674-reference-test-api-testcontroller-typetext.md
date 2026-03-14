# Source: https://testcafe.io/documentation/402674/reference/test-api/testcontroller/typetext

Title: .typeText() | TestController | Test API | API

URL Source: https://testcafe.io/documentation/402674/reference/test-api/testcontroller/typetext

Markdown Content:
t.typeText Method
-----------------

Types a string into an `input` field, a `textarea` element, or an element with the [`contenteditable`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable) attribute. The method is [chainable](https://testcafe.io/402898/resources/blog/2020-8-19-testcafe-webinar-your-questions-answered#action-chaining).

```
t.typeText(selector, text [, options]) → this | Promise<any>
```

| Parameter | Type | Description |
| --- | --- | --- |
| `selector` | Function | String | Selector | Snapshot | Promise | Action target. See [Select Page Elements](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors). |
| `text` | String | The string to type. |
| `options`_(optional)_ | Object | Action parameters. See [Options](https://testcafe.io/documentation/402674/reference/test-api/testcontroller/typetext#options). |

[](https://testcafe.io/documentation/402674/reference/test-api/testcontroller/typetext#interaction-requirements)Interaction Requirements[](https://testcafe.io/documentation/402674/reference/test-api/testcontroller/typetext#interaction-requirements)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

TestCafe cannot execute the `t.typeText` action if the target element is not **focused**. To prevent action failure, TestCafe **automatically**[clicks](https://testcafe.io/documentation/402710/reference/test-api/testcontroller/click)`t.typeText` targets that don’t have focus. Test reports don’t count the click as a separate action. If the element doesn’t gain `:focus` from the click, the action fails.

If the `t.typeText` target is focused, TestCafe doesn’t perform the additional click action.

[](https://testcafe.io/documentation/402674/reference/test-api/testcontroller/typetext#caret-position)Caret Position[](https://testcafe.io/documentation/402674/reference/test-api/testcontroller/typetext#caret-position)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The `t.typeText` action doesn’t delete content from the target element. TestCafe places the caret after the existing content.

Specify the `caretPos` option to move the caret. To empty the target element before the action, set the `replace` option to `true`. See [Options](https://testcafe.io/documentation/402674/reference/test-api/testcontroller/typetext#options).

The following example shows how to use `t.typeText` with and without options:

```
import { Selector } from 'testcafe';

const nameInput = Selector('#developer-name');

fixture`TestController.typeText`
    .page`https://devexpress.github.io/testcafe/example/`;

test('Type and Replace', async t => {
    await t
        .typeText(nameInput, 'Peter')
        .typeText(nameInput, 'Paker', { replace: true })
        .typeText(nameInput, 'r', { caretPos: 2 })
        .expect(nameInput.value).eql('Parker');
});
```

[](https://testcafe.io/documentation/402674/reference/test-api/testcontroller/typetext#typing-into-datetime-color-and-range-inputs)Typing Into DateTime, Color, and Range Inputs[](https://testcafe.io/documentation/402674/reference/test-api/testcontroller/typetext#typing-into-datetime-color-and-range-inputs)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Some input types, such as `DateTime`, `Color`, and `Range`, only accept values of a certain format.

The following table lists common HTML5 input types and the values that they accept:

| Input type | Pattern | Example |
| --- | --- | --- |
| Date | `yyyy-mm-dd` | `'2017-12-23'` |
| Week | `yyyy-Www` | `'2017-W03'` |
| Month | `yyyy-mm` | `'2017-08'` |
| DateTime | `yyyy-mm-ddThh:mm` | `'2017-11-03T05:00'` |
| Time | `hh:mm` | `'15:30'` |
| Color | `#rrggbb` (hex) | `'#FF8040'` |
| Range | `n` | `'45'` |

The example below demonstrates the `color`, `datetime-local`, and `range` input fields:

```
import { Selector } from 'testcafe';

fixture`TestController.typeText`
    .page`./pages/index.html`;

const color    = Selector('input[type=color]');
const datetime = Selector('input[type=datetime-local]');
const range    = Selector('input[type=range]');

test('Interact with inputs', async t => {

    await t
        .typeText(color, '#FF8040')
        .typeText(datetime, '2017-11-03T05:00')
        .typeText(range, '80');
});
```

[](https://testcafe.io/documentation/402674/reference/test-api/testcontroller/typetext#select-target-elements)Select Target Elements[](https://testcafe.io/documentation/402674/reference/test-api/testcontroller/typetext#select-target-elements)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

[](https://testcafe.io/documentation/402674/reference/test-api/testcontroller/typetext#options)Options[](https://testcafe.io/documentation/402674/reference/test-api/testcontroller/typetext#options)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
{
    modifiers: {
        ctrl: Boolean,
        alt: Boolean,
        shift: Boolean,
        meta: Boolean
    },

    offsetX: Number, // Integer
    offsetY: Number, //Integer
    caretPos: Number, //Zero-based Integer
    replace: Boolean,
    paste: Boolean,
    speed: Number //Float
}
```

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| `ctrl`, `alt`, `shift`, `meta` | Boolean | Simulates modifier key presses to trigger event listeners. Does not affect the output. See the [Modifier keys](https://testcafe.io/documentation/402674/reference/test-api/testcontroller/typetext#modifier-keys) section. | `false` |
| `offsetX`, `offsetY` | Number (Integer). | The relative coordinates of the cursor during the [click action](https://testcafe.io/documentation/402674/reference/test-api/testcontroller/typetext#interaction-requirements). A positive offset value moves the cursor in relation to the top (`offsetY`) or the left (`offsetX`) border of the element. A negative offset value moves the cursor in relation to the bottom (`offsetY`) or the right (`offsetX`) border of the element. | No value. Testcafe clicks the center of the element. |
| `caretPos` | Number (Zero-based Integer) | The initial caret position. | The length of the target element content. |
| `replace` | Boolean | Set `replace` to `true` to empty the target element before the action. | `false` |
| `paste` | Boolean | Set `paste` to `true` to insert the string in one go. | `false` |
| `speed` | Number (Float) | Action emulation speed from `0.1` (the slowest) to `1` (the fastest). Overrides the [command line option](https://testcafe.io/documentation/402639/reference/command-line-interface#--speed-factor), the [Runner option](https://testcafe.io/documentation/402655/reference/testcafe-api/runner/run) and the [test-wide option](https://testcafe.io/documentation/402682/reference/test-api/testcontroller/settestspeed). | `1` |

**Example**

```
import { Selector } from 'testcafe';

const nameInput = Selector('#developer-name');

fixture `My Fixture`
    .page `http://devexpress.github.io/testcafe/example/`

test('My Test', async t => {
    await t
        .typeText(nameInput, 'Peter')
        .typeText(nameInput, 'Parker', { replace: true });
});
```

### [](https://testcafe.io/documentation/402674/reference/test-api/testcontroller/typetext#modifier-keys)Modifier keys[](https://testcafe.io/documentation/402674/reference/test-api/testcontroller/typetext#modifier-keys)

The `modifiers` option simulates key presses in order to trigger event listeners. Before the start of the action, TestCafe sets off a [`keydown`](https://developer.mozilla.org/en-US/docs/Web/API/Element/keydown_event) event with the modifier keys that you select.

[Listen](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener) for a `keydown` event to detect modifier keys.

Note

Modifier keys have no effect on the output string. For example, the shift modifier does **not** influence character case. This behavior occurs because TestCafe simulates user actions with browser scripts, and key interactions take place outside of the browser. When you press `shift` and `a` on a keyboard, your operating system substitutes the lowercase `a` for an uppercase `A`. By the time your browser registers the key press, the character is already uppercase.

**Example**

```
//TestCafe types the red string when `shift` is pressed

import { Selector } from 'testcafe';

const scriptContent = `
window.addEventListener('DOMContentLoaded', function () {
    const nameInput = document.getElementById('developer-name');
    nameInput.addEventListener('keydown', logKey);

    function logKey(e) {
        if (e.shiftKey) {
            nameInput.style.color = "red";
        }
    }
});
`;

fixture `Example`
    .page `https://devexpress.github.io/testcafe/example/`
    .clientScripts({ content: scriptContent });

test('My Test', async t => {

    const nameInput = Selector('#developer-name')
    await t
        .typeText(nameInput, 'John Doe', {
            speed: 0.1,
            modifiers: {
               shift: true 
            }
        });

});
```

### [](https://testcafe.io/documentation/402674/reference/test-api/testcontroller/typetext#paste-option)Paste option[](https://testcafe.io/documentation/402674/reference/test-api/testcontroller/typetext#paste-option)

When the option is `true`, TestCafe uses the [`Node.insertBefore()`](https://developer.mozilla.org/en-US/docs/Web/API/Node/insertBefore) JavaScript method to insert the string into the target element in one go.
