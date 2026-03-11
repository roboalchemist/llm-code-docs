# Source: https://archivedocs.stackstate.com/5.1/develop/developer-guides/custom-functions/component-actions.md

# Component actions

## Overview

This how-to describes the steps to create a [component action](https://archivedocs.stackstate.com/5.1/configure/topology/component_actions) that's available for specific components. Component actions can be executed from the component context menu in the StackState UI Topology Perspective or the right panel details tab when detailed information about a component has been selected - **Component details**.

## Add or edit a component action

The component actions available in StackState can be managed in the StackState UI from the page **Settings** > **Actions** > **Component Actions**.

* To add a new component action, click the **ADD COMPONENT ACTION** button.
* To edit an existing component action, click the **...** menu to the right of its description and select **Edit**.

![Component Actions](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-29f660ad12f630b18e4cbb7bb18797d917321345%2Fcomponent_actions.png?alt=media)

Each component action includes the following details:

* **Name** - The name displayed to users in the StackState UI when the component action is available for a component. The component action name is case-sensitive.
* **Description** - The text shown in the tooltip when a user hovers over the component action name in the StackState UI.
* **STQL Query** - An advanced topology query that returns all components for which this component action should be available. For details, see the [STQL Query](#stql-query) section below.
* **Script** - A script written in StackState Scripting Language that's run whenever the component action is executed in the StackState UI. For details, see the [script](#script) section and the [example scripts](#example-scripts) below.
* **Identifier** - Optional. A unique identifier for the component action. For details, see the [identifier](#identifier) section below.

### STQL query

The STQL query specified in a component action determines which components of the topology will be able to use this component action. This should be an advanced topology query that returns all of the components that should have access to this specific component action. For example, to bind a component action to all components in the "Production" domain that are present in the "databases" layer, you would use the STQL query:

```
(domain IN ("Production") AND layer IN ("databases"))
```

You can find more information about writing advanced topology queries in StackState on the page [using STQL](https://archivedocs.stackstate.com/5.1/develop/reference/stql_reference).

### Script

The script determines behavior of the component action when it's executed by a user. YOu can use the [StackState Scripting Language](https://archivedocs.stackstate.com/5.1/develop/reference/scripting/scripting-in-stackstate) to script almost any action you need, such as redirecting a user to another view with a specific context, restarting remote components, or calling predictions for components. Some [example scripts](#example-scripts) are available below to help you get started.

Component action scripts always have access to a `component` variable, this represents the component for which the component action was invoked.

The properties in the table below can be accessed directly in the component action script:

| Property                                | Type             | Returns                                                                                             |
| --------------------------------------- | ---------------- | --------------------------------------------------------------------------------------------------- |
| `component.id`                          | Long             | The StackGraph ID of the component.                                                                 |
| `component.lastUpdateTimestamp`         | Long             | The timestamp when the component was last updated.                                                  |
| `component.name`                        | String           | The name of the component.                                                                          |
| `component.description`                 | Option\[String]  | The description of the component.                                                                   |
| `component.labels`                      | Set\[Label]      | Set of labels, each containing a `name` property.                                                   |
| `component.state.healthState`           | HealthStateValue | The health state of the component. Can be `UNKNOWN`, `CLEAR`, `DEVIATING` or `CRITICAL`.            |
| `component.state.propagatedHealthState` | HealthStateValue | The propagated health state of the component. Can be `UNKNOWN`, `CLEAR`, `DEVIATING` or `CRITICAL`. |
| `component.layer`                       | Long             | The StackGraph ID of the layer that the component is in.                                            |
| `component.domain`                      | Long             | The StackGraph ID of the domain that the component is in.                                           |
| `component.environments`                | Set\[Long]       | The StackGraph IDs of all environments that the component is in.                                    |

Other properties of the component can be accessed using the [component script API](https://archivedocs.stackstate.com/5.1/develop/reference/scripting/script-apis/component).

Other variables accessible from the script are the following:

* `topologyTime: Instant` - is a [topology time](https://archivedocs.stackstate.com/5.1/use/stackstate-ui/timeline-time-travel#topology-time) of the timeline. For [live mode](https://archivedocs.stackstate.com/5.1/use/stackstate-ui/timeline-time-travel#live-mode) the variable value is `null`.
* `telemetryTimeStart: Instant` - is a [telemetry interval](https://archivedocs.stackstate.com/5.1/use/stackstate-ui/timeline-time-travel#telemetry-interval) start. This variable always have a value.
* `telemetryTimeEnd: Instant` - is a telemetry interval end. For live mode the variable value is `null`.

For more details for time usage in scripts see [script API documentation](https://archivedocs.stackstate.com/5.1/develop/reference/scripting/script-apis/time).

### Identifier

Providing an identifier is optional, but is necessary when you want to store your component action in a StackPack. A valid [identifier](https://archivedocs.stackstate.com/5.1/configure/topology/identifiers) for a component action is a URN that follows the convention:

```
urn:stackpack:{stackpack-name}:component-action:{component-action-name}
```

## Example scripts

### Show a topology query

The component action script below will direct the StackState UI to open a new topology query:

```
def componentId = component.id.longValue()
UI.showTopologyByQuery("withNeighborsOf(direction = 'both', components = (id = '${componentId}'), levels = '15') and label = 'stackpack:openshift'")
```

### Navigate the user to an external URL

The component action script below will direct the StackState UI to navigate to a specific URL:

```
def region = (component.labels.find {it -> it.name.startsWith("region") }).name.split(':')[1]
def url = "https://${region}.console.aws.amazon.com/ec2/home?region=${region}#Instances:sort=instanceId"

UI.redirectToURL(url)
```

### Navigate the user to an external URL using time context

The component action script below will direct the StackState UI to navigate to an external monitoring system at point of time:

```
def asEpoch(time) {
  time != null ? Time.epochMs(time) : null
}

def dashboardURL = "https://grafana.my-organization.com/dashboard"
def params = [
    ["from", asEpoch(telemetryTimeStart)],
    ["to", asEpoch(telemetryTimeEnd)]
]
def queryParams = params.findAll { it -> it[1] != null }.collect { it -> it.join("=")}.join("&")

UI.redirectToURL("${dashboardURL}?${queryParams}")
```

### Make HTTP requests

The component action script below will invoke an HTTP request to a remote URL. This call is made from the StackState server:

```
Http.post("https://postman-echo.com/post")
    .timeout("30s")
.jsonResponse()
```

## See also

* [StackState Query Language (STQL)](https://archivedocs.stackstate.com/5.1/develop/reference/stql_reference)
* [Scripting in StackState](https://archivedocs.stackstate.com/5.1/develop/reference/scripting/scripting-in-stackstate)
* [Component script API](https://archivedocs.stackstate.com/5.1/develop/reference/scripting/script-apis/component)
