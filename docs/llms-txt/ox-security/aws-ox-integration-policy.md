# Source: https://docs.ox.security/ox-integrations/3rd-party-integrations/cloud-security/aws/aws-ox-integration-policy.md

# AWS OX Integration Policy

* ViewOnlyAccess
* SecurityAudit

When creating the OX Integration Policy as directed in the AWS connection instructions, include the ViewOnlyAccess policy and the SecurityAudit policy, and then copy the following JSON object and paste it in the policy creation page:

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "apigateway:GET",
                "autoscaling:Describe*",
                "backup:List*",
                "ec2:GetEbsEncryptionByDefault",
                "ec2:GetSnapshotBlockPublicAccessState",
                "ec2:GetInstanceMetadataDefaults",
                "ecr:Describe*",
                "ecr:GetRegistryScanningConfiguration",
                "support:Describe*",
                "tag:GetTagKeys",
                "lambda:GetFunction",
                "glue:GetConnections",
                "glue:GetSecurityConfiguration",
                "glue:SearchTables",
                "glue:GetMLTransforms",
                "s3:GetAccountPublicAccessBlock",
                "shield:GetSubscriptionState",
                "shield:DescribeProtection",
                "elasticfilesystem:DescribeBackupPolicy",
                "iam:SimulatePrincipalPolicy",
                "account:Get*",
                "appstream:Describe*",
                "appstream:List*",
                "backup:Get*",
                "bedrock:List*",
                "bedrock:Get*",
                "cloudtrail:GetInsightSelectors",
                "codeartifact:List*",
                "codebuild:BatchGet*",
                "codebuild:ListReportGroups",
                "cognito-idp:GetUserPoolMfaConfig",
                "dlm:Get*",
                "drs:Describe*",
                "ds:Get*",
                "ds:Describe*",
                "ds:List*",
                "dynamodb:GetResourcePolicy",
                "ec2:GetSnapshotBlockPublicAccessState",
                "lambda:GetFunction*",
                "logs:FilterLogEvents",
                "lightsail:GetRelationalDatabases",
                "macie2:GetMacieSession",
                "macie2:GetAutomatedDiscoveryConfiguration",
                "securityhub:BatchImportFindings",
                "securityhub:GetFindings",
                "servicecatalog:Describe*",
                "servicecatalog:List*",
                "ssm:GetDocument",
                "ssm-incidents:List*",
                "states:ListTagsForResource",
                "wellarchitected:List*",
                "eks:ListNodegroups",
                "eks:DescribeFargateProfile",
                "eks:ListTagsForResource",
                "eks:ListAddons",
                "eks:DescribeAddon",
                "eks:ListFargateProfiles",
                "eks:DescribeNodegroup",
                "eks:DescribeIdentityProviderConfig",
                "eks:ListUpdates",
                "eks:DescribeUpdate",
                "eks:AccessKubernetesApi",
                "eks:DescribeCluster",
                "eks:ListClusters",
                "eks:DescribeAddonVersions",
                "eks:ListIdentityProviderConfigs"
            ],
            "Resource": "*",
            "Effect": "Allow"
        },
        {
            "Action": [
                "ecr:GetAuthorizationToken*",
                "ecr:BatchGetImage*",
                "ecr:GetDownloadUrlForLayer*"
            ],
            "Resource": "*",
            "Effect": "Allow"
        }
    ]
}
```
