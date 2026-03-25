# Source: https://docs.statsig.com/metrics/console.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Metrics Dashboard

> Explore your metrics and events through the Statsig console with real-time visualization and organization tools.

Metrics are available for all unit types enabled in the project.  User ID and Stable ID are provided by default and others can be added following [these steps](/guides/experiment-on-custom-id-types#step-1---add-companyid-as-a-new-id-type-in-your-project-settings).  Make a selection from the drop down to view event DAU and user accounting metrics calculated based on the desired unit type.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/xH6BS9VFb4phB4uA/images/metrics/console/172450890-4a4c95eb-a362-49a6-90ad-68f3460a933f.png?fit=max&auto=format&n=xH6BS9VFb4phB4uA&q=85&s=6cfa46b5d7fc8c346a40cd70f5a8086d" alt="Metrics unit type selection" width="1904" height="916" data-path="images/metrics/console/172450890-4a4c95eb-a362-49a6-90ad-68f3460a933f.png" />
</Frame>

## Events

The Metrics console allows you to visualize all the events that you have logged in Statsig. The **Events** tab shows all the events, including a real-time stream of events as they come in.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/xH6BS9VFb4phB4uA/images/metrics/console/172451019-fc450842-a546-4ea0-94a9-d54df8279ed2.png?fit=max&auto=format&n=xH6BS9VFb4phB4uA&q=85&s=630067cb8eb567574c4b52973e79a8ef" alt="Events tab view" width="1845" height="1199" data-path="images/metrics/console/172451019-fc450842-a546-4ea0-94a9-d54df8279ed2.png" />
</Frame>

You can toggle between a list view or chart view of your events to view the trend line over time.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/xH6BS9VFb4phB4uA/images/metrics/console/172461387-a3d42641-2c2c-4128-aabc-fc2b5dba2ed9.png?fit=max&auto=format&n=xH6BS9VFb4phB4uA&q=85&s=77d7810ba634f9fa7b6bf73a78e8166d" alt="Events chart view" width="1865" height="925" data-path="images/metrics/console/172461387-a3d42641-2c2c-4128-aabc-fc2b5dba2ed9.png" />
</Frame>

From here you can drill into each event and see a detailed view of the logs, broken down by each unique value that was logged.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/xH6BS9VFb4phB4uA/images/metrics/console/172462231-ff2f3063-0c4e-49fd-af17-7147bd09d3d1.png?fit=max&auto=format&n=xH6BS9VFb4phB4uA&q=85&s=b67c67efa4b168333733094e03bcc7b9" alt="Event detailed view" width="1019" height="1180" data-path="images/metrics/console/172462231-ff2f3063-0c4e-49fd-af17-7147bd09d3d1.png" />
</Frame>

## Metrics Catalog

The **Metrics Catalog** tab allows you to search and tag your metrics, as well as [create custom metrics](/metrics/create). Tags enable you organize your metrics and create collections of metrics that are associated in some way. For example, you could tag a set of metrics focused on a product area, business function, business objective, and so on. You can also create a loose collection of guardrail metrics that teams check in every experiment to ensure there are causing no unexpected effects in other parts of the business. Once you create a tagged collection of metrics, you can easily pull up this set of metrics when viewing your experiment results and zoom into the context that you want to focus on.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/xH6BS9VFb4phB4uA/images/metrics/console/172462680-68a6de4e-17bf-4b11-920d-6d7830551012.png?fit=max&auto=format&n=xH6BS9VFb4phB4uA&q=85&s=57c7cfbbe125bd047afb5a598124320d" alt="Metrics catalog" width="1846" height="1135" data-path="images/metrics/console/172462680-68a6de4e-17bf-4b11-920d-6d7830551012.png" />
</Frame>

Similar to the **Events** tab, you can toggle between a list view or chart view of your metrics to view the trend line over time.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/xH6BS9VFb4phB4uA/images/metrics/console/172462947-877bbcc7-46b3-45cd-ac57-d0dc2c949d7d.png?fit=max&auto=format&n=xH6BS9VFb4phB4uA&q=85&s=cbcb1d9184b304b185bad1e1175d4b7c" alt="Metrics chart view" width="1851" height="1162" data-path="images/metrics/console/172462947-877bbcc7-46b3-45cd-ac57-d0dc2c949d7d.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).