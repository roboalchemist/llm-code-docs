# Source: https://docs.axonius.com/docs/send-csv-to-amazon-s3.md

# AWS - Send CSV to S3

**AWS - Send CSV to S3** creates a CSV file that includes the assets returned by the selected query or assets selected on the relevant asset page and sends it to a specific Amazon Simple Storage Service (Amazon S3) bucket.

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

      * The user name and the password used for the adapter connection must have the [Required Permissions](#required-permissions) to install software on assets.
    </Callout>

* **Amazon S3 bucket name** - Specify the Amazon S3 bucket name for which the file will be sent.
  For creating, configuring, and access Amazon S3 buckets, see [Configuring an S3 Bucket to use with Axonius](/docs/configuring-an-s3-bucket-to-use-with-axonius).

* **Export Method** - Select an export method from the list. The file name must have the correct file extension at the end of file name:
  * CSV = .csv
  * Excel = .xlsx
  * Parquet = .parquet

## Additional Fields

These fields are optional.

<Callout icon="🚧" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **AWS Access Key ID** and **AWS Access Key Secret** - The credentials of your AWS account.
  * **Use attached IAM role** - When selected, Axonius uses the specified user credentials to perform the Amazon S3 PutObject operation.
    * If not supplied, Axonius will use the attached IAM role of the EC2 instance Axonius is installed on, instead of using the AWS Access Key ID and AWS Access Key Secret credentials supplied.

  The IAM user must have an attached policy that allows the Amazon S3 PutObject operation, for example:

  <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(502).png" />

  For details about creating an IAM user, see [Connecting Amazon Web Services (AWS) Adapter](/docs/amazon-web-services-aws#connecting-the-amazon-web-services-aws-adapter) or [Creating an IAM User in Your AWS Account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) in AWS online help.

  * **AWS region** *(default: us-east-1)* - Specify the region name the Amazon S3 located.
    * If supplied, PutObject operation will be done on the supplied Amazon S3 details in the supplied region.
    * If not supplied, PutObject operation will be done on the supplied Amazon S3 details in 'us-east-1'.

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **External Role ARN** *(for Axonius-Hosted users only, and for both CloudFormation/Organizations connections)* - Enter your External Role ARN using the following format: `arn:aws:iam::[AWSLaunchAccountID]:role/[AccessName]`.

  * **Entry Point External ID** *(for Axonius-Hosted users only, and for both CloudFormation/Organizations connections)* - Copy your Customer ID from your Axonius Instance. To find your Customer ID, log into your Axonius instance and navigate to **System Settings** → **About**.

  <Callout icon="📘" theme="info">
    Note

    Use either the [AWS Configuration Advanced File](/docs/aws-advanced-configuration-file) or the connection parameters to specify your `entry_point_external_id` and `entry_point_role_arn`. Note that the data from the Configuration File overpowers the connection parameters.
  </Callout>
</Callout>

* **Amazon S3 object location (key)** *(default: axonius\_csv)* - Specify the S3 object key to store a CSV file that contains the entities derived from the saved query supplied as a trigger (or entities that have been selected in the asset table).
* If supplied, the CSV file path and name will be stored in the specified object key. For example, if *reports/axonius* is specified, the file path and name will be *reports/axonius.csv*.
* If not supplied, the CSV file will be stored as *axonius\_csv.csv*.
* **Append date and time to file name** -
  * If enabled, the date and time (in UTC) of enforcement action execution will be added as a suffix to the generated CSV file name. For example, *axonius\_csv\_2020-01-06-16:48:13.csv*.
  * If disabled, the CSV file will be stored based on the specified/default object key.
* **Overwrite existing file** - Choose to store the generated CSV file even if a CSV file with the same name already exists.
  * If enabled, the generated CSV file will be stored even if a CSV file with the exact name already exists.
  * If disabled, the generated CSV file will be not be stored if a CSV file with the exact name already exists. As a result, the Enforcement action will fail.

The following settings can only be applied when **Export CSV delimiter to use for multi-value fields** field (see below) is left empty:

* **Always export aggregated fields as arrays** - When this option is selected, the aggregated fields in sent Parquet files are represented as proper lists instead of CSV-style strings.

* **Strict Parquet Schema** - Select this option to ensure that, when **Always export aggregated fields as arrays** is selected, the exported data has a fully consistent array structure in all cases. When both settings are enabled, all values in all fields are enforced to be the same type: string, number, bool, timestamp, etc. If not all values are the same type, the output will be an empty array \[ ].

  <Callout icon="📘" theme="info">
    Note

    When one or both of these options are selected, the field *Aggregated: Asset Unique ID*, always appears as a single, unique value, and not as an array. This is due to it being an internal field, representing a unique, single-value identifier.
  </Callout>

<Accordion title="Additional CSV Settings" icon="fa-info-circle">
  - **Split by asset entities** - Select to create a CSV file where each asset on a device is shown as a separate row. This separates each asset as the 'expand' option in the application. It separates each asset by its entity. For example, you will be able to know which values were fetched from each adapter connection. If you do not select this option, all values on a device are in the same cell on the CSV file.
  - **Split by field values**  - Choose field value - For complex fields and lists you can create a CSV file where the values of complex fields and lists are represented as separate rows in the file. From the drop-down box select the value that you want to display in the file, 'Tags' for instance. Only fields that have been discovered are available. For example, if you export by Installed Software, you will be able to see each installed Software name and its version.
  - **Don't split complex objects into columns**  - When selected, complex objects appear in a single column in JSON format. By default, each field in a complex object is split into a separate column in the CSV file.
  - **Export CSV delimiter to use for multi-value fields** \*(default: **Export CSV delimiter to use for multi-value fields** field under the **System Settings** section in the **[UI Settings](https://docs.axonius.com/docs/configuring-user-interface-settings)** - Specify a delimiter to separate between values within the same field of an exported CSV file, otherwise the delimiter defined in **Export CSV delimiter to use for multi-value fields** is used.
  - **Maximum rows** *(default: 1048500)* - Specify the maximum number of rows to be included in the CSV file.  When you set a value here the generated CSV file will include the top x rows, based on the specified values. Otherwise, the generated CSV file will include the default maximum rows, set as 1048500.  (note that this value is the maximum value supported by Excel, setting a higher value generates a file that can't be displayed fully or correctly in Excel)
  - **Include associated devices (only for Aggregated Security Findings and Software)** - For Software and Aggregated Security Findings queries. Toggle on this option to include the associated devices with the preferred hostname as a predefined field for each software or Aggregated Security Finding.   When you create a CSV file with associated devices (for Aggregated Security Findings or Software),  if the exported query results are larger than the value set under Maximum rows (or the default value of 1048500), an appropriate notice is displayed at the end of the CSV file.
    * **Device fields** -  This option is available for Software and Aggregated Security Findings. Select the device fields to add. By default Preferred Host Name is selected. Click add to select more fields. At least one field must be selected. Once you select fields, you can drag and drop to rearrange in the order that you want them to appear in the CSV file. Click the bin icon to remove a device field.
  - **Include Associated fetch events (only for Fetch History)** - For Adapter Fetch History queries, select this option to include details of the associated Fetch Events in the CSV file that is created.
  - **Exclude parent complex objects columns** *(default: Disabled)* - Enable this option to hide the parent field of complex fields in exported files.
</Accordion>

<br />

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).