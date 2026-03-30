# Source: https://docs.axonius.com/docs/install-software-using-aws-ssm.md

# AWS - Install Software Using SSM

**AWS - Install Software Using SSM**  installs software on Amazon Web Services (AWS) instances that match the results of the selected saved query, and match the Enforcement Action Conditions, if defined, or assets selected on the relevant asset page.

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

* **Use stored credentials from the Amazon Web Services (AWS) adapter** - Select this option to use the first connected AWS adapter credentials.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

    <Callout icon="📘" theme="info">
      Note

      To use this option, you must successfully configure an [Amazon Web Services (AWS)](https://docs.axonius.com/axonius-help-docs/docs/amazon-web-services-aws) adapter connection.

      The user name and password used for the adapter connection must have the [required permissions](#required-permissions) to install software on assets.
    </Callout>

* **Package Name (same account) or Package ARN (external account)** - The package to install. It can be the name of the package if the package is in the same AWS account as the devices or package ARN if the package is in a different AWS account.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **AWS Access Key ID** - Provide AWS Access Key ID or choose to use EC2 instance attached IAM role.

* **AWS Access Key Secret** - Provide AWS Access Key Secret or choose to use EC2 instance attached IAM role.

* **Proxy** - The proxy to use.

* **Use instance profile (attached role)** - Select to use the instance profile.

* **Role ARN to assume** – A file with role-ARNs which the AWS Adapter will try to assume for cross-account access with the single IAM user. Two available formats:
  * List of comma-delimited role-ARNs
  ```
  arn:aws:iam::111111111111:role/axonius-role, arn:aws:iam::222222222222:role/axonius-role
  ```
  * JSON format - list of dictionaries that define each role.
  * external\_id is only supported in the JSON format
  * The external\_id can be different for every role in the list.
  ```json
  [
      {"arn": "arn:aws:iam::111111111111:role/axonius-role"},
      {"arn": "arn:aws:iam::222222222222:role/axonius-role", "external_id": "MY-SECRET"}
  ]
  ```

* **External ID** - Use the External ID configured for the [Amazon Web Services (AWS)](/amazon-web-services-aws) adapter.

* **MFA Serial Number** - The AWS MFA Serial Number configured for the [Amazon Web Services (AWS)](/amazon-web-services-aws) adapter.

* **MFA device secret key** - The The AWS MFA Secret Key configured for the [Amazon Web Services (AWS)](/amazon-web-services-aws) adapter.

* **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

* **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

* **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

* **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

* **SSM Document Name** *(default: AWS-ConfigureAWSPackage)* -  The document name to run in SSM to install an application.

## APIs

Axonius uses the [Amazon SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.create_association).

## Required Ports

Axonius must be able to communicate with the value supplied in [Connection Settings](#Connection-Settings) via the following ports:

* TCP port 443

## Required Permissions

The values supplied in [**AWS Access Key ID** and **AWS Access Key Secret**](#connection-settings) or the EC2 instance (Axonius installed on) attached IAM role account must have permissions to install software on instances:

* **Register Task with Maintenance Window** - Requires *ssm:CreateAssociation* permission.

This permission must be added to a policy attached to relevant IAM user account.
For details on creating an IAM user and attaching policies, see [Connecting the Amazon Web Services (AWS) Adapter](/docs/connecting-aws-adapter-using-iam-user).

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version                    | Supported | Notes |
| -------------------------- | --------- | ----- |
| AWS SDK for Python (Boto3) | Yes       |       |

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).