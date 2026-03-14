# Source: https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors

Title: Element Selectors | Basic Guides | Guides

URL Source: https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors

Markdown Content:
[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#article-summary)Article Summary[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#article-summary)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Element Selectors are similar in purpose to CSS Selectors. Selectors filter the DOM and return page elements that match your criteria. The following Selector returns an element with the `big-red-button` ID:

```
Selector('#big-red-button');
```

[Test actions](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions) and [assertions](https://testcafe.io/documentation/402837/guides/basic-guides/assertions) accept Selector queries as arguments:

```
await t.click(Selector('#big-red-button'));
```

You can use the [Selector Generator](https://testcafe.io/documentation/404288/guides/intermediate-guides/visual-selector-debugger) to interactively generate and debug Selector queries.

Execute _standalone_ Selector queries to [examine the page](https://testcafe.io/documentation/403654/recipes/basics/selector-recipes#examine-dom-elements-dom-node-snapshot). The following query returns the `textContent` of the `#header` element:

```
const headerText = await Selector('#header').textContent;
```

TestCafe includes three selector types.

*   Keyword-based Selectors look for elements that match the CSS Selector argument.
*   Function-based Selectors filter the DOM with a client-side function.
*   Selector-based Selectors extend other Selector queries.

Selector methods narrow down your element selection. Unlike CSS Keyword queries, Selector methods can freely traverse the DOM tree.

Users of popular front-end frameworks, such as React and Angular, can create Selectors that reference components by name.

[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#table-of-contents)Table of Contents[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#table-of-contents)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   [Introduction](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#introduction)
*   [Element Selector Basics](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#element-selector-basics)
    *   [Use Element Selectors with Actions and Assertions](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#use-element-selectors-with-actions-and-assertions)
    *   [Simple Selectors and Compound Selectors](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#simple-selectors-and-compound-selectors)

*   [How Selectors Work](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#how-selectors-work)
*   [Selector Types](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#selector-types)
*   [Keyword-Based Selectors](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#keyword-based-selectors)
    *   [Selector Keywords](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#selector-keywords)
    *   [Top Tip: Use Custom HTML Attributes](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#top-tip-use-custom-html-attributes)

*   [Function-based Selectors](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#function-based-selectors)
*   [Selector-Based Selectors](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#selector-based-selectors)
    *   [Copy and extend another Selector’s query](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#copy-and-extend-another-selectors-query)
    *   [Copy and filter another Selector’s results](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#copy-and-filter-another-selectors-results)

*   [Selector Options](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#selector-options)
    *   [boundTestRun](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#boundtestrun)
    *   [dependencies](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#dependencies)
    *   [visibilityCheck](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#visibilitycheck)
    *   [timeout](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#timeout)
    *   [Override Selector Options](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#override-selector-options)

*   [Selector Methods](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#selector-methods)
    *   [Why use Selector Methods](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#why-use-selector-methods)
    *   [Selector Method Types](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#selector-method-types)

*   [Framework-Specific Selectors](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#framework-specific-selectors)
    *   [React](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#react)
    *   [Angular](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#angular)
    *   [AngularJS](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#angularjs)
    *   [Vue](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#vue)
    *   [Aurelia](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#aurelia)

*   [Reuse Element Selectors](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#reuse-element-selectors)
*   [Selector Limitations](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#selector-limitations)
*   [Access the Shadow DOM](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#access-the-shadow-dom)
*   [Debug Selectors](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#debug-selectors)
*   [Further Reading](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#further-reading)

[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#introduction)Introduction[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#introduction)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Actions](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions) and [assertions](https://testcafe.io/documentation/402837/guides/basic-guides/assertions) use Selector query arguments to locate their targets:

```
t.click('#big-red-button');
```

The `t.click` action targets the result of the `#big-red-button` Selector query. This query matches elements with the `big-red-button` ID.

[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#element-selector-basics)Element Selector Basics[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#element-selector-basics)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Selector queries begin with an invocation of the `Selector()` constructor. Constructor _arguments_ determine the initial results of the Selector query.

```
Selector(/*arguments go here*/);
```

There are [three ways](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#selector-types) to initialize a Selector. The most common way is to use a [CSS Keyword](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#keyword-based-selectors):

```
Selector('button');
```

The Selector above returns all the `button` elements on the page.

After you initialize a Selector, you can perform additional actions with the results of the query. Append [Selector methods](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#selector-methods) to the constructor:

```
Selector('button').withText('click me');
```

The `withText` method helped you narrow down the results. The query above only matches `button` elements with the “click me” label.

### [](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#use-element-selectors-with-actions-and-assertions)Use Element Selectors with Actions and Assertions[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#use-element-selectors-with-actions-and-assertions)

[Actions](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions) and [assertions](https://testcafe.io/documentation/402837/guides/basic-guides/assertions) use Selector queries to identify their targets.

You can pass any valid Selector query to an action or an assertion:

```
t.click(Selector('#big-red-button'));
```

If your Selector query does not include [methods](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#selector-methods), you can omit the `Selector` keyword:

```
t.click('#big-red-button');
```

### [](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#simple-selectors-and-compound-selectors)Simple Selectors and Compound Selectors[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#simple-selectors-and-compound-selectors)

**Simple** Selectors filter the DOM once:

```
Selector('#big-red-button');
```

**Compound** Selectors filter the DOM multiple times:

```
Selector('nav .button');
// or 
Selector('nav').find('.button')
```

The example above matches `button` class elements that reside inside `nav` blocks.

[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#how-selectors-work)How Selectors Work[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#how-selectors-work)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Selectors are asynchronous.

TestCafe executes Selector queries when it encounters them in actions and assertions.

Element selectors can return multiple items. The [selector.count](https://testcafe.io/documentation/402755/reference/test-api/selector/count) property indicates the number of page elements that match the query.

If a page action / assertion Selector matches multiple DOM elements, TestCafe performs the action / assertion with the first matching element.

If a Selector query yields zero matches, its return value is **null**. If a test action uses this Selector, the test fails. If you pass such a Selector to an assertion that expects a non-null return value, the test fails, too:

```
await t.expect(Selector('.holyGrail').count).eql(1)
.expect(Selector('.holyGrail').exists).ok()
```

If you save a Selector query to a variable, TestCafe only executes the query when you call or [await](https://testcafe.io/documentation/402670/reference/test-api/domnodestate) that variable.

The example below contains three identical actions. Yet, since every action changes the DOM, each call of the `buttons` variable yields a different result.

```
test('Click a button', async t => {
    const buttons = Selector('button').withText("A button number");

    await t
        .click(buttons.nth(0))
        .click(buttons.nth(0))
        .click(buttons.nth(0))
});
```

```
<html>
    <body>
        <div>
        <button onclick= "this.textContent= 'Pressed';">A button number 1</button>
        <button onclick= "this.textContent= 'Pressed';">A button number 2</button>
        <button onclick= "this.textContent= 'Pressed';">A button number 3</button>
        </div>
    </body>
</html>
```

[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#selector-types)Selector Types[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#selector-types)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   [Keyword-Based Selectors](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#keyword-based-selectors) filter the page in search of elements that match a CSS Selector.
*   [Function-Based Selectors](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#function-based-selectors) execute a client-side function that traverses the DOM.
*   [Selector-Based Selectors](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#function-based-selectors) execute, or filter the results of, another Selector query.

Additional libraries enable the use of [Framework-Specific Selectors](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#framework-specific-selectors).

[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#keyword-based-selectors)Keyword-Based Selectors[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#keyword-based-selectors)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Keyword-Based Selectors filter the page in search of elements that match [CSS keywords](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#selector-keywords).

```
Selector('#some-element');
```

A few examples:

*   `body` matches the `body` element.
*   `.login` matches elements with the `login` class name.
*   `#input` matches the first element with the `input` ID.

### [](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#selector-keywords)Selector Keywords[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#selector-keywords)

TestCafe Selector keywords are syntactically identical to [CSS Selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors).

### [](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#top-tip-use-custom-html-attributes)Top Tip: Use Custom HTML Attributes[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#top-tip-use-custom-html-attributes)

Keywords that reference custom HTML attributes are more reliable, because they don’t reference mutable code.

*   **Selectors break** when you _change_ the page code that they reference.
*   **Bad Selectors** reference class names or DOM relationships – things that change fairly often during development.
*   **Reliable Selectors** reference properties that are independent of page design and layout.

Mark your actions’ targets with custom HTML attributes, and write better, more reliable Selectors.

1.   Add a custom HTML attribute (for example: `data-test-id`) to all the page elements that your test interacts with.
2.   Reference your attribute when you write Selector queries:

```
t.click('button').withAttribute('data-test-id','left-button') // or
t.click('[data-test-id="left-button"]')
```

[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#function-based-selectors)Function-based Selectors[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#function-based-selectors)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Function-based Selectors execute a client-side function that traverses the DOM and returns one of the following objects:

*   A DOM node
*   An array of DOM nodes
*   A `NodeList` object
*   An `HTMLCollection` object
*   A `null` object
*   An `undefined` object

The function-based Selector below retrieves a string from `localStorage` and finds a DOM element with the identical ID:

```
const element = Selector(() => {
    const storedElementId = window.localStorage.storedElementId;
    return document.getElementById(storedElementId);
});
```

Function-based Selectors can have additional parameters:

```
const elementWithId = Selector(id => {
    return document.getElementById(id);
});

await t.click(elementWithId('buy'));
```

[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#selector-based-selectors)Selector-Based Selectors[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#selector-based-selectors)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can create Selectors based on other Selectors. This is an easy way to extend existing Selector queries or filter their results.

### [](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#copy-and-extend-another-selectors-query)Copy and extend another Selector’s query[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#copy-and-extend-another-selectors-query)

You can create a new Selector based on another Selector’s query.

The example code below saves a simple Selector query to the `parent` variable. It then declares a `child` variable that adds the `find` method to the original Selector.

```
const parent = Selector('div'); // filters the DOM
const child = parent.find('button'); // inherits the "parent" query, modifies it, and filters the DOM again
```

Note that the `child` Selector does not inherit the return value of the `parent` Selector.

You can also nest Selectors. If you pass Selector A to Selector B as an argument, Selector B inherits Selector A’s query. This is an easy way to create a Selector copy with modified options.

The example below saves a simple Selector query to the `ctaButton` variable and passes it to another Selector. As a result, the second Selector inherits the first Selector’s _query_. However, since the second Selector enables the `visibilityCheck` option, it only matches _visible_ elements.

```
const ctaButton = Selector('.cta-button'); // 
Selector(ctaButton, { visibilityCheck: true });
```

You can even pass arguments to Selectors within Selectors:

```
const elementWithIdOrClassName = Selector(value => {
    return document.getElementById(value) || document.getElementsByClassName(value);
});
const submitButton = Selector(elementWithIdOrClassName('main-element'));
```

### [](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#copy-and-filter-another-selectors-results)Copy and filter another Selector’s results[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#copy-and-filter-another-selectors-results)

You can create a new Selector based on another Selector’s return value.

If you want to copy the query’s **return value**, you need to asynchronously execute the query. Asynchronous Selector calls return a [DOM Node State](https://testcafe.io/documentation/402670/reference/test-api/domnodestate) object that contains the query’s results. If you pass this object to another Selector, you can filter the original Selector’s results.

In the example below, the `visibleTopMenu` Selector filters the return value of the `topMenuSnapshot` Selector. Since it contains an additional `visibilityCheck` option, it only returns visible elements.

```
const topMenuSnapshot = await Selector('#top-menu')(); // TestCafe executes this query asynchronously, filters the DOM and returns a DOMNodeState object.
const visibleTopMenu = Selector(topMenuSnapshot, { visibilityCheck: true }); // TestCafe doesn't filter the DOM. It only filters the results of the topMenuSnapshot query
```

[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#selector-options)Selector Options[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#selector-options)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

> Main article: [Selector Constructor](https://testcafe.io/documentation/402756/reference/test-api/selector/constructor#options).

Use constructor options to customize Selector behavior.

### [](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#boundtestrun)boundTestRun[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#boundtestrun)

The `boundTestRun` option binds the `TestController` object to a Node.js callback. This is necessary to execute Selectors inside the callback function.

### [](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#dependencies)dependencies[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#dependencies)

Use the `dependencies` option to share data with a Selector function.

### [](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#visibilitycheck)visibilityCheck[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#visibilitycheck)

If the `visibilityCheck` option is `true`, TestCafe imposes a visibility requirement on Selector targets.

TestCafe does not interact with invisible elements.

If the element or one of its parents meets the following criteria, TestCafe considers the element to be **invisible**.

*   The value of the element’s `display` property is `none`
*   The value of the element’s `visibility` property is `hidden` or `collapse`
*   The element has a `width` or `height` of `0`.

Elements that do not meet these criteria may still be invisible to the user. The following factors **do not** influence the element’s visibility status:

*   The element’s `z-index`
*   The element’s `opacity`
*   The element’s position on the page

### [](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#timeout)timeout[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#timeout)

When TestCafe runs tests, it automatically waits for action targets to appear and [become visible](https://testcafe.io/documentation/402751/reference/test-api/selector/filtervisible#visibility-criteria). The value of the _element selector timeout_ variable defines the maximum waiting time. If a _visible_ DOM element that matches a Selector query does not appear on the page within the _element selector timeout_, the test fails.

Use the [timeout](https://testcafe.io/documentation/402756/reference/test-api/selector/constructor#optionstimeout) Selector option to specify a custom selector timeout.

Selector timeouts have no effect on [Selector.exists](https://testcafe.io/documentation/402754/reference/test-api/selector/exists) and [Selector.count](https://testcafe.io/documentation/402755/reference/test-api/selector/count) properties. TestCafe calculates their values immediately. If you want to evaluate these properties in an assertion, set a custom [assertion timeout](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#assertion-timeout).

```
await t.expect(Selector('#elementId', { timeout: 500 }).innerText).eql('text', 'check element text');
```

See [Automatic Waiting](https://docs.devexpress.com/TestCafeStudio/400177/basic-guides/run-tests?v=2.0) for more information.

### [](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#override-selector-options)Override Selector Options[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#override-selector-options)

Use the [with](https://testcafe.io/documentation/402743/reference/test-api/selector/with) method to override the [options](https://testcafe.io/documentation/402743/reference/test-api/selector/with#options) of another Selector.

```
import { Selector } from 'testcafe';

const elementWithId = Selector(id => document.getElementById(id));

fixture `My fixture`
    .page `http://www.example.com/`;

test('My Test', async t => {
    const visibleElementWithId = elementWithId.with({
        visibilityCheck: true
    });

    const visibleButton = await visibleElementWithId('submit-button');
});
```

[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#selector-methods)Selector Methods[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#selector-methods)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Selector methods perform additional actions with the return value of the main Selector query. Selector methods narrow, expand, or otherwise modify the selection of page elements.

```
Selector('keyword1 keyword2').method1().method2();
```

### [](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#why-use-selector-methods)Why use Selector Methods[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#why-use-selector-methods)

Keyword-based Selectors have limited capabilities.

Complex [keyword-based Selectors](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#keyword-based-selectors) are long and difficult to maintain:

```
await t.click('div > .my-class > div:nth-child(2) > span > a[href="https://my-site.com/page"]');
```

CSS selectors cannot query parent elements:

```
<html>
    <body>
        <!-- ... -->
                    <div>
                        <!-- you cannot query this div by its child's ID -->
                        <div>
                            <div id="query-my-parent"></div>
                        </div>
                    </div>
        <!-- ... -->
    </body>
</html>
```

Selector methods can overcome these limitations and freely traverse the DOM tree:

```
const link = Selector('div')
    .child('.my-class')
    .child('div')
    .nth(2)
    .child('span')
    .child('a')
    .withAttribute('href', 'https://my-site.com/page');

const parent = Selector('#query-my-parent').parent();
```

### [](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#selector-method-types)Selector Method Types[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#selector-method-types)

*   [Filter methods](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#filter-methods) filter the page element selection.
*   [Related Element Lookup methods](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#related-element-lookup-methods) look for page elements related to the existing element selection.

### [](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#filter-methods)Filter Methods[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#filter-methods)

Filter methods filter the page element selection.

| Method | Description |
| --- | --- |
| [nth](https://testcafe.io/documentation/402748/reference/test-api/selector/nth) | Finds the element with the specified _index_. The index starts at 0. Negative index values indicate the element’s location relative to the final element of the array. |
| [withText](https://testcafe.io/documentation/402740/reference/test-api/selector/withtext) | Finds elements with a `textContent` value that _contains_ the specified case-sensitive string or matches the regular expression. |
| [withExactText](https://testcafe.io/documentation/402741/reference/test-api/selector/withexacttext) | Finds elements with a `textContent` value equal to the specified string (case-sensitive). |
| [withAttribute](https://testcafe.io/documentation/402742/reference/test-api/selector/withattribute) | Finds elements with the specified attribute or attribute value. |
| [filterVisible](https://testcafe.io/documentation/402751/reference/test-api/selector/filtervisible) | Finds visible elements. |
| [filterHidden](https://testcafe.io/documentation/402752/reference/test-api/selector/filterhidden) | Finds hidden elements. |
| [filter](https://testcafe.io/documentation/402753/reference/test-api/selector/filter) | Finds elements that match a CSS selector, or meet the conditions of a filter function. |

Related element lookup methods find elements related to the existing element selection.

| Method | Description |
| --- | --- |
| [find](https://testcafe.io/documentation/402750/reference/test-api/selector/find) | Returns an array of descendant nodes that match a CSS Selector, or meet the conditions of a filter function. |
| [parent](https://testcafe.io/documentation/402747/reference/test-api/selector/parent) | Returns an array of parent elements. |
| [child](https://testcafe.io/documentation/402757/reference/test-api/selector/child) | Returns an array of child elements. |
| [sibling](https://testcafe.io/documentation/402744/reference/test-api/selector/sibling) | Returns an array of sibling elements. |
| [nextSibling](https://testcafe.io/documentation/402749/reference/test-api/selector/nextsibling) | Returns an array of succeeding sibling elements. |
| [prevSibling](https://testcafe.io/documentation/402746/reference/test-api/selector/prevsibling) | Returns an array of preceding sibling elements. |
| [shadowRoot](https://testcafe.io/documentation/402745/reference/test-api/selector/shadowroot) | Returns the **shadow root** node. |

[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#framework-specific-selectors)Framework-Specific Selectors[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#framework-specific-selectors)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Users of popular front-end frameworks can simplify their Selectors with the help of special TestCafe plugins.

For instance, users that install the [testcafe-react-selectors](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#react) plugin can reference the React component tree.

Note

Front-end development tools (such as React DevTools or Vue DevTools) can interfere with TestCafe and cause errors. Do not open them when you run or debug TestCafe tests.

### [](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#react)React[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#react)

Install the [testcafe-react-selectors](https://github.com/DevExpress/testcafe-react-selectors) npm package.

Import the `ReactSelector` method to reference React components by name.

For more information, refer to the [official plugin documentation](https://github.com/DevExpress/testcafe-react-selectors/blob/master/README.md).

```
import { ReactSelector } from 'testcafe-react-selectors';
const reactComponent      = ReactSelector('MyComponent');
const reactComponentState = await reactComponent.getReact();

// >> reactComponentState
//
// {
//     props:    <component_props>,
//     state:    <component_state>
// }
```

### [](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#angular)Angular[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#angular)

Install the [testcafe-angular-selectors](https://github.com/DevExpress/testcafe-angular-selectors) npm package.

Import the `AngularSelector` method to reference Angular components by name. Call the method without parameters to obtain the project’s root element.

For more information, refer to the [official plugin documentation](https://github.com/DevExpress/testcafe-angular-selectors/blob/master/angular-selector.md).

```
import { AngularSelector } from 'testcafe-angular-selectors';

const rootAngular       = AngularSelector();
const list        = AngularSelector('list');
const listAngular = await list.getAngular();

await t.expect(listAngular.testProp).eql(1);
```

### [](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#angularjs)AngularJS[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#angularjs)

Install the [testcafe-angular-selectors](https://github.com/DevExpress/testcafe-angular-selectors) npm package. Import the `AngularJSSelector` method to look for DOM elements by their Angular binding.

For more information, refer to the [official plugin documentation](https://github.com/DevExpress/testcafe-angular-selectors/blob/master/angularJS-selector.md).

```
import { AngularJSSelector } from 'testcafe-angular-selectors';
import { Selector } from 'testcafe';

fixture `TestFixture`
    .page('http://todomvc.com/examples/angularjs/');

test('add new item', async t => {
    await t
        .typeText(AngularJSSelector.byModel('newTodo'), 'new item')
        .pressKey('enter')
        .expect(Selector('#todo-list').visible).ok();
});
```

### [](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#vue)Vue[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#vue)

Install the [testcafe-vue-selectors](https://github.com/DevExpress/testcafe-vue-selectors) npm package.

Import the `VueSelector` method to reference Vue components by name.

For more information, refer to the [official plugin documentation](https://github.com/DevExpress/testcafe-vue-selectors/blob/master/README.md).

```
import VueSelector from 'testcafe-vue-selectors';

const rootVue   = VueSelector();
const vueComponent      = VueSelector('componentTag');
const vueComponentState = await vueComponent.getVue();

// >> vueComponentState
//
// {
//     props:    <component_props>,
//     state:    <component_state>,
//     computed: <component_computed>
// }
```

### [](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#aurelia)Aurelia[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#aurelia)

Install the [testcafe-aurelia-selectors](https://github.com/DevExpress/testcafe-aurelia-selectors) plugin.

Import the `AureliaSelector` method to look for elements by their Aurelia binding.

For more information, refer to the [official plugin documentation](https://github.com/DevExpress/testcafe-aurelia-selectors/blob/master/README.md).

```
import AureliaSelector from 'testcafe-aurelia-selectors';

fixture `TestFixture`
    .page('http://todomvc.com/examples/aurelia/');

test('add new item', async t => {
    await t
        .typeText(AureliaSelector.byValueBind('newTodoTitle'), 'new item')
        .pressKey('enter')
        .expect(AureliaSelector.byShowBind('items.length').exists).ok();
});
```

[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#reuse-element-selectors)Reuse Element Selectors[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#reuse-element-selectors)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Tests that repeat identical Selector queries are slower and harder to maintain. You can reuse Selectors in one of the two ways:

Assign the value of a Selector query to a constant, and use that constant later in code. Every time you invoke this constant, you execute the Selector query anew.

```
const myBeautifulSelector = Selector('div').withText('hello world'); // does not execute the query
<…>
await t.click(myBeautifulSelector); // executes the query
```

Selector queries take time to resolve. Await the Selector to execute the query once and only re-use its [return value](https://testcafe.io/documentation/402670/reference/test-api/domnodestate).

```
const myBeautifulSelector = await Selector('div').withText('hello world'); // executes the query
<…>
await t.click(myBeautifulSelector); // uses the query result from before
```

[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#selector-limitations)Selector Limitations[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#selector-limitations)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   Selector queries cannot access user variables outside of their scope. If a Selector query needs to access a variable, pass that variable through the [dependency](https://testcafe.io/documentation/402756/reference/test-api/selector/constructor#optionsdependencies) option.
*   Keyword-based Selectors and Selector-based Selectors do not accept custom arguments. Use the [dependencies](https://testcafe.io/documentation/402756/reference/test-api/selector/constructor#optionsdependencies) option to pass additional data to a Selector query.
*   [Function-based Selectors](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#function-based-selectors) can not contain generators or `async/await` keywords.
*   Selector [dependencies](https://testcafe.io/documentation/402789/reference/test-api/clientfunction/constructor#optionsdependencies) do not support property shorthands.

[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#access-the-shadow-dom)Access the Shadow DOM[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#access-the-shadow-dom)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Important

When TestCafe uses [native automation](https://testcafe.io/documentation/404237/guides/intermediate-guides/native-automation-mode) to interact with the Shadow DOM, the mouse cursor is not visible.

You cannot access Shadow DOM elements directly. To interact with the Shadow DOM, [identify](https://testcafe.io/documentation/402745/reference/test-api/selector/shadowroot) the root node of a shadow tree, and use other Selector methods to traverse it.

Tip

**Reuse** shadowRoot Selector queries for greater convenience.

Warning

You cannot perform actions with the `shadowRoot()` element, or use it in assertions. Use this element as the shadow DOM entry point.

The following example returns the `<p>` element from the shadow DOM:

```
import { Selector } from 'testcafe';

fixture`Selector.shadowRoot`
    .page`https://devexpress.github.io/testcafe/example/`;

test('Get text within shadow tree', async t => {
    const shadowRoot = Selector('div').withAttribute('id', 'shadow-host').shadowRoot();
    const paragraph  = shadowRoot.child('p');

    await t.expect(paragraph.textContent).eql('This paragraph is in the shadow tree');

    try {
        await t.click(shadowRoot);
        // causes an error
        // do not target the shadow root directly or use it in assertions
    }
    catch (error) {
        await t.expect(error.code).eql('E27');
    }
});
```

[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#debug-selectors)Debug Selectors[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#debug-selectors)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

> Main article: [Debug Tests](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests)

If a Selector or a [Selector method](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#selector-methods) does not match any DOM elements, the test fails and TestCafe throws an error.

If you chain multiple Selector methods together, TestCafe stops Selector execution after the first unsuccessful Selector method.

![Image 1: Selector Error Screenshot](https://testcafe.io/images/selector-error.png)

Use the [Visual Selector Debugger](https://testcafe.io/documentation/404288/guides/intermediate-guides/visual-selector-debugger) to debug failing Selector queries.

![Image 2: Enter a Selector query](https://testcafe.io/images/inspector/enter-query.gif)

[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#further-reading)Further Reading[](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#further-reading)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Read the [Best Practices](https://testcafe.io/documentation/402836/guides/best-practices/best-practices) guide for more information on Selector best practices.

The [Advanced Selector Techniques](https://testcafe.io/documentation/403655/guides/advanced-guides/advanced-selector-techniques) guide describes the following advanced Selector techniques:

*   [Extend the Selector class with Custom Properties and Methods](https://testcafe.io/documentation/403655/guides/advanced-guides/advanced-selector-techniques#extend-the-selector-class)
*   [Execute Selectors inside Node.JS Callbacks](https://testcafe.io/documentation/403655/guides/advanced-guides/advanced-selector-techniques#execute-selectors-inside-nodejs-callbacks)
*   [Select Elements with Dynamic IDs](https://testcafe.io/documentation/403655/guides/advanced-guides/advanced-selector-techniques#select-elements-with-dynamic-ids)

The [Selector Recipes](https://testcafe.io/documentation/403654/recipes/basics/selector-recipes) page features additional Selector code examples.
