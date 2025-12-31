# Source: https://playwright.dev/docs/test-annotations

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Playwright Test]
-   [Annotations]

On this page

<div>

# Annotations

</div>

## Introduction[​](#introduction "Direct link to Introduction") 

Playwright supports tags and annotations that are displayed in the test report.

You can add your own tags and annotations at any moment, but Playwright comes with a few built-in ones:

-   [test.skip()](/docs/api/class-test#test-skip) marks the test as irrelevant. Playwright does not run such a test. Use this annotation when the test is not applicable in some configuration.
-   [test.fail()](/docs/api/class-test#test-fail) marks the test as failing. Playwright will run this test and ensure it does indeed fail. If the test does not fail, Playwright will complain.
-   [test.fixme()](/docs/api/class-test#test-fixme) marks the test as failing. Playwright will not run this test, as opposed to the `fail` annotation. Use `fixme` when running the test is slow or crashes.
-   [test.slow()](/docs/api/class-test#test-slow) marks the test as slow and triples the test timeout.

Annotations can be added to a single test or a group of tests.

Built-in annotations can be conditional, in which case they apply when the condition is truthy, and may depend on test fixtures. There could be multiple annotations on the same test, possibly in different configurations.

## Focus a test[​](#focus-a-test "Direct link to Focus a test") 

You can focus some tests. When there are focused tests, only these tests run.

``` 
test.only('focus this test', async () => );
```

## Skip a test[​](#skip-a-test "Direct link to Skip a test") 

Mark a test as skipped.

``` 
test.skip('skip this test', async () => );
```

## Conditionally skip a test[​](#conditionally-skip-a-test "Direct link to Conditionally skip a test") 

You can skip certain test based on the condition.

``` 
test('skip this test', async () => );
```

## Group tests[​](#group-tests "Direct link to Group tests") 

You can group tests to give them a logical name or to scope before/after hooks to the group.

``` 
import  from '@playwright/test';

test.describe('two tests', () => ) => );

  test('two', async () => );
});
```

## Tag tests[​](#tag-tests "Direct link to Tag tests") 

Sometimes you want to tag your tests as `@fast` or `@slow`, and then filter by tag in the test report. Or you might want to only run tests that have a certain tag.

To tag a test, either provide an additional details object when declaring a test, or add `@`-token to the test title. Note that tags must start with `@` symbol.

``` 
import  from '@playwright/test';

test('test login page', , async () => );

test('test full report @slow', async () => );
```

You can also tag all tests in a group or provide multiple tags:

``` 
import  from '@playwright/test';

test.describe('group', , () => ) => );

  test('test full report', , async () => );
});
```

You can now run tests that have a particular tag with [`--grep`](/docs/test-cli#all-options) command line option.

-   Bash
-   PowerShell
-   Batch

``` 
npx playwright test --grep @fast
```

``` 
npx playwright test --grep "@fast"
```

``` 
npx playwright test --grep @fast
```

Or if you want the opposite, you can skip the tests with a certain tag:

-   Bash
-   PowerShell
-   Batch

``` 
npx playwright test --grep-invert @fast
```

``` 
npx playwright test --grep-invert "@fast"
```

``` 
npx playwright test --grep-invert @fast
```

To run tests containing either tag (logical `OR` operator):

-   Bash
-   PowerShell
-   Batch

``` 
npx playwright test --grep "@fast|@slow"
```

``` 
npx playwright test --grep --% "@fast^|@slow"
```

``` 
npx playwright test --grep "@fast^|@slow"
```

Or run tests containing both tags (logical `AND` operator) using regex lookaheads:

``` 
npx playwright test --grep "(?=.*@fast)(?=.*@slow)"
```

You can also filter tests in the configuration file via [testConfig.grep](/docs/api/class-testconfig#test-config-grep) and [testProject.grep](/docs/api/class-testproject#test-project-grep).

## Annotate tests[​](#annotate-tests "Direct link to Annotate tests") 

If you would like to annotate your tests with something more substantial than a tag, you can do that when declaring a test. Annotations have a `type` and a `description` for more context and available in reporter API. Playwright\'s built-in HTML reporter shows all annotations, except those where `type` starts with `_` symbol.

For example, to annotate a test with an issue url:

``` 
import  from '@playwright/test';

test('test login page', ,
}, async () => );
```

You can also annotate all tests in a group or provide multiple annotations:

``` 
import  from '@playwright/test';

test.describe('report tests', ,
}, () => ) => );

  test('test full report', ,
      ,
    ],
  }, async () => );
});
```

## Conditionally skip a group of tests[​](#conditionally-skip-a-group-of-tests "Direct link to Conditionally skip a group of tests") 

For example, you can run a group of tests just in Chromium by passing a callback.

example.spec.ts

``` 
test.describe('chromium only', () => ) => browserName !== 'chromium', 'Chromium only!');

  test.beforeAll(async () => );

  test('test 1', async () => );

  test('test 2', async () => );
});
```

## Use fixme in `beforeEach` hook[​](#use-fixme-in-beforeeach-hook "Direct link to use-fixme-in-beforeeach-hook") 

To avoid running `beforeEach` hooks, you can put annotations in the hook itself.

example.spec.ts

``` 
test.beforeEach(async () => );

test('user profile', async () => );
```

## Runtime annotations[​](#runtime-annotations "Direct link to Runtime annotations") 

While the test is already running, you can add annotations to [`test.info().annotations`](/docs/api/class-testinfo#test-info-annotations).

example.spec.ts

``` 
test('example test', async () => );

  // ...
});
```