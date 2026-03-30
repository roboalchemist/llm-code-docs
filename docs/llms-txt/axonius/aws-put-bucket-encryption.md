# Source: https://docs.axonius.com/docs/aws-put-bucket-encryption.md

# AWS - Put Bucket Encryption

**AWS - Put Bucket Encryption** enforces at-rest encryption on Amazon Web Services (AWS) instances that are the result of the saved query supplied as a trigger or devices selected in the asset table.

Query the S3 bucket names (Object storage asset type).

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## General Settings

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.
* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

## Connection Settings

* **Use stored credentials from the Amazon Web Services (AWS) adapter** *(required, default: False)* - Select this option to use the first connected AWS adapter credentials.

<Callout icon="📘" theme="info">
  NOTE

  * To use this option, you must successfully configure a AWS [Amazon Web Services (AWS)](/amazon-web-services-aws) adapter connection.

  * The user name and the password used for the adapter connection must have the [Required Permissions](#required-permissions) to install software on assets.
</Callout>

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Server Side Encryption Configuration** - Specify the default server-side-encryption configuration in JSON format. For example:

```
 {
   "Rules": [
     {
       "ApplyServerSideEncryptionByDefault": {
         "SSEAlgorithm": "AES256"|"aws:fsx"|"aws:kms"|"aws:kms:dsse",
         "KMSMasterKeyID": "string"
       },
       "BucketKeyEnabled": true|false
     }
   ]
 }
```

<br />

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **AWS Access Key ID** - Provide AWS Access Key ID or choose to use EC2 instance attached IAM role.

* **AWS Access Key Secret** - Provide AWS Access Key Secret or choose to use EC2 instance attached IAM role.

* **Proxy** - The proxy to use.

* **Use instance profile (attached role)** - The instance profile to use.

* **Content MD5** - The Base64 encoded 128-bit MD5 digest of the server-side encryption configuration.

* **Checksum Algorithm** - Select the checksum algorithm to use.

* **Expected Bucket Owner** - Enter the name of the expected bucket owner.

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.
  <br />

## APIs

Axonius uses the [PutBucketEncryption - Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketEncryption.html).

## Required Ports

Axonius must be able to communicate with the value supplied in [Connection Settings](#Connection-Settings) via the following ports:

* TCP port 443

## Required Permissions

The values supplied in [**AWS Access Key ID** and **AWS Access Key Secret**](#connection-settings) or the EC2 instance (Axonius installed on) attached IAM role account must have permissions to install software on instances:

* s3:PutEncryptionConfiguration

This permission must be added to a policy attached to relevant IAM user account.
For details on creating an IAM user and attaching policies, see [Connecting the Amazon Web Services (AWS) Adapter](/docs/connecting-aws-adapter-using-iam-user).

<br />

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).