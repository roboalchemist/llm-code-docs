# Source: https://playwright.dev/docs/test-fixtures

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Playwright Test]
-   [Fixtures]

On this page

<div>

# Fixtures

</div>

## Introduction[​](#introduction "Direct link to Introduction") 

Playwright Test is based on the concept of test fixtures. Test fixtures are used to establish the environment for each test, giving the test everything it needs and nothing else. Test fixtures are isolated between tests. With fixtures, you can group tests based on their meaning, instead of their common setup.

### Built-in fixtures[​](#built-in-fixtures "Direct link to Built-in fixtures") 

You have already used test fixtures in your first test.

``` 
import  from '@playwright/test';

test('basic test', async () => );
```

The `` argument tells Playwright Test to set up the `page` fixture and provide it to your test function.

Here is a list of the pre-defined fixtures that you are likely to use most of the time:

Fixture

Type

Description

page

[Page](/docs/api/class-page "Page")

Isolated page for this test run.

context

[BrowserContext](/docs/api/class-browsercontext "BrowserContext")

Isolated context for this test run. The `page` fixture belongs to this context as well. Learn how to [configure context](/docs/test-configuration).

browser

[Browser](/docs/api/class-browser "Browser")

Browsers are shared across tests to optimize resources. Learn how to [configure browsers](/docs/test-configuration).

browserName

[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

The name of the browser currently running the test. Either `chromium`, `firefox` or `webkit`.

request

[APIRequestContext](/docs/api/class-apirequestcontext "APIRequestContext")

Isolated [APIRequestContext](/docs/api/class-apirequestcontext) instance for this test run.

### Without fixtures[​](#without-fixtures "Direct link to Without fixtures") 

Here is how a typical test environment setup differs between the traditional test style and the fixture-based one.

`TodoPage` is a class that helps us interact with a \"todo list\" page of the web app, following the [Page Object Model](/docs/pom) pattern. It uses Playwright\'s `page` internally.

Click to expand the code for the `TodoPage`

<div>

<div>

todo-page.ts

``` 
import type  from '@playwright/test';

export class TodoPage 

  async goto() 

  async addToDo(text: string) 

  async remove(text: string) );
    await todo.hover();
    await todo.getByLabel('Delete').click();
  }

  async removeAll() 
  }
}
```

</div>

</div>

todo.spec.ts

``` 
const  = require('@playwright/test');
const  = require('./todo-page');

test.describe('todo tests', () => ) => );

  test.afterEach(async () => );

  test('should add an item', async () => );

  test('should remove an item', async () => );
});
```

### With fixtures[​](#with-fixtures "Direct link to With fixtures") 

Fixtures have a number of advantages over before/after hooks:

-   Fixtures **encapsulate** setup and teardown in the same place so it is easier to write. So if you have an after hook that tears down what was created in a before hook, consider turning them into a fixture.
-   Fixtures are **reusable** between test files - you can define them once and use them in all your tests. That\'s how Playwright\'s built-in `page` fixture works. So if you have a helper function that is used in multiple tests, consider turning it into a fixture.
-   Fixtures are **on-demand** - you can define as many fixtures as you\'d like, and Playwright Test will setup only the ones needed by your test and nothing else.
-   Fixtures are **composable** - they can depend on each other to provide complex behaviors.
-   Fixtures are **flexible**. Tests can use any combination of fixtures to precisely tailor the environment to their needs, without affecting other tests.
-   Fixtures simplify **grouping**. You no longer need to wrap tests in `describe`s that set up their environment, and are free to group your tests by their meaning instead.

Click to expand the code for the `TodoPage`

<div>

<div>

todo-page.ts

``` 
import type  from '@playwright/test';

export class TodoPage 

  async goto() 

  async addToDo(text: string) 

  async remove(text: string) );
    await todo.hover();
    await todo.getByLabel('Delete').click();
  }

  async removeAll() 
  }
}
```

</div>

</div>

example.spec.ts

``` 
import  from '@playwright/test';
import  from './todo-page';

// Extend basic test by providing a "todoPage" fixture.
const test = base.extend<>(, use) => ,
});

test('should add an item', async () => );

test('should remove an item', async () => );
```

## Creating a fixture[​](#creating-a-fixture "Direct link to Creating a fixture") 

To create your own fixture, use [test.extend()](/docs/api/class-test#test-extend) to create a new `test` object that will include it.

Below we create two fixtures `todoPage` and `settingsPage` that follow the [Page Object Model](/docs/pom) pattern.

Click to expand the code for the `TodoPage` and `SettingsPage`

<div>

<div>

todo-page.ts

``` 
import type  from '@playwright/test';

export class TodoPage 

  async goto() 

  async addToDo(text: string) 

  async remove(text: string) );
    await todo.hover();
    await todo.getByLabel('Delete').click();
  }

  async removeAll() 
  }
}
```

SettingsPage is similar:

settings-page.ts

``` 
import type  from '@playwright/test';

export class SettingsPage 

  async switchToDarkMode() 
}
```

</div>

</div>

my-test.ts

``` 
import  from '@playwright/test';
import  from './todo-page';
import  from './settings-page';

// Declare the types of your fixtures.
type MyFixtures = ;

// Extend base test by providing "todoPage" and "settingsPage".
// This new "test" can be used in multiple test files, and each of them will get the fixtures.
export const test = base.extend<MyFixtures>(, use) => ,

  settingsPage: async (, use) => ,
});
export  from '@playwright/test';
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

Custom fixture names should start with a letter or underscore, and can contain only letters, numbers, and underscores.

## Using a fixture[​](#using-a-fixture "Direct link to Using a fixture") 

Just mention a fixture in your test function argument, and the test runner will take care of it. Fixtures are also available in hooks and other fixtures. If you use TypeScript, fixtures will be type safe.

Below we use the `todoPage` and `settingsPage` fixtures that we defined above.

``` 
import  from './my-test';

test.beforeEach(async () => );

test('basic test', async () => );
```

## Overriding fixtures[​](#overriding-fixtures "Direct link to Overriding fixtures") 

In addition to creating your own fixtures, you can also override existing fixtures to fit your needs. Consider the following example which overrides the `page` fixture by automatically navigating to the `baseURL`:

``` 
import  from '@playwright/test';

export const test = base.extend(, use) => ,
});
```

Notice that in this example, the `page` fixture is able to depend on other built-in fixtures such as [testOptions.baseURL](/docs/api/class-testoptions#test-options-base-url). We can now configure `baseURL` in the configuration file, or locally in the test file with [test.use()](/docs/api/class-test#test-use).

example.spec.ts

``` 
test.use();
```

Fixtures can also be overridden, causing the base fixture to be completely replaced with something different. For example, we could override the [testOptions.storageState](/docs/api/class-testoptions#test-options-storage-state) fixture to provide our own data.

``` 
import  from '@playwright/test';

export const test = base.extend(, use) => );
  },
});
```

## Worker-scoped fixtures[​](#worker-scoped-fixtures "Direct link to Worker-scoped fixtures") 

Playwright Test uses [worker processes](/docs/test-parallel) to run test files. Similar to how test fixtures are set up for individual test runs, worker fixtures are set up for each worker process. That\'s where you can set up services, run servers, etc. Playwright Test will reuse the worker process for as many test files as it can, provided their worker fixtures match and hence environments are identical.

Below we\'ll create an `account` fixture that will be shared by all tests in the same worker, and override the `page` fixture to log in to this account for each test. To generate unique accounts, we\'ll use the [workerInfo.workerIndex](/docs/api/class-workerinfo#worker-info-worker-index) that is available to any test or fixture. Note the tuple-like syntax for the worker fixture - we have to pass `` so that test runner sets this fixture up once per worker.

my-test.ts

``` 
import  from '@playwright/test';

type Account = ;

// Note that we pass worker fixture types as a second template parameter.
export const test = base.extend<, >(, use, workerInfo) => );
  }, ],

  page: async (, use) =>  = account;
    await page.goto('/signin');
    await page.getByLabel('User Name').fill(username);
    await page.getByLabel('Password').fill(password);
    await page.getByText('Sign in').click();
    await expect(page.getByTestId('userinfo')).toHaveText(username);

    // Use signed-in page in the test.
    await use(page);
  },
});
export  from '@playwright/test';
```

## Automatic fixtures[​](#automatic-fixtures "Direct link to Automatic fixtures") 

Automatic fixtures are set up for each test/worker, even when the test does not list them directly. To create an automatic fixture, use the tuple syntax and pass ``.

Here is an example fixture that automatically attaches debug logs when the test fails, so we can later review the logs in the reporter. Note how it uses the [TestInfo](/docs/api/class-testinfo "TestInfo") object that is available in each test/fixture to retrieve metadata about the test being run.

my-test.ts

``` 
import debug from 'debug';
import fs from 'fs';
import  from '@playwright/test';

export const test = base.extend<>(, use, testInfo) => );
    }
  }, ],
});
export  from '@playwright/test';
```

## Fixture timeout[​](#fixture-timeout "Direct link to Fixture timeout") 

By default, the fixture inherits the timeout value of the test. However, for slow fixtures, especially [worker-scoped](#worker-scoped-fixtures) ones, it is convenient to have a separate timeout. This way you can keep the overall test timeout small, and give the slow fixture more time.

``` 
import  from '@playwright/test';

const test = base.extend<>(, use) => , ]
});

test('example test', async () => );
```

## Fixtures-options[​](#fixtures-options "Direct link to Fixtures-options") 

Playwright Test supports running multiple test projects that can be configured separately. You can use \"option\" fixtures to make your configuration options declarative and type safe. Learn more about [parameterizing tests](/docs/test-parameterize).

Below we\'ll create a `defaultItem` option in addition to the `todoPage` fixture from other examples. This option will be set in the configuration file. Note the tuple syntax and `` argument.

Click to expand the code for the `TodoPage`

<div>

<div>

todo-page.ts

``` 
import type  from '@playwright/test';

export class TodoPage 

  async goto() 

  async addToDo(text: string) 

  async remove(text: string) );
    await todo.hover();
    await todo.getByLabel('Delete').click();
  }

  async removeAll() 
  }
}
```

</div>

</div>

my-test.ts

``` 
import  from '@playwright/test';
import  from './todo-page';

// Declare your options to type-check your configuration.
export type MyOptions = ;
type MyFixtures = ;

// Specify both option and fixture types.
export const test = base.extend<MyOptions & MyFixtures>(],

  // Our "todoPage" fixture depends on the option.
  todoPage: async (, use) => ,
});
export  from '@playwright/test';
```

We can now use the `todoPage` fixture as usual, and set the `defaultItem` option in the configuration file.

playwright.config.ts

``` 
import  from '@playwright/test';
import type  from './my-test';

export default defineConfig<MyOptions>(,
    },
    ,
    },
  ]
});
```

**Array as an option value**

If the value of your option is an array, for example `[, ]`, you\'ll need to wrap it into an extra array when providing the value. This is best illustrated with an example.

``` 
type Person = ;
const test = base.extend<>(],
});

// Option value is an array of persons.
const actualPersons = [, ];
test.use(],
});

test.use();
```

**Reset an option**

You can reset an option to the value defined in the config file by setting it to `undefined`. Consider the following config that sets a `baseURL`:

playwright.config.ts

``` 
import  from '@playwright/test';

export default defineConfig(,
});
```

You can now configure `baseURL` for a file, and also opt-out for a single test.

intro.spec.ts

``` 
import  from '@playwright/test';

// Configure baseURL for this file.
test.use();

test('check intro contents', async () => );

test.describe(() => );

  test('can navigate to intro from the home page', async () => );
});
```

If you would like to completely reset the value to `undefined`, use a long-form fixture notation.

intro.spec.ts

``` 
import  from '@playwright/test';

// Completely unset baseURL for this file.
test.use(, use) => use(undefined), ],
});

test('no base url', async () => );
```

## Execution order[​](#execution-order "Direct link to Execution order") 

Each fixture has a setup and teardown phase before and after the `await use()` call in the fixture. Setup is executed before the test/hook requiring it is run, and teardown is executed when the fixture is no longer being used by the test/hook.

Fixtures follow these rules to determine the execution order:

-   When fixture A depends on fixture B: B is always set up before A and torn down after A.
-   Non-automatic fixtures are executed lazily, only when the test/hook needs them.
-   Test-scoped fixtures are torn down after each test, while worker-scoped fixtures are only torn down when the worker process executing tests is torn down.

Consider the following example:

``` 
import  from '@playwright/test';

const test = base.extend<, >() => , ],

  autoWorkerFixture: [async () => , ],

  testFixture: [async () => , ],

  autoTestFixture: [async () => , ],

  unusedFixture: [async () => , ],
});

test.beforeAll(async () => );
test.beforeEach(async () => );
test('first test', async () => );
test('second test', async () => );
test.afterEach(async () => );
test.afterAll(async () => );
```

Normally, if all tests pass and no errors are thrown, the order of execution is as following.

-   worker setup and `beforeAll` section:
    -   `browser` setup because it is required by `autoWorkerFixture`.
    -   `autoWorkerFixture` setup because automatic worker fixtures are always set up before anything else.
    -   `beforeAll` runs.
-   `first test` section:
    -   `autoTestFixture` setup because automatic test fixtures are always set up before test and `beforeEach` hooks.
    -   `page` setup because it is required in `beforeEach` hook.
    -   `beforeEach` runs.
    -   `first test` runs.
    -   `afterEach` runs.
    -   `page` teardown because it is a test-scoped fixture and should be torn down after the test finishes.
    -   `autoTestFixture` teardown because it is a test-scoped fixture and should be torn down after the test finishes.
-   `second test` section:
    -   `autoTestFixture` setup because automatic test fixtures are always set up before test and `beforeEach` hooks.
    -   `page` setup because it is required in `beforeEach` hook.
    -   `beforeEach` runs.
    -   `workerFixture` setup because it is required by `testFixture` that is required by the `second test`.
    -   `testFixture` setup because it is required by the `second test`.
    -   `second test` runs.
    -   `afterEach` runs.
    -   `testFixture` teardown because it is a test-scoped fixture and should be torn down after the test finishes.
    -   `page` teardown because it is a test-scoped fixture and should be torn down after the test finishes.
    -   `autoTestFixture` teardown because it is a test-scoped fixture and should be torn down after the test finishes.
-   `afterAll` and worker teardown section:
    -   `afterAll` runs.
    -   `workerFixture` teardown because it is a workers-scoped fixture and should be torn down once at the end.
    -   `autoWorkerFixture` teardown because it is a workers-scoped fixture and should be torn down once at the end.
    -   `browser` teardown because it is a workers-scoped fixture and should be torn down once at the end.

A few observations:

-   `page` and `autoTestFixture` are set up and torn down for each test, as test-scoped fixtures.
-   `unusedFixture` is never set up because it is not used by any tests/hooks.
-   `testFixture` depends on `workerFixture` and triggers its setup.
-   `workerFixture` is lazily set up before the second test, but torn down once during worker shutdown, as a worker-scoped fixture.
-   `autoWorkerFixture` is set up for `beforeAll` hook, but `autoTestFixture` is not.

## Combine custom fixtures from multiple modules[​](#combine-custom-fixtures-from-multiple-modules "Direct link to Combine custom fixtures from multiple modules") 

You can merge test fixtures from multiple files or modules:

fixtures.ts

``` 
import  from '@playwright/test';
import  from 'database-test-utils';
import  from 'a11y-test-utils';

export const test = mergeTests(dbTest, a11yTest);
```

test.spec.ts

``` 
import  from './fixtures';

test('passes', async () => );
```

## Box fixtures[​](#box-fixtures "Direct link to Box fixtures") 

Usually, custom fixtures are reported as separate steps in the UI mode, Trace Viewer and various test reports. They also appear in error messages from the test runner. For frequently used fixtures, this can mean lots of noise. You can stop the fixtures steps from being shown in the UI by \"boxing\" it.

``` 
import  from '@playwright/test';

export const test = base.extend(, use, testInfo) => , ],
});
```

This is useful for non-interesting helper fixtures. For example, an [automatic](/docs/test-fixtures#automatic-fixtures) fixture that sets up some common data can be safely hidden from a test report.

You can also mark the fixture as `box: 'self'` to only hide that particular fixture, but include all the steps inside the fixture in the test report.

## Custom fixture title[​](#custom-fixture-title "Direct link to Custom fixture title") 

Instead of the usual fixture name, you can give fixtures a custom title that will be shown in test reports and error messages.

``` 
import  from '@playwright/test';

export const test = base.extend(, use, testInfo) => , ],
});
```

## Adding global beforeEach/afterEach hooks[​](#adding-global-beforeeachaftereach-hooks "Direct link to Adding global beforeEach/afterEach hooks") 

[test.beforeEach()](/docs/api/class-test#test-before-each) and [test.afterEach()](/docs/api/class-test#test-after-each) hooks run before/after each test declared in the same file and same [test.describe()](/docs/api/class-test#test-describe) block (if any). If you want to declare hooks that run before/after each test globally, you can declare them as auto fixtures like this:

fixtures.ts

``` 
import  from '@playwright/test';

export const test = base.extend<>(, use) => , ],  // automatically starts for every test.
});
```

And then import the fixtures in all your tests:

mytest.spec.ts

``` 
import  from './fixtures';
import  from '@playwright/test';

test('basic', async () => );
```

## Adding global beforeAll/afterAll hooks[​](#adding-global-beforeallafterall-hooks "Direct link to Adding global beforeAll/afterAll hooks") 

[test.beforeAll()](/docs/api/class-test#test-before-all) and [test.afterAll()](/docs/api/class-test#test-after-all) hooks run before/after all tests declared in the same file and same [test.describe()](/docs/api/class-test#test-describe) block (if any), once per worker process. If you want to declare hooks that run before/after all tests in every file, you can declare them as auto fixtures with `scope: 'worker'` as follows:

fixtures.ts

``` 
import  from '@playwright/test';

export const test = base.extend<, >(, use) => `);
    await use();
    // This code runs after all the tests in the worker process.
    console.log(`Stopping test worker $`);
  }, ],  // automatically starts for every worker.
});
```

And then import the fixtures in all your tests:

mytest.spec.ts

``` 
import  from './fixtures';
import  from '@playwright/test';

test('basic', async () => );
```

Note that the fixtures will still run once per [worker process](/docs/test-parallel#worker-processes), but you don\'t need to redeclare them in every file.