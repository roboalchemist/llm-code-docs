# Source: https://archivedocs.stackstate.com/5.1/stackpacks/integrations/splunk/splunk_stackpack.md

# Splunk

## Overview

The StackState Splunk integration synchronizes events, metrics, health and topology data from Splunk to StackState. The integration uses [StackState Agent V2](https://archivedocs.stackstate.com/5.1/setup/agent/about-stackstate-agent) to collect Splunk events, metrics, health and topology data.

Splunk is a [StackState core integration](https://archivedocs.stackstate.com/5.1/stackpacks/about_integrations#stackstate-core-integrations).

![Data flow](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-c8942ea3a627ec18f8a592b241e2ea5b222b29f1%2Fstackpack-splunk.svg?alt=media)

* StackState Agent V2 periodically connects to the configured Splunk instance to execute Splunk saved searches and retrieve data:
  * Topology data from the searches configured in the Splunk Topology Agent check.
  * Metrics data from the searches configured in the Splunk Metrics Agent check.
  * Events data from the searches configured in the Splunk Events Agent check.
  * Health data from the searches configured in the Splunk Health Agent check.
* The Agents push retrieved data to StackState.
* StackState translates incoming data:
  * [Topology data](#topology) is translated into components and relations.
  * [Metrics data](#metrics) is available in StackState as a metrics telemetry stream.
  * [Events](#events) are available in StackState as a log telemetry stream.
  * [Health](#health) information is added to associated components and relations.

## Setup

### Prerequisites

* A running Splunk instance.
* A Splunk user account with access to Splunk saved searches. The user should have the capability `search` to dispatch and read Splunk saved searches.
* A compatible [StackState Agent V2](https://archivedocs.stackstate.com/5.1/setup/agent/about-stackstate-agent) installed on a machine that can connect to both Splunk and StackState.

### Install

The Splunk StackPack provides all the necessary configuration to easily work with Splunk topology data in StackState. Install the Splunk StackPack from the StackState UI **StackPacks** > **Integrations** screen. You will need to enter the following details:

* **Splunk instance name** - A unique name to identify the Splunk instance in StackState.
* **Splunk API URL** - The URL where the Splunk API can be reached. For example: `http://splunk.network.local:8089`.

After the StackPack has been installed, you should follow the instructions below to configure the required Splunk checks on StackState Agent V2.

### Configure

A Splunk check must be configured on StackState Agent V2 for each type of data you want to retrieve from Splunk:

* [Splunk Health check](https://archivedocs.stackstate.com/5.1/stackpacks/integrations/splunk/splunk_health) - to retrieve health data from Splunk
* [Splunk Topology check](https://archivedocs.stackstate.com/5.1/stackpacks/integrations/splunk/splunk_topology) - to retrieve topology data from Splunk
* [Splunk Events check](https://archivedocs.stackstate.com/5.1/stackpacks/integrations/splunk/splunk_events) - to retrieve events data from Splunk
* [Splunk Metrics check](https://archivedocs.stackstate.com/5.1/stackpacks/integrations/splunk/splunk_metrics) - to retrieve metrics data from Splunk

### Authentication

Each Splunk check configured on StackState Agent V2 must include authentication details to allow the Agent to connect to your Splunk instance and execute the configured Splunk saved searches.

Two authentication mechanisms are available:

* [Token-based authentication (recommended)](#token-based-authentication)
* [HTTP basic authentication](#http-basic-authentication)

#### Token-based Authentication

Token-based authentication supports Splunk authentication tokens. An initial Splunk token is provided in the Splunk check configuration. This initial token is used the first time the check starts, it's then exchanged for a new token. For details on using token based authentication with Splunk, see the [Splunk documentation (docs.splunk.com)](https://docs.splunk.com/Documentation/Splunk/8.1.3/Security/Setupauthenticationwithtokens).

Token-based authentication is preferred over HTTP basic authentication and will override basic authentication in case both are configured.

{% tabs %}
{% tab title="Example check configuration with token-based authentication" %}

```
instances:
    - url: "https://localhost:8089"

    # username: "admin" ## deprecated
    # password: "admin" ## deprecated

    # verify_ssl_certificate: false

    authentication:
      token_auth:
        name: "api-user"
        initial_token: "my-initial-token-hash"
        audience: "search"
        token_expiration_days: 90
        renewal_days: 10
```

{% endtab %}
{% endtabs %}

To enable token-based authentication, the following parameters should be included in the section `authentcation.token_auth` of each StackState Agent V2 Splunk check configuration file:

* **name** - Name of the user who will use this token.
* **initial\_token** - An initial, valid token. This token will be used once only and then replaced with a new generated token requested by the integration.
* **audience** - The Splunk token audience.
* **token\_expiration\_days** - Validity of the newly requested token. Default 90 days.
* **renewal\_days** - Number of days before a new token should be refreshed. Default 10 days.

The first time the check runs, the configured `initial_token` will be exchanged for a new token. After the configured `renewal_days` days, another new token will be requested from Splunk with a validity of `token_expiration_days`.

#### HTTP basic authentication

{% hint style="info" %}
It's recommended to use [token-based authentication](#token-based-authentication).
{% endhint %}

With HTTP basic authentication, the `username` and `password` specified in the StackState Agent V2 check configuration files are used to connect to Splunk. These parameters are specified in the section `authentication.basic_auth` of each StackState Agent V2 Splunk check configuration file.

{% tabs %}
{% tab title="Example check configuration with HTTP basic authentication" %}

```
instances:
    - url: "https://localhost:8089"

    # username: "admin" ## deprecated - don't use
    # password: "admin" ## deprecated - don't use

    # verify_ssl_certificate: false

    authentication:
      basic_auth:
        username: "admin"
        password: "admin"
```

{% endtab %}
{% endtabs %}

### Status

To check the status of the Splunk integration, run the status subcommand and look for `splunk_topology`, `splunk_metrics` or `splunk_events` under `Running Checks`:

```
sudo stackstate-agent status
```

## Integration details

### Data retrieved

The Splunk integration can retrieve the following data:

* [Events](#events)
* [Metrics](#metrics)
* [Topology](#topology)
* [Health](#health)

#### Events

When the Splunk Events Agent check is configured, events will be retrieved from the configured Splunk saved search or searches. Events retrieved from splunk are available in StackState as a log telemetry stream in the `stackstate-generic-events` data source. This can be [mapped to associated components](https://archivedocs.stackstate.com/5.1/use/metrics/add-telemetry-to-element).

For details on how to configure the events retrieved, see the [Splunk Events check configuration](https://archivedocs.stackstate.com/5.1/stackpacks/integrations/splunk/splunk_events).

#### Metrics

When the Splunk Metrics Agent check is configured, metrics will be retrieved from the configured Splunk saved search or searches. One metric can be retrieved from each saved search. Metrics retrieved from splunk are available in StackState as a metrics telemetry stream in the `stackstate-metrics` data source. This can be [mapped to associated components](https://archivedocs.stackstate.com/5.1/use/metrics/add-telemetry-to-element).

For details on how to configure the metrics retrieved, see the [Splunk Metrics check configuration](https://archivedocs.stackstate.com/5.1/stackpacks/integrations/splunk/splunk_metrics).

#### Topology

When the Splunk StackPack is installed, and a Splunk Topology Agent check is configured, topology will be retrieved from the configured Splunk saved searches. The check that you should configure depends on the StackState Agent that you will use to retrieve topology data.

For details on how to configure the components and relations retrieved, see the [Splunk Topology check configuration](https://archivedocs.stackstate.com/5.1/stackpacks/integrations/splunk/splunk_topology).

If you have an existing Splunk Topology integration configured to use StackState Agent V1 (legacy) and would like to upgrade to use StackState Agent V2, refer to the [Agent migration instructions](https://archivedocs.stackstate.com/5.1/setup/agent/migrate-agent-v1-to-v2).

#### Health

When the Splunk Health Agent check is configured, health check states will be retrieved from the configured Splunk saved searches. Retrieved health check states are mapped to the associated components and relations in StackState.

For details on how to configure the health retrieved, see the [Splunk Health check configuration](https://archivedocs.stackstate.com/5.1/stackpacks/integrations/splunk/splunk_health).

#### Traces

The StackState Splunk integration doesn't retrieve any trace data.

### REST API endpoints

StackState Agent V2 connects to the Splunk API at the endpoints listed below. The same endpoints are used to retrieve events, metrics and topology data.

| Endpoint                                                               | Description               |
| ---------------------------------------------------------------------- | ------------------------- |
| `/services/auth/login?output_mode=json`                                | Auth login                |
| `/services/authorization/tokens?output_mode=json`                      | Create token              |
| `/services/saved/searches?output_mode=json&count=-1`                   | List of saved searches    |
| `/servicesNS/<user>/<app>/saved/searches/<saved_search_name>/dispatch` | Dispatch the saved search |
| `/services/search/jobs/<saved_search_id>/control`                      | Finalize the saved search |

For further details, see the [Splunk API documentation (docs.splunk.com)](https://docs.splunk.com/Documentation/Splunk/8.1.3/RESTREF/RESTprolog).

### Open source

The Splunk StackPack and the Agent checks for Splunk Events, metrics and topology are open source and available on GitHub at the links below:

* [Splunk StackPack (github.com)](https://github.com/StackVista/stackpack-splunk)
* [Splunk Topology check (github.com)](https://github.com/StackVista/stackstate-agent-integrations/tree/master/splunk_topology)
* [Splunk Metrics check (github.com)](https://github.com/StackVista/stackstate-agent-integrations/tree/master/splunk_metric)
* [Splunk Events check (github.com)](https://github.com/StackVista/stackstate-agent-integrations/tree/master/splunk_event)
* [Splunk Health check (github.com)](https://github.com/StackVista/stackstate-agent-integrations/tree/master/splunk_health)

## Troubleshooting

Troubleshooting steps for any known issues can be found in the [StackState support Knowledge base](https://support.stackstate.com/hc/en-us/search?category=360002777619\&filter_by=knowledge_base\&query=Splunk).

## Uninstall

To uninstall the Splunk StackPack, go to the StackState UI **StackPacks** > **Integrations** > **Splunk** screen and click **UNINSTALL**. All Splunk topology specific configuration will be removed from StackState.

For instructions on how to disable the Splunk Agent checks, see:

* [Disable the Splunk Topology Agent check](https://archivedocs.stackstate.com/5.1/stackpacks/integrations/splunk_topology#disable-the-agent-check)
* [Disable the Splunk Metrics Agent check](https://archivedocs.stackstate.com/5.1/stackpacks/integrations/splunk_metrics#disable-the-agent-check)
* [Disable the Splunk Events Agent check](https://archivedocs.stackstate.com/5.1/stackpacks/integrations/splunk_events#disable-the-agent-check)
* [Disable the Splunk Health Agent check](https://archivedocs.stackstate.com/5.1/stackpacks/integrations/splunk_health#disable-the-agent-check)

## Release notes

The [Splunk StackPack release notes](https://github.com/StackVista/stackpack-splunk/blob/master/src/main/stackpack/resources/RELEASE.md) are available on GitHub.

## See also

Configure the StackState Agent V2 Splunk checks:

* [Splunk Health check](https://archivedocs.stackstate.com/5.1/stackpacks/integrations/splunk/splunk_health) - to retrieve health data from Splunk
* [Splunk Topology check](https://archivedocs.stackstate.com/5.1/stackpacks/integrations/splunk/splunk_topology) - to retrieve topology data from Splunk
* [Splunk Events check](https://archivedocs.stackstate.com/5.1/stackpacks/integrations/splunk/splunk_events) - to retrieve events data from Splunk
* [Splunk Metrics check](https://archivedocs.stackstate.com/5.1/stackpacks/integrations/splunk/splunk_metrics) - to retrieve metrics data from Splunk

Other resources:

* [Set up Splunk authentication with tokens (docs.splunk.com)](https://docs.splunk.com/Documentation/Splunk/8.1.3/Security/Setupauthenticationwithtokens).
* [Splunk API documentation (docs.splunk.com)](https://docs.splunk.com/Documentation/Splunk/8.1.3/RESTREF/RESTprolog)
