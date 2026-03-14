# Source: https://docs.airbyte.com/platform/deploying-airbyte/creating-secrets.md

# Source: https://docs.airbyte.com/platform/2.0/deploying-airbyte/creating-secrets.md

# Source: https://docs.airbyte.com/platform/1.8/deploying-airbyte/creating-secrets.md

# Source: https://docs.airbyte.com/platform/1.7/deploying-airbyte/creating-secrets.md

# Source: https://docs.airbyte.com/platform/1.6/deploying-airbyte/creating-secrets.md

# Preconfiguring Kubernetes Secrets

Copy Page

Deploying Airbyte requires specifying a number of sensitive values. These can be API keys, usernames and passwords, etc. In order to protect these sensitive values, the Helm Chart assumes that these values are pre-configured and stored in a Kubernetes Secret *before* the Helm installation begins. Each [integration](#integrations) will provide the Secret values that are required for the specific integration.

While you can set the name of the secret to whatever you prefer, you will need to set that name in various places in your values.yaml file. For this reason we suggest that you keep the name of `airbyte-config-secrets` unless you have a reason to change it.

* Creating Secrets with YAML
* Creating secrets with kubectl

You can apply your yaml to the cluster with `kubectl apply -f secrets.yaml -n airbyte` to create the secrets.

```
apiVersion: v1
kind: Secret
metadata:
  name: airbyte-config-secrets
type: Opaque
stringData:
  # Examples
  key-1: "value-1"
  key-2: "value-2"
```

You can also use `kubectl` to create the secret directly from the CLI:

```
kubectl create secret generic airbyte-config-secrets \
  --from-literal=key-1='value-1' \
  --from-literal=key2='value-2' \
  --namespace airbyte
```
