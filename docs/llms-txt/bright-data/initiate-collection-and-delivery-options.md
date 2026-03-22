# Source: https://docs.brightdata.com/datasets/scraper-studio/initiate-collection-and-delivery-options.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Initiate Data Collection & Delivery with IDE Scraper

> Learn how to initiate data collection and set up delivery options using the IDE Scraper. Explore manual, API, and scheduled methods for efficient data scraping.

When writing a scraper code on the IDE, the system auto-saves the scraper as a draft to the development environment. From inside the IDE, you can run one page at a time to sample how your scraper will behave. To get a full production run, you need to save scraper to production by clicking the 'Save to production' button at the top right corner of the IDE screen. All scrapers will appear under the **My scrapers** tab in the control panel. Any inactive scraper will be shown in a faded state.

<Frame>
    <img src="https://mintcdn.com/brightdata/ilemiSHw8UogZ13k/images/scraping-automation/web-scraping-ide/initiate-collection-and-delivery-options/my-scrapers.png?fit=max&auto=format&n=ilemiSHw8UogZ13k&q=85&s=9e15b58693b5b900307378dfa344a78c" alt="" width="1317" height="831" data-path="images/scraping-automation/web-scraping-ide/initiate-collection-and-delivery-options/my-scrapers.png" />
</Frame>

## Initiate scraper

To start collecting the data, choose one of three options:

<Tabs>
  <Tab title="Initiate by API">
    Start data collection through our API without needing to access the Bright Data control panel : [Getting started with API documentation](/api-reference/scraper-studio-api/Getting_started_wtih_the_API)

    Before initiating an API request, Create an API key. **To create an API key, go to:**\
    [Dashboard side menu settings > account settings > API key](https://brightdata.com/cp/setting)

    <Frame>
            <img src="https://mintcdn.com/brightdata/ilemiSHw8UogZ13k/images/scraping-automation/web-scraping-ide/initiate-collection-and-delivery-options/initiate-by-api.png?fit=max&auto=format&n=ilemiSHw8UogZ13k&q=85&s=cfa88b89067509c7d2556d406829bb12" alt="" width="1712" height="453" data-path="images/scraping-automation/web-scraping-ide/initiate-collection-and-delivery-options/initiate-by-api.png" />
    </Frame>

    1. **Set Up Inputs Manually** - provide input manually or through the API request
    2. **Trigger behavior** - you can add several requests in parallel that are activated according to the order they're defined. You can add another job run to the queue and run more than two jobs simultaneously.
    3. **Preview of the API Request** - Bright Data provides you with a REST API call to initiate the scraper. Please select the "Linux Bash" viewer for CURL commands. As soon as you send the request, you will receive a job id.

    You will receive the data according to the delivery preferences defined earlier.

    <Note>
      Receive data API call is required in order to receive data when delivery preferences is set to API download
    </Note>
  </Tab>

  <Tab title="Initiate manually">
    Bright Data's control panel makes it easy to get started collecting data.

    <Frame>
            <img src="https://mintcdn.com/brightdata/ilemiSHw8UogZ13k/images/scraping-automation/web-scraping-ide/initiate-collection-and-delivery-options/initiate-manually.png?fit=max&auto=format&n=ilemiSHw8UogZ13k&q=85&s=4f2270461d5e2b503ff1513b3af4d6bb" alt="" width="1718" height="515" data-path="images/scraping-automation/web-scraping-ide/initiate-collection-and-delivery-options/initiate-manually.png" />
    </Frame>

    1. **Trigger behavior** - you can add several requests in parallel that are activated according to the order they're defined. You can add another job run to the queue and run more than two jobs simultaneously.
    2. **Set up inputs manually**
    3. **Upload CSV file** - If you'd like to add a large amount of input, the easiest way is to add them to a CSV file and upload it to the system. For example, a list of URLs.\
       See the example provided for reference.
  </Tab>

  <Tab title="Schedule a scraper">
    Choose when to initiate the scraper.

    **Step One:**

    1. Choose a date and time for the scraper to start.
    2. Select the frequency it will run (hourly, daily, weekly, etc.)
    3. Set a deadline for when a scraper is complete.
    4. Review your setup.

    <Frame>
            <img src="https://mintcdn.com/brightdata/ilemiSHw8UogZ13k/images/scraping-automation/web-scraping-ide/initiate-collection-and-delivery-options/schedule-configuration.png?fit=max&auto=format&n=ilemiSHw8UogZ13k&q=85&s=8ff98514169433ce6b70e810786a063d" alt="" width="1738" height="908" data-path="images/scraping-automation/web-scraping-ide/initiate-collection-and-delivery-options/schedule-configuration.png" />
    </Frame>

    **Step Two :**

    1. Add a large number of inputs to a CSV file. For instance, a list of URLs. To upload easily without errors, you can download a template of a CSV structure example.
    2. Set up Inputs manually

    <Frame>
            <img src="https://mintcdn.com/brightdata/ilemiSHw8UogZ13k/images/scraping-automation/web-scraping-ide/initiate-collection-and-delivery-options/enter-input.png?fit=max&auto=format&n=ilemiSHw8UogZ13k&q=85&s=fc5ef217b959819e9803129824e37113" alt="" width="1735" height="912" data-path="images/scraping-automation/web-scraping-ide/initiate-collection-and-delivery-options/enter-input.png" />
    </Frame>
  </Tab>
</Tabs>

***

## Rate Limits & Concurrent Requests

To ensure stable performance and fair usage, Scraper Studio IDE enforces rate limits based on the request type: single-input (real-time) or batch

### **What is the Rate Limit?**

The Scraper Studio IDE supports the following maximum number of concurrent requests:

| Method    | Rate-limit                     |
| :-------- | :----------------------------- |
| Batch     | up to 1000 concurrent requests |
| Real-time | no limit                       |

Exceeding the batch request limit will result in the following error response: "Maximum limit of 1000 jobs per collector has been exceeded. Please reduce the number of parallel jobs...’

## Batch vs. Real-time Collection Methods

**Batch collection** is designed for large-scale data collection. It lets you submit a list of URLs (or inputs) and retrieve the results once the job is complete.

**Real-time collection** is designed for use cases that require immediate results. It lets you submit a single URL (or input) and receive the response in real time.

Both methods are reliable and efficient—they’re simply optimized for different data collection needs.

## Delivery Options

You can set your delivery preferences for the dataset. To do that simply click on the scraper row from the 'My scrapers' tab and then click on 'Delivery preferences'

<AccordionGroup>
  <Accordion title="Choose when to get the data">
    * Batch : an efficient way of managing large amounts of data
      * Split batch : deliver the data in smaller batches as soon as it's ready
    * Real-time : is an ideal way to get a fast response for one request
      * Skip retries : Do not retry when error occurs. Can speed up collection
  </Accordion>

  <Accordion title="Choose file format">
    * JSON
    * NDJSON
    * CSV
    * XLSX
    * PARQUET
  </Accordion>

  <Accordion title="Choose how to receive the data">
    * Email
    * API Download
    * Webhook
    * Cloud storage providers : Amazon S3, Google Cloud Storage, Azure, Alibaba Cloud OSS
    * SFTP/FTP

      <Note>
        Media files cannot be delivered when it's set to Email or API download
      </Note>
  </Accordion>

  <Accordion title="Choose data preferences (batch)">
    * Result and Errors in separate files
    * Result and Errors together in one file
    * Only successful results
    * Only errors
  </Accordion>

  <Accordion title="Define notifications">
    * Notify when the collection is complete
    * Notify success rates
    * Notify when an error occurs
  </Accordion>
</AccordionGroup>

### Output schema

Schema defines the data point structure and how the data will be organized.

You can change the schema structure and modify the data points to suit your needs, re-order, edit, set default values and add additional data to your output configuration.

<img src="https://mintcdn.com/brightdata/ilemiSHw8UogZ13k/images/scraping-automation/web-scraping-ide/initiate-collection-and-delivery-options/output-schema.png?fit=max&auto=format&n=ilemiSHw8UogZ13k&q=85&s=23688a07496b17cb34408ca55a5a3a6d" alt="" width="1600" height="853" data-path="images/scraping-automation/web-scraping-ide/initiate-collection-and-delivery-options/output-schema.png" />

|                           |                                                                                      |
| ------------------------- | ------------------------------------------------------------------------------------ |
| **Input / Output schema** | choose the tab you'd like to configure                                               |
| **Custom validation**     | validate the schema                                                                  |
| **Parsed data**           | data points collected by the scraper                                                 |
| **Add new field**         | if you need additional data point, you can add fields and define field name and type |
| **Additional data**       | additional information you can add to the schema (timestamp, screenshot, etc.)       |
