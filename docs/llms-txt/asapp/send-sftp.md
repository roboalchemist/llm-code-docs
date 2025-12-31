# Source: https://docs.asapp.com/reporting/send-sftp.md

# Transmitting Data to SFTP

SFTP is the supported mechanism for **one-time data transmissions**, typically used for sending training data files during the implementation phase prior to initial launch. ASAPP customers can transmit the following types of training data via SFTP:

* Conversation transcripts from messaging or voice interactions
* Recorded call audio files
* Free-text agent notes associated with messaging or voice interactions

## Getting Started

ASAPP will require you to provide the following information to set up the SFTP site.

* An SSH public key.  This should use RSA encryption with a key length of 4096 bits.

ASAPP will provide you a username to associate with the key. This will be of the form: `sftp<company marker>` where the company marker will be selected by ASAPP.  For example a username could be: `sftptestcompany`

In your network, open port 22 outbound to sftp.us-east-1.asapp.com.

## Data File Formatting and Preparation

**General Requirements:**

* Files should be UTF-8 encoded.
* Control characters should be escaped.
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

## Generate SSH Public Key Pair and Upload Files

You can generate the key and upload files via Windows, Mac, or Linux.

### Windows Users

If you are using Windows, follow the steps below:

#### 1. Generate an SSH Key Pair

There are multiple tools that you can use to generate an SSH Key Pair. For example: by using puTTYgen (available from [PuTTY](https://www.putty.org/) ) as shown below.

Choose RSA and 4096 bits, then click **generate** and move the mouse pointer randomly.  When the key is generated, enter `sftp` followed by your company marker as the key comment.

<Frame>
  <img src="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c78294a9-8551-783f-d909-ad56002dcc71.PNG?fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=3800feaa7cc37476f8a2d258adb40ed2" data-og-width="797" width="797" data-og-height="575" height="575" data-path="image/uuid-c78294a9-8551-783f-d909-ad56002dcc71.PNG" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c78294a9-8551-783f-d909-ad56002dcc71.PNG?w=280&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=5153291e961ad38ab6436ee25c2f7a06 280w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c78294a9-8551-783f-d909-ad56002dcc71.PNG?w=560&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=f1df5854002cc0873eb7aa841eb5afec 560w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c78294a9-8551-783f-d909-ad56002dcc71.PNG?w=840&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=b663b33754e212010a2d9d7ca2465d46 840w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c78294a9-8551-783f-d909-ad56002dcc71.PNG?w=1100&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=ab5c7c4ac3a243084a32af0e7e0f34eb 1100w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c78294a9-8551-783f-d909-ad56002dcc71.PNG?w=1650&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=0380f0239197fe4eb25e626645bf6205 1650w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c78294a9-8551-783f-d909-ad56002dcc71.PNG?w=2500&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=40f1813dfb68ed134f70098dc3583b88 2500w" />
</Frame>

#### 2. Provide the Public Key to ASAPP

Save the public and private key.  Only send the public file for your key pair to ASAPP.  This is not a secret and can be emailed.

#### 3. Upload Files

Use an SFTP utility such as Cyberduck (available from [Cyberduck](https://cyberduck.io/) ) to upload files to ASAPP.  Click **Open Connection**, add sftp.us-east-1.asapp.com as the Server,  and add `sftpcompanymarker` as the Username.  Choose the private key you generated in step 2 as the SSH Private Key and click **connect**.  The following screenshots show how to do this using Cyberduck.

<Frame>
  <img src="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-46081ee0-cb13-663d-a3b2-10c7a0b76d40.PNG?fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=62b926b21fa2647d3dff2b4b558b55d1" data-og-width="1285" width="1285" data-og-height="794" height="794" data-path="image/uuid-46081ee0-cb13-663d-a3b2-10c7a0b76d40.PNG" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-46081ee0-cb13-663d-a3b2-10c7a0b76d40.PNG?w=280&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=45dbd93b2167b376a746f8c4e87f8d5f 280w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-46081ee0-cb13-663d-a3b2-10c7a0b76d40.PNG?w=560&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=1f3b94ff23037b2e5fee1e5ede94f52e 560w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-46081ee0-cb13-663d-a3b2-10c7a0b76d40.PNG?w=840&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=8196bb97067dbf57a5978766edb30406 840w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-46081ee0-cb13-663d-a3b2-10c7a0b76d40.PNG?w=1100&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=7d830d03e3948a7874044a6b69445d31 1100w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-46081ee0-cb13-663d-a3b2-10c7a0b76d40.PNG?w=1650&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=3a9ed9fca2c742a68acc959a8f386eed 1650w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-46081ee0-cb13-663d-a3b2-10c7a0b76d40.PNG?w=2500&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=14d5e3bf4996c9d5eb3a49a72408c840 2500w" />
</Frame>

A pop-up window appears. Click to allow the unknown fingerprint.  You will then see the `in` and `out` directories.

<Frame>
  <img src="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-72764c0e-5e59-0831-3148-a5b5fa016b8f.PNG?fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=1805d7ea24c5bdbea866c89bb25bcbc6" data-og-width="1285" width="1285" data-og-height="800" height="800" data-path="image/uuid-72764c0e-5e59-0831-3148-a5b5fa016b8f.PNG" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-72764c0e-5e59-0831-3148-a5b5fa016b8f.PNG?w=280&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=d0b75b97f994f0651b1a4fef61ecdce4 280w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-72764c0e-5e59-0831-3148-a5b5fa016b8f.PNG?w=560&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=ea2b5044011daa24f1d8be664429612b 560w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-72764c0e-5e59-0831-3148-a5b5fa016b8f.PNG?w=840&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=6a7f707c2dffb0ba8a88f18f62a80e42 840w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-72764c0e-5e59-0831-3148-a5b5fa016b8f.PNG?w=1100&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=14f8a9708dbd0ca868cf4080d920ff6b 1100w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-72764c0e-5e59-0831-3148-a5b5fa016b8f.PNG?w=1650&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=ca62f52c3d7c31f6d6f2be60ba97c1a7 1650w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-72764c0e-5e59-0831-3148-a5b5fa016b8f.PNG?w=2500&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=7eccfc8a9b5713d24448777514c3d80e 2500w" />
</Frame>

Double click the `in` directory and click **Upload** to choose files to send to ASAPP.

### Mac/Linux Users

If you are using a Mac or Linux, follow the steps below:

#### 1. Generate an SSH Key Pair

If you are using a Mac or Linux, you can generate a key pair from the terminal as follows.

If you already have an `id_rsa` file in the `.ssh` directory that you use with other applications, you should specify a different filename for the key so you do not overwrite it.  You can either do that with the `-f` option or type in a `filename` when prompted.

`ssh-keygen -t rsa -b 4096 -C sftp<companymarker>; -f filename`

For Example:

`ssh-keygen -t rsa -b 4096 -C sftptestcompany -f keyforasapp`

Where the filename will be the name of two files generated - `filename` (the private key you must keep to yourself) and `filename.pub` (the public key which ASAPP needs)

If you do not have an `id_rsa` file in the `.ssh` directory, you can go with the default filename of  `id_rsa` and do not need to use the `-f` option.

`ssh-keygen -t rsa -b 4096 -C sftp<companymarker>`

#### 2. Provide the Public Key to ASAPP

Send the `.pub` file for your key pair to ASAPP.  This is not a secret and can be emailed.

#### 3. Upload Files

You can upload files using the terminal or you can use [Cyberduck](https://cyberduck.io/). This section describes how to upload files using the terminal.

To login to the ASAPP server, type one of the following:

If you used the default id\_rsa key name:

`sftp sftp<companymarker>@sftp.us-east-1.asapp.com`

If you specified a different filename for the key:

`sftp -oIdentityFile=filename`

`sftp sftp<companymarker>@sftp.us-east-1.asapp.com`

For Example:

`sftp -oIdentityFile=keyforasapp`

`sftptestcompany@sftp.us-east-1.asapp.com`

You will see the command line prompt change to `sftp>`

If the `sftp` command fails, adding the `-v` parameter will provide logging information to help to diagnose the problem.

Use terminal commands such as `ls, cd, mkdir` on the remote server.

* `ls:` list files
* `cd:` change directory
* `mkdir`: make a new directory
  `ls` will show two directories: `in` (for sending files to ASAPP) and `out` (for receiving files from ASAPP).

To create a transcripts directory on the remote machine to send transcripts to ASAPP, type:

```json  theme={null}
cd in
mkdir transcripts
cd transcripts
```

To navigate on the local machine, prefix terminal commands with l

* `lcd`: change the local directory
* `lls`: list local files
* `lpwd`: to see the local working directory

Use `get` (retrieve) and `put` (upload) to transfer files.

`get` will fetch files from the remote server to the current directory on the local machine.

For example:

`get output.csv` will transfer a file named output.csv from the remote server.

`put` will transfer files to the remote server from the current directory on the local machine.

Navigate to local directory with transcripts and type:

`put transcripts.csv` will transfer a file named transcripts.csv to the remote server.

or

`put *` will transfer all files in the local directory.

or

`put -r <local directory>` works recursively and will transfer all files in the local directory, all sub directories, and all files within them to the remote machine. 

For example:

`put -r sftptest`

will transfer the sftptest directory and everything within it and below it from the local machine to the remote machine.

To end the SFTP session, type `quit` or `exit`.
