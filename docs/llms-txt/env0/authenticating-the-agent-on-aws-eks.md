# Source: https://docs.envzero.com/guides/admin-guide/self-hosted-kubernetes-agent/authenticating-the-agent-on-aws-eks.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Authenticating the Agent On AWS EKS

> Authenticate env zero self-hosted agents on AWS EKS using Pod Identity, IRSA, or Node Roles

If your env zero agent runs on an AWS EKS cluster, you can leverage any of these methods to assign an AWS IAM role to your deployments.

<Info>
  **Credential Resolution Order**

  The env zero deployment agent resolves credentials in the following priority order:

  1. Pod Identity
  2. IRSA (IAM Roles for Service Accounts)
  3. Node Role

  This order ensures that more granular and secure identity methods (like Pod Identity and IRSA) are preferred over the instance-level Node Role.
</Info>

## Using EKS Pod Identity

EKS Pod Identity simplifies the management of IAM permissions for applications on EKS clusters by allowing administrators to associate IAM roles directly with Kubernetes service accounts, eliminating the need for OIDC identity providers and enabling role reuse across multiple clusters.

<Warning>
  Version Support

  To use EKS Pod Identity with Terraform, you must be using:

* Terraform AWS Provider version ≥ 5.27.0
* if fetching credentials for the S3 backend - OpenTofu version ≥ 1.10.0

  Earlier versions do not support EKS Pod Identity and will fall back to other credentials (IRSA, Node Roles, etc).
</Warning>

For more details about EKS Pod identity and how to configure it, refer to the [EKS User Guide](https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html).

## Using IAM Roles for Service Accounts (IRSA)

IAM Roles for Service Accounts (IRSA) in Amazon EKS allow Kubernetes pods to securely assume IAM roles, enabling fine-grained access to AWS services without managing AWS credentials within the pods.

For more details about IRSA and how to configure it, refer to the [EKS User Guide](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html).

<Info>
  **Using a Custom Kubernetes Service Account**

  By default, env zero uses the default service account within the namespace where the agent is installed.

  To specify a different service account, set the `deploymentJobServiceAccountName` Helm value.

  For detailed steps on configuring a new service account, refer to this [AWS Guide](https://docs.aws.amazon.com/eks/latest/userguide/associate-service-account-role.html).
</Info>

<Warning>
  IRSA & EKS Pod Identity Session Expiry

  Please note that when using IRSA or EKS Pod Identity, the assumed session is only valid for 1 hour.

  This limitation exists because these methods internally assume the role associated with the Kubernetes service account, and role chaining is restricted to 1-hour sessions.
</Warning>

## Using the Node Role

The Node Role is the IAM Role assigned to the EC2 instances that serve as nodes in your EKS cluster.

You can use this role directly by assigning the appropriate permissions required for your env zero deployments.

For more details, refer to the [EKS User Guide](https://docs.aws.amazon.com/eks/latest/userguide/create-node-role.html).

<Warning>
  Restricting Access to the Node IAM Role

  If you are using AWS EKS and do not want to use the Node IAM Role, you must explicitly restrict access to it.

  More details can be [found here](https://aws.github.io/aws-eks-best-practices/security/docs/iam/#restrict-access-to-the-instance-profile-assigned-to-the-worker-node)
</Warning>

Built with [Mintlify](https://mintlify.com).
