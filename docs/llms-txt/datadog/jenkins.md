# Source: https://docs.datadoghq.com/continuous_testing/cicd_integrations/jenkins.md

# Source: https://docs.datadoghq.com/continuous_integration/pipelines/jenkins.md

---
title: Jenkins Setup for CI Visibility
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Continuous Integration Visibility > CI Pipeline Visibility in Datadog >
  Jenkins Setup for CI Visibility
source_url: https://docs.datadoghq.com/pipelines/jenkins/index.html
---

# Jenkins Setup for CI Visibility

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

[Jenkins](https://www.jenkins.io/) is an automation server with continuous integration and delivery features. With its plugin architecture, Jenkins can be customized to fit any CI/CD need and automates all aspects of project development, testing, and deployment.

Set up CI Visibility for Jenkins to collect data across various stages of your pipeline executions, identify performance bottlenecks, resolve operational challenges, and refine your deployment processes.

### Compatibility{% #compatibility %}

| Pipeline Visibility                                                                                                                              | Platform                            | Definition                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Manual steps](https://docs.datadoghq.com/glossary/#manual-step)                                                                                 | Manual steps                        | View manually triggered pipelines.                                                                                                                                                                     |
| [Queue time](https://docs.datadoghq.com/glossary/#queue-time)                                                                                    | Queue time                          | View the amount of time pipeline jobs sit in the queue before processing.                                                                                                                              |
| Logs correlation                                                                                                                                 | Logs correlation                    | Correlate pipeline spans to logs and enable [job logs collection](https://docs.datadoghq.com/continuous_integration/pipelines/jenkins/?tab=linux#enable-job-log-collection).                           |
| Infrastructure metric correlation                                                                                                                | Infrastructure metric correlation   | Correlate jobs to [infrastructure host metrics](https://docs.datadoghq.com/continuous_integration/pipelines/jenkins/?tab=agentlessusinganapikey#correlate-infrastructure-metrics) for Jenkins workers. |
| [Custom spans](https://docs.datadoghq.com/glossary/#custom-span)                                                                                 | Custom spans                        | Configure custom spans for your pipelines.                                                                                                                                                             |
| Custom pre-defined tags                                                                                                                          | Custom pre-defined tags             | Set [custom tags](https://docs.datadoghq.com/continuous_integration/pipelines/custom_tags_and_measures/) to all generated pipeline, stages, and job spans.                                             |
| [Custom tags](https://docs.datadoghq.com/glossary/#custom-tag) [and measures at runtime](https://docs.datadoghq.com/glossary/#custom-measure)    | Custom tags and measures at runtime | Configure [custom tags and measures](https://docs.datadoghq.com/continuous_integration/pipelines/custom_tags_and_measures/) at runtime.                                                                |
| [Parameters](https://docs.datadoghq.com/glossary/#parameter)                                                                                     | Parameters                          | Set custom parameters (such as the default branch name or Git information) when a pipeline is triggered.                                                                                               |
| [Pipeline failure reasons](https://docs.datadoghq.com/glossary/#pipeline-failure)                                                                | Pipeline failure reasons            | Identify pipeline failure reasons from error messages.                                                                                                                                                 |
| [Running pipelines](https://docs.datadoghq.com/glossary/#running-pipeline)                                                                       | Running pipelines                   | View pipeline executions that are running. Requires Jenkins plugin version >= 8.0.0                                                                                                                    |
| [Filter CI Jobs on the critical path](https://docs.datadoghq.com/continuous_integration/guides/identify_highest_impact_jobs_with_critical_path/) | Filter CI Jobs on the critical path | Filter by jobs on the critical path.                                                                                                                                                                   |
| [Execution time](https://docs.datadoghq.com/glossary/#pipeline-execution-time)                                                                   | Execution time                      | View the amount of time pipelines have been running jobs.                                                                                                                                              |

The following Jenkins versions are supported:

- Jenkins >= 2.346.1

This integration supports both Agentless and Agent-based installation. Installing the Agent is required for infrastructure metrics correlation.

### Terminology{% #terminology %}

This table shows the mapping of concepts between Datadog CI Visibility and Jenkins:

| Datadog  | Jenkins  |
| -------- | -------- |
| Pipeline | Pipeline |
| Stage    | Stage    |
| Job      | Step     |

## Install the Datadog Agent{% #install-the-datadog-agent %}

Skip this step if you do not need infrastructure metrics correlation.

Install Datadog Agent on your Jenkins controller node and on your worker nodes by following the [Agent installation instructions](https://docs.datadoghq.com/agent/).

If the Jenkins controller and the Datadog Agent have been deployed to a Kubernetes cluster, Datadog recommends using the [Admission Controller](https://docs.datadoghq.com/agent/cluster_agent/admission_controller/), which automatically sets the `DD_AGENT_HOST` environment variable in the Jenkins controller pod to communicate with the local Datadog Agent.

If you want to report the logs of your Jenkins jobs to Datadog, make sure that custom logs collection over TCP is [enabled and configured](https://docs.datadoghq.com/agent/logs/?tab=tcpudp#custom-log-collection) in the Agent.

If your Agent runs in a container, add the `DD_DOGSTATSD_NON_LOCAL_TRAFFIC=true` environment variable to it and make sure the following ports are accessible by the Jenkins controller:

- [DogStadsD](https://docs.datadoghq.com/developers/dogstatsd/) port, defaults to `8125/udp`
- [APM traces port](https://docs.datadoghq.com/containers/docker/apm/#tracing-from-the-host), defaults to `8126/tcp`
- [logs collection port](https://docs.datadoghq.com/agent/logs/?tab=tcpudp#custom-log-collection), defaults to `10518/tcp`

{% alert level="info" %}
Sending CI Visibility traces through UNIX domain sockets is not supported.
{% /alert %}

## Install the Datadog Jenkins plugin{% #install-the-datadog-jenkins-plugin %}

{% alert level="info" %}
Whether you choose to use Agentless mode or the Agent-based mode to report your data to Datadog, you are **required** to use the plugin.
{% /alert %}

Install and enable the [Datadog Jenkins plugin](https://plugins.jenkins.io/datadog/) v3.1.0 or later:

1. In your Jenkins instance web interface, go to **Manage Jenkins > Manage Plugins**.
1. In the [Update Center](https://wiki.jenkins-ci.org/display/JENKINS/Plugins#Plugins-Howtoinstallplugins) on the **Available** tab, search for `Datadog Plugin`.
1. Select the checkbox next to the plugin, and install using one of the two install buttons at the bottom of the screen.
1. To verify that the plugin is installed, search for `Datadog Plugin` on the **Installed** tab.

## Configure the Datadog Jenkins plugin{% #configure-the-datadog-jenkins-plugin %}

There are several ways you can configure the Datadog Jenkins plugin.

### Configure with the Jenkins configuration UI{% #configure-with-the-jenkins-configuration-ui %}

#### Report through the Datadog Agent (recommended){% #report-through-the-datadog-agent-recommended %}

1. In your Jenkins instance web interface, go to **Manage Jenkins > Configure System**.
1. Go to the `Datadog Plugin` section, scrolling down the configuration screen.
1. Select the mode `Use the Datadog Agent to report to Datadog`.
1. Configure the `Agent` host.
1. Configure CI Visibility:
   1. Configure the `Traces Collection Port` if not using the default port `8126`.
   1. Click the `Test traces connection` button to verify that your configuration is valid.
   1. Enable the `Enable CI Visibility` checkbox.
   1. (Optional) Configure your CI Instance name.
1. (Optional) Configure logs collection:
   1. Configure the `Log Collection` port as configured in the Datadog Agent.
   1. Click the `Test logs connection` button to verify that your configuration is valid.
   1. Enable the `Enable Log Collection` checkbox.
1. (Optional) Enter the name of the host that you use to access Datadog UI (for example, `app.datadoghq.com`) in the `Datadog App hostname` field.
1. Save your configuration.

{% image
   source="https://datadog-docs.imgix.net/images/ci/ci-jenkins-plugin-config-agentful-app-hostname.9db126889fd16f86830130d52f77fbf5.png?auto=format"
   alt="Datadog Plugin configuration for Jenkins" /%}

#### Agentless (using an API key){% #agentless-using-an-api-key %}

Use this option to make the Jenkins plugin report directly to Datadog without using the Datadog Agent. It requires an API Key.

1. In your Jenkins instance web interface, go to **Manage Jenkins > Configure System**.
1. Go to the `Datadog Plugin` section, scrolling down the configuration screen.
1. Select the mode `Use Datadog site and API key to report to Datadog`.
1. Select your [Datadog site](https://docs.datadoghq.com/getting_started/site/#access-the-datadog-site) in the `Pick a site` dropdown.
1. Enter a valid `Datadog API Key` (or use `Select from credentials` option).
1. Click the `Test Key` button to verify that your API key is valid.
1. Configure CI Visibility:
   1. Enable the `Enable CI Visibility` checkbox.
   1. (Optional) Configure your CI Instance name.
1. (Optional) Configure logs collection:
   1. Enable the `Enable Log Collection` checkbox.
1. (Optional) Enter the name of the host that you use to access Datadog UI (for example, `app.datadoghq.com`) in the `Datadog App hostname` field.
1. Save your configuration.

{% image
   source="https://datadog-docs.imgix.net/images/ci/ci-jenkins-plugin-config-agentless-app-hostname.91c692b697d9bdffeb04493e2d1a2e17.png?auto=format"
   alt="Datadog Plugin configuration for Jenkins" /%}

### Use Configuration-as-Code{% #use-configuration-as-code %}

#### Report through the Datadog Agent (recommended){% #report-through-the-datadog-agent-recommended-1 %}

If your Jenkins instance uses the Jenkins [`configuration-as-code`](https://docs.datadoghq.com/getting_started/site/#access-the-datadog-site) plugin:

1. Create or modify the configuration YAML by adding an entry for `datadogGlobalConfiguration`:

```yaml
unclassified:
  datadogGlobalConfiguration:
    datadogClientConfiguration:
      # Select the `Datadog Agent` mode
      datadogAgentConfiguration:
        # Configure Datadog Agent host
        agentHost: '<your-agent-host>'
        # Configure Datadog Agent port
        agentPort: 8125
        # (Optional) Configure logs collection port as configured in your Datadog Agent
        agentLogCollectionPort: 10518
        # Configure traces collection port
        agentTraceCollectionPort: 8126
    # Enable CI Visibility flag
    enableCiVisibility: true
    # (Optional) Configure your CI Instance name
    ciInstanceName: 'jenkins'
    # (Optional) Configure the name of the host that you use to access Datadog UI
    datadogAppHostname: 'app.datadoghq.com'
    # (Optional) Enable logs collection
    collectBuildLogs: true
```
In your Jenkins instance web interface, go to **Manage Jenkins > Configuration as Code**.Apply or reload the configuration.Check the configuration using the `View Configuration` button.
#### Agentless (using an API key){% #agentless-using-an-api-key-1 %}

If your Jenkins instance uses the Jenkins [`configuration-as-code`](https://docs.datadoghq.com/getting_started/site/#access-the-datadog-site) plugin:

1. Create or modify the configuration YAML by adding an entry for `datadogGlobalConfiguration`:

```yaml
unclassified:
  datadogGlobalConfiguration:
    datadogClientConfiguration:
      # Select the `Agentless` mode (using API key).
      datadogApiConfiguration:
        intake:
          datadogIntakeSite:
            # Configure your Datadog site
            site: ''
        apiKey:
          datadogCredentialsApiKey:
            # Configure ID of Jenkins credentials that store your API key
            credentialsId: 'my-api-key-credentials-id'
    # Enable CI Visibility flag
    enableCiVisibility: true
    # (Optional) Configure your CI Instance name
    ciInstanceName: 'jenkins'
    # (Optional) Configure the name of the host that you use to access Datadog UI
    datadogAppHostname: ''
    # (Optional) Enable logs collection
    collectBuildLogs: true
```
In your Jenkins instance web interface, go to **Manage Jenkins > Configuration as Code**.Apply or reload the configuration.Check the configuration using the `View Configuration` button.
### Configure with Groovy{% #configure-with-groovy %}

#### Report through the Datadog Agent (recommended){% #report-through-the-datadog-agent-recommended-2 %}

1. In your Jenkins instance web interface, go to **Manage Jenkins > Script Console**.
1. Run the configuration script:

```groovy
import jenkins.model.Jenkins
import org.datadog.jenkins.plugins.datadog.DatadogGlobalConfiguration
import org.datadog.jenkins.plugins.datadog.configuration.DatadogAgentConfiguration

def jenkins = Jenkins.getInstance()
def datadog = jenkins.getDescriptorByType(DatadogGlobalConfiguration)

def agentHost = 'localhost' // Configure your Datadog Agent host
def agentPort = 8125
def agentLogCollectionPort = 10518 // (Optional) Configure logs collection port as configured in your Datadog Agent
def agentTraceCollectionPort = 8126 // Configure traces collection port
datadog.datadogClientConfiguration = new DatadogAgentConfiguration(agentHost, agentPort, agentLogCollectionPort, agentTraceCollectionPort)

datadog.datadogAppHostname = 'app.datadoghq.com' // the name of the host that you use to access Datadog UI
datadog.enableCiVisibility = true
datadog.collectBuildLogs = true // (Optional) Enable logs collection

datadog.ciInstanceName = 'jenkins' // (Optional) Set your CI Instance name

// Save config
datadog.save()
```

#### Agentless (using an API key){% #agentless-using-an-api-key-2 %}

1. In your Jenkins instance web interface, go to **Manage Jenkins > Script Console**.
1. Run the configuration script:

```groovy
import hudson.util.Secret
import jenkins.model.Jenkins
import org.datadog.jenkins.plugins.datadog.DatadogGlobalConfiguration
import org.datadog.jenkins.plugins.datadog.configuration.DatadogApiConfiguration
import org.datadog.jenkins.plugins.datadog.configuration.api.intake.DatadogIntakeSite
import org.datadog.jenkins.plugins.datadog.configuration.api.intake.DatadogSite
import org.datadog.jenkins.plugins.datadog.configuration.api.key.DatadogTextApiKey

def jenkins = Jenkins.getInstance()
def datadog = jenkins.getDescriptorByType(DatadogGlobalConfiguration)

def site = new DatadogIntakeSite(DatadogSite.) // Pick your Datadog site
def apiKey = new DatadogTextApiKey(Secret.fromString('<YOUR_API_KEY>')) // or `new DatadogCredentialsApiKey('<YOUR_CREDENTIALS_ID>')`
datadog.datadogClientConfiguration = new DatadogApiConfiguration(site, apiKey)

datadog.datadogAppHostname = '' // the name of the host that you use to access Datadog UI
datadog.enableCiVisibility = true
datadog.collectBuildLogs = true // (Optional) Enable logs collection

datadog.ciInstanceName = 'jenkins' // (Optional) Set your CI Instance name

// Save config
datadog.save()
```

### Use environment variables{% #use-environment-variables %}

#### Report through the Datadog Agent (recommended){% #report-through-the-datadog-agent-recommended-3 %}

1. Set the following environment variables on your Jenkins instance machine:

```bash
# Select the Datadog Agent mode
DATADOG_JENKINS_PLUGIN_REPORT_WITH=DSD

# Configure the Agent host
DATADOG_JENKINS_PLUGIN_TARGET_HOST=your-agent-host

# Configure the Traces Collection port (default 8126)
DATADOG_JENKINS_PLUGIN_TARGET_TRACE_COLLECTION_PORT=8126

# Enable CI Visibility
DATADOG_JENKINS_PLUGIN_ENABLE_CI_VISIBILITY=true

# (Optional) Configure your CI Instance name
DATADOG_JENKINS_PLUGIN_CI_VISIBILITY_CI_INSTANCE_NAME=jenkins

# (Optional) Configure Log Collection port as configured in your Datadog Agent
DATADOG_JENKINS_PLUGIN_TARGET_LOG_COLLECTION_PORT=10518

# (Optional) Enable logs collection
DATADOG_JENKINS_PLUGIN_COLLECT_BUILD_LOGS=true

# (Optional) Configure the name of the host that you use to access Datadog UI
DATADOG_JENKINS_PLUGIN_DATADOG_APP_HOSTNAME=app.datadoghq.com
```
Restart your Jenkins instance.
#### Agentless (using an API key){% #agentless-using-an-api-key-3 %}

1. Set the following environment variables on your Jenkins instance machine:

```bash
# Select the Datadog Agent mode
DATADOG_JENKINS_PLUGIN_REPORT_WITH=HTTP

# Configure your Datadog site
DATADOG_JENKINS_PLUGIN_DATADOG_SITE=

# Configure your API key
DATADOG_JENKINS_PLUGIN_TARGET_API_KEY=your-api-key

# Enable CI Visibility
DATADOG_JENKINS_PLUGIN_ENABLE_CI_VISIBILITY=true

# (Optional) Configure your CI Instance name
DATADOG_JENKINS_PLUGIN_CI_VISIBILITY_CI_INSTANCE_NAME=jenkins

# (Optional) Enable logs collection
DATADOG_JENKINS_PLUGIN_COLLECT_BUILD_LOGS=true

# (Optional) Configure the name of the host that you use to access Datadog UI
DATADOG_JENKINS_PLUGIN_DATADOG_APP_HOSTNAME=
```
Restart your Jenkins instance.
## Collect job logs{% #collect-job-logs %}

Job logs collection can be enabled optionally when configuring the Jenkins plugin (see previous section). Both Agentless and Agent-based options are supported.

Logs are billed separately from CI Visibility.

Log retention, exclusion, and indexes are configured in [Log Management](https://docs.datadoghq.com/logs/guide/best-practices-for-log-management/). Logs for Jenkins jobs can be identified by the `source:jenkins` tag.

## Correlate infrastructure metrics{% #correlate-infrastructure-metrics %}

If you are using Jenkins workers, you can correlate pipelines with the infrastructure that is running them. For this feature to work:

1. Install the [Datadog Agent](https://docs.datadoghq.com/getting_started/site/#access-the-datadog-site) in every Jenkins worker.
1. Set and export a new environment variable called `DD_CI_HOSTNAME` in every Jenkins worker with the worker hostname.

- It must be the same hostname that the Datadog Agent is reporting in the infrastructure metrics for that worker.
- You can use fixed values or other environment variables as valid values.

```bash
export DD_CI_HOSTNAME=my-hostname
```

If you are using Kubernetes to manage your Jenkins instances, add the `DD_CI_HOSTNAME` environment variable to the [pod that executes the Jenkins job](https://plugins.jenkins.io/kubernetes/#plugin-content-pod-template). The value of this environment variable depends on what you are using in your Datadog Agent daemonset when reporting the infrastructure metrics.

This is only required for Jenkins workers. For the Jenkins controller, the infrastructure metric correlation does not require additional actions.

**Note**: Infrastructure metric correlation is supported since Jenkins Plugin v5.0.0 or later.

## Enable Test Optimization{% #enable-test-optimization %}

This is an optional step that enables the collection of tests data using [Test Optimization](https://docs.datadoghq.com/continuous_integration/tests/).

See the [Test Optimization documentation](https://docs.datadoghq.com/continuous_integration/tests/setup/) for your language to make sure that the testing framework that you use is supported.

There are different ways to enable Test Optimization inside a Jenkins job or pipeline:

1. Using the Jenkins configuration UI.
1. Adding the `datadog` step inside the pipeline script.
1. Configuring the tracer manually.

For pipelines that spin up a Docker container to execute tests, you can only configure the tracer manually.

### Enable with the Jenkins configuration UI{% #enable-with-the-jenkins-configuration-ui %}

UI-based Test Optimization configuration is available in Datadog Jenkins plugin v5.6.0 or later.

This option is not suitable for pipelines that are configured entirely in `Jenkinsfile` (for example, Multibranch pipelines or pipelines from Organization Folder). For these pipelines use declarative configuration with the `datadog` step (described in the next section).

To enable Test Optimization through the UI do the following:

1. In your Jenkins instance web interface, go to the job or pipeline that you want to instrument and choose the **Configure** option.
1. In the **General** configuration section, tick the **Enable Datadog Test Optimization** checkbox.
1. Enter the name of the service or library being tested into the **Service Name** input. You can choose any value that makes sense to you.
1. Choose the languages for which you want to enable tests instrumentation. Some of the languages do not support configuration through the UI. To configure Test Optimization for these languages, follow the manual [configuration instructions](https://docs.datadoghq.com/tracing/trace_collection/library_config/).
1. Optionally, provide [additional configuration settings](https://docs.datadoghq.com/tracing/trace_collection/library_config/).
1. Click **Save**.

{% image
   source="https://datadog-docs.imgix.net/images/ci/ci-jenkins-plugin-tests-config-2.2cff40406218e29eab4d45620583c0e1.png?auto=format"
   alt="Datadog Test Optimization configuration for Jenkins" /%}

### Enable with the `datadog` pipeline step{% #enable-with-the-datadog-pipeline-step %}

This configuration option is available in Datadog Jenkins plugin v5.6.2 or later.

In declarative pipelines, add the step to a top-level `options` block like so:

```groovy
pipeline {
    agent any
    options {
        datadog(testOptimization: [
            enabled: true,
            serviceName: "my-service", // the name of service or library being tested
            languages: ["JAVA"], // languages that should be instrumented (available options are "JAVA", "JAVASCRIPT", "PYTHON", "DOTNET", "RUBY")
            additionalVariables: ["my-var": "value"]  // additional tracer configuration settings (optional)
        ])
    }
    stages {
        stage('Example') {
            steps {
                echo "Hello world."
            }
        }
    }
}
```

In a scripted pipeline, wrap the relevant section with the `datadog` step like so:

```groovy
datadog(testOptimization: [ enabled: true, serviceName: "my-service", languages: ["JAVASCRIPT"], additionalVariables: [:] ]) {
  node {
    stage('Example') {
      echo "Hello world."
    }
  }
}
```

The other `datadog` settings, such as `collectLogs` or `tags` can be added alongside the `testOptimization` block.

### Enable with manual tracer configuration{% #enable-with-manual-tracer-configuration %}

Follow the manual Test Optimization [configuration instructions](https://docs.datadoghq.com/continuous_integration/tests/setup/) that are specific to your language.

## Propagate Git information{% #propagate-git-information %}

Some features of the Datadog Jenkins plugin need Git information associated with the Jenkins builds to work correctly.

The minimum required Git info for a build is repository URL, branch, commit SHA, and commit author email. This information can be determined by the plugin automatically, propagated from SCM, provided manually with environment variables, or obtained by combining these approaches.

**Note:** If a pipeline checks out multiple repositories, Git info of the repositories that are checked out later in the pipeline has higher priority.

### Propagate Git information from SCM{% #propagate-git-information-from-scm %}

The Jenkins plugin is capable of automatically detecting Git information associated with a build or a pipeline. However, depending on the Jenkins version and the pipeline details, there may be cases when automatic Git data detection is not possible.

In this case you can make the Git information available to the plugin by using the `.each {k,v -> env.setProperty(k, v)}` function after executing the `checkout` or `git` steps. For example:

#### Using Declarative Pipelines{% #using-declarative-pipelines %}

If you're using a declarative pipeline to configure your pipeline, propagate Git information using a `script` block as follows:

Using the `checkout` step:

```groovy
pipeline {
  stages {
    stage('Checkout') {
        script {
          checkout(...).each {k,v -> env.setProperty(k,v)}
        }
    }
    ...
  }
}
```

Using the `git` step:

```groovy
pipeline {
  stages {
    stage('Checkout') {
      script {
        git(...).each {k,v -> env.setProperty(k,v)}
      }
    }
    ...
  }
}
```

#### Using Scripted Pipelines{% #using-scripted-pipelines %}

If you're using a scripted pipeline to configure your pipeline, you can propagate the git information to environment variables directly.

Using the `checkout` step:

```groovy
node {
  stage('Checkout') {
    checkout(...).each {k,v -> env.setProperty(k,v)}
  }
  ...
}
```

Using the `git` step:

```groovy
node {
  stage('Checkout') {
    git(...).each {k,v -> env.setProperty(k,v)}
  }
  ...
}
```

### Set Git information manually{% #set-git-information-manually %}

In case the plugin cannot detect Git information automatically and propagating Git data via SCM is not an option, the necessary Git information can be set manually.

To do so, set the following environment variables.

**Note:** These variables are optional, but if they are set, they take precedence over the Git information set by other Jenkins plugins.

{% dl %}

{% dt %}
`DD_GIT_REPOSITORY_URL` (Optional)
{% /dt %}

{% dd %}
The repository URL of your service.**Example**: `https://github.com/my-org/my-repo.git`
{% /dd %}

{% dt %}
`DD_GIT_BRANCH` (Optional)
{% /dt %}

{% dd %}
The branch name.**Example**: `main`
{% /dd %}

{% dt %}
`DD_GIT_TAG` (Optional)
{% /dt %}

{% dd %}
The tag of the commit (if any).**Example**: `0.1.0`
{% /dd %}

{% dt %}
`DD_GIT_COMMIT_SHA` (Optional)
{% /dt %}

{% dd %}
The commit expressed in the hex 40 chars length form.**Example**: `faaca5c59512cdfba9402c6e67d81b4f5701d43c`
{% /dd %}

{% dt %}
`DD_GIT_COMMIT_MESSAGE` (Optional)
{% /dt %}

{% dd %}
The commit message.**Example**: `Initial commit message`
{% /dd %}

{% dt %}
`DD_GIT_COMMIT_AUTHOR_NAME` (Optional)
{% /dt %}

{% dd %}
The name of the author of the commit.**Example**: `John Smith`
{% /dd %}

{% dt %}
`DD_GIT_COMMIT_AUTHOR_EMAIL` (Optional)
{% /dt %}

{% dd %}
The email of the author of the commit.**Example**: `john@example.com`
{% /dd %}

{% dt %}
`DD_GIT_COMMIT_AUTHOR_DATE` (Optional)
{% /dt %}

{% dd %}
The date when the author submitted the commit expressed in ISO 8601 format.**Example**: `2021-08-16T15:41:45.000Z`
{% /dd %}

{% dt %}
`DD_GIT_COMMIT_COMMITTER_NAME` (Optional)
{% /dt %}

{% dd %}
The name of the committer of the commit.**Example**: `Jane Smith`
{% /dd %}

{% dt %}
`DD_GIT_COMMIT_COMMITTER_EMAIL` (Optional)
{% /dt %}

{% dd %}
The email of the committer of the commit.**Example**: `jane@example.com`
{% /dd %}

{% dt %}
`DD_GIT_COMMIT_COMMITTER_DATE` (Optional)
{% /dt %}

{% dd %}
The date when the committer submitted the commit expressed in ISO 8601 format.**Example**: `2021-08-16T15:41:45.000Z`
{% /dd %}

{% /dl %}

If you set only repository, branch and commit, the plugin will try to extract the rest of the Git information from the `.git` folder.

An example of usage:

```groovy
pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        script {
          def gitVars = git url:'https://github.com/my-org/my-repo.git', branch:'some/feature-branch'

          // Setting Git information manually via environment variables.
          env.DD_GIT_REPOSITORY_URL=gitVars.GIT_URL
          env.DD_GIT_BRANCH=gitVars.GIT_BRANCH
          env.DD_GIT_COMMIT_SHA=gitVars.GIT_COMMIT
        }
      }
    }
    stage('Test') {
      steps {
        // Execute the rest of the pipeline.
      }
    }
  }
}
```

## Include or exclude pipelines{% #include-or-exclude-pipelines %}

You can configure the Jenkins Plugin to include or exclude specific pipelines:

1. In the web interface of your Jenkins instance, go to **Manage Jenkins > Configure System**.
1. Go to the `Datadog Plugin` section by scrolling down the configuration screen.
1. Click on the `Advanced` button.
1. Configure the `Excluded Jobs`.
1. Configure the `Included Jobs`.
1. Save your configuration.

{% dl %}

{% dt %}
**Excluded jobs**
{% /dt %}

{% dd %}
A comma-separated list of Jenkins jobs that should not be monitored. The exclusion applies to all metrics, traces, events, and service checks. Excluded jobs can use regular expressions to reference multiple jobs.**Environment variable**: `DATADOG_JENKINS_PLUGIN_EXCLUDED`**Example**: `susans-job,johns-.*,prod_folder/prod_release`
{% /dd %}

{% dt %}
**Included jobs**
{% /dt %}

{% dd %}
A comma-separated list of Jenkins job names that should be monitored. If the included jobs list is empty, all jobs that are not excluded explicitly are monitored. The inclusion applies to all metrics, traces, events, and service checks. Included jobs can use regular expressions to reference multiple jobs.**Environment variable**: `DATADOG_JENKINS_PLUGIN_INCLUDED`**Example**: `susans-job,johns-.*,prod_folder/prod_release`
{% /dd %}

{% /dl %}

Lists of included and excluded jobs can contain regular expressions, but not glob patterns. To include a job with a specific prefix, use `prefix-.*`ânot `prefix-*`.

## Advanced configuration{% #advanced-configuration %}

### Set the default branch name{% #set-the-default-branch-name %}

To report pipeline results, attach the default branch name (for example, `main`) to pipeline spans in an attribute called `git.default_branch`. This is usually done automatically, but in some cases the plugin cannot extract this information because it might not be provided by Jenkins.

If this happens, set the default branch manually using the `DD_GIT_DEFAULT_BRANCH` environment variable in your build. For example:

```groovy
pipeline {
    agent any
    environment {
        DD_GIT_DEFAULT_BRANCH = 'main'
        ...
    }
    stages {
        ...
    }
}
```

### Set custom tags for your pipelines{% #set-custom-tags-for-your-pipelines %}

The Datadog plugin adds a `datadog` step that allows adding custom tags to your pipeline-based jobs.

In declarative pipelines, add the step to a top-level option block:

```groovy
def DD_TYPE = "release"
pipeline {
    agent any
    options {
        datadog(tags: ["team:backend", "type:${DD_TYPE}", "${DD_TYPE}:canary"])
    }
    stages {
        stage('Example') {
            steps {
                echo "Hello world."
            }
        }
    }
}
```

In scripted pipelines, wrap the relevant section with the `datadog` step:

```groovy
datadog(tags: ["team:backend", "release:canary"]){
    node {
        stage('Example') {
            echo "Hello world."
        }
    }
}
```

#### Integrate with Datadog Teams{% #integrate-with-datadog-teams %}

To display and filter the teams associated with your pipelines, add `team:<your-team>` as a custom tag. The custom tag name must match your [Datadog Teams](https://docs.datadoghq.com/account_management/teams/) team handle exactly.

### Set global custom tags{% #set-global-custom-tags %}

You can configure the Jenkins Plugin to send custom tags (like global tags and global job tags) in all pipeline traces:

1. In the web interface of your Jenkins instance, go to **Manage Jenkins > Configure System**.
1. Go to the `Datadog Plugin` section, scrolling down the configuration screen.
1. Click on the `Advanced` button.
1. Configure the `Global Tags`.
1. Configure the `Global Job Tags`.
1. Save your configuration.

{% dl %}

{% dt %}
**Global tags**
{% /dt %}

{% dd %}
A comma-separated list of tags to apply to all metrics, traces, events, and service checks. Tags can include environment variables that are defined in the Jenkins controller instance.**Environment variable**: `DATADOG_JENKINS_PLUGIN_GLOBAL_TAGS`**Example**: `key1:value1,key2:${SOME_ENVVAR},${OTHER_ENVVAR}:value3`
{% /dd %}

{% dt %}
**Global job tags**
{% /dt %}

{% dd %}
A comma-separated list of regexes to match a job and a list of tags to apply to that job. Tags can include environment variables that are defined in the Jenkins controller instance. Tags can reference match groups in the regex using the `$` symbol.**Environment variable**: `DATADOG_JENKINS_PLUGIN_GLOBAL_JOB_TAGS`**Example**: `(.*?)_job_(.*?)_release, owner:$1, release_env:$2, optional:Tag3`
{% /dd %}

{% /dl %}

## Visualize pipeline data in Datadog{% #visualize-pipeline-data-in-datadog %}

Once the integration is successfully configured, both the [**CI Pipeline List**](https://app.datadoghq.com/ci/pipelines) and [**Executions**](https://app.datadoghq.com/ci/pipeline-executions) pages populate with data after pipelines finish.

The **CI Pipeline List** page shows data for only the default branch of each repository. For more information, see [Search and Manage CI Pipelines](https://docs.datadoghq.com/continuous_integration/search/#search-for-pipelines).

## Troubleshooting{% #troubleshooting %}

### Generate diagnostic flare{% #generate-diagnostic-flare %}

When reporting an issue to the Datadog support team, generate a plugin diagnostic flare and provide it along with the issue description.

To generate the flare do the following:

1. In your Jenkins instance web interface, go to **Manage Jenkins > Troubleshooting > Datadog**.
1. In the Diagnostic Flare form, check which information you want to include in the flare. The default selection works best. The more information you provide, the easier it is to diagnose your issue.
1. Click **Download** to generate and download the flare archive.

### Enable DEBUG log level for the Datadog Plugin{% #enable-debug-log-level-for-the-datadog-plugin %}

If you have any issues with the Datadog Plugin, you can set the logs for the plugin in `DEBUG` level. Using this level you are able to see stacktrace details if an exception is thrown.

1. In your Jenkins instance web interface, go to **Manage Jenkins > System log**.
1. Click on `Add new log recorder` button.
1. Type the log recorder name. E.g: **Datadog Plugin Logs**.
1. Add the following loggers to the list:
   - Logger: `org.datadog.jenkins.plugins.datadog.clients` -> Log Level `ALL`
   - Logger: `org.datadog.jenkins.plugins.datadog.traces` -> Log Level `ALL`
   - Logger: `org.datadog.jenkins.plugins.datadog.logs` -> Log Level `ALL`
   - Logger: `org.datadog.jenkins.plugins.datadog.model` -> Log Level `ALL`
   - Logger: `org.datadog.jenkins.plugins.datadog.listeners` -> Log Level `ALL`
1. Save the configuration.

You may also want to split the loggers into different log recorders.

Once the log recorders are successfully configured, you can check the logs in the `DEBUG` mode by accessing the desired log recorder through **Manage Jenkins > System log**.

If you trigger a Jenkins pipeline, you can search for the message `Send pipeline traces` in the **Datadog Plugin Logs**. This message indicates that the plugin is sending **CI Visibility** data to the **Datadog Agent**.

```text
Send pipeline traces.
...
Send pipeline traces.
...
```

### Pipeline executions data is not available in Datadog{% #pipeline-executions-data-is-not-available-in-datadog %}

#### HTTP connectivity check{% #http-connectivity-check %}

If your Jenkins instance is behind an HTTP proxy, go to **Manage Jenkins** > **Manage Plugins** > **Advanced tab** and make sure the proxy configuration is correct:

- If the Datadog plugin is configured to send data to a Datadog Agent, check that the Agent host has been added to the `No Proxy Hosts` section.
- If the Datadog plugin is configured to send data directly to Datadog (Agentless mode), check that Datadog host has been added to the `No Proxy Hosts` section. The table below shows the supported Datadog sites and their corresponding host values:

| Datadog site | Host value        |
| ------------ | ----------------- |
| US1          | datadoghq.com     |
| US3          | us3.datadoghq.com |
| US5          | us5.datadoghq.com |
| EU1          | datadoghq.eu      |
| AP1          | ap1.datadoghq.com |

#### The Datadog Plugin cannot write payloads to the server{% #the-datadog-plugin-cannot-write-payloads-to-the-server %}

If the following error message appears in the **Jenkins Log**, make sure that the plugin configuration is correct.

```text
Error writing to server
```

If you are using `localhost` as the hostname, change it to the server hostname instead.

### Jenkins logs are not available in Datadog{% #jenkins-logs-are-not-available-in-datadog %}

If the Datadog plugin is configured to send data to a Datadog Agent, do the following:

- Make sure that custom logs collection over TCP is [enabled and configured](https://docs.datadoghq.com/agent/logs/?tab=tcpudp#custom-log-collection) in the Agent.
- Go to the plugin configuration UI and click **Test logs connection** to verify logs connectivity.

### The Datadog Plugin section does not appear in the Jenkins configuration{% #the-datadog-plugin-section-does-not-appear-in-the-jenkins-configuration %}

If the Datadog Plugin section does not appear in Jenkins configuration section, make sure that the plugin is enabled. To do so:

1. In your Jenkins instance web interface, go to **Manage Jenkins > Manage Plugins**.
1. Search for `Datadog Plugin` in the **Installed** tab.
1. Check that the `Enabled` checkbox is marked.
1. If you enable the plugin here, restart your Jenkins instance using the `/safeRestart` URL path.

### The CI Visibility option does not appear in the Datadog Plugin section.{% #the-ci-visibility-option-does-not-appear-in-the-datadog-plugin-section %}

If the CI Visibility option does not appear in the Datadog Plugin section, make sure that the correct version is installed and restart the Jenkins instance. To do so:

1. In your Jenkins instance web interface, go to **Manage Jenkins > Manage Plugins**.
1. Search for `Datadog Plugin` in the **Installed** tab.
1. Check that the installed version is correct.
1. Restart your Jenkins instance using the `/safeRestart` URL path.

### Infrastructure metrics do not get correlated with Jenkins pipelines{% #infrastructure-metrics-do-not-get-correlated-with-jenkins-pipelines %}

Make sure you have gone through the steps to [correlate infrastructure metrics with Jenkins pipelines](https://docs.datadoghq.com/continuous_integration/pipelines/jenkins/?tab=agentlessusinganapikey#correlate-infrastructure-metrics).

If, even after following the steps, infrastructure metrics are still not correlated with Jenkins pipelines, try restarting the Jenkins instance.

## Further reading{% #further-reading %}

- [Explore Pipeline Execution Results and Performance](https://docs.datadoghq.com/continuous_integration/pipelines)
- [Extend Pipeline Visibility by tracing individual commands](https://docs.datadoghq.com/continuous_integration/pipelines/custom_commands/)
- [Troubleshooting CI Visibility](https://docs.datadoghq.com/continuous_integration/troubleshooting/)
