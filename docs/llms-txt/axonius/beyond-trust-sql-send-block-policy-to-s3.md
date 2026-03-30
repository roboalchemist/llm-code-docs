# Source: https://docs.axonius.com/docs/beyond-trust-sql-send-block-policy-to-s3.md

# BeyondTrust BeyondInsight Send Block Policy to S3

**BeyondTrust BeyondInsight - Send Block Policy to S3** sends a block policy, in XML format,  for the software that results from the saved query supplied as a trigger (or assets that were selected in the asset table), and sends it to a specific path on an SSH server using S3.

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

<Callout icon="📘" theme="info">
  Note

  This enforcement action runs on Software assets.
</Callout>

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Amazon S3 bucket name** - Specify the Amazon S3 bucket name for which the file will be sent.
  For creating, configuring, and access Amazon S3 buckets, see [Configuring an S3 Bucket to use with Axonius](/docs/amazon-web-services-aws#onfiguring-an-s3-bucket-to-use-with-axonius).

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **AWS Access Key ID** - Specify the AWS Access Key ID to access the Amazon S3 bucket.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **AWS Secret Access Key** - Specify the AWS Secret Access Key for the specified **AWS Access Key ID**.

  * **Use attached IAM role** - When selected, Axonius uses the specified user credentials to perform the Amazon S3 PutObject operation.

  * When not selected, Axonius uses the EC2 instance (Axonius installed on) attached IAM role instead of using the **AWS Access Key ID** and **AWS Access Key Secret** credentials supplied.

  The IAM user must have an attached policy that allows the Amazon S3 PutObject operation, for example:

  <Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(502).png" />

  For details about creating an IAM user, see [Connecting Amazon Web Services (AWS) Adapter](/docs/amazon-web-services-aws#connecting-the-amazon-web-services-aws-adapter) or [Creating an IAM User in Your AWS Account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) in AWS online help.

  * **AWS region** *(default: us-east-1)* - Specify the region name in which Amazon S3 is located.

  * When supplied, the PutObject operation is performed on the supplied Amazon S3 details in the supplied region.

  * When not supplied, the PutObject operation is performed on the supplied Amazon S3 details in 'us-east-1'.

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
</Callout>

* **Amazon S3 object location (key)** - Specify the S3 object key to store a CSV file that contains the entities derived from the saved query supplied as a trigger (or entities that have been selected in the asset table).
  * When supplied, the CSV file path and name are stored in the specified object key. For example, if *reports/axonius* is specified, the file path and name are *reports/axonius.csv*.
  * When not supplied, the CSV file is stored as *axonius\_csv.csv*.

* **Append date and time to file name** -
  * When this option is enabled, the date and time (in UTC) of enforcement action execution are added as a suffix to the generated CSV file name. For example, *axonius\_csv\_2024-07-06-16:48:13.csv*.
  * When this option is disabled, the CSV file is stored based on the specified/default object key.

* **Overwrite existing file** - Choose to store the generated CSV file even if a CSV file with the same name already exists.
  * When this option is enabled, the generated CSV file is stored even if a CSV file with the exact name already exists.

  * When this option is disabled, the generated CSV file is not stored if a CSV file with the exact name already exists. As a result, the Enforcement action fails.

* The following fields are section names in the XML that are created by the Enforcement Action. Enter a value for the relevant fields.

  * **Configuration ID**
  * **Configuration Version**
  * **Configuration Revision**
  * **Configuration Revision Number**
  * **GlobalOptionsSet ID**
  * **Trusted Application Protection Version**
  * **Trusted Application Protection Revision**
  * **Application Group ID**
  * **Application Group Name**
  * **Default Application Type** *(default: exe)*

  An XML tag is created for each installed application.

* **Get installed software from CSV adapter only** -
  * When this option is enabled (the default), the XML file only includes software titles that are from the CSV adapter connection.
  * When this option is disabled, the XML file includes software titles from the specified adapter connections.

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).