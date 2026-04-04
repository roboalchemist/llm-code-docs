# Source: https://docs.asapp.com/reporting/send-s3.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Transmitting Data via S3

S3 supports ongoing data transmissions, though you can also use it for one-time transfers where needed. ASAPP customers can transmit the following types of data to S3:

* Call center data attributes
* Conversation transcripts from messaging or voice interactions
* Recorded call audio files
* Sales records with attribution metadata

## Getting Started

### Your Target S3 Buckets

ASAPP will provide you with a set of S3 buckets to which you may securely upload your data files, as well as a dedicated set of credentials authorized to write to those buckets. See the next section for more on those credentials.

For clarity, ASAPP name buckets use the following convention:

`s3://asapp-\{env\}-\{company_name\}-imports-\{aws-region\}`

<table class="informaltable frame-void rules-rows">
  <thead>
    <tr>
      <th class="th leftcol"><p>Key</p></th>
      <th class="th leftcol"><p>Description</p></th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td class="td leftcol"><p>env</p></td>
      <td class="td leftcol"><p>Environment (prod, pre\_prod, test)</p></td>
    </tr>

    <tr>
      <td class="td leftcol"><p>company\_name</p></td>

      <td class="td leftcol">
        <p>The company name: acme, duff, stark\_industries, etc.</p>
        <p><strong>Note:</strong> company name should not have spaces within.</p>
      </td>
    </tr>

    <tr>
      <td class="td leftcol"><p>aws-region</p></td>

      <td class="td leftcol">
        <p>us-east-1</p>
        <p><strong>Note:</strong> this is the current region supported for your ASAPP instance.</p>
      </td>
    </tr>
  </tbody>
</table>

So, for example, an S3 bucket set up to receive pre-production data from ACME would be named:

`s3://asapp-pre_prod-acme-imports-us-east-1`

#### S3 Target for Historical Transcripts

ASAPP has a distinct target location for sending historical transcripts for AI Services and will provide an exclusive access folder to which transcripts should be uploaded. The S3 bucket location follows this naming convention:

`asapp-customers-sftp-\{env\}-\{aws-region\}`

Values for `env` and `aws-region` are set in the same way as above. As an example, an S3 bucket to receive transcripts for use in production is named:

`asapp-customers-sftp-prod-us-east-1`

<Note>
  See the [Historical Transcript File Structure](/reporting/send-s3#historical-transcript-file-structure "Historical Transcript File Structure") section more information on how to format transcript files for transmission.
</Note>

### Encryption

ASAPP ensures that TLS/SSL encrypts the data you write to your dedicated S3 buckets in transit and AES256 encrypts it at rest.

### Your Dedicated Export AWS Credentials

ASAPP will provide you with a set of AWS credentials that allow you to securely upload data to your designated S3 buckets. (Since you need write access in order to upload data to S3, you'll need to use a different set of credentials than the read-only credentials you might already have.)

In order for ASAPP to securely send credentials to you, you must provide ASAPP with a public GPG key that we can use to encrypt a file containing those credentials.

<Note>
  GitHub provides one of many good available  tutorials on GPG key generation here: [https://help.github.com/en/articles/generating-a-new-gpg-key](https://help.github.com/en/articles/generating-a-new-gpg-key) .
</Note>

It's safe to send your public GPG key to ASAPP using any available channel. Please do NOT provide ASAPP with your private key.

Once you've provided ASAPP with your public GPG key, we'll forward to you an expiring https link pointing to an S3-hosted file containing credentials that have permissions to write to your dedicated S3 target buckets.

<Caution>
  ASAPP's standard practice is to have these links expire after 24 hours.
</Caution>

The file itself will be encrypted using your public GPG key. Once you decrypt the provided file using your private GPG key, your credentials will be contained within a tab delimited file with the following structure:

`id     secret      bucket     sub-folder (if any)`

## Data File Formatting and Preparation

**General Requirements:**

* Encode files in UTF-8.
* Escape control characters.
* You may provide files as CSV or JSONL format, but we strongly recommend JSONL where possible. (CSV files are just too fragile.)
* If you send a CSV file, ASAPP recommends that you include a header. Otherwise, your CSV must provide columns in the exact order listed below.
* When providing a CSV file, you must provide an explicit null value (as the unquoted string: `NULL` ) for missing or empty values.

### Call Center Data File Structure

The table below shows the required fields to include in your uploaded call center data.

<table class="informaltable frame-void rules-rows">
  <thead>
    <tr>
      <th class="th leftcol"><p>FIELD NAME</p></th>
      <th class="th leftcol"><p>REQUIRED?</p></th>
      <th class="th leftcol"><p>FORMAT</p></th>
      <th class="th leftcol"><p>EXAMPLE</p></th>
      <th class="th leftcol"><p>NOTES</p></th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td class="td leftcol"><p><strong>customer\_id</strong></p></td>
      <td class="td leftcol"><p>Yes</p></td>
      <td class="td leftcol"><p>String</p></td>
      <td class="td leftcol"><p>347bdddb-d3a1-45fc-bbcd-dbd3a175fc1c</p></td>
      <td class="td leftcol"><p>External User ID. This is a hashed version of the client ID.</p></td>
    </tr>

    <tr>
      <td class="td leftcol"><p><strong>conversation\_id</strong></p></td>
      <td class="td leftcol"><p>No</p></td>
      <td class="td leftcol"><p>String</p></td>
      <td class="td leftcol"><p>21352352</p></td>
      <td class="td leftcol"><p>If filled in, should map to ASAPP's system.  May be empty, if the customer has not had a conversation with ASAPP.</p></td>
    </tr>

    <tr>
      <td class="td leftcol"><p><strong>call\_start</strong></p></td>
      <td class="td leftcol"><p>Yes</p></td>
      <td class="td leftcol"><p>Timestamp</p></td>
      <td class="td leftcol"><p>2020-01-03T20:02:13Z</p></td>
      <td class="td leftcol"><p>ISO 8601 formatted UTC timestamp.  Time/date call is received by the system.</p></td>
    </tr>

    <tr>
      <td class="td leftcol"><p><strong>call\_end</strong></p></td>
      <td class="td leftcol"><p>Yes</p></td>
      <td class="td leftcol"><p>Timestamp</p></td>
      <td class="td leftcol"><p>2020-01-03T20:02:13Z</p></td>

      <td class="td leftcol">
        <p>ISO 8601 formatted UTC timestamp.  Time/date call ends.</p>
        <p><strong>Note:</strong> duration of call should be Call End - Call Start.</p>
      </td>
    </tr>

    <tr>
      <td class="td leftcol"><p><strong>call\_assigned\_to\_agent</strong></p></td>
      <td class="td leftcol"><p>No</p></td>
      <td class="td leftcol"><p>Timestamp</p></td>
      <td class="td leftcol"><p>2020-01-03T20:02:13Z</p></td>
      <td class="td leftcol"><p>ISO 8601 formatted UTC timestamp. The date/time the call was answered by the agent.</p></td>
    </tr>

    <tr>
      <td class="td leftcol"><p><strong>customer\_type</strong></p></td>
      <td class="td leftcol"><p>No</p></td>
      <td class="td leftcol"><p>String</p></td>
      <td class="td leftcol"><p>Wireless Premier</p></td>
      <td class="td leftcol"><p>Customer account classification by client.</p></td>
    </tr>

    <tr>
      <td class="td leftcol"><p><strong>survey\_offered</strong></p></td>
      <td class="td leftcol"><p>No</p></td>
      <td class="td leftcol"><p>Bool</p></td>
      <td class="td leftcol"><p>true/false</p></td>
      <td class="td leftcol"><p>Whether a survey was offered or not.</p></td>
    </tr>

    <tr>
      <td class="td leftcol"><p><strong>survey\_taken</strong></p></td>
      <td class="td leftcol"><p>No</p></td>
      <td class="td leftcol"><p>Bool</p></td>
      <td class="td leftcol"><p>true/false</p></td>
      <td class="td leftcol"><p>When a survey was offered, whether it was completed or not.</p></td>
    </tr>

    <tr>
      <td class="td leftcol"><p><strong>survey\_answer</strong></p></td>
      <td class="td leftcol"><p>No</p></td>
      <td class="td leftcol"><p>String</p></td>

      <td class="td leftcol" />

      <td class="td leftcol"><p>Survey answer</p></td>
    </tr>

    <tr>
      <td class="td leftcol"><p><strong>toll\_free\_number</strong></p></td>
      <td class="td leftcol"><p>No</p></td>
      <td class="td leftcol"><p>String</p></td>
      <td class="td leftcol"><p>888-929-1467</p></td>

      <td class="td leftcol">
        <p>Client phone number (toll free number) used to call in that allows for tracking different numbers, particularly ones referred directly by SRS.</p>
        <p>If websource or click to call, the web campaign is passed instead of TFN.</p>
      </td>
    </tr>

    <tr>
      <td class="td leftcol"><p><strong>ivr\_intent</strong></p></td>
      <td class="td leftcol"><p>No</p></td>
      <td class="td leftcol"><p>String</p></td>
      <td class="td leftcol"><p>Power Outage</p></td>
      <td class="td leftcol"><p>Phone pathing logic for routing to the appropriate agent group or providing self-service resolution. Could be multiple values.</p></td>
    </tr>

    <tr>
      <td class="td leftcol"><p><strong>ivr\_resolved</strong></p></td>
      <td class="td leftcol"><p>No</p></td>
      <td class="td leftcol"><p>Bool</p></td>
      <td class="td leftcol"><p>true/false</p></td>
      <td class="td leftcol"><p>Caller triggered a self-service response from the IVR and then disconnected.</p></td>
    </tr>

    <tr>
      <td class="td leftcol"><p><strong>ivr\_abandoned</strong></p></td>
      <td class="td leftcol"><p>No</p></td>
      <td class="td leftcol"><p>Bool</p></td>
      <td class="td leftcol"><p>true/false</p></td>
      <td class="td leftcol"><p>Caller disconnected without receiving a self-service response from IVR nor being placed in live agent queue.</p></td>
    </tr>

    <tr>
      <td class="td leftcol"><p><strong>agent\_queue\_assigned</strong></p></td>
      <td class="td leftcol"><p>No</p></td>
      <td class="td leftcol"><p>String</p></td>
      <td class="td leftcol"><p>Wireless Sales</p></td>
      <td class="td leftcol"><p>Agent group/agent skill group (aka queue name)</p></td>
    </tr>

    <tr>
      <td class="td leftcol"><p><strong>time\_in\_queue</strong></p></td>
      <td class="td leftcol"><p>No</p></td>
      <td class="td leftcol"><p>Integer</p></td>
      <td class="td leftcol"><p>600</p></td>
      <td class="td leftcol"><p>Seconds caller waits in queue to be assigned to an agent.</p></td>
    </tr>

    <tr>
      <td class="td leftcol"><p><strong>queue\_abandoned</strong></p></td>
      <td class="td leftcol"><p>No</p></td>
      <td class="td leftcol"><p>Bool</p></td>
      <td class="td leftcol"><p>true/false</p></td>
      <td class="td leftcol"><p>Caller disconnected after being assigned to a live agent queue but before being assigned to an agent.</p></td>
    </tr>

    <tr>
      <td class="td leftcol"><p><strong>call\_handle\_time</strong></p></td>
      <td class="td leftcol"><p>No</p></td>
      <td class="td leftcol"><p>Integer</p></td>
      <td class="td leftcol"><p>650</p></td>
      <td class="td leftcol"><p>Call duration in seconds from call assignment event to call disconnect event.</p></td>
    </tr>

    <tr>
      <td class="td leftcol"><p><strong>call\_wrap\_time</strong></p></td>
      <td class="td leftcol"><p>No</p></td>
      <td class="td leftcol"><p>Integer</p></td>
      <td class="td leftcol"><p>30</p></td>
      <td class="td leftcol"><p>Duration in seconds from call disconnect event to end of agent wrap event.</p></td>
    </tr>

    <tr>
      <td class="td leftcol"><p><strong>transfer</strong></p></td>
      <td class="td leftcol"><p>No</p></td>
      <td class="td leftcol"><p>String</p></td>
      <td class="td leftcol"><p>Sales Group</p></td>
      <td class="td leftcol"><p>Agent queue name if call was transferred. NA or Null value for calls not transferred.</p></td>
    </tr>

    <tr>
      <td class="td leftcol"><p><strong>disposition\_category</strong></p></td>
      <td class="td leftcol"><p>No</p></td>
      <td class="td leftcol"><p>String</p></td>
      <td class="td leftcol"><p>Change plan</p></td>
      <td class="td leftcol"><p>Categorical outcome selection from agent. Alternatively, could be category like 'Resolved', 'Unresolved', 'Transferred', 'Referred'.</p></td>
    </tr>

    <tr>
      <td class="td leftcol"><p><strong>disposition\_notes</strong></p></td>
      <td class="td leftcol"><p>No</p></td>
      <td class="td leftcol"><p>String</p></td>

      <td class="td leftcol" />

      <td class="td leftcol"><p>Notes from agent regarding the disposition of the call.</p></td>
    </tr>

    <tr>
      <td class="td leftcol"><p><strong>transaction\_completed</strong></p></td>
      <td class="td leftcol"><p>No</p></td>
      <td class="td leftcol"><p>String</p></td>
      <td class="td leftcol"><p>Upgrade Completed, Payment Processed</p></td>
      <td class="td leftcol"><p>Name of transaction type completed by call agent on behalf of customer. Could contain multiple delimited values. May not be available for all agents.</p></td>
    </tr>

    <tr>
      <td class="td leftcol"><p><strong>caller\_account\_value</strong></p></td>
      <td class="td leftcol"><p>No</p></td>
      <td class="td leftcol"><p>Decimal</p></td>
      <td class="td leftcol"><p>129.45</p></td>
      <td class="td leftcol"><p>Current account value of customer.</p></td>
    </tr>
  </tbody>
</table>

### Historical Transcript File Structure

ASAPP accepts uploads for historical conversation transcripts for both voice calls and chats.

The fields described below must be the columns in your uploaded .CSV table.

Each row in the uploaded .CSV table should correspond to one sent message.

| FIELD NAME                   | REQUIRED? | FORMAT    | EXAMPLE                          | NOTES                                             |
| :--------------------------- | :-------- | :-------- | :------------------------------- | :------------------------------------------------ |
| **conversation\_externalId** | Yes       | String    | 3245556677                       | Unique identifier for the conversation            |
| **sender\_externalId**       | Yes       | String    | 6433421                          | Unique identifier for the sender of the message   |
| **sender\_role**             | Yes       | String    | agent                            | Supported values are 'agent', 'customer' or 'bot' |
| **text**                     | Yes       | String    | Happy to help, one moment please | Message from sender                               |
| **timestamp**                | Yes       | Timestamp | 2022-03-16T18:42:24.488424Z      | ISO 8601 formatted UTC timestamp                  |

<Note>
  Proper transcript formatting and sampling ensures data is usable for model training. Please ensure transcripts conform to the following:

  **Formatting**

  * Each utterance is clearly demarcated and sent by one identified sender
  * Utterances are in chronological order and complete, from beginning to very end of the conversation
  * Where possible, transcripts include the full content of the conversation rather than an abbreviated version. For example, in a digital messaging conversation:

  <table class="informaltable frame-void rules-rows">
    <thead>
      <tr>
        <th class="th"><p>Full</p></th>
        <th class="th"><p>Abbreviated</p></th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td class="td">
          <p><strong>Agent</strong>: Choose an option from the list below</p>
          <p><strong>Agent</strong>: (A) 1-way ticket (B) 2-way ticket (C) None of the above</p>
          <p><strong>Customer</strong>: (A) 1-way ticket</p>
        </td>

        <td class="td">
          <p><strong>Agent</strong>: Choose an option from the list below</p>
          <p><strong>Customer</strong>: (A)</p>
        </td>
      </tr>
    </tbody>
  </table>

  **Sampling**

  * Transcripts are from a wide range of dates to avoid seasonality effects; random sampling over a 12-month period is recommended
  * Transcripts mimic the production conversations on which models will be used - same types of participants, same channel (voice, messaging), same business unit
  * There are no duplicate transcripts
</Note>

**Transmitting Transcripts to S3**

Historical transcripts are sent to a distinct S3 target separate from other data imports.

<Note>
  Please refer to the [S3 Target for Historical Transcripts](/reporting/send-s3#your-target-s3-buckets "Your Target S3 Buckets") section for details.
</Note>

### Sales Methods & Attribution Data File Structure

The table below shows the required fields to be included in your uploaded sales methods and attribution data.

| FIELD NAME                        | REQUIRED? | FORMAT    | EXAMPLE                               | NOTES                                                                                                                                                                                                                    |
| :-------------------------------- | :-------- | :-------- | :------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **transaction\_id**               | Yes       | String    | 1d71dce2-a50c-11ea-bb37-0242ac130002  | An identifier which is unique within the customer system to track this transaction.                                                                                                                                      |
| **transaction\_time**             | Yes       | Timestamp | 2007-04-05T14:30:05.123Z              | ISO 8601 formatted UTC timestamp. Details potential duplicates and also attribute to the right period of time                                                                                                            |
| **transaction\_value\_one\_time** | No        | Float     | 65.25                                 | Single value of initial purchase.                                                                                                                                                                                        |
| **transaction\_value\_recurring** | No        | Float     | 7.95                                  | Recurring value of subscription purchase.                                                                                                                                                                                |
| **customer\_category**            | No        | String    | US                                    | Custom category value per client.                                                                                                                                                                                        |
| **customer\_subcategory**         | No        | String    | wireless                              | Custom subcategory value per client.                                                                                                                                                                                     |
| **external\_customer\_id**        | No        | String    | 34762720001                           | External User ID. This is hashed version of the client ID. In order to attribute to ASAPP metadata, one of these will be required (Customer ID or Conversation ID)                                                       |
| **issue\_id**                     | No        | String    | 1E10412200CC60EEABBF32                | IF filled in, should map to ASAPP's system. May be empty, if the customer has not had a conversation with ASAPP. In order to attribute to ASAPP metadata, one of these will be required (Customer ID or Conversation ID) |
| **external\_session\_id**         | Yes       | String    | 1a09ff6d-3d07-45dc-8fa9-4936bfc4e3e5  | External session id so we can track a customer                                                                                                                                                                           |
| **product\_category**             | No        | String    | Wireless Internet                     | Category of product purchased.                                                                                                                                                                                           |
| **product\_subcategory**          | No        | String    | Broadband                             | Subcategory of product purchased.                                                                                                                                                                                        |
| **product\_name**                 | No        | String    | Broadband Gold Package                | The name of the product.                                                                                                                                                                                                 |
| **product\_id**                   | No        | String    | WI-BBGP                               | The identifier of the product.                                                                                                                                                                                           |
| **product\_quantity**             | Yes       | Integer   | 1                                     | A number indicating the quantity of the product purchased.                                                                                                                                                               |
| **product\_value\_one\_time**     | No        | Float     | 60.00                                 | Value of the product for one time purchase.                                                                                                                                                                              |
| **product\_value\_recurring**     | No        | Float     | 55.00                                 | Value of the product for recurring purchase.                                                                                                                                                                             |

## Uploading Data to S3

At a high level, uploading your data is a three step process:

1. Build and format your files for upload, as detailed above.
2. Construct a "target path" for those files following the convention in the section "Constructing your Target Path" below.
3. Signal the completion of your upload by writing an empty \_SUCCESS file to your "target path", as described in the section "Signaling that your upload is complete" below.

### Constructing your target path

ASAPP's automation will use the S3 filename of your upload when deciding how to process your data file, where the filename is formatted as follows:

`s3://BUCKET_NAME/FEED_NAME/version=VERSION_NUMBER/format=FORMAT_NAME/dt=DATE/hr=HOUR/mi=MINUTE/DATAFILE_NAME(S)`

The following table details the convention that ASAPP follows when handling uploads:

### Signaling that Your Upload Is Complete

Upon completing a data upload, you must upload an EMPTY file named \_SUCCESS to the same path as your uploaded file, as a flag that indicates your data upload is complete. Until this file is uploaded, ASAPP will assume that the upload is in progress and will not import the associated data file.

As an example, let's say you're uploading one day of call center data in a set of files.

### Incremental and Snapshot Modes

You may provide data to ASAPP as either Incremental or Snapshot data. The value you provide us in the `format` field discussed above, tells ASAPP whether to treat the data you provide as Incremental or Snapshot data.

When importing data using **Incremental** mode, ASAPP will **append** the given data to the existing data imported for that `FEED_NAME`. When you specify **Incremental** mode, you are telling ASAPP that for a given date, the data which was uploaded is for that day only.  If you use the value `dt=2018-09-02` in your constricted filename, you are indicating that the data contained in that file includes records from `2018-09-02 00:00:00 UTC` → `2018-09-02 23:59:59 UTC`.

When importing data using **Snapshot** mode, ASAPP will **replace** any existing data for the indicated `FEED_NAME` with the contents of the uploaded file. When you specify **Snapshot** mode, ASAPP treats the uploaded data as a complete record from "the time history started" until that particular day end.  A date of `2018-09-02` means the data includes, effectively, all things from `1970-01-01 00:00:00 UTC` → `2018-09-02 23:59:59 UTC`.

### Other Upload Notes and Tips

1. Make sure the structure for the imported file (whether columnar or json formatted) matches the current import standards (see below for details)
2. Data imports are scheduled daily, 4 hours after UTC midnight (for the previous day's data)
3. In the event that you upload historical data (i.e., from older dates than are currently in the system), please inform your ASAPP team so a complete re-import can be scheduled.
4. Snapshot data must go into a format=snapshot\_\{type} folder.
5. Providing a Snapshot allows you to provide all historical data at once.  In effect, this reloads the entire table rather than appending data as in the non-snapshot case.

### Upload Example

The example below assumes a shell terminal with python 2.7+ installed.

```json  theme={null}
# install aws cli (assumes python)
pip install awscli
# configure your S3 credentials if not already done
aws configure
# push the files for 2019-01-20 for the call_center_issues import
# for a company named `umbrella-corp` to your local drive in production
aws s3 cp /location/of/your/file.csv s3://asapp-prod-umbrella-corp-imports-us-east-1/call_center_issues/version=1/format=csv/dt=2019-01-20/
aws s3 cp _SUCCESS s3://asapp-prod-umbrella-corp-imports-us-east-1/call_center_issues/version=1/format=csv/dt=2019-01-20/
# you should see some files now in the s3 location
aws s3 ls s3://asapp-prod-umbrella-corp-imports-us-east-1/call_center_issues/version=1/format=csv/dt=2019-01-20/
    file.csv
    _SUCCESS
```
