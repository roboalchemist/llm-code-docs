# Source: https://docs.brightdata.com/datasets/scrapers/scrapers-library/ai-scrapers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# AI Web Scrapers Documentation

> This document provides an overview of the AI-powered web scrapers integrated into our system. These scrapers interact with advanced AI models to retrieve structured responses to user prompts, including relevant metadata such as sources, citations, and contextual information.

<Warning>
  [Grok Scraper](https://brightdata.com/cp/scrapers/browse?domain=grok.com) is currently experiencing an outage, and requests are being blocked on their side.
  Our team is doing its best to resolve the issue as soon as possible.

  For updates, please check here, or open a support ticket at [support@brightdata.com](mailto:support@brightdata.com).
</Warning>

# Overview

Our platform supports the following AI scrapers:

* [ChatGPT](https://brightdata.com/cp/scrapers/browse?domain=chatgpt.com)
* [Perplexity](https://brightdata.com/cp/scrapers/browse?domain=perplexity.ai)
* [Gemini](https://brightdata.com/cp/scrapers/browse?domain=gemini.google.com)
* [Grok](https://brightdata.com/cp/scrapers/browse?domain=grok.com)
* [Google - AI Mode](https://brightdata.com/cp/scrapers/browse?domain=google.com)
* [Copilot](https://brightdata.com/cp/scrapers/browse?domain=copilot.microsoft.com)

Each scraper is designed to handle user prompts and return enriched responses, with varying levels of detail and supporting data.

<div>
  ## How AI Scraping Differs from Traditional SERP Scraping
</div>

AI bot scraping offers a smarter, more efficient alternative to traditional SERP (Search Engine Results Page) scraping. While SERP scraping involves extracting raw HTML from search engine result pages—often requiring complex parsing and frequent maintenance—AI bot scraping uses natural language models to understand the intent behind a query and return structured, context-rich answers.
Key advantages of AI bot scraping over SERP scraping:

* ✅ Understands query context and delivers direct answers
* ✅ Includes citations, sources, and enriched content (e.g., maps, product links)
* ✅ More resilient to UI changes and search engine updates
* ✅ Easier to integrate via official APIs
* ✅ Provides a better user experience with cleaner, more relevant results

In contrast, SERP scraping is limited to surface-level data, often lacks context, and may violate search engine terms of service. AI bot scraping is the modern, scalable solution for intelligent data extraction.

***

| Scraper                | Short Description                                                               | Includes                                                                                                                                                                                                                                                    |
| :--------------------- | :------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **ChatGPT Scraper**    | Generates detailed, conversational answers using OpenAI's ChatGPT.              | <ul><li>Hyperlinks</li><li>Citations (when available)</li><li>Product recommendations</li><li>Embedded map data</li><li>[Available countries](https://github.com/brightdata/answer-engines-country-codes/blob/main/chatgpt_countries.csv)</li></ul>         |
| **Perplexity Scraper** | Provides concise, well-sourced answers via Perplexity AI, ideal for research.   | <ul><li>Hyperlinked citations for verification</li><li>[Available countries](https://github.com/brightdata/answer-engines-country-codes/blob/main/perplexity_countries.csv)</li></ul>                                                                       |
| **Copilot Scraper**    | Offers contextual answers with sources using Microsoft's Copilot                | <ul><li>Hyperlinked citations</li><li>Contextual explanations</li><li>[Available countries](https://github.com/brightdata/answer-engines-country-codes/blob/main/copilot_countries.csv)</li></ul>                                                           |
| **Gemini Scraper**     | Delivers informative responses with potential web searches via Google's Gemini. | <ul><li>Web-based citations and sources</li><li>Hyperlinked references (when available)</li><li>[Country targeting](https://github.com/brightdata/answer-engines-country-codes/blob/main/gemini_countries.csv) (European countries not available)</li></ul> |
| **Google AI Scraper**  | Collect Google AI mode search results by prompt                                 | <ul><li>[Available countries](https://github.com/brightdata/answer-engines-country-codes/blob/main/google_aimode_countries.csv)</li></ul>                                                                                                                   |
| **Grok Scraper**       | Collect Grok search results by prompt                                           | <ul><li>Hyperlinked citations</li><li>[Available countries](https://github.com/brightdata/answer-engines-country-codes/blob/main/grok_countries.csv)</li></ul>                                                                                              |

<Note>
  The decision to search the web is controlled internally by Gemini and cannot currently be forced or disabled via the scraper. Prompt phrasing may influence whether web search is triggered.
</Note>
