# Source: https://docs.cortexlabs.com/clusters/advanced/kubectl.md

# Source: https://docs.cortexlabs.com/0.41/clusters/advanced/kubectl.md

# Source: https://docs.cortexlabs.com/0.40/clusters/advanced/kubectl.md

# Source: https://docs.cortexlabs.com/0.39/clusters/advanced/kubectl.md

# Source: https://docs.cortexlabs.com/0.38/clusters/advanced/kubectl.md

# Source: https://docs.cortexlabs.com/0.37/clusters/advanced/kubectl.md

# Source: https://docs.cortexlabs.com/0.36/clusters/advanced/kubectl.md

# Source: https://docs.cortexlabs.com/0.35/clusters/advanced/kubectl.md

# Source: https://docs.cortexlabs.com/0.34/clusters/advanced/kubectl.md

# Source: https://docs.cortexlabs.com/0.33/clusters/advanced/kubectl.md

# Source: https://docs.cortexlabs.com/0.32/clusters/advanced/kubectl.md

# Source: https://docs.cortexlabs.com/0.31/clusters/gcp/kubectl.md

# Source: https://docs.cortexlabs.com/0.31/clusters/aws/kubectl.md

# Source: https://docs.cortexlabs.com/0.30/clusters/gcp/kubectl.md

# Source: https://docs.cortexlabs.com/0.30/clusters/aws/kubectl.md

# Source: https://docs.cortexlabs.com/0.29/clusters/cortex-cloud-on-gcp/kubectl.md

# Source: https://docs.cortexlabs.com/0.29/clusters/cortex-cloud-on-aws/kubectl.md

# Source: https://docs.cortexlabs.com/0.28/clusters/cortex-cloud-on-gcp/kubectl.md

# Source: https://docs.cortexlabs.com/0.28/clusters/cortex-cloud-on-aws/kubectl.md

# Setting up kubectl

## Install kubectl

Follow these [instructions](https://kubernetes.io/docs/tasks/tools/install-kubectl).

## Install the AWS CLI

Follow these [instructions](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html).

## Configure the AWS CLI

```bash
aws --version  # should be >= 1.16

aws configure
```

## Update kubeconfig

```bash
aws eks update-kubeconfig --name=<cluster_name> --region=<region>
```

## Test kubectl

```bash
kubectl get pods
```
