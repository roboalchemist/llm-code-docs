# Source: https://docs.mage.ai/production/configuring-production-settings/overview.md

# Source: https://docs.mage.ai/production/ci-cd/overview.md

# Source: https://docs.mage.ai/production/authentication/permissions/overview.md

# Source: https://docs.mage.ai/production/authentication/overview.md

# Source: https://docs.mage.ai/orchestration/pipeline-runs/overview.md

# Source: https://docs.mage.ai/orchestration/backfills/overview.md

# Source: https://docs.mage.ai/introduction/overview.md

# Source: https://docs.mage.ai/guides/overview.md

# Source: https://docs.mage.ai/guides/dbt/overview.md

# Source: https://docs.mage.ai/extensibility/pro-api-reference/overview.md

# Source: https://docs.mage.ai/extensibility/pro-api-reference/deployments/overview.md

# Source: https://docs.mage.ai/extensibility/global-hooks/overview.md

# Source: https://docs.mage.ai/extensibility/global-data-products/overview.md

# Source: https://docs.mage.ai/extensibility/api-reference/sessions/overview.md

# Source: https://docs.mage.ai/extensibility/api-reference/pipelines/overview.md

# Source: https://docs.mage.ai/extensibility/api-reference/pipeline-schedules/overview.md

# Source: https://docs.mage.ai/extensibility/api-reference/pipeline-runs/overview.md

# Source: https://docs.mage.ai/extensibility/api-reference/overview.md

# Source: https://docs.mage.ai/extensibility/api-reference/oauth-access-tokens/overview.md

# Source: https://docs.mage.ai/extensibility/api-reference/logs/overview.md

# Source: https://docs.mage.ai/extensibility/api-reference/blocks/overview.md

# Source: https://docs.mage.ai/extensibility/api-reference/backfills/overview.md

# Source: https://docs.mage.ai/development/variables/overview.md

# Source: https://docs.mage.ai/data-integrations/sources/overview.md

# Source: https://docs.mage.ai/data-integrations/overview.md

# Source: https://docs.mage.ai/data-integrations/destinations/overview.md

# Source: https://docs.mage.ai/contributing/overview.md

# Source: https://docs.mage.ai/contributing/frontend/overview.md

# Source: https://docs.mage.ai/contributing/documentation/overview.md

# Source: https://docs.mage.ai/contributing/backend/testing/overview.md

# Source: https://docs.mage.ai/contributing/backend/overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Contributing to the backend server

> Mage backend code is written in Python 🐍 and our server uses the Tornado 🌪️ framework. Here are some guides on adding features to the Mage backend.

## Guides

### API

* [Overview](/api-reference/overview)

### Data integrations

* [Add a new source to the data integration pipeline](/contributing/data-integrations/add-new-source)
* [Add a new destination to the data integration pipeline](/contributing/data-integrations/add-new-destination)

### Streaming pipelines

* [Add a new source or destination to the streaming pipeline](/contributing/backend/streaming/sources-and-destinations)

### IO classes

* [Add a new IO class](/contributing/backend/io/adding-a-class)

## Style guide

### Linter

Install `flake8` in your IDE to lint the Python code.

To run the linter locally, execute this script:

```bash  theme={"system"}
./scripts/server/lint.sh
```

## Testing

### Unit tests

Add unit tests for the feature in
[mage\_ai/tests](https://github.com/mage-ai/mage-ai/tree/master/mage_ai/tests) directory.

To run the tests locally, execute this script:

```bash  theme={"system"}
./scripts/server/test.sh
```

It is also possible to run unit tests directly in a live docker instance, as given in the following steps.

1. Find out the backend server container name, with the command `docker container ls` in a terminal:

```bash  theme={"system"}
 % docker container ls

CONTAINER ID   IMAGE       COMMAND                  CREATED      STATUS          PORTS                    NAMES
8dbcfbe41755   mage/data   "./scripts/install_a…"   5 days ago   Up 38 minutes   0.0.0.0:3000->3000/tcp   mage-ai-app-1
b9d811e1e3e8   mage/data   "python mage_ai/serv…"   5 days ago   Up 38 minutes   0.0.0.0:6789->6789/tcp   mage-ai-server-1
```

2. Start an interactive `bash` session with the backend server container:

```bash  theme={"system"}
% docker exec -it mage-ai-server-1 /bin/bash
```

3. Run unit tests with the following command:

```bash  theme={"system"}
root@b9d811e1e3e8:/home/src# python3 -m unittest discover -s mage_ai.tests --failfast
```

## Debugging

<Snippet file="debugging-backend.mdx" />


Built with [Mintlify](https://mintlify.com).