# Source: https://docs.axonius.com/docs/aws-delete-files-from-s3-bucket.md

# AWS - Delete Files From S3 Bucket

**AWS - Delete Files From S3 Bucket** deletes a file from a specific S3 bucket.

<Callout icon="💡" theme="warn">
  Important note

  This Enforcement Action runs independently, regardless of the assets selected in the query. Selecting a query is only required to trigger a successful run of the action, so you can select any query.
</Callout>

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from the Amazon Web Services (AWS) adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure an [Amazon Web Services (AWS)](/docs/amazon-web-services-aws) adapter connection.
</Callout>

* **Filename to delete** - The name of the file to delete.
* **S3 Bucket Name** - The bucket from which to delete the file.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Use attached IAM role**

  * When enabled, Axonius will use the attached IAM role / instance profile.

  * When disabled, Axonius will use the supplied credentials for **AWS Access Key ID** and **AWS Access Key Secret**.

  * **AWS Access Key ID** and **AWS Access Key Secret** - The credentials for an account that has the [Required Permissions](/docs/aws-delete-files-from-s3-bucket#required-permissions) to perform this action.

  * When not supplied, Axonius will use the attached IAM role of the EC2 instance Axonius is installed on / instance profile.

  <Callout icon="📘" theme="info">
    Note

    For this action to succeed, you must either enable **Use attached IAM role** or provide the  **AWS Access Key ID** and **AWS Access Key Secret**.
  </Callout>

  * **Proxy** - An optional https proxy.
  * **AWS session token** - The token for this current AWS session.
</Callout>

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the following permission(s) to perform this Enforcement Action:

* s3:DeleteObject
* s3:ListBucket
* s3:GetObject

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).