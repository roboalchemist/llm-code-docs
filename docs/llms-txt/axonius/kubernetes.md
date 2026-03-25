# Source: https://docs.axonius.com/docs/kubernetes.md

# Kubernetes

Kubernetes (K8s) is an open-source system for automating deployment, scaling, and management of containerized applications.

## Asset Types Fetched

* Devices, Containers, Compute Images

## Before You Begin

### APIs

Axonius uses the [Kubernetes API Server](https://kubernetes.io/docs/concepts/overview/components/#kube-apiserver).

### Required Ports

* the default port is **6443**

### Required Permissions

The value supplied for the **Token** parameter:

* Must have read authorization to Pods and Nodes.
* Must be associated to a service account that has read authorizations in the APIServer. If you use RBAC (Role Based Access Control) please refer to the official docs at [https://kubernetes.io/docs/reference/access-authn-authz/rbac/](https://kubernetes.io/docs/reference/access-authn-authz/rbac/).
  * To perform an authorization test you can run the following command (in your K8s cluster):
  * If the command outputs **no**, it means the user doesn't have the necessary permissions.

```
kubectl auth can-i get pods --all-namespaces --as 
```

#### Troubleshooting

* Make sure the cluster has ApiServer component enabled
* To perform an authentication test you can run the following command (in your K8s cluster):

```
curl :/api/v1/pods -H "Authorization: Bearer "
```

* Explore the API with token: [https://kubernetes.io/docs/tasks/administer-cluster/access-cluster-api/](https://kubernetes.io/docs/tasks/administer-cluster/access-cluster-api/)

## Deploying the Adapter in Axonius

Click **Add Connection** and provide the following parameters:

1. **Host Name or IP Address** - The hostname or IP address of the Kubernetes API Server endpoint that Axonius can communicate with via the [Required Ports](#required-ports). In order to locate the IP Address of an API Server run the following command (in your K8s cluster):

```

kubectl config view | grep server 
```

2. **Port** *(default: 6443)* - The port used in the connection.
3. **Token** A bearer token associated with a service account that has the [Required Permissions](#required-permissions) to fetch assets. For more information, see [Accessing Clusters](https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster/).
   * To retrieve the token, first run the following command in your K8s cluster to get the list of secrets:
   ```
   kubectl get secrets
   ```
   * Then, run this command on the relevant secret name and copy from the output the content of the **token** field.
   ```
   kubectl describe secret 
   ```
4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

<Image border={false} src="https://files.readme.io/43c54e97ead7fcaff6a5d20e4436bad080976b272e94ef1fbd92ef155eddd452-image.png" />

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Enrich containers with Ingress Rules** - Select to enrich Container assets with Ingress rules.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>