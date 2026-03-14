# Source: https://docs.cortexlabs.com/clusters/advanced/registry.md

# Source: https://docs.cortexlabs.com/0.41/clusters/advanced/registry.md

# Source: https://docs.cortexlabs.com/0.40/clusters/advanced/registry.md

# Source: https://docs.cortexlabs.com/0.39/clusters/advanced/registry.md

# Source: https://docs.cortexlabs.com/0.38/clusters/advanced/registry.md

# Source: https://docs.cortexlabs.com/0.37/clusters/advanced/registry.md

# Source: https://docs.cortexlabs.com/0.36/clusters/advanced/registry.md

# Source: https://docs.cortexlabs.com/0.35/clusters/advanced/registry.md

# Source: https://docs.cortexlabs.com/0.34/clusters/advanced/registry.md

# Source: https://docs.cortexlabs.com/0.33/clusters/advanced/registry.md

# Source: https://docs.cortexlabs.com/0.32/clusters/advanced/registry.md

# Source: https://docs.cortexlabs.com/0.31/clusters/registry.md

# Source: https://docs.cortexlabs.com/0.30/clusters/registry.md

# Source: https://docs.cortexlabs.com/0.29/clusters/registry.md

# Source: https://docs.cortexlabs.com/0.28/clusters/registry.md

# Private Docker registry

## Install and configure kubectl

Follow the instructions for [AWS](https://docs.cortexlabs.com/0.28/clusters/cortex-cloud-on-aws/kubectl) or [GCP](https://docs.cortexlabs.com/0.28/clusters/cortex-cloud-on-gcp/kubectl).

## Setting credentials

```bash
$ DOCKER_USERNAME=***
$ DOCKER_PASSWORD=***

$ kubectl create secret docker-registry registry-credentials \
    --namespace default \
    --docker-username=$DOCKER_USERNAME \
    --docker-password=$DOCKER_PASSWORD

$ kubectl patch serviceaccount default --namespace default \
    -p "{\"imagePullSecrets\": [{\"name\": \"registry-credentials\"}]}"
```

## Deleting credentials

```bash
$ kubectl delete secret --namespace default registry-credentials

$ kubectl patch serviceaccount default --namespace default \
    -p "{\"imagePullSecrets\": []}"
```
