# Source: https://playwright.dev/docs/testing-library

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Migration]
-   [Migrating from Testing Library]

On this page

<div>

# Migrating from Testing Library

</div>

## Migration principles[​](#migration-principles "Direct link to Migration principles") 

This guide describes migration to Playwright\'s [Experimental Component Testing](/docs/test-components) from [DOM Testing Library](https://testing-library.com/docs/dom-testing-library/intro/), [React Testing Library](https://testing-library.com/docs/react-testing-library/intro/), [Vue Testing Library](https://testing-library.com/docs/vue-testing-library/intro) and [Svelte Testing Library](https://testing-library.com/docs/svelte-testing-library/intro).

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

If you use DOM Testing Library in the browser (for example, you bundle end-to-end tests with webpack), you can switch directly to Playwright Test. Examples below are focused on component tests, but for end-to-end test you just need to replace `await mount` with `await page.goto('http://localhost:3000/')` to open the page under test.

## Cheat Sheet[​](#cheat-sheet "Direct link to Cheat Sheet") 

Testing Library

Playwright

[screen](https://testing-library.com/docs/queries/about#screen)

[page](/docs/api/class-page) and [component](/docs/api/class-locator)

[queries](https://testing-library.com/docs/queries/about)

[locators](/docs/locators)

[async helpers](https://testing-library.com/docs/dom-testing-library/api-async)

[assertions](/docs/test-assertions)

[user events](https://testing-library.com/docs/user-event/intro)

[actions](/docs/api/class-locator)

`await user.click(screen.getByText('Click me'))`

`await component.getByText('Click me').click()`

`await user.click(await screen.findByText('Click me'))`

`await component.getByText('Click me').click()`

`await user.type(screen.getByLabelText('Password'), 'secret')`

`await component.getByLabel('Password').fill('secret')`

`expect(screen.getByLabelText('Password')).toHaveValue('secret')`

`await expect(component.getByLabel('Password')).toHaveValue('secret')`

`screen.getByRole('button', )`

`component.getByRole('button', )`

`screen.getByLabelText('...')`

`component.getByLabel('...')`

`screen.queryByPlaceholderText('...')`

`component.getByPlaceholder('...')`

`screen.findByText('...')`

`component.getByText('...')`

`screen.getByTestId('...')`

`component.getByTestId('...')`

`render(<Component />);`

`mount(<Component />);`

`const  = render(<Component />);`

`const  = await mount(<Component />);`

`const  = render(<Component />);`

`const  = await mount(<Component />);`

## Example[​](#example "Direct link to Example") 

Testing Library:

``` 
import React from 'react';
import  from '@testing-library/react';
import userEvent from '@testing-library/user-event';

test('sign in', async () => ));

  // Verify signed in state by waiting until "Welcome" message appears.
  expect(await screen.findByText('Welcome, John')).toBeInTheDocument();
});
```

Line-by-line migration to Playwright Test:

``` 
const  = require('@playwright/experimental-ct-react'); // 1

test('sign in', async () => ).click();

  // Verify signed in state by waiting until "Welcome" message appears.
  await expect(component.getByText('Welcome, John')).toBeVisible(); // 5
});
```

Migration highlights (see inline comments in the Playwright Test code snippet):

1.  Import everything from `@playwright/experimental-ct-react` (or -vue, -svelte) for component tests, or from `@playwright/test` for end-to-end tests.
2.  Test function is given a `page` that is isolated from other tests, and `mount` that renders a component in this page. These are two of the [useful fixtures](/docs/api/class-fixtures) in Playwright Test.
3.  Replace `render` with `mount` that returns a [component locator](/docs/locators).
4.  Use locators created with [locator.locator()](/docs/api/class-locator#locator-locator) or [page.locator()](/docs/api/class-page#page-locator) to perform most of the actions.
5.  Use [assertions](/docs/test-assertions) to verify the state.

## Migrating queries[​](#migrating-queries "Direct link to Migrating queries") 

All queries like `getBy...`, `findBy...`, `queryBy...` and their multi-element counterparts are replaced with `component.getBy...` locators. Locators always auto-wait and retry when needed, so you don\'t have to worry about choosing the right method. When you want to do a [list operation](/docs/locators#lists), e.g. assert a list of texts, Playwright automatically performs multi-element operations.

## Replacing `waitFor`[​](#replacing-waitfor "Direct link to replacing-waitfor") 

Playwright includes [assertions](/docs/test-assertions) that automatically wait for the condition, so you don\'t usually need an explicit `waitFor`/`waitForElementToBeRemoved` call.

``` 
// Testing Library
await waitFor(() => );
await waitForElementToBeRemoved(() => queryByText('the mummy'));

// Playwright
await expect(page.getByText('the lion king')).toBeVisible();
await expect(page.getByText('the mummy')).toBeHidden();
```

When you cannot find a suitable assertion, use [`expect.poll`](/docs/test-assertions#expectpoll) instead.

``` 
await expect.poll(async () => ).toBe(200);
```

## Replacing `within`[​](#replacing-within "Direct link to replacing-within") 

You can create a locator inside another locator with [locator.locator()](/docs/api/class-locator#locator-locator) method.

``` 
// Testing Library
const messages = screen.getByTestId('messages');
const helloMessage = within(messages).getByText('hello');

// Playwright
const messages = component.getByTestId('messages');
const helloMessage = messages.getByText('hello');
```

## Playwright Test Super Powers[​](#playwright-test-super-powers "Direct link to Playwright Test Super Powers") 

Once you\'re on Playwright Test, you get a lot!

-   Full zero-configuration TypeScript support
-   Run tests across **all web engines** (Chrome, Firefox, Safari) on **any popular operating system** (Windows, macOS, Ubuntu)
-   Full support for multiple origins, [(i)frames](/docs/api/class-frame), [tabs and contexts](/docs/pages)
-   Run tests in isolation in parallel across multiple browsers
-   Built-in test [artifact collection](/docs/test-use-options#recording-options)

You also get all these ✨ awesome tools ✨ that come bundled with Playwright Test:

-   [Visual Studio Code integration](/docs/getting-started-vscode)
-   [UI mode](/docs/test-ui-mode) for debugging tests with a time travel experience complete with watch mode.
-   [Playwright Inspector](/docs/debug#playwright-inspector)
-   [Playwright Test Code generation](/docs/codegen-intro)
-   [Playwright Tracing](/docs/trace-viewer) for post-mortem debugging

## Further Reading[​](#further-reading "Direct link to Further Reading") 

Learn more about Playwright Test runner:

-   [Getting Started](/docs/intro)
-   [Experimental Component Testing](/docs/test-components)
-   [Locators](/docs/locators)
-   [Assertions](/docs/test-assertions)
-   [Auto-waiting](/docs/actionability)