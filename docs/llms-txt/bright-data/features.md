# Source: https://docs.brightdata.com/scraping-automation/web-unlocker/features.md

# Source: https://docs.brightdata.com/scraping-automation/browser-extension/features.md

# Source: https://docs.brightdata.com/datasets/scraper-studio/features.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Features

## Data scraper Dashboard

<Frame>
    <img src="https://mintcdn.com/brightdata/ilemiSHw8UogZ13k/images/scraping-automation/web-scraping-ide/features/dashboard.png?fit=max&auto=format&n=ilemiSHw8UogZ13k&q=85&s=62c3e3a82c86fbc885baab922ab92114" alt="" width="1181" height="581" data-path="images/scraping-automation/web-scraping-ide/features/dashboard.png" />
</Frame>

Any scraper you create using the AI tool, the IDE, or custom scraper will appear on your Scrapers dashboard under 'My Scrapers'.

### Overview

* **Free trial**: As part of the 7-day free trial, you're entitled to 1,000-page loads
* **Update available**: A new version of the scraper is available. If there is no update button, you have the latest version.
* **Delivery preferences**: Choose your desired file format, delivery method, and notification settings.
* **Limitations**  - Our collectors have a limitation of **1000 parallel-running batch jobs**. When more than 1000 jobs are triggered, the additional jobs are placed in a queue and wait until the earlier ones finish.

***

### Scraper action menu

The scraper action menu allows performing different actions with the scraper.

* **Initiate by API** - start a data collection without having to enter the control panel
* **Initiate manually** - Bright Data's control panel makes it easy to get started collecting data
* **Run on schedule** - select precisely when to collect the data you need
* **Versions** - review the modified versions of the scraper
* **Report an issue** - You can use this form to communicate any problems you have with the platform, the scraper, or the dataset results
* **Copy link** - copy the link of the scraper to share it with your colleagues
* **Tickets** - view the status of your tickets
* **Advanced options:**
  * Edit the code - edit the scraper's code within the IDE.
  * Disable scraper - temporarily disable the scraper, but you can reactivate it if needed.
  * Delete scraper - permanently delete the scraper.

<Frame>
    <img src="https://mintcdn.com/brightdata/ilemiSHw8UogZ13k/images/scraping-automation/web-scraping-ide/features/action-menu.png?fit=max&auto=format&n=ilemiSHw8UogZ13k&q=85&s=0698f36f40317d6cc61810457b8a828c" alt="" width="1665" height="737" data-path="images/scraping-automation/web-scraping-ide/features/action-menu.png" />
</Frame>

***

### Properties:

<img src="https://mintcdn.com/brightdata/ilemiSHw8UogZ13k/images/scraping-automation/web-scraping-ide/features/properties.png?fit=max&auto=format&n=ilemiSHw8UogZ13k&q=85&s=5ac5399790eed696ef86d53c1255b9b0" alt="" width="1605" height="446" data-path="images/scraping-automation/web-scraping-ide/features/properties.png" />

* Maintainer of the scraper :
  * Self-serve: scraper is maintained by you
  * Full-service: scraper is maintained by Bright Data Developers
* Type of the scraper :
  * Search : The scraper input is a keyword (i.e., iPhone)
  * PDP : The scraper input is a product page URL
  * Discovery : The scraper input is a category URL
  * Other
* Use case of the scraper (Social media, eCommerce, Travel, etc.)
* Last modified : indicates when the scraper was last updated
* Price of CPM : 1 CPM = 1,000 page loads.
* Avg. Page-load per input : Average number of loaded pages to process 1 input set

## Initiate scraper and get collection results

**Initiate scraper**

To start collecting the data, you have three options:

A. [Initiate by API](/datasets/functions/initiate-collection-and-delivery-options#initiate-scraper)\
B. [Initiate manually](/datasets/functions/initiate-collection-and-delivery-options#initiate-manually)\
C. [Schedule a scraper](/datasets/functions/initiate-collection-and-delivery-options#schedule-a-scraper)

<img src="https://mintcdn.com/brightdata/ilemiSHw8UogZ13k/images/scraping-automation/web-scraping-ide/features/options.png?fit=max&auto=format&n=ilemiSHw8UogZ13k&q=85&s=88c34478b83feb8bbcb3bc8bdb92690c" alt="" width="1655" height="561" data-path="images/scraping-automation/web-scraping-ide/features/options.png" />

**Get collection results**

Once the data collection is completed, click the "three dots" icon and select "Statistics" to access the results and download the data.

<Note>
  Realtime job input and output cannot be downloaded since it is not stored on our end
</Note>

## Statistics

<img src="https://mintcdn.com/brightdata/ilemiSHw8UogZ13k/images/scraping-automation/web-scraping-ide/features/statistics.png?fit=max&auto=format&n=ilemiSHw8UogZ13k&q=85&s=a9c3610ab0ced4dca32a56c520bacc31" alt="" width="1632" height="571" data-path="images/scraping-automation/web-scraping-ide/features/statistics.png" />

The statistics page presents essential information about the success of the data collection. Below is a list of all the terms included in the statistics table:

**Statistics actions menu**

<img src="https://mintcdn.com/brightdata/ilemiSHw8UogZ13k/images/scraping-automation/web-scraping-ide/features/statistics-action-menu.png?fit=max&auto=format&n=ilemiSHw8UogZ13k&q=85&s=14ba9fc668eaf5a8e66d340a36a22155" alt="" width="1672" height="454" data-path="images/scraping-automation/web-scraping-ide/features/statistics-action-menu.png" />

* **3 dots** Here you can perform different functions with the data collection job: The statistics page presents essential information about the success of the data collection. Below is a list of all the terms included in the statistics table:

<img src="https://mintcdn.com/brightdata/ilemiSHw8UogZ13k/images/scraping-automation/web-scraping-ide/features/collector-runs.png?fit=max&auto=format&n=ilemiSHw8UogZ13k&q=85&s=74e152493504e366a896d58a4008c236" alt="" width="1716" height="270" data-path="images/scraping-automation/web-scraping-ide/features/collector-runs.png" />

* **Job ID** - The unique id of the collection
* **Trigger** - The person who initiated the data collection and how (API, manually or scheduled)
* **Inputs** - The number of inputs inserted into the collection
* **Records** - The number of results collected
* **Failed** - The number of pages failed to be crawled
* **Success rate** - The percentage of the results that were successfully collected
* **Queued at** - The queue timestamp
* **Started at** - The date and time when the scraper began collecting
* **Finished at** - The date and time when the scraper finished collecting
* **Job time** - The length of time it took to complete
* **Estimated time left** - The amount of time left until collection is complete
* **Queue** - The name of the job given in the trigger behavior (Queue name)
* **Usage** - The total amount of page loads used

<img src="https://mintcdn.com/brightdata/ilemiSHw8UogZ13k/images/scraping-automation/web-scraping-ide/features/three-dots.png?fit=max&auto=format&n=ilemiSHw8UogZ13k&q=85&s=73ab24c67538eaa2354f20dd7877b914" alt="" width="1672" height="454" data-path="images/scraping-automation/web-scraping-ide/features/three-dots.png" />
