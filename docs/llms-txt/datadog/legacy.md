# Source: https://docs.datadoghq.com/developers/guide/legacy.md

---
title: Create an Agent check for Datadog Agent 5
description: Learn how to create an Agent check for Datadog Agent 5.
breadcrumbs: >-
  Docs > Developers > Developer Guides > Create an Agent check for Datadog Agent
  5
---

# Create an Agent check for Datadog Agent 5

This documentation explains how to create an Agent check for Datadog Agent v5, which has been superseded by Agent v6. It is still possible to write your own local checks for v5, however no new integrations for v5 are considered upstream. To learn more about creating integrations for Agent v6, see [Create a New Integration](https://docs.datadoghq.com/developers/integrations/agent_integration).

## Requirements{% #requirements %}

You need a working [Ruby](https://www.ruby-lang.org) environment. For more information on installing Ruby, see [Installing Ruby](https://www.ruby-lang.org/en/documentation/installation).

You also need [Wget](https://www.gnu.org/software/wget). Wget is already installed on most Linux systems. Use [Homebrew](https://brew.sh) on Mac or [Chocolatey](https://chocolatey.org) on Windows.

## Setup{% #setup %}

There is [a gem](https://rubygems.org/gems/datadog-sdk-testing) and a set of scripts to help you get set up, ease development, and provide testing. To begin:

1. Fork the [integrations-extras repository](https://github.com/DataDog/integrations-extras) on Github and clone the repository to your dev environment.
1. Run `gem install bundler`
1. Run `bundle install`

Once the required Ruby gems have been installed by Bundler, create a Python environment.

1. Run `rake setup_env`. This installs a Python virtual environment along with all the components necessary for integration development (including the core Agent used by the integrations). Some basic software might be needed to install the python dependencies like `gcc` and `libssl-dev`.

1. Run `source venv/bin/activate` to activate the installed Python virtual environment. To exit the virtual environment, run `deactivate`. Learn more about the Python virtual environment on the [Virtualenv documentation](https://virtualenv.pypa.io/en/stable).

## Building an integration{% #building-an-integration %}

Use rake to generate the skeleton for a new integration by running: `rake generate:skeleton[my_integration]`, where *my\_integration* is the name of your new integration (note: enclose your integration name in square brackets).

This creates a new directory, `my_integration`, that contains all the files required for your new integration. This also creates an entry for your new integration in the `.travis.yml` and `circle.yml` continuous integration files to ensure that your tests are run whenever new builds are created.

### Integration files{% #integration-files %}

New integrations should contain the following files:

#### `README.md`{% #readmemd %}

The README file must provide the following sections:

- **Overview** (required): Let others know what they can expect to do with your integration.
- **Installation** (required): Provide information about how to install your integration.
- **Configuration** (required): Detail any steps necessary to configure your integration or the service you are integrating.
- **Validation** (required): How can users ensure the integration is working as intended?
- **Troubleshooting**: Help other users by sharing solutions to common problems they might experience.
- **Compatibility** (required): List the version(s) of the application or service that your integration has been tested and validated against.
- **Metrics** (required): Include a list of the metrics your integration provides.
- **Events**: Include a list of events if your integration provides any.
- **Service checks**: Include a list of service checks if your integration provides any.

For more information, see [Create an Agent-based Integration](https://docs.datadoghq.com/developers/integrations/agent_integration).

#### `check.py`{% #checkpy %}

The file where your check logic should reside. The skeleton function boilerplates an integration class for your integration, including a `check` method where you should place your check logic.

For example:

```python

# Example check.py
import time
from checks import AgentCheck

class MyIntegrationCheck(AgentCheck):
  def __init__(self, name, init_config, agentConfig, instances=None):
    AgentCheck.__init__(self, name, init_config, agentConfig, instances)

  def check(self, instance):
    # Send a custom event.
    self.event({
      'timestamp': int(time.time()),
      'source_type_name': 'my_integration',
      'msg_title': 'Custom event',
      'msg_text': 'My custom integration event occurred.',
      'host': self.hostname,
      'tags': [
          'action:my_integration_custom_event',
      ]
    })
```

For more information about writing integrations and sending metrics with the Datadog Agent, see [Introduction to Agent-based Integrations](https://docs.datadoghq.com/developers/integrations/).

If you need to import any third party libraries, add them to the `requirements.txt` file.

##### `ci/my_integration.rake`{% #cimy_integrationrake %}

If your tests require a testing environment, use the `install` and `cleanup` tasks to respectively set up and tear down a testing environment.

For example:

```ruby
# Example my_integration.rake
namespace :ci do
  namespace :my_integration do |flavor|
    task install: ['ci:common:install'] do

      # Use the Python Virtual Environment and install packages.
      use_venv = in_venv
      install_requirements('my_integration/requirements.txt',
                           "--cache-dir #{ENV['PIP_CACHE']}",
                           "#{ENV['VOLATILE_DIR']}/ci.log",
                           use_venv)

      # Setup a docker testing container.
      $(docker run -p 80:80 --name my_int_container -d my_docker)
```

For more information about writing integration tests, see the documentation in the [Datadog Agent repository](https://github.com/DataDog/dd-agent/blob/master/tests/README.md#integration-tests). You can also reference the [ci common library](https://github.com/DataDog/dd-agent/blob/master/ci/common.rb) for helper functions such as `install_requirements` and `sleep_for`.

**Note**: You may notice the variable `flavor` in this file and other areas of testing. *Flavor* is a term used to denote variations of integrated software, typically versions. This allows you to write one set of tests, but target different *flavors*, variants, or versions of the software you are integrating.

#### `conf.yaml.example`{% #confyamlexample %}

To install your integration, you need to configure it for your specific instances. To do this, copy the `conf.yaml.example` file into your Agent's `conf.d` directory, then update it with your instance specific information.

Your `conf.yaml.example` file should provide two sections:

- `init_config` for any globally configured parameters
- `instances` for specific instances to integrate. This often includes a server or host address with additional parameters such as authentication information, additional tags and configuration settings.

##### `manifest.json`{% #manifestjson %}

This JSON file provides metadata about your integration and should include:

- **`maintainer`**: Provide a valid email address where you can be contacted regarding this integration.
- **`manifest_version`**: The version of this manifest file.
- **`max_agent_version`**: The maximum version of the Datadog Agent that is compatible with your integration. Datadog tries to maintain integration stability within major versions, so you should leave this at the number generated for you. If your integration breaks with a new release of the Datadog Agent, set this number and [submit an issue on the Datadog Agent project](https://github.com/DataDog/dd-agent/blob/master/CONTRIBUTING.md#submitting-issues).
- **`min_agent_version`**: The minimum version of the Datadog Agent that is compatible with your integration.
- **`name`**: The name of your integration.
- **`short_description`**: Provide a short description of your integration.
- **`support`**: As a community contributed integration, this should be set to "contrib". Only set this to another value if directed to do so by Datadog staff.
- **`version`**: The current version of your integration.
- **`is_public`**: Boolean set to true if your integration is public
- **`has_logo`**: Boolean set to true if there is a logo for this integration in `/src/images/integrations_logo`
- **`type`**: **check**
- **`categories`**: Categories to classify your [Integration](https://docs.datadoghq.com/integrations) in the Datadog documentation.

Reference one of the existing integrations [for an example of the manifest file](https://github.com/DataDog/integrations-core/blob/master/activemq/manifest.json).

#### `metadata.csv`{% #metadatacsv %}

The metadata CSV contains a list of the metrics your integration provides and basic details that help inform the Datadog web application as to which graphs and alerts can be provided for the metric.

The CSV should include a header row and the following columns:

**`metric_name`** (required): The name of the metric as it should appear on the Datadog site when creating dashboards or monitors. Often this name is a period delimited combination of the provider, service, and metric, for example: `aws.ec2.disk_write_ops`) or the application, application feature, and metric, for example: `apache.net.request_per_s`.

**`metric_type`** (required): The type of metric you are reporting. This influences how the Datadog web application handles and displays your data. Accepted values are: `count`, `gauge`, or `rate`.

- `count`: A count is the number of particular events that have occurred. When reporting a count, you should only submit the number of new events (delta) recorded since the previous submission. For example, the `aws.apigateway.5xxerror` metric is a `count` of the number of server-side errors.
- `gauge`: A gauge is a metric that tracks a value at a specific point in time. For example, `docker.io.read_bytes` is a `gauge` of the number of bytes read per second.
- `rate`: A rate a metric over time (and as such, typically includes a `per_unit_name` value). For example, `lighttpd.response.status_2xx` is a `rate` metric capturing the number of 2xx status codes produced per second.

**`interval`**: The interval used for conversion between rates and counts. This is required when the `metric_type` is set to the `rate` type.

**`unit_name`**: The label for the unit of measure you are gathering. The following units (grouped by type) are available:

- **Bytes**: `bit`, `byte`, `kibibyte`, `mebibyte`, `gibibyte`, `tebibyte`, `pebibyte`, `exbibyte`
- **Cache**: `eviction`, `get`, `hit`, `miss`, `set`
- **Database**: `assertion`, `column`, `command`, `commit`, `cursor`, `document`, `fetch`, `flush`, `index`, `key`, `lock`, `merge`, `object`, `offset`, `query`, `question`, `record`, `refresh`, `row`, `scan`, `shard`, `table`, `ticket`, `transaction`, `wait`
- **Disk**: `block`, `file`, `inode`, `sector`
- **Frequency**: `hertz`, `kilohertz`, `megahertz`, `gigahertz`
- **General**: `buffer`, `check`, `email`, `error`, `event`, `garbage`, `collection`, `item`, `location`, `monitor`, `occurrence`, `operation`, `read`, `resource`, `sample`, `stage`, `task`, `time`, `unit`, `worker`, `write`
- **Memory**: `page`, `split`
- **Money**: `cent`, `dollar`
- **Network**: `connection`, `datagram`, `message`, `packet`, `payload`, `request`, `response`, `segment`, `timeout`
- **Percentage**: `apdex`, `fraction`, `percent`, `percent_nano`
- **System**: `core`, `fault`, `host`, `instance`, `node`, `process`, `service`, `thread`
- **Time**: `microsecond`, `millisecond`, `second`, `minute`, `hour`, `day`, `week`

If the unit name is not listed above, leave this value blank. To add a unit to this listing, file an [issue](https://github.com/DataDog/integrations-extras/issues)

**`per_unit_name`**: If you are gathering a per unit metric, you may provide an additional unit name here and it's combined with the `unit_name`. For example, providing a `unit_name` of "request" and a `per_unit_name` of "second" results in a metric of "requests per second". If provided, this must be a value from the available units listed above.

**`description`**: A basic description (limited to 400 characters) of the information this metric represents.

**`orientation`** (required): An integer of `-1`, `0`, or `1`.

- `-1` indicates that smaller values are better. For example, `mysql.performance.slow_queries` or `varnish.fetch_failed` where low counts are desirable.
- `0` indicates no intrinsic preference in values. For example, `rabbitmq.queue.messages` or `postgresql.rows_inserted` where there is no preference for the size of the value or the preference depends on the business objectives of the system.
- `1` indicates that larger values are better. For example, `mesos.stats.uptime_secs` where higher uptime or `mysql.performance.key_cache_utilization` where more cache hits are desired.

**`integration`** (required): This must match the name of your integration, for example: "my_integration".

**`short_name`**: A more human-readable and abbreviated version of the metric name. For example, `postgresql.index_blocks_read` might be set to `idx blks read`. Aim for human-readability and easy understandability over brevity. Don't repeat the integration name. If you can't make the `short_name` shorter and easier to understand than the `metric_name`, leave this field empty.

**`curated_metric`**: To mark which metrics for an integration are noteworthy for a given type (`cpu` and `memory` are both accepted). These are displayed in the UI above the other integration metrics.

#### `requirements.txt`{% #requirementstxt %}

If you require any additional Python libraries, list them in `requirements.txt`. The libraries are automatically installed using pip when others use your integration.

#### `test_my_integration.py`{% #test_my_integrationpy %}

Integration tests ensure that the Datadog Agent is correctly receiving and recording metrics from the software you are integrating.

Tests are not required for each of the metrics collected by your integration, but Datadog strongly encourages you to provide as much coverage as possible. Run the `self.coverage_report()` method in your test to see which metrics are covered.

Here's an example `test_my_integration.py`:

```
# Example test_my_integration.py
from nose.plugins.attrib import attr
from checks import AgentCheck
from tests.checks.common import AgentCheckTest

@attr(requires='my_integration')
Class TestMyIntegration(AgentCheckTest):

  def testMyIntegration(self):
    self.assertServiceCheck('my_integration.can_connect', count=1, status=AgentCheck.OK, tags=[host:localhost', 'port:80'])
    self.coverage_report()
```

For more information about tests and available test methods, reference the [AgentCheckTest class in the Datadog Agent repository](https://github.com/DataDog/dd-agent/blob/master/tests/checks/common.py)

## Libraries{% #libraries %}

The [Datadog Agent](https://github.com/DataDog/dd-agent) provides several useful libraries in the [`utils` directory](https://github.com/DataDog/dd-agent/tree/master/utils). These libraries can be helpful when building your integration, but be aware that these libraries are moved in the Datadog Agent v6.

## Testing your integration{% #testing-your-integration %}

As you build your check and test code, use the following to run your tests:

- `rake lint`: Lint your code for potential errors
- `rake ci:run[my_integration]`: Run the tests that you have written in your `test_my_integration.py` file and that have an `@attr(requires='my_integration')` annotation.
- `rake ci:run[default]`: Run the tests you have written written in your `test_my_integration.py` file (without the `@attr(requires='my_integration')` annotation) in addition to some additional generic tests.

Travis CI automatically runs tests when you create a pull request. Ensure that you have thorough test coverage and that you are passing all tests prior to submitting pull requests.

Add the `@attr(requires='my_integration')` annotation on the test classes or methods that require a full docker testing environment (see next section). Don't add this annotation to your unit and mock tests, run those with `rake ci:run[default]` on Travis CI.

To iterate quickly on your unit and mock tests, instead of running all the tests with `rake ci:run[default]`, run:

```
# run unit and mock tests, in the virtualenv
$ bundle exec rake exec["nosetests my_integration/test/test_*.py -A 'not requires'"]
```

### Docker test environments{% #docker-test-environments %}

Datadog uses Docker containers for testing environments, which is the recommended approach. Containers are lightweight, easy to manage, and provide consistent, standardized environments for each test run.

For example, the [`ci/mysql.rake` file](https://github.com/DataDog/integrations-core/blob/5.19.x/mysql/ci/mysql.rake) for the Datadog MySQL integration uses the [official MySQL container](https://hub.docker.com/_/mysql) and involves four main tasks:

1. `before_install` - Prior to starting the new Docker test environment, ensure that any previous Docker test environments are stopped and removed.
1. `install` - The install task performs the Docker `run` which starts the MySQL test server.
1. `before_script` - This task first ensures that the MySQL server is running, then connects to the server to perform some setup tasks. Keep setup tasks in your `test_integration.py` file when possible, but sometimes setup and configurations need to be performed prior to the python test script.
1. `cleanup` - After the tests are complete, the Docker test environment is stopped and removed.

### Installing your integration locally{% #installing-your-integration-locally %}

When your integration is merged into the `integrations-extras` repository, Datadog generates packages so that others can easily install your integration. However, you may want to install your integration locally before it's merged.

To run locally, first copy your `check.py` file into the Datadog Agent's `checks.d` directory and rename it to `my_integration.py` (using the actual name of your integration).

Next, copy your `conf.yaml.example` file into the Datadog Agent's `conf.d` directory and rename it to `my_integration.yaml` (again, using the actual name of your integration).

See [Create a New Integration](https://docs.datadoghq.com/developers/integrations/agent_integration) for more information about the Datadog Agent directory structure.

### Teardown and cleanup{% #teardown-and-cleanup %}

When you have finished building your integration, run `rake clean_env` to remove the Python virtual environment.

## Submitting your integration{% #submitting-your-integration %}

Once you have completed the development of your integration, submit a [pull request](https://github.com/DataDog/integrations-extras/compare) to have Datadog review your integration. After your integration is reviewed, Datadog approves and merges your pull request or provides feedback and next steps required for approval.

### Other considerations{% #other-considerations %}

Consider the following when writing tests:

- Test clusters. Testing single instances of your software is often easier, but tests are more useful when run against setups that are representative of real-world uses. For example, MongoDB is typically used with sharding and replica set features, so the [tests](https://github.com/DataDog/integrations-core/tree/5.22.x/mongo/test/ci) reflect that.
- Consider generating calculated metrics in addition to raw metrics. For example, many databases have slow, but less frequently run queries. So it's often useful to look at percentiles. For example, the Datadog MySQL integration includes a calculated metric for the [95th percentile query execution time](https://www.ruby-lang.org).
