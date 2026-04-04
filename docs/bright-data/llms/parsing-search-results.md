# Source: https://docs.brightdata.com/scraping-automation/serp-api/parsed-json-results/parsing-search-results.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Parsed JSON Results with SERP API

> In this article, we will cover the basics of parsing with SERP API and see real JSON examples of parsed data.

## What is Parsing?

[Parsing](https://brightdata.com/blog/web-data/what-is-data-parsing) for SERP API is the process of transforming a raw HTML response into a **structured JSON** with fields and values of data. This advanced parsing functionality is supported specifically for Google & Bing.

When parsing is activated, data from SERP HTMLs are further structured into usable fields and values (such as, `rank`, `link`, `title`, `description`, `rating`, and dozens more fields) enabling you to monitor competitor SERP rankings, analyze keyword trends, and gather valuable market insights.

## Send a Basic Parsed Request

By default, the basic parsed request is configured in the web access SERP api creation page.

## Overriding default configuration

In order to override default data format, learn how to use the designated header parameter here.

<Tip>
  Parsing is supported for both **Google** and **Bing** search engines
</Tip>

<Info>
  The above request is a **synchronous** request (the response is received in real-time). If you are looking to send an **asynchronous** parsed request see [here](/scraping-automation/serp-api/asynchronous-requests).
</Info>

***

## Basic Request - Breakdown

|                                                                                                                                                                                             |                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `brd.superproxy.io`                                                                                                                                                                         | Address of our load balancer that will find the fastest Super Proxy for your request                                   |
| <Tooltip tip="Port 33335 replacing port 22225 deprecated on Sep 2026, click to read more">[33335](https://docs.brightdata.com/general/faqs#which-port-shall-i-use-22225-or-33335)</Tooltip> | Infrastructure port of our Super Proxies that is used to receive your requests                                         |
| `-user brd-customer-<customer_id> -zone-<zone_name>`                                                                                                                                        | Username authentication. In its most basic form, it defines your username and what zone you will use for your request. |
| `ZONE_PASSWORD`                                                                                                                                                                             | Zone password. All zones have passwords that are used for authentication                              \`               |

***
