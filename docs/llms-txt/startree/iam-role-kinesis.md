# Source: https://docs.startree.ai/corecapabilities/ingestdata/recipes/iam-role-kinesis.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# IAM-Role Based Access for Kinesis

This guide details the process of setting up cross-account IAM roles to allow your **StarTree Cloud Data Plane** to access **Kinesis streams** residing in a separate AWS account.

### 1. Source Account (Account A) Configuration

This section covers the necessary configurations within the AWS account that owns the Kinesis stream (**Source Account**).

#### 1.1. Create an IAM Policy for Kinesis Access

Create a new **IAM policy** that grants the necessary permissions to read from your Kinesis stream.

```json  theme={null}
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "kinesis:DescribeStream",
        "kinesis:GetShardIterator",
        "kinesis:GetRecords",
        "kinesis:ListShards",
        "kinesis:DescribeStreamSummary",
        "kinesis:RegisterStreamConsumer",
        "kinesis:SubscribeToShard",
        "kinesis:DescribeStreamConsumer"
      ],
      "Effect": "Allow",
      "Resource": [
        "arn:aws:kinesis:<REGION>:<SOURCE_AWS_ACCOUNT_ID>:stream/<STREAM_NAME>",
        "arn:aws:kinesis:<REGION>:<SOURCE_AWS_ACCOUNT_ID>:stream/<STREAM_NAME>/*"
      ]
    }
  ],

}
```

##### Replace the placeholders

1. REGION: The AWS region where your Kinesis stream is located (e.g., us-east-1).
2. SOURCE\_AWS\_ACCOUNT\_ID: Your AWS account ID where the Kinesis stream resides.
3. STREAM\_NAME: The name of your Kinesis stream.

#### 1.2. Create an IAM Role (e.g., KA-Source-Stream-Role)

Create a new IAM role in your Source Account. After creation, attach the IAM policy you created in the previous step to this new role.

#### 1.3. Update Trust Relationships for the IAM Role

Modify the trust policy of the newly created IAM role (KA-Source-Stream-Role) to allow the StarTree Cloud Data Plane (acting as a "Sink AWS Principal") to assume this role. This establishes the cross-account trust.

```json  theme={null}
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "<SINK_AWS_PRINCIPAL_ARN>"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

##### Replace the placeholder

1. SINK\_AWS\_PRINCIPAL\_ARN: The ARN of the AWS Principal in the Sink Account (Account B) that will be assuming this role. This can be:

* The Root User: arn:aws:iam::SINK\_AWS\_ACCOUNT\_ID:root
* A Service Role: arn:aws:iam::SINK\_AWS\_ACCOUNT\_ID:role/service-role/SERVICE\_ROLE\_NAME

### 2. Sink Account (Data Plane - Account B) Configuration

This section details the configuration required within the AWS account where your StarTree Data Plane is deployed (Sink Account).

#### 2.1. Identify the Data Plane IAM Role ARN

Obtain the ARN of the EC2 Instance Profile Role attached to the EC2 instances running your StarTree Data Plane. This role is automatically created by StarTree during environment deployment.

#### 2.2. Attach an Assume Role Policy to the Data Plane IAM Role

Create and attach an IAM policy to the Data Plane IAM Role (identified in the previous step). This policy grants the Data Plane permission to assume the KA-Source-Stream-Role in the Source Account.

```json  theme={null}
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AssumeRoleInSourceAccount",
            "Effect": "Allow",
            "Action": "sts:AssumeRole",
            "Resource": "arn:aws:iam::<SOURCE_AWS_ACCOUNT_ID>:role/KA-Source-Stream-Role"
        }
    ]
}
```

##### Replace the placeholder

1. SOURCE\_AWS\_ACCOUNT\_ID: Your AWS account ID where the Kinesis stream and KA-Source-Stream-Role reside.

### 3. Verify Access

Once the IAM roles and policies are configured, you can verify access by creating a table in StarTree Data Portal. [More documentation here](/corecapabilities/ingestdata/dataportal/streaming/kinesis).

Built with [Mintlify](https://mintlify.com).
