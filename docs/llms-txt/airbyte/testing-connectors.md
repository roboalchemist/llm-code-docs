# Source: https://docs.airbyte.com/platform/connector-development/testing-connectors.md

# Source: https://docs.airbyte.com/platform/2.0/connector-development/testing-connectors.md

# Source: https://docs.airbyte.com/platform/1.8/connector-development/testing-connectors.md

# Source: https://docs.airbyte.com/platform/1.7/connector-development/testing-connectors.md

# Source: https://docs.airbyte.com/platform/1.6/connector-development/testing-connectors.md

# Testing Connectors

Copy Page

Multiple tests suites compose the Airbyte connector testing pyramid

## Tests run by our CI pipeline[​](#tests-run-by-our-ci-pipeline "Direct link to Tests run by our CI pipeline")

* [Connector QA Checks](/community/contributing-to-airbyte/resources/qa-checks.md): Static asset checks that validate that a connector is correctly packaged to be successfully released to production.
* Unit Tests: Connector-specific tests written by the connector developer which don’t require access to the source/destination.
* Integration Tests: Connector-specific tests written by the connector developer which *may* require access to the source/destination.
* [Connector Acceptance Tests](https://docs.airbyte.com/connector-development/testing-connectors/connector-acceptance-tests-reference/): Connector-agnostic tests that verify that a connector adheres to the [Airbyte protocol](https://docs.airbyte.com/understanding-airbyte/airbyte-protocol). Credentials to a source/destination sandbox account are **required**.
* [Regression Tests](https://github.com/airbytehq/airbyte/tree/master/airbyte-ci/connectors/live-tests): Connector-agnostic tests that verify that the behavior of a connector hasn’t changed unexpectedly between connector versions. A sandbox cloud connection is required. Currently only available for API source connectors.

## 🤖 CI[​](#-ci "Direct link to 🤖 CI")

If you want to run the global test suite, exactly like what is run in CI, you should install [`airbyte-ci` CLI](https://github.com/airbytehq/airbyte/blob/master/airbyte-ci/connectors/pipelines/README.md) and use the following command:

```
airbyte-ci connectors --name=<connector_name> test
```

CI will run all the tests that are available for a connector. This can include all of the tests listed above, if we have the appropriate credentials. At a minimum, it will include the Connector QA checks and any tests that exist in a connector's `unit_tests` and `integration_tests` directories. To run Connector Acceptance tests locally, you must provide connector configuration as a `config.json` file in a `.secrets` folder in the connector code directory. Regression tests may only be run locally with authorization to our cloud resources.

Our CI infrastructure runs the connector tests with [`airbyte-ci` CLI](https://github.com/airbytehq/airbyte/blob/master/airbyte-ci/connectors/pipelines/README.md). Connectors tests are automatically and remotely triggered on your branch according to the changes made in your branch. **Passing tests are required to merge a connector pull request.**

## Connector specific tests[​](#connector-specific-tests "Direct link to Connector specific tests")

### 🐍 Python connectors[​](#-python-connectors "Direct link to 🐍 Python connectors")

We use `pytest` to run unit and integration tests:

```
# From connector directory
poetry run pytest
```

### ☕ Java connectors[​](#-java-connectors "Direct link to ☕ Java connectors")

warning

Airbyte is revamping its core Java destinations codebase. We're not reviewing/accepting new Java connectors at this time.

We run Java connector tests with gradle.

```
# Unit tests
./gradlew :airbyte-integrations:connectors:source-postgres:test
# Integration tests
./gradlew :airbyte-integrations:connectors:source-postgres:integrationTestJava
```

Please note that according to the test implementation you might have to provide connector configurations as a `config.json` file in a `.secrets` folder in the connector code directory.
