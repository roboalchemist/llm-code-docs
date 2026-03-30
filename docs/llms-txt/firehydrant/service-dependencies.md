# Source: https://docs.firehydrant.com/docs/service-dependencies.md

# Service Dependencies

Adding service dependencies to respective services can help establish the network of relationships across your Service Catalog. Anytime an incident impacts a service, you can quickly discover dependencies to accurately understand the scope of impact from an incident. This can allow you to pull in all needed responding teams to resolve the incident quickly.

## Create a Service Dependency

Navigate to an existing Service and click the **Service Dependencies** tab. Here, you can create a **Downstream** or **Upstream** dependency for the service you are visiting by clicking "+ Add Dependency."

* **Downstream Dependencies** - These services rely on the current service being viewed.
* **Upstream Dependencies** - The current service being viewed relies on these other services.

Each dependency can be given a **Dependency Note**. This allows you to provide further context around the dependency relationship at the time of an incident for further discovery. Each dependency highlights if the service is impacted, the dependency note, service tier, and owning team.

<Image alt="Adding a Dependency" align="center" width="400px" src="https://files.readme.io/1a844b2-image.png">
  Adding a Dependency
</Image>

## Using the Graph

<Image alt="View of the Dependency Graph and table below" align="center" width="650px" src="https://files.readme.io/d1e8ede-image.png">
  View of the Dependency Graph and table below
</Image>

* **Moving around the graph** - You can drag and move the focus of the graph by clicking on empty space and moving your cursor. You can zoom in or out using the **-** or **+** buttons in the bottom right corner or pinch with two fingers on your touch pad.
* **Highlight impacted services** - You can toggle this filter in the bottom left corner of the graph to showcase all impacted services in active incidents.
* **Service Snapshot** - Double-click on any service node to open a side panel for that service. This will quickly preview that service’s analytics, owning/responding teams, and the active incidents it is involved in.
* **Add to Incident** - When exploring dependencies, you can add them to current incidents through the “Add service to incident” button. Quickly bring in the service experts to resolve issues across your infrastructure.
* **Table View** - Below our service graph is a dependency table view allowing you to sort each column quickly and update or delete dependency notes.

## Update or Delete a Service Dependency

To update or delete a service dependency, scroll down to the table. Click the ellipses next to the service dependency you'd like to edit. Here, you can either **Edit note** or **Delete dependency**. **Edit note** will allow you to change the description of the dependency relationship. **Delete dependency** will only delete the service dependency specifically from the selected service you are currently viewing.

## Service Dependencies via API

If you would like to set up **Service Dependencies** via API, visit our developer API docs under `service_dependencies` **[here](https://developers.firehydrant.com/#/operations/postV1ServiceDependencies)**.

## Next Steps

Learn more about our Service Catalog's capabilities:

* You can [automatically alert](https://docs.firehydrant.com/docs/auto-alerting-services) escalation policies and on-call schedules tied to Service Catalog components
* Ingest [Change Events](https://docs.firehydrant.com/docs/change-events) so you can more quickly identify potential contributing factors to issues and incidents