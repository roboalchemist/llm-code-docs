# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/snowflake-bulk-loader.md

# Snowflake Bulk Loader

Use the Snowflake Bulk Loader step in your transformation to bulk-load data to Snowflake. This is different from the Table Output step in that this allows you to bulk load the data as opposed to loading it row-by-row. This can result in significantly better performance.

## Prerequisites

You must have the following information in order to connect to your Snowflake instance:

1. **Location of the source S3 bucket or Internal Staging Area and file**. Note that your Snowflake instance must also have access to this location in order to access the files / objects that will be loaded. The following (input) file formats are supported:

   1. Delimited
   2. Avro
   3. JSON
   4. ORC
   5. Parquet
   6. XML

   You will need to setup a VFS connection to the S3 bucket to Internal Staging area. See \<link> for further details
2. I**P / Domain, Port, Private Key File / Password** for the target Snowflake Database. You will need to setup a connection to the target Snowflake Database (see \<link> for further details on how to setup a Snowflake connection)
3. **Schema and Table name** in the target Snowflake Database to which the data will be uploaded

## Using the Step

Once you have the step on main canvas, double click on the step. This will open a dialog to configure the step details.

{% stepper %}
{% step %}

#### Specify Step Name

Specify the **unique name of the step** on the canvas. You can customize the name or leave it as the default.

<figure><img src="https://773338310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYwnJ6Fexn4LZwKRHghPK%2Fuploads%2Fpw9uEDayyyBGcfWl2iJY%2Fimage.png?alt=media&#x26;token=64bd52a8-b955-4a9b-979c-d800410853ff" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

#### Specify Input Source

Specify the following:

1. **Source Type**: S3 or Snowflake Staging Area
2. **S3 location or Snowflake Staging Area & file** from which the data will be loaded (should be known as laid out in the *Prerequisites* above)
3. **File type** (see *Prerequisites* for supported file types)&#x20;
4. **Compression type** of the source file

<figure><img src="https://773338310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYwnJ6Fexn4LZwKRHghPK%2Fuploads%2FQ00o5zeAGv3jgRB7k3Rk%2Fimage.png?alt=media&#x26;token=52f67900-61d7-4ed4-9a5f-a958891a4128" alt=""><figcaption></figcaption></figure>

If you choose file type as "**Delimited**" or "**JSON**" or "**XML**", then you will need to provide additional information as shown in the image below

<figure><img src="https://773338310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYwnJ6Fexn4LZwKRHghPK%2Fuploads%2F6GHU68KCnrLLlBPtxJHw%2Fimage.png?alt=media&#x26;token=84408918-6146-4e5c-9a81-3dc615605232" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

#### Specify Output Target

You will need to specify the target database **Connection, Schema, and Table** here. These should all be established / known as laid out in the *Prerequisites* above. You can also create a new Snowflake connection here (by clicking on New). You will need to follow the same instructions as specified in *Prerequisites* above.

<figure><img src="https://773338310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYwnJ6Fexn4LZwKRHghPK%2Fuploads%2FjqplSEITVyYVMQjZdw8B%2Fimage.png?alt=media&#x26;token=32286f69-5040-4f60-aca8-a6342b6f6c05" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

#### Specify Options / Advanced Options

Specify the following:

1. Whether you need the target Table truncated before the load starts
2. What action to take on encountering errors
3. Advanced options (see Copy Options under <https://docs.snowflake.com/en/sql-reference/sql/copy-into-table>)
   {% endstep %}
   {% endstepper %}

## Metadata Injection Support

All fields of this step support metadata injection. You can use this step with [ETL metadata injection](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/etl-metadata-injection) to pass metadata to your transformation at runtime.
