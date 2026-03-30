# Source: https://docs.axonius.com/docs/aws-create-snapshot-for-ebs-volume.md

# AWS - Create Snapshot for EBS Volume

**AWS - Create Snapshot for EBS Volume** creates snapshots for provided EBS volumes for:

* Assets returned by the selected query or assets selected on the relevant asset page.

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from the [Amazon Web Services (AWS)](/docs/amazon-web-services-aws) adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure an [Amazon Web Services (AWS)](/docs/amazon-web-services-aws) adapter connection.
</Callout>

* **Description** - Enter the reason the snapshot is created, for example, "Performing a weekly backup".

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Use attached IAM role**

  * If enabled (and **Use stored credentials from the AWS adapter** is disabled), Axonius will use the EC2 instance (Axonius installed on) attached IAM to be used to send a JSON file to an S3 bucket.

  * If disabled (and **Use stored credentials from the AWS adapter** is disabled), Axonius will use the supplied account details in the **IAM Access Key ID** and **IAM Access Key Secret** to send a JSON file to an S3 bucket.

  <Callout icon="📘" theme="info">
    Note

    This option will be ignored if **Use stored credentials from the AWS adapter** is enabled.
  </Callout>

  * **AWS Access Key ID** - Specify the  AWS Access Key ID to access the Amazon S3 bucket.
  * **AWS Secret Access Key** - Specify the AWS Secret Access Key for the specified **AWS Access Key ID**.
    * If supplied (and both **Use stored credentials from the AWS adapter** and **Use attached IAM role** are disabled), Axonius uses the account user credentials to send a JSON file to an S3 bucket.
    * If not supplied (and both **Use stored credentials from the AWS adapter** and **Use attached IAM role** are disabled), Axonius will fail any execution of this action.
  * **Proxy** - An optional HTTPS proxy.
  * **AWS session token** - The AWS session token for this current AWS session.
</Callout>

* **Volume ID** - Provide a (single) EBS Volume ID (format: `vol-xxxxxx`) to create a snapshot for.

## APIs

Axonius uses the [AWS Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.create_association) API.

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the following permission(s) to perform this Enforcement Action:

* ec2:CreateSnapshot
* ec2:DescribeVolumes
* ec2:DescribeSnapshots

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).