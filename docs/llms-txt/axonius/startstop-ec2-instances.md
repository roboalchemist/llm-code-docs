# Source: https://docs.axonius.com/docs/startstop-ec2-instances.md

# AWS - Start/Stop EC2 Instances

**AWS - Starts EC2 Instances** starts an EC2 Instance for:

* Assets that match the results of the selected saved query, and match the Enforcement Action Conditions, if defined or assets selected on the relevant asset page.

**AWS - Stops EC2 Instances** stops an EC2 Instance for:

* Assets that match the results of the selected saved query, and match the Enforcement Action Conditions, if defined or assets selected on the relevant asset page.

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

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **Use attached IAM role**
  * If enabled, Axonius will use the attached IAM role / instance profile.
  * If disabled, Axonius will use the supplied account details in the **AWS Access Key ID** and **AWS Access Key Secret**.
* **AWS Access Key ID** and **AWS Access Key Secret** - The credentials for an account that has the [Required Permissions](#required-permissions) to start or to stop EC2 instances.
  * If supplied, Axonius will use the supplied account details to start or to stop EC2 instances.
  * If not supplied,  Axonius will use the EC2 instance (Axonius installed on) attached IAM role / instance profile to start or to stop EC2 instances.
* **Proxy** - An optional https proxy.

## Required Permissions

The values supplied in [**AWS Access Key ID** and **AWS Access Key Secret**](#parameters) or the EC2 instance (Axonius installed on) attached IAM role account must have permissions to start or to stop EC2 instances:

* **Start Amazon EC2 Instance** - Requires *ec2:StartInstances* permission.
* **Stop Amazon EC2 Instance** - Requires *ec2:StopInstances* permission.

Those permissions must be added to a policy attached to relevant IAM user account.
For details on creating an IAM user and attaching policies, see [Connecting the Amazon Web Services (AWS) Adapter](/docs/connecting-aws-adapter-using-iam-user).

<Callout icon="📘" theme="info">
  NOTE

  Devices (EC2 instances) fetched from an Amazon Web Services (AWS) adapter connection using an assumed role can be started/stopped only if the used account has *sts:AssumeRole* permission and a trust relationship for has been established for that role.
</Callout>

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).