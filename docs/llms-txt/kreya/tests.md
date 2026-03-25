# Source: https://kreya.app/docs/scripting-and-tests/tests.md

# Tests [Pro / Enterprise](/pricing.md)

Kreya makes it easy to validate API responses and ensure your workflows behave as expected. The recommended way to test in Kreya is with [snapshot tests](/docs/scripting-and-tests/tests/snapshot-testing.md), which require no coding, just enable them in the settings and Kreya will automatically capture and compare your API responses. For more advanced scenarios, you can also define custom tests directly in your scripts.

## [📄️<!-- --> <!-- -->Snapshot tests](/docs/scripting-and-tests/tests/snapshot-testing.md)

[Learn how to use snapshot tests in Kreya to automatically validate API responses.](/docs/scripting-and-tests/tests/snapshot-testing.md)

## [📄️<!-- --> <!-- -->Scripting tests](/docs/scripting-and-tests/tests/scripting-tests.md)

[Learn how to write custom test assertions using scripts in Kreya.](/docs/scripting-and-tests/tests/scripting-tests.md)

## Running tests[​](#running-tests "Direct link to Running tests")

Tests run as part of every execution flow in Kreya, whether you start an individual operation, a collection sequence, or a script. Each run executes the associated tests automatically after the operation completes, so you get immediate feedback without extra clicks.

### Running tests in CI/CD[​](#running-tests-in-cicd "Direct link to Running tests in CI/CD")

Use the Kreya CLI `kreyac` to run the same tests in your pipelines. Invoking operations, collections, or scripts via the CLI executes their tests, making it straightforward to validate changes in CI/CD. See the [CLI documentation](/docs/cli.md) for command examples like `kreyac collection invoke` or `kreyac script invoke`, and use the `--test-report-junit` flag to produce a JUnit report for CI systems to consume.

## Viewing test results[​](#viewing-test-results "Direct link to Viewing test results")

Test results are displayed in the **Tests** tab, which provides a clear overview of passed and failed tests. The tab header shows the total number of passed tests, and detailed error messages are displayed for any failed tests.

![Viewing Kreya test results](/assets/ideal-img/viewing-tests.8d8059f.400.png)

## Key features of the tests tab[​](#key-features-of-the-tests-tab "Direct link to Key features of the tests tab")

* **Real-time feedback**: See test results immediately after running your scripts.
* **Detailed error messages**: Quickly identify and debug failed tests.
* **Organized view**: Easily navigate through multiple test cases.
* **Snapshot diffing**: When a snapshot changes, you can view a visual diff to easily see what has changed and decide whether to accept or reject the update.
