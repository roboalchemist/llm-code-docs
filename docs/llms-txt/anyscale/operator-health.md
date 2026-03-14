# Source: https://docs.anyscale.com/monitoring/operator-health.md

# Health report for the Anyscale operator for Kubernetes

[View Markdown](/monitoring/operator-health.md)

# Health report for the Anyscale operator for Kubernetes

This page provides instructions for viewing health checks for the Anyscale operator for Kubernetes. Use this health report to help troubleshoot issues with your Anyscale cloud for Kubernetes.

Anyscale reports operator health for each deployment of the Anyscale operator to a Kubernetes cluster. You must use Anyscale operator version 0.7.0 or later to view health checks in the Anyscale console.

## View Anyscale operator health[​](#view-anyscale-operator-health "Direct link to View Anyscale operator health")

To view the operator health for an Anyscale cloud resource deployed to Kubernetes, complete the following steps:

1. [Log in to the Anyscale console](https://console.anyscale.com/).
2. Click your user icon.
3. Click **Clouds**.
4. Click the name of a cloud containing a Kubernetes resource.
5. Click on the name of the resource.
   <!-- -->
   * Kubernetes resources display **K8s** under the **Stack** field.

The operator health report displays under the **Operator health** tab.

## Operator health report[​](#operator-health-report "Direct link to Operator health report")

The operator health report provides the following information:

important

The Anyscale operator runs health checks every five minutes. Anyscale polls the operator for new results every minute.

The Anyscale console reports the timestamp it last successfully polled for results. Status updates related to changed configurations might take five minutes or more to display in the Anyscale console.

| Field   | Description                                                                                                                                                       |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checks  | The name of the check run. See [What operator health checks does Anyscale run?](#checks).                                                                         |
| Outcome | The state reported by the check. One of the following:- **Success**<br />- **Error**<br />- **Warning**: Warns if Kubernetes version is outside the tested range. |
| Message | Displays the error message if the check results in an error.                                                                                                      |
| Logs    | View the logs for the check in JSON format.                                                                                                                       |

## What operator health checks does Anyscale run?[​](#checks "Direct link to What operator health checks does Anyscale run?")

The following table provides an overview of the health checks reported by the Anyscale operator:

| Check name               | Description                                                                                                            |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| `cloud_resources`        | The operator has permission to access the default cloud object storage configured for the resource.                    |
| `gateway_resources`      | If the configuration has a gateway enabled, checks that the related CRDs are present on the Kubernetes cluster.        |
| `iam_identity`           | The IAM identity of the operator matches the configuration for the Anyscale cloud.                                     |
| `kubernetes_permissions` | The operator has necessary Kubernetes RBAC permissions.                                                                |
| `kubernetes_version`     | The Kubernetes cluster uses a Kubernetes version tested for support for the deployed version of the Anyscale operator. |
