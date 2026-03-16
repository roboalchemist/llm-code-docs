# Source: https://docs.brightdata.com/scraping-automation/serp-api/pricing-and-billing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SERP Pricing & Billing

> Pay only for successful requests. Learn Bright Data SERP API billing, what’s included, how async billing works.

Bright Data SERP API uses **per‑1,000 successful requests** pricing. Failed/errored requests are not billed. Parsing and unlocking are included—no bandwidth fees.

> * Billing unit: per successful request (per 1,000)
> * Parsing/unlocking included (no bandwidth fees)
> * Async: “send request” billed; “collect/retrieve” free

[Bright Data SERP API price tiers and volume discounts](https://brightdata.com/pricing/serp?utm_source=docs\&utm_medium=pricing-billing\&utm_campaign=serp_pricing)

## Pay per success

With Bright Data, **only successful responses** are billed.

* Unit: per 1,000 successful requests
* Included: parsing (JSON/Markdown/HTML), proxy management, unlocking/CAPTCHA handling
* No bandwidth fees

<Note>If a request is retried behind the scenes, you’re **not** charged extra, only the successful response is billed.</Note>

***

## Async billing

Use asynchronous mode for long‑running jobs or large batches.

* **Billed**: the initial “send request” call
* **Not billed**: the follow‑up “collect/retrieve” call

See: [Asynchronous Requests](/scraping-automation/serp-api/asynchronous-requests)

***

## What’s included in the unit price

* Structured outputs: **JSON**, **Markdown**, or **raw HTML**
* Proxy management & **unlocking** (incl. CAPTCHA handling)
* Automatic retries and best header/device logic
* City/ZIP geotargeting; **desktop and mobile** user agents

***

## FAQs

**Are retries or async “collect” billed?**\
Retries are included. In async mode, “collect/retrieve” is **not** billed—only the “send request” is billed.

**Is parsing included?**\
Yes—**JSON/Markdown/HTML** are included in the unit price.

**Do you charge bandwidth fees?**\
No, pricing is per successful request only.

***

## See also

* [SERP pricing](https://brightdata.com/pricing/serp?utm_source=docs\&utm_medium=pricing-billing\&utm_campaign=serp_pricing)
* [Introduction to SERP API](/scraping-automation/serp-api/introduction)
* [Asynchronous Requests](/scraping-automation/serp-api/asynchronous-requests)
* [Parsed JSON Results](/scraping-automation/serp-api/parsed-json-results/parsing-search-results)
