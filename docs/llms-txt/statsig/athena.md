# Source: https://docs.statsig.com/statsig-warehouse-native/connecting-your-warehouse/athena.md

# Source: https://docs.statsig.com/data-warehouse-ingestion/athena.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Athena Ingestion

## Overview

To set up connection with Athena, Statsig needs the following

* Region
* Granting Athena Access Permissions to a Statsig-owned Service Account

In place of granting Athena Access Permissions to a Statsig-owned Service Account, you can also provide the following:

* IAM User Access Key
* IAM Secret Access Key

The above IAM User will need to be given permissions to query from Athena. Here's a sample policy with required permissions to access Athena:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "athena:StartQueryExecution",
                "athena:GetQueryExecution",
                "athena:GetQueryResults",
                "athena:CreatePreparedStatement",
                "athena:DeletePreparedStatement",
                "athena:GetPreparedStatement",
                "athena:GetQueryResultsStream",
                "s3:GetObject",
                "s3:ListBucket",
                "s3:GetBucketLocation",
                "glue:GetTable",
                "glue:GetDatabase"
            ],
            "Resource": [
                "arn:aws:athena:*:<ACCOUNT_ID>:workgroup/*",
                "arn:aws:glue:<REGION>:<ACCOUNT_ID>:*"
            ]
        }
    ]
}
```


Built with [Mintlify](https://mintlify.com).