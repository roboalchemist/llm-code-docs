# Source: https://docs.anyscale.com/administration/cloud-deployment/aws-ecr.md

# Access Amazon ECR

[View Markdown](/administration/cloud-deployment/aws-ecr.md)

# Access Amazon ECR

This section configures [**Amazon Elastic Container Registry**](https://aws.amazon.com/ecr/) access for Anyscale clusters. This setup is useful if you want to launch clusters with [**custom images**](/container-image/custom-image.md) stored in a private registry. This configuration consists of two steps:

1. The IAM role used by Anyscale clusters needs the correct policies to read from ECR.
2. The repository in ECR must grant access to the given IAM role.

## Identify the IAM role used by Anyscale clusters[​](#identify-the-iam-role-used-by-anyscale-clusters "Direct link to Identify the IAM role used by Anyscale clusters")

When deploying an Anyscale Cloud on AWS, Anyscale configures a default IAM role that is assumed by all Ray cluster nodes. This IAM role follows this naming pattern if you set up the cloud using `anyscale cloud setup`:

```
<Anyscale Cloud ID>-cluster_node_role
```

For clouds created with `anyscale cloud register`, the role is specified through the flag `--instance-iam-role-id`.

You can also override the default IAM role by specifying an existing role in your compute configuration. See [Specify an IAM role for an Anyscale cluster](/iam/aws.md#compute-config).

tip

To determine the IAM role on a running cluster, execute:

```
aws sts get-caller-identity
```

## Grant Permissions to the IAM role[​](#grant-permissions-to-the-iam-role "Direct link to Grant Permissions to the IAM role")

Once you've identified the IAM role used by Anyscale clusters, you can grant the required permissions to that role.

### Attach AmazonEC2ContainerRegistryReadOnly to the cluster node role[​](#attach-policy "Direct link to Attach AmazonEC2ContainerRegistryReadOnly to the cluster node role")

1. Look in the **Permissions policies** section of your Role. If the role is assigned **AmazonEC2ContainerRegistryReadOnly**, no further action is required. If it does not, continue to set up the correct policies.

![](/assets/images/ecr-read-only-policy-ecb82b82baebb4c1d304b799653ec6d7.png)

2. Click **Add Permissions** and select **Attach policies**.

![](/assets/images/attach-policies-be3196f84e11da512fb6cc6a446ac82a.png)

3. Search for **AmazonEC2ContainerRegistryReadOnly** and select the policy.

![](/assets/images/select-ecr-policy-51c571b7648ee92e205353de737b9882.png)

4. Click **Attach policies**.

### Grant the cluster node role access to a private ECR repository[​](#grant-access "Direct link to Grant the cluster node role access to a private ECR repository")

1. Search for the Cluster Node Role on the [**AWS IAM**](https://us-east-1.console.aws.amazon.com/iamv2/home#/roles) page and select it.

![](/assets/images/autoscaler-role-search-d8277e3f650bf700bcc243603263c308.png)

2. Find and copy the ARN.

![](/assets/images/autoscaler-v1-arn-8f287b49e54141d203af8b7a5def306d.png)

3. Search for the private repo that you want to grant access to on the [**AWS ECR page**](https://us-east-1.console.aws.amazon.com/ecr/repositories) and select it.

![](/assets/images/private-repositories-4c8ad9f104c4a8015dc6a76d3d59dcbe.png)

4. Navigate to the **Permissions** section.

![](/assets/images/test-registry-permissions-f9d17552ecd030453718b9bb9d1cf4c3.png)

5. Select **Edit JSON Policy**.

![](/assets/images/select-ecr-policy-51c571b7648ee92e205353de737b9882.png)

6. Add the role ARN from step 2 into the `<REPLACE_WITH_ARN>` field in the JSON below.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowPull",
      "Effect": "Allow",
      "Principal": {
        "AWS": "<REPLACE_WITH_ARN>"
      },
      "Action": [
        "ecr:BatchCheckLayerAvailability",
        "ecr:BatchGetImage",
        "ecr:DescribeImageScanFindings",
        "ecr:DescribeImages",
        "ecr:DescribeRepositories",
        "ecr:GetAuthorizationToken",
        "ecr:GetDownloadUrlForLayer",
        "ecr:GetLifecyclePolicy",
        "ecr:GetLifecyclePolicyPreview",
        "ecr:GetRepositoryPolicy",
        "ecr:ListImages",
        "ecr:ListTagsForResource"
      ]
    }
  ]
}
```

Once this step is completed, nodes launched by Anyscale should have access to your private registry.
