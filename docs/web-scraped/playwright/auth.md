# Source: https://playwright.dev/docs/auth

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Guides]
-   [Authentication]

On this page

<div>

# Authentication

</div>

## Introduction[​](#introduction "Direct link to Introduction") 

Playwright executes tests in isolated environments called [browser contexts](/docs/browser-contexts). This isolation model improves reproducibility and prevents cascading test failures. Tests can load existing authenticated state. This eliminates the need to authenticate in every test and speeds up test execution.

## Core concepts[​](#core-concepts "Direct link to Core concepts") 

Regardless of the authentication strategy you choose, you are likely to store authenticated browser state on the file system.

We recommend to create `playwright/.auth` directory and add it to your `.gitignore`. Your authentication routine will produce authenticated browser state and save it to a file in this `playwright/.auth` directory. Later on, tests will reuse this state and start already authenticated.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTUuMDUuMzFjLjgxIDIuMTcuNDEgMy4zOC0uNTIgNC4zMUMzLjU1IDUuNjcgMS45OCA2LjQ1LjkgNy45OGMtMS40NSAyLjA1LTEuNyA2LjUzIDMuNTMgNy43LTIuMi0xLjE2LTIuNjctNC41Mi0uMy02LjYxLS42MSAyLjAzLjUzIDMuMzMgMS45NCAyLjg2IDEuMzktLjQ3IDIuMy41MyAyLjI3IDEuNjctLjAyLjc4LS4zMSAxLjQ0LTEuMTMgMS44MSAzLjQyLS41OSA0Ljc4LTMuNDIgNC43OC01LjU2IDAtMi44NC0yLjUzLTMuMjItMS4yNS01LjYxLTEuNTIuMTMtMi4wMyAxLjEzLTEuODkgMi43NS4wOSAxLjA4LTEuMDIgMS44LTEuODYgMS4zMy0uNjctLjQxLS42Ni0xLjE5LS4wNi0xLjc4QzguMTggNS4zMSA4LjY4IDIuNDUgNS4wNS4zMkw1LjAzLjNsLjAyLjAxeiI+PC9wYXRoPjwvc3ZnPg==)]danger

The browser state file may contain sensitive cookies and headers that could be used to impersonate you or your test account. We strongly discourage checking them into private or public repositories.

-   Bash
-   PowerShell
-   Batch

``` 
mkdir -p playwright/.auth
echo $'\nplaywright/.auth' >> .gitignore
```

``` 
New-Item -ItemType Directory -Force -Path playwright\.auth
Add-Content -path .gitignore "`r`nplaywright/.auth"
```

``` 
md playwright\.auth
echo. >> .gitignore
echo "playwright/.auth" >> .gitignore
```

## Basic: shared account in all tests[​](#basic-shared-account-in-all-tests "Direct link to Basic: shared account in all tests") 

This is the **recommended** approach for tests **without server-side state**. Authenticate once in the **setup project**, save the authentication state, and then reuse it to bootstrap each test already authenticated.

**When to use**

-   When you can imagine all your tests running at the same time with the same account, without affecting each other.

**When not to use**

-   Your tests modify server-side state. For example, one test checks the rendering of the settings page, while the other test is changing the setting, and you run tests in parallel. In this case, tests must use different accounts.
-   Your authentication is browser-specific.

**Details**

Create `tests/auth.setup.ts` that will prepare authenticated browser state for all other tests.

tests/auth.setup.ts

``` 
import  from '@playwright/test';
import path from 'path';

const authFile = path.join(__dirname, '../playwright/.auth/user.json');

setup('authenticate', async () => ).click();
  // Wait until the page receives the cookies.
  //
  // Sometimes login flow sets cookies in the process of several redirects.
  // Wait for the final URL to ensure that the cookies are actually set.
  await page.waitForURL('https://github.com/');
  // Alternatively, you can wait until the page reaches a state where all cookies are set.
  await expect(page.getByRole('button', )).toBeVisible();

  // End of authentication steps.

  await page.context().storageState();
});
```

Create a new `setup` project in the config and declare it as a [dependency](/docs/test-projects#dependencies) for all your testing projects. This project will always run and authenticate before all the tests. All testing projects should use the authenticated state as `storageState`.

playwright.config.ts

``` 
import  from '@playwright/test';

export default defineConfig(,

    ,
      dependencies: ['setup'],
    },

    ,
      dependencies: ['setup'],
    },
  ],
});
```

Tests start already authenticated because we specified `storageState` in the config.

tests/example.spec.ts

``` 
import  from '@playwright/test';

test('test', async () => );
```

Note that you need to delete the stored state when it expires. If you don\'t need to keep the state between test runs, write the browser state under [testProject.outputDir](/docs/api/class-testproject#test-project-output-dir), which is automatically cleaned up before every test run.

### Authenticating in UI mode[​](#authenticating-in-ui-mode "Direct link to Authenticating in UI mode") 

UI mode will not run the `setup` project by default to improve testing speed. We recommend to authenticate by manually running the `auth.setup.ts` from time to time, whenever existing authentication expires.

First [enable the `setup` project in the filters](/docs/test-ui-mode#filtering-tests), then click the triangle button next to `auth.setup.ts` file, and then disable the `setup` project in the filters again.

## Moderate: one account per parallel worker[​](#moderate-one-account-per-parallel-worker "Direct link to Moderate: one account per parallel worker") 

This is the **recommended** approach for tests that **modify server-side state**. In Playwright, worker processes run in parallel. In this approach, each parallel worker is authenticated once. All tests ran by worker are reusing the same authentication state. We will need multiple testing accounts, one per each parallel worker.

**When to use**

-   Your tests modify shared server-side state. For example, one test checks the rendering of the settings page, while the other test is changing the setting.

**When not to use**

-   Your tests do not modify any shared server-side state. In this case, all tests can use a single shared account.

**Details**

We will authenticate once per [worker process](/docs/test-parallel#worker-processes), each with a unique account.

Create `playwright/fixtures.ts` file that will [override `storageState` fixture](/docs/test-fixtures#overriding-fixtures) to authenticate once per worker. Use [testInfo.parallelIndex](/docs/api/class-testinfo#test-info-parallel-index) to differentiate between workers.

playwright/fixtures.ts

``` 
import  from '@playwright/test';
import fs from 'fs';
import path from 'path';

export * from '@playwright/test';
export const test = baseTest.extend<, >(, use) => use(workerStorageState),

  // Authenticate once per worker with a worker-scoped fixture.
  workerStorageState: [async (, use) => .json`);

    if (fs.existsSync(fileName)) 

    // Important: make sure we authenticate in a clean environment by unsetting storage state.
    const page = await browser.newPage();

    // Acquire a unique account, for example create a new one.
    // Alternatively, you can have a list of precreated accounts for testing.
    // Make sure that accounts are unique, so that multiple team members
    // can run tests at the same time without interference.
    const account = await acquireAccount(id);

    // Perform authentication steps. Replace these actions with your own.
    await page.goto('https://github.com/login');
    await page.getByLabel('Username or email address').fill(account.username);
    await page.getByLabel('Password').fill(account.password);
    await page.getByRole('button', ).click();
    // Wait until the page receives the cookies.
    //
    // Sometimes login flow sets cookies in the process of several redirects.
    // Wait for the final URL to ensure that the cookies are actually set.
    await page.waitForURL('https://github.com/');
    // Alternatively, you can wait until the page reaches a state where all cookies are set.
    await expect(page.getByRole('button', )).toBeVisible();

    // End of authentication steps.

    await page.context().storageState();
    await page.close();
    await use(fileName);
  }, ],
});
```

Now, each test file should import `test` from our fixtures file instead of `@playwright/test`. No changes are needed in the config.

tests/example.spec.ts

``` 
// Important: import our fixtures.
import  from '../playwright/fixtures';

test('test', async () => );
```

## Advanced scenarios[​](#advanced-scenarios "Direct link to Advanced scenarios") 

### Authenticate with API request[​](#authenticate-with-api-request "Direct link to Authenticate with API request") 

**When to use**

-   Your web application supports authenticating via API that is easier/faster than interacting with the app UI.

**Details**

We will send the API request with [APIRequestContext](/docs/api/class-apirequestcontext "APIRequestContext") and then save authenticated state as usual.

In the [setup project](#basic-shared-account-in-all-tests):

tests/auth.setup.ts

``` 
import  from '@playwright/test';

const authFile = 'playwright/.auth/user.json';

setup('authenticate', async () => 
  });
  await request.storageState();
});
```

Alternatively, in a [worker fixture](#moderate-one-account-per-parallel-worker):

playwright/fixtures.ts

``` 
import  from '@playwright/test';
import fs from 'fs';
import path from 'path';

export * from '@playwright/test';
export const test = baseTest.extend<, >(, use) => use(workerStorageState),

  // Authenticate once per worker with a worker-scoped fixture.
  workerStorageState: [async (, use) => .json`);

    if (fs.existsSync(fileName)) 

    // Important: make sure we authenticate in a clean environment by unsetting storage state.
    const context = await request.newContext();

    // Acquire a unique account, for example create a new one.
    // Alternatively, you can have a list of precreated accounts for testing.
    // Make sure that accounts are unique, so that multiple team members
    // can run tests at the same time without interference.
    const account = await acquireAccount(id);

    // Send authentication request. Replace with your own.
    await context.post('https://github.com/login', 
    });

    await context.storageState();
    await context.dispose();
    await use(fileName);
  }, ],
});
```

### Multiple signed in roles[​](#multiple-signed-in-roles "Direct link to Multiple signed in roles") 

**When to use**

-   You have more than one role in your end to end tests, but you can reuse accounts across all tests.

**Details**

We will authenticate multiple times in the setup project.

tests/auth.setup.ts

``` 
import  from '@playwright/test';

const adminFile = 'playwright/.auth/admin.json';

setup('authenticate as admin', async () => ).click();
  // Wait until the page receives the cookies.
  //
  // Sometimes login flow sets cookies in the process of several redirects.
  // Wait for the final URL to ensure that the cookies are actually set.
  await page.waitForURL('https://github.com/');
  // Alternatively, you can wait until the page reaches a state where all cookies are set.
  await expect(page.getByRole('button', )).toBeVisible();

  // End of authentication steps.

  await page.context().storageState();
});

const userFile = 'playwright/.auth/user.json';

setup('authenticate as user', async () => ).click();
  // Wait until the page receives the cookies.
  //
  // Sometimes login flow sets cookies in the process of several redirects.
  // Wait for the final URL to ensure that the cookies are actually set.
  await page.waitForURL('https://github.com/');
  // Alternatively, you can wait until the page reaches a state where all cookies are set.
  await expect(page.getByRole('button', )).toBeVisible();

  // End of authentication steps.

  await page.context().storageState();
});
```

After that, specify `storageState` for each test file or test group, **instead of** setting it in the config.

tests/example.spec.ts

``` 
import  from '@playwright/test';

test.use();

test('admin test', async () => );

test.describe(() => );

  test('user test', async () => );
});
```

See also about [authenticating in the UI mode](#authenticating-in-ui-mode).

### Testing multiple roles together[​](#testing-multiple-roles-together "Direct link to Testing multiple roles together") 

**When to use**

-   You need to test how multiple authenticated roles interact together, in a single test.

**Details**

Use multiple [BrowserContext](/docs/api/class-browsercontext "BrowserContext")s and [Page](/docs/api/class-page "Page")s with different storage states in the same test.

tests/example.spec.ts

``` 
import  from '@playwright/test';

test('admin and user', async () => );
  const adminPage = await adminContext.newPage();

  // userContext and all pages inside, including userPage, are signed in as "user".
  const userContext = await browser.newContext();
  const userPage = await userContext.newPage();

  // ... interact with both adminPage and userPage ...

  await adminContext.close();
  await userContext.close();
});
```

### Testing multiple roles with POM fixtures[​](#testing-multiple-roles-with-pom-fixtures "Direct link to Testing multiple roles with POM fixtures") 

**When to use**

-   You need to test how multiple authenticated roles interact together, in a single test.

**Details**

You can introduce fixtures that will provide a page authenticated as each role.

Below is an example that [creates fixtures](/docs/test-fixtures#creating-a-fixture) for two [Page Object Models](/docs/pom) - admin POM and user POM. It assumes `adminStorageState.json` and `userStorageState.json` files were created in the global setup.

playwright/fixtures.ts

``` 
import  from '@playwright/test';

// Page Object Model for the "admin" page.
// Here you can add locators and helper methods specific to the admin page.
class AdminPage 
}

// Page Object Model for the "user" page.
// Here you can add locators and helper methods specific to the user page.
class UserPage 
}

// Declare the types of your fixtures.
type MyFixtures = ;

export * from '@playwright/test';
export const test = base.extend<MyFixtures>(, use) => );
    const adminPage = new AdminPage(await context.newPage());
    await use(adminPage);
    await context.close();
  },
  userPage: async (, use) => );
    const userPage = new UserPage(await context.newPage());
    await use(userPage);
    await context.close();
  },
});
```

tests/example.spec.ts

``` 
// Import test with our new fixtures.
import  from '../playwright/fixtures';

// Use adminPage and userPage fixtures in the test.
test('admin and user', async () => );
```

### Session storage[​](#session-storage "Direct link to Session storage") 

Reusing authenticated state covers [cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies), [local storage](https://developer.mozilla.org/en-US/docs/Web/API/Storage) and [IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API) based authentication. Rarely, [session storage](https://developer.mozilla.org/en-US/docs/Web/API/Window/sessionStorage) is used for storing information associated with the signed-in state. Session storage is specific to a particular domain and is not persisted across page loads. Playwright does not provide API to persist session storage, but the following snippet can be used to save/load session storage.

``` 
// Get session storage and store as env variable
const sessionStorage = await page.evaluate(() => JSON.stringify(sessionStorage));
fs.writeFileSync('playwright/.auth/session.json', sessionStorage, 'utf-8');

// Set session storage in a new context
const sessionStorage = JSON.parse(fs.readFileSync('playwright/.auth/session.json', 'utf-8'));
await context.addInitScript(storage => 
}, sessionStorage);
```

### Avoid authentication in some tests[​](#avoid-authentication-in-some-tests "Direct link to Avoid authentication in some tests") 

You can reset storage state in a test file to avoid authentication that was set up for the whole project.

not-signed-in.spec.ts

``` 
import  from '@playwright/test';

// Reset storage state for this file to avoid being authenticated
test.use( });

test('not signed in test', async () => );
```