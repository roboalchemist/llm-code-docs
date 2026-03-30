# Source: https://docs.datadoghq.com/developers/integrations/agent_integration.md

---
title: Create an Agent-based Integration
description: Learn how to develop and publish a Datadog Agent integration.
breadcrumbs: Docs > Developers > Datadog Integrations > Create an Agent-based Integration
---

# Create an Agent-based Integration

## Overview{% #overview %}

This page guides Technology Partners through the process of creating an official Datadog Agent integration.

Agent-based integrations are designed to collect telemetry from software or systems running on customer-managed infrastructure, where the Datadog Agent is installed or has network access. These integrations use the [Datadog Agent](https://docs.datadoghq.com/agent/) to collect and submit data through custom agent checks developed by approved Technology Partners.

Agent checks can emit [metrics](https://docs.datadoghq.com/metrics/), [events](https://docs.datadoghq.com/service_management/events/), and [logs](https://docs.datadoghq.com/logs/log_collection/agent_checks/) into a customer's Datadog account. Each agent-based integration is as a Python package built on top of the Datadog Agent, allowing customers to easily [install](https://docs.datadoghq.com/agent/guide/integration-management/?tab=linux#install) it through the Datadog Agent. Traces, however, are collected outside of the agent check using one of Datadog's tracing libraries. For more information, see the [Application Instrumentation documentation](https://docs.datadoghq.com/tracing/trace_collection/).

## Building an agent-based integration{% #building-an-agent-based-integration %}

Before you begin, ensure that you've [joined the Datadog Partner Network](https://docs.datadoghq.com/developers/integrations/?tab=integrations#join-the-datadog-partner-network), have access to a partner developer organization, and have [created a listing in the Developer Platform](https://docs.datadoghq.com/developers/integrations/build_integration/#create-a-listing).

Follow these steps to create your agent-based integration:

1. Install the required development tools.
1. Configure the Datadog Agent integration developer tool.
1. Generate your integration scaffolding.
1. Develop your agent check.
1. Test your integration.
1. Submit your code for review.

### Prerequisites{% #prerequisites %}

Ensure following tools are installed:

- [pipx](https://github.com/pypa/pipx) for installing development tooling and dependencies
- [Datadog Agent Integration Developer Tool](https://docs.datadoghq.com/developers/integrations/python/) (`ddev`) to generate scaffolding and manage integration development
- [Docker](https://docs.docker.com/get-docker/) to run the full test suite
- Git ([command line](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) or [GitHub Desktop client](https://desktop.github.com/))

### Configure the Datadog Agent integration developer tool{% #configure-the-datadog-agent-integration-developer-tool %}

Use the Datadog Agent developer tool to build and test your integration. The setup steps differ depending on whether you're developing an [out-of-the-box (OOTB) integration or a Marketplace integration](https://docs.datadoghq.com/developers/integrations/?tab=integrations#out-of-the-box-integrations-vs-marketplace-offerings). Select the appropriate tab below.

{% tab title="OOTB integration" %}

1. Create a working directory. The developer tool expects your work to be located in `$HOME/dd/`:

   ```shell
   mkdir $HOME/dd && cd $HOME/dd
   ```

1. Fork the [Datadog/integrations-extras](https://github.com/Datadog/integrations-extras) repository to your GitHub account.

1. Clone your fork into the `dd` directory:

   ```shell
   git clone git@github.com:<YOUR_USERNAME>/integrations-extras.git
   ```

1. Create and switch to a new branch for your integration:

   ```shell
   cd integrations-extras
   git switch -c <YOUR_INTEGRATION_NAME> origin/master
   ```

1. Set `extras` as the default working repository:

   ```shell
   ddev config set repo extras
   ```

If your repository is stored outside `$HOME/dd/`, specify the path before setting it as the default:

   ```shell
   ddev config set repos.extras "/path/to/integrations-extras"
   ddev config set repo extras
   ```

{% /tab %}

{% tab title="Marketplace integration" %}

1. Create a working directory. The developer tool expects your work to be located in `$HOME/dd/`:

   ```shell
   mkdir $HOME/dd && cd $HOME/dd
   ```

1. Clone the [Datadog/marketplace](https://github.com/DataDog/marketplace) repository. If you don't have access, request it from your Datadog contact.

   ```shell
   git clone git@github.com:DataDog/marketplace.git
   ```

1. Create and switch to a new branch for your integration:

   ```shell
   cd marketplace
   git switch -c <YOUR_INTEGRATION_NAME> origin/master
   ```

1. Set `marketplace` as the default working repository:

   ```shell
   ddev config set repo marketplace
   ```

If your repository is stored outside `$HOME/dd/`, specify the path before setting it as the default:

   ```shell
   ddev config set repos.marketplace "/path/to/marketplace"
   ddev config set repo marketplace
   ```

{% /tab %}

### Generate your scaffolding{% #generate-your-scaffolding %}

Use the `ddev create` command to generate the initial file and directory structure for your agent-based integration.

{% alert level="info" %}
See the Configuration Method tab in the Developer Platform for the correct command for your integration.
{% /alert %}

1. **Run a dry run (recommended)**

Use the `-n` or `--dry-run` flag to preview the files that are generated, without writing anything to disk. Confirm that the output path matches the expected repository location.

   ```shell
   ddev create -nt check_only <YOUR_INTEGRATION_NAME> --skip-manifest
   ```

1. **Generate the files**

After verifying the directory location, run the same command without the `-n` to create the scaffolding. Follow the prompts to provide integration details.

   ```shell
   ddev create -t check_only <YOUR_INTEGRATION_NAME> --skip-manifest
   ```

### Develop your agent check{% #develop-your-agent-check %}

Each agent-based integration centers around an agent check, a Python class that periodically collects telemetry and submits it to Datadog.

Agent [checks](https://docs.datadoghq.com/glossary/#check) inherit from the `AgentCheck` base class and must meet the following requirements:

- **Python compatibility**:
  - Integrations for Datadog Agent v7+ must support Python 3. All new integrations must target v7+.
  - Integrations for Datadog Agent v5-v6 use Python 2.7.
- **Class inheritance**: Each check must subclass `AgentCheck`.
- **Entry point**: Each check must implement a `check(self, instance)` method.
- **Package structure**: Checks are organized under the `datadog_checks` namespace. For example, an integration named `<INTEGRATION_NAME>` lives in: `<integration_name>/datadog_checks/<integration_name>/`.
- **Naming**:
  - The package name must match the check name.
  - Python module and class names within the package can be freely chosen.

#### Implement check logic{% #implement-check-logic %}

The following example shows logic for an integration named `Awesome`.

This check defines a [service check](https://docs.datadoghq.com/developers/service_checks/) called `awesome.search`, which searches a webpage for a specific string:

- Returns `OK` if the string is found.
- Returns `WARNING` if the page loads but the string is missing.
- Returns `CRITICAL` if the page cannot be reached.

To learn how to submit additional data from your check, see:

- [Custom Agent Check](https://docs.datadoghq.com/metrics/custom_metrics/agent_metrics_submission/?tab=count) for submitting metrics.
- [Agent Integration Log Collection](https://docs.datadoghq.com/logs/log_collection/agent_checks/) for collecting logs from your AgentCheck using `send_log`. Best for single-source log emission.
- [HTTP Crawler Tutorial](https://datadoghq.dev/integrations-core/tutorials/logs/http-crawler/) for collecting logs from multiple log sources, such as when pollin several endpoints or external HTTP APIs.

The file `awesome/datadog_checks/awesome/check.py` might look like this:

In the `check.py` file:

```python
import requests
import time

from datadog_checks.base import AgentCheck, ConfigurationError


class AwesomeCheck(AgentCheck):
    """AwesomeCheck derives from AgentCheck, and provides the required check method."""

    def check(self, instance):
        url = instance.get('url')
        search_string = instance.get('search_string')

        # It's a very good idea to do some basic sanity checking.
        # Try to be as specific as possible with the exceptions.
        if not url or not search_string:
            raise ConfigurationError('Configuration error, please fix awesome.yaml')

        try:
            response = requests.get(url)
            response.raise_for_status()
        # Something went horribly wrong
        except Exception as e:
            # Ideally we'd use a more specific message...
            self.service_check('awesome.search', self.CRITICAL, message=str(e))
            # Submit an error log
            self.send_log({
                'message': f'Failed to access {url}: {str(e)}',
                'timestamp': time.time(),
                'status': 'error',
                'service': 'awesome',
                'url': url
            })
        # Page is accessible
        else:
            # search_string is present
            if search_string in response.text:
                self.service_check('awesome.search', self.OK)
                # Submit an info log
                self.send_log({
                    'message': f'Successfully found "{search_string}" at {url}',
                    'timestamp': time.time(),
                    'status': 'info',
                    'service': 'awesome',
                    'url': url,
                    'search_string': search_string
                })
            # search_string was not found
            else:
                self.service_check('awesome.search', self.WARNING)
                # Submit a warning log
                self.send_log({
                    'message': f'String "{search_string}" not found at {url}',
                    'timestamp': time.time(),
                    'status': 'warning',
                    'service': 'awesome',
                    'url': url,
                    'search_string': search_string
                })
```

To learn more about the base Python class, see [Anatomy of a Python Check](https://github.com/DataDog/datadog-agent/blob/6.2.x/docs/dev/checks/python/check_api.md).

### Write validation tests{% #write-validation-tests %}

There are two types of tests:

- Unit tests for specific functionality
- Integration tests that execute the `check` method and verify proper metrics collection

[pytest](https://docs.pytest.org/en/latest) and [hatch](https://github.com/pypa/hatch) are used to run the tests. Tests are required to publish your integration.

#### Write a unit test{% #write-a-unit-test %}

The first part of the `check` method for Awesome retrieves and verifies two elements from the configuration file. This is a good candidate for a unit test.

Open the file at `awesome/tests/test_awesome.py` and replace the contents with the following:

In the `test_awesome.py` file:

```python
import pytest

    # Don't forget to import your integration

from datadog_checks.awesome import AwesomeCheck
from datadog_checks.base import ConfigurationError


@pytest.mark.unit
def test_config():
    instance = {}
    c = AwesomeCheck('awesome', {}, [instance])

    # empty instance
    with pytest.raises(ConfigurationError):
        c.check(instance)

    # only the url
    with pytest.raises(ConfigurationError):
        c.check({'url': 'http://foobar'})

    # only the search string
    with pytest.raises(ConfigurationError):
        c.check({'search_string': 'foo'})

    # this should not fail
    c.check({'url': 'http://foobar', 'search_string': 'foo'})
```

`pytest` has the concept of markers that can be used to group tests into categories. Notice that `test_config` is marked as a `unit` test.

The scaffolding is set up to run all the tests located in `awesome/tests`. To run the tests, run the following command:

```
ddev test awesome
```

#### Write an integration test{% #write-an-integration-test %}

The unit test above doesn't check the collection logic. To test the logic, you need to create an environment for an integration test and write an integration test.

##### Create an environment for the integration test{% #create-an-environment-for-the-integration-test %}

The toolkit uses `docker` to spin up an NGINX container and lets the check retrieve the welcome page.

To create an environment for the integration test, create a docker-compose file at `awesome/tests/docker-compose.yml` with the following contents:

In the `docker-compose.yml` file:

```yaml
version: "3"

services:
  nginx:
    image: nginx:stable-alpine
    ports:
      - "8000:80"
```

Next, open the file at `awesome/tests/conftest.py` and replace the contents with the following:

In the `conftest.py` file:

```python
import os

import pytest

from datadog_checks.dev import docker_run, get_docker_hostname, get_here

URL = 'http://{}:8000'.format(get_docker_hostname())
SEARCH_STRING = 'Thank you for using nginx.'
INSTANCE = {'url': URL, 'search_string': SEARCH_STRING}


@pytest.fixture(scope='session')
def dd_environment():
    compose_file = os.path.join(get_here(), 'docker-compose.yml')

    # This does 3 things:
    #
    # 1. Spins up the services defined in the compose file
    # 2. Waits for the url to be available before running the tests
    # 3. Tears down the services when the tests are finished
    with docker_run(compose_file, endpoints=[URL]):
        yield INSTANCE


@pytest.fixture
def instance():
    return INSTANCE.copy()
```

#### Add an integration test{% #add-an-integration-test %}

After you've setup an environment for the integration test, add an integration test to the `awesome/tests/test_awesome.py` file:

In the `test_awesome.py` file:

```python
@pytest.mark.integration
@pytest.mark.usefixtures('dd_environment')
def test_service_check(aggregator, instance):
    c = AwesomeCheck('awesome', {}, [instance])

    # the check should send OK
    c.check(instance)
    aggregator.assert_service_check('awesome.search', AwesomeCheck.OK)

    # the check should send WARNING
    instance['search_string'] = 'Apache'
    c.check(instance)
    aggregator.assert_service_check('awesome.search', AwesomeCheck.WARNING)
```

To speed up development, use the `-m/--marker` option to run integration tests only:

```
ddev test -m integration awesome
```

## Test your agent check{% #test-your-agent-check %}

Agent-based integrations are distributed as Python wheel (.whl) files that customers install through the Datadog Agent. Before publishing your integration, you can locally test it by manually bulding and installing the wheel package.

### Build the wheel{% #build-the-wheel %}

The `pyproject.toml` file provides the metadata that is used to package and build the wheel. The wheel contains the files necessary for the functioning of the integration itself, which includes the agent check, configuration example file, and artifacts generated during the wheel build.

To learn more about Python packaging, see [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/).

After your `pyproject.toml` is ready, create a wheel using one of the following options:

- (Recommended) With the `ddev` tooling: `ddev release build <INTEGRATION_NAME>`.
- Without the `ddev` tooling: `cd <INTEGRATION_DIR> && pip wheel . --no-deps --wheel-dir dist`.

### Install the wheel{% #install-the-wheel %}

The wheel is installed using the Agent `integration` command, available in [Agent v6.10.0 or later](https://docs.datadoghq.com/agent/). Depending on your environment, you may need to execute this command as a specific user or with specific privileges:

**Linux** (as `dd-agent`):

```bash
sudo -u dd-agent datadog-agent integration install -w /path/to/wheel.whl
```

**OSX** (as admin):

```bash
sudo datadog-agent integration install -w /path/to/wheel.whl
```

**Windows PowerShell** (Ensure that your shell session has *administrator* privileges):

{% collapsible-section %}
Agent `v6.11` or earlier
```ps
& "C:\Program Files\Datadog\Datadog Agent\embedded\agent.exe" integration install -w /path/to/wheel.whl
```

{% /collapsible-section %}

{% collapsible-section open=null %}
Agent`v6.12` or later
```ps
& "C:\Program Files\Datadog\Datadog Agent\bin\agent.exe" integration install -w /path/to/wheel.whl
```

{% /collapsible-section %}

For installing your wheel to test in Kubernetes environments:

1. Mount the `.whl` file into an initContainer.
1. Run the wheel install in the initContainer.
1. Mount the initContainer in the Agent container while it's running.

For customer install commands for both host and container environments, see the [Community and Marketplace Integrations documentation](https://docs.datadoghq.com/agent/guide/use-community-integrations/).

## Submit your code for review{% #submit-your-code-for-review %}

Open a pull request with your integration directory in the appropriate repo, either [Datadog/integrations-extras](https://github.com/Datadog/integrations-extras) or [Datadog/marketplace](https://github.com/DataDog/marketplace). The pull request is reviewed in parallel with your Developer Platform submission.

## Updating your integration{% #updating-your-integration %}

After your integration is published, you can release updates through the Developer Platform.

### Bumping an integration version{% #bumping-an-integration-version %}

A version bump is needed whenever you add, remove, or modify functionality (for example, when introducing new metrics, updating dashboards, or changing integration code). It's not required for non-functional updates, such as changes to written content, branding, logos, or images.

In Developer Platform, include a new entry in the **Release Notes** tab following this format:

```
## Version Number / Date (YYYY-MM-DD)

***Added***:

* Description of new feature
* Description of new feature

***Fixed***:

* Description of fix
* Description of fix

***Changed***:

* Description of update or improvement
* Description of update or improvement

***Removed***:

* Description of removed feature
* Description of removed feature
```

Make sure to update all references to the version number across the integration's documentation and installation instructions.

## Further reading{% #further-reading %}

- [Create an integration](https://docs.datadoghq.com/developers/integrations/)
- [Python for Agent-based Integration Development](https://docs.datadoghq.com/developers/integrations/python/)
- [Learn how to develop on the Datadog platform](https://docs.datadoghq.com/developers/)
