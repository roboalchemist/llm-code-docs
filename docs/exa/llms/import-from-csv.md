# Source: https://exa.ai/docs/websets/dashboard/import-from-csv.md


> ## Documentation Index
>
> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Import from CSV

> Turn your existing CSV data into a Webset

<br />

## Overview

The Import from CSV feature allows you to transform your existing CSV files containing URLs into fully-functional Websets. This is perfect when you already have a list of websites, companies, or resources that you want to enrich with additional data or apply search criteria to filter.

<br />

## How it works

<img src="https://mintcdn.com/exa-52/tmzyKnsgpKLGddKC/images/websets/import-flow.png?fit=max&auto=format&n=tmzyKnsgpKLGddKC&q=85&s=6cf23e9e291fe7811942d18c3aa08b33" alt="" data-og-width="1512" width="1512" data-og-height="857" height="857" data-path="images/websets/import-flow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/exa-52/tmzyKnsgpKLGddKC/images/websets/import-flow.png?w=280&fit=max&auto=format&n=tmzyKnsgpKLGddKC&q=85&s=7144bcac1257ad6234f84e09b3b46e65 280w, https://mintcdn.com/exa-52/tmzyKnsgpKLGddKC/images/websets/import-flow.png?w=560&fit=max&auto=format&n=tmzyKnsgpKLGddKC&q=85&s=e0002f49d319b209241babc75e41bb8c 560w, https://mintcdn.com/exa-52/tmzyKnsgpKLGddKC/images/websets/import-flow.png?w=840&fit=max&auto=format&n=tmzyKnsgpKLGddKC&q=85&s=4a05c88f7ee0b6c5e1aff2b9b2123458 840w, https://mintcdn.com/exa-52/tmzyKnsgpKLGddKC/images/websets/import-flow.png?w=1100&fit=max&auto=format&n=tmzyKnsgpKLGddKC&q=85&s=00a37fce8580e9c539033d63d15c00cb 1100w, https://mintcdn.com/exa-52/tmzyKnsgpKLGddKC/images/websets/import-flow.png?w=1650&fit=max&auto=format&n=tmzyKnsgpKLGddKC&q=85&s=11b6832f570530b2a28d21ced7ce3ad1 1650w, https://mintcdn.com/exa-52/tmzyKnsgpKLGddKC/images/websets/import-flow.png?w=2500&fit=max&auto=format&n=tmzyKnsgpKLGddKC&q=85&s=be874fa671009913eae844700df875d6 2500w" />

1. Click "Start from CSV" to select your CSV file
2. Select which column contains the URLs you want to analyze
3. Review how your data will be imported before proceeding
4. Your URLs are transformed into a Webset with enrichments and metadata

<br />

## CSV preparation

Ensure your CSV file has a URL column

* For People searches: URLs must be LinkedIn profile URLs (e.g., [https://linkedin.com/in/username](https://linkedin.com/in/username))
* For Company search: URLs must be company homepage URLs (e.g., [https://example.com](https://example.com))
* For other searches: use any type of URL

If you do not have URLs, Websets will attempt to infer URLs based on the information in each CSV row and any extra info you provide.

The maximum number of results you can import is determined by your plan.

## What happens next?

Once imported, your CSV becomes a full Webset where you can:

### Enrich with custom columns

Add any information you want about each URL:

* Contact information (emails, phone numbers)
* Company metrics (revenue, employee count)
* Content analysis (sentiment, topics, summaries)
* Custom data specific to your use case

### Apply search criteria

Filter your imported URLs based on specific criteria:

* Company stage or size
* Industry or sector
* Geographic location
* Content type or topic
