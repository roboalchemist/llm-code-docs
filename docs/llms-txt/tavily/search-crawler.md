# Source: https://docs.tavily.com/documentation/search-crawler.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavily.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Tavily Search Crawler

Like any other search engine, Tavily Search has a crawler to discover new pages and index their content.

The Tavily Search crawler does not advertise a differentiated user agent because we must avoid discrimination from websites that allow only Google to crawl them. However, if a domain or page is not crawlable by Googlebot, then Tavily Search’s bot will not crawl it either.

### Indexing and Delisting

* robots.txt is not used to prevent a page from being indexed. Instead, a site owner can delist a page by using the robots noindex directive.
* Once your web page has been updated with this directive, Tavily needs to re-fetch it to apply the changes.

### Right to Be Forgotten

If your inquiry is about delisting web pages containing personal data about you, please follow the guidance and process of the [right to be forgotten](/documentation/Right-To-Be-Forgotten).

### Reporting Non-Existent Pages

In case Tavily Search is returning a page that no longer exists, and you would like to have it delisted, you may contact us at **[support@tavily.com](mailto:support@tavily.com)**.
