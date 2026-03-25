# Source: https://docs.brightdata.com/datasets/scraper-studio/warc-ide.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# WARC files

> Produce WARC files during scraping operations

## How to Get WARC File Output

**Overview**

Web Scraper IDE now supports returning the full HTTP response in WARC (Web ARChive) format. This feature allows you to archive the exact content and metadata of a web page as it was received during scraping.

**What is a WARC File?**

WARC is a standardized file format used to store web crawls and HTTP interactions. It is commonly used in digital preservation, research, and compliance scenarios.

**How to Enable WARC Output**

WARC files are available only for browser workers 

To include WARC files in your scraping results:

* Open your Web-Scraper IDE configuration.
* In the Output Schema, under ‘additional\_data’ field, click the eye icon next to warc\_snapshot.

<img src="https://mintcdn.com/brightdata/ilemiSHw8UogZ13k/images/warc_example.png?fit=max&auto=format&n=ilemiSHw8UogZ13k&q=85&s=2d7eb3b2d77e5efb3dca9e822f345f52" alt="Warc Example Pn" width="987" height="648" data-path="images/warc_example.png" />

* Save and run a job
* Once the job completes, the WARC file(s) will be delivered to you according to the scraper's delivery settings.

**Optimal usage**

To ensure the WARC file captures as much of the page content as possible, keep the following in mind:

* WARC capture is limited to browser-side requests only. This includes all network activity initiated by the browser during page load (e.g., HTML, CSS, JS, images, XHR requests).
* Use the wait\_network\_idle() function in your scraping workflow to allow the browser to finish loading all resources before the WARC is finalized. This helps maximize the completeness of the captured data.
