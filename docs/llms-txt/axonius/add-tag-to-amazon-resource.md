# Source: https://docs.axonius.com/docs/add-tag-to-amazon-resource.md

# AWS - Add Tags to Resource

<Callout icon="📘" theme="info">
  Note

  This Enforcement Action was previously named **Add Tag to Amazon EC2 Instance**.
</Callout>

**AWS - Add Tags to Resource** adds the tags to Amazon Resource​s from:

* Assets that match the results of the selected saved query, and match the Enforcement Action Conditions, if defined or assets selected on the relevant asset page.

<Callout icon="📘" theme="info">
  Note

  This Enforcement Action supports devices, users, and roles.
</Callout>

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

* **Tag keys** - A semicolon (;) separated list of tag keys to be added. A tag key must not begin with "aws:".
* **Target AWS assets** - Select the resource types to which the tags will be added. Select all that apply.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **Use attached IAM role**
  * If enabled, Axonius will use the attached IAM role / instance profile.
  * If disabled, Axonius will use the supplied account details in the **AWS Access Key ID** and **AWS Access Key Secret**.
* **AWS Access Key ID** and **AWS Access Key Secret** - The credentials for an account that has the [Required Permissions](#required-permissions) to remove tags.
  * If supplied, Axonius will use the supplied account details.
  * If not supplied,  Axonius will use the attached IAM role / instance profile.
* **Proxy** - An optional HTTPS proxy.
* **Tag values** - Enter the tag values separated by a semicolon (;).

## Required Permissions

The values supplied in [**AWS Access Key ID** and **AWS Access Key Secret**](#parameters) or the attached IAM role account must have the proper permissions to add tags to resources.

The required permissions are:

* tag:GetResources
* tag:TagResources
* tag:UntagResources
* tag:getTagKeys
* tag:getTagValues
* iam:ListUserTags
* iam:TagUser
* iam:UntagUser

These permissions must be added to a policy attached to relevant IAM user account.
For details on creating an IAM user and attaching policies, see [Connecting the Amazon Web Services (AWS) Adapter](/docs/connecting-aws-adapter-using-iam-user).

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).