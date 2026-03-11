# Source: https://docs.axonius.com/docs/aws-parameters.md

# AWS Parameters

1. **Region Names** or **Get All Regions** *(optional)* - Specify one or more comma-separated region names for specific regions. Alternatively, select the **Get All Regions** option to connect to all available regions. See the [List of Supported AWS Regions in Axonius](/docs/aws-parameters#appendix-list-of-supported-aws-regions).
2. **AWS Access Key ID** *(optional)* - Provide AWS Access Key ID or choose to use an EC2 instance attached IAM role.
3. **AWS Access Key Secret** *(optional)* - Provide AWS Access Key Secret or choose to use an EC2 instance attached IAM role.

<Callout icon="📘" theme="info">
  Note

  When you use an instance profile, **AWS Access Key ID** and **AWS Access Key Secret** are not required, and if input are ignored.
</Callout>

4. **Account Tag** *(optional)* - Tag for the EC2 instance ("nickname").
5. **Proxy** *(optional)* - HTTPS proxy to use when connecting to the AWS APIs.
   * If supplied, Axonius will utilize the proxy when connecting to the AWS APIs.
   * If not supplied, Axonius will connect directly to the AWS APIs.
6. **Roles to assume** *(optional)* – A file with role-ARNs which the AWS Adapter will try to assume for cross-account access with the single IAM user. Two available formats:
   * List of comma-delimited role-ARNs
   ```
   arn:aws:iam::111111111111:role/axonius-role, arn:aws:iam::222222222222:role/axonius-role
   ```
   * JSON format - list of dictionaries that define each role.
   * external\_id is only supported in the JSON format
   * The external\_id can be different for every role in the list.
   ```JSON
   [
       {"arn": "arn:aws:iam::111111111111:role/axonius-role"},
       {"arn": "arn:aws:iam::222222222222:role/axonius-role", "external_id": "MY-SECRET"}
   ]
   ```
7. **Use instance profile (attached role)** *(optional)* - Select to use the EC2 instance (Axonius installed on) attached IAM role / instance profile instead of using the **AWS Access Key ID** and **AWS Access Key Secret** credentials supplied.  This does not affect the **Roles to assume** parameter.

<Callout icon="📘" theme="info">
  Note

  When you use the EC2 instance the adapter ignores the **AWS Access Key ID** and **AWS Access Key Secret**
</Callout>

8. **Advanced Configuration File** *(optional)*  - Upload an advanced configuration JSON file. For details, see [AWS Advanced Configuration File](/docs/aws-advanced-configuration-file).
9. For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).
10. **External Role ARN** *(optional; for Axonius-Hosted users only, and for both CloudFormation/Organizations connections)* - Enter your External Role ARN using the following format: `arn:aws:iam::[AWSLaunchAccountID]:role/[AccessName]`.
11. **Entry Point External ID** *(optional; for Axonius-Hosted users only, and for both CloudFormation/Organizations connections)* - Copy your Customer ID from your Axonius Instance. To find your Customer ID, log into your Axonius instance and navigate to **System Settings** → **About**.

<Callout icon="📘" theme="info">
  Note

  Use either the [AWS Configuration Advanced File](/docs/aws-advanced-configuration-file) or the connection parameters to specify your `entry_point_external_id` and `entry_point_role_arn`. Note that the data from the Configuration File overpowers the connection parameters.
</Callout>

![AWSConnectionParameters](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-CSOGHIYM.png)

## Appendix: List of Supported AWS Regions

### Commercial Regions

The following regions are supported in Axoinus by default. These are commercial, out-of-the-box regions.

```
   'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2',
   'ap-south-1', 'ap-northeast-3', 'ap-northeast-2', 'ap-northeast-1',
   'ap-southeast-1', 'ap-southeast-2',
   'ca-central-1',
   'eu-central-1', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'eu-north-1',
   'sa-east-1'
```

<br />

### GovCloud Regions

The following US GovCloud regions are supported

```
GOV_REGION_NAMES: 'us-gov-west-1', 'us-gov-east-1' 
ISO_REGIONS_NAMES 'us-iso-east-1', 'us-iso-west-1', 'us-isob-east-1', 'us-isof-east-1', 'us-isof-south-1' 
```

<br />

### Opt-in Regions

The following regions are **not** supported in Axoinus by default. To activate them, you need to enable them manually. Once you enable them, they also become commercial. For more information, see [Considerations for activating AWS opt-in Regions](https://docs.aws.amazon.com/controltower/latest/userguide/opt-in-region-considerations.html).

```
'ap-east-1', 'ap-southeast-3', 'eu-south-1', 'af-south-1', 'me-south-1', 'il-central-1',
'me-central-1', 'eu-south-2', 'ap-south-2', 'eu-central-2', 'ap-southeast-4', 'ca-west-1'
```