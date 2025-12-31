# Source: https://playwright.dev/docs/api-testing

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Guides]
-   [API testing]

On this page

<div>

# API testing

</div>

## Introduction[​](#introduction "Direct link to Introduction") 

Playwright can be used to get access to the [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) API of your application.

Sometimes you may want to send requests to the server directly from Node.js without loading a page and running js code in it. A few examples where it may come in handy:

-   Test your server API.
-   Prepare server side state before visiting the web application in a test.
-   Validate server side post-conditions after running some actions in the browser.

All of that could be achieved via [APIRequestContext](/docs/api/class-apirequestcontext "APIRequestContext") methods.

## Writing API Test[​](#writing-api-test "Direct link to Writing API Test") 

[APIRequestContext](/docs/api/class-apirequestcontext "APIRequestContext") can send all kinds of HTTP(S) requests over network.

The following example demonstrates how to use Playwright to test issues creation via [GitHub API](https://docs.github.com/en/rest). The test suite will do the following:

-   Create a new repository before running tests.
-   Create a few issues and validate server state.
-   Delete the repository after running tests.

### Configuration[​](#configuration "Direct link to Configuration") 

GitHub API requires authorization, so we\'ll configure the token once for all tests. While at it, we\'ll also set the `baseURL` to simplify the tests. You can either put them in the configuration file, or in the test file with `test.use()`.

playwright.config.ts

``` 
import  from '@playwright/test';
export default defineConfig(`,
    },
  }
});
```

**Proxy configuration**

If your tests need to run behind a proxy, you can specify this in the config and the `request` fixture will pick it up automatically:

playwright.config.ts

``` 
import  from '@playwright/test';
export default defineConfig(,
  }
});
```

### Writing tests[​](#writing-tests "Direct link to Writing tests") 

Playwright Test comes with the built-in `request` fixture that respects configuration options like `baseURL` or `extraHTTPHeaders` we specified and is ready to send some requests.

Now we can add a few tests that will create new issues in the repository.

``` 
const REPO = 'test-repo-1';
const USER = 'github-username';

test('should create a bug report', async () => /$/issues`, 
  });
  expect(newIssue.ok()).toBeTruthy();

  const issues = await request.get(`/repos/$/$/issues`);
  expect(issues.ok()).toBeTruthy();
  expect(await issues.json()).toContainEqual(expect.objectContaining());
});

test('should create a feature request', async () => /$/issues`, 
  });
  expect(newIssue.ok()).toBeTruthy();

  const issues = await request.get(`/repos/$/$/issues`);
  expect(issues.ok()).toBeTruthy();
  expect(await issues.json()).toContainEqual(expect.objectContaining());
});
```

### Setup and teardown[​](#setup-and-teardown "Direct link to Setup and teardown") 

These tests assume that repository exists. You probably want to create a new one before running tests and delete it afterwards. Use `beforeAll` and `afterAll` hooks for that.

``` 
test.beforeAll(async () => 
  });
  expect(response.ok()).toBeTruthy();
});

test.afterAll(async () => /$`);
  expect(response.ok()).toBeTruthy();
});
```

## Using request context[​](#using-request-context "Direct link to Using request context") 

Behind the scenes, [`request` fixture](/docs/api/class-fixtures#fixtures-request) will actually call [apiRequest.newContext()](/docs/api/class-apirequest#api-request-new-context). You can always do that manually if you\'d like more control. Below is a standalone script that does the same as `beforeAll` and `afterAll` from above.

``` 
import  from '@playwright/test';
const REPO = 'test-repo-1';
const USER = 'github-username';

(async () => );

  // Create a repository.
  await context.post('/user/repos', `,
    },
    data: 
  });

  // Delete a repository.
  await context.delete(`/repos/$/$`, `,
    }
  });
})();
```

## Sending API requests from UI tests[​](#sending-api-requests-from-ui-tests "Direct link to Sending API requests from UI tests") 

While running tests inside browsers you may want to make calls to the HTTP API of your application. It may be helpful if you need to prepare server state before running a test or to check some postconditions on the server after performing some actions in the browser. All of that could be achieved via [APIRequestContext](/docs/api/class-apirequestcontext "APIRequestContext") methods.

### Establishing preconditions[​](#establishing-preconditions "Direct link to Establishing preconditions") 

The following test creates a new issue via API and then navigates to the list of all issues in the project to check that it appears at the top of the list.

``` 
import  from '@playwright/test';

const REPO = 'test-repo-1';
const USER = 'github-username';

// Request context is reused by all tests in the file.
let apiContext;

test.beforeAll(async () => `,
    },
  });
});

test.afterAll(async () => );

test('last created issue should be first in the list', async () => /$/issues`, 
  });
  expect(newIssue.ok()).toBeTruthy();

  await page.goto(`https://github.com/$/$/issues`);
  const firstIssue = page.locator(`a[data-hovercard-type='issue']`).first();
  await expect(firstIssue).toHaveText('[Feature] request 1');
});
```

### Validating postconditions[​](#validating-postconditions "Direct link to Validating postconditions") 

The following test creates a new issue via user interface in the browser and then uses checks if it was created via API:

``` 
import  from '@playwright/test';

const REPO = 'test-repo-1';
const USER = 'github-username';

// Request context is reused by all tests in the file.
let apiContext;

test.beforeAll(async () => `,
    },
  });
});

test.afterAll(async () => );

test('last created issue should be on the server', async () => /$/issues`);
  await page.getByText('New Issue').click();
  await page.getByRole('textbox', ).fill('Bug report 1');
  await page.getByRole('textbox', ).fill('Bug description');
  await page.getByText('Submit new issue').click();
  const issueId = new URL(page.url()).pathname.split('/').pop();

  const newIssue = await apiContext.get(
      `https://api.github.com/repos/$/$/issues/$`
  );
  expect(newIssue.ok()).toBeTruthy();
  expect(newIssue.json()).toEqual(expect.objectContaining());
});
```

## Reusing authentication state[​](#reusing-authentication-state "Direct link to Reusing authentication state") 

Web apps use cookie-based or token-based authentication, where authenticated state is stored as [cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies). Playwright provides [apiRequestContext.storageState()](/docs/api/class-apirequestcontext#api-request-context-storage-state) method that can be used to retrieve storage state from an authenticated context and then create new contexts with that state.

Storage state is interchangeable between [BrowserContext](/docs/api/class-browsercontext "BrowserContext") and [APIRequestContext](/docs/api/class-apirequestcontext "APIRequestContext"). You can use it to log in via API calls and then create a new context with cookies already there. The following code snippet retrieves state from an authenticated [APIRequestContext](/docs/api/class-apirequestcontext "APIRequestContext") and creates a new [BrowserContext](/docs/api/class-browsercontext "BrowserContext") with that state.

``` 
const requestContext = await request.newContext(
});
await requestContext.get(`https://api.example.com/login`);
// Save storage state into the file.
await requestContext.storageState();

// Create a new context with the saved storage state.
const context = await browser.newContext();
```

## Context request vs global request[​](#context-request-vs-global-request "Direct link to Context request vs global request") 

There are two types of [APIRequestContext](/docs/api/class-apirequestcontext "APIRequestContext"):

-   associated with a [BrowserContext](/docs/api/class-browsercontext "BrowserContext")
-   isolated instance, created via [apiRequest.newContext()](/docs/api/class-apirequest#api-request-new-context)

The main difference is that [APIRequestContext](/docs/api/class-apirequestcontext "APIRequestContext") accessible via [browserContext.request](/docs/api/class-browsercontext#browser-context-request) and [page.request](/docs/api/class-page#page-request) will populate request\'s `Cookie` header from the browser context and will automatically update browser cookies if [APIResponse](/docs/api/class-apiresponse "APIResponse") has `Set-Cookie` header:

``` 
test('context request will share cookie storage with its browser context', async () => ) =>
      [name, value])
    )).toEqual(responseCookies);

    await route.fulfill(,
    });
  });
  await page.goto('https://www.github.com/');
});
```

If you don\'t want [APIRequestContext](/docs/api/class-apirequestcontext "APIRequestContext") to use and update cookies from the browser context, you can manually create a new instance of [APIRequestContext](/docs/api/class-apirequestcontext "APIRequestContext") which will have its own isolated cookies:

``` 
test('global context request has isolated cookie storage', async () => );
    const contextCookies2 = await browserContext2.cookies();
    // The new browser context will already contain all the cookies from the API response.
    expect(
        new Map(contextCookies2.map(() => [name, value]))
    ).toEqual(responseCookies);

    await route.fulfill(,
    });
  });
  await page.goto('https://www.github.com/');
  await request.dispose();
});
```