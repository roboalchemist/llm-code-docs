# Source: https://playwright.dev/docs/test-parallel

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Playwright Test]
-   [Parallelism]

On this page

<div>

# Parallelism

</div>

## Introduction[​](#introduction "Direct link to Introduction") 

Playwright Test runs tests in parallel. In order to achieve that, it runs several worker processes that run at the same time. By default, **test files** are run in parallel. Tests in a single file are run in order, in the same worker process.

-   You can configure tests using [`test.describe.configure`](#parallelize-tests-in-a-single-file) to run **tests in a single file** in parallel.
-   You can configure **entire project** to have all tests in all files to run in parallel using [testProject.fullyParallel](/docs/api/class-testproject#test-project-fully-parallel) or [testConfig.fullyParallel](/docs/api/class-testconfig#test-config-fully-parallel).
-   To **disable** parallelism limit the number of [workers to one](#disable-parallelism).

You can control the number of [parallel worker processes](#limit-workers) and [limit the number of failures](#limit-failures-and-fail-fast) in the whole test suite for efficiency.

## Worker processes[​](#worker-processes "Direct link to Worker processes") 

All tests run in worker processes. These processes are OS processes, running independently, orchestrated by the test runner. All workers have identical environments and each starts its own browser.

You can\'t communicate between the workers. Playwright Test reuses a single worker as much as it can to make testing faster, so multiple test files are usually run in a single worker one after another.

Workers are always shutdown after a [test failure](/docs/test-retries#failures) to guarantee pristine environment for following tests.

## Limit workers[​](#limit-workers "Direct link to Limit workers") 

You can control the maximum number of parallel worker processes via [command line](/docs/test-cli) or in the [configuration file](/docs/test-configuration).

From the command line:

``` 
npx playwright test --workers 4
```

In the configuration file:

playwright.config.ts

``` 
import  from '@playwright/test';

export default defineConfig();
```

## Disable parallelism[​](#disable-parallelism "Direct link to Disable parallelism") 

You can disable any parallelism by allowing just a single worker at any time. Either set `workers: 1` option in the configuration file or pass `--workers=1` to the command line.

``` 
npx playwright test --workers=1
```

## Parallelize tests in a single file[​](#parallelize-tests-in-a-single-file "Direct link to Parallelize tests in a single file") 

By default, tests in a single file are run in order. If you have many independent tests in a single file, you might want to run them in parallel with [test.describe.configure()](/docs/api/class-test#test-describe-configure).

Note that parallel tests are executed in separate worker processes and cannot share any state or global variables. Each test executes all relevant hooks just for itself, including `beforeAll` and `afterAll`.

``` 
import  from '@playwright/test';

test.describe.configure();

test('runs in parallel 1', async () => );
test('runs in parallel 2', async () => );
```

Alternatively, you can opt-in all tests into this fully-parallel mode in the configuration file:

playwright.config.ts

``` 
import  from '@playwright/test';

export default defineConfig();
```

You can also opt in for fully-parallel mode for just a few projects:

playwright.config.ts

``` 
import  from '@playwright/test';

export default defineConfig(,
      fullyParallel: true,
    },
  ]
});
```

## Serial mode[​](#serial-mode "Direct link to Serial mode") 

You can annotate inter-dependent tests as serial. If one of the serial tests fails, all subsequent tests are skipped. All tests in a group are retried together.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

Using serial is not recommended. It is usually better to make your tests isolated, so they can be run independently.

``` 
import  from '@playwright/test';

// Annotate entire file as serial.
test.describe.configure();

let page: Page;

test.beforeAll(async () => );

test.afterAll(async () => );

test('runs first', async () => );

test('runs second', async () => );
```

## Opt out of fully parallel mode[​](#opt-out-of-fully-parallel-mode "Direct link to Opt out of fully parallel mode") 

If your configuration applies parallel mode to all tests using [testConfig.fullyParallel](/docs/api/class-testconfig#test-config-fully-parallel), you might still want to run some tests with default settings. You can override the mode per describe:

``` 
test.describe('runs in parallel with other describes', () => );
  test('in order 1', async () => );
  test('in order 2', async () => );
});
```

## Shard tests between multiple machines[​](#shard-tests-between-multiple-machines "Direct link to Shard tests between multiple machines") 

Playwright Test can shard a test suite, so that it can be executed on multiple machines. See [sharding guide](/docs/test-sharding) for more details.

``` 
npx playwright test --shard=2/3
```

## Limit failures and fail fast[​](#limit-failures-and-fail-fast "Direct link to Limit failures and fail fast") 

You can limit the number of failed tests in the whole test suite by setting `maxFailures` config option or passing `--max-failures` command line flag.

When running with \"max failures\" set, Playwright Test will stop after reaching this number of failed tests and skip any tests that were not executed yet. This is useful to avoid wasting resources on broken test suites.

Passing command line option:

``` 
npx playwright test --max-failures=10
```

Setting in the configuration file:

playwright.config.ts

``` 
import  from '@playwright/test';

export default defineConfig();
```

## Worker index and parallel index[​](#worker-index-and-parallel-index "Direct link to Worker index and parallel index") 

Each worker process is assigned two ids: a unique worker index that starts with 1, and a parallel index that is between `0` and `workers - 1`. When a worker is restarted, for example after a failure, the new worker process has the same `parallelIndex` and a new `workerIndex`.

You can read an index from environment variables `process.env.TEST_WORKER_INDEX` and `process.env.TEST_PARALLEL_INDEX`, or access them through [testInfo.workerIndex](/docs/api/class-testinfo#test-info-worker-index) and [testInfo.parallelIndex](/docs/api/class-testinfo#test-info-parallel-index).

### Isolate test data between parallel workers[​](#isolate-test-data-between-parallel-workers "Direct link to Isolate test data between parallel workers") 

You can leverage `process.env.TEST_WORKER_INDEX` or [testInfo.workerIndex](/docs/api/class-testinfo#test-info-worker-index) mentioned above to isolate user data in the database between tests running on different workers. All tests run by the worker reuse the same user.

Create `playwright/fixtures.ts` file that will [create `dbUserName` fixture](/docs/test-fixtures#creating-a-fixture) and initialize a new user in the test database. Use [testInfo.workerIndex](/docs/api/class-testinfo#test-info-worker-index) to differentiate between workers.

playwright/fixtures.ts

``` 
import  from '@playwright/test';
// Import project utils for managing users in the test database.
import  from './my-db-utils';

export * from '@playwright/test';
export const test = baseTest.extend<, >(, use) => `;
    // Initialize user in the database.
    await createUserInTestDatabase(userName);
    await use(userName);
    // Clean up after the tests are done.
    await deleteUserFromTestDatabase(userName);
  }, ],
});
```

Now, each test file should import `test` from our fixtures file instead of `@playwright/test`.

tests/example.spec.ts

``` 
// Important: import our fixtures.
import  from '../playwright/fixtures';

test('test', async () => );
```

## Control test order[​](#control-test-order "Direct link to Control test order") 

Playwright Test runs tests from a single file in the order of declaration, unless you [parallelize tests in a single file](#parallelize-tests-in-a-single-file).

There is no guarantee about the order of test execution across the files, because Playwright Test runs test files in parallel by default. However, if you [disable parallelism](#disable-parallelism), you can control test order by either naming your files in alphabetical order or using a \"test list\" file.

### Sort test files alphabetically[​](#sort-test-files-alphabetically "Direct link to Sort test files alphabetically") 

When you **disable parallel test execution**, Playwright Test runs test files in alphabetical order. You can use some naming convention to control the test order, for example `001-user-signin-flow.spec.ts`, `002-create-new-document.spec.ts` and so on.

### Use a \"test list\" file[​](#use-a-test-list-file "Direct link to Use a "test list" file") 

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiPjwvcGF0aD48L3N2Zz4=)]warning

Tests lists are discouraged and supported as a best-effort only. Some features such as VS Code Extension and tracing may not work properly with test lists.

You can put your tests in helper functions in multiple files. Consider the following example where tests are not defined directly in the file, but rather in a wrapper function.

feature-a.spec.ts

``` 
import  from '@playwright/test';

export default function createTests() ) => );
}
```

feature-b.spec.ts

``` 
import  from '@playwright/test';

export default function createTests()  });

  test('feature-b example test', async () => );
}
```

You can create a test list file that will control the order of tests - first run `feature-b` tests, then `feature-a` tests. Note how each test file is wrapped in a `test.describe()` block that calls the function where tests are defined. This way `test.use()` calls only affect tests from a single file.

test.list.ts

``` 
import  from '@playwright/test';
import featureBTests from './feature-b.spec.ts';
import featureATests from './feature-a.spec.ts';

test.describe(featureBTests);
test.describe(featureATests);
```

Now **disable parallel execution** by setting workers to one, and specify your test list file.

playwright.config.ts

``` 
import  from '@playwright/test';

export default defineConfig();
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

Do not define your tests directly in a helper file. This could lead to unexpected results because your tests are now dependent on the order of `import`/`require` statements. Instead, wrap tests in a function that will be explicitly called by a test list file, as in the example above.