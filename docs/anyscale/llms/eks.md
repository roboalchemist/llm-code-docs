# Source: https://docs.anyscale.com/iam/eks.md

# Configure IAM roles for clusters on Anyscale on EKS

[View Markdown](/iam/eks.md)

# Configure IAM roles for clusters on Anyscale on EKS

This page describes how to use and manage IAM roles for Anyscale clouds deployed on Amazon Elastic Kubernetes Service (EKS).

## What is the IAM model for Anyscale on EKS?[​](#iam-model "Direct link to What is the IAM model for Anyscale on EKS?")

The Anyscale control plane interacts with EKS service accounts through the Anyscale operator. You manage all identity and access management (IAM) for Anyscale workloads on EKS through Kubernetes service accounts that map to AWS IAM roles.

EKS supports integration with AWS IAM using the following methods:

* [EKS Pod Identity](https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html)
* [IAM roles for service accounts (IRSA)](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html)

For the best performance, Anyscale recommends the following:

* Configure your EKS cluster to use IRSA with an OIDC identity provider.
* Create IAM roles with appropriate trust policies to allow assumption by Kubernetes service accounts.
* Map a single IAM role to each Kubernetes service account in your EKS cluster used by Anyscale.

important

You provide an AWS IAM role name to Anyscale when registering a new cloud resource backed by EKS. The Anyscale operator uses this identity to sign messages, and the Anyscale control plane validates that the signature matches the registered role. The Anyscale control plane never assumes this identity.

## EKS service accounts and IAM roles used by Anyscale[​](#service-accounts "Direct link to EKS service accounts and IAM roles used by Anyscale")

You annotate EKS service accounts to add a trust relationship with an IAM role. This annotation provides Ray nodes in your Anyscale cluster access to resources in your AWS account, such as the default S3 bucket configured during your cloud deployment.

The following table describes the IAM roles you need to configure for Anyscale:

| Term                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Anyscale operator IAM role | When you deploy an Anyscale cloud on EKS, you configure a Kubernetes service account for the Anyscale operator that maps to an IAM role in your AWS account.The permissions in this IAM role govern all actions that the Anyscale operator can take in your EKS cluster. The Anyscale operator is responsible for processing all instructions from the Anyscale control plane to deploy nodes for Ray clusters in your EKS cluster.                                                                                                                |
| Cluster IAM role           | When you configure the Anyscale operator for your Anyscale cloud on EKS, you configure a default Kubernetes service account that maps to an IAM role. When the Anyscale operator deploys a new cluster or autoscales to add worker nodes, the Pods use this service account and assume the IAM role to gain access to necessary resources in your AWS account.You must define a Kubernetes service account and IAM role for each unique set of IAM permissions you want to assign to a given user, workload, or project through cloud IAM mapping. |

## View cluster service account and IAM role[​](#view "Direct link to View cluster service account and IAM role")

Run the following commands to find the Kubernetes service account in use for Pods in your Anyscale cluster:

```
# Define your EKS namespace.
NAMESPACE="<your-anyscale-namespace>"

# Get all Pods and manually identify your Pod.
kubectl get pods -n ${NAMESPACE} | grep k-

# Define a variable for your Pod name.
POD_NAME="<your-pod-name>"

# Get the Kubernetes service account name used by your Pod.
kubectl get pod ${POD_NAME} -n ${NAMESPACE} -o jsonpath='{.spec.serviceAccountName}'
```

To see the AWS IAM role used by your Kubernetes service account, run the following command:

```
kubectl get serviceaccount "<your-kubernetes-service-account>" -n "${NAMESPACE}" \
  -o jsonpath='{.metadata.annotations.eks\.amazonaws\.com/role-arn}{"\n"}'
```

## Create and map an EKS cluster IAM role[​](#create-role "Direct link to Create and map an EKS cluster IAM role")

To create a new cluster IAM role, you annotate a Kubernetes service account with an AWS IAM role. You add policies to the IAM role to grant access to additional resources in your AWS account, such as S3 buckets.

note

Use cloud IAM mapping to control how Anyscale assigns cluster IAM roles based on user identity, workload type, or project.

You must create and annotate a Kubernetes service account for each unique IAM role you need to assign to Anyscale clusters. See [Anyscale cloud IAM mapping](/iam/cloud-iam-mapping.md).

Complete the following steps to annotate an EKS service account.

### Requirements[​](#requirements "Direct link to Requirements")

The following instructions assume the following:

* You have created an EKS cluster and registered it as an Anyscale cloud resource.
* You have installed and authenticated the AWS CLI.
* You have installed and configured `kubectl` for your EKS cluster.
* You have enabled the OIDC identity provider on your EKS cluster. See [Create an IAM OIDC provider for your cluster](https://docs.aws.amazon.com/eks/latest/userguide/enable-iam-roles-for-service-accounts.html).

### Step 0: Identify or create an IAM role[​](#step-0 "Direct link to Step 0: Identify or create an IAM role")

Identify or create the IAM role you need to attach to your EKS cluster.

For Anyscale to operate correctly, your IAM role must have permissions to interact with the S3 bucket configured as default storage for your Anyscale cloud resource. See [Minimum privileges for Anyscale cluster IAM roles](/iam/aws.md#minimum).

important

You use the ARN for the IAM role to configure the trust relationship with EKS.

You define your IAM role name as a variable in the next step and use the AWS CLI to construct the ARN.

### Step 1: Configure variables[​](#step-1 "Direct link to Step 1: Configure variables")

The following commands configure variables that describe your AWS account, EKS cluster, and Anyscale account. Replace the variables denoted with `<>` before running these commands. For example, replace `<your-eks-cluster-name>` with the name of your EKS cluster.

note

You can save and run these commands as a `.sh` script, or run each command sequentially from the command line.

```
#!/bin/bash

# Specify the namespace for Anyscale in your EKS cluster.
# Anyscale uses 'anyscale-operator' as the default EKS namespace.
export NAMESPACE="<your-anyscale-namespace>"

# Specify the AWS region and name of your EKS cluster.
export AWS_REGION="<your-aws-region>"
export EKS_CLUSTER_NAME="<your-eks-cluster-name>"

# Capture the AWS account ID as a variable.
export AWS_ACCOUNT_ID="$(aws sts get-caller-identity --query Account --output text)"

# Define the name for a new service account.
export SERVICE_ACCOUNT_NAME="<your-service-account-name>"

# Specify the name of IAM role to use with the service account.
export IAM_ROLE_NAME="<your-iam-role-name>"

# Define the ARN for the IAM role.
export AWS_ROLE_ARN="arn:aws:iam::${AWS_ACCOUNT_ID}:role/${IAM_ROLE_NAME}"
```

### Step 2: Show current service accounts[​](#step-2 "Direct link to Step 2: Show current service accounts")

Run the following commands to connect to your EKS cluster and list all service accounts present in your namespace:

```
aws eks update-kubeconfig --region "${AWS_REGION}" --name "${EKS_CLUSTER_NAME}"
kubectl get serviceaccounts -n ${NAMESPACE}
```

note

You can review service accounts currently registered for Anyscale cloud IAM mapping in the Anyscale console or using the CLI. See [Anyscale cloud IAM mapping](/iam/cloud-iam-mapping.md).

### Step 3: Create a Kubernetes service account[​](#step-3 "Direct link to Step 3: Create a Kubernetes service account")

Run the following command to create a Kubernetes service account in the namespace of your EKS cluster:

```
kubectl create serviceaccount "${SERVICE_ACCOUNT_NAME}" -n "${NAMESPACE}" \
  --dry-run=client -o yaml | kubectl apply -f -
```

### Step 4: Annotate the Kubernetes service account[​](#step-4 "Direct link to Step 4: Annotate the Kubernetes service account")

Run the following command to annotate the EKS service account with the IAM role ARN:

```
kubectl annotate serviceaccount "${SERVICE_ACCOUNT_NAME}" -n "${NAMESPACE}" \
  eks.amazonaws.com/role-arn="${AWS_ROLE_ARN}" --overwrite
```

### Step 5: Configure the IAM role trust policy[​](#step-5 "Direct link to Step 5: Configure the IAM role trust policy")

Create a trust policy that allows the Kubernetes service account to assume the IAM role. This step establishes the trust relationship between your EKS cluster's OIDC provider and the IAM role.

Start by getting the OIDC issuer URL for your EKS cluster:

```
export OIDC_PROVIDER=$(aws eks describe-cluster --name "${EKS_CLUSTER_NAME}" \
    --region "${AWS_REGION}" \
    --query "cluster.identity.oidc.issuer" \
    --output text | sed -e "s/^https:\/\///")
```

Create a trust policy file:

```
cat > trust-policy.json << EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Federated": "arn:aws:iam::${AWS_ACCOUNT_ID}:oidc-provider/${OIDC_PROVIDER}"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {
          "${OIDC_PROVIDER}:aud": "sts.amazonaws.com",
          "${OIDC_PROVIDER}:sub": "system:serviceaccount:${NAMESPACE}:${SERVICE_ACCOUNT_NAME}"
        }
      }
    }
  ]
}
EOF
```

Update the IAM role with the trust policy:

```
aws iam update-assume-role-policy \
    --role-name "${IAM_ROLE_NAME}" \
    --policy-document file://trust-policy.json
```

See [Configuring a Kubernetes service account to assume an IAM role](https://docs.aws.amazon.com/eks/latest/userguide/associate-service-account-role.html) for more details.

### Step 6: Verify the annotation[​](#step-6 "Direct link to Step 6: Verify the annotation")

Run the following command to display the annotation field of your service account:

```
kubectl get serviceaccount "${SERVICE_ACCOUNT_NAME}" -n "${NAMESPACE}" \
  -o jsonpath='{.metadata.annotations.eks\.amazonaws\.com/role-arn}{"\n"}'
```

The IAM role ARN you assigned to the service account displays.

### Step 7: Register the service account with Anyscale[​](#step-7 "Direct link to Step 7: Register the service account with Anyscale")

Each Anyscale cloud resource has a default service account used by all clusters. To use your new service account as the default, update the `workloads.serviceAccount.name` setting in your Helm chart with the name of your service account and upgrade your Anyscale operator.

Anyscale recommends using cloud IAM mapping to scope service accounts to users, projects, and workloads for more fine-grained access controls. Cloud owners can define cloud IAM mapping rules in the Anyscale console or using the CLI. See [Anyscale cloud IAM mapping](/iam/cloud-iam-mapping.md).
