# Source: https://docs.brightdata.com/api-reference/scraper-studio-api/Getting_started_wtih_the_API.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Getting started with the API

> The Data scraper product offers a JSON API to control and inspect your data scrapers programmatically.

1. Signup (or login) to our control panel
2. Insert target URL (website to collect data from) or choose a ready-made template
3. Set up the delivery preference of scraper: Batch or Real-Time
4. Initiate by API

<Tip>
  NOT A DEVELOPER? Contact our support for easy onboarding.
</Tip>

The data scraper is divided into two crawling systems:

<Tabs>
  <Tab title="Batch">
    This is an efficient way of handling large amounts of data. Data is collected in batches over a period of time. After the data is collected, entered, and processed, the batch results are generated. You can deliver the results all at once or stream them to your system as they're collected.
  </Tab>

  <Tab title="Real-Time">
    This is an ideal way to get a fast response for one request. This is useful in environments where you have a limited amount of time to crawl a page and get the data.
  </Tab>
</Tabs>

The Data scraper API has four general workflows:

1. [Batch trigger + Push delivery](/api-reference/scraper-studio-api/Trigger_a_scraper_for_batch_collection_method)
2. [Batch trigger + API polling](/api-reference/scraper-studio-api/Receive_batch_data)
3. [Real-time trigger + Push delivery](/api-reference/scraper-studio-api/Trigger_a_scraper_for_real_time_collection)
4. [Real-time trigger + API polling](/api-reference/scraper-studio-api/Receive_data_from_real_time_work_scraper)
5. [Real-time Synchronous trigger](/api-reference/scraper-studio-api/initiate-a-realtime-job/sync-realtime-job)
