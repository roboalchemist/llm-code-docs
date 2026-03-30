# Source: https://docs.envzero.com/guides/admin-guide/templates/k8s.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Kubernetes (K8s) Integration

> Deploy and manage Kubernetes resources with env zero using kubectl and Kustomize for labeling and drift detection

Kubernetes (also known as K8s) is an open source system for automating deployment, scaling, and management of containerized applications. Amplify the power of Kubernetes's scaled container applications with env zero's unique benefits such as Pull Request Plans and Drift Detection.

Kubernetes uses YAML or JSON files to declare the resources it manages.

## Environment Deployment

1. Create a Kubernetes [Template](/guides/admin-guide/templates)
2. Follow our guide to [Connect Your Kubernetes Cluster](/guides/getting-started/getting-started/connect-your-cloud-account/#kubernetes)
3. Create an environment. env zero will label the resources for each environment separately, so no collisions will occur when using the same template several times.

<Info>
  **Cluster Authentication**

  Cluster authentication varies from one provider to another. Please refer to the [Connect Your Kubernetes Cluster](/guides/getting-started/getting-started/connect-your-cloud-account/#kubernetes) guide to learn more.
</Info>

## Execution Steps

In addition to the common steps such as Clone, Loading Variables, etc., a Kubernetes environment in env zero has the following features:

1. K8s Label Resources -  in order to manage resources per environment env zero uses `Kustomize` for labeling relevant resources so the user won't need to change files.\
   `kustomize create --autodetect`\
   `kustomize edit remove resource metadatLabelTransformer.yaml`\
   `kustomize edit add transformer metadatLabelTransformer.yaml`

2. K8s Diff -\
   `kubectl apply -k . --prune --dry-run=server -l env0-environment-id=<environmentId>`\
   `kubectl diff -k . -l  env0-environment-id=<environmentId>`

3. K8s Apply - `kubectl apply -k . --prune -l env0-environment-id=<environmentId>`

4. K8s Delete - `kubectl delete "$(kubectl api-resources --verbs=delete -o name | tr "\n" "," | sed -e 's/,$//')" --ignore-not-found -l env0-environment-id=<environmentId>`

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/NFoAIaj_CGEzw-yg/images/guides/admin-guide/templates/77b5768-k8s_sidebar.png?fit=max&auto=format&n=NFoAIaj_CGEzw-yg&q=85&s=6bea28badb58157ea6cac01eab5b1a7b" alt="Interface screenshot showing configuration options" width="1923" height="937" data-path="images/guides/admin-guide/templates/77b5768-k8s_sidebar.png" />
</Frame>

<Info>
  **Labels description**

  The following labels are added to each resource created by env zero:

* `env0-environment-id=<environmentId>`. All resources created for a certain environment are labeled with the environment's ID.
* `app.kubernetes.io/managed-by: env0`. Regardless of the environment, every resource is labeled with the [recommended label](https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/#labels) `managed-by`
</Info>

<Warning>
  Supported versions

  The `kubectl` version is `1.23`, and the `kustomize` version is `4.5.4`.\
  It is recommended for the remote cluster not to be more than one minor version ahead or behind the client's.\
  Kubernetes's documentation goes back to version `1.20`, therefore older versions won't be supported.
</Warning>

Built with [Mintlify](https://mintlify.com).
