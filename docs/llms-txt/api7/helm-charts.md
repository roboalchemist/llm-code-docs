# Source: https://docs.api7.ai/ingress-controller/reference/helm-charts.md

# Helm Charts

APISIX and API7 Ingress Controllers can be deployed using Helm charts. There are separate charts for these controllers, with different configuration options and deployment approaches.

## APISIX Helm Chart[â](#apisix-helm-chart "Direct link to APISIX Helm Chart")

[APISIX Helm Chart](https://github.com/apache/apisix-helm-chart) provides Helm-based installation and management of APISIX components on Kubernetes.

APISIX Ingress Controller can be deployed on Kubernetes in two ways:

* Embedded with the `apisix/apisix` chart, where the controller is enabled as part of the APISIX release by setting `ingress-controller.enabled=true`.
* As a separate Helm release using the `apisix/apisix-ingress-controller` chart.

The installation command in the [Getting Started tutorial](https://docs.api7.ai/ingress-controller/set-up-ingress-controller-and-gateway.md#install-apisix-and-apisix-ingress-controller) deploys APISIX Ingress Controller together with APISIX in a single Helm release. In this setup, the ingress controller pod runs alongside the APISIX gateway pod, but only one Helm release (`apisix`) appears in `helm ls`.

Alternatively, you can deploy the APISIX Ingress Controller independently from APISIX as a separate Helm release. The following example command shows how to install the APISIX Ingress Controller as a separate release:

```
# replace with your configuration details
helm install apisix-ingress-controller \
  --create-namespace \
  -n aic \
  --set gatewayProxy.createDefault=true \
  --set gatewayProxy.provider.controlPlane.auth.adminKey.value=edd1c9f034335f136f87ad84b625c8f1 \
  --set apisix.adminService.namespace=aic \
  --set apisix.adminService.name=apisix-admin \
  --set apisix.adminService.port=9180 \
  apisix/apisix-ingress-controller
```

## API7 Helm Chart[â](#api7-helm-chart "Direct link to API7 Helm Chart")

[API7 Helm Chart](https://github.com/api7/api7-helm-chart) provides a Helm-based method for installing and managing API7 components on Kubernetes.

API7 Ingress Controller has its own dedicated Helm chart, designed to deploy only the ingress controller component, which connects to an existing API7 control plane. Unlike the APISIX Helm chart, the API7 Gateway chart does not include an option to deploy the ingress controller as part of the same release.

For installation, API7 Dashboard guides you through deploying both the Ingress Controller and the Gateway on Kubernetes, generating the necessary deployment scripts and commands along the way.

## Helm Chart Values[â](#helm-chart-values "Direct link to Helm Chart Values")

Helm chart values define the configuration of a chart. They can come from the chart's default `values.yaml` file or be overridden during installation or upgrade to customize the deployment.

### View Default Values[â](#view-default-values "Direct link to View Default Values")

To view the default values provided by a Helm chart, run:

```
helm show values <repo>/<chart-name>

# For example:
# helm show values apisix/apisix
# helm show values apisix/apisix-ingress-controller
# helm show values api7/api7-ingress-controller
```

Note that the output shows only the chartâs default values. It does not include any values overridden during `helm install` or `helm upgrade`, nor does it reflect the effective values currently running in the cluster.

For additional explanations of the chart parameters, refer to the following documentation:

* [APISIX Ingress Controller Helm chart values](https://github.com/apache/apisix-helm-chart/blob/master/charts/apisix-ingress-controller/README.md#values)
* [API7 Ingress Controller Helm chart values](https://github.com/api7/api7-helm-chart/blob/main/charts/ingress-controller/README.md#values)

### View Effective Values[â](#view-effective-values "Direct link to View Effective Values")

To view the values applied to an installed release (including both defaults and overrides), run:

```
helm get values <release-name> -n <namespace> --all
```

### Update Values[â](#update-values "Direct link to Update Values")

To update a Helm release, you can edit its effective values and apply the changes.

First, export the full set of values for the release to a file, including both chart defaults and any overrides:

```
helm get values <release-name> -n <namespace> --all -o yaml > my-values.yaml
```

Next, open the exported values file and update the parameter values.

Finally, apply the updated values to your release:

```
helm upgrade <release-name> <chart-name> -n <namespace> -f my-values.yaml
```
