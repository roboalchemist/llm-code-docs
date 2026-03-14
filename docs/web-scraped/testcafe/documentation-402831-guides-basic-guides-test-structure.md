# Source: https://testcafe.io/documentation/402831/guides/basic-guides/test-structure

Title: Test Structure | Basic Guides | Guides

URL Source: https://testcafe.io/documentation/402831/guides/basic-guides/test-structure

Markdown Content:
This article describes how to structure TestCafe files.

[](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#article-summary)Article Summary[](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#article-summary)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

TestCafe test files consist of [fixtures](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#fixtures). Fixtures are groups of [tests](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#tests) that share the same starting URL. [Hooks](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#hooks) run before and after other parts of the test suite. You can attach hooks to fixtures, tests, and entire test runs.

Example:

```
fixture`Test structure`
    .page`https://devexpress.github.io/testcafe/example`;

test('Test1', async t => {
    // Starts at http://devexpress.github.io/testcafe/example
});
```

[](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#table-of-contents)Table of Contents[](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#table-of-contents)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   [Fixtures](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#fixtures)
    *   [Declare a fixture](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#declare-a-fixture)
        *   [Absolute fixture URL](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#absolute-fixture-url)
        *   [Relative fixture URL](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#relative-fixture-url)

*   [Tests](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#tests)
    *   [Declare a Test](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#declare-a-test)
    *   [Specify Test Content](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#specify-test-content)
    *   [Specify a Custom Starting URL](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#specify-a-custom-starting-url)
        *   [Relative test URL](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#relative-test-url)

*   [Hooks](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#hooks)
    *   [Hook Types](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#hook-types)
        *   [Hooks by entity](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#hooks-by-entity)
        *   [Local Hooks and Global Hooks](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#local-hooks-and-global-hooks)

[](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#fixtures)Fixtures[](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#fixtures)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Note

If you use [eslint](https://eslint.org/), install the [TestCafe plugin](https://www.npmjs.com/package/eslint-plugin-testcafe) to avoid the `'fixture' is not defined` and `'test' is not defined` errors.

TestCafe test files begin with a fixture declaration. A fixture is a group of tests. Every test belongs to a fixture.

It is best to use one fixture per test file. If your test suite contains tests with different starting URLs, place these tests into several test files - one for each starting URL. Alternatively, you can [specify the starting URL](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#specify-a-custom-starting-url) on a test-by-test basis.

### [](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#declare-a-fixture)Declare a fixture[](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#declare-a-fixture)

Declare a fixture with the `fixture` keyword.

```
fixture`Test structure`
```

The `fixture.page` method defines the starting URL of the tests in the fixture. If you set a suite-wide [base URL](https://testcafe.io/documentation/402638/reference/configuration-file#base-url), you can omit this method.

#### [](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#absolute-fixture-url)Absolute fixture URL[](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#absolute-fixture-url)

An absolute fixture URL takes priority over the suite-wide [base URL](https://testcafe.io/documentation/402638/reference/configuration-file#base-url).

```
fixture`Test structure`
    .page`https://devexpress.github.io/testcafe/example`;

test('Test1', async t => {
    // Starts at http://devexpress.github.io/testcafe/example
});
```

#### [](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#relative-fixture-url)Relative fixture URL[](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#relative-fixture-url)

If you set a suite-wide [base URL](https://testcafe.io/documentation/402638/reference/configuration-file#base-url), you can define a relative starting URL for the tests in the fixture. Relative URLs begin with the period character (`.`).

For example, if your configuration file contains the following declaration:

```
"baseUrl": "https://devexpress.github.io/testcafe"
```

You can define your fixture URL as such:

```
fixture`Test structure`
    .page`./example`;

test('Test1', async t => {
    // Starts at http://devexpress.github.io/testcafe/example
});
```

[](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#tests)Tests[](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#tests)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Tests belong to fixtures. The code for tests that constitute a particular fixture follow that fixture’s [declaration](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#declare-a-fixture).

### [](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#declare-a-test)Declare a Test[](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#declare-a-test)

Declare a test with the `test` keyword. Pass two arguments to the `test` function - a string with the test’s name and an asynchronous function with test content.

```
fixture`Test structure`;

test('Test1', async t => {
    /* Test 1 Code */
});

test('Test2', async t => {
    /* Test 2 Code */
});
```

The asynchronous function with the test content needs to receive the [test controller](https://testcafe.io/documentation/402665/reference/test-api/testcontroller)`t` object as an argument. The test controller object provides access to the TestCafe test API.

### [](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#specify-test-content)Specify Test Content[](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#specify-test-content)

Use TestCafe [actions](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions) to interact with the page. Use [element selectors](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors) and [client functions](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions) to retrieve client-side information. Use [assertions](https://testcafe.io/documentation/402837/guides/basic-guides/assertions) to evaluate page data and determine if a test is successful.

The internal structure of TestCafe tests is up to the individual user. TestCafe tests may include any code, as long as it is valid. TestCafe tests can reference third-party libraries and communicate with other APIs.

### [](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#specify-a-custom-starting-url)Specify a Custom Starting URL[](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#specify-a-custom-starting-url)

Use the [test.page](https://testcafe.io/documentation/402732/reference/test-api/test/page) function to override the starting URL from the [fixture definition](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#declare-a-fixture).

```
fixture`Test structure`
    .page`https://devexpress.github.io/testcafe/example`;

test('My test', async t => {
    // Starts at http://devexpress.github.io/testcafe/blog/
}).page`https://devexpress.github.io/testcafe/blog/`;
```

#### [](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#relative-test-url)Relative test URL[](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#relative-test-url)

If you set a suite-wide [base URL](https://testcafe.io/documentation/402638/reference/configuration-file#base-url), you can define a relative starting URL for the test. Relative URLs begin with the period character (`.`).

For example, if your configuration file contains the following declaration:

```
"baseUrl": "https://devexpress.github.io/testcafe"
```

You can define a custom test URL as such:

```
fixture`Test structure`
    .page`./example`;

test('Test1', async t => {
    // Starts at http://devexpress.github.io/testcafe/example
});
```

[](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#hooks)Hooks[](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#hooks)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Note

Test hooks and request hooks are different entities. Read the [Request Interception Guide](https://testcafe.io/documentation/402669/reference/test-api/requesthook) for more information on request hooks.

Hooks are functions that run immediately before or immediately after other test entities. You can attach hooks to the following test entities: [tests, fixtures, and test runs](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#hooks-by-entity).

“Before” hooks often prepare the testing environment (for example, to authenticate the user) for future tests. Likewise, “after” hooks often ‘reset’ the testing environment (for example, to remove a database object) after the end of a test.

You can attach a single hook to multiple entities of the same kind, which helps you reuse setup and teardown code.

### [](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#hook-types)Hook Types[](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#hook-types)

#### [](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#hooks-by-entity)Hooks by entity[](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#hooks-by-entity)

The following two hooks run [before and after test runs](https://testcafe.io/documentation/403435/guides/intermediate-guides/hooks#hooks-before-and-after-test-runs):

*   testRun.before
*   testRun.after

The following two hooks run [before and after fixtures](https://testcafe.io/documentation/403435/guides/intermediate-guides/hooks#hooks-before-and-after-fixtures):

*   [fixture.before](https://testcafe.io/documentation/402785/reference/test-api/fixture/before)
*   [fixture.after](https://testcafe.io/documentation/402787/reference/test-api/fixture/after)

The following four hooks run [before and after tests](https://testcafe.io/documentation/403435/guides/intermediate-guides/hooks#hooks-before-and-after-tests):

*   [fixture.beforeEach](https://testcafe.io/documentation/402784/reference/test-api/fixture/beforeeach)
*   [fixture.afterEach](https://testcafe.io/documentation/402786/reference/test-api/fixture/aftereach)
*   [test.before](https://testcafe.io/documentation/402738/reference/test-api/test/before)
*   [test.after](https://testcafe.io/documentation/402739/reference/test-api/test/after)

#### [](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#local-hooks-and-global-hooks)Local Hooks and Global Hooks[](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#local-hooks-and-global-hooks)

**Local** hooks reside inside individual test files. These hooks do not affect the rest of the test suite.

**Global** hooks apply to your entire test suite. You can only define them in a [JavaScript configuration file](https://testcafe.io/documentation/402638/reference/configuration-file#javascript).

Test and fixture hooks can be either _local_ or _global_. Test run hooks are only _global_.

Read the [Hooks guide](https://testcafe.io/documentation/403435/guides/intermediate-guides/hooks) to learn more.
