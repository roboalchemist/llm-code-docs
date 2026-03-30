# Source: https://docs.envzero.com/guides/cloud-analyst/cloud-analyst/env-zero-model.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# env zero Model

> Explore the Cloud Analyst data model including entities, relationships, and query attributes

The Cloud Analyst data model provides a structured view of the data available within our system, enabling users to run queries and extract meaningful insights. It includes detailed information about key entities, relationships, and attributes, allowing users to explore their resources, usage, costs, performance and other critical data and metrics.

Whether using our AI chatbot or building custom visualizations, users can leverage this data model to gain a deeper understanding of their cloud environment and make data-driven decisions.

## Full Entities Relational Diagram

<img src="https://mintcdn.com/envzero-b61043c8/noVHY1C-wdNQ4iZn/images/guides/cloud-analyst/cloud-analyst/5bc6f583204a74aa88930b3266ed4ea8f1fe3dd86c753def89140d4e972ce1fd-image.png?fit=max&auto=format&n=noVHY1C-wdNQ4iZn&q=85&s=2b54d60516348d47225abe4bab170f35" alt="" width="2830" height="1488" data-path="images/guides/cloud-analyst/cloud-analyst/5bc6f583204a74aa88930b3266ed4ea8f1fe3dd86c753def89140d4e972ce1fd-image.png" />

## Elaborating on the Main Entities

| Table                     | Fields                                                                                                          | Connects To                                                                              | Description                                                                       |
| :------------------------ | :-------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------- |
| **Projects**              | Name, Dates                                                                                                     | `Templates`, `Environments`, `Budgets`                                                   |                                                                                   |
| **Environments**          | Name, Dates, Template data, Status, Drift Status                                                                | `Projects`, `Deployments`, `Daily Costs`, `State Resources`, `Templates`, `Module Usage` |                                                                                   |
| **Deployments**           | Type, Drift Detected, Duration, Error, Date, Start/Finish Times, IaC version, Status                            | `Environments`, `Deployment Steps`and `Users` (which started the deployment)             |                                                                                   |
| **Deployment Steps**      | Name, Duration, Start/Compete Times, Status                                                                     | `Deployments`                                                                            |                                                                                   |
| **Templates**             | Name, Dates, Type, Project Association                                                                          | `Projects`, `Environments`                                                               |                                                                                   |
| **Users**                 | Name, Dates, Email                                                                                              | `Deployments` (they started), `Teams`                                                    |                                                                                   |
| **Teams**                 | Name, Dates                                                                                                     | `Users`                                                                                  |                                                                                   |
| **Budgets**               | Date, Time Frame, Amount                                                                                        | `Projects`                                                                               |                                                                                   |
| **Modules**               | Name, Dates                                                                                                     | `Module Downloads`, `Module Usages`                                                      |                                                                                   |
| **Module Downloads**      | Date, Version                                                                                                   | `Modules`                                                                                | How many times a module was downloaded                                            |
| **Module Usage**          | Dates, Provider, Version                                                                                        | `Modules`, `Environments`                                                                | Which Environments use which modules                                              |
| **State Resources**       | Dates, Type, Cloud Provider, Account, Region, IaC tool, Module, Provider, Deployment (last one that managed it) | `Environments` , `Cloud Resources`                                                       | All resources created by your env zero Environments                               |
| **Cloud Resources**       | Name, Dates, IaC/API/Click Operations, First Seen, Severity, Type, Service, Management Type, Cloud Provider     | `State Resources`, `Change Events`, `Cloud Resource Trends`                              | All resources found in the cloud (which may or may not be managed using env zero) |
| **Change Events**         | Event Name, Dates, User Agent, Username                                                                         | `Cloud Resources`                                                                        | All change events found in the cloud                                              |
| **Cloud Resource Trends** | Dates, IaC/API/Click Count, Type                                                                                | `Cloud Resources`                                                                        |                                                                                   |

<Info>
  **Sub Entities**

  In the env zero data model, we also store sub-entity data (sub environments and sub deployment logs of workflows).

  These sub-entities are not counted in pricing calculations, but are included when analyzing usage with Cloud Analyst.
</Info>

Built with [Mintlify](https://mintlify.com).
