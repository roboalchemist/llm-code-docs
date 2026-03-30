# Source: https://archivedocs.stackstate.com/5.1/stackpacks/integrations/scom.md

# SCOM

## Overview

The SCOM StackPack is used to create a near real time synchronisation with your SCOM instance. The SCOM integration can be configured to run as either an API integration or PowerShell integration, these are described in the tabs below the diagram.

SCOM is a [StackState curated integration](https://archivedocs.stackstate.com/5.1/stackpacks/about_integrations#stackstate-curated-integrations).

![Data flow](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-ccde89e3d83b2608368992b6fc6531d8e01a2931%2Fstackpack-scom.svg?alt=media)

{% tabs %}
{% tab title="API integration" %}

#### API integration

The StackState SCOM API integration sends requests to the SCOM API to retrieve topology data and events.

* connects to the configured [SCOM API](#rest-api-endpoints).
* Topology data and events for the configured criteria are retrieved from SCOM.
* Agent V3 pushes [retrieved data](#data-retrieved) to StackState.
* StackState translates incoming SCOM topology data into components and relations. Incoming events are used to determine component health state and publish SCOM alerts in StackState.

**When to choose API integration**

The SCOM API integration produces a clean topology in StackState by allowing you to specify the topology to collect. You can run the SCOM check from any StackState Agent V3 as long as it can connect to both the SCOM API and StackState.

Retrieving a large topology can require a high number of API requests, this can take time and may place some stress on your SCOM system. The size of topology you can retrieve may also be limited by the number of requests possible. To avoid this, use the SCOM PowerShell integration.
{% endtab %}

{% tab title="PowerShell integration" %}

#### PowerShell integration

The StackState SCOM PowerShell integration runs PowerShell scripts on the SCOM box to retrieve topology data and events.

* PowerShell scripts in Agent V3 collect topology data and events from SCOM.
* Agent V3 pushes [retrieved data](#data-retrieved) to StackState.
* StackState translates incoming SCOM topology data into components and relations. Incoming events are used to determine component health state and publish SCOM alerts in StackState.

**When to choose PowerShell integration**

The PowerShell integration retrieves all SCOM topology data quickly without placing strain on your SCOM system. As a result, there is no limit on the size of topology that can be retrieved.

The PowerShell integration scripts must be run by an instance of StackState Agent V3 installed on the same box as SCOM and will always retrieve all topology data. This might be undesirable or confusing when viewed in StackState. If you would like to specify a criteria for the data to be retrieved or need to run the integration from a StackState Agent installed elsewhere, you should use the SCOM API integration.
{% endtab %}
{% endtabs %}

## Setup

### Prerequisites

{% tabs %}
{% tab title="API integration" %}
To set up the StackState SCOM API integration, you need to have:

* [StackState Agent V3](https://archivedocs.stackstate.com/5.1/setup/agent/about-stackstate-agent) must be installed on any machine that can connect to both SCOM and StackState.
* A running SCOM instance (version 1806 or 2019).
* A SCOM user with the role **Operations Manager Read-Only Operators**.
  {% endtab %}

{% tab title="PowerShell integration" %}
To set up the StackState SCOM PowerShell integration, you need to have:

* [StackState Agent V3](https://archivedocs.stackstate.com/5.1/setup/agent/about-stackstate-agent) must be installed on the same machine running SCOM.
* A running SCOM instance (version 1806 or 2019).
  {% endtab %}
  {% endtabs %}

### Install

Install the SCOM StackPack from the StackState UI **StackPacks** > **Integrations** screen. You will need to enter the following details:

* **SCOM Instance URL**: the SCOM instance URL from which topology need to be collected.

### Configure

{% tabs %}
{% tab title="API integration" %}
To enable the SCOM check and begin collecting data from SCOM, add the following configuration to StackState Agent V3:

1. Edit the Agent integration configuration file `/etc/stackstate-agent/conf.d/scom.d/conf.yaml` to include details of your SCOM instance:
   * **hostip** - SCOM IP.
   * **domain** - active directory domain where the SCOM is located.
   * **username**
   * **password** - use [secrets management](https://archivedocs.stackstate.com/5.1/configure/security/secrets_management) to store passwords outside of the configuration file.
   * **auth\_mode** - Network or Windows (Default is Network).
   * **integration mode** - to use the API integration, set to `api`.
   * **max\_number\_of\_requests** - The maximum number of requests that should be sent to the SCOM API. See how to [determine the required number of API requests](#determine-the-required-number-of-api-requests), default 10000.
   * **criteria** - A query to [specify the components to retrieve data for](#specify-the-components-to-retrieve-data-for).

     ```
     init_config:
       
       
     instances:
     # run every minute
     - # min_collection_interval: 60 # use in place of collection_interval for Agent V2.14.x or earlier 
       collection_interval: 60
       hostip: localhost
       domain: stackstate
       username: <username>
       password: <password>
       auth_mode: Network
       integration_mode: api    # can be api or powershell, default api
       max_number_of_requests: 10000   # default 10000
       criteria : "(FullName LIKE 'Microsoft.Windows.Computer:%')" # an Operations Manager Data Query
     ```
2. [Restart StackState Agent V3](https://archivedocs.stackstate.com/5.1/setup/agent/about-stackstate-agent#deployment) to apply the configuration changes.

**Specify the components to retrieve data for**

The components to retrieve data for can be defined using an [Operations Manager Data Query (learn.microsoft.com)](https://learn.microsoft.com/en-us/previous-versions/system-center/developer/bb437497\(v=msdn.10\)). For example, to retrieve data for all Microsoft Windows computers:

```
criteria : “(FullName LIKE ‘Microsoft.Windows.Computer:%’)”
```

Errors in the configured criteria query will be reported in the [StackState Agent log file](https://archivedocs.stackstate.com/5.1/setup/agent/about-stackstate-agent).

```
2020-11-05 09:19:31 GMT | ERROR | ... | (scom2.py:114) | Invalid criteria :The property FullNsame is not valid for the given criteria.
```

**Determine the required number of API requests**

Use the script below to determine the number of components that match a criteria query and the number of dependencies. Add these numbers together and multiply by 2 to find the required number of API requests to retrieve topology data from SCOM. Two API requests are required to retrieve data for each component and each dependency.

```
$components = (Get-SCOMManagementGroup).GetMonitoringObjects("FullName LIKE 'Microsoft.Windows.Computer:%'")
"total number of components that match criteria: "+$components.count 
$deps= ($components.GetRelatedMonitoringObjects('Recursive')).count
"Total number of dependencies: "+ $deps
```

As two API requests are required to retrieve data for each component and each dependency, the configured `max_number_of_requests` must be higher than the returned `total number of components that match criteria` AND `total number of dependencies` multiplied by 2.
{% endtab %}

{% tab title="PowerShell integration" %}
To enable the SCOM check and begin collecting data from SCOM, add the following configuration to StackState Agent V3 running on the same box as your SCOM instance:

1. Edit the Agent integration configuration file `/etc/stackstate-agent/conf.d/scom.d/conf.yaml` to include details of your SCOM instance:
   * **integration mode** - to use the PowerShell integration, set to `powershell`.

     ```
     init_config:
       # run every minute
       # min_collection_interval: 60 # use in place of collection_interval for Agent V2.14.x or earlier 
       collection_interval: 60
     instances:
     - integration_mode: powershell    # api or powershell, default api
     ```
2. [Restart StackState Agent V3](https://archivedocs.stackstate.com/5.1/setup/agent/about-stackstate-agent#deployment) to apply the configuration changes.
   {% endtab %}
   {% endtabs %}

## Status

### Integration status

To check the status of the SCOM integration, run the status subcommand and look for SCOM under `Running Checks`:

```
sudo stackstate-agent status
```

### API connectivity (API integration only)

To check connectivity between StackState Agent V3 and the SCOM API, open the [StackState Agent log file](https://archivedocs.stackstate.com/5.1/setup/agent/about-stackstate-agent) and search for the SCOM `Connection Status Code`. Connection status is reported as an HTTP status code - `200` is a good connection, other codes show a problem with connectivity.

```
(scom.py:118) | Connection Status Code 200
```

## Integration details

### REST API endpoints

Retrieving topology data from SCOM requires 2 API requests per component.

| API endpoint                               | Description                              |
| ------------------------------------------ | ---------------------------------------- |
| `OperationsManager/data/scomObjects`       | Get type of component.                   |
| `OperationsManager/data/objectInformation` | Get component information and relations. |
| `OperationsManager/data/alert`             | Get alerts.                              |

### Data retrieved

#### Events

Alerts and Health state from SCOM are available in StackState as events.

| Data         | Description                                                                                                                                                                                                              |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Alerts       | The following alert fields are retrieved: `id`, `name`, `monitoringobjectdisplayname`, `description`, `resolutionstate`, `timeadded`, `monitoringobjectpath`.                                                            |
| Health state | The component health state retrieved from SCOM is used to determine component health in StackState: `Healthy` = green `Warning` = orange `Critical` = red `Not monitored`, `Out of contact` or `Maintenance mode` = gray |

#### Metrics

The SCOM check doesn't retrieve any metrics data.

#### Topology

Retrieved topology data is visible in the StackState UI SCOM view, named \**SCOM.\** .

* Components
* Relations

#### Traces

The SCOM check doesn't retrieve any traces data.

### Open source

The code for the StackState SCOM check is open source and available on GitHub at: <https://github.com/StackVista/stackstate-agent-integrations/tree/master/scom>

## Troubleshooting

Troubleshooting steps for any known issues can be found in the [StackState support Knowledge base](https://support.stackstate.com/hc/en-us/search?category=360002777619\&filter_by=knowledge_base\&query=SCOM).

## Uninstall

To uninstall the SCOM StackPack and disable the SCOM check:

1. Go to the StackState UI **StackPacks** > **Integrations** > **SCOM** screen and click **UNINSTALL**.
   * All SCOM specific configuration will be removed from StackState.
2. Remove or rename the Agent integration configuration file, for example:

   ```
    mv scom.d/conf.yaml scom.d/conf.yaml.bak
   ```
3. [Restart StackState Agent V3](https://archivedocs.stackstate.com/5.1/setup/agent/about-stackstate-agent#deployment) to apply the configuration changes.

## Release notes

**SCOM StackPack v2.1.1 (2021-04-12)**

* Improvement: Common bumped from 2.5.0 to 2.5.1

## See also

* [StackState Agent V3](https://archivedocs.stackstate.com/5.1/setup/agent/about-stackstate-agent)
* [Secrets management in StackState](https://archivedocs.stackstate.com/5.1/configure/security/secrets_management)
* [StackState Agent integrations - SCOM (github.com)](https://github.com/StackVista/stackstate-agent-integrations/tree/master/scom)
* [Operations Manager API reference (learn.microsoft.com)](https://learn.microsoft.com/en-us/rest/api/operationsmanager/)
* [Using Operations Manager data queries (learn.microsoft.com)](https://learn.microsoft.com/en-us/previous-versions/system-center/developer/bb437497\(v=msdn.10\))
