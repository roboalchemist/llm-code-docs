# Source: https://docs.axonius.com/docs/aws-advanced-configuration-file.md

# AWS Advanced Configuration File

The [Advanced Configuration File](/docs/aws-parameters) field lets you upload an advanced configuration JSON file. The file can be empty (`{}`) or can contain any combination of the following key/value pairs in a JSON format.

* If supplied, when connecting to the source, Axonius will consider the configuration in the uploaded file in addition to the values specified in the various fields of the connection for this adapter.
* If not supplied, when connecting to the source, Axonius will only consider the values specified in the various fields of the connection for this adapter.

***

### Skip Verification

**Key/Value Pair**

```json
{
  "skip_ec2_verification": true
}
```

**Using the JSON file**
By default, the specified IAM user / roles of the connection for this adapter must have at least EC2 permissions.
If the file contains this key/value pair, Axonius skips the EC2 permissions verifications.
As a result, the connection for this adapter will be considered valid even if the specified connection parameters are correct, but the specified IAM user / roles do not have EC2 permissions.

***

### Authenticate with MFA

The attached file contains the procedure of how to get the information needed to set up the MFA portion of the AWS adapter.

<HTMLBlock>
  {`
  <iframe
    src="https://docs.google.com/gview?embedded=true&url=https://raw.githubusercontent.com/Axonius/ax-docs-pub/main/Files/AWS%20Adapter%20MFA%20Procedure.pdf"
    width="100%"
    height="720"
    style="border:1px solid #e5e7eb;border-radius:8px;"
  ></iframe>
  `}
</HTMLBlock>

<br />

<br />

**Key/Value Pair**

```json
{
  "aws_mfa_serial_number": "arn:aws:iam::mfa/<name>",
  "aws_mfa_totp_code": ""
}
```

**Using the JSON file**
AWS allows creating policies that require MFA to access some APIs. If those two key/value pairs exist, Axonius will use the values to try to authenticate the user with MFA.

The MFA settings can be configured and viewed from the IAM entity, under the **Security Credentials** tab.

* **"aws\_mfa\_serial\_number":** `arn:aws:iam::mfa/&lt;name&gt;` — replace with the virtual MFA device name.
* **aws\_mfa\_totp\_code** — The virtual MFA device secret key.

***

### Remote Roles to Assume

**Key/Value Pair**

```json
{
  "remote_roles_to_assume": [
    {
      "service": "S3",
      "bucket_name": "",
      "key_name": "",
      "region": ""
    }
  ]
}
```

**Using the JSON file**
The assumed role path location will be located at: `s3:///<bucket>/<key>`.
This file uses the exact same conventions as the “Roles to assume” field in the adapter configuration dialog.
The roles to assume can be either a comma-separated string of roles or a JSON list of dictionaries.

**Note:** More than one entry in the `remote_roles_to_assume` section of the advanced config can be specified.
**Note:** You cannot populate both the advanced config **and** the “Roles to assume” in the adapter configuration dialog.

***

### Roles for Account Name

**Key/Value Pair**

```json
{
  "roles_for_account_name": [
    {
      "role_arn": "arn:aws:iam::111111111111:role/Axonius-Adapter",
      "role_arn": "arn:aws:iam::222222222222:role/Axonius-Adapter"
    }
  ],
  "skip_ec2_verification": true
}
```

**Using the JSON file**
Adds the “Account name” to the AWS Organization data that is populated in every AWS device and user.
Each IAM Role in this advanced configuration is used to query an individual AWS Organization.
In case there are multiple AWS Organizations, each should be populated as an individual `role_arn` entry.

<Callout icon="📘" theme="info">
  Note:

  <ul>
    <li>It is highly recommended that <code>skip\_ec2\_verification</code> is set to true, since per AWS Best Practices, only IAM resources should be present in the root organization account, and this is the account that we will query to fetch the organization account name.</li>
    <li>This feature requires the <strong>organizations:ListAccounts IAM</strong> permission for the roles that will be inherited.</li>
  </ul>
</Callout>

***

### Fetch Roles from Organization

**Key/Value Pair**

```json
{
  "fetch_roles_from_organization": {
    "organization_role_for_discovery": "arn:aws:iam::111111111111:role/Axonius-Adapter",
    "role_name": "",
    "role_path": "",
    "external_id": "",
    "region": "",
    "excluded_accounts": ["123456789001", "123456789002", "123456789003"]
  },
  "skip_ec2_verification": true
}
```

**Using the JSON file**
This feature allows the user to set a role in the advanced configuration that allows Axonius to discover all member accounts in an AWS Organization.
Axonius can then assume roles in each of these member accounts in order to perform asset discovery using a single adapter connection.
The adapter will query the AWS Organization API to find all member accounts.
The role ARN specified in `organization_role_for_discovery` will be assumed by the IAM user, and we will use this role to perform `organizations:listaccounts`.

The role specified in `role_name` will then be assumed by the IAM user in all member accounts.
Note that the role names to assume in the member account must be consistent in all accounts, otherwise Axonius will not have access to that member account.
`role_path` is optional. `region` is optional; if not input, the default value is `us-east-1`.

**Note:** It is recommended that `skip_ec2_verification` is set to true when the user account configured in the adapter connection has no IAM rights other than `sts:AssumeRole`.
If the user account has no resources in the root account, this must be set in the advanced config.
If this is not set, or if the rights to query for EC2 are not granted to the role, the adapter will fail completely.

**Note:** This feature requires the following IAM permissions for the role(s) that will be inherited:

* `organizations:ListAccounts`
* `sts:AssumeRole`

**Fetch only OU Specific accounts (optional settings)**

* `ou_id_to_fetch_from` - Use this setting to fetch only accounts that are hierarchically under the specific OU (instead of the entire organization).
  The syntax is:

  ```json
  "ou_id_to_fetch_from": ["ou-aaaa-aaaa", "ou-bbbb-bbbb"]
  ```

  The following permissions are required for the organization role when you use this:

  * `organizations:ListAccountsForParent`
  * `organizations:ListChildren`
* `ou_id_to_exclude` - Use this setting to exclude accounts with specific OUs from fetch.
  The syntax is:

  ```json
  "ou_id_to_exclude": ["ou-aaaa-aaaa", "ou-bbbb-bbbb"]
  ```

  * If you provide an OU to exclude, but there is no `ou_id_to_fetch_from` to fetch from, it will get all accounts and try to exclude accounts that are children of the excluded OU in `ou_id_to_exclude`.

***

**Common Role Name**

The `role_name` is the name of the role that must be present in all member accounts and the role that will be used for the normal device and user discovery by Axonius.
This role should have all of the normal permissions for the adapter.

**Role Path**

If your IAM strategy uses special paths for IAM roles, that path should be entered here.
In most AWS deployments, this field will be left empty.

***

### Tag Allow/Block List for Fetching Devices

**Key/Value Pair**

```json
{
  "tags_to_match": {
    "tags": [
      {
        "Key": "First Key",
        "Value": "First Value"
      },
      {
        "Key": "Second Key",
        "Value": "Second Value"
      }
    ],
    "include_device": true
  }
}
```

**Using the JSON file**
Use this configuration to set an allow list of AWS tags or an exclude list of AWS tags.
Add a list of tags to an adapter connection and Axonius will either fetch **only** devices that have the tags, or **not** fetch devices that have these tags.

Set the parameters as follows:

* **tags\_to\_match** - the name of the advanced configuration file section for this feature.
* **tags** - a list of dictionaries that define a dictionary key and a dictionary value to search for.
* Set **include\_device** to `true` to include only those EC2 devices that match one or more tags from the tags section.
  Set to `false` to remove EC2 devices that match one or more of the tags from the **tags** section.