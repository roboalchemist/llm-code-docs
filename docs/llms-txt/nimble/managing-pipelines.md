# Source: https://docs.nimbleway.io/management-tools/nimble-dashboard/managing-pipelines.md

# Managing Pipelines

{% embed url="<https://www.loom.com/share/746ce231588c4bd8a9ebcd1ba0b24086?sid=4c1c35dc-b5d3-46ab-b61d-1f9b13705b33>" %}

### What are Pipelines?

A pipeline groups and directs requests through Nimble IP to a relevant proxy peer. Every request to Nimble IP flows through a pipeline, and every account comes with a default pipeline.&#x20;

Users can create multiple pipelines, depending on the size of their account. Pipelines serve two main functions:

* **Marking a business use case** - reports and statistics can be filtered to a particular pipeline, making it easy to view how the total data transfer, requests, spending, and success rate for a particular use case. Some examples include:
  * A business that collects E-commerce data may choose to make a dedicated pipeline for each data source, such as Amazon, Walmart, Home Depot, etc.
  * An organization that gathers SERP data may choose to create a pipeline for different goals, such as competitor monitoring, search term tracking, paid and SEM monitoring, etc.
  * A team that performs brand protection can create a pipeline for each client/brand they manage.
* **Setting defaults** - Pipelines contain default settings that are inherited by the requests they oversee, and become especially useful when using Authenticated IPs, where parameters cannot be set manually in the request body and must be configured within the pipeline. Some of the parameters that can be set on the pipeline level include:
  * IP rotation (rotating/fixed interval)
  * Country, State, and City geotargeting
  * Optimization engine profile&#x20;

### How do I create/delete/configure a pipeline?

In the Dashboard, click on the "Pipelines" page in the left navigation menu.

* To create a new pipeline, click "+Add Pipeline" on the right-hand button.
* Pipelines can be disabled and/or archived by clicking the three-dot menu handle in the relevant pipeline's row, and then "Disable Pipeline" or "Archive Pipeline".
* To modify a pipeline, click anywhere on the pipeline row to enter the pipeline details page. Then click on the "Settings" tab to view and edit the pipeline settings.
