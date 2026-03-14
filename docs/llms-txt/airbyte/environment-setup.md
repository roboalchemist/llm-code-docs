# Source: https://docs.airbyte.com/platform/connector-development/tutorials/custom-python-connector/environment-setup.md

# Source: https://docs.airbyte.com/platform/2.0/connector-development/tutorials/custom-python-connector/environment-setup.md

# Source: https://docs.airbyte.com/platform/1.8/connector-development/tutorials/custom-python-connector/environment-setup.md

# Source: https://docs.airbyte.com/platform/1.7/connector-development/tutorials/custom-python-connector/environment-setup.md

# Source: https://docs.airbyte.com/platform/1.6/connector-development/tutorials/custom-python-connector/environment-setup.md

# Environment setup

Copy Page

Let's first start by cloning the repository, optionally forking it first

```
git clone git@github.com:airbytehq/airbyte.git
cd airbyte
```

Next, you will want to create a new connector.

## Initialize connector project[​](#initialize-connector-project "Direct link to Initialize connector project")

```
git clone git@github.com:airbytehq/airbyte.git
cd airbyte

# Make a directory for a new connector and navigate to it
mkdir airbyte-integrations/connectors/source-exchange-rates-tutorial
cd airbyte-integrations/connectors/source-exchange-rates-tutorial

# Initialize a project, follow Poetry prompts, and then add airbyte-cdk as a dependency.
poetry init
poetry add airbyte-cdk
```

For this walkthrough, we'll refer to our source as `exchange-rates-tutorial`.

## Add Connector Metadata file[​](#add-connector-metadata-file "Direct link to Add Connector Metadata file")

Each Airbyte connector needs to have a valid `metadata.yaml` file in the root of the connector directory. [Here is metadata.yaml format documentation](/platform/1.6/connector-development/connector-metadata-file.md).

## Implement connector entrypoint scripts[​](#implement-connector-entrypoint-scripts "Direct link to Implement connector entrypoint scripts")

Airbyte connectors are expected to be able to run `spec`, `check`, `discover`, and `read` commands. You can use `run.py` file in Airbyte connectors as an example of how to implement them.

## Running operations[​](#running-operations "Direct link to Running operations")

```
poetry run source-survey-monkey-demo check --config secrets/config.json
```

It should return a failed connection status

```
{
  "type": "CONNECTION_STATUS",
  "connectionStatus": {
    "status": "FAILED",
    "message": "Config validation error: 'TODO' is a required property"
  }
}
```

The discover operation should also fail as expected

```
poetry run source-survey-monkey-demo discover --config secrets/config.json
```

It should fail because `TODO' is a required property`

The read operation should also fail as expected

```
poetry run source-survey-monkey-demo read --config secrets/config.json --catalog integration_tests/configured_catalog.json
```

It should fail because `TODO' is a required property`

We're ready to start development. In the [next section](/platform/1.6/connector-development/tutorials/custom-python-connector/reading-a-page.md), we'll read a page of records from the surveys endpoint.
