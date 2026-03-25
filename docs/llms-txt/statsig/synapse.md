# Source: https://docs.statsig.com/data-warehouse-ingestion/synapse.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Synapse

## Overview

To set up connection with Azure Synapse, Statsig needs the following

* Workspace SQL Endpoint
* Database Name
* Admin User Name
* Admin User Password

<b>
  Admin user name and password will be used by Statsig to create a user with restricted access to query from your data warehouse.
</b>

You can find this information in your Azure console within your Synapse workspace overview page, as shown in the image below. (Open image in new tab for a bigger image)

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/KzTmSDyskL8DnHsb/images/data-warehouse-ingestion/synapse/198148122-6488a470-5394-46ee-aeb1-ef2425fa743e.png?fit=max&auto=format&n=KzTmSDyskL8DnHsb&q=85&s=8c62f39e45568732f0e10c34671931b7" alt="Azure Synapse workspace overview page" width="2264" height="1044" data-path="images/data-warehouse-ingestion/synapse/198148122-6488a470-5394-46ee-aeb1-ef2425fa743e.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).