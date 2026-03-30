# Source: https://docs.axonius.com/docs/send-json-to-amazon-s3.md

# AWS - Send JSON to S3

**AWS - Send JSON to S3** creates a JSON file with the assets returned by the selected query or assets selected on the relevant asset page and sends it to a specific Amazon Simple Storage Service (Amazon S3) bucket.

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

These fields are required to run the Enforcement Action.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from the Amazon Web Services (AWS) adapter** - Select this option to use the first connected AWS adapter credentials.

  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

  <br />

  <Callout icon="📘" theme="info">
    Note

    * To use this option, you must successfully configure a AWS [Amazon Web Services (AWS)](/docs/amazon-web-services-aws) adapter connection.

    * The user name and the password used for the adapter connection must have the [required permissions](#required-permissions) to install software on assets.
  </Callout>

* **Use stored credentials from the AWS adapter** -
  * If enabled, Axonius will use the AWS adapter connection credentials that match the specified **AWS Access Key ID** to determine the IAM user/role to be used to send a JSON file to an S3 bucket.
  * If disabled:
    * If **Use attached IAM role** is enabled, Axonius will use the attached IAM role of the EC2 instance Axonius is installed on to send a JSON file to an S3 bucket.
    * Else, Axonius will use the IAM user/role associated with the specified **IAM Access Key ID** and **IAM Access Key Secret** to send a JSON file to an S3 bucket.

<Callout icon="📘" theme="info">
  NOTE

  To use this option, you must successfully configure an [AWS adapter connection](/docs/amazon-web-services-aws).
</Callout>

* **Amazon S3 bucket name** - Specify the Amazon S3 bucket name for which the file will be sent.
  For creating, configuring, and access Amazon S3 buckets, see see [Configuring an S3 Bucket to use with Axonius](/docs/amazon-web-services-aws#configuring-an-s3-bucket-to-use-with-axonius).

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **AWS Access Key ID** - Specify the  AWS Access Key ID to access the Amazon S3 bucket.

  * **AWS Secret Access Key** - Specify the AWS Secret Access Key for the specified **AWS Access Key ID**.

  * If supplied (and both **Use stored credentials from the AWS adapter** and **Use attached IAM role** are disabled), Axonius uses the account user credentials to send a JSON file to an S3 bucket.

  * If not supplied (and both **Use stored credentials from the AWS adapter** and **Use attached IAM role** are disabled), Axonius will fail any execution of this action.

  * **Use attached IAM role**

  * If enabled (and **Use stored credentials from the AWS adapter** is disabled), Axonius will use the attached IAM role of the EC2 instance Axonius is installed on to send a JSON file to an S3 bucket.

  * If disabled (and **Use stored credentials from the AWS adapter** is disabled), Axonius will use the supplied account details in the **IAM Access Key ID** and **IAM Access Key Secret** to send a JSON file to an S3 bucket.

  * **AWS region** *(default: us-east-1)* - Specify the region name the Amazon S3 located.
    * If supplied, PutObject operation will be done on the supplied Amazon S3 details in the supplied region.
    * If not supplied, PutObject operation will be done on the supplied Amazon S3 details in 'us-east-1'.

  * **HTTPS\_Proxy** (optional) - Connect the adapter to a proxy instead of directly connecting it to the domain.
</Callout>

* **Amazon S3 object location (key)** - Specify the S3 object key to store a JSON file that contains the entities derived from the saved query supplied as a trigger (or entities that have been selected in the asset table).
  * If supplied, the JSON file path and name will be stored in the specified object key. For example, if *reports/axonius* is specified, the file path and name will be *reports/axonius.json*.
  * If not supplied, the JSON file will be stored as *axonius\_enforcement\_center\_data.json*.
* **Append date and time to file name**
  * If enabled, the date and time (in UTC) of enforcement action execution will be added as a suffix to the generated JSON file name. For example, *axonius\_2020-01-06-16:48:13.json*.
  * If disabled, the JSON file will be stored based on the specified/default object key.
* **Override file if exists** - choose to store the generated JSON file even if a JSON file with the same name already exists.
  * If enabled, the generated JSON file will be stored even if a JSON file with the exact name already exists.
  * If disabled, the generated JSON file will be not be stored if a JSON file with the exact name already exists. As a result, the Enforcement action will fail.
* **Always export aggregated fields as arrays** - Select this option to always represent aggregated fields as  arrays in the JSON file that is created.
* **Compress File Using GZip** - Select this option to upload the JSON file as a compressed .gz file.

## Required Permissions

The values supplied in [**AWS Access Key ID** and **AWS Access Key Secret**](#parameters) or the EC2 instance (Axonius installed on) attached IAM role account must have the following permissions:

* s3:PutObject
* s3:GetObject
* s3:ListAllMyBuckets
* s3:ListBucket
* s3:PutObjectTagging
* s3:DeleteObject

If the target S3 bucket is encrypted with a KMS key: then the kms:GenerateDataKey permission is also required.

Those permissions must be added to a policy attached to relevant IAM user account.

For details on creating an IAM user and attaching policies, see [Connecting the Amazon Web Services (AWS) Adapter](/docs/amazon-web-services-aws#connecting-the-amazon-web-services-aws-adapter).

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).