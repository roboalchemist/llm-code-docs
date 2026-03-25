# Source: https://docs.acceldata.io/documentation/amazon-athena.md

# Amazon Athena

Amazon Athena is a **serverless query tool** provided by AWS that lets you run SQL queries directly on data stored in Amazon S3—without needing to manage infrastructure. With Acceldata’s Observability Cloud (ADOC), you gain insight into the health and usage of your Athena data. Once connected, you can monitor usage on the **Data Reliability** dashboard in ADOC.

## Prerequisites

Ensure the following requirements are met before you connect Athena as a data source:

- An active **AWS account** with access to Athena and S3.
- An **S3 bucket** to store query results.
- Access to **AWS Glue**, which Athena uses as its data catalog.
- Proper [IAM permissions](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/amazon-athena#iam-role-and-permissions) for Athena, S3, and Glue. These include:
    - Running Athena queries
    - Reading and writing to the S3 results bucket
    - Listing and reading Glue databases and tables

- For integration with ADOC, a **Data Plane** ready (either preexisting or newly created).

### IAM Role and Permissions

ADOC connects to Athena by assuming an IAM role in the customer AWS account. This role must have permissions for Athena, S3, and AWS Glue.

The following IAM policy represents the **baseline permissions** required for Athena when using the Glue Data Catalog (Glue-only setup).

Note Replace the placeholder `<s3-result-storage-bucket>` with the name of the S3 bucket specified during Athena data source creation for storing query results.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "athena:CreatePreparedStatement",
                "athena:DeletePreparedStatement",
                "athena:GetPreparedStatement",
                "athena:ListPreparedStatements",
                "athena:StartQueryExecution",
                "athena:GetQueryExecution",
                "athena:GetQueryResults",
                "athena:GetQueryResultsStream",
                "athena:ListQueryExecutions",
                "athena:BatchGetNamedQuery",
                "athena:BatchGetQueryExecution",
                "athena:ListDataCatalogs",
                "athena:ListDatabases",
                "athena:ListTableMetadata"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:PutObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::<s3-result-storage-bucket>",
                "arn:aws:s3:::<s3-result-storage-bucket>/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "glue:GetDatabases",
                "glue:GetTable",
                "glue:GetTables",
                "glue:GetPartition",
                "glue:GetPartitions",
                "glue:GetDatabase"
            ],
            "Resource": [
                "arn:aws:glue:<region>:<account-id>:catalog",
                "arn:aws:glue:<region>:<account-id>:database/*",
                "arn:aws:glue:<region>:<account-id>:table/*/*"
            ]
        }
    ]
}
```



This IAM policy enables the following:

1. **Athena Permissions** – Allows the user to run queries in Athena, manage prepared statements, and list/query Athena resources.
2. **S3 Permissions** – Grants access to the S3 bucket you specify (`<s3-result-storage-bucket>`) so Athena can read from it and write query results to it.
3. **Glue Permissions** – Provides read-only access to AWS Glue’s catalog, databases, and tables so Athena can look up table and schema information.

### Additional Prerequisites When AWS Lake Formation Is Enabled

If the underlying S3 locations for Athena tables are registered as **AWS Lake Formation Data Lake resources**, the following additional prerequisites apply.

#### Additional IAM Permission (Required)

The IAM role assumed by ADOC must be allowed to request data access from Lake Formation:

```json
{
	"Effect": "Allow",
	"Action": [
	"lakeformation:GetDataAccess"
	],
	"Resource": "*"
}
```



IAM permissions alone are **not sufficient** when Lake Formation is enabled. This permission is mandatory for Athena queries to succeed.

#### Lake Formation Data Permissions (Required)

In addition to IAM permissions, the ADOC IAM role must be explicitly granted permissions in the **AWS Lake Formation console**.

Grant the following permissions on the relevant resources:

- **Glue Database**: `DESCRIBE`
- **Glue Table**: `SELECT`

These grants must be applied to every database and table that ADOC needs to query.

#### S3 Permissions for Data Locations

Even with Lake Formation enabled, the IAM role must have read access to the underlying S3 data locations used by Athena tables:

- `s3:GetObject` on the S3 bucket and prefix where table data resides

This is in addition to the permissions required for the Athena query results bucket.

Important When AWS Lake Formation is enabled, Athena enforces **both IAM policies and Lake Formation grants**. If either layer is missing or misconfigured, queries may fail with access denied errors even though the IAM policy appears correct.

## Add Amazon Athena as a Data Source

### Step 1: Start Setup

1. Select **Register** from the left main menu.
2. Select **Add Data Source** -&gt; **AWS Athena** from the list of data sources.
3. On the **Data Source Details** page:
4. Name the data source.
5. Add a short description (optional).
6. Pick a Data Plane from the dropdown. If you don’t have one yet, select [Set Up Data Plane](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/dataplane-installation) to create one.
7. Click **Next**.

### Step 2: Add Connection Details

On the **Connection Details** page:

1. Choose your **AWS S3 authentication method**:
    1. **IAM Instance Profile:** relies on the IAM role of your EC2 or Kubernetes service account (no keys are needed).
    2. **Access Key / Secret Key**: enter your AWS credentials manually.
    3. **IAM Roles for Service Accounts (IRSA)**: for secure, no-credential access in Kubernetes environments; note it's not available for Athena via EKS Pod Identity yet.

2. (Optional) Turn on **Use Secret Manager** to keep credentials safely in AWS Secrets Manager.
3. Enter your **AWS Region**.
4. Enter the **full S3 bucket path** (starting with `s3://`) where Athena stores query results.
5. Select your **Data Plane Engine**: either **Spark** or **Pushdown Data Engine**, for profiling and quality checks.
6. Click **Test Connection**. If credentials are valid, you'll see a **Connected** message. If not, double-check your credentials and retry.
7. Click **Next** when ready.

### Step 3: Set Up Observability

1. On the **Set Up Observability** page:
2. Select the **databases** you want ADOC to monitor.

**Optional Configurations**

- Enable **Schema Drift Monitoring** to detect changes in file schemas (e.g., added, removed, or renamed columns) over time.
- **Note: Schema drift detection requires a scheduled crawler.***
- Enable **Job Concurrency** and set a maximum number of parallel jobs using Maximum Slots. For more information, see [Control Plane Concurrent Connections and Queueing Mechanism](https://docs.google.com/document/d/1W9E7ZGWzrtjXnNbVOHq-6x9F1FDbI0Fqa2gSPqUn5QI/edit?tab=t.0#heading=h.nnqa6y67lnw).
- Use **Crawler Execution Schedule** to set when background jobs scan files and collect metadata for observability:
    - Select how often the crawler runs (e.g., daily)
    - Set execution time and time zone
    - Add multiple execution times if needed

- Set Notifications
    - **Notify on Crawler Failure**: Select one or more channels for failure alerts.
    - **Notify on Success**: Receive success notifications (toggle on/off)

- Turn on the **Crawler Execution Schedule** toggle to set when ADOC should crawl Athena. Choose your preferred time and time zone.

3. Click **Submit**.

Now ADOC is set up to monitor your Athena data source, and you can run the crawler immediately or let it run based on the crawler schedule.

## What’s Next

After you connect Athena as a data source, you can start using Acceldata’s reliability features to better understand and manage your data:

- **Discover assets**: Navigate to the Reliability &gt; Discover Assets to locate and explore your newly added Athena data source.
- **Profile your data source**: Run profiling to get a summary of data structure, distribution, and quality.
- **Apply reliability policies**: Set up rules and checks to monitor data quality, freshness, and consistency over time.
- **Track insights**: Use the **Data Reliability** dashboards to see trends, alerts, and overall health of your Athena data.