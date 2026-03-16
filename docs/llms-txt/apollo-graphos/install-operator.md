# Source: https://www.apollographql.com/docs/apollo-operator/get-started/install-operator.md

# Install Apollo GraphOS Operator

In this guide, you will:

* Create an Apollo GraphOS Operator API key
* Store the API key in your cluster
* Install the operator using Helm

You will need:

* A Kubernetes cluster with permissions to install resources
* [kubectl](https://kubernetes.io/docs/reference/kubectl/) configured to access your cluster
* [Helm](https://helm.sh/) installed
* An Apollo GraphOS account (Developer, Standard, or Enterprise plan)

## 1. Create an Operator API Key

The Operator needs an Apollo GraphOS API key to publish subgraph changes and fetch supergraph schemas. It uses a special type of key that is not tied to a single user in your organization.

To create it, you will need to have the [Rover CLI](https://www.apollographql.com/docs/rover/getting-started) version 0.36.0 or newer installed and configured locally.

1. Navigate to [https://studio.apollographql.com/](https://studio.apollographql.com/) and log in.
2. Make sure you select the right Apollo organization in the top left corner.
3. Click on the **Organization** tab.
4. Take note of the **Organization ID** in that tab.
5. Run the following command in a terminal: `rover api-key create "<<Organization ID>>" operator "<<API key name>>"`
6. Copy the API key provided.

## 2. Store the API Key in your cluster

Open a terminal and run the following command to store the secret in your cluster.

```sh
APOLLO_KEY=<YOUR_APOLLO_API_KEY>
kubectl create secret generic apollo-api-key --from-literal="APOLLO_KEY=$APOLLO_KEY"
```

## 3. Create the Apollo GraphOS Operator Helm values file

In your IDE, create a new file named `values.yaml` and add the following:

```yaml title=values.yaml
apiKey:
  secretName: apollo-api-key
```

Alternatively, you can point to a file containing the API key using `apiKey.keyPath`. This is useful if you cannot use Kubernetes secrets, similar to the [`APOLLO_KEY_PATH`](https://www.apollographql.com/docs/graphos/routing/configuration/cli#--apollo-key-path) environment variable in the GraphOS Router.

```yaml title=values.yaml
apiKey:
  keyPath: /path/to/api-key.txt
```

## 4. Install the operator

Run the following command to install the Apollo GraphOS Operator in your cluster. You should run it in the same folder as the **values.yaml** file you've created previously.

```text
helm upgrade --install --atomic apollo-operator oci://registry-1.docker.io/apollograph/operator-chart -f values.yaml
```

You should now have the Apollo GraphOS Operator running in your cluster!

## Next steps

Now that you have the Operator installed, you can continue with [adding subgraphs to your cluster](https://www.apollographql.com/docs/apollo-operator/get-started/add-subgraphs).
