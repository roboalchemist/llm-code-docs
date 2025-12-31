# Source: https://playwright.dev/docs/test-assertions

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Guides]
-   [Assertions]

On this page

<div>

# Assertions

</div>

## Introduction[​](#introduction "Direct link to Introduction") 

Playwright includes test assertions in the form of `expect` function. To make an assertion, call `expect(value)` and choose a matcher that reflects the expectation. There are many [generic matchers](/docs/api/class-genericassertions) like `toEqual`, `toContain`, `toBeTruthy` that can be used to assert any conditions.

``` 
expect(success).toBeTruthy();
```

Playwright also includes web-specific [async matchers](/docs/api/class-locatorassertions) that will wait until the expected condition is met. Consider the following example:

``` 
await expect(page.getByTestId('status')).toHaveText('Submitted');
```

Playwright will be re-testing the element with the test id of `status` until the fetched element has the `"Submitted"` text. It will re-fetch the element and check it over and over, until the condition is met or until the timeout is reached. You can either pass this timeout or configure it once via the [testConfig.expect](/docs/api/class-testconfig#test-config-expect) value in the test config.

By default, the timeout for assertions is set to 5 seconds. Learn more about [various timeouts](/docs/test-timeouts).

## Auto-retrying assertions[​](#auto-retrying-assertions "Direct link to Auto-retrying assertions") 

The following assertions will retry until the assertion passes, or the assertion timeout is reached. Note that retrying assertions are async, so you must `await` them.

Assertion

Description

[await expect(locator).toBeAttached()](/docs/api/class-locatorassertions#locator-assertions-to-be-attached)

Element is attached

[await expect(locator).toBeChecked()](/docs/api/class-locatorassertions#locator-assertions-to-be-checked)

Checkbox is checked

[await expect(locator).toBeDisabled()](/docs/api/class-locatorassertions#locator-assertions-to-be-disabled)

Element is disabled

[await expect(locator).toBeEditable()](/docs/api/class-locatorassertions#locator-assertions-to-be-editable)

Element is editable

[await expect(locator).toBeEmpty()](/docs/api/class-locatorassertions#locator-assertions-to-be-empty)

Container is empty

[await expect(locator).toBeEnabled()](/docs/api/class-locatorassertions#locator-assertions-to-be-enabled)

Element is enabled

[await expect(locator).toBeFocused()](/docs/api/class-locatorassertions#locator-assertions-to-be-focused)

Element is focused

[await expect(locator).toBeHidden()](/docs/api/class-locatorassertions#locator-assertions-to-be-hidden)

Element is not visible

[await expect(locator).toBeInViewport()](/docs/api/class-locatorassertions#locator-assertions-to-be-in-viewport)

Element intersects viewport

[await expect(locator).toBeVisible()](/docs/api/class-locatorassertions#locator-assertions-to-be-visible)

Element is visible

[await expect(locator).toContainText()](/docs/api/class-locatorassertions#locator-assertions-to-contain-text)

Element contains text

[await expect(locator).toContainClass()](/docs/api/class-locatorassertions#locator-assertions-to-contain-class)

Element has specified CSS classes

[await expect(locator).toHaveAccessibleDescription()](/docs/api/class-locatorassertions#locator-assertions-to-have-accessible-description)

Element has a matching [accessible description](https://w3c.github.io/accname/#dfn-accessible-description)

[await expect(locator).toHaveAccessibleName()](/docs/api/class-locatorassertions#locator-assertions-to-have-accessible-name)

Element has a matching [accessible name](https://w3c.github.io/accname/#dfn-accessible-name)

[await expect(locator).toHaveAttribute()](/docs/api/class-locatorassertions#locator-assertions-to-have-attribute)

Element has a DOM attribute

[await expect(locator).toHaveClass()](/docs/api/class-locatorassertions#locator-assertions-to-have-class)

Element has specified CSS class property

[await expect(locator).toHaveCount()](/docs/api/class-locatorassertions#locator-assertions-to-have-count)

List has exact number of children

[await expect(locator).toHaveCSS()](/docs/api/class-locatorassertions#locator-assertions-to-have-css)

Element has CSS property

[await expect(locator).toHaveId()](/docs/api/class-locatorassertions#locator-assertions-to-have-id)

Element has an ID

[await expect(locator).toHaveJSProperty()](/docs/api/class-locatorassertions#locator-assertions-to-have-js-property)

Element has a JavaScript property

[await expect(locator).toHaveRole()](/docs/api/class-locatorassertions#locator-assertions-to-have-role)

Element has a specific [ARIA role](https://www.w3.org/TR/wai-aria-1.2/#roles)

[await expect(locator).toHaveScreenshot()](/docs/api/class-locatorassertions#locator-assertions-to-have-screenshot-1)

Element has a screenshot

[await expect(locator).toHaveText()](/docs/api/class-locatorassertions#locator-assertions-to-have-text)

Element matches text

[await expect(locator).toHaveValue()](/docs/api/class-locatorassertions#locator-assertions-to-have-value)

Input has a value

[await expect(locator).toHaveValues()](/docs/api/class-locatorassertions#locator-assertions-to-have-values)

Select has options selected

[await expect(locator).toMatchAriaSnapshot()](/docs/api/class-locatorassertions#locator-assertions-to-match-aria-snapshot)

Element matches the Aria snapshot

[await expect(page).toHaveScreenshot()](/docs/api/class-pageassertions#page-assertions-to-have-screenshot-1)

Page has a screenshot

[await expect(page).toHaveTitle()](/docs/api/class-pageassertions#page-assertions-to-have-title)

Page has a title

[await expect(page).toHaveURL()](/docs/api/class-pageassertions#page-assertions-to-have-url)

Page has a URL

[await expect(response).toBeOK()](/docs/api/class-apiresponseassertions#api-response-assertions-to-be-ok)

Response has an OK status

## Non-retrying assertions[​](#non-retrying-assertions "Direct link to Non-retrying assertions") 

These assertions allow to test any conditions, but do not auto-retry. Most of the time, web pages show information asynchronously, and using non-retrying assertions can lead to a flaky test.

Prefer [auto-retrying](#auto-retrying-assertions) assertions whenever possible. For more complex assertions that need to be retried, use [`expect.poll`](#expectpoll) or [`expect.toPass`](#expecttopass).

Assertion

Description

[expect(value).toBe()](/docs/api/class-genericassertions#generic-assertions-to-be)

Value is the same

[expect(value).toBeCloseTo()](/docs/api/class-genericassertions#generic-assertions-to-be-close-to)

Number is approximately equal

[expect(value).toBeDefined()](/docs/api/class-genericassertions#generic-assertions-to-be-defined)

Value is not `undefined`

[expect(value).toBeFalsy()](/docs/api/class-genericassertions#generic-assertions-to-be-falsy)

Value is falsy, e.g. `false`, `0`, `null`, etc.

[expect(value).toBeGreaterThan()](/docs/api/class-genericassertions#generic-assertions-to-be-greater-than)

Number is more than

[expect(value).toBeGreaterThanOrEqual()](/docs/api/class-genericassertions#generic-assertions-to-be-greater-than-or-equal)

Number is more than or equal

[expect(value).toBeInstanceOf()](/docs/api/class-genericassertions#generic-assertions-to-be-instance-of)

Object is an instance of a class

[expect(value).toBeLessThan()](/docs/api/class-genericassertions#generic-assertions-to-be-less-than)

Number is less than

[expect(value).toBeLessThanOrEqual()](/docs/api/class-genericassertions#generic-assertions-to-be-less-than-or-equal)

Number is less than or equal

[expect(value).toBeNaN()](/docs/api/class-genericassertions#generic-assertions-to-be-na-n)

Value is `NaN`

[expect(value).toBeNull()](/docs/api/class-genericassertions#generic-assertions-to-be-null)

Value is `null`

[expect(value).toBeTruthy()](/docs/api/class-genericassertions#generic-assertions-to-be-truthy)

Value is truthy, i.e. not `false`, `0`, `null`, etc.

[expect(value).toBeUndefined()](/docs/api/class-genericassertions#generic-assertions-to-be-undefined)

Value is `undefined`

[expect(value).toContain()](/docs/api/class-genericassertions#generic-assertions-to-contain-1)

String contains a substring

[expect(value).toContain()](/docs/api/class-genericassertions#generic-assertions-to-contain-2)

Array or set contains an element

[expect(value).toContainEqual()](/docs/api/class-genericassertions#generic-assertions-to-contain-equal)

Array or set contains a similar element

[expect(value).toEqual()](/docs/api/class-genericassertions#generic-assertions-to-equal)

Value is similar - deep equality and pattern matching

[expect(value).toHaveLength()](/docs/api/class-genericassertions#generic-assertions-to-have-length)

Array or string has length

[expect(value).toHaveProperty()](/docs/api/class-genericassertions#generic-assertions-to-have-property)

Object has a property

[expect(value).toMatch()](/docs/api/class-genericassertions#generic-assertions-to-match)

String matches a regular expression

[expect(value).toMatchObject()](/docs/api/class-genericassertions#generic-assertions-to-match-object)

Object contains specified properties

[expect(value).toStrictEqual()](/docs/api/class-genericassertions#generic-assertions-to-strict-equal)

Value is similar, including property types

[expect(value).toThrow()](/docs/api/class-genericassertions#generic-assertions-to-throw)

Function throws an error

## Asymmetric matchers[​](#asymmetric-matchers "Direct link to Asymmetric matchers") 

These expressions can be nested in other assertions to allow more relaxed matching against a given condition.

Matcher

Description

[expect.any()](/docs/api/class-genericassertions#generic-assertions-any)

Matches any instance of a class/primitive

[expect.anything()](/docs/api/class-genericassertions#generic-assertions-anything)

Matches anything

[expect.arrayContaining()](/docs/api/class-genericassertions#generic-assertions-array-containing)

Array contains specific elements

[expect.arrayOf()](/docs/api/class-genericassertions#generic-assertions-array-of)

Array contains elements of specific type

[expect.closeTo()](/docs/api/class-genericassertions#generic-assertions-close-to)

Number is approximately equal

[expect.objectContaining()](/docs/api/class-genericassertions#generic-assertions-object-containing)

Object contains specific properties

[expect.stringContaining()](/docs/api/class-genericassertions#generic-assertions-string-containing)

String contains a substring

[expect.stringMatching()](/docs/api/class-genericassertions#generic-assertions-string-matching)

String matches a regular expression

## Negating matchers[​](#negating-matchers "Direct link to Negating matchers") 

In general, we can expect the opposite to be true by adding a `.not` to the front of the matchers:

``` 
expect(value).not.toEqual(0);
await expect(locator).not.toContainText('some text');
```

## Soft assertions[​](#soft-assertions "Direct link to Soft assertions") 

By default, failed assertion will terminate test execution. Playwright also supports *soft assertions*: failed soft assertions **do not** terminate test execution, but mark the test as failed.

``` 
// Make a few checks that will not stop the test when failed...
await expect.soft(page.getByTestId('status')).toHaveText('Success');
await expect.soft(page.getByTestId('eta')).toHaveText('1 day');

// ... and continue the test to check more things.
await page.getByRole('link', ).click();
await expect.soft(page.getByRole('heading', )).toBeVisible();
```

At any point during test execution, you can check whether there were any soft assertion failures:

``` 
// Make a few checks that will not stop the test when failed...
await expect.soft(page.getByTestId('status')).toHaveText('Success');
await expect.soft(page.getByTestId('eta')).toHaveText('1 day');

// Avoid running further if there were soft assertion failures.
expect(test.info().errors).toHaveLength(0);
```

Note that soft assertions only work with Playwright test runner.

## Custom expect message[​](#custom-expect-message "Direct link to Custom expect message") 

You can specify a custom expect message as a second argument to the `expect` function, for example:

``` 
await expect(page.getByText('Name'), 'should be logged in').toBeVisible();
```

This message will be shown in reporters, both for passing and failing expects, providing more context about the assertion.

When expect passes, you might see a successful step like this:

``` 
✅ should be logged in    @example.spec.ts:18
```

When expect fails, the error would look like this:

``` 
    Error: should be logged in

    Call log:
      - expect.toBeVisible with timeout 5000ms
      - waiting for "getByText('Name')"

      2 |
      3 | test('example test', async() => );
      6 |
```

Soft assertions also support custom message:

``` 
expect.soft(value, 'my soft assertion').toBe(56);
```

## expect.configure[​](#expectconfigure "Direct link to expect.configure") 

You can create your own pre-configured `expect` instance to have its own defaults such as `timeout` and `soft`.

``` 
const slowExpect = expect.configure();
await slowExpect(locator).toHaveText('Submit');

// Always do soft assertions.
const softExpect = expect.configure();
await softExpect(locator).toHaveText('Submit');
```

## expect.poll[​](#expectpoll "Direct link to expect.poll") 

You can convert any synchronous `expect` to an asynchronous polling one using `expect.poll`.

The following method will poll given function until it returns HTTP status 200:

``` 
await expect.poll(async () => , ).toBe(200);
```

You can also specify custom polling intervals:

``` 
await expect.poll(async () => , ).toBe(200);
```

You can combine `expect.configure()` with expect.poll to perform soft assertions in polling logic.

``` 
const softExpect = expect.configure();
await softExpect.poll(async () => , ).toBe(200);
```

This allows the test to continue even if the assertion inside poll fails.

## expect.toPass[​](#expecttopass "Direct link to expect.toPass") 

You can retry blocks of code until they are passing successfully.

``` 
await expect(async () => ).toPass();
```

You can also specify custom timeout and retry intervals:

``` 
await expect(async () => ).toPass();
```

Note that by default `toPass` has timeout 0 and does not respect custom [expect timeout](/docs/test-timeouts#expect-timeout).

## Add custom matchers using expect.extend[​](#add-custom-matchers-using-expectextend "Direct link to Add custom matchers using expect.extend") 

You can extend Playwright assertions by providing custom matchers. These matchers will be available on the `expect` object.

In this example we add a custom `toHaveAmount` function. Custom matcher should return a `pass` flag indicating whether the assertion passed, and a `message` callback that\'s used when the assertion fails.

fixtures.ts

``` 
import  from '@playwright/test';
import type  from '@playwright/test';

export  from '@playwright/test';

export const expect = baseExpect.extend()  catch (e: any) 

    if (this.isNot) 

    const message = pass
      ? () => this.utils.matcherHint(assertionName, undefined, undefined, ) +
          '\n\n' +
          `Locator: $\n` +
          `Expected: not $\n` +
          (matcherResult ? `Received: $` : '')
      : () =>  this.utils.matcherHint(assertionName, undefined, undefined, ) +
          '\n\n' +
          `Locator: $\n` +
          `Expected: $\n` +
          (matcherResult ? `Received: $` : '');

    return ;
  },
});
```

Now we can use `toHaveAmount` in the test.

example.spec.ts

``` 
import  from './fixtures';

test('amount', async () => );
```

### Compatibility with expect library[​](#compatibility-with-expect-library "Direct link to Compatibility with expect library") 

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

Do not confuse Playwright\'s `expect` with the [`expect` library](https://jestjs.io/docs/expect). The latter is not fully integrated with Playwright test runner, so make sure to use Playwright\'s own `expect`.

### Combine custom matchers from multiple modules[​](#combine-custom-matchers-from-multiple-modules "Direct link to Combine custom matchers from multiple modules") 

You can combine custom matchers from multiple files or modules.

fixtures.ts

``` 
import  from '@playwright/test';
import  from 'database-test-utils';
import  from 'a11y-test-utils';

export const expect = mergeExpects(dbExpect, a11yExpect);
export const test = mergeTests(dbTest, a11yTest);
```

test.spec.ts

``` 
import  from './fixtures';

test('passes', async () => );
```