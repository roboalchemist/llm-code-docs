# Source: https://archivedocs.stackstate.com/5.1/stackpacks/integrations/servicenow.md

# ServiceNow

## Overview

The ServiceNow StackPack allows near real time synchronization between ServiceNow and StackState. When the ServiceNow Agent integration is enabled, configuration items (CIs) and their dependencies from the ServiceNow CMDB will be added to the StackState topology as components and relations. ServiceNow change request events are also retrieved.

ServiceNow is a [StackState core integration](https://archivedocs.stackstate.com/5.1/stackpacks/about_integrations#stackstate-core-integrations).

![Data flow](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-f110e7b949a7084db13099472d72d288398457ba%2Fstackpack-servicenow.svg?alt=media)

* Agent V3 connects to the configured [ServiceNow API](#rest-api-endpoints).
* CIs and dependencies for the configured CI types are retrieved from the ServiceNow CMDB (default all). Change request events are retrieved in the same run.
* Agent V3 pushes [retrieved data](#data-retrieved) to StackState:
  * CIs and dependencies are translated into [topology components and relations](#topology).
  * [Tags](#tags) defined in ServiceNow are added to components and relations in StackState. Any defined StackState tags are used by StackState when the topology is retrieved.
  * Change requests are attached to the associated elements as [events](#events) and listed in the StackState Events Perspective.

## Setup

### Prerequisites

To set up the StackState ServiceNow integration, you need to have:

* [StackState Agent V3](https://archivedocs.stackstate.com/5.1/setup/agent/about-stackstate-agent) installed on a machine that can connect to both ServiceNow (via HTTPS) and StackState.
* A running ServiceNow instance.
* A ServiceNow user with access to the required [ServiceNow API endpoints](#rest-api-endpoints).

### Install

Install the ServiceNow StackPack from the StackState UI **StackPacks** > **Integrations** screen. You will need to enter the following details:

* **ServiceNow Instance URL**: The ServiceNow instance URL from which topology data will be collected.
* **ServiceNow Instance Name**: the user-defined name of the ServiceNow account shown in configurations such as views.

### Configure

To enable the ServiceNow check and begin collecting data from ServiceNow, add the following configuration to StackState Agent V3:

1. Edit the Agent integration configuration file `/etc/stackstate-agent/conf.d/servicenow.d/conf.yaml` to include details of your ServiceNow instance:
   * **url** - The REST API URL, uses HTTPS protocol for communication.
   * **user** - A ServiceNow user with access to the required [ServiceNow API endpoints](#rest-api-endpoints)
   * **password** - Use [secrets management](https://archivedocs.stackstate.com/5.1/configure/security/secrets_management) to store passwords outside of the configuration file.

     ```
     init_config:
     # Any global configurable parameters should be added here
     default_timeout: 10

     instances:
     - url: "https://<instance_ID>.service-now.com"
       user: <instance_username>
       password: <instance_password>
       # min_collection_interval: 5 # use in place of collection_interval for Agent V2.14.x or earlier 
       collection_interval: 5
       # batch_size: 1000  
       # change_request_bootstrap_days: 10
       # change_request_process_limit: 1000 
       # timeout: 20
       # verify_https: true
       # cert: /path/to/cert.pem
       # keyfile: /path/to/key.pem
     ```
2. You can also add optional configuration and filters:
   * **batch\_size** - The maximum number of records to be returned (default `2500`, max `10000`).
   * **change\_request\_bootstrap\_days** - On first start, all change requests that have been updated in last N days will be retrieved (default `100`).
   * **change\_request\_process\_limit** - The maximum number of change requests that should be processed (default `1000`).
   * **timeout** - Timeout for requests to the ServiceNow API in seconds (default `20`).
   * **verify\_https** - Verify the certificate when using https (default `true`).
   * **cert** - Path to the certificate file for https verification.
   * **keyfile** - Path to the public key of certificate for https verification.
   * Use queries to [filter change requests retrieved](#use-servicenow-queries-to-filter-retrieved-events-and-ci-types) from ServiceNow (default all).
   * Use queries to [filter the CI types retrieved](#use-servicenow-queries-to-filter-retrieved-events-and-ci-types) (default all).
   * [Specify the CI types](#specify-ci-types-to-retrieve) that should be retrieved (default all).
3. [Restart StackState Agent V3](https://archivedocs.stackstate.com/5.1/setup/agent/about-stackstate-agent#deployment) to apply the configuration changes.
4. Once the Agent has restarted, wait for the Agent to collect data from ServiceNow and send it to StackState.

#### Use ServiceNow queries to filter retrieved events and CI types

1. In ServiceNow, create and copy a filter for CI types or change requests. See the ServiceNow documentation for details on [filtering with sysparm\_query parameters (servicenow.com)](https://developer.servicenow.com/dev.do#!/learn/learning-plans/orlando/servicenow_application_developer/app_store_learnv2_rest_orlando_more_about_query_parameters)
2. Edit the Agent integration configuration file `/etc/stackstate-agent/conf.d/servicenow.d/conf.yaml`.
3. Uncomment the CI type or event that you would like to add a filter to:
   * `cmdb_ci_sysparm_query` - ServiceNow CMDB Configuration Items query.
   * `cmdb_rel_ci_sysparm_query` - ServiceNow CMDB Configuration Items Relations query.
   * `change_request_sysparm_query` - ServiceNow Change Request query.
   * `custom_cmdb_ci_field` - ServiceNow CMDB Configuration Item custom field mapping.
4. Add the filter you copied from ServiceNow. For example

   ```
   ... 
   instances:
     - url: "https://<instance_ID>.service-now.com"
       user: <instance_username>
       password: <instance_password>

       # ServiceNow CMDB Configuration Items query. There is no default value.
       # cmdb_ci_sysparm_query: company.nameSTARTSWITHstackstate

       # ServiceNow CMDB Configuration Items Relations query. There is no default value.
       # cmdb_rel_ci_sysparm_query: parent.company.nameSTARTSWITHstackstate^ORchild.company.nameSTARTSWITHstackstate

       # ServiceNow Change Request query. There is no default value.
       # change_request_sysparm_query: company.nameSTARTSWITHstackstate

       # ServiceNow CMDB Configuration Item custom field mapping. The default value is cmdb_ci.
       # custom_cmdb_ci_field: u_configuration_item
   ...
   ```
5. [Restart StackState Agent V3](https://archivedocs.stackstate.com/5.1/setup/agent/about-stackstate-agent#deployment) to apply the configuration changes.

#### Specify CI types to retrieve

By default, all available ServiceNow CI types will be sent to StackState. If you prefer to work with a specific set of resource types, you can configure the Agent integration to filter the CI types it retrieves:

1. Edit the Agent integration configuration file `/etc/stackstate-agent/conf.d/servicenow.d/conf.yaml`.
   * A subset of the available CI types is listed and commented out.
2. Uncomment the line `include_resource_types` and the CI types you would like to send to StackState. You can add any valid ServiceNow CI type to the **include\_resource\_types** list, however, components from resource types that you have added will appear on the **Uncategorized** layer of a StackState view.

   ```
    instances:
      - url: "https://<instance_ID>.service-now.com"
        user: <instance_username>
        password: <instance_password>
        batch_size: 100
        #    include_resource_types: # optional and by default includes all resource types(sys Class Names)
        #        - cmdb_ci_netgear
        #        - cmdb_ci_ip_router
        #        - cmdb_ci_aix_server
        #        - cmdb_ci_storage_switch
        #        - cmdb_ci_win_cluster
        #        - cmdb_ci_email_server
        #        - cmdb_ci_web_server
        #        - cmdb_ci_app_server
        #        - cmdb_ci_printer
        #        - cmdb_ci_cluster
        #        - cmdb_ci_cluster_node
        #        - cmdb_ci_computer
        #        - cmdb_ci_msd
        #        - cmdb_ci
        #        - cmdb_ci_unix_server
        #        - cmdb_ci_win_cluster_node
        #        - cmdb_ci_datacenter
        #        - cmdb_ci_linux_server
        #        - cmdb_ci_db_ora_catalog
        #        - cmdb_ci_win_server
        #        - cmdb_ci_zone
        #        - cmdb_ci_appl
        #        - cmdb_ci_computer_room
        #        - cmdb_ci_ip_switch
        #        - service_offering
        #        - cmdb_ci_disk
        #        - cmdb_ci_peripheral
        #        - cmdb_ci_service_group
        #        - cmdb_ci_db_mysql_catalog
        #        - cmdb_ci_ups
        #        - cmdb_ci_service
        #        - cmdb_ci_app_server_java
        #        - cmdb_ci_spkg
        #        - cmdb_ci_database
        #        - cmdb_ci_rack
        #        - cmdb_ci_server
        #        - cmdb_ci_network_adapter
   ```
3. [Restart StackState ](https://archivedocs.stackstate.com/5.1/setup/agent/about-stackstate-agent#deployment)to apply the configuration changes.

### Status

To check the status of the ServiceNow integration, run the status subcommand and look for ServiceNow under `Running Checks`:

```
sudo stackstate-agent status
```

### Upgrade

When a new version of the ServiceNow StackPack is available in your instance of StackState, you will be prompted to upgrade in the StackState UI on the page **StackPacks** > **Integrations** > **ServiceNow**. For a quick overview of recent StackPack updates, check the [StackPack versions](https://archivedocs.stackstate.com/5.1/setup/upgrade-stackstate/stackpack-versions) shipped with each StackState release.

For considerations and instructions on upgrading a StackPack, see [how to upgrade a StackPack](https://archivedocs.stackstate.com/5.1/about-stackpacks#upgrade-a-stackpack).

## Integration details

### Data retrieved

#### Events

The ServiceNow check retrieves the following events data from ServiceNow:

| Data            | Description                                                                                                                                                                                                                                                                                     |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Change requests | The change requests retrieved can be [filtered using ServiceNow queries](#use-servicenow-queries-to-filter-retrieved-events-and-ci-types) and will be visible in the StackState [Events Perspective](https://archivedocs.stackstate.com/5.1/use/stackstate-ui/perspectives/events_perspective). |

#### Metrics

The ServiceNow check doesn't retrieve any metrics data.

#### Tags

All tags defined in ServiceNow will be retrieved and added to the associated components and relations in StackState.

The ServiceNow integration also understands StackState [common tags](https://archivedocs.stackstate.com/5.1/configure/topology/tagging#common-tags). These StackState tags can be assigned to elements in ServiceNow to influence the way that the resulting topology is built in StackState. For example, by placing a component in a specific layer or domain.

#### Topology

The ServiceNow check retrieves the following topology data from the ServiceNow CMDB:

| Data       | Description                                                                                                  |
| ---------- | ------------------------------------------------------------------------------------------------------------ |
| Components | CI types retrieved from the ServiceNow CMDB, see [filter retrieved CI types](#specify-ci-types-to-retrieve). |
| Relations  | Relations retrieved from the `cmdb_rel_ci` table.                                                            |

{% hint style="info" %}
The ServiceNow integration understands StackState [common tags](https://archivedocs.stackstate.com/5.1/configure/topology/tagging#common-tags). These StackState tags can be assigned to elements in ServiceNow to influence the way that the resulting topology is built in StackState. For example, by placing a component in a specific layer or domain.
{% endhint %}

#### Traces

The ServiceNow check doesn't retrieve any traces data.

### REST API endpoints

The ServiceNow user configured in StackState must have access to read the ServiceNow `TABLE` API. The specific table names and endpoints used in the StackState integration are described below. All named REST API endpoints use the HTTPS protocol for communication.

| Table Name      | REST API Endpoint               |
| --------------- | ------------------------------- |
| change\_request | `/api/now/table/change_request` |
| cmdb\_ci        | `/api/now/table/cmdb_ci`        |
| cmdb\_rel\_type | `/api/now/table/cmdb_rel_type`  |
| cmdb\_rel\_ci   | `/api/now/table/cmdb_rel_ci`    |

{% hint style="info" %}
Refer to the ServiceNow product documentation for details on [how to configure a ServiceNow user and assign roles](https://docs.servicenow.com/bundle/geneva-servicenow-platform/page/administer/users_and_groups/task/t_CreateAUser.html).
{% endhint %}

### ServiceNow views in StackState

When the ServiceNow integration is enabled, the following ServiceNow specific views are available in StackState:

* ServiceNow Applications
* ServiceNow Business Processes
* ServiceNow Discovered
* ServiceNow Infrastructure and Network
* ServiceNow Machines and Load balancers

### Open source

The code for the StackState ServiceNow check is open source and available on GitHub at: <https://github.com/StackVista/stackstate-agent-integrations/tree/master/servicenow>

## Troubleshooting

Troubleshooting steps for any known issues can be found in the [StackState support knowledge base](https://support.stackstate.com/hc/en-us/search?category=360002777619\&filter_by=knowledge_base\&query=ServiceNow).

## Uninstall

To uninstall the ServiceNow StackPack and disable the ServiceNow check:

1. Go to the StackState UI **StackPacks** > **Integrations** > **ServiceNow** screen and click UNINSTALL.
   * All ServiceNow specific configuration will be removed from StackState.
2. Remove or rename the Agent integration configuration file, for example:

   ```
    mv servicenow.d/conf.yaml servicenow.d/conf.yaml.bak
   ```
3. [Restart StackState ](https://archivedocs.stackstate.com/5.1/setup/agent/about-stackstate-agent#deployment)to apply the configuration changes.

## Release notes

**ServiceNow StackPack v5.3.3 (2022-06-13)**

* Improvement: Updated documentation

**ServiceNow StackPack v5.3.2 (2022-06-03)**

* Improvement: Updated documentation

**ServiceNow StackPack v5.3.1 (2021-04-12)**

* Improvement: Common bumped from 2.5.0 to 2.5.1

## See also

* [StackState](https://archivedocs.stackstate.com/5.1/setup/agent/about-stackstate-agent)
* [Secrets management](https://archivedocs.stackstate.com/5.1/configure/security/secrets_management)
* [StackState Agent integrations - ServiceNow (github.com)](https://github.com/StackVista/stackstate-agent-integrations/tree/master/servicenow)
* [How to configure a ServiceNow user and assign roles (servicenow.com)](https://docs.servicenow.com/bundle/geneva-servicenow-platform/page/administer/users_and_groups/task/t_CreateAUser.html)
* [Filtering with sysparm\_query parameters (servicenow.com)](https://developer.servicenow.com/dev.do#!/learn/learning-plans/orlando/servicenow_application_developer/app_store_learnv2_rest_orlando_more_about_query_parameters)
