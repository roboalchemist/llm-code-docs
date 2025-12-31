# Source: https://docs.asapp.com/reporting/retrieve-messaging-data.md

# Retrieving Data for ASAPP Messaging

> Learn how to retrieve data from ASAPP Messaging

ASAPP provides secure access to your messaging application data through SFTP (Secure File Transfer Protocol).

The data exported will need to be [deduplicated](#removing-duplicate-data) before importing into your system.

<Note>
  If you're retrieving data from ASAPP's AI Services, use [File Exporter](/reporting/file-exporter) instead.
</Note>

## Download Data via SFTP

To download data from ASAPP via SFTP, you need to:

<Steps>
  <Step title="Generate a SSH key pair">
    You need to generate a SSH key pair and share the public key with ASAPP.

    <Accordion title="Generating a SSH key pair">
      If you don't have one already, you can generate one using the ssh-keygen command.

      ```bash  theme={null}
      ssh-keygen -b 4096
      ```

      This will walk you creating a key pair.
    </Accordion>

    Share your `<keyname>.pub` file with your ASAPP team.
  </Step>

  <Step title="Connect to SFTP server">
    To connect to the SFTP server, you will need to use the following information:

    * Host: `prod-data-sftp.asapp.com`
    * Port: `22`
    * Username: `sftp{company name}`
      <Note>
        If you are unsure what your company name is, please reach out to your ASAPP account team.
      </Note>

    You should not use a password for SSH directly as you will be using the SSH key pair to authenticate.

    <Note>
      If you have a passphrase on your SSH key, you will need to enter it when prompted.
    </Note>
  </Step>

  <Step title="Download data">
    Once connected, you can download or upload files. The folder structure and file names have a naming standard indicating the feed type and time of export, and other relevant information:

    <Tabs>
      <Tab title="Path Structure">
        `/FEED_NAME/version=VERSION_NUMBER/format=FORMAT_NAME/dt=DATE/hr=HOUR/mi=MINUTE/DATAFILE(S)`

        | Path Element    | Description                                                                                                                                       |
        | :-------------- | :------------------------------------------------------------------------------------------------------------------------------------------------ |
        | **FEED\_NAME**  | The name of the table, extract, feed, etc.                                                                                                        |
        | **version**     | The version of the feed at hand. Changes whenever the schema, meaning of a column, etc., changes in a way that could break existing integrations. |
        | **format**      | The format of the exported data. Almost always, this will be JSON Lines.\*                                                                        |
        | **dt**          | The YYYY-MM-DD formatted date corresponding to the exported data.                                                                                 |
        | **hr**          | The hour of the day the data was exported.                                                                                                        |
        | **mi**          | The minute of the hour the data was exported.                                                                                                     |
        | **DATAFILE(s)** | The filename or filenames of the exported feed partition.                                                                                         |

        <Note>
          It is possible to have duplicate entries within a given data feed for a given day. You need to [remove duplicates](#removing-duplicate-data) before importing it.
        </Note>
      </Tab>

      <Tab title="File Naming">
        File names that correspond to an exported feed partition will have names in the following form:

        `\{FEED_NAME\}\{FORMAT\}\{SPLIT_NUMBER\}.\{COMPRESSION\}.\{ENCRYPTION\}`

        | File name element | Description                                                                                                                                                                                                                                                                                                                                                 |
        | :---------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        | **FEED\_NAME**    | The feed name from which this partition is exported.                                                                                                                                                                                                                                                                                                        |
        | **FORMAT**        | .jsonl                                                                                                                                                                                                                                                                                                                                                      |
        | **SPLIT\_NUMBER** | (optional) In the event that a particular partition's export needs to be split across multiple physical files in order to accommodate file size constraints, each split file will be suffixed with a dot followed by a two-digit incrementing sequence. If the whole partition can fit in a single file, no SPLIT\_NUMBER will be present in the file name. |
        | **COMPRESSION**   | (optional) .gz will be appended to the file name if the file is gzip compressed.                                                                                                                                                                                                                                                                            |
        | **ENCRYPTION**    | (optional) In the atypical case where a file written to the SFTP store is doubly encrypted, the filename will have a .enc extension.                                                                                                                                                                                                                        |
      </Tab>
    </Tabs>

    ### Verifying the Data Export is Complete

    New Export files are continuously being generated depending on the feed and the export schedule. You can check the `_SUCCESS` file to verify that the export is complete.

    Upon completing the generating for a particular partition, ASAPP will create an EMPTY file named `_SUCCESS` to the same path as the export file or files. This `_SUCCESS` file acts as a flag indicating that the generation for the associated partition is complete. A `_SUCCESS` file will be written even if there is no available data selected for export for the partition at hand.

    Until the `_SUCCESS` file is created, ASAPP's export is in progress and you should not import the associated data file. You should check for this file before downloading any data partition.

    ### General Data Formatting Notes

    All ASAPP exports are formatted as follows:

    * Files are in [JSON Lines format](http://jsonlines.org/).
    * ASAPP export files are UTF-8 encoded.
    * Control characters are escaped.
    * Files are formatted with Unix-style line endings.
  </Step>
</Steps>

## Removing Duplicate Data

ASAPP continuously generates data, which means newer files may contain updated versions of previously exported records. To ensure you're working with the most up-to-date information, you need to remove duplicate data by keeping only the latest version of each record and discarding older duplicates.

To remove duplicates from the feeds, download the latest instance of a feed, and use the **Unique Conditions** as the "primary key" for that feed.

Each table's unique conditions are listed in the relevant [feed schema](/reporting/asapp-messaging-feeds).

### Example

In order to remove duplicates from the table [`convos_metrics`](/reporting/asapp-messaging-feeds#table-convos-metrics), use this query:

```sql  theme={null}
SELECT *
FROM
    (SELECT
    *,
    ROW_NUMBER() OVER (partition by {{ primary_key }} order by {{ logical_timestamp}} DESC, {{ insertion_timestamp }} DESC) as row_idx
    FROM convos_metrics
    )
WHERE row_idx = 1
```

We partition by the `primary_key` for that table and get the latest data using order by `logical_timestamp`DESC in the subquery. Then we only select where `row_idx` = 1 to only pull the latest information we have for each `issue_id`.

### Schema Adjustments

We will occasionally extend the schema of an existing feed to add new columns. Your system should be able to handle these changes gracefully.

We will communicate any changes to the schema via your ASAPP account team.

You can also enable automated schema evolution detection and identify any changes using `export_docs.yaml`, which is generated each day and sent via the S3 feed. By incorporating this into the workflows, you can maintain a proactive stance, ensuring uninterrupted service and a smooth transition in the event of schema adjustments.

## Export Schema

We publish a [schema for each feed](/reporting/asapp-messaging-feeds). These schemas include the unique conditions for each table that you can use to remove duplicates from your data.

<Note>
  If you are retrieving data from Standalone Services, you need to use [File Exporter](/reporting/file-exporter).
</Note>
