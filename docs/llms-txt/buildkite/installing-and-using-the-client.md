# Source: https://buildkite.com/docs/test-engine/bktec/installing-and-using-the-client.md

# Installing and using the client

This page provides instructions on how to install the Test Engine Client ([bktec](https://github.com/buildkite/test-engine-client)) using [installers](#installation) provided by Buildkite, as well as [configure and use bktec](#using-bktec).

## Installation

bktec is supported on both Linux ([Debian](#installation-debian) and [Red Hat](#installation-red-hat)) and [macOS](#installation-macos), as well as in [Docker](#installation-docker), for 64-bit ARM and AMD architectures. You can install the client using the following installers.
If you need to install this tool on a system without an installer listed below, you'll need to perform a manual installation using one of the binaries from [Test Engine Client's releases page](https://github.com/buildkite/test-engine-client/releases/latest). Once you have the binary, make it executable in your pipeline.

### Debian

1. Ensure you have curl and gpg installed first:

    ```shell
    apt update && apt install curl gpg -y
    ```

1. Install the registry signing key:

    ```shell
    curl -fsSL "https://packages.buildkite.com/buildkite/test-engine-client-deb/gpgkey" | gpg --dearmor -o /etc/apt/keyrings/buildkite_test-engine-client-deb-archive-keyring.gpg
    ```

1. Configure the registry:

    ```shell
    echo -e "deb [signed-by=/etc/apt/keyrings/buildkite_test-engine-client-deb-archive-keyring.gpg] https://packages.buildkite.com/buildkite/test-engine-client-deb/any/ any main\ndeb-src [signed-by=/etc/apt/keyrings/buildkite_test-engine-client-deb-archive-keyring.gpg] https://packages.buildkite.com/buildkite/test-engine-client-deb/any/ any main" > /etc/apt/sources.list.d/buildkite-buildkite-test-engine-client-deb.list
    ```

1. Install the package:

    ```shell
    apt update && apt install bktec
    ```

### Red Hat

1. Configure the registry:

    ```shell
    echo -e "[test-engine-client-rpm]\nname=Test Engine Client - rpm\nbaseurl=https://packages.buildkite.com/buildkite/test-engine-client-rpm/rpm_any/rpm_any/\$basearch\nenabled=1\nrepo_gpgcheck=1\ngpgcheck=0\ngpgkey=https://packages.buildkite.com/buildkite/test-engine-client-rpm/gpgkey\npriority=1" > /etc/yum.repos.d/test-engine-client-rpm.repo
    ```

2. Install the package:

    ```shell
    dnf install -y bktec
    ```

### macOS

The Test Engine Client can be installed using [Homebrew](https://brew.sh) with [Buildkite tap formulae](https://github.com/buildkite/homebrew-buildkite). To install, run:

```shell
brew tap buildkite/buildkite && brew install buildkite/buildkite/bktec
```

### Docker

You can run the Test Engine Client inside a Docker container using the official image in [Docker Hub](https://hub.docker.com/r/buildkite/test-engine-client/tags).

To run the client using Docker:

```shell
docker run buildkite/test-engine-client
```

Or, to add the Test Engine Client binary to your Docker image, include the following in your Dockerfile:

```dockerfile
COPY --from=buildkite/test-engine-client /usr/local/bin/bktec /usr/local/bin/bktec
```

## Dependencies

bktec relies on execution timing data captured by the test collectors from previous builds to partition your tests evenly across your agents. Therefore, you will need to configure the [test collector](/docs/test-engine/test-collection) for your test framework.

## Using bktec

Buildkite maintains its open source Test Engine Client ([bktec](https://github.com/buildkite/test-engine-client)) tool. Currently, the bktec tool supports [RSpec](/docs/test-engine/test-collection/ruby-collectors#rspec-collector), [Jest](/docs/test-engine/test-collection/javascript-collectors#configure-the-test-framework-jest), [Cypress](/docs/test-engine/test-collection/javascript-collectors#configure-the-test-framework-cypress), [PlayWright](/docs/test-engine/test-collection/javascript-collectors#configure-the-test-framework-playwright), and [Pytest](/docs/test-engine/test-collection/python-collectors#pytest-collector), pytest-pants, [Go](/docs/test-engine/test-collection/golang-collectors), and cucumber testing frameworks.

If your testing framework is not supported, get in touch through support@buildkite.com or submit a pull request.

Once you have [installed the bktec binary](#installation) and it is executable in your pipeline, you'll need to [configure some additional environment variables](#using-bktec-configure-environment-variables) for bktec to function. You can then [update your pipeline step](#using-bktec-update-the-pipeline-step) to call `bktec run` instead of calling RSpec to run your tests.

### Configure environment variables

bktec uses a number of [predefined](#predefined-environment-variables) and [mandatory](#mandatory-environment-variables) environment variables, as well as several optional ones for either [RSpec](#optional-rspec-environment-variables) or [Jest](#optional-jest-environment-variables).

<h4 id="predefined-environment-variables">Predefined environment variables</h4>

By default, the following predefined environment variables are available to your testing environment and do not need any further configuration. If, however, you use Docker or some other type of containerization tool to run your tests, and you wish to use these predefined environment variables in these tests, you may need to expose these environment variables to your containers.

<table class="Docs__attribute__table">
  <tbody>

      <tr id="BUILDKITE_BUILD_ID">
        <th>
          <code>BUILDKITE_BUILD_ID <a class="Docs__attribute__link" href="#BUILDKITE_BUILD_ID">#</a></code>
        </th>
        <td>
          
              <p>The UUID of the pipeline build. The Test Engine Client uses this UUID along with <code>BUILDKITE_STEP_ID</code> to uniquely identify the test plan.</p>

        </td>
      </tr>
    
      <tr id="BUILDKITE_JOB_ID">
        <th>
          <code>BUILDKITE_JOB_ID <a class="Docs__attribute__link" href="#BUILDKITE_JOB_ID">#</a></code>
        </th>
        <td>
          
              <p>The UUID of the job in the pipeline's build.</p>

        </td>
      </tr>
    
      <tr id="BUILDKITE_ORGANIZATION_SLUG">
        <th>
          <code>BUILDKITE_ORGANIZATION_SLUG <a class="Docs__attribute__link" href="#BUILDKITE_ORGANIZATION_SLUG">#</a></code>
        </th>
        <td>
          
              <p>The slug of your Buildkite organization.</p>

        </td>
      </tr>
    
      <tr id="BUILDKITE_PARALLEL_JOB">
        <th>
          <code>BUILDKITE_PARALLEL_JOB <a class="Docs__attribute__link" href="#BUILDKITE_PARALLEL_JOB">#</a></code>
        </th>
        <td>
          
              <p>The index number of a parallel job created from a parallel build step.</p>

              <p>Ensure you configure <code>parallelism</code> in your pipeline definition. Learn more about parallel build steps in <a href="https://buildkite.com/docs/pipelines/controlling-concurrency#concurrency-and-parallelism">Concurrency and parallelism</a>.</p>

        </td>
      </tr>
    
      <tr id="BUILDKITE_PARALLEL_JOB_COUNT">
        <th>
          <code>BUILDKITE_PARALLEL_JOB_COUNT <a class="Docs__attribute__link" href="#BUILDKITE_PARALLEL_JOB_COUNT">#</a></code>
        </th>
        <td>
          
              <p>The total number of parallel jobs created from a parallel build step.</p>

              <p>Ensure you configure <code>parallelism</code> in your pipeline definition. Learn more about parallel build steps in <a href="https://buildkite.com/docs/pipelines/controlling-concurrency#concurrency-and-parallelism">Concurrency and parallelism</a>.</p>

        </td>
      </tr>
    
      <tr id="BUILDKITE_STEP_ID">
        <th>
          <code>BUILDKITE_STEP_ID <a class="Docs__attribute__link" href="#BUILDKITE_STEP_ID">#</a></code>
        </th>
        <td>
          
              <p>The UUID of the step group in the pipeline build. The Test Engine Client uses this UUID along with <code>BUILDKITE_BUILD_ID</code> to uniquely identify the test plan.</p>

        </td>
      </tr>
    
  </tbody>
</table>

<h4 id="mandatory-environment-variables">Mandatory environment variables</h4>

The following mandatory environment variables must be set.

<table class="Docs__attribute__table">
  <tbody>

      <tr id="BUILDKITE_TEST_ENGINE_API_ACCESS_TOKEN">
        <th>
          <code>BUILDKITE_TEST_ENGINE_API_ACCESS_TOKEN <a class="Docs__attribute__link" href="#BUILDKITE_TEST_ENGINE_API_ACCESS_TOKEN">#</a></code>
        </th>
        <td>
          
            <p>Buildkite API access token with <code>read_suites</code>, <code>read_test_plan</code>, and <code>write_test_plan</code> scopes. You can create an <a href="https://buildkite.com/user/api-access-tokens">API access token</a> from <strong>Personal Settings</strong> &gt; <strong>API Access Tokens</strong> in the Buildkite interface. To avoid this token being tied to any one employee or person, ideally, the token should be created for a bot user account within your Buildkite organization.</p>

        </td>
      </tr>
    
      <tr id="BUILDKITE_TEST_ENGINE_RESULT_PATH">
        <th>
          <code>BUILDKITE_TEST_ENGINE_RESULT_PATH <a class="Docs__attribute__link" href="#BUILDKITE_TEST_ENGINE_RESULT_PATH">#</a></code>
        </th>
        <td>
          
            <p>The path to store the test result. The Test Engine Client uses this environment variable to tell the runner where to store the test result. The Test Engine Client reads the test result after each test run for retries and verification.</p>

            <p>For RSpec, the result is generated using the <code>--format json</code> and <code>--out</code> CLI options, while for Jest, it is generated using the <code>--json</code> and <code>--outputFile</code> options. We have included these options in the default test command for RSpec and Jest. If you need to customize your test command, make sure to append the CLI options to save the result to a file.</p>

            <p>Please refer to the <code>BUILDKITE_TEST_ENGINE_TEST_CMD</code> environment variable for more details.</p>

            <section class="callout callout--info">
              
                <p>The Test Engine Client will not delete the file after running the test, however it will be deleted by the Buildkite agent as part of the build lifecycle.</p>

            </section>
          
        </td>
      </tr>
    
      <tr id="BUILDKITE_TEST_ENGINE_TEST_RUNNER">
        <th>
          <code>BUILDKITE_TEST_ENGINE_TEST_RUNNER <a class="Docs__attribute__link" href="#BUILDKITE_TEST_ENGINE_TEST_RUNNER">#</a></code>
        </th>
        <td>
          
            <p>The test runner to use for running tests. Currently <code>rspec</code>, <code>jest</code>, <code>cypress</code>, <code>playwright</code>, <code>pytest</code>, <code>pytest-pants</code>, <code>gotest</code>, and <code>cucumber</code> are supported.</p>

        </td>
      </tr>
    
      <tr id="BUILDKITE_TEST_ENGINE_SUITE_SLUG">
        <th>
          <code>BUILDKITE_TEST_ENGINE_SUITE_SLUG <a class="Docs__attribute__link" href="#BUILDKITE_TEST_ENGINE_SUITE_SLUG">#</a></code>
        </th>
        <td>
          
            <p>The slug of your Test Engine test suite. You can find the suite slug in the url for your test suite.</p>

            <p>For example, the slug for the url: <code>https://buildkite.com/organizations/my-organization/analytics/suites/my-suite</code> is <code>my-suite</code>.</p>

        </td>
      </tr>
    
  </tbody>
</table>

<h4 id="optional-rspec-environment-variables">Optional RSpec environment variables</h4>

The following optional RSpec environment variables can also be used to configure bktec's behavior.

<table class="Docs__attribute__table">
  <tbody>

      <tr id="BUILDKITE_TEST_ENGINE_DEBUG_ENABLED">
        <th>
          <code>BUILDKITE_TEST_ENGINE_DEBUG_ENABLED <a class="Docs__attribute__link" href="#BUILDKITE_TEST_ENGINE_DEBUG_ENABLED">#</a></code>
          <p class="Docs__attribute__env-var">
            <strong>Default</strong>:<br>
            <code>-</code>
          </p>
        </th>
        <td>
          
            <p>A flag to enable more verbose logging.</p>

        </td>
      </tr>
    
      <tr id="BUILDKITE_TEST_ENGINE_RETRY_CMD">
        <th>
          <code>BUILDKITE_TEST_ENGINE_RETRY_CMD <a class="Docs__attribute__link" href="#BUILDKITE_TEST_ENGINE_RETRY_CMD">#</a></code>
          <p class="Docs__attribute__env-var">
            <strong>Default</strong>:<br>
            <code>-</code>
          </p>
        </th>
        <td>
          
            <p>The command to retry the failed tests. The Test Engine Client will replace the <code>{{testExamples}}</code> placeholder with the failed tests. If not set, the client will use the same command defined in <code>BUILDKITE_TEST_ENGINE_TEST_CMD</code>.</p>

        </td>
      </tr>
    
      <tr id="BUILDKITE_TEST_ENGINE_RETRY_COUNT">
        <th>
          <code>BUILDKITE_TEST_ENGINE_RETRY_COUNT <a class="Docs__attribute__link" href="#BUILDKITE_TEST_ENGINE_RETRY_COUNT">#</a></code>
          <p class="Docs__attribute__env-var">
            <strong>Default</strong>:<br>
            <code>0</code>
          </p>
        </th>
        <td>
          
            <p>The number of retries. The Test Engine Client runs the test command defined in <code>BUILDKITE_TEST_ENGINE_TEST_CMD</code> and retries only the failed tests up to <code>BUILDKITE_TEST_ENGINE_RETRY_COUNT</code> times, using the retry command defined in <code>BUILDKITE_TEST_ENGINE_RETRY_CMD</code>.</p>

        </td>
      </tr>
    
      <tr id="BUILDKITE_TEST_ENGINE_SPLIT_BY_EXAMPLE">
        <th>
          <code>BUILDKITE_TEST_ENGINE_SPLIT_BY_EXAMPLE <a class="Docs__attribute__link" href="#BUILDKITE_TEST_ENGINE_SPLIT_BY_EXAMPLE">#</a></code>
          <p class="Docs__attribute__env-var">
            <strong>Default</strong>:<br>
            <code>-</code>
          </p>
        </th>
        <td>
          
            <p>A flag to enable split by example. When this option is <code>true</code>, the Test Engine Client will split the execution of slow test files over multiple partitions.</p>

        </td>
      </tr>
    
      <tr id="BUILDKITE_TEST_ENGINE_TEST_CMD">
        <th>
          <code>BUILDKITE_TEST_ENGINE_TEST_CMD <a class="Docs__attribute__link" href="#BUILDKITE_TEST_ENGINE_TEST_CMD">#</a></code>
          <p class="Docs__attribute__env-var">
            <strong>Default</strong>:<br>
            <code>bundle exec rspec --format progress --format json --out {{resultPath}} {{testExamples}}</code>
          </p>
        </th>
        <td>
          
            <p>The test command to run your tests. The Test Engine Client will replace the <code>{{testExamples}}</code> placeholder with the test plan.</p>

            <section class="callout callout--info">
              
                <p>It is necessary to include <code>--format json --out {{resultPath}}</code> in the test command, because the Test Engine Client needs to read the result after each test run.</p>

                <p>Please refer to the <code>BUILDKITE_TEST_ENGINE_RESULT_PATH</code> environment variable for more details.</p>

            </section>
          
        </td>
      </tr>
    
      <tr id="BUILDKITE_TEST_ENGINE_TEST_FILE_EXCLUDE_PATTERN">
        <th>
          <code>BUILDKITE_TEST_ENGINE_TEST_FILE_EXCLUDE_PATTERN <a class="Docs__attribute__link" href="#BUILDKITE_TEST_ENGINE_TEST_FILE_EXCLUDE_PATTERN">#</a></code>
          <p class="Docs__attribute__env-var">
            <strong>Default</strong>:<br>
            <code>-</code>
          </p>
        </th>
        <td>
          
            <p>The glob pattern to exclude certain test files or directories. The exclusion will be applied after discovering the test files using a pattern configured with <code>BUILDKITE_TEST_ENGINE_TEST_FILE_PATTERN</code>.</p>

            <p><em>This option accepts <a href="/docs/pipelines/configure/glob-pattern-syntax">glob pattern syntax</a>.</em></p>

        </td>
      </tr>
    
      <tr id="BUILDKITE_TEST_ENGINE_TEST_FILE_PATTERN">
        <th>
          <code>BUILDKITE_TEST_ENGINE_TEST_FILE_PATTERN <a class="Docs__attribute__link" href="#BUILDKITE_TEST_ENGINE_TEST_FILE_PATTERN">#</a></code>
          <p class="Docs__attribute__env-var">
            <strong>Default</strong>:<br>
            <code>spec/**/*_spec.rb</code>
          </p>
        </th>
        <td>
          
            <p>The glob pattern to discover test files. You can exclude certain test files or directories from the discovered test files using a pattern that can be configured with <code>BUILDKITE_TEST_ENGINE_TEST_FILE_EXCLUDE_PATTERN</code>.</p>

            <p><em>This option accepts <a href="/docs/pipelines/configure/glob-pattern-syntax">glob pattern syntax</a>.</em></p>

        </td>
      </tr>
    
  </tbody>
</table>

<h4 id="optional-jest-environment-variables">Optional Jest environment variables</h4>

The following optional Jest environment variables can also be used to configure bktec's behavior.

<table class="Docs__attribute__table">
  <tbody>

      <tr id="BUILDKITE_TEST_ENGINE_DEBUG_ENABLED">
        <th>
          <code>BUILDKITE_TEST_ENGINE_DEBUG_ENABLED <a class="Docs__attribute__link" href="#BUILDKITE_TEST_ENGINE_DEBUG_ENABLED">#</a></code>
          <p class="Docs__attribute__env-var">
            <strong>Default</strong>:<br>
            <code>-</code>
          </p>
        </th>
        <td>
          
            <p>A flag to enable more verbose logging.</p>

        </td>
      </tr>
    
      <tr id="BUILDKITE_TEST_ENGINE_RETRY_CMD">
        <th>
          <code>BUILDKITE_TEST_ENGINE_RETRY_CMD <a class="Docs__attribute__link" href="#BUILDKITE_TEST_ENGINE_RETRY_CMD">#</a></code>
          <p class="Docs__attribute__env-var">
            <strong>Default</strong>:<br>
            <code>yarn test --testNamePattern '{{testNamePattern}}' --json --testLocationInResults --outputFile {{resultPath}}</code>
          </p>
        </th>
        <td>
          
            <p>The command to retry the failed tests. The Test Engine Client will replace the <code>{{testNamePattern}}</code> placeholder with the failed tests.</p>

            <section class="callout callout--info">
              
                <p>It is necessary to include <code>--json --testLocationInResults --outputFile {{resultPath}}</code> in the command, because the Test Engine Client needs to read the result after each test run.</p>

                <p>Please refer to the <code>BUILDKITE_TEST_ENGINE_RESULT_PATH</code> environment variable for more details.</p>

            </section>
          
        </td>
      </tr>
    
      <tr id="BUILDKITE_TEST_ENGINE_RETRY_COUNT">
        <th>
          <code>BUILDKITE_TEST_ENGINE_RETRY_COUNT <a class="Docs__attribute__link" href="#BUILDKITE_TEST_ENGINE_RETRY_COUNT">#</a></code>
          <p class="Docs__attribute__env-var">
            <strong>Default</strong>:<br>
            <code>0</code>
          </p>
        </th>
        <td>
          
            <p>The number of retries. The Test Engine Client runs the test command defined in <code>BUILDKITE_TEST_ENGINE_TEST_CMD</code> and retries only the failed tests up to <code>BUILDKITE_TEST_ENGINE_RETRY_COUNT</code> times, using the retry command defined in <code>BUILDKITE_TEST_ENGINE_RETRY_CMD</code>.</p>

        </td>
      </tr>
    
      <tr id="BUILDKITE_TEST_ENGINE_TEST_CMD">
        <th>
          <code>BUILDKITE_TEST_ENGINE_TEST_CMD <a class="Docs__attribute__link" href="#BUILDKITE_TEST_ENGINE_TEST_CMD">#</a></code>
          <p class="Docs__attribute__env-var">
            <strong>Default</strong>:<br>
            <code>yarn test {{testExamples}} --json --testLocationInResults --outputFile {{resultPath}}</code>
          </p>
        </th>
        <td>
          
            <p>The test command to run your tests. The Test Engine Client will replace and populate the <code>{{testExamples}}</code> placeholder with the test plan.</p>

            <section class="callout callout--info">
              
                <p>It is necessary to include <code>--json --testLocationInResults --outputFile {{resultPath}}</code> in the command, because the Test Engine Client needs to read the result after each test run.</p>

                <p>Please refer to the <code>BUILDKITE_TEST_ENGINE_RESULT_PATH</code> environment variable for more details.</p>

            </section>
          
        </td>
      </tr>
    
      <tr id="BUILDKITE_TEST_ENGINE_TEST_FILE_EXCLUDE_PATTERN">
        <th>
          <code>BUILDKITE_TEST_ENGINE_TEST_FILE_EXCLUDE_PATTERN <a class="Docs__attribute__link" href="#BUILDKITE_TEST_ENGINE_TEST_FILE_EXCLUDE_PATTERN">#</a></code>
          <p class="Docs__attribute__env-var">
            <strong>Default</strong>:<br>
            <code>node_modules</code>
          </p>
        </th>
        <td>
          
            <p>The glob pattern to exclude certain test files or directories. The exclusion will be applied after discovering the test files using a pattern configured with <code>BUILDKITE_TEST_ENGINE_TEST_FILE_PATTERN</code>.</p>

            <p><em>This option accepts <a href="/docs/pipelines/configure/glob-pattern-syntax">glob pattern syntax</a>.</em></p>

        </td>
      </tr>
    
      <tr id="BUILDKITE_TEST_ENGINE_TEST_FILE_PATTERN">
        <th>
          <code>BUILDKITE_TEST_ENGINE_TEST_FILE_PATTERN <a class="Docs__attribute__link" href="#BUILDKITE_TEST_ENGINE_TEST_FILE_PATTERN">#</a></code>
          <p class="Docs__attribute__env-var">
            <strong>Default</strong>:<br>
            <code>**/{__tests__/**/*,*.spec,*.test}.{ts,js,tsx,jsx}</code>
          </p>
        </th>
        <td>
          
            <p>The glob pattern to discover test files. You can exclude certain test files or directories from the discovered test files using a pattern that can be configured with <code>BUILDKITE_TEST_ENGINE_TEST_FILE_EXCLUDE_PATTERN</code>.</p>

            <p><em>This option accepts <a href="/docs/pipelines/configure/glob-pattern-syntax">glob pattern syntax</a>.</em></p>

        </td>
      </tr>
    
  </tbody>
</table>

### Update the pipeline step

With the environment variables configured, you can now update your pipeline step to run bktec instead of running RSpec, or Jest directly. The following example pipeline step demonstrates how to partition your RSpec test suite across 10 nodes.

```
steps:
  - name: "RSpec"
    command: bktec run
    parallelism: 10
    env:
      BUILDKITE_TEST_ENGINE_API_ACCESS_TOKEN: your-secret-token
      BUILDKITE_TEST_ENGINE_RESULT_PATH: tmp/rspec-result.json
      BUILDKITE_TEST_ENGINE_SUITE_SLUG: my-suite
      BUILDKITE_TEST_ENGINE_TEST_RUNNER: rspec
```

{: codeblock-file="pipeline.yml"}

## API rate limits

There is a limit on the number of API requests that bktec can make to the server. This limit is 10,000 requests per minute per Buildkite organization. When this limit is reached, bktec will pause and wait until the next minute is reached before retrying the request. This rate limit is independent of the [REST API rate limits](/docs/apis/rest-api/limits), and only applies to the Test Engine Client's interactions with the Test Splitting API.

## Dynamic parallelism

Usually the `parallelism` value is hard coded in the bktec pipeline step. However, from version 2.0.0, it is possible to run bktec with a dynamic `parallelism` value based on a target time for the test run. A common use case for this is test selection, where feature branch builds only run a subset of tests relevant to the changes being made.

Dynamic parallelism is supported using the `bktec plan` command. When used with the `--max-parallelism` and `--target-time` flags (see list of [bktec plan flags](#dynamic-parallelism-bktec-plan-flags) for more information), bktec generates a test plan and estimates the `parallelism` required to achieve the specified target build time. bktec then [uploads a dynamic pipeline](/docs/agent/cli/reference/pipeline) using the specified pipeline template.

In the following example, the `test-selection.sh` script is assumed to generate a list of test files, one per line, relevant to the changes in a feature branch.

```
steps:
  - name: "Test selection"
    command: test-selection.sh > selected-files.txt

  - wait: ~

  - name: "Dynamic pipeline"
    key: "dynamic-pipeline"
    command: bktec plan --max-parallelism 10 --target-time 2m --files selected-files.txt --pipeline-upload .buildkite/dynamic-pipeline-template.yml
```

{: codeblock-file="pipeline.yml"}

In this example pipeline, bktec uploads a dynamic pipeline using `.buildkite/dynamic-pipeline-template.yml` by invoking `buildkite agent pipeline upload`. Learn more about the [bktec plan additional environment variables](#dynamic-parallelism-bktec-plan-additional-environment-variables) generated during pipeline uploads.

These variables can be used in the template file provided to the `--pipeline-upload` flag, where you can use [environment variable substitution](/docs/agent/cli/reference/pipeline#environment-variable-substitution) to obtain their values.

```
steps:
- command: "bktec run --plan-identifier ${BUILDKITE_TEST_ENGINE_PLAN_IDENTIFIER}"
  name: "bktec run"
  depends_on: "dynamic-pipeline"
  parallelism: ${BUILDKITE_TEST_ENGINE_PARALLELISM}
```

{: codeblock-file=".buildkite/dynamic-pipeline-template.yml"}

### bktec plan flags

The `bktec plan` command supports the following flags, which controls the behavior of the dynamic parallelism test plan. Each flag's value alternatively can be supplied using an environment variable.

<table class="responsive-table">
  <tbody>
    <tr>
      <td><code>--max-parallelism</code></td>
      <td>
        The maximum allowed parallelism for a dynamic parallelism test plan.
        <br>
        <strong>Environment variable:</strong>
        <code>$BUILDKITE_TEST_ENGINE_MAX_PARALLELISM</code>
      </td>
    </tr>
    <tr>
      <td><code>--target-time</code></td>
      <td>
        Target duration for each node, for example, <code>2m30s</code>.
        The test planner will attempt to split the test plan into equal duration buckets of this duration and calculate the optimum parallelism to achieve this, up to the value supplied to <code>--max-parallelism</code>
        <br>
        <strong>Environment variable:</strong>
        <code>$BUILDKITE_TEST_ENGINE_TARGET_TIME</code>
      </td>
    </tr>
    <tr>
      <td><code>--files</code></td>
      <td>
        Path to a file containing a newline separated list of test file names to be executed.
        <br>
        <strong>Environment variable:</strong>
        <code>$BUILDKITE_TEST_ENGINE_FILES</code>
      </td>
    </tr>
  </tbody>
</table>

### bktec plan additional environment variables

The `bktec plan` command generates the following additional environment variables when uploading the pipeline.

<table class="responsive-table">
  <tbody>
    <tr>
      <td><code>BUILDKITE_TEST_ENGINE_PLAN_IDENTIFIER</code></td>
      <td>The identifier of the test plan generated by <code>bktec plan</code>.</td>
    </tr>
    <tr>
      <td><code>BUILDKITE_TEST_ENGINE_PARALLELISM</code></td>
      <td>The parallelism estimated by the test planner to achieve the requested target build time.</td>
    </tr>
  </tbody>
</table>
