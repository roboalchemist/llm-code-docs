# Source: https://ngrok.com/docs/k8s/guides/managed-resources.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# ngrok Kubernetes Operator Managed Resources

> Learn about the resources that the ngrok Kubernetes Operator manages.

The ngrok Kubernetes Operator has many different custom resource definitions that are installed along with it.
Many of these are resources that you can create on your own, others are primarily created and managed by the Operator.

## Managed labels

The ngrok Operator uses the following labels to mark which resources it created and manages versus resources that you create and manage manually.
The values are determined by your installation name and namespace.

```yaml  theme={null}
k8s.ngrok.com/controller-name: ngrok-operator-manager
k8s.ngrok.com/controller-namespace: ngrok-operator
```

Any resource with these labels will have its lifecycle controlled by the ngrok Operator. They should never be used on resources you create and manage yourself.
When the Operator translates `Ingress` and Gateway API configuration resources into `AgentEndpoint` and `CloudEndpoint` resources for you, it marks those as managed resources using the above labels.
Adding these labels to resources you create and manage yourself can cause the Operator to delete them since it thinks that the resource was created from an `Ingress`/etc. that no longer exists.

You can use these labels to your advantage to list the resources that the Operator manages. For example, to get all `AgentEndpoint` resources that are created and managed by the Operator:

```bash  theme={null}
kubectl get aep --all-namespaces -l k8s.ngrok.com/controller-name=ngrok-operator-manager,k8s.ngrok.com/controller-namespace=ngrok-operator
```


Built with [Mintlify](https://mintlify.com).