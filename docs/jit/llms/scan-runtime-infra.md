# Source: https://docs.jit.io/docs/scan-runtime-infra.md

# Cloud Security Posture Management (CSPM)

## Jit IaC Security Scanning: Key things to know

* **Brief description:** Continuously scan your cloud environment in runtime for infrastructure security misconfigurations using hundreds of detection rules that surface issues like publicly available resources, lack of MFA, unencrypted data, and many more.
* **Scanning process**: Jit CSPM automatically scans your cloud environment every day and documents infrastructure security misconfigurations in the [Findings Page](https://dash.readme.com/project/jitsecurity/v5.0/docs/jit-findings).
* **How to get started:** Start by integrating Jit with your cloud provider (see instructions below for AWS, Azure, and GCP). Then enable CSPM by navigating to **ASPM → Security Plans** (left menu) → **Jit Max Security Plan** → **Scan your infrastructure for runtime misconfigurations**. Hit **Activate**, which will kick off the scanning processes described above.
* **Based on Prowler:** Jit unifies and enhances the leading open source scanners for all product security scanning technologies. For CSPM, Jit leverages [Prowler](https://github.com/prowler-cloud/prowler).
* **Cloud provider support**: Jit CSPM supports AWS, Azure, and GCP environments. See integration details below.

<br />

## Integration requirements

Depending on your specific cloud provider(s), you must perform one or more of the following integrations before you can activate this security control.

* [Integrating with AWS](https://docs.jit.io/docs/integrating-with-aws)
* [Integrating with Azure](https://docs.jit.io/docs/integrating-with-azure)
* [Integrating with GCP](https://docs.jit.io/docs/integrating-with-gcp)

<br />

## User Experience

Security Teams can view and filter infrastructure security misconfigurations across all cloud environments — unified alongside all other product security issues.

**Detecting and investigating infrastructure security misconfigurations**

* Go to the Jit [Backlog](https://dash.readme.com/project/jitsecurity/v5.0/docs/jit-backlog) and create a **Vulnerability Type** filter and select **Cloud Infrastructure Misconfigurations**.
* Open a security issue to bring up helpful information like its location and Knowledge Graph, which describes the runtime context of the issue.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/edb8aeea1d8cc198da048a44e4379969a6dedca04a1f645f75150f037d843e43-Screenshot_2025-01-10_at_3.56.09_PM.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

**Prioritizing the riskiest infrastructure security issues**

* In many environments, there can be thousands of infrastructure security issues. Rather than manually trying to determine which vulnerabilities introduce the most risk, Jit assigns each issue a Priority Score based on the issue's runtime context — making it easy to focus on the top risks.
* Learn more about Jit's contextual prioritization on the Context Engine [page](https://docs.jit.io/docs/contextual-prioritization-context-engine).

**Triaging and remediating infrastructure security issues**

* Create a ticket through Jira, Slack, Linear and other notification endpoints (see ticketing and triage information [here](https://docs.jit.io/docs/integrating-with-third-party-products-and-services)). Or, you can open a fix PR to patch the security issue with an updated OSS version.
* Create a fix PR from within Jit to auto remediate the issue immediately with one-click code suggestions.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/b1b39caf6d2c053acd3ad6c5972c30de298ce21fad33e09817445f7bc6d142e3-Screenshot_2025-01-10_at_3.57.57_PM.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

<br />

## AWS detection rules

| Cloud Service      | Checks                                                                                                                 |
| :----------------- | :--------------------------------------------------------------------------------------------------------------------- |
| **IAM**            | Ensure no root account access key exists                                                                               |
|                    | Ensure that no custom IAM policies exist which allow permissive role   assumption (e.g. sts:AssumeRole on \*)          |
|                    | Avoid the use of the root accounts                                                                                     |
|                    | Ensure Multi-Factor Authentication (MFA) is enabled for all IAM users that have a console password                     |
|                    | Ensure users of groups with AdministratorAccess policy have MFA tokens enabled                                         |
|                    | Ensure MFA is enabled for the root account                                                                             |
|                    | Ensure no Customer Managed IAM policies allow actions that may lead into Privilege Escalation                          |
|                    | Ensure only hardware MFA is enabled for the root account                                                               |
|                    | Ensure that all the expired SSL/TLS certificates stored in AWS IAM are removed                                         |
| **S3**             | Check if S3 buckets have policies which allow WRITE access                                                             |
|                    | Ensure there are no S3 buckets open to Everyone or Any AWS user                                                        |
|                    | Check S3 Account Level Public Access Block                                                                             |
| **CloudTrail**     | Ensure the S3 bucket CloudTrail logs is not publicly accessible                                                        |
|                    | Ensure CloudTrail is enabled in all regions                                                                            |
| **SQS**            | Check if SQS queues have policy set as Public                                                                          |
| **EC2**            | Ensure there are no EC2 AMIs set as Public                                                                             |
|                    | Ensure there are no EBS Snapshots set as Public                                                                        |
|                    | Ensure no security groups allow ingress from 0.0.0.0/0 or ::/0 to any port                                             |
|                    | Ensure no security groups allow ingress from 0.0.0.0/0 or ::/0 to Memcached port 11211                                 |
|                    | Ensure no security groups allow ingress from 0.0.0.0/0 or ::/0 to Kafka port 9092                                      |
|                    | Ensure no security groups allow ingress from 0.0.0.0/0 or ::/0 to Postgres port 5432                                   |
|                    | Ensure no security groups allow ingress from 0.0.0.0/0 or ::/0 to Redis port 6379                                      |
|                    | Ensure no security groups allow ingress from 0.0.0.0/0 or ::/0 to FTP ports 20 or 21                                   |
|                    | Ensure no security groups allow ingress from 0.0.0.0/0 or ::/0 to Telnet port 23                                       |
|                    | Ensure no security groups allow ingress from 0.0.0.0/0 or ::/0 to MySQL port 3306                                      |
|                    | Ensure no security groups allow ingress from 0.0.0.0/0 or ::/0 to Windows SQL Server ports 1433 or 1434                |
|                    | Ensure no security groups allow ingress from 0.0.0.0/0 or ::/0 to Cassandra ports 7199 or 9160 or 8888                 |
|                    | Ensure no security groups allow ingress from 0.0.0.0/0 or ::/0 to MongoDB ports 27017 and 27018                        |
|                    | Ensure there are no security groups without ingress filtering being used                                               |
|                    | Ensure no security groups allow ingress from 0.0.0.0/0 or ::/0 to Oracle ports 1521 or 2483                            |
|                    | Ensure no security groups allow ingress from 0.0.0.0/0 or ::/0 to port 3389                                            |
|                    | Ensure no security groups allow ingress from 0.0.0.0/0 or ::/0 to SSH port 22                                          |
|                    | Ensure the default security group of every VPC restricts all traffic                                                   |
|                    | Check if any of the Elastic or Public IP are in Shodan (requires Shodan API KEY)                                       |
|                    | Ensure no security groups allow ingress from 0.0.0.0/0 or ::/0 to Elasticsearch/Kibana ports                           |
|                    | Ensure no security groups allow ingress from wide-open non-RFC1918 address                                             |
|                    | Find security groups with more than 50 ingress or egress rules                                                         |
| **RDS**            | Ensure there are no Public Accessible RDS instances                                                                    |
|                    | Check if RDS Snapshots and Cluster Snapshots are public                                                                |
|                    | Check if RDS instances client connections are encrypted (Microsoft SQL Server and PostgreSQL)                          |
| **Glacier**        | Check if S3 Glacier vaults have policies which allow access to everyone                                                |
| **EFS**            | Check if EFS have policies which allow access to everyone                                                              |
| **SNS**            | Check if SNS topics have policy set as Public                                                                          |
|                    | Ensure there are no SNS Topics unencrypted                                                                             |
| **Opensearch**     | Check if Amazon Elasticsearch/Opensearch Service domains has Amazon Cognito authentication for Kibana enabled          |
|                    | Check if Amazon Elasticsearch/Opensearch domains are set as Public or if it has open policy access                     |
| **SSM**            | Find secrets in SSM Documents                                                                                          |
|                    | Check if there are SSM Documents set as public                                                                         |
|                    | Check if EC2 instances managed by Systems Manager are compliant with patching requirements                             |
| **AutoScaling**    | Find secrets in EC2 Auto Scaling Launch Configuration                                                                  |
| **GuardDuty**      | There are High severity GuardDuty findings                                                                             |
| **Redshift**       | Check for Publicly Accessible Redshift Clusters                                                                        |
| **CloudFormation** | Find secrets in CloudFormation outputs                                                                                 |
| **ECR**            | Ensure there are no ECR repositories set as Public                                                                     |
| **EKS**            | Ensure EKS Clusters are created with Private Endpoint Enabled and Public Access Disabled                               |
| **EMR**            | EMR Account Public Access Block enabled                                                                                |
| **ACM**            | Check if ACM Certificates are about to expire in specific days or less                                                 |
| **CodeArtifact**   | Ensure CodeArtifact internal packages do not allow external public source publishing                                   |
| **WorkSpaces**     | Ensure that your Amazon WorkSpaces storage volumes are encrypted in order to meet security and compliance requirements |

## Azure detection rules

| Cloud Service | Checks                                                                                                                     |
| :------------ | :------------------------------------------------------------------------------------------------------------------------- |
| **defender**  | Ensure That Microsoft Defender for App Services Is Set To 'On'                                                             |
|               | Ensure That Microsoft Defender for Azure Resource Manager Is Set To 'On'                                                   |
|               | Ensure That Microsoft Defender for Azure SQL Databases Is Set To 'On'                                                      |
|               | Ensure That Microsoft Defender for Containers Is Set To 'On'                                                               |
|               | Ensure That Microsoft Defender for Cosmos DB Is Set To 'On'                                                                |
|               | Ensure That Microsoft Defender for Databases Is Set To 'On'                                                                |
|               | Ensure That Microsoft Defender for DNS Is Set To 'On'                                                                      |
|               | Ensure That Microsoft Defender for KeyVault Is Set To 'On'                                                                 |
|               | Ensure That Microsoft Defender for Open-Source Relational Databases Is Set To 'On'                                         |
|               | Ensure That Microsoft Defender for Servers Is Set to 'On'                                                                  |
|               | Ensure That Microsoft Defender for SQL Servers on Machines Is Set To 'On'                                                  |
|               | Ensure That Microsoft Defender for Storage Is Set To 'On'                                                                  |
| **IAM**       | Ensure that no custom subscription owner roles are created                                                                 |
| **storage**   | Ensure that your Microsoft Azure Storage accounts are using Customer Managed Keys (CMKs) instead of Microsoft Managed Keys |

## Google Cloud Platform detection rules

| Cloud Service    | Checks                                                                                        |
| :--------------- | :-------------------------------------------------------------------------------------------- |
| **bigquery**     | Ensure BigQuery datasets are encrypted with Customer-Managed Keys (CMKs)                      |
|                  | Ensure That BigQuery Datasets Are Not Anonymously or Publicly Accessible.                     |
|                  | Ensure BigQuery tables are encrypted with Customer-Managed Keys (CMKs).                       |
| **cloudsql**     | Ensure That Cloud SQL Database Instances Do Not Implicitly Whitelist All Public IP Addresses  |
|                  | Ensure 'external scripts enabled' database flag for Cloud SQL Server instance is set to 'off' |
|                  | Ensure 'remote access' database flag for Cloud SQL Server instance is set to 'off'            |
| **cloudstorage** | Ensure That Cloud Storage Bucket Is Not Anonymously or Publicly Accessible                    |
| **compute**      | Check for Virtual Machine Instances with Public IP Addresses                                  |
|                  | Ensure that the default network does not exist                                                |
| **IAM**          | Ensure Service Account does not have admin privileges                                         |
| **KMS**          | Check for Publicly Accessible Cloud KMS Keys                                                  |