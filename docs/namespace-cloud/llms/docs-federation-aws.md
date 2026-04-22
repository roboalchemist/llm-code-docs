<!-- Source: https://namespace.so/docs/federation/aws -->

# Workload Federation with AWS

Namespace relies on Workload Identity Federation to allow Namespace to interact
with different systems, instead of relying on pre-shared keys which can be more
easily compromised.

## Accessing Namespace resources from AWS

Identity Federation with AWS allows your AWS-based workloads to identify
themselves to Namespace using short-lived secure credentials.

To enable this federation, we rely on [AWS Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/getting-started-with-identity-pools.html) to establish a [OpenID Connect provider](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html), and then we configure your Namespace workspace to trust
that AWS Cognito Identity Pool.

### Create an AWS Cognito Identity Pool

1. Open the **Cognito** console at <https://console.aws.amazon.com/cognito/> and click on **Create identity pool** in the section **Identity pools**.
2. Check the options **Authenticated Access** and **Custom developer provider**.
3. Select an existing IAM role to use with Cognito, or create a new one.

   AWS requires you to associate an IAM role with the identity pool. The role can have minimal permissions as the pool will be used to access Namespace resources, not AWS resources.
4. Under **Developer provider name** enter `namespace.so`.
5. Pick an arbitrary name for the identity pool and create the identity pool.

AWS will print the ID of the new identity pool. It's of the format
`{region}:{guid}`.

### Establish a trust relationship in Namespace

1. Open the [**Dashboard**](https://cloud.namespace.so/workspace/settings) and copy your Workspace ID.
2. Use the [CLI](/docs/reference/cli/installation) to establish the trust relationship:

   ```
   nsc auth trust-aws-cognito-identity-pool \
       --aws_region <region> \
       --identity_pool <guid> \
       --tenant_id <workspace-id>
   ```

### Obtain Namespace credentials from a AWS workload

Using an IAM role with permissions to access the Cognito Identity Pool, you can obtain Namespace credentials as follows:

```
nsc auth exchange-aws-cognito-token \
    --aws_region <region> \
    --identity_pool <guid> \
    --tenant_id <workspace-id>
```

This command should succeed with the name of workspace you've signed in to. It
stores a short-lived token that will be used automatically in subsequent calls.

When testing locally, you can select an AWS profile by passing `--aws_profile`.

## Accessing AWS resources from Namespace

Identity Federation with AWS allows your Namespace workloads to identify
themselves to AWS using short-lived secure credentials.

To enable this federation, create an IAM OIDC identity provider for Namespace federation in the AWS Management Console.

### Create a Namespace OIDC identity provider

1. Open the IAM console at <https://console.aws.amazon.com/iam/> and in the
   navigation pane, choose **Identity providers**, and click **Add provider**.
2. Select **OpenID Connect** as a **Provider type** and fill in `https://federation.namespaceapis.com` as the **Provider URL**.

   The expected thumbprint is `a053375bfe84e8b748782c7cee15827a6af5a405`.
3. For **Audience**, type `sts.amazonaws.com`.
4. Verify the information that you have provided. When you are done choose Add provider.

Note down the ARN of your newly created identity provider. It is of the form `arn:aws:iam::<aws-account-id>:oidc-provider/federation.namespaceapis.com`.

### Create a IAM role for federated access

1. Open the IAM console at <https://console.aws.amazon.com/iam/>.
2. In the navigation pane, choose **Roles** and click **Create role**.
3. Select the **Custom trust policy** role type, using the following JSON template as the policy:

   ```
   {
   	"Version": "2012-10-17",
   	"Statement": [
   		{
   			"Effect": "Allow",
   			"Action": "sts:AssumeRoleWithWebIdentity",
   			"Principal": {
   				"Federated": "<identity-provider-arn>"
   			},
   			"Condition": {
   				"StringLike": {
   					"federation.namespaceapis.com:aud": "sts.amazonaws.com",
   					"federation.namespaceapis.com:sub": "<workspace-id>/*"
   				}
   			}
   		}
   	]
   }
   ```

   Replace `<identity-provider-arn>` with the ARN of the new identity provider, and `<workspace-id>` with your Namespace workspace identifier (found in the [**Dashboard**](https://cloud.namespace.so/workspace/settings)).
4. Choose **Next** and add the desired permissions policies for your federated workloads.

### Accessing AWS resources from a Namespace workload

1. Obtain AWS credentials.

   ```
   $

   ```
   nsc aws assume-role --role_arn <identity-provider-arn> --write_env aws.env
   ```
   ```

   In this command, `<identity-provider-arn>` is the ARN of the new identity provider.
2. Apply the obtained credentials.

   ```
   $

   ```
   source aws.env
   ```
   ```
3. Access AWS resources.

   ```
   $

   ```
   aws s3 cp test.txt s3://amzn-s3-demo-bucket/test2.txt
   ```
   ```

Last updated September 17, 2025
