# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/kubernetes-stack/kubernetes/custom-crds.md

# Custom CRDs

In addition to built-in Kubernetes API resources, it is possible to use Port's Kubernetes exporter to export and map [CRDs](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) from your Kubernetes cluster.

We created several pre-built Port K8s [exporter templates](/build-your-software-catalog/sync-data-to-catalog/kubernetes-stack/kubernetes/templates/.md), which use CRD exporting, for a quick start when using common 3rd party k8s tools.

It is also possible to write custom CRD export templates for any additional CRDs you might use in your Kubernetes clusters. To obtain all the resource types you can query in your cluster, you can run:

```
$ kubectl api-resources
```

For example, to figure out how to map your ArgoCD resources, you can run:

```
$ kubectl api-resources | grep -i argo
applications                      app,apps           argoproj.io/v1alpha1                   true         Application
applicationsets                   appset,appsets     argoproj.io/v1alpha1                   true         ApplicationSet
appprojects                       appproj,appprojs   argoproj.io/v1alpha1                   true         AppProject
```

Then, to map ArgoCD `applications`, add the matching resource kind to your exporter configuration:

```
- kind: argoproj.io/v1alpha1/applications
  identifier: .metadata.name
  blueprint: '"argoApp"'
  properties:
  ...
```
