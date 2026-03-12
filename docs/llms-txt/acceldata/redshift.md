# Source: https://docs.acceldata.io/documentation/redshift.md

# Amazon Redshift

Amazon Redshift is a fully managed data warehouse service from AWS. ADOC can connect to and monitor Amazon Redshift to provide insights into data quality, schema drift, and usage trends.

## Prerequisites

Ensure the following requirements are met before you connect Redshift as a data source:

- Access to an Amazon Redshift cluster and database with the required user credentials.
- The ADOC Data Plane is deployed and has network access to the Redshift endpoint (host and port).
- Required firewall rules or security groups allow inbound traffic from the ADOC Data Plane.
- The IAM policy or database user permissions allow access to schema, table, and column metadata.

---

## Add Redshift as a Data Source

To register Amazon Redshift as a data source in ADOC, perform the following steps:

### Step 1: Start Setup

1. Select **Register** from the left main menu.
2. Select **Add Data Source**.
3. Select **Redshift** from the list of data sources.
4. On the **Data Source Details** page:
    1. Enter a unique name for this data source.
    2. Optionally, add a brief description to clarify its purpose.
    3. Enable the **Data Reliability** toggle and select your **data plane** from the drop-down list.

5. Select **Next** to proceed.

### Step 2: Add Connection Details

Enter your Redshift connection information. Required fields vary depending on the selected Authentication Type.

**Common Fields (Always Required)**

| Field | Description | 
| ---- | ---- | 
| **Redshift JDBC URL** | The connection string to your Redshift cluster. Format:`jdbc:redshift://<host>:<port>/<database>` | 
| **Redshift DB Username** | The Redshift user with metadata access permissions. | 


**Authentication Type-Specific Fields**

| **Authentication Type** | **Additional Fields Required** | 
| ---- | ---- | 
| DB Username and Password | - **Password**: Enter the Redshift password manually.\n- (Optional) Toggle **Use Secret Manager** to fetch credentials from AWS Secrets Manager. If enabled:\n- **Select Secret Manager**: Choose the secret manager from the dropdown. \n- **Secret Key/Name**: Enter the key name inside the secret that stores the password. | 
| AWS EC2 Instance Profile | No additional input fields are shown. Credentials are automatically fetched by the EC2 instance running the Data Plane. | 
| AWS IAM Roles for Service Accounts (IRSA) | No additional input fields are shown. The Data Plane running on Kubernetes uses IRSA to assume the appropriate role configured via annotations. | 


> - **Use Secret Manager** toggle is only shown when DB Username and Password is selected.> - For IAM-based methods (EC2 Instance Profile or IRSA), credentials are automatically handled through the environment.

Once all required fields are completed:

1. Select **Test Connection** to validate access to the Redshift cluster.
2. If the test is successful, proceed by clicking **Next**.

If the connection fails, verify that:

- The JDBC URL is correct and accessible from the Data Plane. For more information, see this [AWS documentation](https://docs.aws.amazon.com/redshift/latest/mgmt/jdbc20-obtain-url.html).
- The username is valid and has required privileges.
- The credentials or IAM roles are correctly configured.

### Step 3: Setup Observability

Configure how ADOC will monitor:

- **Schema Names (Required)**: Select one or more schemas from your Redshift instance for which you want to enable observability features.
- **Configure Observability Options (Optional)**: You can optionally enable the following observability features to enhance data monitoring for your S3 buckets.

| Feature | Description | 
| ---- | ---- | 
| **Enable Query Analysis** | Analyzes query patterns and performance metrics to help detect inefficiencies and optimize query execution. | 
| **Enable Data Freshness Monitoring** | Monitors the timeliness of incoming data by checking for delays in expected file arrival times. | 
| **Enable Schema Drift Monitoring** | Detects changes in file schema over time (e.g., columns added, removed, or renamed). Requires enabling a crawler to track schema changes. | 
| **Enable Crawler Execution Schedule** | Sets up a recurring crawler to scan the bucket for schema and metadata updates. - Choose frequency (e.g., daily) - Set time and timezone - Add multiple execution times if needed | 
| **Notify on Crawler Failure** | Select one or more notification channels (e.g., Slack, Email) to receive alerts if the crawler fails to execute. | 
| **Notify on Success** | Toggle this if you’d like to receive success notifications after each crawler execution. | 


After configuring these options, click **Submit** to save your configuration and begin monitoring the Redshift data source.

---

## What’s Next

Once Redshift is connected, you can:

- **Monitor data quality and reliability**: Run profiling jobs to assess metrics such as row count, null percentages, and freshness.
- **Track schema changes over time**: Enable schema drift to stay informed about structural changes in tables and columns.
- **Set data quality rules**: Enforce validations on columns such as non-null constraints, value thresholds, and outlier detection.

---

## Additional Reference

### IAM Authentication and Access Management for Redshift

Acceldata supports IAM-based authentication mechanisms for securely connecting to Amazon Redshift without using static credentials. This includes both **IAM Roles for Service Accounts (IRSA)** and **EKS Pod Identity**, which enable secure access using dynamic, role-based permissions.

### IAM Roles for Service Accounts (IRSA)

**IRSA** enables Kubernetes workloads to securely access AWS services such as Redshift without embedding AWS credentials in your configuration. IRSA binds IAM roles to Kubernetes service accounts, enforcing the principle of least privilege.

**Usage in ADOC**

When using IRSA for Redshift authentication in ADOC:

- You must annotate the Kubernetes service account used by the ADOC Data Plane with the appropriate IAM role.
- The IAM role must have the required permissions to connect to Amazon Redshift and fetch credentials using the AWS SDK.

**Sample Annotation**

```none
eks.amazonaws.com/role-arn: arn:aws:iam::<AWS Account ID>:role/<IAM Role Name>
```



Replace `<AWS Account ID>` and `<IAM Role Name>` with the appropriate values.

**Required IAM Policy for Redshift Access**

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "redshift:GetClusterCredentials",
        "redshift:DescribeClusters"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": "secretsmanager:GetSecretValue",
      "Resource": "<AWS ARN of the Secret>"
    }
  ]
}
```



Replace `<AWS ARN of the Secret>` with the actual Amazon Resource Name (ARN) of your AWS Secrets Manager entry (if using secrets-based authentication).

### EKS Pod Identity (Optional Alternative)

**EKS Pod Identity** is an AWS-native method of assigning IAM roles directly to pods running in your EKS cluster without requiring annotations on Kubernetes service accounts.

**Usage in ADOC**

If your EKS cluster is configured for Pod Identity:

- The IAM role is associated directly with the pod, and ADOC automatically uses the credentials available through the underlying AWS SDK.
- You must still ensure the IAM role has the same permissions as listed above for accessing Redshift and Secrets Manager.

Refer to [AWS Documentation](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) for steps on configuring Pod Identity.