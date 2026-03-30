# Source: https://docs.brightdata.com/integrations/dify.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Set Up Bright Data With Dify

<Card title="Building an AI startup?" cta="Learn more" href="https://brightdata.com/ai/ai-startups-program" icon="rocket-launch" iconType="duotone" arrow="true">
  You might be eligible for our Startup Program. Get fully funded access to the infrastructure you're reading about right now (up to \$20K value).
</Card>

A comprehensive web scraping and data extraction plugin powered by Bright Data's enterprise-grade infrastructure with intelligent auto-detection. Supports 50+ platforms including Amazon, LinkedIn, Instagram, YouTube, and more.

<Frame>
  ![image](https://github.com/user-attachments/assets/5825d274-d47b-4fed-950f-65e6b7c63e58)
</Frame>

<Note>
  For the most up-to-date updates, please refer to this [Repository](https://github.com/brightdata/brightdata-dify-plugin/blob/main/BrightData/brightdata-dify-plugin/README.md)
</Note>

## Available Tools

### Structured Data Feeds

Extract structured data from popular platforms:

* **E-commerce**: Amazon, eBay, Walmart, Best Buy, Etsy, Zara
* **Social Media**: Instagram, Facebook, TikTok, YouTube, X (Twitter)
* **Professional**: LinkedIn profiles, companies, jobs
* **Business**: Crunchbase, ZoomInfo
* **Maps & Reviews**: Google Maps, booking sites
* **News**: Reuters and other news sources

### Scrape As Markdown

Convert any webpage into clean, readable markdown format perfect for:

* Content analysis
* Documentation extraction
* Article processing

### Search Engine

Get search results from major search engines:

* Google
* Bing
* Yandex, etc.

## Use Cases

* **E-commerce Monitoring**: Track product prices and availability
* **Lead Generation**: Extract business information from LinkedIn
* **Content Research**: Gather articles and news for analysis
* **Market Research**: Monitor competitor websites and social media
* **SEO Analysis**: Track search engine results and rankings

## How to Integrate Bright Data With Dify

<Steps>
  <Step title="Install the plugin">
    Install Bright Data Plugin from [Dify Marketplace](https://marketplace.dify.ai/plugins/idanvilenski/brightdata)
  </Step>

  <Step title="Obtain Your Bright Data API Key">
    * Log in to your [Bright Data dashboard](https://brightdata.com/cp).
    * Go to [Account Settings](https://brightdata.com/cp/setting/users).
    * [Generate an API key](https://docs.brightdata.com/api-reference/authentication#api-key) if you haven't already done so.
  </Step>

  <Step title="Create Your First Workflow">
    1. Go to **Dify Studio** → **Workflow**
    2. Add one of the **Bright Data Web Scraper** tools:

    * **Structured Data Feeds** - Extract structured data from 20+ platforms
    * **Scrape As Markdown** - Convert any webpage to clean markdown
    * **Search Engine** - Get search results from Google, Bing, Yandex

    3. Enter your Bright Data API key when prompted
    4. You can connect an **LLM node** to process and summarize the scraped data
  </Step>

  <Step title="Example Workflow">
    <Tip>
      see workflow in banner image
    </Tip>

    **Sample Use Case**: Extract Amazon product information and create a summary

    1. **START** → Input: **Product** URL
    2. **STRUCTURED DATA FEEDS** → Extract product details
    3. **LLM** → Summarize into easy-to-read text
    4. **END** → Output: Clean product summary

    <Note>
      ### Important tips

      * Reference every stage of the workflow to the output of the previous stage
      * Set a high character limit in input fields (for the URL input field choose the "short paragraph" var option)
    </Note>
  </Step>
</Steps>

### Advanced Option: Use Bright Data MCP

While the Bright Data plugin for Dify uses hosted APIs, advanced users can also integrate directly with [**Bright Data MCP (Model Context Protocol)**](https://docs.brightdata.com/ai/mcp-server/overview#configuration) — a local server that exposes Bright Data’s full scraping and automation toolset via HTTP.

You can call MCP tools from Dify using custom HTTP requests or external service nodes to unlock advanced capabilities like browser automation, structured data extraction, and real-time scraping.

* [Explore MCP on GitHub](https://github.com/brightdata/brightdata-mcp/tree/main)
* [Try MCP in the Smithery Playground](https://smithery.ai/server/@luminati-io/brightdata-mcp/tools)
