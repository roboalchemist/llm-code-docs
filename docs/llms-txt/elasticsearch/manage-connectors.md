# Source: https://www.elastic.co/docs/deploy-manage/manage-connectors

﻿---
title: Connectors
description: Connectors serve as a central place to store connection information for both Elastic and third-party systems. They enable the linking of actions to rules,...
url: https://www.elastic.co/docs/deploy-manage/manage-connectors
products:
  - Elastic Cloud Serverless
  - Kibana
applies_to:
  - Elastic Cloud Serverless: Generally available
  - Elastic Stack: Generally available
---

# Connectors
Connectors serve as a central place to store connection information for both Elastic and third-party systems. They enable the linking of actions to rules, which execute as background tasks on the Kibana server when rule conditions are met. This allows rules to route actions to various destinations such as log files, ticketing systems, and messaging tools. Different Kibana apps may have their own rule types, but they typically share connectors. The **Connectors** provides a central location to view and manage all connectors in the current space.
You can find the **Connectors** management page in the navigation menu or use the [global search field](https://www.elastic.co/docs/explore-analyze/find-and-organize/find-apps-and-objects).
<note>
  This page is about Kibana connectors that integrate with services like generative AI model providers. If you’re looking for content connectors that synchronize third-party data into Elasticsearch, refer to [Connector clients](https://www.elastic.co/docs/reference/search-connectors).
</note>


## Required permissions

Access to connectors is granted based on your privileges to alerting-enabled features. For more information, go to [Security](/docs/explore-analyze/alerting/alerts/alerting-setup#alerting-security).

## Connector networking configuration

<applies-to>
  - Elastic Stack: Generally available
</applies-to>

If you're using Elastic Stack, use the [action configuration settings](https://www.elastic.co/docs/reference/kibana/configuration-reference/alerting-settings#action-settings) to customize connector networking configurations, such as proxies, certificates, or TLS settings. You can set configurations that apply to all your connectors or use `xpack.actions.customHostSettings` to set per-host configurations.

## Connector list

In **Connectors**, you can find a list of the connectors in the current space. You can use the search bar to find specific connectors by name and type. The **Type** dropdown also enables you to filter to a subset of connector types.
![Filtering the connector list by types of connectors](https://www.elastic.co/docs/deploy-manage/images/kibana-connector-filter-by-type.png)

You can delete individual connectors using the trash icon. Alternatively, select multiple connectors and delete them in bulk using the **Delete** button.
![Deleting connectors individually or in bulk](https://www.elastic.co/docs/deploy-manage/images/kibana-connector-delete.png)

<note>
  You can delete a connector even if there are still actions referencing it. When this happens the action will fail to run and errors appear in the Kibana logs.
</note>


## Creating a new connector

New connectors can be created with the **Create connector** button, which guides you to select the type of connector and configure its properties. For a full list of available connectors, see [Available connectors](https://www.elastic.co/docs/reference/kibana/connectors-kibana).
<note>
  Some connector types are paid commercial features, while others are free. For a comparison of the Elastic subscription levels, go to [the subscription page](https://www.elastic.co/subscriptions).
</note>

![Connector select type](https://www.elastic.co/docs/deploy-manage/images/kibana-connector-select-type.png)

After you create a connector, it is available for use any time you set up an action in the current space.
<tip>
  For out-of-the-box and standardized connectors, refer to [preconfigured connectors](https://www.elastic.co/docs/reference/kibana/connectors-kibana/pre-configured-connectors).You can also manage connectors as resources with the [Elasticstack provider](https://registry.terraform.io/providers/elastic/elasticstack/latest) for Terraform. For more details, refer to the [elasticstack_kibana_action_connector](https://registry.terraform.io/providers/elastic/elasticstack/latest/docs/resources/kibana_action_connector) resource.Preconfigured connectors and the Terraform resource are not available in Elastic Cloud Serverless projects.
</tip>


## Importing and exporting connectors

To import and export connectors, use the [Saved Objects Management UI](https://www.elastic.co/docs/explore-analyze/find-and-organize/saved-objects).
If a connector is missing sensitive information after the import, a **Fix** button appears in **Connectors**.
![Connectors with missing secrets](https://www.elastic.co/docs/deploy-manage/images/kibana-connectors-with-missing-secrets.png)


## Monitoring connectors

You can query the [Event log index](https://www.elastic.co/docs/explore-analyze/alerting/alerts/event-log-index) to gather information on connector successes and failures.
If you're using Elastic Stack, then you can also use the [Task Manager health API](https://www.elastic.co/docs/deploy-manage/monitor/kibana-task-manager-health-monitoring) to monitor connector performance. However, if connectors fail to run, they will report as successful to Task Manager. The failure stats will not accurately depict connector failures.