# Source: https://docs.brightdata.com/datasets/scraper-studio/ai-agent.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Scraper Studio AI Agent

> AI Scraper Studio is a no-code tool that lets you build custom web scrapers using natural language. Simply chat with AI by describing what data you want to collect from a website, and it automatically creates a scraper for you - no coding required.

### Build your first scraper with the AI Agent

In this tutorial, we will use Scraper Studio's AI Agent to create a custom web scraper using natural language - no coding required. By the end, you will have a running scraper that collects structured data from any public website.

> Time to complete: \~10 minutes

<Accordion title="Prerequisites" icon="list-check" iconType="duotone">
  * A Bright Data account ([sign up free](https://brightdata.com/?hs_signup=1\&utm_source=docs))
  * The URL of the website you want to scrape
</Accordion>

<Steps>
  <Step title="Navigate to Scraper Studio page">
    <Frame>
            <img src="https://mintcdn.com/brightdata/0kdpzMb_52Lhtx88/images/datasets/scraper-studio/ai-agent/scraper-studio-location.png?fit=max&auto=format&n=0kdpzMb_52Lhtx88&q=85&s=d058d3141d2bbbaa970c3bf8fd584e3b" alt="Navigate to Scraper Studio page" width="1280" height="522" data-path="images/datasets/scraper-studio/ai-agent/scraper-studio-location.png" />
    </Frame>
  </Step>

  <Step title="Enter the target website URL">
    Paste the URL of the page you want to scrape into the chat input and submit it.

    Along with the URL, you can include additional instructions (optional) to help the AI build a more accurate scraper straight away. The more context you provide, the better the output.

    <Frame>
            <img src="https://mintcdn.com/brightdata/0kdpzMb_52Lhtx88/images/datasets/scraper-studio/ai-agent/add-additional-instructions.png?fit=max&auto=format&n=0kdpzMb_52Lhtx88&q=85&s=0f0ea79cd4ae22d2dfe21a91379507e1" alt="add-additional-instructions.png" width="1280" height="523" data-path="images/datasets/scraper-studio/ai-agent/add-additional-instructions.png" />
    </Frame>

    Useful things to include:

    * **Specific fields** you want to collect (e.g., "I need price, title, and stock status")
    * **Where the data lives** on the page (e.g., "prices are in the product detail panel, not the listing page")
    * **Actions required** to reach the data (e.g., "you need to click 'Show more' to load full descriptions")
    * **CSS selectors**, if you know them (e.g., ".product-price span.amount")
    * **Page load behavior**, if the site is slow or lazy-loads content (e.g., "results load dynamically, give it extra time")

    > ***Expected result**: The AI Agent acknowledges the URL and may ask one or two clarifying questions about what data you want to collect*
  </Step>

  <Step title="Answer the AI's questions">
    Respond in plain language

    > ***Expected result**: The AI Agent generates a schema - a structured list of data fields it will extract, along with their data types. This is the blueprint for your scraper's output.*
  </Step>

  <Step title="Review and Approve Schema">
    Read through the generated schema. If the fields look correct, click <Badge stroke color="blue">Approve</Badge>. If you need changes, click <Badge stroke color="blue">Decline</Badge>, type your feedback in the chat (e.g., "Remove the image field and add a rating field") and the AI will regenerate it.

    > ***Expected result**: Once approved, the AI Agent begins generating the scraper code.*

    <Frame>
            <img src="https://mintcdn.com/brightdata/0kdpzMb_52Lhtx88/images/datasets/scraper-studio/ai-agent/approve-schema.png?fit=max&auto=format&n=0kdpzMb_52Lhtx88&q=85&s=3ea1c0cd014eadd0fd335f26c08a4a68" alt="approve-schema.png" width="1280" height="358" data-path="images/datasets/scraper-studio/ai-agent/approve-schema.png" />
    </Frame>
  </Step>

  <Step title="Wait for code generation">
    The AI writes the full scraper code - including extraction logic, navigation handling, data validation, and error handling. This takes a few minutes.

    > ***Expected result**: A confirmation popup appears indicating your scraper is ready.*

    <Frame>
            <img src="https://mintcdn.com/brightdata/0kdpzMb_52Lhtx88/images/datasets/scraper-studio/ai-agent/collector-created-successfully.png?fit=max&auto=format&n=0kdpzMb_52Lhtx88&q=85&s=e580534c47fce22db159d3ff8e302f7c" alt="collector-created-successfully.png" width="1280" height="552" data-path="images/datasets/scraper-studio/ai-agent/collector-created-successfully.png" />
    </Frame>
  </Step>

  <Step title="Run Your Scraper">
    Click <Badge stroke color="blue">Try it out</Badge> - this redirects you to the Initiate Manually page. Review your collection settings and click <Badge stroke color="blue">Start</Badge> to begin data collection.

    <Frame>
            <img src="https://mintcdn.com/brightdata/0kdpzMb_52Lhtx88/images/datasets/scraper-studio/ai-agent/start-button.png?fit=max&auto=format&n=0kdpzMb_52Lhtx88&q=85&s=cfbee02af6931d9cff634c97cf0dbd25" alt="start-button" width="2635" height="1090" data-path="images/datasets/scraper-studio/ai-agent/start-button.png" />
    </Frame>

    You can also choose an alternative initiation method:

    * **Initiate by API** - trigger the scraper programmatically without entering the control panel
    * **Schedule** - set a recurring run on a daily, weekly, or custom interval

    > ***Expected result**: Your scraper starts collecting data. You can monitor progress from the Runs dashboard and download results in JSON, NDJSON, CSV, or XLSX once the job completes.*
  </Step>
</Steps>

You can use our <Badge color="blue">New</Badge> [Self-Healing Tool](/datasets/functions/self-healing-tool) (*AI Code Refactor*) to make adjustments to the scraper after it's ready, or edit the code in the built-in IDE if needed.

***

## What the AI Agent can build

The AI Agent creates scrapers based on a specific input type and collection goal. It does not scrape an entire domain - providing a homepage URL and asking it to "scrape everything" will not produce useful results.

There are four scraper types the AI Agent can create:

### 1. Product page (PDP) scraper

You provide a list of product page URLs. The scraper visits each URL and extracts product-level data (e.g., title, price, description, images).

> **Use when**: you already have the URLs of the specific pages you want to scrape.

### 2. Discovery scraper

You provide a category page URL or a listing page URL. The scraper collects the available data directly from that listing - such as product titles, prices, and ratings - without visiting individual product pages.

> **Use when**: you need an overview of items from a category or search results page, and individual product page detail is not required.

### 3. Discovery + PDP scraper

You provide a category or listing page URL. The scraper first discovers all product URLs on that page, then visits each product page to collect full product-level detail.

> **Use when**: you need complete product data from an entire category, not just what's visible on the listing page.

### 4. Search scraper

You provide a search keyword. The AI Agent creates either a Discovery or a Discovery + PDP scraper based on your stated requirements - first finding results for that keyword, then collecting data from them.

> **Use when**: you don't have specific URLs and want to collect data based on a search term.
