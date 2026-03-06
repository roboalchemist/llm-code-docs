# Source: https://docs.salad.com/container-engine/how-to-guides/platform-integrations/installation-helm-chart.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Installation Using the Helm Chart

> Integrate unlimited GPU resources from SaladCloud into your Kubernetes clusters

## Introduction

The easiest way to install a Salad VK instance into your Kubernetes cluster is by using
[the provided Helm chart](https://github.com/SaladTechnologies/virtual-kubelet-saladcloud/tree/v0.2.1/charts/virtual-kubelet-saladcloud-chart).
This will deploy the VK instance as **a single-pod deployment**, along with other necessary resources, such as **a
service account, secret** and **cluster role binding** within the designated namespace.

By using different instance names, the Helm chart allows multiple VK instances to be installed within a single
namespace, ensuring that one can be safely removed without affecting the others. Alternatively, you can create a
dedicated namespace for each VK instance to enhance resource isolation and management.

Here is an example of the deployed resources for two VK instances, **scnode1** and **scnode2**, within the
**salad-cloud** namespace:

<img src="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-nodes.png?fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=12ed7a18ed73ee2d04a9922fbb1b987c" data-og-width="452" width="452" data-og-height="146" height="146" data-path="container-engine/images/k8s-nodes.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-nodes.png?w=280&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=b8a2764723c4320a3b1e8254f81723be 280w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-nodes.png?w=560&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=150dda4708a95ed33c8f71698b5009ae 560w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-nodes.png?w=840&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=656ee90dab074b00b529e4e0def02532 840w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-nodes.png?w=1100&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=57de1619d022fa34de0db22ad1e9c497 1100w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-nodes.png?w=1650&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=b42640fcb6669a7f0a9f4550497642d9 1650w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-nodes.png?w=2500&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=e5f83587b9355c2f55da0ff1770bfbfb 2500w" />

<img src="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-install1.png?fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=8b1a03c31fb204d777b7e9ae2f8669b7" data-og-width="864" width="864" data-og-height="433" height="433" data-path="container-engine/images/k8s-install1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-install1.png?w=280&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=34c3f4f17e802f6eccb2bd9b6a50d15a 280w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-install1.png?w=560&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=6cb009e29be18ca3e36527d1bf885485 560w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-install1.png?w=840&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=6ddb296372a3ef34b955855dc705d40e 840w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-install1.png?w=1100&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=477f78eab6a97f23ac5a85c0861acdd9 1100w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-install1.png?w=1650&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=4ae2f1a5041d7a9d8c0146bf04be3305 1650w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-install1.png?w=2500&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=684038b3910c51056026687fe078e9fd 2500w" />

By default, Helm also creates a secret to store release information for each chart deployment.

The cluster role binding is a cluster-wide resource and is not associated with any specific namespace. In this example,
the two service accounts for the two VK instances are assigned the **system:node** ClusterRole.

<img src="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-install2.png?fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=9645f8589eba6c0200f38ba900398dfe" data-og-width="793" width="793" data-og-height="109" height="109" data-path="container-engine/images/k8s-install2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-install2.png?w=280&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=a21c874f44dbe576a35e75fab4a653f1 280w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-install2.png?w=560&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=6848da8e1deee59d9c9a4b3fa2b5ebf1 560w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-install2.png?w=840&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=9518faf0e7b7918388af19708bccef18 840w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-install2.png?w=1100&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=a65a82cf17b7e20df72f4c313a8e105c 1100w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-install2.png?w=1650&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=997db0364207ecc62874bd84c8ebf12b 1650w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-install2.png?w=2500&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=1bbce3bc12905c26b4c5e2de34c94c51 2500w" />

## Perform a Dry Run and Install

Before deploying the chart, you can perform a dry run and check the generated Kubernetes YAML manifests without applying
them to the cluster.

First, define the following environment variables using your SaladCloud account details, including your organization
name, project name and API key:

```
export SALAD_API_KEY=************
export SALAD_PROJECT_NAME=************
export SALAD_ORGANIZATION_NAME=************
```

If you're still using the legacy UUID-based API key, you will need to create a new style API key for the Salad VK
provider, which will start with `salad_cloud_user_`. **Additionally, make sure to create a dedicated, empty project on
SaladCloud for each VK instance.**

Then run the **helm template** command to pull the chart (0.2.3) hosted on the OCI registry at GitHub Container Registry
(GHCR) and render the chart with the above environment variables:

```
helm template scnode3-dryrun oci://ghcr.io/saladtechnologies/virtual-kubelet-saladcloud-chart --version 0.2.3 \
  --create-namespace \
  --namespace salad-cloud \
  --set salad.apiKey=$SALAD_API_KEY \
  --set salad.organizationName=$SALAD_ORGANIZATION_NAME \
  --set salad.projectName=$SALAD_PROJECT_NAME \
  --set salad.nodeName=scnode3
```

It is highly recommended to provide a unique node name (e.g., **scnode3**) for each VK instance deployment. If the node
name is not specified, a default name in the format **saladcloud-node-xxx** with a random suffix will be automatically
applied.

Now, install the chart using the **helm install** command. Helm follows the same kubeconfig precedence as kubectl, and
the cluster-admin or equivalent permissions are required to install the chart.

```
helm install scnode3 oci://ghcr.io/saladtechnologies/virtual-kubelet-saladcloud-chart --version 0.2.3 \
  --create-namespace \
  --namespace salad-cloud \
  --set salad.apiKey=$SALAD_API_KEY \
  --set salad.organizationName=$SALAD_ORGANIZATION_NAME \
  --set salad.projectName=$SALAD_PROJECT_NAME \
  --set salad.nodeName=scnode3
```

If the salad-cloud namespace exists, Helm will use it without creating a new one. If the namespace doesn't exist, Helm
will create it automatically with the --create-namespace flag.

You can also clone the Salad VK project from the GitHub repository to your local machine and customize the chart as
needed. For example, you may add resource constraints for the VK pod, such as CPU and memory limits and requests, or
assign a custom role for the service account.

<img src="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-install3.png?fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=b6e7415ec4d14806b1fe57c55fb87f49" data-og-width="871" width="871" data-og-height="382" height="382" data-path="container-engine/images/k8s-install3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-install3.png?w=280&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=bbff237096435b39511867b57f0236fc 280w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-install3.png?w=560&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=ad23b2c31477e83acbd928a31b325341 560w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-install3.png?w=840&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=1cb0d16ad867bb9f72800318b6557d2d 840w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-install3.png?w=1100&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=6f82cbdeed27d40af39177b7df4c724a 1100w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-install3.png?w=1650&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=1956ed1d866df508150888caecd2baf3 1650w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-install3.png?w=2500&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=ed4d25c55548b603a8d3d8005f940fd2 2500w" />

Then install your customized chart:

```
helm install scnode3 ./charts/virtual-kubelet-saladcloud-chart \
  --create-namespace \
  --namespace salad-cloud \
  --set salad.apiKey=$SALAD_API_KEY \
  --set salad.organizationName=$SALAD_ORGANIZATION_NAME \
  --set salad.projectName=$SALAD_PROJECT_NAME \
  --set salad.nodeName=scnode3
```

## Troubleshooting

The scnode3 node should become ready shortly after deploying the chart.

If any issues arise, you can retrieve detailed resource information, running state and check logs for troubleshooting:

<img src="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-install-scnode3.png?fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=0986dbaf5f5948b28e071db90e6d751e" data-og-width="877" width="877" data-og-height="147" height="147" data-path="container-engine/images/k8s-install-scnode3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-install-scnode3.png?w=280&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=60b5108661f6626faa04173c36084220 280w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-install-scnode3.png?w=560&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=5c645afdbc28da96b589aab0d30f4217 560w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-install-scnode3.png?w=840&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=984f1171e9481974b88db45d3e05f582 840w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-install-scnode3.png?w=1100&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=be4258514b0923ca8235d38cc27574db 1100w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-install-scnode3.png?w=1650&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=446c276e6797bedf10e4f00904714039 1650w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-install-scnode3.png?w=2500&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=d3e5c3fecad0315838fa19feb2db5d95 2500w" />

<img src="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-troubleshooting.png?fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=e6695794279fc852d2abc3ec80bbff67" data-og-width="1103" width="1103" data-og-height="391" height="391" data-path="container-engine/images/k8s-troubleshooting.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-troubleshooting.png?w=280&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=5900fa5b9806d1521c9b181ad4883eaa 280w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-troubleshooting.png?w=560&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=65fc524d0d49689ce19fa039ce5f6124 560w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-troubleshooting.png?w=840&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=68078041271b981c9e9488f9a6959cca 840w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-troubleshooting.png?w=1100&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=41b6832d6ceb4ecbcd4bdbb673f40ca7 1100w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-troubleshooting.png?w=1650&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=77ff9a2e0e97fd3a56183e74b284dba1 1650w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-troubleshooting.png?w=2500&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=2a0964db4a6bf7395bbcc7b2e5729f15 2500w" />

<img src="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-install-logs1.png?fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=5d4275d98ef53ce53246c882e7dbe388" data-og-width="918" width="918" data-og-height="165" height="165" data-path="container-engine/images/k8s-install-logs1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-install-logs1.png?w=280&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=040fecb67cb17fe8f9fc9b78d5fd0185 280w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-install-logs1.png?w=560&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=79b10021d3cebb33f6f2a44955ee6243 560w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-install-logs1.png?w=840&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=252555df9405004e60efbbbe57d187c2 840w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-install-logs1.png?w=1100&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=9e44ac849b3bda5d131c8f6812c02181 1100w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-install-logs1.png?w=1650&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=3cbdc7f606c75c4622fa3e506e900a5f 1650w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-install-logs1.png?w=2500&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=52993f2ba6ccb849607666690fc4b674 2500w" />

The warning msg in the logs is expected and can be ignored, as the Salad VK provider doesn’t run an HTTP server.

## Uninstall

Before uninstalling a VK instance, make sure that no virtual pods are running on the virtual node. Then, you can list
the installed releases in the namespace and uninstall the chart:

<img src="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-uninstall.png?fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=e4be915edf5a6852fd956d9d3e598135" data-og-width="812" width="812" data-og-height="181" height="181" data-path="container-engine/images/k8s-uninstall.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-uninstall.png?w=280&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=72a28bc428c0ddd6d6110a84114a0ca8 280w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-uninstall.png?w=560&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=e79c0e4a4d7024f57d3deb657fe3e928 560w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-uninstall.png?w=840&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=ce97f7c761e89c4577976e664f3841c9 840w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-uninstall.png?w=1100&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=ce7d351b35a8a3424030169ac34ad260 1100w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-uninstall.png?w=1650&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=4bcf94145caaa05f0df3245a67a268d6 1650w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-uninstall.png?w=2500&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=7b5962dc9ef9ae970413b21bd3b9843d 2500w" />

Now, remove the node from the Kubernetes cluster:

<img src="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-delete-node.png?fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=a9898386a9fe971bdd225be01f2e5459" data-og-width="482" width="482" data-og-height="217" height="217" data-path="container-engine/images/k8s-delete-node.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-delete-node.png?w=280&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=cd6e1ea6e24da5372deb6c91f9f4a51c 280w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-delete-node.png?w=560&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=252d7ae1f4df1a17e2f2ef2ceccc40fc 560w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-delete-node.png?w=840&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=3ed00b7e9049995efcbfc6ae433d0020 840w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-delete-node.png?w=1100&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=95aedce3007176bb0dd2d726e9031adb 1100w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-delete-node.png?w=1650&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=a56a9c87350a80f582bbe8819eacf60d 1650w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/k8s-delete-node.png?w=2500&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=2ed897fcd6335b5ff33a0ebd3cb8701e 2500w" />

## Common Commands

```
# Troubleshooting

kubectl get nodes -o wide
kubectl describe node scnode1

kubectl -n salad-cloud get all,sa,secret
kubectl -n salad-cloud get all,sa,secret | grep scnode1
kubectl get clusterrolebinding | grep salad

kubectl -n salad-cloud describe pod <VK_NODE_POD_NAME>
kubectl -n salad-cloud logs <VK_NODE_POD_NAME> -f

# Install and Uninstall

export SALAD_API_KEY=************
export SALAD_PROJECT_NAME=************
export SALAD_ORGANIZATION_NAME=************

helm -n salad-cloud list
helm -n salad-cloud status scnode1

helm template scnode3-dryrun oci://ghcr.io/saladtechnologies/virtual-kubelet-saladcloud-chart --version 0.2.3 \
  --create-namespace \
  --namespace salad-cloud \
  --set salad.apiKey=$SALAD_API_KEY \
  --set salad.organizationName=$SALAD_ORGANIZATION_NAME \
  --set salad.projectName=$SALAD_PROJECT_NAME \
  --set salad.nodeName=scnode3

helm install scnode3 oci://ghcr.io/saladtechnologies/virtual-kubelet-saladcloud-chart --version 0.2.3 \
  --create-namespace \
  --namespace salad-cloud \
  --set salad.apiKey=$SALAD_API_KEY \
  --set salad.organizationName=$SALAD_ORGANIZATION_NAME \
  --set salad.projectName=$SALAD_PROJECT_NAME \
  --set salad.nodeName=scnode3

helm -n salad-cloud uninstall scnode3

kubectl delete node scnode3
```
