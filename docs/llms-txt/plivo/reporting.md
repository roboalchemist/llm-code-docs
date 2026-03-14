# Source: https://plivo.com/docs/messaging/concepts/reporting.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Reporting

> Analyze SMS and MMS traffic using console logs, APIs, and callback URLs

The Plivo console SMS/MMS Logs screen helps you analyze and gather information about your outbound and inbound messaging traffic. In addition to the Logs screen, you can get details about your messages by using [Plivo APIs](/messaging/api/overview) and [SDKs](/sdk/server/) to get message information programmatically. You can also use [Callback URLs](/messaging/concepts/callbacks/) to get live information about the state of your messages.

## SMS logs

To view the SMS Logs screen, log in to the console and navigate to the Messaging > [Logs](https://cx.plivo.com/logs?tab=messages) page.

<Frame>
    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/reporting/img1.jpg?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=d65067ba98d87f3521d323fb0b6b58e3" alt="SMS Logs" width="1440" height="804" data-path="images/reporting/img1.jpg" />
</Frame>

You can view details for all your outbound and inbound messages for the selected time filter on the Logs screen:

* **Date**: The time at which the message was queued in Plivo.
* **From:** The source number of the text message.
* **To**: The destination number of the text message.
* **To country**: Country ISO of the destination country.
* **Direction**: Message direction — Inbound or Outbound.
* **Status**: The current status of the message.
  Statuses for **Outbound** messages are

  * Queued
  * Failed
  * Send
  * Delivered
  * Undelivered

  Statuses for **Inbound** messages are

  * Received
  * Delivered
  * Undelivered
* **Error reason**: The reason for failure in cases where message status is Undelivered or Failed
* **Total amount (\$)**: Total amount charged for this message. This includes the carrier pass-through fees.

## Filters

By default, all messages for your account are displayed on the Logs screen. Use filters to add context to the displayed results. You can filter your results based on:

* From number
* To number
* Direction
* Status
* Error
* Time range
* Subaccount

<Frame>
    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/reporting/img2.jpg?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=81ab45fa5a58ab2f3506007609f06185" alt="Logs" width="1440" height="427" data-path="images/reporting/img2.jpg" />
</Frame>

Using a combination of these filters, you can narrow your search to relevant messages.

<Note>
  <strong>Note:</strong> You can view data up to 90 days old on the Logs screen. Plivo doesn’t retain data for longer than 90 days.
</Note>

## Export

To analyze data, you can download the message details or the summary as a CSV file.

<Note>
  <strong>Note:</strong> You can download CSV files with 10,000 or fewer records. Plivo will send you larger CSV files via email.
</Note>

<Frame>
    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/reporting/img3.jpg?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=03ffa03297761542677ae46a6ac16ace" alt="SMS Logs" width="1440" height="272" data-path="images/reporting/img3.jpg" />
</Frame>

### Export MDRs

To export all messages matching your filter criteria:

* Enter the time range and your search keywords, if any, and then click **Search**.
* From the **Export** drop-down list, select **All MDRs** or **Selected MDRs**, then then click **Export**.

The downloaded CSV will have the following fields:

* Message UUID
* From
* To
* To Country ISO2
* Direction
* Message Time
* Status
* Error Code
* Error Reason
* Units
* Rate Per Unit (USD)
* Carrier Surcharge Per Unit (USD)
* Total Charge Per Unit (USD)
* Total Charge (USD)

### Export Summary

To perform a high-level analysis of your SMS traffic, use the **Usage Summary** options from the **Export** drop-down list. You can view the usage summary by day, or by day and hour. MDR summary data includes:

* Date
* Hour
* Subaccount ID
* Message Direction
* To Country
* Message State
* Mobile Country Code
* Mobile Network Code
* Error Code
* Error Reason
* Powerpack ID
* Application
* Message Intent
* Message Units

Plivo calculates Total Count, Total Units, and Total Spend Including Carrier Passthrough Fee for each of the grouped data points and adds that data to the CSV file.

<Note>
  <strong>Note:</strong> For reference, <a href="https://s3.amazonaws.com/plivo_blog_uploads/static_assets/Plivo-MCC-MNC-Network.csv">download</a> a file mapping Mobile Country Code (MCC) and Mobile Network Code (MNC) to network operators.
</Note>

## Examples

Here are some examples of how you can use the CSV data to gain insights:

1. *“During some hours of the day I see a dip in the message delivery of my outbound messages. What is the hour-wise distribution of outbound delivery rates for the last three days?”*

   * On the SMS Logs page, select the date range for the last three days.
   * In the search field, tick **Direction** from the drop-down filter list and choose **Outbound**, then click **Apply** to display only the outbound messages.
   * At the top of the rightmost column select **logs on this page**.
   * To export the summary of the displayed data, select **By Day & Hour** from the Export drop-down list, then click **Export**.
   * Select a folder to save the CSV file in, then click **Save**.
   * You can use the downloaded CSV to surface the required data using Microsoft Excel or Google Sheets Data Pivots.

   <Frame>
       <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/reporting/img4.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=f5b363186c62faa75d700f6a6a140849" alt="Downloaded CSV" width="770" height="412" data-path="images/reporting/img4.png" />
   </Frame>
2. *“I ran two SMS campaigns this week and want to monitor the daily DND opt-in and opt-out rates for that time period.”*

   * In the SMS Logs page, select the date range for the last week.
   * In the search field, tick **Direction** from the drop-down filter list and choose **Inbound**, then click **Apply** to display only the inbound messages.
   * At the top of the rightmost column select **logs on this page**.
   * To export the summary of the displayed data, select **By Day** from the Export drop-down list, then click **Export**.
   * Select a folder to save the CSV file in, then click **Save**.
   * You can use the downloaded CSV to surface the required data using Microsoft Excel or Google Sheets Data Pivots.

   <Frame>
       <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/reporting/img5.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=82a39ce036f4caecdd497af642bf7d8f" alt="Export CSV" width="611" height="316" data-path="images/reporting/img5.png" />
   </Frame>
3. *“I’m in the process of budgeting my SMS campaigns for the next quarter and I need to check my daily spends on SMS over the last month per subaccount.”*

   * On the SMS Logs page, use the Filter Logs drop-down, choose Date Range, select the start and end for the last month, then click **Search**.
   * At the top of the rightmost column select **logs on this page**.
   * To export the summary of the displayed data, select **By Day** from the Export drop-down list, and then click **Export**.
   * Select a folder to save the CSV file in, then click **Save**.
   * You can use the downloaded CSV to surface the required data using Microsoft Excel or Google Sheets Data Pivots.

   <Frame>
       <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/reporting/img6.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=87d6c4abfae1edf1d30f29b92813f297" alt="Save CSV" width="1280" height="701" data-path="images/reporting/img6.png" />
   </Frame>
